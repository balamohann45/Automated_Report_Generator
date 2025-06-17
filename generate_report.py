import csv
import os
from fpdf import FPDF
from collections import defaultdict
import matplotlib.pyplot as plt

# Step 0: Create the dataset if not exists
def generate_sample_csv(filename):
    data = [
        ["City", "Violent Crime", "Property Crime", "Drug Offenses"],
        ["New York", 500, 3000, 200],
        ["Los Angeles", 800, 2500, 300],
        ["Chicago", 600, 2000, 250],
        ["Houston", 400, 1500, 150],
        ["Phoenix", 300, 1200, 100]
    ]
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"{filename} created.")

# Step 1: Read and analyze data
def read_and_analyze_data(filename):
    city_crime_data = defaultdict(lambda: defaultdict(int))
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = row['City']
            city_crime_data[city]['Violent Crime'] += int(row['Violent Crime'])
            city_crime_data[city]['Property Crime'] += int(row['Property Crime'])
            city_crime_data[city]['Drug Offenses'] += int(row['Drug Offenses'])
    return city_crime_data

# Step 2: Create PDF Report
class PDFReport(FPDF):
    def header(self):
        self.set_fill_color(0, 102, 204)
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", 'B', 20)
        self.cell(0, 20, "Crime Statistics Across Cities", ln=True, align='C', fill=True)
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 10)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_intro(self):
        self.set_font("Arial", '', 12)
        intro_text = (
            "This report provides an analytical overview of crime data collected from various cities. "
            "The data includes incidents of violent crimes, property crimes, and drug offenses. "
            "The purpose of this report is to highlight crime patterns and support data-driven decisions."
        )
        self.multi_cell(0, 10, intro_text)
        self.ln(5)

    def report_body(self, city_crime_data):
        self.set_font("Arial", 'B', 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, "Crime Data Breakdown by City:", ln=True)
        self.ln(3)
        self.set_font("Arial", '', 12)
        self.set_text_color(0, 0, 0)
        for city, crimes in city_crime_data.items():
            self.set_font("Arial", 'B', 13)
            self.set_text_color(0, 102, 204)
            self.cell(0, 10, f"{city}", ln=True)
            self.set_font("Arial", '', 12)
            self.set_text_color(50, 50, 50)
            for crime_type, count in crimes.items():
                self.cell(0, 8, f"- {crime_type}: {count} incidents", ln=True)
            self.ln(4)

    def add_summary(self, city_crime_data):
        total_violent = sum(crimes['Violent Crime'] for crimes in city_crime_data.values())
        total_property = sum(crimes['Property Crime'] for crimes in city_crime_data.values())
        total_drug = sum(crimes['Drug Offenses'] for crimes in city_crime_data.values())

        self.set_font("Arial", 'B', 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, "Overall Crime Totals:", ln=True)
        self.ln(3)
        self.set_font("Arial", '', 12)
        self.set_text_color(70, 70, 70)
        self.cell(0, 8, f"Total Violent Crimes reported: {total_violent}", ln=True)
        self.cell(0, 8, f"Total Property Crimes reported: {total_property}", ln=True)
        self.cell(0, 8, f"Total Drug Offenses reported: {total_drug}", ln=True)
        self.ln(8)

    def add_disclaimer(self):
        self.set_font("Arial", 'I', 10)
        self.set_text_color(125, 125, 125)
        disclaimer = (
            "Note: Crime data is based on official records and may be subject to reporting delays or "
            "variations depending on the source jurisdiction."
        )
        self.multi_cell(0, 8, disclaimer, align='C')

    def add_graph(self, graph_path):
        self.add_page()
        self.set_font("Arial", 'B', 16)
        self.set_text_color(0, 51, 102)
        self.cell(0, 15, "Visual Representation of Crime Data", ln=True, align='C')
        self.ln(5)

        page_width = self.w - 2 * self.l_margin
        img_width = page_width
        img_height = img_width * 0.6
        current_y = self.get_y()
        self.image(graph_path, x=self.l_margin, y=current_y, w=img_width, h=img_height)
        self.ln(img_height + 10)

def create_pdf(city_crime_data, graph_path, output_filename):
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_intro()
    pdf.report_body(city_crime_data)
    pdf.add_summary(city_crime_data)
    pdf.add_disclaimer()
    pdf.add_graph(graph_path)
    pdf.output(output_filename)

# Step 3: Create a graphical representation
def create_graph(city_crime_data, output_filename):
    cities = list(city_crime_data.keys())
    violent_crimes = [city_crime_data[city]['Violent Crime'] for city in cities]
    property_crimes = [city_crime_data[city]['Property Crime'] for city in cities]
    drug_offenses = [city_crime_data[city]['Drug Offenses'] for city in cities]

    bar_width = 0.25
    x = range(len(cities))

    plt.figure(figsize=(10, 6))
    plt.bar(x, violent_crimes, width=bar_width, label='Violent Crime', color="#e7943c", align='center')
    plt.bar([p + bar_width for p in x], property_crimes, width=bar_width, label='Property Crime', color="#34db5e", align='center')
    plt.bar([p + bar_width * 2 for p in x], drug_offenses, width=bar_width, label='Drug Offenses', color="#6d2ecc", align='center')

    plt.xlabel('Cities')
    plt.ylabel('Number of Incidents')
    plt.title('Crime Statistics by City')
    plt.xticks([p + bar_width for p in x], cities, rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()

# Main execution
if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())

    data_file = 'crime_rates.csv'
    if not os.path.exists(data_file):
        generate_sample_csv(data_file)

    crime_data = read_and_analyze_data(data_file)
    graph_output = 'crime_statistics.png'
    create_graph(crime_data, graph_output)
    pdf_output = 'crime_report.pdf'
    create_pdf(crime_data, graph_output, pdf_output)

    print(f"Report generated: {pdf_output}")
    print(f"Graph generated: {graph_output}")
    
    
 



