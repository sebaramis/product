##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models, api


class ProductProduct(models.Model):

    _inherit = 'product.product'

    internal_code = fields.Char(
        'Internal Code', copy=False)

    # we move this to search improoved, if we want to keep we should fix
    # duplicated searchs
    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     res = []
    #     if name:
    #         recs = self.search([('internal_code', operator, name)] + args,
    #                            limit=limit)
    #         res = recs.name_get()
    #     res += super(Product, self).name_search(
    #         name=name, args=args, operator=operator, limit=limit)
    #     return res

    @api.model
    def create(self, vals):
        if (not vals.get('internal_code', False) and not self.
                _context.get('default_internal_code', False)):
            vals['internal_code'] = self.env[
                'ir.sequence'].next_by_code('product.internal.code') or '/'
        return super(ProductProduct, self).create(vals)

    _sql_constraints = {
        ('internal_code_uniq', 'unique(internal_code)',
            'Internal Code mast be unique!')
    }
