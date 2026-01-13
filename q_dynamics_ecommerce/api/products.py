import frappe

@frappe.whitelist(allow_guest=True)
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
        p["route"] = f"/{p['route']}" if p.get("route") else "#"
        p["image"] = p.get("image") or "/assets/frappe/images/no-image.png"

    return products

@frappe.whitelist(allow_guest=True)
def get_product_tags():
    return frappe.db.sql("""
        SELECT DISTINCT tag
        FROM `tabTag Link`
        WHERE document_type = 'Item'
        ORDER BY tag
    """, as_dict=True)
