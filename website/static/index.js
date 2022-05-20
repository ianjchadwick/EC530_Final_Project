function deleteNote(noteId){
    fetch('/delete-note', { //send a request to endpoint
           method: 'POST',
           body: JSON.stringify({ noteId: noteId})
           }).then((_res) => {
             window.location.href ="/"; // redirect to the home page
           });
}

function deleteWeight(weightId){
    fetch('/delete-weight', { //send a request to endpoint
           method: 'POST',
           body: JSON.stringify({ weightId: weightId})
           }).then((_res) => {
             window.location.href ="/weight"; // redirect to the weight page
           });
}

function deleteTemp(tempId){
    fetch('/delete-temp', { //send a request to endpoint
           method: 'POST',
           body: JSON.stringify({ tempId: tempId})
           }).then((_res) => {
             window.location.href ="/temp"; // redirect to the weight page
           });
}