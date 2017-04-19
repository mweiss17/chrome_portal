// retrieve budget from mint


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
  console.log(statusText)
  console.log(document.getElementById('transactions'))
  document.getElementById('transactions').textContent = statusText;
}

// store the most recent values in a cache

