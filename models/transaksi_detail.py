from odoo import api, fields, models


class TransaksiDetail(models.Model):
    _name = 'penjualan_kue.transaksi_detail'
    _description = 'Transaksi Detail'

    produk_id = fields.Many2one(comodel_name='penjualan_kue.produk', string='Pilih Produk')
    kuantitas = fields.Integer(string='Kuantitas', required=True)
