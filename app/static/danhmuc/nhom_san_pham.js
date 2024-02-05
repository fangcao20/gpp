$.get('/danh-muc/get-nhom-san-pham'
).done(res => {
    let nhom_san_pham_list = res.nhom_san_pham_list;
    let html = '', i = 1;
    for (let r of nhom_san_pham_list) {
        html += `<tr>
            <td>${i}</td>
            <td>${r.name}</td>
        <tr>`;
        i++;
    }
    document.getElementById('table_nhom_san_pham').innerHTML = html;
}).fail(err => {
    console.log(err);
})