"""
El camino samurai
"""
import random

print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢗⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢶⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⡇⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⢸⠀⣸⣧⡀⠀⠀⠀⠀⠀⠀⢀⣠⣧⡀⢇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⣾⠾⠛⣹⠿⠃⠀⠀⠀⠀⠀⠻⢏⡛⠻⣿⡀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⡞⠁⢠⠊⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠉⢆⠀⠳⡀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⡘⠀⢰⠃⠀⣀⣴⣿⣭⣀⣀⣬⣽⣶⣄⡀⠀⢃⠀⠱⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡇⠀⡇⠀⣷⣶⣿⠟⡿⠛⣻⣿⣿⣿⡛⢿⡻⢿⣷⣾⠀⠀⡇⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⡇⠀⢹⡚⢠⠊⣠⣮⡷⣿⣿⢴⣽⣆⠙⢆⠙⡾⠀⢀⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⠖⣲⣤⣧⡀⠹⣄⠀⠙⠧⣤⣧⣼⢦⣼⣮⡴⢿⣼⣦⠼⠛⠀⢀⠞⠀⣸⣥⡔⠒⣄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡰⠋⣾⣿⣿⣿⠳⣄⡈⠓⠦⢤⣌⣇⢹⣏⣽⢫⢈⣯⢩⣃⡤⠴⠚⢁⣠⡾⢿⣿⣿⣿⡌⢆⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⠼⠅⣀⣿⣿⣿⠟⠀⠘⣭⡿⠶⠦⠤⠽⠿⠯⢻⣿⠨⠿⠯⠤⠤⠶⢾⣯⠟⠀⠘⠿⢿⣟⣃⡠⠵⡄⠀⠀⠀
    ⠀⠀⠀⠘⠓⠲⢤⣌⠓⢄⠀⠀⠀⢹⡀EL CAMINO SAMURAI⠀⣹⠀⠀⠀⢀⠔⢉⣤⠶⠞⠛⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢸⣷⡈⢢⠀⠀⡾⢿⣶⣤⣄⣠⣤⣤⣤⣤⣤⣤⣤⣄⣶⣶⡾⢿⡄⠀⠰⠁⣴⣿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢠⣋⡩⢷⠈⡆⣸⢡⣶⣿⣿⣿⣿⣿⣿⠉⠉⢿⣿⣿⣿⣿⣿⣷⡄⣳⠀⡇⣼⠍⣙⣆⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢠⣏⠡⠤⢾⡇⣿⠻⣾⣟⢿⣿⣿⣿⣿⣿⡄⢠⣼⣿⣿⣿⣿⡿⣿⣣⠟⢿⢠⡿⠤⠤⣙⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⠎⢀⣀⡠⠞⣧⠇⢀⠈⠁⠀⠙⠛⠛⣁⣾⣿⣧⢻⣎⡙⠛⠋⠁⠈⠁⢀⠈⣾⡓⠤⣀⡀⠙⡄⠀⠀⠀⠀
    ⠀⠀⠀⢀⠞⠋⠉⠀⣀⣼⣿⣷⣜⣷⣶⣤⣄⡘⢻⠋⣼⣿⣿⣷⡍⡿⢋⣠⣤⣴⣾⣫⣴⣿⣷⣄⡀⠈⠙⠛⢄⠀⠀⠀
    ⠀⠀⣠⠿⠒⠚⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠈⠀⠈⠁⠈⠉⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠑⠒⠮⣆⠀⠀
    ⠀⡼⢁⣀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⢤⣤⡤⠤⣤⡤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⢣⡀
    ⣼⠛⠉⠀⠀⠉⠙⠛⠻⠿⠿⠿⣿⣿⣿⠀⣿⣿⣿⣘⣀⣀⣀⣥⣅⣿⣿⣿⠇⣿⣿⣿⠿⠿⠿⠿⠛⠋⠉⠁⠀⠈⠙⣷
    ⠘⠷⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⡘⣿⡾⠿⣿⡉⢉⣯⡿⠗⣿⠏⣴⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠋
    ⠀⠀⠀⠀⠉⠉⠓⠒⠒⠢⠤⠤⠤⢄⣈⣿⣷⣌⠻⡗⠂⠀⠂⠀⠻⠟⣫⣾⣿⣋⣀⡤⠤⠤⠤⠒⠒⠒⠉⠉⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠦⠴⠶⠤⠾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    Bienvenido al Juego del Camino samurai, en esta misión  tendrás que 
    derrotar a una antigua criatura que amenaza con destruir toda tu aldea,
    para eso tendras que utilizar tus habilidades magicas y marciales para poder
    cumplir esta tarea
""")

print("    Deberas escojer cual sera tu elemento mágico\n"
      "    Esto será fundamental a la hora de combatir\n"
      "    A) Fuego 🔥" "    B) Viento 💨" "    C) Tierra 🗻" "    D) Agua 🌊\n"
      "   ------------------------------------------------------------"
      )

"""Le pedimos al usuario que escoja su elemento y almacenamos la opcion en la variable elemento_magico y el elemento 
en la variable tipo_samurai"""

elemento_magico = input("Selecciona tu elemento mágico: ")

if elemento_magico.lower() == "a":
    print("Eres un samurai de fuego 🔥")
    print("Tus habilidades son:\n"
          """
    - Control de Llamas: Pueden convocar y manipular llamas con precisión, lo que les permite lanzar bolas de fuego o 
    crear barreras ardientes para defenderse. 
    - Espada de Fuego: Infunden sus armas con fuego, haciéndolas extremadamente letales y capaces de cortar a través de 
    casi cualquier cosa.
    - Visión de Llama: Tienen la capacidad de ver las emociones y la intención de las personas a través del fuego, 
    lo que les permite anticipar los movimientos de sus oponentes.
    
    """)
    tipo_samurai = "fuego"

elif elemento_magico.lower() == "b":
    print("Eres un samurai de Viento 💨")
    print("Tus habilidades son:\n"
          """
    - Vuelo: Pueden manipular las corrientes de aire para elevarse y volar, lo que les brinda una ventaja estratégica en 
    el campo de batalla.
    - Ráfaga de Viento: Pueden crear poderosas ráfagas de viento que pueden repeler a los enemigos o desviar ataques.
    - Evasión Increíble: Su agilidad y capacidad para manipular el aire los hacen extremadamente evasivos, 
    permitiéndoles esquivar los ataques con facilidad.
    
          """)
    tipo_samurai = "viento"

elif elemento_magico.lower() == "c":
    print("Eres un samurai de Tierra 🗻")
    print("Tus habilidades son:\n"
          """
    - Manipulación de la Tierra: Los samuráis que controlan la magia de la tierra pueden moldear el suelo a su voluntad, 
    creando muros y barreras defensivas sólidas o levantando pilares de roca para atacar a sus enemigos.
    - Conexión Tierra: Pueden sentir y comunicarse con la tierra misma, permitiéndoles moverse silenciosamente, 
    detectar trampas y sentir los movimientos de sus enemigos a través de las vibraciones del suelo.
    - Piedra Protectora: Pueden invocar una armadura de piedra que les brinda una gran resistencia física y los hace 
    virtualmente invulnerables a ataques físicos.
    
          """)
    tipo_samurai = "tierra"

elif elemento_magico.lower() == "d":
    print("Eres un samurai de Agua 🌊")
    print("Tus habilidades son:\n"
          """
    - Manipulación del Agua: Los samuráis del elemento agua pueden controlar y dar forma al agua, creando torrentes, 
    olas o incluso armas de agua letales.
    - Curación Acuática: Tienen la capacidad de sanar heridas tanto propias como de otros utilizando el agua, acelerando 
    el proceso de curación y aliviando el dolor.
    - Camino del Espejismo: Pueden crear ilusiones acuáticas para confundir a sus enemigos o camuflarse en su entorno, 
    haciéndolos prácticamente invisibles.
    
          """)
    tipo_samurai = "agua"
else:
    print("Eres un samurai de sin elemento mágico, solo cuentas con habilidades físicas normales\n")
    tipo_samurai = "ninguno"

print("-----------------------------------------------------------------------")
print("×º°”˜`”°º× ▌│█║▌║▌║ ꧁乇爪卩丨乇乙卂 ㄥ卂 爪丨丂丨Ó几꧂ ║▌║▌║█│▌ ×º°”˜`”°º×")
print("-----------------------------------------------------------------------")

print("""

    En los albores de un antiguo pueblo samurái, en un rincón remoto de Japón, la paz y la serenidad que habían 
    reinado durante generaciones se vieron amenazadas por una presencia oscura y ancestral. Una criatura mágica, 
    nacida de pesadillas y leyendas olvidadas, emergió de las sombras, sumiendo a la aldea en un estado de temor y 
    desesperación.
    
    En medio de esta crisis, se alza un samurái valiente y decidido: Takeshi, un guerrero de renombre conocido por su 
    destreza en la espada y su profundo vínculo con la magia de los elementos. Con su armadura reluciente y sus 
    habilidades mágicas, Takeshi se convierte en la última esperanza de su pueblo. Jurando proteger a su gente y 
    restaurar la paz que tanto aman, Takeshi emprende un viaje hacia lo desconocido, decidido a enfrentar la criatura 
    mágica y poner fin a la amenaza que se cierne sobre su aldea. La batalla que se avecina será una prueba de coraje, 
    habilidad y magia como nunca antes se ha visto en esta tierra ancestral.
 
""")

print("""
⠀ ⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣠⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣀⠀⠀⠀⣀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠁⠀⠀⠀⠀ ⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠂⠀⠀⠀⠀⠀⠀⠀ ⢹⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⢳⣦⣄⡀⠀⠀⠀⠀⢸⣿⣤⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠉⠀⠀⠀⠀⠻⣼⠹⣗⢦⣄⣰⣿⣿⣿⣥⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⣤⠴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠹⣗⠮⣭⡟⢱⣿⣿⣿⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠁⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⣆⠀⠹⣿⡿⢀⣾⣿⣿⣿⣛⡷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣏⡁⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠘⠁⠀⣿⣄⡴⠋⢀⣼⣿⢤⣬⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠓⠶⢤⣄⣀⣘⠃⠀⠀⠀⢺⠁⠀⡾⠋⠀⣠⣿⣿⣿⣿⣿⣿⡿⠃⠀⣴⣶⣶⣷⠶⠶⠀⠀⠀⠀⠀⠀⢀⢢⣔⣱⣮⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠉⢿⣿⣿⣿⣶⣶⠏⠀⢀⣾⣿⣿⣿⣿⣿⣿⣇⢀⣀⣰⣿⣿⡏⠉⠀⠀⠀⠀⠀⠀⢀⠸⣎⣷⣿⣿⣷⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣿⣿⣿⣾⣿⢿⡿⠛⠁⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⡟⠛⠛⠁⠀⠀⣀⣴⣣⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡿⠛⠉⡴⠋⠀⢀⡴⣻⣽⣿⣿⣿⣿⣿⣿⡛⠟⠿⢻⣿⣿⡛⠁⣽⡄⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡟⠀⠀⠈⠀⢀⡴⢯⣳⣿⡿⠷⣿⣿⣿⣿⣬⣟⣛⠛⡋⢸⣿⣿⣷⣞⣷⣾⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡟⠀⠀⣀⣀⡴⣏⣼⣿⣿⣿⣦⣤⣸⣿⣿⣿⣿⣿⠮⣍⣉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⡇⣠⣟⣯⣵⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⣤⡴⣖⡷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⢀⣀⡤⣴⡶⣿⣿⣽⣷⣿⡿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣠⣤⣤⣤⣼⣿⣻⣿⣿⣿⣿⡿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣇⠘⢧⡘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣾⣿⣿⣻⣿⣿⣯⣿⣟⣿⣿⡿⣟⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⢚⣇⠈⠱⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣳⢯⣷⢿⣟⣿⣿⣽⣿⢿⣿⣻⣿⣿⣿⢿⣻⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣭⠾⣆⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡽⣟⣯⣿⣞⡿⣞⣯⢿⣻⡽⣟⣷⢿⡾⣿⣟⣯⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
""")

print("""

    Takeshi avanzó con cautela por el oscuro bosque, guiado por el eco de los susurros de la criatura mágica. La luna llena 
    brillaba en el cielo, arrojando una tenue luz sobre los árboles retorcidos. Finalmente, llegó a un claro donde una 
    gigantesca figura acechaba entre las sombras. Era la bestia, una criatura de pesadilla con ojos centelleantes y 
    colmillos afilados. La tierra temblaba bajo sus pesadas pisadas, y un viento helado soplaba desde su dirección
""")
print("""
    Opción A: Atacar directamente
    Opción B: Intentar razonar
    Opción C: Buscar una ruta de escape
""")

opcion = input("¿Qué decides hacer?: ")

if opcion.lower() == "a":
    print("""
    
    Takeshi decidió no perder tiempo y desenfundó su espada mágica. Con una resuelta determinación, avanzó hacia la 
    bestia, decidido a enfrentarla directamente y poner fin a la amenaza de una vez por todas. La batalla que se 
    avecina será una prueba de sus habilidades de combate y su magia elemental.
    """)
    print(f"""
    Opción A: Usar la magia de {tipo_samurai} 
    Opción B: Atacar sin usar mágia
    Opción C: Buscar ayuda de los aldeanos
    """)
    opcion = input("¿Qué decides hacer?: ")
    if opcion.lower() == "a":

        if tipo_samurai == "fuego":
            print("""
            Takeshi lanza bola de Fuego contra la bestia pero esto no parece afecatarle
            La bestia absorbe el ataque y y se lo regresa a Takeshi y este muere
                           
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
            """)
            exit()

        elif tipo_samurai == "viento":
            print("""
            Takeshi lanza una rafaga de viento contra la bestia pero esto no parece afecatarle
            La bestia absorbe el ataque y y se lo regresa a Takeshi y este muere
                   
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
                   """)
            exit()

        elif tipo_samurai == "tierra":
            print("""
            Takeshi lanza una roca gigante contra la bestia pero esto no parece afecatarle
            La bestia absorbe el ataque y y se lo regresa a Takeshi y este muere
    
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
                   """)
            exit()

        elif tipo_samurai == "agua":
            print("""
            Takeshi lanza una ola gigante contra la bestia pero esto no parece afecatarle
            La bestia absorbe el ataque y y se lo regresa a Takeshi y este muere
    
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
                   """)
            exit()

        else:
            print("""
            No Tienes poder Elemental, asi que la bestia te derrota fácilmente y mueres
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
            """)
            exit()

    elif opcion.lower() == "b":
        print("""
        Takeshi elige luchar en solitario sin la ayuda de la magia elemental. Este es derrotado por la bestia y muere
                                 ⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
                    
        """)
        exit()

    elif opcion.lower() == "c":
        print("""
        Takeshi, en medio de la batalla, se da cuenta de que no puede vencer a la criatura mágica solo. Decide buscar la 
        ayuda de los aldeanos, quienes se reúnen con él en el claro del bosque. Juntos, los samuráis y los aldeanos 
        intentan derrotar a la bestia en un asalto conjunto. """)

        print("""
        Opción A: Formar una barricada defensiva
        Opción B: Emboscar a la bestia
        Opción C: Invocar la magia de los elementos en conjunto
        """)
        opcion = input("¿Qué decides hacer?: ")

        if opcion == "a":
            print("""
            Los aldeanos, siguiendo las indicaciones de Takeshi, utilizan su conocimiento de la tierra y la madera para 
            construir una barricada defensiva alrededor de la bestia, pero la bestia se percata de lo que hacen y los 
            ataca, todos mueren

                                 ⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
            """)
            exit()

        elif opcion == "b":
            print("""
            Takeshi y los aldeanos preparan una emboscada astuta. Algunos de los aldeanos se esconden en los árboles, 
            mientras Takeshi y el resto atraen la atención de la bestia. Cuando la criatura se adentra en el claro, 
            los aldeanos emboscados atacan desde todas las direcciones, pero la bestia logra repeler el ataque y 
            derrotarlos, todos mueren

                                         ⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                                ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                                ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                                ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                                ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
                    """)
            exit()

        elif opcion == "c":
            print("""
            Takeshi y los aldeanos se unen en un círculo mágico y canalizan la magia de los elementos de manera 
            coordinada. Crean una tormenta de elementos que rodea a la bestia, debilitándola y disminuyendo su poder.
            Ahora Takeshi debe acumular la magia de todos para poder usar el poder de los cuatro elementos y derrotar 
            a la bestia, para eso debe multiplicar la cantidad de personas presentes por la distancia de la bestia y 
            dividirlo por la cantidad de elementos magicos para obtener el número de invocación 
            """)
            cantidad_personas = random.randint(1, 10)
            distancia_bestia = random.randint(1, 10)
            cantidad_de_elementos = 4
            print(f"""
            La cantidad de personas es {cantidad_personas}
            La distancia de la bestia es de {distancia_bestia}
            La cantidad de elementos es de {cantidad_de_elementos}
            """)
            numero_invocacion = (cantidad_personas * distancia_bestia) / cantidad_de_elementos

            print(f""" 
            El número de invocación es 31
            El número de invocación es 100
            El número de invocación es {numero_invocacion}
            """)
            opcion = float(input("¿Cuál es el número?: "))

            if opcion == float(numero_invocacion):
                print("""
                Ya tienes el número de invocación, para poder usar los cuatro elementos debes usar un arma mágica 
                que pueda controlar el poder sin romperse, y tambien una armadura que proteja a Takeshi.
                Puedes Usar la siguientes armas: 
                Opción A: Lanza
                Opción B: Cuchillo kunai
                Opción C: katana
                """)
                opcion = input("¿Qué decides hacer?: ")

                if opcion.lower() == "a":
                    print("Escojiste la lanza")
                    arma_correcta = False
                elif opcion.lower() == "b":
                    print("Escojiste el cuchillo kunai")
                    arma_correcta = False
                elif opcion.lower() == "c":
                    print("Escojiste la katana")
                    arma_correcta = True
                else:
                    print("No escojiste ninguna arma")
                    arma_correcta = False

                print("""
                Puedes Usar la siguientes armaduras: 
                Opción A: La armadura león
                Opción B: La armadura tigre
                Opción C: La armadura dragón 
                """)
                opcion = input("¿Qué decides hacer?: ")

                if opcion.lower() == "a":
                    print("Escojiste armadura león")
                    armadura_correcta = False
                elif opcion.lower() == "b":
                    print("Escojiste la armadura tigre")
                    armadura_correcta = False
                elif opcion.lower() == "c":
                    print("Escojiste la armadura dragón")
                    armadura_correcta = True
                else:
                    print("No escojiste ninguna armadura")
                    arma_correcta = False

                if arma_correcta == True and armadura_correcta == True:
                    print("""
                    La armadura y el arma son las indicadas logras usar el poder de los cuatro elementos.
                    La espada mágica de Takeshi brilla con intensidad y, con un golpe certero, corta profundamente a la 
                    bestia.
                    La criatura mágica se retuerce en agonía antes de desvanecerse en la nada. El claro del bosque 
                    recupera su tranquilidad, y la aldea está a salvo una vez más. Takeshi y los aldeanos se reúnen, 
                    exhaustos pero triunfantes, habiendo demostrado que juntos pueden superar cualquier desafío.
                    La paz y la gratitud llenan el corazón de los habitantes del pueblo mientras Takeshi y los aldeanos 
                    celebran su victoria. Takeshi se ha convertido en una leyenda en su tierra, no solo como un samurái 
                    valiente, sino como un líder que supo unir a su comunidad en tiempos de necesidad.
                    
                   ⢸⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢠⡇⢀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⡇⣼⢃⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⣸⠁⣿⣸⣿⡿⠀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠐⣎⣿⣿⣰⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⢋⣶⣶⣶⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣶⣤⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡇⣿⣿⣿⠿⣛⣩⣭⣭⣭⣭⣉⣙⡛⣋⣩⣥⣴⣶⣶⣶⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠇⣾⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⣛⡛⠛⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠁⠚⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣡⣴⣾⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣏⣼⣿⣿⣿⣿⣿⣯⣍⣛⠿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⠏⢻⣿⣿⣿⣿⣿⣿⣿⠿⠛⢛⣛⠛⠻⠿⣷⣤⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣶⣷⣦⣝⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣍⣝⡛⠿⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢰⡿⣫⣿⣿⣿⡟⣿⣿⡇⢸⣿⣿⣿⣿⠿⢿⣿⣷⣦⣌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣇⣡⢾⣿⣿⣿⡟⣸⣿⣿⡇⢸⣿⣿⣿⣿⣿⣷⣦⣌⡙⠛⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⢋⣵⣿⣿⣿⣿⢡⣿⣿⣿⠃⢸⣿⣿⣿⣿⣤⣬⣙⡛⠿⢷⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣶⣿⣿⣿⣿⣿⠇⣘⣩⣿⣿⠀⢸⣿⣿⣿⣿⡛⡻⠿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣵⣾⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣷⣦⣌⡙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠿⠟⠛⠻⢿⣿⣿⣿⣿⠀⢾⣿⣿⣿⣿⣴⣮⣍⡛⠻⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠿⠛⠉⣠⣴⣾⠟⣃⣤⠙⣿⣿⣿⡀⠻⠿⢿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⡿⢛⣩⣴⣿⣿⣿⣧⠘⣿⣿⣿⣶⣦⣤⣄⣀⣈⠉⠙⠻⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠙⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⡛⢁⣼⣿⣿⣿⡿⠟⣋⣵⣿⣿⡇⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⢠⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣾⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣼⡟⣿⣿⣿⣿⣿⡿⠟⣠⣿⣿⣿⣿⣿⣿⣿⣟⢻⡉⣛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠉⠀⠈⠁⠉⠙⠉⠀⠀⠉⠉⠉⢛⠛⠛⠿⠿⠿⢠⢇⣿⣿⣿⣿⣿⣿⡿⢋⣉⣉⠛⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣡⣴⣿⣿⣿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣭⣭⣿⣿⣿⣿⠿⢿⣿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⣿⣟⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠉⠙⠛⠿⣿⣿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⣡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣙⣋⣭⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣿⣶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣸⡟⠰⠿⠿⠿⠿⠿⣿⢿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢠⣿⢣⣿⣿⣿⣶⣶⣶⣶⣾⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⡸⠿⠿⠿⢿⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢿⣿⣿⣷⣦⣀⠀
            ⠀⠀⠀⠀⠀⠀⣾⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣼⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⠧
            ⠀⠀⠀⠀⠀⠀⣿⡇⠾⢿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢠⣿⠇⣶⣶⣶⣶⣶⣶⣦⣼⣿⣿⣿⡟⢠⣿⣿⣿⣿⣿⣿⣿⡇⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣥⣾⣿⣿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⠿⠿⠿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢼⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    """)
                    print("-----------------------------------------------------------------------")
                    print("×º°”˜`”°º× ▌│█║▌║▌║ ꧁千丨几 ᗪ乇 ㄥ卂 爪丨丂丨Ó几꧂ ║▌║▌║█│▌ ×º°”˜`”°º×")
                    print("-----------------------------------------------------------------------")

                else:
                    print("""La armadura o el arma no son las indicadas para logras usar el poder de los cuatro 
                    elementos, la bestia se libera ataca a todos y mueren
                    
                                         ⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                                ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                                ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                                ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                                ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇ 
                    
                    """)
                    exit()



            else:
                print("""
                No lograste obtener el número de invocación, la bestia se libera de la tormenta y mata a todos
                
                                         ⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                                ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                                ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                                ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                                ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
                """)
                exit()

elif opcion.lower() == "b":
    print("""
    Takeshi, recordando las viejas leyendas de su abuelo, decidió intentar un enfoque más pacífico. Se acercó a la 
    bestia con las manos abiertas y habló en un lenguaje antiguo. La criatura pareció entender y bajó la guardia 
    momentáneamente. Esto hizo que takeshi se confiara muriera y que la bestia lo ataque desprevenido y muera

                                 ⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
    """)
    exit()

elif opcion.lower() == "c":
    print("""
    Al ver el inmenso tamaño y la ferocidad de la bestia, Takeshi decidió que era una batalla que no podía ganar 
    directamente.Optó por buscar una ruta de escape, pero en lo que iba escapando la bestia lo atacó y murió

                                 ⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                        ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                        ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                        ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                        ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
    """)
    exit()

else:
    print("""
        No haces nada asi que mueres

                                     ⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⡏⡆⠀
                            ⠀⠀⠀⠀⠀⠀⠀⣠⣾⠿⠛⠋⠉⠉⠉⠈⠉⠛⠛⢳⡇⠀
                            ⠀⠀⠀⠀⠀⢀⠞⠋⠀⠀⣷⣤⣀⣀⣀⠀⠀⠀⠀⠸⡇⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣢⠄⠀⠀⡇⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⡀⠀⠀⡇⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⣀⣇⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣧⣴⣾⣻⡆
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡇
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣭⣾⣿⣿⣿⠉⣛⢿⠿⠁
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⣶⣿⣻⣿⣆⠙⣿⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⡿⣸⣔⣿⣿⡄⣿⠀⠀
                            ⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⡏⠀⠀
                            ⠐⠶⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠇
        """)
