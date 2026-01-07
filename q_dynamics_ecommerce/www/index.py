import frappe

def get_context(context):

    # Category Section
    context.item_groups = frappe.get_all(
        "Item Group",
        filters={
            "is_group": 0,
            "show_in_website": 1
        },
        fields=["name", "route", "image"],
        order_by="name asc"
    )

    # Promotion Videos Section ✅
    context.promotion_videos = frappe.get_all(
        "Promotion Videos",
        filters={"is_active": 1},
        fields=[
            "name",
            "name1",
            "upload_videos",
            "order_sequence"
        ],
        order_by="order_sequence asc"
    )

    # Hero Banner Section ✅
    context.hero_banners = frappe.get_all(
        "Hero Banner Image",
        filters={
            "is_active": 1
        },
        fields=[
            "name",
            "name1",
            "link",
            "order_sequence",
            "attach_image"
        ],
        order_by="order_sequence asc"
    )
