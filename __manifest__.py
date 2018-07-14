# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-TODAY Linserv Aktiebolag, Sweden (<http://www.linserv.se>).
#
##############################################################################
{
    "name": "Purchase SO Link",
    "version": "1.0",
    "author": "Linserv AB",
    "category": "Purchase",
    "summary": "Purchase SO Link",
    "website": "www.linserv.se",
    "contributors": [
        'Gediminas Venclova <gediminasv@live.com>'
    ],
    "license": "",
    "depends": ['base', 'sale_order_extra_fields'],
    'description': """

        Purchase SO Link - module adds two field (Customer Reference, Customer PO No.) in purchase order and fills
        its values from sales order, if correct route is set for a product. 
        
    """,
    "demo": [],
    "data": [
        'views/inhetired_purchase.xml',
    ],
    "test": [],
    "js": [],
    "css": [],
    "qweb": [],
    "installable": True,
    "auto_install": False,
}