document.addEventListener("DOMContentLoaded", function() {
    var tableHD = document.getElementById('tableHD');
    selected_row(tableHD, selected_row_tableHD);
});

function selected_row(table, func) {
    var rows = Array.from(table.rows);
    rows.forEach(row => {
        row.addEventListener("click", function() {
            var checkedRow = rows.filter(r => r.classList.contains("selected-row"));
            for (let r of checkedRow) {
                r.classList.remove("selected-row");
            }
            row.classList.add("selected-row");
            func(row);
        })
    })
}

function selected_row_tableHD(row) {
    var cells = row.cells;
    var tenKH = cells[2].innerText;
    document.getElementById('select_KH').innerHTML = tenKH;
}