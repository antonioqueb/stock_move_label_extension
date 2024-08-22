{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',  # Permisos de seguridad
        
        'views/custom_product_label_action.xml',
   
        'report/report_product_label_template_letter.xml'
    
    ],
    'installable': True,
    'application': False,
}
