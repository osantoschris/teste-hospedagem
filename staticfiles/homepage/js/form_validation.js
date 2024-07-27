document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('formContact');

    form.addEventListener('submit', function (e) {
        if (!validateForm()) {
            e.preventDefault();
        };
    });
});

function validateForm() {

    var isValid = true;

    var name = document.getElementById('input_name');
    if (name.value.trim() === '') {
        isValid = false;
        alert('Atenção! Preencha o campo de nome!')
        name.focus();
        name.style.border = '1px solid red';
        return isValid;
    } else {
        name.style.border = '1px solid #CCCCCC';
    };
    
    var email = document.getElementById('input_email');
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email.value.trim() === '' || !emailPattern.test(email.value)) {
        isValid = false;
        alert('Atenção! Preencha o campo de email!')
        email.focus();
        email.style.border = '1px solid red';
        return isValid;
    } else {
        email.style.border = '1px solid #CCCCCC';
    };
    
    var message = document.getElementById('input_message');
    if (message.value.trim() === '') {
        isValid = false;
        alert('Atenção! Preencha o campo de mensagem!')
        message.focus();
        message.style.border = '1px solid red';
        return isValid
    } else {
        email.style.border = '1px solid #CCCCCC';
    };

    return isValid;

};