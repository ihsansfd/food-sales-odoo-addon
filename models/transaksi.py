
from pyparsing import null_debug_action
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Transaksi(models.Model):
    _name = 'penjualan_kue.transaksi'
    _description = 'Transaksi Kue'

    produk_ids = fields.Many2many(comodel_name='penjualan_kue.produk', string='Pilih Produk', required=True)
    kuantitas = fields.Integer(string='Kuantitas', required=True)
    
    pembeli = fields.Many2many(comodel_name='penjualan_kue.pembeli', string='Pilih Pembeli')
    
    total_beli = fields.Float(string='Total Pembelian', required=True)
    uang_bayar = fields.Float(string='Uang Bayar')
    
    # By default gk kesimpen ke database, kecuali pakai store=True
    kembalian = fields.Float(compute='_compute_kembalian', string='Kembalian', readonly=True)
    
    @api.depends("total_beli", "uang_bayar")
    def _compute_kembalian(self):
        for record in self:
            record.kembalian = record.uang_bayar - record.total_beli

    # clear fields
    def clear_all_fields(self):
        for record in self:
            record.produk_ids = None 
            record.kuantitas = 0
            record.pembeli = None
            record.total_beli = 0
            record.uang_bayar = 0

    @api.constrains('uang_bayar')
    def _constrains_uang_bayar(self):
        for record in self:
            if record.total_beli > record.uang_bayar:
                raise ValidationError("Uang Bayar haruslah tidak kurang dari Total Pembelian")
