$.get('/danh-muc/get-nha-san-xuat'
).done(res => {
    let res_list = res.nha_san_xuat_list;
    let html = '', i = 1;
    for (let r of res_list) {
        html += `<tr>
            <td>${i}</td>
            <td>${r.name}</td>
        <tr>`;
        i++;
    }
    document.getElementById('table_nha_san_xuat').innerHTML = html;
}).fail(err => {
    console.log(err);
})