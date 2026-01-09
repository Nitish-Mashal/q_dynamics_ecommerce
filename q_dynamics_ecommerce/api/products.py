import frappe

@frappe.whitelist()
def get_products_by_tag(tag):
    products = frappe.db.sql("""
        SELECT
            i.name,
            i.item_name,
            i.image,
            i.standard_rate,
            wi.route
        FROM `tabItem` i
        INNER JOIN `tabTag Link` tl
            ON tl.document_name = i.name
        LEFT JOIN `tabWebsite Item` wi
            ON wi.item_code = i.name
        WHERE
            tl.tag = %s
            AND i.disabled = 0
            AND wi.published = 1
        ORDER BY i.modified DESC
        LIMIT 12
    """, tag, as_dict=True)

    for p in products:
        # prepend slash for frontend
        if p.get("route"):
            p["route"] = f"/{p['route']}"
        else:
            p["route"] = "#"

        if not p.get("image"):
            p["image"] = "/assets/frappe/images/no-image.png"

    return products
