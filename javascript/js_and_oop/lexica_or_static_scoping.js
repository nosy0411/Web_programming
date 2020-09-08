var i = 5;

function a(){
    var i = 10;
    b();
}

function b(){
    console.log(i);
}

a();