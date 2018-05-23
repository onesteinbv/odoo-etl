# -*- coding: utf-8 -*-
from openerp import models, fields, api, SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)


class multi_tgt_db(models.Model):
    """
    """

    _name = 'etl.multi_tgt_db'
    _description = 'multi_tgt_db'

    manager_id = fields.Many2one(
        'etl.manager', string='Manager', required=True, ondelete='cascade'
    )
    src_field = fields.Char(string='Source Reference Field', required=True)
    target_database = fields.Char(string='Target Database', required=True)
    target_hostname = fields.Char(string='Target Hostname', required=True)
    target_login = fields.Char(string='Target Login', required=True)
    target_password = fields.Char(string='Target Password', required=True)
    target_port = fields.Integer(string='Target Port', required=True)
