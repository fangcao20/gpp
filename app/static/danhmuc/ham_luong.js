$.get('/danh-muc/get-ham-luong'
).done(res => {
    let ham_luong_list = res.ham_luong_list;
    let html = '', i = 1;
    for (let r of ham_luong_list) {
        html += `<tr>
            <td>${i}</td>
            <td>${r.name}</td>
        <tr>`;
        i++;
    }
    document.getElementById('table_ham_luong').innerHTML = html;
}).fail(err => {
    console.log(err);
})