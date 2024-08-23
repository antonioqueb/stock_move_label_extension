{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',  # Permisos de seguridad
        'report/report_product_label_template_letter.xml',  # Plantilla y reporte QWeb
        'views/custom_product_label_action.xml'  # Vistas y acciones
    ],
    'installable': True,
    'application': False,
}
