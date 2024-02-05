console.log(document.URL);
$.get('/danh-muc/get-hoat-chat'
).done(res => {
    var hoat_chat_list = res.hoat_chat_list;
    let html = '', i = 1;
    for (let r of hoat_chat_list) {
        html += `<tr>
            <td>${i}</td>
            <td>${r.name}</td>
        <tr>`;
        i++;
    }
    document.getElementById('table_hoat_chat').innerHTML = html;
}).fail(err => {
    console.log(err);
})