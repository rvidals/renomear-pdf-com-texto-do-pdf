# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:34:25 2021

@author: Rogerio Vidal de Siqueira
"""

import os
import re
from PyPDF2 import PdfFileReader

#Função de extração de texto
def text_extractor(filename):
    global cutReplace

    with open(filename, 'rb') as f:
        pdf = PdfFileReader(f)
        
        # Pegando somente a primeira págia
        page = pdf.getPage(0)
        text = page.extractText()

        #Recorte de textos na posição 187:229
        cut = re.sub(r"[A-Z]+[:]|[-]|[0-9]|[a-z]", "", text[187:229]) 
        #Remoção de possíveis erros!
        cutReplace = cut.replace('AA','A')
        cutReplace = cutReplace.replace(':','')
        print(cutReplace) #Verificador de leitura
   
    return cutReplace

#Função para renomear arquivos com texto extraido
def file_rename(filename):
    print(os.path.join(dir,filename))
    os.rename(os.path.join(dir,filename), os.path.join(dir,"Boletim 1ºBimestre - {}.pdf".format(cutReplace.title())))


if __name__ == '__main__':
    
    dir = r'D:\AULAS E MATERIAIS DIDÁTICOS DE GEOGRAFIA\CED DARCY RIBEIRO\FECHAMENTO DE NOTAS\1º BIMESTRE\BOLETINS\3G'

    #Como se trata de uma lista de arquivos, importante passar no loop
    for filename in os.listdir(dir):
        #Somente arquivos com final .pdf
        if filename.endswith(".pdf"):
            #Extraia o texto
            text_extractor(os.path.join(dir,filename))
            #Renomei o arquivo
            file_rename(os.path.join(dir,filename))
            #Printando resultado, novo nome!
            print(os.path.join(dir,filename))
        else:
            continue
    
