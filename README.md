# Automated_Report_Generator

COMPANY : CODTECH IT SOLUTIONS

NAME : TELLAGORLA BALAMOHAN

INTERN ID : CT6WTDG727

DOMAIN : PYTHON PROGRAMMING

DURATION : 6 WEEKS

MENTOR : NEELA SANTOSH

# OVERVIEW OF PROJECT
Automated Report Generation is a Python-based project that reads structured data (e.g., from a .csv file), performs basic analysis (like statistical summaries), and produces a formatted PDF report automatically. This automation is particularly useful for generating regular business reports, academic summaries, or dashboard exports without manual effort.

The project uses:

1.pandas for data manipulation and analysis

2.FPDF (or optionally ReportLab) for PDF report creation

# Features used
1.📂 Reads data from a CSV file

2.📊 Generates descriptive statistics (mean, count, std, etc.)

3.🖨️ Creates a clean, formatted PDF report

4.🔁 Fully automated: runs in a single command

5.🧩 Modular structure for easy customization

# Technologies used
Tool	  ------          Purpose

Python	 -----     Programming Language

pandas	 -------  Data analysis and manipulation

FPDF     ----------	Lightweight PDF generation


# 📥 How to Run
1. Clone the repository:

    git clone https://github.com/yourusername/automated-report-generation.git
    cd automated-report-generation

2.Install dependencies:

    pip install -r requirements.txt

3. Add your .csv data to the data/ folder.
  
4. Run the script:

    python generate_report.py

5. View the report:
     Open the generated reports/report.pdf

# ⚙️ How It Works

Step	  -------------------------------------------------- Description

🗂️ 1. Load Data	-----------------------    The script reads input from a CSV file (e.g., data/sample_data.csv).

📊 2. Analyze	--------------------------   It uses pandas to compute summaries like count, mean, std, min, max.

🖨️ 3. Generate Report	-------------------  The analyzed data is formatted and written into a PDF using fpdf.

📁 4. Output	---------------------------- The final PDF report is saved in the reports/ folder.


# ✅ Why Use Automated Report Generation?
Benefit	--------------------------------------------------Description

⏱️ Saves Time	----------------------------Eliminates repetitive manual analysis and formatting

📑 Consistency----------------------	    Generates standardized reports every time

🔁 Automation	------------------------    Can be integrated with schedulers like cron or CI/CD pipelines

📈 Business --------------------------   Insight	Useful for teams needing regular updates from data sources

🧩 Extensible	--------------------------- Easily modified to include charts, tables, or advanced analysis


