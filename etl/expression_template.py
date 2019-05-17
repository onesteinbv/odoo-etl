from openerp import models, fields, api, _


class ExpressionTemplate(models.Model):
    _name = 'etl.expression_template'

    name = fields.Char()
    expr = fields.Text()

