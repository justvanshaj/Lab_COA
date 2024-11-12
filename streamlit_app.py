import streamlit as st
from fpdf import FPDF
from datetime import datetime

# Function to create PDF with top gap and alignment for "Kindly Att." and Date
def create_pdf(date, salutation1, full_name, designation, company_name, city_state, salutation2, guar_type_1, guar_weight_1, guar_type_2, guar_weight_2):
    pdf = FPDF()
    pdf.add_page()

    # Setting font
    pdf.set_font("Arial", size=10)

    # Adding top gap
    pdf.ln(50)  # Adjust the value as needed to match your desired gap

    # Adding "Kindly Att." on the left and Date on the right on the same line
    pdf.cell(0, 10, txt="Kindly Att.", ln=False, align='L')
    pdf.cell(0, 10, txt=f"Date-{date}", ln=True, align='R')
    
    # Adding the rest of the content
    pdf.ln(10)  # Line break after the first line
    
    # Bold Full Name and City State
    pdf.set_font("Arial", style='B', size=10)
    pdf.cell(200, 10, txt=f"{salutation1} {full_name},", ln=True)
    pdf.cell(200, 10, txt=designation, ln=True)
    pdf.cell(200, 10, txt=company_name + ",", ln=True)
    pdf.cell(200, 10, txt=city_state, ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Dear {salutation2},", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt="As per your requirement we are sending you sample of -", ln=True)
    pdf.ln(5)
    
    pdf.cell(200, 10, txt=f"A) Guar {guar_type_1} - {guar_weight_1}KG.", ln=True)
    pdf.cell(200, 10, txt=f"B) Guar {guar_type_2} - {guar_weight_2}KG.", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Kindly acknowledge me receipt of the same.", ln=True)
    pdf.ln(10)
    
    # Bold Authorized Signatory and Company Name
    pdf.set_font("Arial", style='B', size=10)
    pdf.cell(200, 10, txt="Yours Faithfully,", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Authorised Signatory", ln=True)
    pdf.cell(200, 10, txt="Aravally Processed Agrotech Pvt Ltd", ln=True)
    
    # Saving the PDF
    pdf_output = "generated_letter.pdf"
    pdf.output(pdf_output)
    return pdf_output

# Streamlit App
st.title("Generate a Custom PDF Letter")

# Form to collect data
with st.form("pdf_form"):
    date = st.date_input("Date", value=datetime.today())
    salutation1 = st.selectbox("Salutation1", ["Sir", "Ma’am", "Mr.", "Mrs."])  # Added Mr./Mrs. options
    full_name = st.text_input("Full Name")
    designation = st.text_input("Designation")
    company_name = st.text_input("Company Name")
 
