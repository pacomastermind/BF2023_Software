//Iniciacion de var
var tamano=10;
var piezzaDes;
var piezza;
var comodin;
var arrayPiezas=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
var cont;
var srcImg;
var idInterval;
var jugar;
var jugarAcabado;
var tiempoJugado;
var arrayImgElegida=['monaLisa','elBeso','lasMeninas','theScream','vanGogh']

//Identificar que imagen se esta moviendo
function moviendoImg(event){
    piezzaDes=event.target;   //para identificar que objeto se esta moviendo
}
function cambiarImg(event){
    piezza=event.target;
    comodin=piezzaDes.src;
    piezzaDes.src=piezza.src;
    piezza.src=comodin;

    comodin=piezzaDes.alt;
    piezzaDes.alt=piezza.alt;
    piezza.alt=comodin;
    ganar();

}
/**
 * Determina si se ha completado el puzzle y realiza los procesos necesarios
 * @date 2023-04-26
 */
function ganar(){
    piezza=document.getElementsByClassName("piezzaImg")
    let cont=1
    for(let item of piezza){
        if(item.alt!=cont){
            return false;
        }
        cont = cont+1;
    }
    //parar temporizador
    clearInterval(idInterval);
    //parar eventos arrastables
    piezzaDes=document.getElementsByClassName("piezzaDesImg");
    for(let item of piezzaDes){
        item.removeEventListener('dragstart', moviendoImg);
        item.removeEventListener('dragover',e=>{e.preventDefault()});
        item.removeEventListener('drop',cambiarImg);
    }
    piezza=document.getElementsByClassName("piezzaImg");
    for(let item of piezza){
        item.removeEventListener('dragstart', moviendoImg);
        item.removeEventListener('dragover',e=>{e.preventDefault()});
        item.removeEventListener('drop',cambiarImg);
    }
    //PUNTOS
    let puntosEnPagina=document.getElementById('puntos');
    let puntosTenia=parseInt(puntosEnPagina.innerText);
    let puntos=0;
    if (tiempoJugado<15) {
        puntos+=5;
    }else if(tiempoJugado<25) {
        puntos+=4;
    }else if(tiempoJugado<40) {
        puntos+=3;
    }else if(tiempoJugado<60) {
        puntos+=2;
    }else {
        puntos+=1;
    }
    puntosEnPagina.innerText=(puntosTenia+puntos);
    localStorage.setItem('puntosUsuario', (puntosTenia+puntos));
    //mostrar pestaña JUEGO ACABADO
    let winAcabado=document.getElementById('winJuegoAcabado');
    winAcabado.innerText='HAS GANADO';
    let puntosJuegoAcabado=document.getElementById('puntosJuegoAcabado');
    puntosJuegoAcabado.innerText=puntos;
    //mostrar la pestaña de Juego Acabado
    let mesaJuegoAcabado=document.getElementById('mesaJuegoAcabado');
    mesaJuegoAcabado.style.zIndex=3;
    mesaJuegoAcabado.style.width='500px';
    mesaJuegoAcabado.classList.add('mesaJuegoAcabadoColor');
    

}
/**
 * Esta funcion elige el juego
 * @date 2023-04-26
 * @param { * } cuadro
 */
function elegirCuadro(cuadro){
    piezzaDes=document.getElementsByClassName("piezzaDesImg");
    piezza=document.getElementsByClassName("piezzaImg");
    cont=0;
    arrayPiezas.sort(() => Math.random() - 0.5);
    for(let item of piezzaDes){
        srcImg='./img/'+cuadro+''+arrayPiezas[cont]+'.png';
        item.src=srcImg;
        item.alt=arrayPiezas[cont];
        cont=cont+1;
    }
    for(let item of piezza){
        item.src="./img/blanca.png";
        item.alt="";
    }
    let imagenElegida=document.getElementById('imgCambiarCuadro')
    imagenElegida.src='./img/'+cuadro+'.png';
    //reinicimos todo
    let winAcabado=document.getElementById('winJuegoAcabado');
    winAcabado.innerText='LISTO PARA JUGAR';
}
/**
 * Mecanismo flecha derecha
 * @date 2023-04-26
 */
function cambiarCuadroFlechaDer() {
    puzzleElejigo = sessionStorage.getItem('puzzleElejigo');
    let index=arrayImgElegida.indexOf(puzzleElejigo);
    console.log(index);
    index+=1;
    if (index>4) index=0;
    sessionStorage.setItem('puzzleElejigo', arrayImgElegida[index]);
    elegirCuadro(arrayImgElegida[index]);
}
/**
 * Mecanismo flecha izquierda
 * @date 2023-04-26
 */
function cambiarCuadroFlechaIzq() {
    puzzleElejigo = sessionStorage.getItem('puzzleElejigo');
    let index=arrayImgElegida.indexOf(puzzleElejigo);
    console.log(index);
    index-=1;
    if (index<0) index=4;
    sessionStorage.setItem('puzzleElejigo', arrayImgElegida[index]);
    elegirCuadro(arrayImgElegida[index]);
}
/**
 * Funcion que pinta el panel del juego
 * @date 2023-04-17
 */
function pintarPanelJuego(){
    //pintamos el panel de puzzleDes
    document.getElementById('puzzleDes').style.gridTemplateColumns="100px 100px";
    let items="";
    for (let index = 0; index < (parseInt(tamano)); index++) {
        items+=`<div class="piezzaDes"><img src="./img/blanca.png" class="piezzaDesImg" alt="" draggable="true"></div>`;
    }
    document.getElementById('puzzleDes').innerHTML=items
    //pintamos el panel de puzzleDes2
    document.getElementById('puzzleDes2').style.gridTemplateColumns="100px 100px";
    items="";
    for (let index = 0; index < (parseInt(tamano)); index++) {
        items+=`<div class="piezzaDes"><img src="./img/blanca.png" class="piezzaDesImg" alt="" draggable="true"></div>`;
    }
    document.getElementById('puzzleDes2').innerHTML=items
    //pintamos el panel de puzzle
    document.getElementById('puzzle').style.gridTemplateColumns="100px 100px 100px 100px";
    items="";
    for (let index = 0; index < (parseInt(tamano)*2); index++) {
        items+=`<div class="piezza"><img src="./img/blanca.png" class="piezzaImg" alt="" draggable="true"></div>`;
    }
    document.getElementById('puzzle').innerHTML=items
    //añadimos el fondo al panel 
    let mesaJuegoAcabado=document.getElementById('mesaJuegoAcabado');
    mesaJuegoAcabado.classList.add('mesaJuegoAcabadoColor');
}
/**
 * Contador de tiempo
 * @date 2023-04-26
 */
function contador() {
    tiempoJugado=document.getElementById('contador').value;
    tiempoJugado=parseInt(tiempoJugado)+1;
    document.getElementById('contador').value=tiempoJugado;

}
/**
 * inicializar eventos y temporizador
 * @date 2023-04-26
 */
function eventosPuzzle() {
    piezzaDes=document.getElementsByClassName("piezzaDesImg");
    for(let item of piezzaDes){
        item.addEventListener('dragstart', moviendoImg);
        item.addEventListener('dragover',e=>{e.preventDefault()});
        item.addEventListener('drop',cambiarImg);
    }
    piezza=document.getElementsByClassName("piezzaImg");
    for(let item of piezza){
        item.addEventListener('dragstart', moviendoImg);
        item.addEventListener('dragover',e=>{e.preventDefault()});
        item.addEventListener('drop',cambiarImg);
    }
    //Contador
    idInterval=setInterval(contador,1000);
}
/**
 * Iniciar juego y ocultar panel
 * @date 2023-04-26
 */
function empezarJuego() {
    //reinicimos todo
    let winAcabado=document.getElementById('winJuegoAcabado');
    winAcabado.innerText='LISTO PARA JUGAR';
    let puntosJuegoAcabado=document.getElementById('puntosJuegoAcabado');
    puntosJuegoAcabado.innerText=0;
    tiempoJugado=document.getElementById('contador');
    tiempoJugado.value=0;
    //ocultar la pestaña de Juego Acabado
    let mesaJuegoAcabado=document.getElementById('mesaJuegoAcabado');
    mesaJuegoAcabado.style.zIndex=1
    mesaJuegoAcabado.style.width='300px';
    mesaJuegoAcabado.classList.remove('mesaJuegoAcabadoColor');
    //Eventos del Drag and Drop
    eventosPuzzle()
}
/**
 * DOM 
 * @date 2023-04-15
 */
function domCargado(){
    //puntos
    regularizarPuntos()
    //pintar panel
    pintarPanelJuego()
    //Cargar puzzle al entrar en la pagina
    puzzleElejigo = sessionStorage.getItem('puzzleElejigo');
    elegirCuadro(puzzleElejigo);

    //Inicializar botones del panel
    botonDer=document.getElementById('flechaDerCambiarCuadro');
    botonDer.addEventListener('click', cambiarCuadroFlechaDer);
    botonIzq=document.getElementById('flechaIzqCambiarCuadro');
    botonIzq.addEventListener('click', cambiarCuadroFlechaIzq);

    jugarAcabado=document.getElementById('contenedorJuegoAcabado');
    jugarAcabado.addEventListener('click', empezarJuego);
}


//Inicio de carga evento
document.addEventListener('DOMContentLoaded', domCargado);
