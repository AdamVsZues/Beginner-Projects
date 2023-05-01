let rowid = 0;
let x = 0;
// let
function deleteRow(row) {
  document.getElementById(row).remove();
}

function editRow(row) {
  let upcTable = document.getElementById(`upcvalue${row}`).innerText;
  document.getElementById("upc").value = upcTable;
  let descTable = document.getElementById(`descvalue${row}`).innerText;
  document.getElementById("description").value = descTable;
  let quantityTable = document.getElementById(`quanvalue${row}`).innerText;
  document.getElementById("quantity").value = quantityTable;
  let lpTable = document.getElementById(`lpvalue${row}`).innerText;
  document.getElementById("list-price").value = lpTable;

  document.getElementById(row).remove();
  
  document.getElementById('add').innerHTML = "Update"
}


document.getElementById("add").addEventListener("click", function addData() {
  let upc = document.getElementById("upc").value;
  let desc = document.getElementById("description").value;
  let quan = document.getElementById("quantity").value;
  let listprice = document.getElementById("list-price").value;
  let table = document.getElementById("table");
  let row = table.insertRow(-1);
  let upcTable = row.insertCell(0);
  let descTable = row.insertCell(1);
  let quantityTable = row.insertCell(2);
  let listPriceTable = row.insertCell(3);
  let retailPriceTable = row.insertCell(4);
  let editBtnTable = row.insertCell(5);
  let deleteBtnTable = row.insertCell(6);

  row.setAttribute(`id`, rowid);
  upcTable.innerHTML = upc;
  upcTable.setAttribute("id", `upcvalue` + x);
  descTable.innerHTML = desc;
  descTable.setAttribute("id", `descvalue` + x);
  quantityTable.innerHTML = quan;
  quantityTable.setAttribute("id", `quanvalue` + x);
  listPriceTable.innerHTML = listprice;
  listPriceTable.setAttribute("id", `lpvalue` + x);

  // edit button
  editBtnTable.setAttribute("class", "btn text-success");
  editBtnTable.setAttribute("id", "edit ");
  editBtnTable.setAttribute("onclick", `editRow(${rowid})`);
  editBtnTable.innerHTML = "EDIT";

  // delete button
  deleteBtnTable.setAttribute(`class`, `btn text-danger`);
  deleteBtnTable.setAttribute(`id`, `delete`);
  deleteBtnTable.setAttribute(`onclick`, `deleteRow(${rowid})`);
  deleteBtnTable.innerHTML = "DELETE";

  //update button
    if ((document.getElementById("add").innerHTML = "Update")) {
      document.getElementById("add").innerHTML = "Add";
    }

  // math
  if (quan < 50 && quan > 0) {
    let retailPrice = listprice * 1.5;
    retailPriceTable.innerHTML = "$ " + retailPrice;
  } else if (quan >= 50 && quan < 100) {
    let retailPrice = listprice * 2;
    retailPriceTable.innerHTML = "$ " + retailPrice;
  } else if (quan >= 100 && quan < 500) {
    let retailPrice = listprice * 2.25;
    retailPriceTable.innerHTML = "$ " + retailPrice;
  } else if (quan >= 500 && quan < 1000) {
    let retailPrice = listprice * 3;
    retailPriceTable.innerHTML = "$ " + retailPrice;
  } else if (quan >= 1000) {
    let retailPrice = listprice * 5;
    retailPriceTable.innerHTML = "$ " + retailPrice;
  } else {
    let retailPrice = null;
    retailPriceTable.innerHTML = retailPrice;
  }

  x++;
  rowid++;
});
