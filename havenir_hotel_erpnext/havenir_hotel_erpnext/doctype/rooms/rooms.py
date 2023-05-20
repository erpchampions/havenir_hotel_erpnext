# -*- coding: utf-8 -*-
# Copyright (c) 2020, Havenir and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Rooms(Document):
    def after_insert(self):
        try:
            # Check if an item with the same item_code already exists
            existing_item = frappe.get_value("Item", {"item_code": self.room_number})

            if existing_item:
                frappe.msgprint(f"Item with code {self.room_number} already exists.")
            else:
                item = frappe.new_doc("Item")
                item.item_code = self.room_number
                item.item_group = "Services"
                item.item_name = self.room_name
                item.standard_rate = self.price
                item.is_stock_item = False
                item.include_item_in_manufacturing = False
                item.save()
                
                # Display a success message in the UI.
                frappe.msgprint(f"Item {self.room_name} has been created successfully!")
        except Exception as e:
            # If there's an error, display the error message in the UI.
            frappe.msgprint(f"An error occurred: {str(e)}")