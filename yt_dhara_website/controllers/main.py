from odoo import http
from odoo.http import request

class DharaWebsite(http.Controller):
    
    @http.route('/dhara/test', auth='public', website=True)
    def test_page(self):
        return "<h1>Dhara Enterprise Module Installed Successfully</h1>"
