import readchar
import os
import random
import time

# Map base
map_definition = """\
GGGGDWGGGGGGGGGGGGGGGGGGGDDDMrrrIEEEEEPEEPEEPEEPEEPEEPEEPEEPEEPEEPEEPEEPEEPE
GGGGDWGGGGGGGGGGGGGGGGGGGDDDwrFrwEEEEMEIMEIMEIMEIMEIMEIMEIMEIMEIMEIMEIMEIMEI
GGGGDFFFFFFFFFFFFFFFFFFFFDDDrrrrrEEEMEEEIEMEEEIEMEEEIEMEEEIEMEEEIEMEEEIEMEEE
GGGGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDEEMEEEEEMEEEEEMEEEEEMEEEEEMEEEEEMEEEEEMEEEE
GGGGDWFFFFFFFFFFFFFFFFFFFFFFFDDDDEMEEEEEMEEEEEMEEEEEMEEEEEMEEEEEMEEEEEMEEEEE
GGGGDWGGGGGGGGGGGGGGGGGGGGGGGDDDDDDDDWDDDDDDDMrrrIDGGGGOOOOOOOOOOOOOOOOOOOOO
GGGGDWGGGGGGGGGGGGGGGGGGGGGLGDDDDDDDDWDDDDDDDwrFrwDGGGGOOOOOOOOOOOOOOOOOOOOO
HHHHDHHHHHHHHHHHHHHHHHHHHHHGGGGGGGGDDWDDDDDDDrrrrrDGGGGOOOOOOOOOOOOOOOOOOOOO
DDDDDDDDDDDDDDDDDDMrrrIGGGHGGGGGGGGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
DDDDDDDDDDDDDDDDDDwrFrwGGGHGGGGGGGGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDPDDDDDPDDDD
DPDDPDDPDDPDDDDDDDrrrrrGGGHGGGGGGGGDDWFFFFFFFFFFFFFFFFFFFFDDDDDDMEIDPDMEIDPD
MEIMEIMEIMEIDDDDDDDDDDDDDDHGGGGGGGGDDWGGGGGGGGGGGGGGGGGGGGDDDDDDDKDMEIDKDMEI
DKDDKDDKDDKDDDDDDLDDDDDDDDHGGGGGGGGDDWGGGGGGGGGGGGGGGGGGGGDDDDDDDDDDKDDDDDKD
OOOOOOOOOOOOOOODDOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOODDOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOODDOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOODDOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOODDOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOODDOOOOOOOOOOOOOOOO
EPEEPEEMrrrIDDDDDDDDDDDDDDDDDDDDDDDDDDDMrrrIGGHDDDDDDDDPDDDDDDDDDDMrrrIGGGGG
MEIMEIEwrFrwDDDDDDDDDDDDDDDDDDDDDDDDDDDwrFrwGGHDDPDDDDMEIDDDDDDDDDwrFrwGGGGG
EEMEEEIrrrrrDDDDDDDDDDDDDDWFFFFFFFFFDDDrrrrrGGHDMEIDDPDKDDPDDDDDDDrrrrrGGGGG
EMEEEEEIGGGGDDDDDDDDDDDDDDWGGGGGGGGGDDGGGGGGGGHDDKDDMEIDDMEIDDDDDDGGGGGGGGGG
MEEEEEEEIGGGDDDDDDDDDDDDDDWGGGGGGGGGDDGGGGGGGGHDDDDDDKDDDDKDDDDDDDGGGGGGGGGG\
"""
map_definition = [list(row) for row in map_definition.split("\n")]

# Pokemon picture

meltan = ("""
        ▓▓▓▓███               
      █▓▒▒▒▒▒▒▒▒▒▒▓█          
    █▓▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▓        
  █▓▒▒▒▓▓▓██████▓▓▒▒▒▒█       
 ▓▒▒▒▓▓▓█        ██▓▒▒▒█      
 ▓▒▒▒▓██   ███     ▓▒▒▒▓      
 ▓▒▒▒▓██  █▓▓███   ▓▒▒▒▒█     
 █▓▒▒▓██  █████    ▓▒▒▒▒██    
  █▒▒▓▓█          ▓▒▒▒▓██     
   ▓▒▒▒▓▓█     █▓▒▒▒▓▓█       
    ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓█         
    █▒▒▒▒▓▓▓▒▒▒▒▓▓█           
  █▒▒▓▒▒▒▒░░░▒▒▒▒▓            
 █▓▓▓▒▓▒▒░░▒▒▒▒▒▓▓▒▓  ██▓█    
    ▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓▓█▓▓█  
   █▒▒▒▒▒▒▒▒▒▒▒▒▓▒█      ████ 
  █▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓█          
   █▓▒▒▒▓▓▓▓▒▒▒▒▓▓█                  
""")
vaporeon = ("""
                                ▓▓▓██                         
                            ▓▓▒▒▒▒▒▓▓▓███                     
                          ▓▒▒▒▒▓█▓▓▒▓▓▓▓▓███                  
                        ▓▓▒▒▒▓█▓▓▒▓██   ██▓▓▓██               
                     ▓▓▒▒▒▒▒▓▓▓▒▓█        ██▓▓▓▓▓█            
                  █▓▒▒▒░░░▒▒▓▓▓▓█        █▒▒▒▒▒▒▒▒▓█          
              ██▓█▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█      ▓▒▒▒▒▒▓▓▒▒▒▒█         
              █▓▒▓▒▒▒▓▓▒▒▒▒▒▒▒▓▓▒█     ▓▓▒▒▒▒▓███▒▒▒▓█        
              █▒▒▓▒▒▒▓░▓█▒▒▒▒▒▓█▓▓█    ▓▓▒▒▒▓█   ██▓▓██       
             ▓▒▒▒█▓▒▒▒▒░▒█▒▒▒▓▓██▓▒█   █████                  
             ▓▒▒█  █▓▓▒▒░▒▓░ ▓▓▒░▓▒▒██                        
            █▓▓▓█  ▒▒▓▒░▒▒▓▓█▓▒▒▓▒ ░▓█                        
             ███  ▓░▒▒░░▓▒▓▓▓▓▓██▓▒░▒█                        
                   █░ ▒█░░▓████████░  █                       
                  ▓▒░▒▓▒░░░░▒▒▒▒▓██▓▓▓▓▓▓▓▓▓██                
                 ▒▓▒░░▓▒▒░▒▒▓██▒▒▓▒▒▒▒░░░░▒▓                  
                 ███░ ▒▒██▒▒▒▒▒▒▒▒▒▒░░░▒██                    
               ▓▓▒▒▒░░░▓▒▓▓▓▓▓▓▓░░▒▒░░█                       
              ▓▒░░▓███▓▒░░▒░░░░░▒▒██▒█                        
              █▒▒▒▓█    █▒▒▒██▓▒▒▓█                           
              ███▒▓     ███  ▓▓▓▓▓█                           
                              █▒▒▒▒█                          
                               █▒▒▒█                          
                               █▓▒▓▓█                         
                                 ███                                                                                                                                                         
""")
forretress = ("""                        
                               ░▒▒░░                                
                         ▒▒▒▒▒▓██▓█▓▓▒▓▓▒▒                          
                       ░▓███████▓▓████▓▓▓▓▓▒                        
                    ▒▓▓█████████████▓▓██████▓▒▒                     
                  ▒▓███▓███████████████████████▒▒                   
                  ▒████████████████████████▓████▓▒                  
                 ▒▓██▓▓▓▓█████▓▓███▓██████▓▓▓▓███▓▒                 
                 ▒██▓▓░░▒████▓▓░░░░█▓████▒░░▓▓▓██▓▒                 
              ░░▒▒▒▓▓▒░░░▒▓▓▓▒▒░░░░▒▓▓▓▓▒▒▒░░▒█▓▓▒▓▒                
        ▒▒▒▒▒▒▒▒▒▒▒▒▒░▒█░░▒▒▒▒░░▓█░░░▒▒▒░▒▒▒▒▒▒░░░▒░▒▒░░            
        ▒░▒▒▒▒▒▒▒▒▒░░▒▒░▓░░░░░░█░░▓▒░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒░▒          
         ░░░░░░░░░░▒▒░░▓░░░░░░░░██▒░░▒░░░░░░░░░░░░░░░░░░░           
                ░▓▓▓▓░░░░▒▓▓█▒▒░░░░░▓███▒░░░░░▓█▒▒▓░                
                 ▒▓█▓▓▒▒▒████▓▒▒░░░▓▓████▒░░▒█▓█▒▓▒                 
                  ▒▓▓▓▓▓▓██████▓▓▓▓██████▓██▓▓▓▓▓▒                  
                  ▒▒█▓█▓▓▓▓██████████████▓▓▓▓▓█▓▓▒                  
                    ▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▒                    
                     ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▒                       
                      ▒▓▓▓▓▒▒▓▓▓▓▓▓▓██▓▓▒▓▒░                        
                                ░▒▒▒▒▒                                                                                                                                              
""")
politoed = ("""                                  
                            ▓▓▓▓▓▓                                  
                           ▓▒█  █▓▓                                 
                           █▓██▓  █▒                                
                            ███   █▓█                               
                             ▒▒███ █▓█                              
                       ▓▓▓▒░░░░░░░▒▓▓█                              
                      ▒▓░░░░░░░░░██ ░▓█                             
                      █░░▒░▒░░░░▓███ ░▓█                            
                     █░░███▓░░░░░░▒█░░░▒█                           
               █▒░▒░███░░░░░░▒▒▓▓██▒░▓▒▒█  ▓▓                       
               █▒░▒░██ █▒░░░░░░░░░░▒▒▓░░▓█▓░░▓█                     
                ██░░░▓  ██▓▓▓▓▓▓▓▓▒▒░░░░░█░░█░░█                    
                 ██░░░░░░░▒░▒▒▒▒▒▒▒▒░▒▒░▒▓▒░░░█                     
                    █▒▒▒██░░░░░░░░░░░░▓░░░░░▓█                      
                         ▓░░░░░░░░░░░░░▓█░░██                       
                         █░░░░░░░░░░░▒░░░▓█                         
                       █▒▒▓░░░░░░░░▒▒░░░░▒█                         
                      ▓░░░▒▓▓░░░░░░▓░░░░░░▓█                        
                      █▒▒▒▒▒▒██▓▒▒▒██▒▒░▒▒▒█                        
                    ████▓▓▒▓▓        █▓▒▒▒█                         
                    █░░▓█▒▓██        ▓▒▒░▒▓▓                        
                     █████           █░░▒░▒░█                       
                                      ████                                                              
""")
primeape = ("""                          
                                  ▒ ▒▓▒                             
                      ▓▓█▓▒  ░░▒▒██▒███▒                            
                      ▒▓█▓█▒ ░██▒█▓██▓█▓░ ▒▒                        
           ▒▓▓▓▒▒      ▒█▓▓▓█▓▓███▓█▓▓▓█▒█▓▒▒▒                      
          ▓▓▓▓▓▒▒▒     ▒▓█▒██████████▓▒█▒███▓                       
         ▓▓▓▓▓▒▒▒░▒   ▒▓▒█████████████▓█████▓▓▓▒                    
         ▒▒▒▒▒▒░░░░▒░ ░░██████████████████████░                     
                 ▒▒▒▓▓▒█▒▓███▓█████▓████████▓▒▒▓▓▓▒                 
                  ░▒▒▓██▓█▒▓▓▒█▓▒▓████████▒▒▒▓▓▓▓▓▓░                
                      ▒██▓▒▒▒▓█▒██████████▒▒▒▒▓▓▓▓▓▒░               
                    ░▓███▒▒▓▒▓▒▓█████████▒▒░░░▒▒▒▒▒▒░               
                     ▒███▓▓▓▓▓▓██████████░▒▒▒░░░                    
                    ▒▒▒▓██████████████████▒░▒▓░                     
                     ░▒▓▓▓▓███████████▓░▒░▒█▓░░                     
                    ░▓▓▓▒░░███████████▓▒▒▓▒▒░                       
                    ░░▒▒░░░▒▒▒█▒▓█▓░▓░ ▒▒▓▓░░░                      
                    ░▒▒▒▒░        ▓      ░▒▒▒▒░                     
                     ▒▒▒▒▒░              ▒▒▒▒▒░                     
                  ▒▒▒▓▓▒                 ░░░░░▒▒░                   
                  ░░▒▒░░                    ░▓▓▓▓▓░                 
                                             ▒▓▒░▒░                                                                             
""")

sirfetchd = ("""                                 
                                            ░▒                    ░             
                                            ▓██▓▓                ▒▓▓            
                                            █████▓              ▒██▓            
                                          ▒▒▓██████▓▒▒          ▓██▓▒▒          
                                          ██▒██████▓█▒         ▒▓██▓▒▓▒         
                                         ░████████▓█▓▒▓▒▓▓ ▒▓▓▓▒▓███▓▓▒     ░   
                                         ▒████████████████▓▓▓▓▓▓▓███▓▒     ░░░░ 
                                          ████████████████▓▓▓▓▓▓▓████▒     ░░░░ 
                                     ▒▒▓▓▓▓████████████████▓▓▓▓▓▓████▓▒   ░░░░░ 
                              ▒▒▓▓▓███████▒▓████████▓▒██▒██▒   ▒▓█████▓░░░░░░░░ 
                     ▒▒▓▓▓▓███████████████▒░▓██████░░░▓▒░▒█▓   ▒▓████▓▓▒░░░░░░░ 
              ░▒▓▓▓▓██████████████▓▓▓█▓▒░ █▒░▒██▓▒░▒▓██▒░░░░░░░░▒▓▓▒█▓▒▒░░░░░░░░
      ▒▓▒▒▓█████████████▓█▓▓▒░            ▓█▒▒░░▒▓▓▒▓▓██░░░░░░░░░░░░░▒▒░░░░░░░░░
▒▓▓▓███████████▓▓▓▓▓▒░                    ██▓▓█████▓▒▓███░░░░░░░░░░░▓█▓██▓▒░░░░░
 ▒▓████▓▒░░                                ▒█████████▒▓██▓▒░░░░░░░▒▓█▓▓███▓░░░░░
                                           ██████▓▓▓▓█████▓▒░░░░░▒███▓▓▓█▓▒░░░░░
                                          ░▓███▓▓▓█████▓░░░░░░░░▒▓▓██▓▓▓▓▓▒░░░░ 
                                           ▒██▓████████▒░░░░░░░░░░▒▓▓█▓██▒░░░░░░
                                            ░▓█▓████████░░░░░░░░░░░▓██▓▓▓▒░░░░░░
                                               ▒████████▒░░░░░░░░░▒▒▓▓▓▓▒░░░░░░ 
                                                 ▓▓██████▒░░░░░░░░░░░▒▒▒▒░░░░░░ 
                                                   ▓██████▓▒░░░░░░░░░░░░░░░░░░  
                                                  ░▓▓▓▓▓███▓▒░░░░░░░░░░░░░░ ░   
                                                  ▓▓▓░       ░░░░░░░░░░░░░░     
                                             ▒▓▓▓▓▓▓▓▒         ░▒▒▒░░░░░░░      
                                            ▒▓▓█████▓▒         ▒▓▓▓▓▒░░░░░      
                                             ▓▓▒▓█▓▒          ▒▓█████▒░░░░      
                                                ▒             ▓▓▓███▓▒░░░       
                                                                  ▒░                                                                                               
""")

pikachu = ("""            
                         ███              
                         █████            
                         ████▓▓           
           ██████         ██▓▒▒▓          
           ████▒▒▒▓▓       ▓▒▒▒▒▓         
    █▒▓█     ██▒▒▒▒▒▒█  ▓█▓▓▓▒▒▒▓▓        
   █▒▒▒▒▒█      █▒▒▒▒▒▓▒▒▒▒▒▒▓▒▒▒▓        
   █▒▒▒▒▒▒▒▒█      █▓▒▒▒▒▒▒▒▒▒▒▒▒▒█       
  █▒▒▒▒▒▒▒▒▒▒▓     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█      
  ██▒▒▒▒▒▒▒▒▒▒▒▓  █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█     
      █▓▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██     
         █▓▓▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓      
           █▓▒▒▒▒█▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒█   
          █▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▓█  
           █▓▒▒▒█▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒██    
            █▓▒▓█▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▓█        
            █▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓          
            █▓█▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒█         
            █▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓         
             █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█                                                             
""")

pikachu_victory = ("""                      
                  ███         ██          
                  █████      ████         
        █         ████▒█     ████         
      ▓▒▒▓        █▓▓▒▒▒█    ▓▒▒▒█        
      ▒▒▒▒▓        █▒▒▒▒▒    ▓▒▒▒█        
    ▓▒▒▒▒▒▒▓        █▓▒▒▒▓████▓▒▓█        
   █▒▒▒▒▒▒▒▒█         █▒▒▒▒▒▒▒▒▒█         
    ▓▒▒▒▒▒▒▒▒█      █▒▒▒▒▒▒▒▒▓▒▒▒▒▓       
      ▒▒▒▒▒▒▒▓     ▓▒▒▒▒▒▒▒▒▒▓█▒▒▒▒▒      
       █▓▒▒▒▒▒▒   █▓▓▒▒▓▒▒▓█▓▒▒▓▓▓▓▓▒█    
         █▒▒▒▒▒▒██▒▒▓▒▒▒▓▒███▓▒▒██▓▒▓█    
           █▒▒▒▒█▒▒▒▓▒▒▒▒▓▒▒▒▒▒▒▒▓▒▓█     
          █▓▒▒▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓█      
         █▓▒▒▓▒▒▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▓█        
          █▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█         
           ██▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒█          
          █▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓          
           ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓          
             █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓         
               █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓                                                 
""")
snorlax_sleep = ("""                       
                  ▓▓▓█        ▓▓▓                 
                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                
                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                
                ▓▓▒▒▒▓▓▓▓▓▒▒▒▓▓▓▓██               
               ▓▓▒▒▒▒▒▓▓▒▒▒▒▒▒▒▓▓██               
               █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████             
              ███▓▒▓▓▒▒▒▒▒▓▓▓▓▒▒██▓▓▓██           
            ▓▓▓▓▓█▓▓▓▓▒▒▒▓▓▒▒▒▒▓█▓▓▓▓▓▓█          
           █▓▓▓▓▓▓▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█         
          █▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓█        
          █▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█▓▓█       
         ██▓▓▓▓▓█▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓█▓▓▓█       
         ██▓█▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▓▓▓█▓▓▓▓█       
      ██ ██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▒▒▓▓▓▓█       
      ▓▓█▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▒▒▓▓▓▓▓█       
    █▓▓▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓█▒█▓▓█       
      ▓▒▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▓▒█        
       ▓▓▓▓▓▓▓███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▒▒▓▓▒▒▒█▓        
        ▓▓▓▓████     ▓██████████▓▒▓▓▓▓▓▒▒▓        
                              ███▒▓▓▓█▒▒█         
                                  ████                                                                                     
""")

snorlax_awake = ("""                           
                      ▓█                          
                     ▓▓▓▓▓▓▓▓▓██▓▓▓▓█             
                    █▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓█             
                   █▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓█             
                   ▓▒█▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓█            
                   █▒▒▒▒▒██▒▒▒▒▒▒▒▒▓▓█            
      █▓█▓█▓▓▓███ ██▒▒▒▒▓▓▓▓▓▒▒▒▒▒▒▓▓█            
     █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓█▓▓▓█▒▒▒▒▒▓▓█▓█████▓███   
      █▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓█  
        ███▓▓█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓█ 
            █▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓████  
          ██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓████       
          ██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█       
         ██▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█      
         █▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█      
     █▓███▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓█      
   ██▓█▒▓▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓█████      
    ▓▓▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▓▓███      
     ▓▒▓▓▓▓▒▓█▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▓       
     ▓▓▓▓▓█▒██████▓▓▓▒▒▒▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▒▓       
        ███                 ██████▓▓▓▓▓▓▓▒█       
                                   █▓▓▓▒██                                                 
""")
quena_instrument = ("""
                       ███▓   
                     ▓███▓▓▒▓ 
                    ▒▒▓▓███▓██
                  ▓▓▒▒▒▓▓▓███ 
                ███▓▓▒▒▒▒▒▓   
              ███████▓▒▒▒     
            ██████████▓▒      
          ████████████        
        ██████▓█████          
      █████▓██████            
     ███████████              
   ███████████                
 ███████████                  
████▓█████                    
█████████                     
  █████                                                                                                     
""")
chansey = ("""
                                         ████▓▓▓▓                                         
                                     ██████████████▓▓                                     
                                   ▓▓████████████████▒░                                   
                                 ▓▓███████████████████▓▒░                                 
                                ▒▓██████████████████████▓░░                               
                              ▒▓▓█████▒▓████░█████████████▓▒▒                             
                          ▒▒▓▓█████████▓▒▒▒▒██████████▓▓█▓▓▓█▓▓▓▓▒▒▒                      
                       ▒▒▓▓▓▓▓██████████▓▒▒▓███████████▓▓███▓▓▒▒▒▓▓▒▒                     
                      ▒▒▒▒▓▓▓████████████████████████████▓▓▒▒█▓▓▓▒▒▒▒                     
                     ▒▒▓▒▒▒▓▓▓▓█████████████████████████▓██▓▓▒▒▒▒▒▓▓▒▒                    
                      ░░▒▓▓▓▒▒███████████▓▓▓█████████████▒▒▒▓▓▓▓▒▒░▒▒                     
                      ░░▒▒░▒████████▓██▓▓███▓▓▓█▓▓██████████▒▒▒▒▒▒░                       
                           ▓█████▓▓███████████▓███████████████▓░                          
                           ▓▓██████▓▒▓████████▓▓▓▓▓▓▓█████████▓░                          
                            ▒▓██████▓▓████████▓▓▒▓████████████▒░                          
                            ▒▓█████▓▓█▓▓▒▒▒▒▒▒▓▓▓▒███████████▓░▒▒▒                        
                             ▒▓████▓▒▓██████▓▓▓▓▒▒███████████░██▓▓▒                       
                              ▒▓████▓▓▓▓▓▓▓▓▓▓▓▒▒██████████▓░█▓▓░                         
                                ▒▓████▓▒▒▓▓▓▒░░██████████▓░▓▒▒                            
                                 ░▒▓▓█████████████████▓▓░░                                
                              ░░░▓▓▓░░▒▓▓▓██████▓▓▓▓▒░░▓░░░                               
                              ░▓▓▓▓░░░    ░░░░░░   ░░▓▓▓▓▓▓░                              
                                                      ░░░░░
""")
game_over = ("""
▒█▀▀█ █▀▀█ █▀▄▀█ █▀▀ 　 █▀▀█ ▀█░█▀ █▀▀ █▀▀█ 
▒█░▄▄ █▄▄█ █░▀░█ █▀▀ 　 █░░█ ░█▄█░ █▀▀ █▄▄▀ 
▒█▄▄█ ▀░░▀ ▀░░░▀ ▀▀▀ 　 ▀▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀
""")
winner = ("""
██╗░░░██╗██╗░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗
██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
░╚████╔╝░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░
░░╚██╔╝░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░
░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
""")

# Pokemon life
LIFE_INITIAL_PIKACHU = 200
LIFE_INITIAL_MELTAN = 200
LIFE_INITIAL_VAPOREON = 200
LIFE_INITIAL_POLITOED = 200
LIFE_INITIAL_FORRETRESS = 200
LIFE_INITIAL_PRIMEAPE = 200
LIFE_INITIAL_SIRFETCHD = 200

current_life_pikachu = LIFE_INITIAL_PIKACHU
current_life_meltan = LIFE_INITIAL_MELTAN
current_life_vaporeon = LIFE_INITIAL_VAPOREON
current_life_politoed = LIFE_INITIAL_POLITOED
current_life_forretress = LIFE_INITIAL_FORRETRESS
current_life_primeape = LIFE_INITIAL_PRIMEAPE
current_life_sirfetchd = LIFE_INITIAL_SIRFETCHD


# Percentage basis
CONSTANTE_BASE = 50

#Interactive options
options = ["w",  "a", "s", "d", "q", "e"]

#Functions

def percentage(a, b):
    return int((CONSTANTE_BASE * a) / b)

def clean_screen():
    if os.name == "posix":
        return os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        return os.system("cls")

# Location of elements
POS_X = 0
POS_Y = 1
my_position = [4, 0]
trainers = [[27, 1], [44, 6], [17, 9], [12, 17], [38, 17], [65, 17]]
musical_instrument = [74, 18]
snorlax = [4, 7]
chansey_location = [[27, 6], [17, 12]]
first_block = [[29, 4], [30, 4], [31, 4], [32, 4]]
second_block = [[58, 13], [59, 13], [58, 14], [59, 14], [58, 15], [59, 15]]
third_block = [[15, 13], [16, 13], [15, 14], [16, 14], [15, 15], [16, 15]]
fourth_block = [[26, 16], [26, 17]]

# Triggers
snorlax_block = False
quena = False
victory = False
defeat = False

# Pokemon life

# Map dimensions
MAP_WIDTH = len(map_definition[0])
MAP_HEIGHT = len(map_definition)

#Presentation
clean_screen()

print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║  
║   ░██╗░░░░░░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗   ║
║   ░██║░░██╗░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝   ║
║   ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░   ║
║   ░░████╔═████║░██╔══╝░░██║░░░░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░   ║
║   ░░╚██╔╝░╚██╔╝░███████╗███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗   ║
║   ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝   ║   
╚═══════════════════════════════════════════════════════════════════════════════╝
""")

time.sleep(2)
clean_screen()

print("""
╔═════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                     ║  
║   ██████╗░░█████╗░██╗░░██╗███████╗███╗░░░███╗███╗░░░███╗░█████╗░███╗░░██╗██████╗░   ║
║   ██╔══██╗██╔══██╗██║░██╔╝██╔════╝████╗░████║████╗░████║██╔══██╗████╗░██║██╔══██╗   ║
║   ██████╔╝██║░░██║█████═╝░█████╗░░██╔████╔██║██╔████╔██║███████║██╔██╗██║██║░░██║   ║
║   ██╔═══╝░██║░░██║██╔═██╗░██╔══╝░░██║╚██╔╝██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║   ║
║   ██║░░░░░╚█████╔╝██║░╚██╗███████╗██║░╚═╝░██║██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝   ║
║   ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░   ║   
╚═════════════════════════════════════════════════════════════════════════════════════╝
""")

time.sleep(2)
clean_screen()

print("""
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                          ║  
║   ███╗░░██╗░█████╗░██████╗░███████╗░█████╗░████████╗██╗░░██╗██████╗░██╗░░░██╗███╗░░██╗   ║
║   ████╗░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░██║██╔══██╗██║░░░██║████╗░██║   ║
║   ██╔██╗██║██║░░██║██║░░██║█████╗░░███████║░░░██║░░░███████║██████╔╝██║░░░██║██╔██╗██║   ║
║   ██║╚████║██║░░██║██║░░██║██╔══╝░░██╔══██║░░░██║░░░██╔══██║██╔══██╗██║░░░██║██║╚████║   ║
║   ██║░╚███║╚█████╔╝██████╔╝███████╗██║░░██║░░░██║░░░██║░░██║██║░░██║╚██████╔╝██║░╚███║   ║
║   ╚═╝░░╚══╝░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝   ║   
╚══════════════════════════════════════════════════════════════════════════════════════════╝
""")

time.sleep(2)
clean_screen()
print("""
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║                    ┌┬┐┌─┐┬  ┬┌─┐┌┬┐┌─┐┌┐┌┌┬┐  ┌─┐─┐ ┬┬┌┬┐  ┬┌┐┌┌─┐┌─┐                    ║
║                    ││││ │└┐┌┘├┤ │││├┤ │││ │   ├┤ ┌┴┬┘│ │   ││││├┤ │ │                    ║
║                    ┴ ┴└─┘ └┘ └─┘┴ ┴└─┘┘└┘ ┴   └─┘┴ └─┴ ┴   ┴┘└┘└  └─┘                    ║
║                       ____ ____ ____ ____        ____         ____                       ║
║                      ||W |||A |||S |||D ||      ||Q ||       ||E ||                      ║
║                      ||__|||__|||__|||__||      ||__||       ||__||                      ║
║                      |/__\|/__\|/__\|/__\|      |/__\|       |/__\|                      ║ 
╚══════════════════════════════════════════════════════════════════════════════════════════╝
""")
input("Presiona Enter para iniciar")
clean_screen()


while victory == False and defeat == False:
    char_to_draw = None
    print("╔" + "═" * MAP_WIDTH + "╗")
    for coordinate_y in range(MAP_HEIGHT):

        print("║", end="")

        for coordinate_x in range(MAP_WIDTH):

            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:  # Player
                char_to_draw = "■"
            elif map_definition[coordinate_y][coordinate_x] == "D":  # Ground
                char_to_draw = " "
            elif map_definition[coordinate_y][coordinate_x] == "G":  # Grass
                char_to_draw = "¥"
            elif map_definition[coordinate_y][coordinate_x] == "M":  # Mountain Asc
                char_to_draw = "/"
            elif map_definition[coordinate_y][coordinate_x] == "I":  # Mountain Desc
                char_to_draw = "\\"
            elif map_definition[coordinate_y][coordinate_x] == "P":  # Mountain peak
                char_to_draw = "^"
            elif map_definition[coordinate_y][coordinate_x] == "E":  # Empty
                char_to_draw = " "
            elif map_definition[coordinate_y][coordinate_x] == "F":  # Fence
                char_to_draw = "▀"
            elif map_definition[coordinate_y][coordinate_x] == "W":  # Wall
                char_to_draw = "█"
            elif map_definition[coordinate_y][coordinate_x] == "H":  # Mountain Wall
                char_to_draw = "▓"
            elif map_definition[coordinate_y][coordinate_x] == "O":  # Wave
                char_to_draw = "~"
            elif map_definition[coordinate_y][coordinate_x] == "K":  # Tree trunk
                char_to_draw = "╦"
            elif map_definition[coordinate_y][coordinate_x] == "w":  # Wall
                char_to_draw = "│"
            elif map_definition[coordinate_y][coordinate_x] == "f":  # floor
                char_to_draw = "_"
            elif map_definition[coordinate_y][coordinate_x] == "r":  # Roof
                char_to_draw = "¯"
            elif map_definition[coordinate_y][coordinate_x] == "L":  # Healing
                char_to_draw = "╬"
            if snorlax[POS_X] == coordinate_x and snorlax[POS_Y] == coordinate_y and snorlax_block == False:  # Snorlax
                char_to_draw = "Z"
            if musical_instrument[POS_X] == coordinate_x and musical_instrument[POS_Y] == coordinate_y \
                    and quena == False:
                char_to_draw = "♪"

            if len(trainers) > 5:
                for block_one in first_block:
                    if block_one[POS_X] == coordinate_x and block_one[POS_Y] == coordinate_y:
                        char_to_draw = "▀"

            if len(trainers) > 4:
                for block_two in second_block:
                    if block_two[POS_X] == coordinate_x and block_two[POS_Y] == coordinate_y:
                        char_to_draw = "~"

            if len(trainers) > 2:
                for block_three in third_block:
                    if block_three[POS_X] == coordinate_x and block_three[POS_Y] == coordinate_y:
                        char_to_draw = "~"

            if len(trainers) > 1:
                for block_four in fourth_block:
                    if block_four[POS_X] == coordinate_x and block_four[POS_Y] == coordinate_y:
                        char_to_draw = "█"
            for trainer in trainers:
                if trainer[POS_X] == coordinate_x and trainer[POS_Y] == coordinate_y:
                    char_to_draw = "¤"

            print("{}".format(char_to_draw), end="")

        print("║")

    print("╚" + "═" * MAP_WIDTH + "╝")


# Player control
    new_position = None
    direction = None
    while direction not in options:

        direction = readchar.readchar()

        if direction == "w":
            new_position = [my_position[POS_X], (my_position[POS_Y] - 1)]
            if new_position[POS_Y] < 0:
                new_position[POS_Y] += 1

        elif direction == "s":
            new_position = [my_position[POS_X], (my_position[POS_Y] + 1)]
            if new_position[POS_Y] > MAP_HEIGHT - 1:
                new_position[POS_Y] -= 1

        elif direction == "a":
            new_position = [(my_position[POS_X] - 1), my_position[POS_Y]]
            if new_position[POS_X] < 0:
                new_position[POS_X] += 1

        elif direction == "d":
            new_position = [(my_position[POS_X] + 1), my_position[POS_Y]]
            if new_position[POS_X] > MAP_WIDTH - 1:
                new_position[POS_X] -= 1


        elif direction == "e":
            if snorlax_block == False:
                clean_screen()
                print("WASD para moverte\n■ = jugador\n¤ = entredadores contrincantes\n♪ = instrumento musical\n"
                      "╬ = curación\nHabilidades de pikachu: 1: Thunder Shock (ataque electrico [65 de poder])\n"
                      "2: Feint(ataque normal [reduce los aumentos de defensa]\n"
                      "3: Doble team (ataque normal [te da evasión contra un atanque])")
                input("Presiona Enter para continuar")

            elif snorlax_block == True:
                clean_screen()
                print("WASD para moverte\n■ = jugador\n¤ = entredadores contrincantes\n♪ = instrumento musical\n"
                      "╬ = curación\n Habilidades de pikachu: 1: Thunder Shock (ataque electrico [65 de poder])\n"
                      "2: Feint(ataque normal [reduce los aumentos de defensa]\n"
                      "3: Doble team (ataque normal [te da evasión contra un atanque])\n"
                      "4: Agility(aumenta +1 la velocidad)\n"
                      "5: Electro Ball(ataque electrico [65 de poder x la velocidad])\n")
                input("Presiona Enter para continuar")


# Player moment
    if direction == "e":
        my_position = my_position

    elif direction == "q":
        defeat = True

    elif new_position == snorlax and quena == False:
        clean_screen()
        print(snorlax_sleep)
        print("Hay un Snorlax dormido, parece que necesitarás algo para despertarlo.")
        my_position = my_position
        input("Presiona Enter para continuar")

    elif new_position == snorlax and quena == True and snorlax_block == False:
        clean_screen()
        print(snorlax_awake)
        print("Usas la quena, el sonido del instrumento despierta al Snorlax\n Se aleja y despeja el camino.")
        print("La montaña brinda nuevos poderes a Pikachu.")
        snorlax_block = True
        my_position = new_position
        input("Presiona Enter para continuar")

    elif new_position in chansey_location:
        clean_screen()
        print(chansey)
        print("Chansey cura toda la vida de Pikachu")
        current_life_pikachu = LIFE_INITIAL_PIKACHU
        print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                   " " * (CONSTANTE_BASE - percentage(current_life_pikachu,LIFE_INITIAL_PIKACHU)),
                                                   current_life_pikachu, LIFE_INITIAL_PIKACHU))
        my_position = new_position
        input("Presiona Enter para continuar")

    elif new_position == musical_instrument and quena == False:
        clean_screen()
        print(quena_instrument)
        print("Obtienes una Quena")
        quena = True
        my_position = new_position
        input("Presiona Enter para continuar")

    #Pokemon combat
    elif new_position in trainers:
        if new_position == [27, 1]:  # vs Meltan (Rocío)
            clean_screen()
            print("Combate contra MELTAN.")
            # stats
            evasion = 0
            defense = 0
            while current_life_pikachu > 0 and current_life_meltan > 0:
                print(meltan)
                print("Turno de Meltan")
                meltan_attack_types = ["Thunder Shock", "Headbutt", "Harden"]
                attack_meltan = random.choice(meltan_attack_types)
                print("Meltan usa {}".format(attack_meltan))
                if evasion > 0 and attack_meltan != "Harden":
                    evasion -= 1
                    print("Pikachu evade el ataque")
                elif attack_meltan == "Thunder Shock":
                    current_life_pikachu -= 40
                elif attack_meltan == "Headbutt":
                    current_life_pikachu -= 40
                elif attack_meltan == "Harden":
                    defense += 20
                    print("Su defensa aumenta durante el resto del combate")

                if current_life_meltan < 0:
                    current_life_meltan = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Meltan [{}{}] ({}/{})".format("█" * percentage(current_life_meltan, LIFE_INITIAL_MELTAN),
                                                          " " * (CONSTANTE_BASE - percentage(current_life_meltan,
                                                                                             LIFE_INITIAL_MELTAN)),
                                                          current_life_meltan, LIFE_INITIAL_MELTAN))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))

                input("Presiona Enter para continuar")

                clean_screen()

                if current_life_pikachu > 0:
                    print(pikachu)
                    print("Turno de Pikachu")
                    attack_pikachu = None
                    pikachu_attack_types = ["0", "Thunder Shock", "Feint", "Doble team"]
                    while attack_pikachu != 1 and attack_pikachu != 2 and attack_pikachu != 3:
                        attack_pikachu = int(input("¿Qué ataque desea realizar?: "
                                                   "\n1: Thunder Shock\n2: Feint\n3: Doble team\n"))
                    print("Pikachu usa {}".format(pikachu_attack_types[attack_pikachu]))

                    if attack_pikachu == 1:
                        current_life_meltan -= (65 - defense)
                    elif attack_pikachu == 2:
                        current_life_meltan -= 40
                        defense = 0
                        print("Reduce la defensa a 0")
                    elif attack_pikachu == 3:
                        evasion += 1
                        print("Aumenta la evasión")

                if current_life_meltan < 0:
                    current_life_meltan = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Meltan [{}{}] ({}/{})".format("█" * percentage(current_life_meltan, LIFE_INITIAL_MELTAN),
                                                          " " * (CONSTANTE_BASE - percentage(current_life_meltan,
                                                                                             LIFE_INITIAL_MELTAN)),
                                                          current_life_meltan, LIFE_INITIAL_MELTAN))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))
                input("Presiona Enter para continuar")
                clean_screen()

            if current_life_pikachu == 0:
                defeat = True
                print("Pikachu pierde el combate")

            else:
                print(pikachu_victory)
                print("Pikachu gana el combate")
                trainers.remove(new_position)
                new_position = my_position
                input("Presiona Enter para continuar")

        elif new_position == [44, 6]:  # vs Vapoeron (Eric)
            clean_screen()
            print("Combate contra VAPOREON.")
            # stats
            evasion = 0
            defense = 0
            while current_life_pikachu > 0 and current_life_vaporeon > 0:
                print(vaporeon)
                print("Turno de Vaporeon")
                vaporeon_attack_types = ["Water Gun", "Tackle", "Tail Whip"]
                attack_vaporeon = random.choice(vaporeon_attack_types)
                print("Vaporeon usa {}".format(attack_vaporeon))
                if evasion > 0 and attack_vaporeon != "Tail Whip":
                    evasion -= 1
                    print("Pikachu evade el ataque")
                elif attack_vaporeon == "Water Gun":
                    current_life_pikachu -= (40 - defense)
                elif attack_vaporeon == "Tackle":
                    current_life_pikachu -= (40 - defense)
                elif attack_vaporeon == "Tail Whip":
                    defense -= 20
                    print("Reduce la defensa de Pikachu durante el resto del combate")

                if current_life_vaporeon < 0:
                    current_life_vaporeon = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Vaporeon [{}{}] ({}/{})".format("█" * percentage(current_life_vaporeon, LIFE_INITIAL_VAPOREON),
                                                            " " * (CONSTANTE_BASE - percentage(current_life_vaporeon,
                                                                                               LIFE_INITIAL_VAPOREON)),
                                                            current_life_vaporeon, LIFE_INITIAL_VAPOREON))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))

                input("Presiona Enter para continuar")

                clean_screen()

                if current_life_pikachu > 0:
                    print(pikachu)
                    print("Turno de Pikachu")
                    attack_pikachu = None
                    pikachu_attack_types = ["0", "Thunder Shock", "Feint", "Doble team"]
                    while attack_pikachu != 1 and attack_pikachu != 2 and attack_pikachu != 3:
                        attack_pikachu = int(
                            input("¿Qué ataque desea realizar?: \n1: Thunder Shock\n2: Feint\n3: Doble team\n"))
                    print("Pikachu usa {}".format(pikachu_attack_types[attack_pikachu]))

                    if attack_pikachu == 1:
                        current_life_vaporeon -= 65
                    elif attack_pikachu == 2:
                        current_life_vaporeon -= 40
                        print("Reduce la defensa a 0")
                    elif attack_pikachu == 3:
                        evasion += 1
                        print("Aumenta la evasión")

                if current_life_vaporeon < 0:
                    current_life_vaporeon = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Vaporeon [{}{}] ({}/{})".format("█" * percentage(current_life_vaporeon, LIFE_INITIAL_VAPOREON),
                                                            " " * (CONSTANTE_BASE - percentage(current_life_vaporeon,
                                                                                               LIFE_INITIAL_VAPOREON)),
                                                            current_life_vaporeon, LIFE_INITIAL_VAPOREON))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))
                input("Presiona Enter para continuar")
                clean_screen()

            if current_life_pikachu == 0:
                print("Pikachu pierde el combate")
                defeat = True
            else:
                print(pikachu_victory)
                print("Pikachu gana el combate")
                trainers.remove(new_position)
                new_position = my_position
                input("Presiona Enter para continuar")

        elif new_position == [65, 17]: # vs Politoed (Caliebre)
            clean_screen()
            print("Combate contra POLITOED.")
            # stats
            evasion = 0
            while current_life_pikachu > 0 and current_life_politoed > 0:
                sleep = False
                print(politoed)
                print("Turno de Politoed")
                politoed_attack_types = ["Bubble Beam", "Double Slap", "Perish Song"]
                attack_politoed = random.choice(politoed_attack_types)
                print("Politoed usa {}".format(attack_politoed))
                if evasion > 0 and attack_politoed != "Perish Song":
                    evasion -= 1
                    print("Pikachu evade el ataque")
                elif attack_politoed == "Bubble Beam":
                    current_life_pikachu -= 65
                elif attack_politoed == "Double Slap":
                    current_life_pikachu -= 30
                elif attack_politoed == "Perish Song":
                    sleep = True
                    print("Politoed realiza una canción")
                    print("♫ La ranita, la ranita, la ranita traca tra, tra, tra tra ♫")

                if current_life_politoed < 0:
                    current_life_politoed = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Politoed [{}{}] ({}/{})".format("█" * percentage(current_life_politoed, LIFE_INITIAL_POLITOED),
                                                            " " * (CONSTANTE_BASE - percentage(current_life_politoed,
                                                                                               LIFE_INITIAL_POLITOED)),
                                                            current_life_politoed, LIFE_INITIAL_POLITOED))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))

                input("Presiona Enter para continuar")

                clean_screen()

                if current_life_pikachu > 0:
                    print(pikachu)
                    print("Turno de Pikachu")
                    if sleep == True:
                        print("Pikachu está dormido")
                    elif sleep == False:
                        attack_pikachu = None
                        pikachu_attack_types = ["0", "Thunder Shock", "Feint", "Doble team"]
                        while attack_pikachu != 1 and attack_pikachu != 2 and attack_pikachu != 3:
                            attack_pikachu = int(
                                input("¿Qué ataque desea realizar?: \n1: Thunder Shock\n2: Feint\n3: Doble team\n"))
                        print("Pikachu usa {}".format(pikachu_attack_types[attack_pikachu]))

                        if attack_pikachu == 1:
                            current_life_politoed -= 65
                        elif attack_pikachu == 2:
                            current_life_politoed -= 40
                            print("Reduce la defensa a 0")
                        elif attack_pikachu == 3:
                            evasion += 1
                            print("Aumenta la evasión")

                if current_life_politoed < 0:
                    current_life_politoed = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Politoed [{}{}] ({}/{})".format("█" * percentage(current_life_politoed, LIFE_INITIAL_POLITOED),
                                                            " " * (CONSTANTE_BASE - percentage(current_life_politoed,
                                                                                               LIFE_INITIAL_POLITOED)),
                                                            current_life_politoed, LIFE_INITIAL_POLITOED))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))
                input("Presiona Enter para continuar")
                clean_screen()

            if current_life_pikachu == 0:
                print("Pikachu pierde el combate")
                defeat = True
            else:
                print(pikachu_victory)
                print("Pikachu gana el combate")
                trainers.remove(new_position)
                new_position = my_position
                input("Presiona Enter para continuar")

        elif new_position == [17, 9]: # vs Forretress (Rafa)
            clean_screen()
            print("Combate contra FORRETRESS.")
            # stats
            evasion = 0
            charge = 0
            weight = 2
            speed = 1

            while current_life_pikachu > 0 and current_life_forretress > 0:
                print(forretress)
                print("Turno de Forretress")
                if charge > 1:
                    forretress_attack_types = ["Protect", "Autotomize", "Heavy Slam"]
                    attack_forretress = random.choice(forretress_attack_types)
                    print("Forretress usa {}".format(attack_forretress))
                    if evasion > 0 and attack_forretress == "Heavy Slam":
                        evasion -= 1
                        print("Pikachu evade el ataque")
                    elif attack_forretress == "Protect":
                        weight += 1
                        print("Forretress ensambla una placa de acero más a su cuerpo.\n Aumenta su defensa")
                    elif attack_forretress == "Autotomize":
                        print(
                            "Forretress desensambla una placa de su cuerpo.\n  Ahora es más ligero y acelera sus ataques.")
                        weight -= 1
                        if weight < 0:
                            weight = 1
                        charge -= 1
                    elif attack_forretress == "Heavy Slam":
                        current_life_pikachu -= (30 * weight)
                        print("Ataca con el peso de su cuerpo")
                    charge -= 1
                elif charge == 1:
                    print("Forretress termina de cargar su ataque y usa Zap Cannon")
                    current_life_pikachu -= 120
                    charge -= 1
                elif charge == 0:
                    forretress_attack_types = ["Zap Cannon", "Protect", "Autotomize", "Heavy Slam"]
                    attack_forretress = random.choice(forretress_attack_types)
                    print("Forretress usa {}".format(attack_forretress))
                    if evasion > 0 and attack_forretress == "Heavy Slam":
                        evasion -= 1
                        print("Pikachu evade el ataque")
                    elif attack_forretress == "Zap Cannon":
                        print("Forretress empieza cargar su ataque")
                        charge = 3
                    elif attack_forretress == "Protect":
                        weight += 1
                        print("Forretress ensambla una placa de acero más a su cuerpo.\n Aumenta su defensa")
                    elif attack_forretress == "Autotomize":
                        print(
                            "Forretress desensambla una placa de su cuerpo.\n  Ahora es más ligero y acelera sus ataques.")
                        weight -= 1
                        if weight < 0:
                            weight = 1
                        charge -= 1
                        if charge < 0:
                            charge = 0
                    elif attack_forretress == "Heavy Slam":
                        current_life_pikachu -= (10 * weight)
                        print("Ataca con el peso de su cuerpo")

                if current_life_forretress < 0:
                    current_life_forretress = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Forretress [{}{}] ({}/{})".format(
                    "█" * percentage(current_life_forretress, LIFE_INITIAL_FORRETRESS),
                    " " * (CONSTANTE_BASE - percentage(current_life_forretress, LIFE_INITIAL_FORRETRESS)),
                    current_life_forretress, LIFE_INITIAL_FORRETRESS))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))

                input("Presiona Enter para continuar")

                clean_screen()

                if current_life_pikachu > 0:
                    print(pikachu)
                    print("Turno de Pikachu")
                    attack_pikachu = None
                    pikachu_attack_types = ["0", "Thunder Shock", "Feint", "Doble team", "Agility", "Electro Ball"]
                    while attack_pikachu != 1 and attack_pikachu != 2 and attack_pikachu != 3 and attack_pikachu != 4 \
                            and attack_pikachu != 5:
                        attack_pikachu = int(
                            input("¿Qué ataque desea realizar?: \n1: Thunder Shock\n2: Feint\n3: Doble team\n"
                                  "4: Agility\n5: Electro Ball\n"))

                    print("Pikachu usa {}".format(pikachu_attack_types[attack_pikachu]))

                    if attack_pikachu == 1:
                        current_life_forretress -= 65 + (20 * weight)
                    elif attack_pikachu == 2:
                        current_life_forretress -= 40
                        print("Rompe una placa")
                        weight -= 1
                        charge -= 1
                        if weight > 0:
                            weight = 0
                        if charge == 0:
                            charge = 1
                    elif attack_pikachu == 3:
                        evasion += 1
                        print("Aumenta la evasión")
                    elif attack_pikachu == 4:
                        speed += 1
                        print("Aumenta su velocidad")
                    elif attack_pikachu == 5:
                        print("Pikachu gira para crear una bola de energía eléctrica")
                        current_life_forretress -= (65 * speed)

                if current_life_forretress < 0:
                    current_life_forretress = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Forretress [{}{}] ({}/{})".format(
                    "█" * percentage(current_life_forretress, LIFE_INITIAL_FORRETRESS),
                    " " * (CONSTANTE_BASE - percentage(current_life_forretress, LIFE_INITIAL_FORRETRESS)),
                    current_life_forretress, LIFE_INITIAL_FORRETRESS))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))
                input("Presiona Enter para continuar")
                clean_screen()

            if current_life_pikachu == 0:
                print("Pikachu pierde el combate")
                defeat = True
            else:
                print(pikachu_victory)
                print("Pikachu gana el combate")
                trainers.remove(new_position)
                new_position = my_position
                input("Presiona Enter para continuar")


        elif new_position == [12, 17]: # vs Primeape (Pazos)
            clean_screen()
            print("Combate contra PRIMEAPE.")
            # stats
            evasion = 0
            fury = 1
            speed = 1
            critic = 2.0

            while current_life_pikachu > 0 and current_life_primeape > 0:
                clean_screen()
                print(primeape)
                print("Turno de Primeape")
                if current_life_primeape > (LIFE_INITIAL_PRIMEAPE / 4):
                    primeape_attack_types = ["Rage", "Low Kick", "Focus Energy"]
                    attack_primeape = random.choice(primeape_attack_types)
                    print("Forretress usa {}".format(attack_primeape))
                    if evasion > 0 and attack_primeape != "Focus Energy":
                        evasion -= 1
                        print("Pikachu evade el ataque")
                    elif attack_primeape == "Rage":
                        print("Primeape ataca y aumenta su furia")
                        current_life_pikachu -= (20 * critic)
                        critic += 0.5
                    elif attack_primeape == "Low Kick":
                        print("Ataca a Pikachu y reduce su velocidad")
                        current_life_pikachu -= 40
                        speed -= 1
                        if speed < 0:
                            speed = 0
                    elif attack_primeape == "Focus Energy":
                        print("Primeape respira hondo, se enfurece y se cura.")
                        critic += 1.0
                        current_life_primeape += 40
                        if current_life_primeape > LIFE_INITIAL_PRIMEAPE:
                            current_life_primeape = LIFE_INITIAL_PRIMEAPE
                elif current_life_primeape <= (LIFE_INITIAL_PRIMEAPE / 4):
                    print("Primeape realiza un ataque desperado")
                    current_life_pikachu -= (current_life_primeape * critic)

                if current_life_primeape < 0:
                    current_life_primeape = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Primeape [{}{}] ({}/{})".format("█" * percentage(current_life_primeape, LIFE_INITIAL_PRIMEAPE),
                                                            " " * (CONSTANTE_BASE - percentage(current_life_primeape,
                                                                                               LIFE_INITIAL_PRIMEAPE)),
                                                            current_life_primeape, LIFE_INITIAL_PRIMEAPE))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))

                input("Presiona Enter para continuar")

                clean_screen()

                if current_life_pikachu > 0:
                    print(pikachu)
                    print("Turno de Pikachu")
                    attack_pikachu = None
                    pikachu_attack_types = ["0", "Thunder Shock", "Feint", "Doble team", "Agility", "Electro Ball"]
                    while attack_pikachu != 1 and attack_pikachu != 2 and attack_pikachu != 3 and attack_pikachu != 4 \
                            and attack_pikachu != 5:
                        attack_pikachu = int(
                            input("¿Qué ataque desea realizar?: \n1: Thunder Shock\n2: Feint\n3: Doble team\n"
                                  "4: Agility\n5: Electro Ball\n"))

                    print("Pikachu usa {}".format(pikachu_attack_types[attack_pikachu]))

                    if attack_pikachu == 1:
                        current_life_primeape -= 65
                    elif attack_pikachu == 2:
                        current_life_primeape -= 40
                        print("No afecta la defensa de Primeape.\nPor lo contrario, enfurece aún más a Primeape")
                        critic += 0.5
                    elif attack_pikachu == 3:
                        evasion += 1
                        print("Aumenta la evasión")
                    elif attack_pikachu == 4:
                        speed += 1
                        print("Aumenta su velocidad")
                    elif attack_pikachu == 5:
                        print("Pikachu gira para crear una bola de energía eléctrica")
                        current_life_primeape -= (65 * speed)

                if current_life_primeape < 0:
                    current_life_primeape = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Primeape [{}{}] ({}/{})".format("█" * percentage(current_life_primeape, LIFE_INITIAL_PRIMEAPE),
                                                            " " * (CONSTANTE_BASE - percentage(current_life_primeape,
                                                                                               LIFE_INITIAL_PRIMEAPE)),
                                                            current_life_primeape, LIFE_INITIAL_PRIMEAPE))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))
                input("Presiona Enter para continuar")
                clean_screen()

            if current_life_pikachu == 0:
                print("Pikachu pierde el combate")
                defeat = True
            else:
                print(pikachu_victory)
                print("Pikachu gana el combate")
                trainers.remove(new_position)
                new_position = my_position
                input("Presiona Enter para continuar")


        elif new_position == [38, 17]:  # vs Sirfetchd (Alex)
            clean_screen()
            print("Combate contra SIRFETCH'D.")
            # stats
            evasion = 0
            speed = 1
            fury = 1
            defense = 0
            duration_defense = 0
            sword_dance = 1
            critic = 1
            phase = False

            while current_life_pikachu > 0 and current_life_sirfetchd > 0:
                clean_screen()
                print(sirfetchd)
                print("Turno de Sirfetchd")
                if current_life_sirfetchd > ((3 * LIFE_INITIAL_SIRFETCHD) / 4):
                    sirfetchd_attack_types = ["Iron Defense", "Fury Cutter"]
                    attack_sirfetchd = random.choice(sirfetchd_attack_types)
                    print("Forretress usa {}".format(attack_sirfetchd))
                    if evasion > 0 and attack_sirfetchd != "Iron Defense":
                        evasion -= 1
                        print("Pikachu evade el ataque")
                    elif attack_sirfetchd == "Iron Defense":
                        print("Endurece su escudo y aumenta su defensa")
                        defense += 40
                        duration_defense += 2
                    elif attack_sirfetchd == "Fury Cutter":
                        print("Ataca con su lanza y aumenta su daño")
                        current_life_pikachu -= (40 + fury)
                        fury += 10
                    duration_defense -= 1
                    if duration_defense < 0:
                        duration_defense = 0
                elif current_life_sirfetchd <= ((3 * LIFE_INITIAL_SIRFETCHD) / 4):
                    duration_defense = 0
                    defense = 0
                    if phase == False:
                        print("Aumenta la determinación de Sirfetchd")
                        phase = True
                    sirfetchd_attack_types = ["Fury Cutter", "Swords Dance", "Leaf Blade"]
                    attack_sirfetchd = random.choice(sirfetchd_attack_types)
                    print("Sirfetch'd usa {}".format(attack_sirfetchd))
                    if evasion > 0:
                        evasion -= 1
                        print("Pikachu evade el ataque")
                    elif attack_sirfetchd == "Fury Cutter":
                        print("Ataca con su lanza y aumenta su daño")
                        current_life_pikachu -= ((40 + fury) * critic)
                        fury += 10
                        critic = 1
                    elif attack_sirfetchd == "Swords Dance":
                        print("Sirfetch'd realiza un giro con su lanza y aumenta su poder")
                        critic = 2
                    elif attack_sirfetchd == "Leaf Blade":
                        print("Sirfetch'd realiza un ataque frontal con su lanza")
                        current_life_pikachu -= 130

                if current_life_sirfetchd < 0:
                    current_life_sirfetchd = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Sirfetch'd [{}{}] ({}/{})".format("█" * percentage(current_life_sirfetchd, LIFE_INITIAL_SIRFETCHD),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_sirfetchd,
                                                                                              LIFE_INITIAL_SIRFETCHD)),
                                                           current_life_sirfetchd, LIFE_INITIAL_SIRFETCHD))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))

                input("Presiona Enter para continuar")
                clean_screen()

                if current_life_pikachu > 0:
                    print(pikachu)
                    print("Turno de Pikachu")
                    attack_pikachu = None
                    pikachu_attack_types = ["0", "Thunder Shock", "Feint", "Doble team", "Agility", "Electro Ball"]
                    while attack_pikachu != 1 and attack_pikachu != 2 and attack_pikachu != 3 and attack_pikachu != 4 \
                            and attack_pikachu != 5:
                        attack_pikachu = int(
                            input("¿Qué ataque desea realizar?: \n1: Thunder Shock\n2: Feint\n3: Doble team\n"
                                  "4: Agility\n5: Electro Ball\n"))

                    print("Pikachu usa {}".format(pikachu_attack_types[attack_pikachu]))

                    if attack_pikachu == 1:
                        current_life_sirfetchd -= (65 - defense)
                    elif attack_pikachu == 2:
                        current_life_sirfetchd -= 40
                        print("Reduce la duración y el efecto de defensa de Sirfetch'd")
                        defense -= 20
                        if defense < 0:
                            print("La reducción de defensa no es muy efectiva")
                            defense = 0
                        duration_defense -= 1
                        if duration_defense < 0:
                            duration_defense = 0
                    elif attack_pikachu == 3:
                        evasion += 1
                        print("Aumenta la evasión")
                    elif attack_pikachu == 4:
                        speed += 1
                        print("Aumenta su velocidad")
                    elif attack_pikachu == 5:
                        print("Pikachu gira para crear una bola de energía eléctrica")
                        current_life_sirfetchd -= ((65 * speed) - defense)

                if current_life_sirfetchd < 0:
                    current_life_sirfetchd = 0
                elif current_life_pikachu < 0:
                    current_life_pikachu = 0

                print("Vida Sirfetch'd [{}{}] ({}/{})".format("█" * percentage(current_life_sirfetchd, LIFE_INITIAL_SIRFETCHD),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_sirfetchd,
                                                                                              LIFE_INITIAL_SIRFETCHD)),
                                                           current_life_sirfetchd, LIFE_INITIAL_SIRFETCHD))
                print("Vida Pikachu [{}{}] ({}/{})".format("█" * percentage(current_life_pikachu, LIFE_INITIAL_PIKACHU),
                                                           " " * (CONSTANTE_BASE - percentage(current_life_pikachu,
                                                                                              LIFE_INITIAL_PIKACHU)),
                                                           current_life_pikachu, LIFE_INITIAL_PIKACHU))
                input("Presiona Enter para continuar")
                clean_screen()

            if current_life_pikachu == 0:
                print("Pikachu pierde el combate")
                defeat = True
            else:
                print(pikachu_victory)
                print("Pikachu gana el combate")
                trainers.remove(new_position)
                new_position = my_position
                input("Presiona Enter para continuar")
                victory = True

    elif new_position in first_block and len(trainers) > 5:
        my_position = my_position
    elif new_position in second_block and len(trainers) > 4:
        my_position = my_position
    elif new_position in third_block and len(trainers) > 2:
        my_position = my_position
    elif new_position in fourth_block and len(trainers) > 1:
        my_position = my_position

    elif map_definition[new_position[POS_Y]][new_position[POS_X]] == "D" or\
            map_definition[new_position[POS_Y]][new_position[POS_X]] == "G":
        my_position = new_position

    clean_screen()
if victory == True:
    print(victory)
else:
    print(game_over)
