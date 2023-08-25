// global variables
const time_el = document.querySelector('.watch .time');
const start_btn = document.getElementById('start');
const reset_btn = document.getElementById('reset');
const input = document.getElementById('letter');


let seconds = 0;
let interval = null;

// Event listeners
start_btn.addEventListener('click', start);
reset_btn.addEventListener('click', reset);

// update the timer
function timer() {
    seconds++;

    // format our time
    let secs = seconds % 60;
    let mins = Math.floor(seconds/60 % 60);
    let hours = Math.floor(seconds/60 / 60);

    if (secs < 10) secs = '0' + secs;
    if (mins < 10) mins = '0' + mins;
    if (hours < 10) hours = '0' + hours;

    
    time_el.innerText = `${hours}:${mins}:${secs}`;
    input.setAttribute('value', `${hours}:${mins}:${secs}`);
}

function start () {
    if (interval) {
        //return
        clearInterval(interval);
        interval = null;
        start_btn.innerText = 'start';
        return;
    }

    interval = setInterval(timer, 1000);
    start_btn.innerText = 'stop';
}

function stop () {
    clearInterval(interval);
    interval = null;
}

function reset() {
    stop();
    seconds = 0;
    time_el.innerText = '00:00:00';
    input.setAttribute("value", '00:00:00');
}