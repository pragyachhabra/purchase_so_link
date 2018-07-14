# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseSoLinkSaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        return super(PurchaseSoLinkSaleOrder, self.with_context(client_order_ref=self.client_order_ref, customer_po_nr=self.customer_po_nr)).action_confirm()
