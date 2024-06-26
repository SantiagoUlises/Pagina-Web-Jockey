document.addEventListener("DOMContentLoaded", function() {
    function updateDate() {
        const dateElement = document.querySelector('.fecha');
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        const today = new Date().toLocaleDateString('es-ES', options);
        dateElement.textContent = today;
    }
    
    updateDate();

});