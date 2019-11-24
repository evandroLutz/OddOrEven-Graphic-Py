def setup():
    size(480, 120)

def draw():
    if  mousePressed:
        fill(0)
    else:
        fill(255)
    ellipse(mouseX, mouseY, 10, 10)
    
# test of function


def odd_or_even(arr,sizeOfArray):
    terminou=0;
    cont_etapa=1;
    while(terminou == 0):
        terminou = 1;
        print('Inicio da Etapa',cont_etapa);
        print('Lendo e comparando índices pares:')
        for i in range(0,sizeOfArray-1,2):
            if(arr[i]>arr[i+1]):
                arrAux = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = arrAux
                terminou=0;                
                                   

                    
        print('Lendo e comparando índices impares:')
        for i in range(1,sizeOfArray-1,2):
            
            if(arr[i]>arr[i+1]):              
                arrAux = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = arrAux
                terminou=0;                
                       
                
    cont_etapa += 1;
                             
                                                                                        
    print(arr);

arr=[5,7,8,63,8,1,2,5,7,18,2,6,7,9,200,4,1,2,3,4]


odd_or_even(arr,len(arr))

print(len(arr));




                
                                
        
        