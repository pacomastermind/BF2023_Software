var arrayCartasGiradas=[];
var numAlet;
var monaLisa;
var elBeso;
var lasMeninas;
var theScream;
var vanGogh;

function irMonaLisa() {
    window.location.href = "./puzzle.html";
    sessionStorage.setItem('puzzleElejigo', 'monaLisa');
}
function irAlBeso() {
    window.location.href = "./puzzle.html";
    sessionStorage.setItem('puzzleElejigo', 'elBeso');
}
function irLasMeninas() {
    window.location.href = "./puzzle.html";
    sessionStorage.setItem('puzzleElejigo', 'lasMeninas');
}
function irTheScream() {
    window.location.href = "./puzzle.html";
    sessionStorage.setItem('puzzleElejigo', 'theScream');
}
function irVanGogh() {
    window.location.href = "./puzzle.html";
    sessionStorage.setItem('puzzleElejigo', 'vanGogh');
}
/**
 * Añade el evento cliclable a las cartas y establece el cuadro de fondo
 * @date 2023-04-25
 */
function añadirEventoClick() {
    //Eventos del click
    let cartas=document.getElementsByClassName('portadaCartas');
    for(let carta of cartas){
        carta.addEventListener('click', girarCarta);
    }
    //elegir numero para cuadro inicial
    numAlet=(Math.floor(Math.random() * 4)*3);
}
function girarCarta(event) {
    let carta=event.target;
    let numero=parseInt(carta.alt)+numAlet;
    console.log(numero);
    carta.src="./img/cuadrosPintores/completaCuadros"+numero+".png";
    if (!arrayCartasGiradas.includes(numero)) {
        arrayCartasGiradas.push(numero);
        console.log(arrayCartasGiradas);
        if (arrayCartasGiradas.length==3) {
            setTimeout(function() {
                location.assign("./completaCuadros.html");
                let cartas=document.getElementsByClassName('portadaCartas');
                for(let carta of cartas){
                    carta.src="./img/cuadrosPintores/dorsalPortada.png";
                }
                arrayCartasGiradas=[]
            }, 1000);
        }
    }else{
        let indice = arrayCartasGiradas.indexOf(numero);
            arrayCartasGiradas.splice(indice, 1);
        carta.src="./img/cuadrosPintores/dorsalPortada.png";
    }
}
/**
 * DOM
 * @date 2023-04-17
 */
function domCargado(){
    //puntos
    regularizarPuntos()
    //cartas
    añadirEventoClick()
    //puzzles
    monaLisa=document.getElementById('monaLisa');
    monaLisa.addEventListener('click', irMonaLisa);
    elBeso=document.getElementById('elBeso');
    elBeso.addEventListener('click', irAlBeso);
    lasMeninas=document.getElementById('lasMeninas');
    lasMeninas.addEventListener('click', irLasMeninas);
    theScream=document.getElementById('theScream');
    theScream.addEventListener('click', irTheScream);
    vanGogh=document.getElementById('vanGogh');
    vanGogh.addEventListener('click', irVanGogh);
}


//Inicio de carga evento
document.addEventListener('DOMContentLoaded', domCargado);