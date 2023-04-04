from tkinter import *
import svgwrite

window = Tk()
window.title('Помощник вязальщика') 
window.geometry('1700x1000')
number_vertical = 10
number_gorizontal = 10
stcv = 10

#Функция печати ---------------------------------------------------------------------------

def printing():
    global number_vertical
    global number_gorizontal
    global stcv
    
    dwg = svgwrite.Drawing('помощник_вязальщика.svg')
    dwg['width'] = '297mm'
    dwg['height'] = '200mm'    
    
    otstup_vert_pixels = stcv / number_vertical
    otstup_vert = 10 * int(otstup_vert_pixels)
    otstup_vert_pixels_save = otstup_vert_pixels    
    
    for iw in range(250):
        dwg.add(dwg.line((str(otstup_vert) + 'mm', '0mm'), (str(otstup_vert) + 'mm', '300mm'), stroke = 'black', fill = 'black'))
        otstup_vert += otstup_vert_pixels_save * 10
        
    otstup_gorizont_pixels = stcv / number_gorizontal
    otstup_gorizont = 10 * int(otstup_gorizont_pixels)
    otstup_gorizont_pixels_save = otstup_gorizont_pixels    
    
    for iw in range(250):
        dwg.add(dwg.line(('0mm', str(otstup_gorizont) + 'mm'), ('297mm', str(otstup_gorizont) + 'mm'), stroke = 'black', fill = 'black'))
        otstup_gorizont += otstup_gorizont_pixels_save * 10    
        
    dwg.save()

    files()
        
#окошко для подтверждения -----------------------------------------------------------------
def files():

    oko = Tk()
    oko.title('')
    oko.geometry('450x150')
    Label(oko, text = 'файл сохранен!', font = ('Arial', 20)).place(x = 100, y = 10)
    Label(oko, text = 'вы можете найти файл под названием "помощник вязальщика.svg" ', font = ('Arial', 10)).place(x = 10, y = 50)
    Button(oko, text = 'OK', command = oko.destroy, width = 7, heigh = 2).place(x = 190, y = 90)
    mainloop()




#Функция прорисовки -----------------------------------------------------------------------
def paint():
    k = 0.75
    c.delete('all')
    i = 0
    otstup_vert_pixels = stcv / number_vertical
    otstup_vert = str(otstup_vert_pixels) + 'c'
    otstup_vert_pixels_save = otstup_vert_pixels
    
    c.delete('all')
    while i < 250:
        otstup_vert = str(otstup_vert_pixels / k) + 'c'
        c.create_line(otstup_vert, '0c' , otstup_vert, '20c' , width = 1, fill = 'black')
        i += 1
        otstup_vert_pixels += otstup_vert_pixels_save 
        
    j = 0
    otstup_gorizont_pixels = stcv / number_gorizontal
    otstup_gorizont = str(otstup_gorizont_pixels) + 'c'
    otstup_gorizont_pixels_save = otstup_gorizont_pixels
        
    while j < 200:
        otstup_gorizont = str(otstup_gorizont_pixels / k) + 'c'
        c.create_line('0c', otstup_gorizont , '40c', otstup_gorizont , width = 1, fill = 'black')
        j += 1
        otstup_gorizont_pixels += otstup_gorizont_pixels_save    
    
 
#Функции для вертикали --------------------------------------------------------------------

def plus_vertical():
    global number_vertical
    global stcv
    global number_gorizontal
    
    number_vertical += 1
    Label_text_vertical.set(number_vertical)    
    
    paint()
    

def minus_vertical():
    global number_vertical
    global stcv
    global number_gorizontal
    
    number_vertical -= 1
    Label_text_vertical.set(number_vertical)
    
    paint()
    
    

       
    
#Функции для горизонтали ------------------------------------------------------------------

def plus_gorizontal():
    global number_vertical
    global stcv
    global number_gorizontal
    number_gorizontal += 1
    Label_text_gorizontal.set(number_gorizontal)
    
    paint() 
        

def minus_gorizontal(): 
    global number_vertical
    global stcv
    global number_gorizontal
    number_gorizontal -= 1
    Label_text_gorizontal.set(number_gorizontal) 
    
    paint()     
#Функции для квадрата ---------------------------------------------------------------------

def plus_stcv():
    global number_vertical
    global stcv
    global number_gorizontal
    stcv += 1
    Label_text_stcv.set(stcv)

    paint()
    
    
    
def minus_stcv():
    global number_vertical
    global stcv
    global number_gorizontal
    stcv -= 1
    Label_text_stcv.set(stcv)
    
    paint()



#Петли по вертикали -----------------------------------------------------------------------
y1 = 150
Button(text = '+' , command = plus_vertical, width = 3, heigh = 1).place(x = 150, y = y1 - 15)
Button(text = '-' , command = minus_vertical, width = 3, heigh = 1).place(x = 150, y = y1 + 15)
Label_text_vertical = StringVar()
Label(textvariable = Label_text_vertical, width = 5).place(x = 110, y = y1)
Label(text = 'Петли по вертикали:' , width = 16).place(x = 0 , y = y1)

#Петли по горизонтали ---------------------------------------------------------------------
y2 = 220
Button(text = '+' , width = 3, heigh = 1, command = plus_gorizontal).place(x = 150, y = y2 - 15)
Button(text = '-' , width = 3, heigh = 1, command = minus_gorizontal).place(x = 150, y = y2 + 15)
Label_text_gorizontal = StringVar()
Label(textvariable = Label_text_gorizontal, width = 5).place(x = 120, y = y2)
Label(text = 'Петли по горизонтали:' , width = 17).place(x = 5 , y = y2)

#Сторона квадрата -------------------------------------------------------------------------
y3 = 80
Button(text = '+' , command = plus_stcv, width = 3, heigh = 1).place(x = 150, y = y3 - 15)
Button(text = '-' , command = minus_stcv, width = 3, heigh = 1).place(x = 150, y = y3 + 15)
Label_text_stcv = StringVar()
Label(textvariable = Label_text_stcv, width = 5).place(x = 110, y = y3)
Label(text = 'Сторона квадрата' , width = 16).place(x = 0 , y = y3)

#Печать ----------------------------------------------------------------------------------

Button(text = 'сохранить для печати' , font = ('Arial', 10), command = printing , heigh = 2 , width = 20).place(x = 0 , y = 300)


#Рисуем -----------------------------------------------------------------------------------

c = Canvas(width = '30c' , heigh = '20c' , bg = 'white')
c.place(x = 350 , y = 10)



i = 0
otstup_vert_pixels = stcv / number_vertical
otstup_vert = str(otstup_vert_pixels) + 'c'
otstup_vert_pixels_save = otstup_vert_pixels

while i < 30:
    otstup_vert = str(otstup_vert_pixels) + 'c'
    c.create_line(otstup_vert, '0c' , otstup_vert, '20c' , width = 1, fill = 'black')
    i += 1
    otstup_vert_pixels += otstup_vert_pixels_save
    

j = 0
otstup_gorizont_pixels = stcv / number_gorizontal
otstup_gorizont = str(otstup_gorizont_pixels) + 'c'
otstup_gorizont_pixels_save = otstup_gorizont_pixels

while j < 30:
    otstup_gorizont = str(otstup_gorizont_pixels) + 'c'
    c.create_line('0c', otstup_gorizont , '40c', otstup_gorizont , width = 1, fill = 'black')
    j += 1
    otstup_gorizont_pixels += otstup_gorizont_pixels_save
    
Label_text_stcv.set(stcv)
Label_text_vertical.set(number_vertical) 
Label_text_gorizontal.set(number_gorizontal)





mainloop()