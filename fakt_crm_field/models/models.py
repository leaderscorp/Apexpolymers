# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class exhibitorGroupName(models.Model):
#     _name = 'exhibitor.group.name'
#     _description = 'Exhibitor group Name'
#
#     name = fields.Char()
#     exhibitor_group = fields.Many2one("crm.lead", string="Exhibitor Group Name")

class exhibitorGroupName(models.Model):
    _name = 'exhibitor.group.name'
    name = fields.Char('Exhibitor Group Name')
    # exhibitor_group = fields.Many2one("crm.lead", string="Exhibitor Group Name")


class industryName(models.Model):
    _name = 'industry.name'
    name = fields.Char('Exhibitor Group Name')

class industryName(models.Model):
    _name = 'sector.name'
    name = fields.Char('Sector')

class fakt_crm_field(models.Model):
    _inherit = 'crm.lead'

    secondary_email = fields.Char(string="Secondary Email")
    secondary_mobile = fields.Char(string="Secondary Mobile")
    exhibitor_contact_status = fields.Selection([('Local', 'Local'), ('International', 'International')])
    fax = fields.Char(string="Fax")

    # exhibitor_group_name = fields.One2many('exhibitor.group.name', 'exhibitor_group')

    # exhibitor_group_name = fields.Many2one("crm.lead", string="Exhibitor Group Name")
    # industry_name = fields.Many2one("crm.lead", string="Industry")
    # selector = fields.Many2one("crm.lead", string="Sector")


    exhibitor_group_name = fields.Many2many('exhibitor.group.name', string='Exhibitor Group Name')
    industry_name = fields.Many2many('industry.name', string='Industry')
    sector = fields.Many2many('sector.name',  string='Sector')




