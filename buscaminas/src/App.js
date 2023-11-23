import logo from './logo.svg';
import { useState } from 'react';
import './App.css';
import Celda from './Celda';
import Tiempo from './Tiempo';

function App() {
  //Valores
  const valores=["1","1","1","0","0","1","*","1","0","0","1","1","2","2","1","0","1","*","*","1","0","1","2","2","1"];
  //Definir state
  const [mapaValores,setMapaValores]=useState(Array(25).fill(" "));
  //State cara BF-23
  const [emotiCara,setEmpotiCara]=useState("acierto.png")
  //State ejecutando BF-23
  const [ejecutando,setEjecutando]=useState(true)

  const celdas=mapaValores.map((item,index)=>
    <div className="col-auto p-0" key={index}><Celda valor={item} onCeldaClick={() => mostrarValor(index)}/></div>
  );

  //Funcion respuesta al BTN
  const btnComenzar = ()=>{
    setMapaValores(Array(25).fill(" "));
    //COMIENZO PARTIDA BF 2023
    setEmpotiCara("acierto.png");
    setEjecutando(true)
  }

  //Funcion que cambia el valor de una celda
  const mostrarValor = (index)=>{
    const valoresNuevos = mapaValores.slice();
    valoresNuevos[index] = valores[index];
    //LOGICA BOMBA //BF 2023
    if(valores[index]!=="*"){
      //LOGICA DESTAPA VALORES ALREDEDOR  //BF 2023
          if(valores[index]==="0"){
            //buscamos en la casilla de la izquierda siempre que no esté en col izquierda
            if(index%5>0) if(valores[index-1]==="0") valoresNuevos[index-1] = valores[index-1];
            //buscamos en la casilla de la derecha siempre que no esté en col derecha
            if((index+1)%5!==0) if(valores[index+1]==="0") valoresNuevos[index+1] = valores[index+1];
            //buscamos en la casilla de arriba siempre que no esté en fil promera
            if((index)>4) if(valores[index-5]==="0") valoresNuevos[index-5] = valores[index-5];
            //buscamos en la casilla de abajo siempre que no esté en fil ultima
            if((index)<20) if(valores[index+5]==="0") valoresNuevos[index+5] = valores[index+5];
          }
      //LOGICA DESTAPA VALORES ALREDEDOR
      }else{
          //FIN PARTIDA BF 2023
          setEmpotiCara("fallo.png");
          setEjecutando(false)
      }
    //LOGICA BOMBA //BF 2023
    setMapaValores(valoresNuevos);
  }


  return (
    <div className="container text-center" style={{ width: 340 }}>
      <div className="grid bg-body-secondary py-2 px-4 borderOutSide m-0">
        <div className="row bg-body-secondary borderInside ">
          <div className="d-flex flex-wrap justify-content-around">
            <div className="lcdText text-danger pe-2 m-2 borderInsideS">10</div>
            <div className="align-self-center m-2 borderInsideS">
              <img src={emotiCara} style={{ width: 50 }} />
            </div>
            <Tiempo ejecutando={ejecutando}/>
          </div>
        </div>
        <div className="row borderInside bg-body-secondary text-center justify-content-center">
          <div className="col my- p-0">
            <div className="d-flex flex-wrap justify-content-center">
              {celdas}
            </div>
          </div>
        </div>
      </div>
      <div><button className="btn btn-outline-secondary mt-2" onClick={btnComenzar}>COMIENZA LA PARTIDA</button></div>
    </div>
    
  );
}

export default App;
