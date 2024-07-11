# -*- coding: utf-8 -*-
{
    'name': 'POS customization',
    'summary': 'PoS, but way better',
    'version': '17.0.0.0.0',
    'category': 'Sales/Point of Sale',
    'license': 'OPL-1',
    'author': 'Rooteam',
    'depends': [
        'point_of_sale', 'pos_preparation_display', 'pos_takeaway'
    ],
    'data': [

    ],
    'assets': {
        'web.assets_backend': [
        ],
        'point_of_sale._assets_pos': [
            '/pos_customization/static/src/scss/pos_customization.scss',
            '/pos_customization/static/src/app/generic_components/orderline/Orderline.xml',
            '/pos_customization/static/src/app/generic_components/orderline/orderline.js',
            '/pos_customization/static/src/js/models.js',
        ],
        'pos_preparation_display.assets': [
            '/pos_customization/static/src/pos_preparation_display/order/order.xml',
            '/pos_customization/static/src/pos_preparation_display/models/order.js',
        ],

    },
    'application': True,
    'installable': True,
    'auto_install': False,
}
