$.get('/danh-muc/get-nha-cung-cap'
).done(res => {
    let res_list = res.nha_cung_cap_list;
    let html = '', i = 1;
    for (let r of res_list) {
        html += `<tr>
            <td>${i}</td>
            <td>${r.name}</td>
        <tr>`;
        i++;
    }
    document.getElementById('table_nha_cung_cap').innerHTML = html;
}).fail(err => {
    console.log(err);
})