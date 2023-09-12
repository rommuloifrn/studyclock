let notes = 0;
let manually = 0;

function toggleNotes() {
    if (notes == 0) {
        noteSpace.style.display = "flex";
        notesHeadText.innerText = "close";
        notes = 1;
    } else {
        noteSpace.style.display = "none";
        notesHeadText.innerText = "write some notes!";
        notes = 0;
    }
}

function toggleManually() {
    if (manually == 0) {
        manuallyBoard.style.display = "flex";
        clockBoard.style.display = "none";
        manButton.innerText = "close"
        manually = 1;
    } else {
        manuallyBoard.style.display = "none";
        clockBoard.style.display = "flex";
        manButton.innerText = "Add manually"
        manually = 0;
    }
}

function toggleNotesOnManually() {
    if (notes == 0) {
        manuallyNoteSpace.style.display = "flex";
        notesManuallyHeadText.innerText = "close";
        notes = 1;
    } else {
        manuallyNoteSpace.style.display = "none";
        notesManuallyHeadText.innerText = "write some notes!";
        notes = 0;
    }
}
// function toggleN() {
//     if (noteSpace.style.display == "none") {
//         noteSpace.style.display = "flex";
//         notesHeadText.innerText = "close";
//     } else {
//         noteSpace.style.display = "none";
//         notesHeadText.innerText = "write some notes!";
//     }
//     //noteSpace.setAttribute("class", '');
// }

// function toggleManually() {
//     if (manuallyBoard.style.display === "none" && clockBoard.style.display == "flex") {
//         manuallyBoard.style.display = "flex";
//         clockBoard.style.display = "none";
//     } else {
//         manuallyBoard.style.display = "none";
//         clockBoard.style.display = "flex";
//     }
// }






// global variables
const time_el = document.getElementById('display');
const start_btn = document.getElementById('start');
const reset_btn = document.getElementById('reset');

const manButton = document.getElementById('manuallybutton');
const manuallyBoard = document.getElementById('manually');
const clockBoard = document.getElementById('clock');

const input = document.getElementById('letter');
const noteSpace = document.getElementById('notes');
const notesHeadText = document.getElementById('notesheadtext');

const manuallyNoteSpace = document.getElementById('notesman');
const notesManuallyHeadText = document.getElementById('notesmanheadtext');


let seconds = 0;
let interval = null;

// Event listeners
//notes.addEventListener('click', toggleNotes);
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