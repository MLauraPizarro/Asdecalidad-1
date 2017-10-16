import numpy as np
import cv2
import os
import sys 
from django.conf import settings
sys.path.append("..")
from modelo.imagen import imagen 

class DAOBDmuestral:
    '''
    Clase DAOBDmuestral
    Encargada de procedimientos relativos a la base de datos de imagenes de los sujetos a clasificar
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.nombres_carpetas=[]
        self.ROOT_PATH = os.path.split(os.path.abspath(__file__))[0]
        self.archivos=[]
        self.directorio= self.ROOT_PATH+"/BaseDatosMuestral/input"
        
    def leerCarpetas(self):
        '''
        Inicializa los nombres de las carpetas y los archivos de la base de datos.
        '''
        for filename in os.listdir( self.directorio):
            self.nombres_carpetas.append(filename) 

    def leerImagenes(self,sujeto):
        '''
        Lee y obtiene las imagenes del sujeto especificado por parametro.
        :param sujeto: Sujeto del cual se desean obtener las imagenes de la base de datos.
        '''
        lista_img=[]
        nombres_archivos=os.listdir(self.directorio+"/"+sujeto)
        
        for nombre_archivo in nombres_archivos:
            
            img = cv2.imread(self.directorio+"/"+sujeto+"/"+nombre_archivo)
            

            i=imagen(img)
            i.vectorizar()
            lista_img.append(i)
        return lista_img

               
    def leerImagenestogris(self):
        '''
        Transforma las imagenes a escala de grises.
        '''
        
        for nombre_archivo in self.nombres_archivos:
            img = cv2.imread("files/"+nombre_archivo)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            a=[]
            for i in gray:
                a=np.concatenate((a,i),axis=0)
                self.archivos.append(np.array(a)[:,None])
    
