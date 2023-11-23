import { useState, useEffect } from 'react';

export default function Tiempo({ejecutando}){
    const [seconds, setSeconds] = useState(0);

    useEffect(() => {
        //BF23 comprobar si temporizador está ejecutando
        if(ejecutando){
            //Monta el temporizador
            const idTemporizador = setInterval(
                ()=>{setSeconds(seconds=>seconds+1)}
                ,1000
            )
            
            //Desmonta el Temporizador
            return () => {
                clearInterval(idTemporizador);
            };
        }else{
            setSeconds(0)
        }
    });

    return(
        <div className='lcdText text-danger pe-2 m-2 borderInsideS' style={{width:54}}>{seconds}</div>
    );
}