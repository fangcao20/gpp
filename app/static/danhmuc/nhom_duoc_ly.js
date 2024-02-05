$.get('/danh-muc/get-nhom-duoc-ly'
).done(res => {
    let nhom_duoc_ly_list = res.nhom_duoc_ly_list;
    let html = '', i = 1;
    for (let r of nhom_duoc_ly_list) {
        html += `<tr>
            <td>${i}</td>
            <td>${r.name}</td>
        <tr>`;
        i++;
    }
    document.getElementById('table_nhom_duoc_lý').innerHTML = html;
}).fail(err => {
    console.log(err);
})