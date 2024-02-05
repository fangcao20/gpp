$.get('/danh-muc/get-nhom-san-pham'
).done(res => {
    let nhom_san_pham_list = res.nhom_san_pham_list;
    document.getElementById('select_nhom_san_pham').innerHTML = set_select(nhom_san_pham_list);
}).fail(err => {
    console.log(err.statusText);
})


function set_select(list) {
    let html = `<option value="">Chọn</option>`, i = 1;
    for (let r of list) {
        html += `<option value="${r.id}">${r.name}</option>`;;
    }
    return html;
}

function select_san_pham(sl) {
    let val = sl.options[sl.selectedIndex].text;
    if (val === "Thuốc") {
        document.getElementById('san_pham_thuoc').style.display = 'block';
    } else {
        document.getElementById('san_pham_thuoc').style.display = 'none';
    }
}