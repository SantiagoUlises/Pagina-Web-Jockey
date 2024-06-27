// document.addEventListener("DOMContentLoaded", function() {
//     function updateDate() {
//         const dateElement = document.querySelector('.fecha');
//         const options = { year: 'numeric', month: 'long', day: 'numeric' };
//         const today = new Date().toLocaleDateString('es-ES', options);
//         dateElement.textContent = today;
//     }
    
//     updateDate();

// });

function mostrafechaActual(){
    const fechaActual=new Date();
    const dia=fechaActual.getDate();
    const mes=fechaActual.getMonth()+1;
    const year=fechaActual.getFullYear();
    const fechaForm = dia + '/' + mes + '/' + year
    document.getElementById("fecha").textContent=fechaForm
}   

window.onload=function(){
    mostrafechaActual()
}