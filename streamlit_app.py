import streamlit as st
from fpdf import FPDF
from datetime import datetime

# Function to create PDF
def create_pdf(date, full_name, designation, company_name, city_state, sir_maam, guar_type_1, guar_weight_1, guar_type_2, guar_weight_2):
    pdf = FPDF()
    pdf.add_page()

    # Setting font
    pdf.set_font("Arial", size=12)

    # Adding the content
    pdf.cell(200, 10, txt="Kindly Att.", ln=True, align='R')
    pdf.cell(200, 10, txt=f"Date-{date}", ln=True, align='R')
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"{sir_maam} {full_name},", ln=True)
    pdf.cell(200, 10, txt=designation, ln=True)
    pdf.cell(200, 10, txt=company_name + ",", ln=True)
    pdf.cell(200, 10, txt=city_state, ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"Dear {sir_maam},", ln=True)
    pdf.ln(10)
    pdf.cell(200, 10, txt="As per your requirement we are sending you sample of -", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt=f"A) Guar {guar_type_1} – {guar_weight_1}KG.", ln=True)
    pdf.cell(200, 10, txt=f"B) Guar {guar_type_2} – {guar_weight_2}KG.", ln=True)
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Kindly acknowledge me receipt of the same.", ln=True)
    pdf.ln(20)
    
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
    full_name = st.text_input("Full Name")
    designation = st.text_input("Designation")
    company_name = st.text_input("Company Name")
    city_state = st.text_input("City, State")
    sir_maam = st.selectbox("Salutation", ["Mr.", "Mrs.", "Miss", "Sir/Ma’am"])
    guar_type_1 = st.selectbox("Guar Type A", ["Churi", "Korma"])
    guar_weight_1 = st.number_input("Guar Weight A (KG)", min_value=0)
    guar_type_2 = st.selectbox("Guar Type B", ["Churi", "Korma"])
    guar_weight_2 = st.number_input("Guar Weight B (KG)", min_value=0)
    
    # Submit button
    submitted = st.form_submit_button("Generate PDF")

if submitted:
    # Convert date to string format
    date_str = date.strftime("%d/%m/%Y")
    
    # Create PDF
    pdf_path = create_pdf(date_str, full_name, designation, company_name, city_state, sir_maam, guar_type_1, guar_weight_1, guar_type_2, guar_weight_2)
    
    # Display the link to download the PDF
    with open(pdf_path, "rb") as f:
        st.download_button("Download PDF", f, file_name="generated_letter.pdf")
