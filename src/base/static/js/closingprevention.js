closingListener = function (e) {
  e.preventDefault();
  e.returnValue = '';
}

function closingWarningLoad() {
  window.addEventListener('beforeunload', closingListener);
}

function closingWarningUnload() {
  window.removeEventListener('beforeunload', closingListener);
}