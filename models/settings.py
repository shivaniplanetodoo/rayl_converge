from odoo import models, fields, api, _


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    def redirect_to_portal_invoice(self):
        return {'type': 'ir.actions.act_url',
                'url': r'/my/invoices/{}'.format(self.id),
                'target': 'self',
                }
