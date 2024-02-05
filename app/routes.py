from flask import render_template, flash, redirect, url_for, request, jsonify, get_flashed_messages
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy import func, case, desc
from app import app, db
from app.models import NhomSanPham, HoatChat, HamLuong, NhomDuocLy, DonViTinh, NhaSanXuat, NhaCungCap, NuocSanXuat


@app.route('/')
@app.route('/danh-muc')
def base():
    return render_template("base.html")


@app.route('/danh-muc/nha-thuoc')
def dm_nha_thuoc():
    return render_template("danhmuc/nha_thuoc.html")


@app.route('/danh-muc/duoc-si')
def dm_duoc_si():
    return render_template("danhmuc/duoc_si.html")


@app.route('/danh-muc/khach-hang')
def dm_khach_hang():
    return render_template("danhmuc/khach_hang.html")


# Nhóm sản phẩm----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/nhom-san-pham')
def dm_nhom_san_pham():
    return render_template("danhmuc/nhom_san_pham.html")


@app.route('/danh-muc/get-nhom-san-pham')
def get_nhom_san_pham():
    nhom_san_pham_list = get_danh_muc(NhomSanPham)
    return jsonify(nhom_san_pham_list=nhom_san_pham_list)


# Thuốc ----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/thuoc')
def dm_thuoc():
    return render_template("danhmuc/thuoc.html")


# Hoạt chất----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/hoat-chat')
def dm_hoat_chat():
    return render_template("danhmuc/hoat_chat.html")


@app.route('/danh-muc/get-hoat-chat')
def get_hoat_chat():
    hoat_chat_list = get_danh_muc(HoatChat)
    return jsonify(hoat_chat_list=hoat_chat_list)


# Hàm lượng----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/ham-luong')
def dm_ham_luong():
    return render_template("danhmuc/ham_luong.html")


@app.route('/danh-muc/get-ham-luong')
def get_ham_luong():
    ham_luong_list = get_danh_muc(HamLuong)
    return jsonify(ham_luong_list=ham_luong_list)


# Nhóm dược lý----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/nhom-duoc-ly')
def dm_nhom_duoc_ly():
    return render_template("danhmuc/nhom_duoc_ly.html")


@app.route('/danh-muc/get-nhom-duoc-ly')
def get_nhom_duoc_ly():
    nhom_duoc_ly_list = get_danh_muc(NhomDuocLy)
    return jsonify(nhom_duoc_ly_list=nhom_duoc_ly_list)


# Đơn vị tính----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/don-vi-tinh')
def dm_don_vi_tinh():
    return render_template("danhmuc/don_vi_tinh.html")


@app.route('/danh-muc/get-don-vi-tinh')
def get_don_vi_tinh():
    don_vi_tinh_list = get_danh_muc(DonViTinh)
    return jsonify(don_vi_tinh_list=don_vi_tinh_list)


# Nhà cung cấp ----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/nha-cung-cap')
def dm_nha_cung_cap():
    return render_template("danhmuc/nha_cung_cap.html")


@app.route('/danh-muc/get-nha-cung-cap')
def get_nha_cung_cap():
    nha_cung_cap_list = get_danh_muc(NhaCungCap)
    return jsonify(nha_cung_cap_list=nha_cung_cap_list)


# Nhà sản xuất ----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/nha-san-xuat')
def dm_nha_san_xuat():
    return render_template("danhmuc/nha_san_xuat.html")


@app.route('/danh-muc/get-nha-san-xuat')
def get_nha_san_xuat():
    nha_san_xuat_list = get_danh_muc(NhaSanXuat)
    return jsonify(nha_san_xuat_list=nha_san_xuat_list)


# Nước sản xuất ----------------------------------------------------------------------------------------------------
@app.route('/danh-muc/nuoc-san-xuat')
def dm_nuoc_san_xuat():
    return render_template("danhmuc/nuoc_san_xuat.html")


@app.route('/danh-muc/get-nuoc-san-xuat')
def get_nuoc_san_xuat():
    nuoc_san_xuat_list = get_danh_muc(NuocSanXuat)
    return jsonify(nuoc_san_xuat_list=nuoc_san_xuat_list)


@app.route('/hoa-don/don-thuoc')
def hoa_don_xuat():
    return render_template("hoadon/don_thuoc.html")


@app.route('/hoa-don/hoa_don_nhap')
def hoa_don_nhap():
    return render_template("hoadon/hoa_don_nhap.html")


@app.route('/bao-cao')
def bao_cao():
    return render_template("bao_cao.html")


def get_danh_muc(Model):
    danhmuc = Model.query.all()
    danhmuc_list = []
    for h in danhmuc:
        danhmuc_list.append(h.to_dict())
    return danhmuc_list
