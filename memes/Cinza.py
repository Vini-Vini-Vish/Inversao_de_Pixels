# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 22:13:55 2021

@author: PC - CASA
"""

from PIL import Image  
  
def main():
    
    image = Image.open('C:/Users/PC - CASA/Downloads/DigitalImageProcessingSamples-master/DigitalImageProcessingSamples-master/Images/memes/Olha_a_morena.jpg')
    print(image.format)
    print(image.size)
    print(image.mode)
    print(image.bits)
    print(image.getextrema())
    
    convertedImage = image.convert('L')
    convertedImage.save('C:/Users/PC - CASA/Downloads/DigitalImageProcessingSamples-master/DigitalImageProcessingSamples-master/Images/memes/Convertida/Olha_a_morena.jpg')
    

if __name__ == "__main__":
    main()