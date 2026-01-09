import frappe

@frappe.whitelist()
def search_products(query):
    if not query:
        return []

    return frappe.db.sql("""
        SELECT
            wi.item_name,
            wi.route,
            wi.website_image AS image,
            (
                SELECT ip.price_list_rate
                FROM `tabItem Price` ip
                WHERE ip.item_code = wi.item_code
                LIMIT 1
            ) AS price
        FROM `tabWebsite Item` wi
        WHERE
            wi.published = 1
            AND wi.item_name LIKE %(query)s
        LIMIT 8
    """, {
        "query": f"%{query}%"
    }, as_dict=True)
