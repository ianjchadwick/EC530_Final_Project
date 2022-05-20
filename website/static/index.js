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