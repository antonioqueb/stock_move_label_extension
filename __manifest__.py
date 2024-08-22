{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',  # Cargar primero los permisos de seguridad
        'report/report_product_label_template_letter.xml',  # Cargar el reporte a continuación
        'views/custom_product_label_action.xml',  # Cargar las vistas y acciones al final
    ],
    'installable': True,
    'application': False,
}
