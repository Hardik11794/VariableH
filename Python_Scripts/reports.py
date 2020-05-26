#!/usr/bin/env python3

from datetime import date
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(str(title +" "+ date.today().strftime("%B %d, %Y")) , styles["h1"])
  report_info = Paragraph(additional_info, styles["Normal"])

  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])


generate_report("/mnt/c/Users/hardi/OneDrive/Desktop/mynewdir/processed.pdf","Processed Update on","<br/><br/> Training")
