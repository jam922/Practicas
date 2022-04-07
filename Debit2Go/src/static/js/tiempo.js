let tiempo = document.getElementById('tiempo')


function hora(){
    let hoy = new Date();
    var fecha = formatearnum(hoy.getDate()) + '/' + formatearnum(( hoy.getMonth() + 1 )) + '/' + hoy.getFullYear();
    var hora = formatearnum(hoy.getHours()) + ':' + formatearnum(hoy.getMinutes()) + ':' + formatearnum(hoy.getSeconds());
    var fechaYHora = fecha + ' ' + hora;
    
    tiempo.innerHTML = fechaYHora;
    
}

function formatearnum(fecha) {
    let dia = parseInt(fecha)
    if (dia<10) {
        dia = `0${dia}`
    }
    return dia
}

setInterval('hora()',1000);