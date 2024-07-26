document.getElementById('menuIcon').addEventListener('click', function() {
    this.classList.toggle('change');
    document.getElementById('dropdownMenu').classList.toggle('--show');
    document.body.classList.toggle('--no-scroll');
});


// function getValues() {
//     var name = document.getElementById('input_name').value.length;
//     var email = document.getElementById('input_email').value.length;
//     var message = document.getElementById('input_message').value.length;

//     if (name < 1 && email < 1 && message < 1) {
//         console.log('Campos não preenchidos');
//     } else {
//         console.log('Campos preenchidos')  
//     };
// };



// function getName() {
//     var name = document.getElementById('input_name').value.length;
//     console.log(name);
// };

// document.getElementById('btnSubmit').addEventListener('click', getValues);