from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.conf import settings
import os
from datetime import datetime
from reportlab.lib.utils import ImageReader


def generate_receipt(student):

    receipt_folder = os.path.join(
        settings.MEDIA_ROOT,
        "receipts"
    )

    os.makedirs(
        receipt_folder,
        exist_ok=True
    )

    filename = f"FBL_{student.id}.pdf"

    filepath = os.path.join(
        receipt_folder,
        filename
    )

    pdf = canvas.Canvas(filepath)

    width = 595
    height = 842

    

    # Outer Border
    pdf.setLineWidth(2)
    pdf.rect(20, 20, width - 40, height - 40)

    # Header
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(
        width / 2,
        800,
        "FRONT BENCHERS LIBRARY"
    )

    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(
        width / 2,
        780,
        "Membership Registration Receipt"
    )

    # Divider
    pdf.line(40, 765, width - 40, 765)

    # Receipt Info
    receipt_no = f"FBL-{student.id:04d}"

    pdf.setFont("Helvetica-Bold", 11)

    pdf.drawString(
        40,
        735,
        f"Receipt No : {receipt_no}"
    )

    pdf.drawRightString(
        width - 40,
        735,
        f"Date : {datetime.now().strftime('%d-%m-%Y')}"
    )

    # Section Title
    pdf.setFont(
        "Helvetica-Bold",
        14
    )

    pdf.drawString(
        40,
        690,
        "Student Information"
    )

    pdf.line(
        40,
        685,
        width - 40,
        685
    )

    # Student Data
    pdf.setFont(
        "Helvetica",
        12
    )

    y = 650

    details = [
        ("Student Name", student.name),
        ("Aadhaar Number", student.aadhaar_card),
        ("Father Name", student.father_name),
        ("WhatsApp Number", student.whatsapp),
        ("Joining Date", str(student.joining_date)),
        ("Monthly Fee", f"₹ {student.fee_amount}"),
        ("Fee Status", student.fee_status),
        ("Renewal Date", str(student.fee_due_date)),
    ]

    for label, value in details:

        pdf.drawString(
            50,
            y,
            label
        )

        pdf.drawString(
            180,
            y,
            ":"
        )

        pdf.drawString(
            200,
            y,
            str(value)
        )

        y -= 35

    # Note Section
    pdf.setFont(
        "Helvetica-Bold",
        13
    )

    pdf.drawString(
        40,
        330,
        "Important Note"
    )

    pdf.line(
        40,
        325,
        width - 40,
        325
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        295,
        "Please keep this receipt for future reference."
    )

    pdf.drawString(
        50,
        275,
        "Membership should be renewed before the due date."
    )

    pdf.drawString(
        50,
        255,
        "Late renewal may affect uninterrupted library access."
    )

    # Signature Area

    image_path = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "sign2.jpeg"
)

    pdf.drawImage(
        image_path,
        width - 195,
        170,
        width=130,
        height=90,
        mask='auto'
)

    pdf.line(
        width - 200,
        170,
        width - 60,
        170
    )

    pdf.setFont(
        "Helvetica",
        10
    )

    pdf.drawString(
        width - 175,
        150,
        "Authorized Signature"
    )

    # Footer
    pdf.line(
        40,
        120,
        width - 40,
        120
    )

    pdf.setFont(
        "Helvetica-Bold",
        11
    )

    pdf.drawCentredString(
        width / 2,
        95,
        "Thank You For Choosing Front Benchers Library"
    )

    pdf.setFont(
        "Helvetica",
        10
    )

    pdf.drawCentredString(
        width / 2,
        75,
        "Learn • Focus • Achieve"
    )

    pdf.save()

    return f"/media/receipts/{filename}"

def generate_payment_receipt(payment):

    receipt_folder = os.path.join(
        settings.MEDIA_ROOT,
        "payment_receipts"
    )

    os.makedirs(
        receipt_folder,
        exist_ok=True
    )

    filename = f"PAY_{payment.id}.pdf"

    filepath = os.path.join(
        receipt_folder,
        filename
    )

    pdf = canvas.Canvas(filepath)

    width = 595
    height = 842

    pdf.setLineWidth(2)
    pdf.rect(20, 20, width - 40, height - 40)

    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(
        width / 2,
        800,
        "FRONT BENCHERS LIBRARY"
    )

    pdf.setFont("Helvetica", 11)
    pdf.drawCentredString(
        width / 2,
        780,
        "Monthly Fee Receipt"
    )

    pdf.line(40, 765, width - 40, 765)

    receipt_no = f"PAY-{payment.id:04d}"

    pdf.setFont("Helvetica-Bold", 11)

    pdf.drawString(
        40,
        735,
        f"Receipt No : {receipt_no}"
    )

    pdf.drawRightString(
        width - 40,
        735,
        f"Date : {datetime.now().strftime('%d-%m-%Y')}"
    )

    pdf.setFont("Helvetica-Bold", 14)

    pdf.drawString(
        40,
        690,
        "Payment Information"
    )

    pdf.line(
        40,
        685,
        width - 40,
        685
    )

    pdf.setFont(
        "Helvetica",
        12
    )

    y = 650

    details = [
        ("Student Name", payment.student.name),
        ("WhatsApp Number", payment.student.whatsapp),
        ("Amount Paid", f"₹ {payment.amount}"),
        ("Payment Date", str(payment.payment_date)),
        ("Fee Status", "Paid"),
    ]

    for label, value in details:

        pdf.drawString(50, y, label)
        pdf.drawString(180, y, ":")
        pdf.drawString(200, y, str(value))

        y -= 35

    pdf.setFont("Helvetica-Bold", 13)

    pdf.drawString(
        40,
        330,
        "Important Note"
    )

    pdf.line(
        40,
        325,
        width - 40,
        325
    )

    pdf.setFont(
        "Helvetica",
        11
    )

    pdf.drawString(
        50,
        295,
        "Please keep this receipt for future reference."
    )

    image_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "sign2.jpeg"
    )

    pdf.drawImage(
        image_path,
        width - 195,
        170,
        width=130,
        height=90,
        mask='auto'
    )

    pdf.line(
        width - 200,
        170,
        width - 60,
        170
    )

    pdf.drawString(
        width - 175,
        150,
        "Authorized Signature"
    )

    pdf.line(
        40,
        120,
        width - 40,
        120
    )

    pdf.drawCentredString(
        width / 2,
        95,
        "Thank You For Choosing Front Benchers Library"
    )

    pdf.drawCentredString(
        width / 2,
        75,
        "Learn • Focus • Achieve"
    )

    pdf.save()

    return f"/media/payment_receipts/{filename}"