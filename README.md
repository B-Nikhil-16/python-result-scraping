# Student Results Scraper and Rank Generator

A Python-based web scraping project that collects student result data from an online results portal and exports it to an Excel sheet. The project can also generate a rank-wise Excel sheet based on total marks.

## Features

- Scrape student result data using hall ticket numbers
- Supports hall ticket ranges
- Extracts:
  - Student Name
  - Hall Ticket Number
  - Subject-wise External Marks
  - Subject-wise Internal Marks
- Exports data to Excel format
- Generates rank-wise result sheets
- Handles invalid or missing data gracefully

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas
- OpenPyXL
- LXML

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/student-results-scraper.git
```

Move into the project directory:

```bash
cd student-results-scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

The project uses the following Python libraries:

```text
requests
beautifulsoup4
pandas
openpyxl
lxml
```

## Usage

Run the script:

```bash
python main.py
```

The program will ask for:

1. Starting hall ticket number
2. Ending hall ticket number
3. Results page URL
4. Excel file name

Optional:
- Generate rank sheet based on total marks

## Example

```text
Enter starting hall ticket: y230000001
Enter last hall ticket: y230000010
Enter results page URL: https://example.com/results
Enter excel file name: results_sheet
Generate rank sheet? (yes/no): yes
```

## Output

The project generates:

- `results_sheet.xlsx`
- `rank_wise_results_sheet.xlsx`

## Project Structure

```text
student-results-scraper/
│
├── main.py
├── requirements.txt
└── README.md
```

## How Ranking Works

- Missing marks (`--`) are treated as `0`
- Total marks are calculated automatically
- Students are ranked in descending order based on total marks

## Disclaimer

This project is intended for educational and personal use only. Ensure you have permission to scrape and use data from the target website.

## Author

Your Name
