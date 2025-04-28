import mysql.connector
from fpdf import FPDF

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="Durga_chandu"
)

# Fetch data from MySQL
mycursor = mydb.cursor()
mycursor.execute("SELECT rollno, name, state, phone_number FROM students")
data = mycursor.fetchall()

# Close the connection
mycursor.close()
mydb.close()

# PDF creation with fpdf (for simplicity)
pdf = FPDF()
pdf.add_page()

# Set font for title
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, txt="Student Data Report", ln=True, align="C")
pdf.ln(10)

# Set font for table header
pdf.set_font("Arial", "B", 12)

# Print headings (like a table header)
pdf.cell(40, 10, "Roll No", border=0, align='L')
pdf.cell(80, 10, "Name", border=0, align='L')
pdf.cell(40, 10, "State", border=0, align='L')
pdf.cell(50, 10, "Phone Number", border=0, align='L')
pdf.ln(10)

# Set font for table data
pdf.set_font("Arial", "", 12)

# Loop through data and print it in a table-like format
for row in data:
    pdf.cell(40, 10, str(row[0]), border=0, align='L')   # Roll No
    pdf.cell(80, 10, row[1], border=0, align='L')         # Name
    pdf.cell(40, 10, row[2], border=0, align='L')         # State
    pdf.cell(50, 10, row[3], border=0, align='L')         # Phone Number
    pdf.ln(10)

# Save the PDF to a file
pdf.output("student_data_report.pdf")

print("PDF generated successfully!")
