# -*- coding: utf-8 -*-
#
# gregoriano.py
#
# Copyright © 2019 Julio Sánchez, Martín Vargas and Edwin Rees
#
# This file is part of Calendario_Gregoriano .
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Calendario_Gregoriano. If not, see <http ://www.gnu.org/licenses/>.
#

# The log store lines about execution of the program
log="I am the log\n"

# Name:         logger
# Date:         14/09/2019
# Author:       Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
# Description:  Store all information produced in running time.
#
# Parameters:   log_input: the string to be stored in the log.
#
def logger( log_input ):
    global log
    log=log+log_input+'\n'

# Name:     print_log
# Date:     15/09/2019
# Author:   Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
#Description: Just print the log
#
def print_log():
    global log
    print(log)

# Name:         is_valid_year
# Date:         14/09/2019
# Author:       Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
# Description:  Evaluate the conditions to determine if a year is valid according to gregorian calendar restrictions. (year>1582)
# 
# Parameters:
#               year:   integer value that holds the year for evaluate.
#
# Return:       True if the year is greather or equal than 1582, False in other case.
#
def is_valid_year(year):
    try:
        if(isinstance(year, int)):
            if ( year >= 1582 ):
                return True
            else:
                logger("year is less than 1582")
                return False
        else:
            logger("Value is not int")
    except:
        logger("Unknown Error in is_valid_year function")
        return False;


#R0
# Name:             fecha_es_tupla 
# Date:             14/09/2019
# Author:           Martín Vargas <martinvargas9622@gmail.com>
#
# Description:      Determine if the input is a valid tuple. Three positive integers.
#
# Variables:
#                   fecha :  The date to be evaluated
#
# Return:           True if the tuple is in a correct form, False if not.
#
def fecha_es_tupla(fecha):
    try:
        if type(fecha) is tuple:
            if(len(fecha)==3):
                for i in fecha:
                    if((type(i) != int) or (i <= 0)):
                        return False
                return True
            else:
                return False
        else:
            return False
    except:
        return False

#R1
# Name:         bisiesto
# Date:         14/09/2019
# Author:       Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
# Description:  Evaluate if a year is leap, according to restrictions on the gregorian calendar
#
# Parameters:
#               year: integer value that holds the year for evaluate.
#
# Return:       True if it is a leap year, Fals in other case.
#
# Restrictions:
#               restriction 1: if the last two digits of the year are divisible by 4, is leap, unless if year is divisible by 100.
#               restriction 2: if the year is divisible by 100, can not be leap, unless restriction 3 is fulfilled
#               restriction 3: if the year is divisible by 400, and the year last two digits are divisible by 4, and year is divisible by 100, te year is leap.
#
def bisiesto ( year ):
    try:
        if( is_valid_year( year) ):

            if ( (( year % 100) % 4) ==0 ): #restriction 1
                if ( year % 100 ) == 0:     #restriction 2
                    if ( year % 400 ) == 0: #restriction 3
                        logger( "Year "+str(year)+" is leap: It is divisible by 100 and also by 400" )
                        return True;
                    else:
                        logger( "Year "+str(year)+" is not leap: It is divisible by 100 but not divisible by 400" )
                        return False
                else:
                    logger( "Year "+str(year)+" is leap: Last two digits are divisible by 4, and it is not divisible by 100")
                    return True;
            else:
                logger("Year "+ str(year)+ " is not leap: Last two digits are not divisible by 4")
                return False
        else:
            logger("Year "+str(year)+" is not a year in acceptable options (less than 1582 or invalid value)")
            return False
    except:
        logger("Unknown Error in bisiesto function")
        return False




#R2
# Name:             fecha_es_valida
# Date:             14/9/19
# Author:           Edwin Rees Sandi <reesedwin1194@gmail.com>
#
# Description:      Determine if the date received is valid
#
# Parameters:
#                   fecha(year,month,day)
#
#
# Restrictions:
#                   if is leap-year, then february 29 is valid
#
def fecha_es_valida(fecha):
    if (fecha_es_tupla(fecha)):
        if fecha[0] == 1582:                        #since 1582
            if fecha[1] >= 10:                      #october
                if fecha[2] >= 15:                  #15 the Gregorian calendar begins
                    return fecha_es_valida_aux(fecha)
                else:
                    return False
            else:
                return False
        else:
            return fecha_es_valida_aux(fecha)
    else:
        return False


def fecha_es_valida_aux(fecha):
    if fecha[0] >= 1582:                #since 1582 the Gregorian calendar begins
        if fecha[1] == 2:               #check February
            if fecha[2] <= 28:
                return True
            elif fecha[2] == 29 and bisiesto(fecha[0]):     #if day is 29 and is a leap-year, then true
                return True
            else:
                return False
        elif fecha[1] in [4, 6, 9, 11]:                     #check months with 30 days
            if fecha[2] <= 30:
                return True
            else:
                return False
        elif fecha[1] in [1, 3, 5, 7, 8, 10, 12]:           #check months with 31 days
            if fecha[2] <= 31:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    

#R3
# Name:             dia_siguiente
# Date:             14/9/19
# Author:           Edwin Rees Sandi <reesedwin1194@gmail.com>
#
# Description:      Return the next day of the given date
#
# Parameters:
#                   fecha
#
# Restrictions:
#                   if is leap-year, then february 29 is valid
#
def dia_siguiente(fecha):
    if fecha_es_valida(fecha):                          #first check if the given date is valid
        fechaRes = (fecha[0], fecha[1], fecha[2]+1)     #add a day and if the date is valid, print it
        if fecha_es_valida(fechaRes):
            return fechaRes
        else:
            fechaRes = (fecha[0], fecha[1]+1, 1)        #if the last check failed, add a month and set day to 1
            if fecha_es_valida(fechaRes):
                return fechaRes
            else:
                fechaRes = (fecha[0]+1, 1, 1)           #if the last check failed, add a year and sets day to 1
                return fechaRes
    else:
        print("La fecha ingresada no es valida")



#R4
# Name:             dias_desde_primero_enero 
# Date:             14/09/2019
# Author:           Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
# Description:      Count the days between january 1st and a given valid date
#
# Variables:
#                   date: a tuple of 3 integers with the date to be evaluated (year, month, day)
#
# Return:           an integer value with the amount of days 
#
def dias_desde_primero_enero ( date ):

    try:
        if ( fecha_es_valida(date) ):
            days=date[2]-1         # Compute the amount of days during the actual month
            month=date[1]
            if( month>1 ):
                if(month==2):       
                    days=days+31    # Add the days of January
                elif(month<=7):
                    days=days+59    # Days of january and february
                    month=month-2
                elif(month<=12):
                    days=days+212   # Days of known past months until july. 31+28+((31*3)+(30*2))
                    month=month-7   
                while(month>1):
                    days=days+30
                    if( month%2 != 0 ):
                        days=days+1
                    month=month-1
                if(bisiesto(date[0])):
                    days=days+1
            logger(str(days) + " passed since 1/1/"+str(date[0])+" until "+ str(date[2])+"/"+str(date[1])+"/"+str(date[0]))        
            return days
        else:
            return -1
    except:
        logger( "Unknown Error in dias_desde_primero_enero function" )
        return -1





#R5
# Name:             dia_semana 
# Date:             14/09/2019
# Author:           Martín Vargas <martinvargas9622@gmail.com>
#
# Description:      Determine the day of the week acording to a given date
#
# Variables:
#                   fecha :  The date to be evaluated
#
# Return:           an integer value. 0 if Sunday, 1 if Monday, 2 if Tuesday, 3 if Wednesday, 4 if Thursday, 5 if Friday, 6 if Saturday.
#
def dia_semana(fecha):
    if(fecha_es_tupla(fecha) and fecha_es_valida(fecha)):
        try:
            offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            Febrero = 1
            if fecha[1] > 2: afterFeb = 0
            aux = fecha[0] - 1700 - Febrero
            dia  = 5
            dia += (aux + Febrero) * 365                     
            dia += aux / 4 - aux / 100 + aux / 400     
            dia += offset[fecha[1] - 1] + (fecha[2] - 1)               
            dia %= 7
            resultado = round(dia)
            if resultado == 7:
                return 0
            else:
                return resultado

        except:
            return -1;
    else:
        return -1

####################
# CODE FOR TESTING #
####################


# Name:             test_fecha_es_tupla
# Date:             15/9/2019
# Author:           Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
# Description:      is a simple tester for the function "fecha_es_tupla"
#
def test_fecha_es_tupla():
    print("\nTesting fecha_es_tupla function")
    correct=0
    incorrect=0
    dates= [(-1,-1,-1),(0,0,0),(-1,1,1),(1,-1,1),(1,1,-1),(-1,-1,1),(1,-1,-1),(-1,1,-1),(0,1,1),(1,0,1),(1,1,0),(1.5,5,5),(5,1.5,5),(5,5,1.5),(1,1,1),(100,100,100),(123456),("Hola"), ("1","2","3"),("Hola","a","todos"),(1,2),(1,2,3,4),(2000,10,10), (True,True,True)]
    answers=[False,     False,  False,   False,    False,   False,    False,    False,    False,  False,  False,  False,      False,  False,   True,    True,        False,    False,       False,      False,              False, False,    True, False]

    x=0
    while(x<len(answers)):
        if(fecha_es_tupla(dates[x])==answers[x]):
            correct=correct+1
        else:
            print("Incorrect value returned in function fecha_es_tupla. Input:"+str(dates[x])+". Expected value:"+str(answers[x])+". Returned value:"+str(fecha_es_tupla(dates[x])))
            incorrect=incorrect+1
        x=x+1
    print("From "+str(correct+incorrect)+" tests, "+str(correct)+" are correct, and "+str(incorrect)+" are incorrect.")


# Name:             test_bisiesto
# Date:             15/9/2019
# Author:           Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
# Description:      is a simple tester for the function "bisiesto"
#
def test_bisiesto():
    print("\nTesting bisiesto function")
    correct=0
    incorrect=0

    #These arrays are the oracle to determine if the answers returned are correct or not
    years=  [1100,  1582,   1583,   1999,   2000,   2001,   2002,   2003,   2004,   2005,   2006,   1500,   1600,   1700,   1800,   1900,   1901,   1902,   1903,   1904,   1905,   5000,   6000,   7000, -1, "Hola", 1.5]
    answers=[False, False,  False,  False,  True,   False,  False,  False,  True,   False,  False,  False,  True,   False,  False,  False,  False,  False,  False,  True,   False,  False,  True,   False, False, False, False]

    x=0
    while(x<len(years)):
        if(bisiesto(years[x])==answers[x]):
            correct=correct+1
        else:
            print("incorrect value returned in year "+str(years[x])+ ". Expected value:"+str(answers[x])+" ,returned value:"+str(bisiesto(years[x])))
            incorrect=incorrect+1
        x=x+1

    print("From "+str(correct+incorrect)+" tests, "+str(correct)+" are correct and "+str(incorrect)+" are incorrect.")


# Name:             test_fecha_es_valida
# Date:             15/9/19
# Author:           Edwin Rees Sandi <reesedwin1194@gmail.com>
#
# Description:      Simple tester for the function "fecha_es_valida"
#
def test_fecha_es_valida():
    print("\nTesting fecha_es_valida function")
    correct=0
    incorrect=0
    
    #These arrays are the oracle to determine if the answer returned is correct or not
    dates=[ (1582,10,15),(1582,10,14),(2000,1,1),(1999,12,31),(2000,2,29),(2001,2,30),(2002,2,29),(2003,4,12),(2004,1,31),(2005,1,32),(2006,3,31),(1900,4,31),(1901,5,31),(1902,6,31),(1903,7,31),(1904,7,1),(1905,8,31),(1900,9,31),(1901,9,30),(1902,10,31),(1903,11,31),(1904,11,30),(1905,12,31),(2000,12,30),(2001,12,32),(2002,2,28),(2004,2,29),(2008,2,29),(1800,2,29),(1900,2,29),(1,1,1),(-1,-1,-1),(1.5,1.5,1.5),("1","2","3"), "Hola"]
    answers=[True,          False,      True,      True,           True,       False,      False,      True,       True,       False,      True,       False,      True,   False,        True,        True,      True,       False,      True,        True,      False,        True,        True,        True,        False,     True,        True,      True,        False,     False,         False,  False,      False,      False,      False]

    x=0
    while(x<len(answers)):
        if(fecha_es_valida(dates[x]) == answers[x]):
            correct=correct+1
        else:
            print("incorrect value returned. Input:"+str(dates[x])+ ". Expected value:"+str(answers[x])+" ,returned value:"+str(fecha_es_valida(dates[x])))
            incorrect=incorrect+1
        x=x+1
    print("From "+str(correct+incorrect)+" tests, "+str(correct)+" are correct, and "+str(incorrect)+" are incorrect")


# Name:             test_dia_siguiente
# Date:             15/9/19
# Author:           Edwin Rees Sandi <reesedwin1194@gmail.com>
#
# Description:      Simple tester for the function "dia_siguiente"
#
def test_dia_siguiente():
    print("\nTesting dia_siguiente function")
    correct=0
    incorrect=0
    
    #These arrays are the oracle to determine if the answer returned is correct or not
    dates=[ (2000,1,1),(1999,12,31),(2000,2,29),(2001,2,28),(2002,2,28),(2003,4,12),(2004,1,31),(2005,1,31),(2006,3,31),(1900,4,30),(1901,5,31),(1902,6,30),(1903,7,31),(1904,7,1),(1905,8,31),(1900,9,30),(1901,9,29),(1902,10,31),(1903,11,30),(1904,11,15),(1905,12,31),(2000,12,30),(2001,12,30),(2002,2,28),(2004,2,29),(2008,2,29),(1800,2,28),(1900,2,28)]
    answers=[(2000,1,2),(2000,1,1),(2000,3,1),(2001,3,1),(2002,3,1),    (2003,4,13),(2004,2,1),(2005,2,1),(2006,4,1),(1900,5,1),    (1901,6,1),(1902,7,1),(1903,8,1),(1904,7,2),(1905,9,1),     (1900,10,1),(1901,9,30),(1902,11,1),(1903,12,1),(1904,11,16),(1906,1,1),(2000,12,31),(2001,12,31),(2002,3,1),(2004,3,1),    (2008,3,1),(1800,3,1),(1900,3,1)]

    x=0
    while(x<len(answers)):
        if(dia_siguiente(dates[x])==answers[x]):
            correct=correct+1
        else:
            print("incorrect value returned. Input:"+str(dates[x])+ ". Expected value:"+str(answers[x])+" ,returned value:"+str(dia_siguiente(dates[x])))
            incorrect=incorrect+1
        x=x+1
    print("From "+str(correct+incorrect)+" tests, "+str(correct)+" are correct, and "+str(incorrect)+" are incorrect")


# Name:             test_dias_desde_primero_enero
# Date:             15/9/19
# Author:           Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
# Description:      Simple tester for the function "dias_desde_primero_enero"
#
def test_dias_desde_primero_enero():
    print("\nTesting dias_desde_primero_enero function")
    correct=0
    incorrect=0
    
    #These arrays are the oracle to determine if the answer returned is correct or not
    dates=[ (2000,1,1),(1999,5,5),(2000,5,5),(2001,5,5),(2002,5,5),(2003,5,5),(2004,5,5),(2005,5,5),(2006,5,5),(1900,7,31),(1901,7,31),(1902,7,31),(1903,7,31),(1904,7,31),(1905,7,31),(1900,8,31),(1901,8,31),(1902,8,31),(1903,8,31),(1904,8,31),(1905,8,31),(2000,12,31),(2001,12,31),(2002,12,31),(2003,12,31),(2004,12,31),(2005,12,31),(2000,10,5),(-1,-1,-1),("1","2","3"),"Hola",(-1,-1,-1)]
    answers=[0,         124,        125,        124,        124,        124,    125,        124,        124,        211,        211,        211,        211,        212,        211,    242,            242,        242,        242,        243,        242,        365,        364,        364,        364,            365,        364,        278, -1, -1, -1, -1]

    x=0
    while(x<len(answers)):
        if(dias_desde_primero_enero(dates[x])==answers[x]):
            correct=correct+1
        else:
            print("incorrect value returned. Input:"+str(dates[x])+ ". Expected value:"+str(answers[x])+" ,returned value:"+str(dias_desde_primero_enero(dates[x])))
            incorrect=incorrect+1
        x=x+1
    print("From "+str(correct+incorrect)+" tests, "+str(correct)+" are correct, and "+str(incorrect)+" are incorrect")


# Name:             test_dia_semana
# Date:             15/9/19
# Author:           Julio Sánchez Jiménez <julio.sanchezjimenez@ucr.ac.cr>
#
# Description:      Simple tester for the function "dia_semana"
#
def test_dia_semana():
    print("\nTesting dia_semana function")
    correct=0
    incorrect=0

    dates=[ (1,1,1), (-1,-1,-1), (1.5,1.5,1.5), (2019,9,15), (1582,10,15), (1582,10,14),    "Hola",(2019,9,16),(2019,9,17),(2019,9,18),(2019,9,19),(2019,9,20),(2019,9,21)]
    answers=[-1,        -1,         -1,             0,              5,           -1,        -1,         1,          2,          3,          4,          5,         6]

    x=0
    while(x<len(answers)):
        if(dia_semana(dates[x])==answers[x]):
            correct=correct+1
        else:
            print("incorrect value returned. Input:"+str(dates[x])+ ". Expected value:"+str(answers[x])+" ,returned value:"+str(dia_semana(dates[x])))
            incorrect=incorrect+1
        x=x+1
    print("From "+str(correct+incorrect)+" tests, "+str(correct)+" are correct, and "+str(incorrect)+" are incorrect")

test_fecha_es_tupla()
test_bisiesto()
test_fecha_es_valida()
test_dia_siguiente()
test_dias_desde_primero_enero()
test_dia_semana()


    
