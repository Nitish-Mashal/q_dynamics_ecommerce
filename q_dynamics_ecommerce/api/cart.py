import frappe

@frappe.whitelist()
def get_cart_count():
    """Return total qty of items in current user's cart"""
    from webshop.webshop.shopping_cart.cart import _get_cart_quotation, get_party

    party = get_party()
    quotation = _get_cart_quotation(party)

    if quotation and quotation.get("items"):
        return sum([item.qty for item in quotation.items])
    return 0

@frappe.whitelist()
def get_wishlist_count():
    """Return total wishlist items for logged-in user"""
    try:
        wishlist_items = frappe.get_all(
            "Wishlist Item", filters={"owner": frappe.session.user}
        )
        return len(wishlist_items)
    except Exception:
        return 0
import frappe

@frappe.whitelist()
def get_cart_count():
    """Return total qty of items in current user's cart"""
    from webshop.webshop.shopping_cart.cart import _get_cart_quotation, get_party

    party = get_party()
    quotation = _get_cart_quotation(party)

    if quotation and quotation.get("items"):
        return sum([item.qty for item in quotation.items])
    return 0

@frappe.whitelist()
def get_wishlist_count():
    """Return total wishlist items for logged-in user"""
    try:
        wishlist_items = frappe.get_all(
            "Wishlist Item", filters={"owner": frappe.session.user}
        )
        return len(wishlist_items)
    except Exception:
        return 0
