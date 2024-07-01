function mostrafechaActual(){
    const fechaActual = new Date();
    
    const diasSemana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
    const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    
    const diaSemana = diasSemana[fechaActual.getDay()];
    const dia = fechaActual.getDate();
    const mes = meses[fechaActual.getMonth()];
    const year = fechaActual.getFullYear();
    
    const fechaForm = `${diaSemana}, ${dia} de ${mes} de ${year}`;
    
    document.getElementById("fecha").textContent = fechaForm;
}

window.onload = function(){
    mostrafechaActual();
}
