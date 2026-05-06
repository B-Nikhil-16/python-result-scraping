import requests
from bs4 import BeautifulSoup
import pandas as pd

def first_hall_ticket():
    while True:
        h = input("Enter starting hall ticket: ").lower()
        if len(h) == 10 and h[0] == "y" and h[1:].isdigit():
            return h
        print("Invalid hall ticket number")


def last_hall_ticket(first_ht):
    while True:
        h = input("Enter last hall ticket: ").lower()
        if (
            len(h) == 10
            and h[0] == "y"
            and h[1:].isdigit()
            and int(h[1:]) >= int(first_ht[1:])
        ):
            return h
        print("Invalid last hall ticket number")


def list_of_hall_tickets_range(first_ht, last_ht):
    start = int(first_ht[1:])
    end = int(last_ht[1:])
    width = len(first_ht) - 1
    return ["y" + str(i).zfill(width) for i in range(start, end + 1)]


def ranked(excel_name):
    df = pd.read_excel(excel_name)

    subject_cols = df.columns[2:]
    df[subject_cols] = (
        df[subject_cols]
        .replace("--", 0)
        .apply(pd.to_numeric, errors="coerce")
    )

    df["Total"] = df[subject_cols].sum(axis=1)
    df["Rank"] = df["Total"].rank(ascending=False, method="min").astype(int)

    df.sort_values("Rank").to_excel(
        "rank_wise_" + excel_name, index=False
    )
    print("Ranked excel sheet created successfully")


def main():
    first_ht = first_hall_ticket()
    last_ht = last_hall_ticket(first_ht)

    website_url = input("Enter results page URL: ")
    rsurl = website_url[website_url.find("UG"):]

    hall_tickets = list_of_hall_tickets_range(first_ht, last_ht)
    all_data = []

    ajax_url = "https://upiqpbank.com/kvrrms/home/getresults"

    for ht in hall_tickets:
        

        payload = {"hno": ht, "rsurl": rsurl}

        try:
            r = requests.post(ajax_url, data=payload, timeout=10)
            soup = BeautifulSoup(r.text, "lxml")

            roll_tag = soup.find("th", string=lambda x: x and "Roll No" in x)
            name_tag = soup.find("th", string=lambda x: x and "Student Name" in x)
            marks_title = soup.find("h5", string=lambda x: x and "Marks Details" in x)

            if not roll_tag or not name_tag or not marks_title:
                print(f"No data for {ht}")
                continue

            data = {
                "Hall Ticket": roll_tag.find_next("td").text.strip(),
                "Student Name": name_tag.find_next("td").text.strip(),
            }

            rows = (
                marks_title.find_next("table")
                .find("tbody")
                .find_all("tr")
            )

            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 5:
                    continue

                sub_code = cols[0].text.strip()
                sub_name = cols[1].text.strip()
                key = f"{sub_code} - {sub_name}"

                data[f"{key} (external)"] = cols[2].text.strip()
                data[f"{key} (internal)"] = cols[4].text.strip()

            all_data.append(data)
            print(f"Data collected for {ht}")

        except Exception as e:
            print(f"Error for {ht}: {e}")

    if not all_data:
        print("No valid data collected")
        return

    df = pd.DataFrame(all_data)
    name = input("Enter excel file name: ") + ".xlsx"
    df.to_excel(name, index=False)

    if input("Generate rank sheet? (yes/no): ").lower() == "yes":
        ranked(name)


if __name__ == "__main__":
    main()
