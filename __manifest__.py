# -*- coding: utf-8 -*-
{
    'name': 'RAYL Converge',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'website': "https://planet-odoo.com",
    'sequence': 1,
    'summary': 'RAYL Converge',
    'description': """All the customization for rayl saas instances. """,
    'author': "Planet odoo",
    "depends": ['base', 'crm', 'account', 'web'],
    "data": [
        'views/invoice_list_view.xml',
        'views/invoice_portal.xml',
    ],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
