{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',  # Cargar primero los permisos de seguridad
        'views/custom_product_label_action.xml'
    ],
    'installable': True,
    'application': False,
}
