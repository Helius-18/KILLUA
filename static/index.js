var productListApiUrl="";
$(document).ready(function () {
    $("button").click(function(){
    $.ajax({
        method: 'POST',
        url: '/get_details'.concat(document.getElementById("mname").value),
        data: JSON.stringify(mname)
        });
        productListApiUrl='http://127.0.0.1:5000/get_details'.concat(document.getElementById("mname").value);
        $.get(productListApiUrl, function (response) {
            if(response) {
                document.getElementById('container').innerHTML="";
                document.getElementById('episodes').innerHTML="";
                var i=0;
                $.each(response, function(index, product) {
                    document.getElementById("container").innerHTML += '<div class="ml-item"> <a onclick="get_movie('+i+')" href="#" class="ml-mask jt" "><p id="hehe_'+i+'" style="display:none;">/get_movie'+product.href+'</p> <img class="lazy thumb mli-thumb" alt="'+product.name+'" src="'+product.image+'"> <span class="mli-info"><h2>'+product.name+'</h2></span> </a> </div>';
                    i+=1;
                });
            }
        });
    });
});
function get_movie(para) {
    var link=document.getElementById("hehe_".concat(para)).innerText
    $.ajax({
            method: 'POST',
            url:'http://127.0.0.1:5000'.concat(link),
            data: JSON.stringify(para)
        });
        link="http://127.0.0.1:5000"+link
        $.get(link, function (response) {
            if(response) {
                console.log("getting data");
                document.getElementById('container').innerHTML="";
                document.getElementById('episodes').innerHTML="";
                var i=Object.keys(response).length
                $.each(response, function(index, product) {
                    document.getElementById("episodes").innerHTML += '<li class="episode"><a onclick="get_episode('+(i-1)+')" href="#">Episode '+i+'</a><p id="haha_'+(i-1)+'" style="display:none">'+product.href+'</p></li>';
                    i-=1;
                });
            }
        });
}

function get_episode(para){
    var link=document.getElementById("haha_".concat(para)).innerText
    if((document.getElementById("frameid"))){
        document.getElementById("frameid").remove()
    }
    $.ajax({
        method: 'POST',
        url:'http://127.0.0.1:5000/get_episode'.concat(link),
        data: JSON.stringify(para)
    });
    link="http://127.0.0.1:5000/get_episode"+link
        $.get(link, function (response) {
            if(response) {
                console.log("getting episode");
                document.getElementById('container').innerHTML="";
                document.getElementById("movie").innerHTML +='<iframe id="frameid" style="position: absolute; border:none;" width="1500" height="845" src="'+response[0][0]+'"></iframe>';
            }
        });
}