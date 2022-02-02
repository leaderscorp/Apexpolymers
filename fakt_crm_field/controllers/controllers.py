# -*- coding: utf-8 -*-
# from odoo import http


# class FaktCrmField(http.Controller):
#     @http.route('/fakt_crm_field/fakt_crm_field/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fakt_crm_field/fakt_crm_field/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fakt_crm_field.listing', {
#             'root': '/fakt_crm_field/fakt_crm_field',
#             'objects': http.request.env['fakt_crm_field.fakt_crm_field'].search([]),
#         })

#     @http.route('/fakt_crm_field/fakt_crm_field/objects/<model("fakt_crm_field.fakt_crm_field"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fakt_crm_field.object', {
#             'object': obj
#         })
