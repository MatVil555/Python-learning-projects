import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import seaborn as sns

filepath_list = glob.glob("inv/*.xlsx")

for filepath in filepath_list:


    pdf = FPDF(orientation="P", unit="mm", format ="A4")
    pdf.add_page()
    filename=Path(filepath).stem
    invoice_nr=filename.split("-")
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice_nr_{invoice_nr[0]}", ln=1)

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=50, h=8, txt=f"Date:{invoice_nr[1]}", ln=1)

    df=pd.read_excel(filepath, sheet_name="Sheet 1")

    #add columns name
    columns=list(df.columns)
    columns=[item.replace("_"," ").title() for item in columns]
    pdf.set_font(family="Times", size=8, style="B")
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=30, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    aux_price=0
    for index, row in df.iterrows():
        #add rows to the table name
      pdf.set_font(family="Times", size=8)
      pdf.set_text_color(80,80,80)
      pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
      pdf.cell(w=30, h=8, txt=str(row["product_name"]), border=1)
      pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
      pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
      pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)
      aux_price=aux_price+row["total_price"]

    sum_of_price=aux_price
    pdf.set_font(family="Times", size=8)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(sum_of_price), border=1, ln=1)

    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=12, txt=f"The total to pay is {sum_of_price} danari", ln=1)
    pdf.set_text_color(80,80,80)

    pdf.output(f"PDFs/{filename}.pdf")






