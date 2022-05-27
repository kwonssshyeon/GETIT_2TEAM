if(localStorage.getItem("alertext")!=''){
    var data = localStorage.getItem("alertext");
    document.getElementById("altText").innerHTML = data;
    add_div();
}

function add_div(){
    var div = document.createElement('div');
    div.innerHTML = document.getElementById('aa').innerHTML;
    ('field').append(div);
    //document.getElementById('field').append(div);
}