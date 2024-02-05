$.get('/danh-muc/get-hoat-chat'
).done(res => {
    let hoat_chat_list = res.hoat_chat_list;
    document.getElementById('select_hoat_chat').innerHTML = set_select(hoat_chat_list);
}).fail(err => {
    console.log(err);
})

$.get('/danh-muc/get-ham-luong'
).done(res => {
    let ham_luong_list = res.ham_luong_list;
    document.getElementById('select_ham_luong').innerHTML = set_select(ham_luong_list);
}).fail(err => {
    console.log(err.statusText);
})

$.get('/danh-muc/get-nhom-duoc-ly'
).done(res => {
    let nhom_duoc_ly_list = res.nhom_duoc_ly_list;
    document.getElementById('select_nhom_duoc_ly').innerHTML = set_select(nhom_duoc_ly_list);
}).fail(err => {
    console.log(err.statusText);
})

$.get('/danh-muc/get-don-vi-tinh'
).done(res => {
    let don_vi_tinh_list = res.don_vi_tinh_list;
    document.getElementById('select_don_vi_tinh').innerHTML = set_select(don_vi_tinh_list);
}).fail(err => {
    console.log(err.statusText);
})

$.get('/danh-muc/get-nha-cung-cap'
).done(res => {
    let nha_cung_cap_list = res.nha_cung_cap_list;
    document.getElementById('select_nha_cung_cap').innerHTML = set_select(nha_cung_cap_list);
}).fail(err => {
    console.log(err.statusText);
})

$.get('/danh-muc/get-nha-san-xuat'
).done(res => {
    let nha_san_xuat_list = res.nha_san_xuat_list;
    document.getElementById('select_nha_san_xuat').innerHTML = set_select(nha_san_xuat_list);
}).fail(err => {
    console.log(err.statusText);
})

$.get('/danh-muc/get-nuoc-san-xuat'
).done(res => {
    let nuoc_san_xuat_list = res.nuoc_san_xuat_list;
    document.getElementById('select_nuoc_san_xuat').innerHTML = set_select(nuoc_san_xuat_list);
}).fail(err => {
    console.log(err.statusText);
})

function addHoatChat() {
    let sl_hc = document.getElementById('select_hoat_chat');
    let hc = sl_hc.options[sl_hc.selectedIndex].text;
    let sl_hl = document.getElementById('select_ham_luong');
    let hl = sl_hl.options[sl_hl.selectedIndex].text;
    let inputs = document.getElementsByClassName('show-hoat-chat');
    inputs[inputs.length - 1].value = hc + ' ' + hl;

    let new_div = document.createElement('div');
    new_div.innerHTML = `
        <input type="text" class="form-control show-hoat-chat" disabled>
        <button class="btn btn-sm btn-danger" onclick="delHoatChat(this)" style="margin-left: 10px">-</button>
    `;
    new_div.classList.add('d-flex', 'flex-row', 'mb-1');
    document.getElementById('show_hoat_chat').appendChild(new_div);
}

function delHoatChat(btn) {
    let div = btn.parentElement;
    div.remove();
}

function set_select(list) {
    let html = `<option value="">Chọn</option>`, i = 1;
    for (let r of list) {
        html += `<option value="${r.id}">${r.name}</option>`;;
    }
    return html;
}

function addThuoc() {
    let name = document.getElementById('name').value;
    let sdk = document.getElementById('sdk').value;
    let solo = document.getElementById('solo').value;
    let sl_dvt = document.getElementById('select_don_vi_tinh');
    let don_vi_tinh_id = sl_dvt.value;
    let dvt = sl_dvt.options[sl_dvt.selectedIndex].text;
    let han_su_dung = document.getElementById('han_su_dung').value;
    let bdg = document.getElementById('bdg').value;
    let sl_ndl = document.getElementById('select_nhom_duoc_ly');
    let nhom_duoc_ly_id = sl_ndl.value;
    let ndl = sl_ndl.options[sl_ndl.selectedIndex].text;
    let sl_ncc = document.getElementById('select_nha_cung_cap');
    let nha_cung_cap_id = sl_ncc.value;
    let ncc = sl_ncc.options[sl_ncc.selectedIndex].text;
    let sl_nsx = document.getElementById('select_nha_san_xuat');
    let nha_san_xuat_id = sl_nsx.value;
    let nsx = sl_nsx.options[sl_nsx.selectedIndex].text;
    let sl_nuocsx = document.getElementById('select_nuoc_san_xuat');
    let nuoc_san_xuat_id = sl_nuocsx.value;
    let nuocsx = sl_nuocsx.options[sl_nuocsx.selectedIndex].text;
    let dkbq = document.getElementById('dkbq').value;
    let note = document.getElementById('note').value;
    let hoat_chat_list = document.getElementsByClassName('show-hoat-chat');
    let hoat_chat = '';
    for (let h of hoat_chat_list) {
        hoat_chat += h.value;
        hoat_chat += ' + '
    }
    hoat_chat = hoat_chat.slice(0, -6);

    let table = document.getElementById('table_thuoc');
    let i = table.rows.length;
    let new_row = document.createElement('tr');
    let html = `
        <td>${i + 1}</td>
        <td>TH000${i + 1}</td>
        <td>${name}</td>
        <td>${hoat_chat}</td>
        <td>${sdk}</td>
        <td>${solo}</td>
        <td>${dvt}</td>
        <td>${han_su_dung}</td>
        <td>${bdg}</td>
        <td>${ndl}</td>
        <td>${ncc}</td>
        <td>${nsx}</td>
        <td>${nuocsx}</td>
        <td>${dkbq}</td>
        <td>${note}</td>
    `;
    new_row.innerHTML = html;
    table.appendChild(new_row);
}