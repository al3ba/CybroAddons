# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import fields, models


class Users(models.Model):
    """Inhering 'res.users' for adding new fields"""
    _inherit = 'res.users'

    is_refresh = fields.Boolean(string='Tree,Kanban Refresh mode Enabled',
                                help="Refreshing feature for specific users",
                                default=False)
    chatbox_position = fields.Char(string="ChatBox position",
                                   help="different layouts for chatBox")
    animation_plus = fields.Char(stirng="Animation",
                                 help="Different Animations", defult='Default')
