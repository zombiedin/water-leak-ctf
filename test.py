import os
import yaml
import unittest
import requests
import re
import PyPDF3
import urllib.request


class WaterLeak(unittest.TestCase):
    with open(os.path.join(os.path.dirname(__file__), "flag"), "r") as f:
        SNYK_FLAG = yaml.safe_load(f)

    def test_flag_is_valid(self):

        # URL of PDF to read
        pdf_url = "https://ctf-web-content.s3.ap-southeast-2.amazonaws.com/Secret.pdf"
        tmp_file = "/tmp/tmp.pdf"
        # Download PDF from URL
        urllib.request.urlretrieve(pdf_url, tmp_file)

        # Open PDF file
        with open(tmp_file, "rb") as pdf_file:
            # Create PDF reader object
            pdf_reader = PyPDF3.PdfFileReader(pdf_file)

            # Loop through all pages
            for page_num in range(pdf_reader.numPages):
                # Get page object
                page = pdf_reader.getPage(page_num)

                # Extract text from page
                text = page.extractText()

            self.assertIn(self.SNYK_FLAG,text)


if __name__ == "__main__":
    unittest.main()