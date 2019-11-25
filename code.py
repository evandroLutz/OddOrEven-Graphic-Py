arr=[940, 445, 686, 460, 29, 487, 351, 573, 291, 640, 615, 571, 830,940, 445, 686, 460, 29, 487, 351, 573, 291, 640, 615, 571, 830,940, 445, 686, 460, 29, 487, 351, 573, 291, 640, 615, 571, 830,940, 445, 686, 460, 29, 487, 351, 573, 291, 640, 615, 571, 830,940, 445, 686, 460, 29, 487, 351, 573, 291, 640, 615, 571, 830]
sizeOfArray = len(arr)
terminou =0

def setup():
    size(1000, 1000)
    background(0)
    noStroke()
 
    
def draw():  
       
    cont_etapa=1; 
    terminou=0   
    while(terminou == 0):       
        terminou = 1 
        print('Inicio da Etapa',cont_etapa);
        print('Lendo e comparando índices pares:')
        
        for i in range(0,sizeOfArray-1,2):
            if(arr[i]>arr[i+1]):
                arrAux = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = arrAux                            
                terminou = 0;
        print('Lendo e comparando índices impares:')
        for i in range(1,sizeOfArray-1,2):            
            if(arr[i]>arr[i+1]):                            
                arrAux = arr[i
                arr[i] = arr[i+1]
                arr[i+1] = arrAux
                terminou = 0
        cont_etapa += 1        
        print(arr)        
        for i in range(0,sizeOfArray-1,1):            
            if(arr[i]<=arr[i+1]):
                fill(0,0,255);                 
                rect(i*20, 1, 10, 1000)             
            else:
                fill(255,0,05);                 
                rect(i*20, 1, 10, 1000)
                          
noLoop()    