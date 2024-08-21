{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'report/report_product_label_template_letter.xml',
        'report/report_action.xml',
        'views/custom_product_label_layout_view.xml',
        'views/custom_product_label_action.xml',
        'views/stock_picking_action_print_label.xml',  # Nueva acción de impresión
        'views/stock_picking_view_inherit.xml',  # Botón en la vista de traslados internos
    ],
    'installable': True,
    'application': False,
}
