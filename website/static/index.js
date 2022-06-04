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
             window.location.href ="/temp"; // redirect to the temperature page
           });
}

function deleteBP(bpId){
    fetch('/delete-bp', { //send a request to endpoint
           method: 'POST',
           body: JSON.stringify({ bpId: bpId})
           }).then((_res) => {
             window.location.href ="/bp"; // redirect to the blood pressure page
           });
}

function deleteGlucose(glucoseId){
    fetch('/delete-glucose', { //send a request to endpoint
           method: 'POST',
           body: JSON.stringify({ glucoseId: glucoseId})
           }).then((_res) => {
             window.location.href ="/glucose"; // redirect to the glucose page
           });
}

function addPatient(patientId){
    fetch('/add-patient', { //send a request to endpoint
           method: 'POST',
           body: JSON.stringify({ patientId: patientId})
           }).then((_res) => {
             window.location.href ="/patient"; // redirect to the doctor portal
           });
}

function removePatient(patientId){
    fetch('/remove-patient', { //send a request to endpoint
           method: 'POST',
           body: JSON.stringify({ patientId: patientId})
           }).then((_res) => {
             window.location.href ="/patient"; // redirect to the doctor portal
           });
}