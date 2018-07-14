# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseSoLinkPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    client_order_ref = fields.Char(string='Customer Reference', copy=False)
    customer_po_nr = fields.Char(string='Customer PO No.')

    @api.model
    def create(self, vals):
        # adding values from context, only if there is no old values
        res = super(PurchaseSoLinkPurchaseOrder, self).create(vals)
        if 'client_order_ref' in self._context and not res.client_order_ref:
            res.client_order_ref = self._context['client_order_ref']
        if 'customer_po_nr' in self._context and not res.customer_po_nr:
            res.customer_po_nr = self._context['customer_po_nr']
        return res
