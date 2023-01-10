# Copyright (c) 2023, D-codE and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

import xlrd


class SmartSearch(Document):
	
	@frappe.whitelist()	
	def read_excel(self):
		file_doc = frappe.get_doc("File", {"file_url": self.excel_file})
		content = file_doc.get_content()

		book = xlrd.open_workbook(file_contents=content)
		# book = xlrd.open_workbook(fcontent=content)
		sheets = book.sheets()
		sheet = sheets[0]
		rows = []
		for i in range(sheet.nrows):
			rows.append(sheet.row_values(i))
		return rows