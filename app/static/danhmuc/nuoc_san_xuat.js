$.get('/danh-muc/get-nuoc-san-xuat'
).done(res => {
    let res_list = res.nuoc_san_xuat_list;
    let html = '', i = 1;
    for (let r of res_list) {
        html += `<tr>
            <td>${i}</td>
            <td>${r.name}</td>
        <tr>`;
        i++;
    }
    document.getElementById('table_nuoc_san_xuat').innerHTML = html;
}).fail(err => {
    console.log(err);
})