document.getElementById('menuIcon').addEventListener('click', function() {
    this.classList.toggle('change');
    document.getElementById('dropdownMenu').classList.toggle('show');
    document.body.classList.toggle('no-scroll');
});