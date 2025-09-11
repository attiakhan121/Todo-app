
    # apps/todo/todo/api/todo.py
import frappe

@frappe.whitelist(allow_guest=True)
def get_todo_list():
    list = frappe.get_all("ToDo", fields=["name", "description", "status"])
    
    return list