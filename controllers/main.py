from odoo import http

class TrainingController(http.Controller):
    @http.route('/training/hello', auth='public')
    def hello(self, **kw):
        return "<h1>testing 5</h1>"
