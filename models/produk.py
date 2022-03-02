from odoo import models, fields

class Produk(models.Model):
	_name = "penjualan_kue.produk"
	_description = "Model kue"

	nama = fields.Char(string='Nama Kue', required=True)
	deskripsi = fields.Char(string='Deskripsi')
	harga = fields.Float(string='Harga', required=True)
	pengeluaran = fields.Float(string='Pengeluaran', required=True)
	resep_ids = fields.Many2one(comodel_name='penjualan_kue.resep', string='Resep')
