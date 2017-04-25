// retrieve budget from mint

$(document).ready(function() {

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

transactions = httpGet("http://127.0.0.1:5000/minty")
renderStatus(transactions)
function renderStatus(statusText) {
  mint = JSON.parse(statusText)
  console.log(mint.budget)
  mint.budget.spend.forEach(function(budget){
    tr = $('<tr>')
    tr.append($('<td>'+budget.cat+"</td>"))
    tr.append($('<td> $'+budget.amt+'</td>'))
    $("#budgets-table").append(tr)
  });
}

// store the most recent values in a cache
});
