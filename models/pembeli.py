from odoo import api, fields, models


class Pembeli(models.Model):
    _name = 'penjualan_kue.pembeli'
    _description = 'Pembeli'

    nama_pembeli = fields.Char(string='Nama Pembeli', required=True)
    no_telp = fields.Char(string='Nomor Telepon')
    alamat = fields.Text(string='Alamat')
        
