{
    'name': 'Task Manager',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'summary': 'To track day to day tasks',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/task_manger.xml'
    ],
   
    'installable': True,
    'application': True,

    'license': 'LGPL-3',
   
}
