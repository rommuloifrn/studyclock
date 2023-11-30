let notes = 0;
let manually = 0;

// toggle manual session insertion
const manButton = document.getElementById('manuallybutton');
const manuallyBoard = document.getElementById('manually');
const clockBoard = document.getElementById('clock');

// toggle session
const input = document.getElementById('letter');
const noteSpace = document.getElementById('notes');
const notesHeadText = document.getElementById('notesheadtext');

const manuallyNoteSpace = document.getElementById('notesman');
const notesManuallyHeadText = document.getElementById('notesmanheadtext');

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

function toggleSessionTableNotes(sessionId) {
    sess = document.getElementById("sess" + sessionId + "notes");
    if (sess.getAttribute("class") == "hidden") {
        sess.setAttribute("class", "");
    } else {
        sess.setAttribute("class", "hidden");
    }
}