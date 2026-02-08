{
    'name': 'Dhara Enterprise Website',
    'version': '1.0',
    'summary': 'eCommerce website for Dhara Enterprise',
    'description': """
        Custom website module for Dhara Enterprise, selling electrical products and services.
        Features:
        - Custom Design inspired by industry standards
        - Product Categories: Switchgear, Wires, Motors, etc.
        - Service Inquiries
    """,
    'category': 'Website/Website',
    'author': 'Yugma Tech',
    'website': 'https://yugmatech.com',
    'depends': ['website', 'website_sale', 'sale_management', 'contacts', 'stock'],
    'data': [
        'data/product_data.xml',
        'data/website_data.xml',
        'views/layout_views.xml',
        'views/homepage_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'yt_dhara_website/static/src/scss/primary_variables.scss',
            'yt_dhara_website/static/src/scss/style.scss',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
