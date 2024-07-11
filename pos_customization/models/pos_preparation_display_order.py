from odoo import models, fields


class PosPreparationDisplayOrder(models.Model):
    _inherit = 'pos_preparation_display.order'

    pos_is_take_away = fields.Boolean(default=False, string="Is a Takeaway Order",
                                 help="Is a Takeaway Order")

    def _export_for_ui(self, preparation_display):
        order_for_ui = super()._export_for_ui(preparation_display)

        if order_for_ui:
            order_for_ui['is_take_away'] = self.pos_order_id.is_takeaway
        return order_for_ui

