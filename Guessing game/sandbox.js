//controlls slider
var slider = document.getElementById('slider');
//corosponding number
var corro = document.getElementById('corro');
//counts clicks
var clicks = 0;
//changing number to show slider value
var output = document.getElementById('f');
//controlls button
var sub = document.getElementById('check');
//play again button
var playagain = document.getElementById('playagain');
output.innerHTML = slider.value

slider.oninput = function(){
    output.innerHTML = this.value;
}

num = Math.floor(Math.random() * 101);
//console.log (num);

function numcheck(){
    var sliderm = Number(slider.value);
    if (num > sliderm){
        corro.innerHTML = ('Try a higher number');
    }
    
    else if (num < sliderm){
        corro.innerHTML = ('Try a lower number');
    }
    
    else {
    corro.innerHTML = ("Congratulations!<br/>" + "Would you like to play again?")
    sub.style.display = 'none';
    playagain.style.display = 'inline-block';
    }
}

function onClick(){
        clicks += 1;
    document.getElementById('clicks').innerHTML = clicks;
    console.log (clicks)
}

function refreshPage(){
    window.location.reload();
}