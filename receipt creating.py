from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def create_payment_receipt(customer_name, amount_paid, payment_date):
    pdf_filename = "payment_receipt.pdf"
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)

    content =   [[ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
    [  "16/11/2020", "TATA RELIANCE", "Lifetime", "10,999.00/-"], 
    [ "16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"], 
    [ "Sub Total", "", "", "20,9998.00/-"], 
    [ "Discount", "", "", "-3,000.00/-"], 
    [ "Total", "", "", "17,998.00/-"],] 


    table = Table(content, colWidths=[150, 150])
    table.setStyle(TableStyle([( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige )])) 
    document.build([table])

    print(f"Payment receipt saved as {pdf_filename}")

create_payment_receipt("John Doe", 500.00, "2024-02-01")
