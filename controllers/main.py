from odoo import http

class TrainingController(http.Controller):
    @http.route('/training/hello', auth='public')
    def hello(self, **kw):
        return "<h1>Hello, Ini adalah versi pertama dari training module sebagai bukti adanya perubahan</h1>"
