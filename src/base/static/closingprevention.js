
window.addEventListener('beforeunload', function (e) {
    e.preventDefault();
    e.returnValue = 'aaaaaaa';
});

/*
window.addEventListener('beforeunload', function (e) {
    // Cancel the event
    e.preventDefault();
    // Chrome requires returnValue to be set
    e.returnValue = '';
  });
  window.onbeforeunload=function(){return "Navigating away will lose the changes you've made to your code."};*/