{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'report/report_product_label_template_letter.xml',
        'report/report_action.xml',
        'views/custom_product_label_layout_view.xml',
        'views/custom_product_label_action.xml',
    ],
    'installable': True,
    'application': False,
}
