from app import db, app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
import jwt


class NhaThuoc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), index=True, unique=True)
    sdk = db.Column(db.String(100))
    ds_dung_ten = db.Column(db.String(100), index=True)
    name = db.Column(db.String(500), index=True)
    ma_so_thue = db.Column(db.String(100))
    chung_chi_hanh_nghe = db.Column(db.String(100))
    address = db.Column(db.String(500))
    gpp = db.Column(db.String(100))
    image = db.Column(db.String(500))

    duoc_sis = db.relationship('DuocSi', cascade="all,delete", backref='nha_thuoc', lazy='dynamic')

    def __repr__(self):
        return '<NhaThuoc {}>'.format(self.name)

    def to_dict(self):
        return {self.id: {'code': self.code, 'sdk': self.sdk, 'ds_dung_ten': self.ds_dung_ten, 'name': self.name,
                          'ma_so_thue': self.ma_so_thue, 'chung_chi_hanh_nghe': self.chung_chi_hanh_nghe,
                          'address': self.address, 'gpp': self.gpp, 'image': self.image}}


class DuocSi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), index=True, unique=True)
    gioi_tinh = db.Column(db.String(5))
    truc_thuoc_nha_thuoc = db.Column(db.Integer, db.ForeignKey('nha_thuoc.id', ondelete='CASCADE', onupdate='CASCADE'),
                                     nullable=False)
    name = db.Column(db.String(100), index=True)
    so_dien_thoai = db.Column(db.String(15), index=True)
    trinh_do_chuyen_mon = db.Column(db.String(30), index=True)
    address = db.Column(db.String(500))
    email = db.Column(db.String(100))
    image = db.Column(db.String(500))

    def __repr__(self):
        return '<DuocSi {}>'.format(self.name)

    def to_dict(self):
        return {self.id: {'code': self.code, 'gioi_tinh': self.gioi_tinh,
                          'truc_thuoc_nha_thuoc': self.truc_thuoc_nha_thuoc, 'name': self.name,
                          'so_dien_thoai': self.so_dien_thoai, 'trinh_do_chuyen_mon': self.trinh_do_chuyen_mon,
                          'address': self.address, 'email': self.email, 'image': self.image}}


class KhachHang(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), index=True, unique=True)
    gioi_tinh = db.Column(db.String(5))
    tuoi = db.Column(db.Integer)
    name = db.Column(db.String(100), index=True)
    so_dien_thoai = db.Column(db.String(15), index=True)
    address = db.Column(db.String(500))
    email = db.Column(db.String(100))
    image = db.Column(db.String(500))

    def __repr__(self):
        return '<KhachHang {}>'.format(self.name)

    def to_dict(self):
        return {self.id: {'code': self.code, 'gioi_tinh': self.gioi_tinh,
                          'tuoi': self.tuoi, 'name': self.name, 'so_dien_thoai': self.so_dien_thoai,
                          'address': self.address, 'email': self.email}}


class NhomSanPham(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)

    def ___repr(self):
        return '<NhomSanPham {}>'.format(self.name)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class NhomDuocLy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)

    thuocs = db.relationship('Thuoc', cascade="all,delete", backref='nhom_duoc_ly', lazy='dynamic')

    def ___repr(self):
        return '<NhomDuocLy {}>'.format(self.name)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class Thuoc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    bdg = db.Column(db.String(1), index=True)
    sdk = db.Column(db.String(50), index=True)
    solo = db.Column(db.String(50), index=True)
    han_su_dung = db.Column(db.Date)
    dkbq = db.Column(db.String(255), index=True)
    note = db.Column(db.String(255), index=True)
    hoat_chat = db.Column(db.String(255), index=True)
    nhom_duoc_ly_id = db.Column(db.Integer, db.ForeignKey('nhom_duoc_ly.id', ondelete='CASCADE', onupdate='CASCADE'))
    don_vi_tinh_id = db.Column(db.Integer, db.ForeignKey('don_vi_tinh.id', ondelete='CASCADE', onupdate='CASCADE'))
    nuoc_san_xuat_id = db.Column(db.Integer, db.ForeignKey('nuoc_san_xuat.id', ondelete='CASCADE', onupdate='CASCADE'))
    nha_san_xuat_id = db.Column(db.Integer, db.ForeignKey('nha_san_xuat.id', ondelete='CASCADE', onupdate='CASCADE'))
    nha_cung_cap_id = db.Column(db.Integer, db.ForeignKey('nha_cung_cap.id', ondelete='CASCADE', onupdate='CASCADE'))

    def ___repr(self):
        return '<Thuoc {}>'.format(self.name)


class HoatChat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)

    def __repr__(self):
        return '<HoatChat {}>'.format(self.name)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class HamLuong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)

    def __repr__(self):
        return '<HamLuong {}>'.format(self.name)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class DonViTinh(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)

    thuocs = db.Relationship('Thuoc', cascade='all,delete', backref='don_vi_tinh', lazy='dynamic')

    def __repr__(self):
        return '<DonViTinh {}>'.format(self.name)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class NuocSanXuat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)

    thuocs = db.Relationship('Thuoc', cascade='all,delete', backref='nuoc_san_xuat', lazy='dynamic')

    def __repr__(self):
        return '<NuocSanXuat {}>'.format(self.name)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class NhaSanXuat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)

    thuocs = db.Relationship('Thuoc', cascade='all,delete', backref='nha_san_xuat', lazy='dynamic')

    def __repr__(self):
        return '<NhaSanXuat {}>'.format(self.name)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class NhaCungCap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)

    thuocs = db.Relationship('Thuoc', cascade='all,delete', backref='nha_cung_cap', lazy='dynamic')

    def __repr__(self):
        return '<NhaCungCap {}>'.format(self.name)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

