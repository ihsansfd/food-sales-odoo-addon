from odoo import api, fields, models


class Resep(models.Model):
    _name = 'penjualan_kue.resep'
    _description = 'Resep-Resep Kue'
    bahan_bahan = fields.Text('Bahan-Bahan', required=True)
    cara_pembuatan = fields.Text('Cara Pembuatan')
