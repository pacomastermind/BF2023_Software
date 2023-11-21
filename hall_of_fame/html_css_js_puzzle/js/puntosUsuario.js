var puntosEnLocal
var puntosEnPagina
function regularizarPuntos() {
    if (isNaN(parseInt(localStorage.getItem('puntosUsuario')))) {
        let puntosNullos=0;
        localStorage.setItem('puntosUsuario', puntosNullos);
    }
    puntosEnLocal=localStorage.getItem('puntosUsuario')
    puntosEnPagina=document.getElementById('puntos');
    puntosEnPagina.innerHTML=puntosEnLocal;
}