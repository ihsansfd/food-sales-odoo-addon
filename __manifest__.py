{
    'name': 'Penjualan Kue',
    'version': '1.0',
    'description': 'Module tentang Point of Sales Kue',
    'summary': '',
    'author': 'Ihsan Nurul Iman',
    'website': 'ihsansfd.github.io',
    'category': 'Business',
    'depends': [
        'base'
    ],
    'data': [
        'views/actions/produk_view.xml',
        'views/actions/resep_view.xml',
        'views/actions/pembeli_view.xml',
        'views/actions/transaksi_view.xml',
        'views/menus/main_menu.xml',
        'security/ir.model.access.csv'
    ],
    'application': True
}