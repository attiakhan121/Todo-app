# apps/todo/todo/api/todo.py
import frappe

@frappe.whitelist(allow_guest=True)
def get_todo_list():

    todos = frappe.get_all(
        "Todo item",   # Doctype ka exact name use karo (case sensitive)
        fields=[
            "name",        # Frappe ka internal ID
            "title",       # Title field
            "description", # Small Text field
            "status",      # Select field
            "due_date",    # Date field
            "id",          # Data field
            "text",        # Small Text field
            "done",        # Checkbox field
            "owner",       # System field (kis user ne create kiya)
            "creation",    # System field (kab create hua)
            "modified"     # System field (last update)
        ]
    )
    return todos
