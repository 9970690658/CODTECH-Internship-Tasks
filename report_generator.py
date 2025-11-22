# Import libraries
import csv
from fpdf import FPDF

# Read CSV data
def read_data(file_path):
    """Reads CSV file and returns list of rows"""
    data = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

# Generate PDF report
def generate_pdf(data, output_file):
    """Creates PDF report from CSV data"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Employee Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(50, 10, "Name", 1)
    pdf.cell(30, 10, "Age", 1)
    pdf.cell(40, 10, "Salary", 1)
    pdf.ln()

    pdf.set_font("Arial", "", 12)
    for row in data[1:]:  # skip header
        pdf.cell(50, 10, row[0], 1)
        pdf.cell(30, 10, row[1], 1)
        pdf.cell(40, 10, row[2], 1)
        pdf.ln()

    pdf.output(output_file)

if __name__ == "__main__":
    data = read_data("data.csv")
    generate_pdf(data, "report.pdf")
    print("PDF report generated successfully!")
