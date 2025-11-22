from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Task 2 Sample PDF Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10, "This is a sample PDF generated for Task 2. You can add more data and formatting here.")
pdf.output("report.pdf")

print("Task 2 PDF created successfully!")
