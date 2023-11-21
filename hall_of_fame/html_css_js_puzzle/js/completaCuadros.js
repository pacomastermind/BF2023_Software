var tamano;
var arrayCartas;
var arrayCartasNoCompletadas;
var arrayCuadros;
var arrayCartasGiradas;
var contadorNumCartasGiradas;
var numFallos;
var jugar;
var jugarAcabado;

/**
 * Funcion que pinta el panel del juego
 * @date 2023-04-17
 */
function pintarPanelJuego(){
    //inicializar variables correctamente
    tamano=6
    arrayCartas=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18];
    arrayCartasNoCompletadas=arrayCartas.slice();
    arrayCuadros=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14],[15,16],[17,18]];
    arrayCartasGiradas=[];
    contadorNumCartasGiradas=0;
    numFallos=0;
    document.getElementById('fallos').value=numFallos;
    //pintamos el manel
    document.getElementById('mesaJuego').style.gridTemplateColumns="repeat("+tamano+", 1fr)";
    document.getElementById('mesaJuego').style.gridTemplateRows="repeat("+(tamano/2)+", 1fr)";
    //elementos de forma automatica
    let items="";
    arrayCartas.sort(() => Math.random() - 0.5);
    for (let index = 0; index < (parseInt(tamano)*parseInt(tamano/2)); index++) {
        items+=`<a href="#"><div class="carta"><img src="./img/cuadrosPintores/dorsal.png" id="${arrayCartas[index]}" class="cartaImg" alt=""></div></a>`;
    }
    document.getElementById('mesaJuego').innerHTML=items
    
    //añadimos el fondo al panel 
    let mesaJuegoAcabado=document.getElementById('mesaJuegoAcabado');
    mesaJuegoAcabado.classList.add('mesaJuegoAcabadoColor');
}


/**
 * Gira la carta cuando le clicas y es la base del mecanismo del juego
 * @date 2023-04-24
 * @param { * } event
 */
function girarCarta(event){
    contadorNumCartasGiradas+=1;
    carta=event.target;
    num=carta.id;
    arrayCartasGiradas.push(parseInt(num));
    if (combrobarSiCartasMismoCuadro()) { 
        carta.src="./img/cuadrosPintores/completaCuadros"+num+".png";
        if (comprobarSiCuadroEntero()) { //Cuadro entero            
            /*for(let ids of arrayCartasGiradas){
                let carta=document.getElementById(ids);
                carta.style.filter = "grayscale(100%)";
            }*/
            arrayCartasGiradas=[];
            ganar();
        }
    }else{        
        carta.src="./img/cuadrosPintores/completaCuadros"+num+".png";
        numFallos+=1;
        document.getElementById('fallos').value=numFallos;
        eliminarEventoClick();
        setTimeout(function() {
            arrayCartasGiradas=[];
            for(let ids of arrayCartasNoCompletadas){
                let carta=document.getElementById(ids);
                carta.src="./img/cuadrosPintores/dorsal.png";
            }
            añadirEventoClick();
            }, 1000);
    } 
}
/**
 * Comprobamos si las cartas giradas pertenecen al mismo cuadro aunque no este completo
 * @date 2023-04-24
 */
function combrobarSiCartasMismoCuadro() {
    for (let cuadro of arrayCuadros){
        let containsAll = arrayCartasGiradas.every(elem => cuadro.includes(elem));
        if (containsAll) {
            return true
        }
    }
}
/**
 * Comprobaos si las cartas giradas forman un cuadro entero y le quitamos el event litsener
 * @date 2023-04-24
 */
function comprobarSiCuadroEntero() {
    for (let cuadro of arrayCuadros){
        // Si los arrays tienen diferentes longitudes, no pueden tener los mismos elementos
        if (arrayCartasGiradas.length == cuadro.length) {
            // Comparamos cada elemento del primer array con los elementos del segundo array
            if(arrayCartasGiradas.every((elemento) => cuadro.includes(elemento))){
                for(let index of arrayCartasGiradas){
                    arrayCartasNoCompletadas=arrayCartasNoCompletadas.filter((elemento) => elemento !== index);//aqui sacamos los cuadros completos del array de cartas para girar
                    //no dejamos que sea clickable
                    let carta=document.getElementById(index);
                    carta.removeEventListener('click', girarCarta);
                }
                return true
            }
        }
    }   
}
/**
 * Comprueba si has ganado y lo muestra en pantalla
 * @date 2023-04-24
 */
function ganar() {
    if (arrayCartasNoCompletadas.length==0) {
        let cartas=document.getElementsByClassName('cartaImg');
        let cont=1
        for(let carta of cartas){
            carta.src="./img/cuadrosPintores/completaCuadros"+cont+".png"
            cont+=1;
        }
        //PUNTOS
        puntosEnPagina=document.getElementById('puntos');
        let puntosTenia=parseInt(puntosEnPagina.innerHTML);
        let puntos=0;
        console.log(puntos);
        if (numFallos<3) {
            puntos+=5;
        }else if(numFallos<6) {
            puntos+=4;
        }else if(numFallos<10) {
            puntos+=3;
        }else if(numFallos<15) {
            puntos+=2;
        }else {
            puntos+=1;
        }
        puntosEnPagina.innerHTML=(puntosTenia+puntos);
        localStorage.setItem('puntosUsuario', (puntosTenia+puntos));
        //mostrar pestaña JUEGO ACABADO
        let winAcabado=document.getElementById('winJuegoAcabado');
        winAcabado.innerText='HAS GANADO';
        let puntosJuegoAcabado=document.getElementById('puntosJuegoAcabado');
        puntosJuegoAcabado.innerText=puntos;
        //ocultar la pestaña de Juego Acabado
        let mesaJuegoAcabado=document.getElementById('mesaJuegoAcabado');
        mesaJuegoAcabado.style.zIndex=3
        mesaJuegoAcabado.classList.add('mesaJuegoAcabadoColor');
    }
}
/**
 * Añadimos el evento click a todas las cartas excepto las que esten ya completas
 * @date 2023-04-24
 */
function añadirEventoClick() {
    //Eventos del click
    for(let ids of arrayCartasNoCompletadas){
        let carta=document.getElementById(ids);
        carta.addEventListener('click', girarCarta);
    }
}
/**
 * Eliminamos el evento click a todas las cartas excepto las que esten ya completas
 * @date 2023-04-24
 */
function eliminarEventoClick() {
    //Eventos del click
    for(let ids of arrayCartasNoCompletadas){
        let carta=document.getElementById(ids);
        carta.removeEventListener('click', girarCarta);
    }
}
/**
 * Boton jugar y hace que empiecw el juego
 * @date 2023-04-24
 */
function empezarJuego() {
    //reinicimos todo
    pintarPanelJuego();
    let winAcabado=document.getElementById('winJuegoAcabado');
    winAcabado.innerHTML='LISTO PARA JUGAR';
    let puntosJuegoAcabado=document.getElementById('puntosJuegoAcabado');
    puntosJuegoAcabado.innerText=0;
    //ocultar la pestaña de Juego Acabado
    let mesaJuegoAcabado=document.getElementById('mesaJuegoAcabado');
    mesaJuegoAcabado.style.zIndex=1;
    mesaJuegoAcabado.classList.remove('mesaJuegoAcabadoColor');
    //enseñar cartas
    let cartas=document.getElementsByClassName('cartaImg')
    let cont=0
    for(let carta of cartas){
        carta.src="./img/cuadrosPintores/completaCuadros"+arrayCartas[cont]+".png";
        cont+=1
    }
    //ocultar cartas y empezar
    setTimeout(function() {
        for(let carta of cartas){
            carta.src="./img/cuadrosPintores/dorsal.png";
        }
        añadirEventoClick();
        }, 3500);
}
/**
 * Carga de objetos del DOM comprovaciones y eventos del formulario
 * @date 2023-04-15
 */
function domCargado(){
    //puntos
    regularizarPuntos()
    //pintamos el panel del juego
    pintarPanelJuego();
    jugar=document.getElementById('contenedorJugar');
    jugar.addEventListener('click', empezarJuego);
    jugarAcabado=document.getElementById('contenedorJuegoAcabado');
    jugarAcabado.addEventListener('click', empezarJuego);
}


//Inicio de carga evento
document.addEventListener('DOMContentLoaded', domCargado);