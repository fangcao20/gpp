$.get('/danh-muc/get-don-vi-tinh'
).done(res => {
    let res_list = res.don_vi_tinh_list;
    let html = '', i = 1;
    for (let r of res_list) {
        html += `<tr>
            <td>${i}</td>
            <td>${r.name}</td>
        <tr>`;
        i++;
    }
    document.getElementById('table_don_vi_tinh').innerHTML = html;
}).fail(err => {
    console.log(err);
})