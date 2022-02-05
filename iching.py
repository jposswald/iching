from random import randint
import random, time, json
 ###
# 3 yan 2 yin

with open('j.json') as f:
  data = json.load(f)  ## abriend0 el js0n, y abaj0 definiend0 l0 que van a ser l0s triagramas
  f.close()
tr_1, tr_2, tr_3, tr_4, tr_5, tr_6, tr_7, tr_8 = [0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1],

# el coso para esperar. Por ahora esto es solo para unix.
# Se que para windows hay otra, tendre que rescribirlo para que sea compatible
# o bien tendre que buscar otra manera.
def wait():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        print("...........")

        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

### el switch para las lineas
graf = 0 ##esto inicia sin el "modo graf"
mut  = 0 # inicia sin modo mutante

six =  "───OO─── ||  ───  ───  ||────────|"
sept=  "──────── ||  ────────  ||────────|"
huit=  "───  ─── ||  ───  ───  ||───  ───|"
neuf=  "───XX─── ||  ────────  ||───  ───|"
 # Lodibujito
sept_fij=  "                  ──────── ||"
huit_fij=  "                  ───  ─── ||"
def seis():
    if graf == True:
        return  six
    return "Linea yin cambiante a yang."
def siete():
    if graf == False:
        return "Linea yang estable."
    elif mut == False:
        return sept_fij
    else: return sept
def ocho():
    if graf == False:
        return "Linea yin estable."
    elif mut == False:
        return huit_fij
    else: return huit
def nueve():
    if graf == True:
        return neuf
    return "Linea yang cambiante a yin."

switcher = {
    6: seis,
    7: siete,
    8: ocho,
    9: nueve,}

def switch(lineas):
    return switcher.get(lineas)()
### definiendo las tiradas
def t1():
    global res1
    val1 = random.randint(2, 3)
    val2 = random.randint(2, 3)  ## res1 es el resultado de la tirada, soles cuenta.
    val3 = random.randint(2, 3) ## y el switch te dice si la linea es yin/yang y cambiante o no
    list_val = [val1, val2, val3] ## despues espera para hacerlo mas _ominoso_ y espera un input para seguir
    soles = list_val.count(3)
    res1 = sum(list_val)
    print ("Primera tirada: " + ((str(soles) + " sol. El resultado es: " + str(res1) +". "+ switch(res1))if res1 == 7 else (str(soles) + " soles. El resultado es: " + str(res1) +". "+ switch(res1))))
    time.sleep(1)
    wait()
def t2():
    global res2
    val1 = random.randint(2, 3)
    val2 = random.randint(2, 3)
    val3 = random.randint(2, 3)
    list_val = [val1, val2, val3]
    soles = list_val.count(3)
    res2 = sum(list_val)
    print ("Segunda tirada: " + ((str(soles) + " sol. El resultado es: " + str(res2) +". "+ switch(res2))if res2 == 7 else (str(soles) + " soles. El resultado es: " + str(res2) +". "+ switch(res2))))
    time.sleep(1)
    wait()
def t3():
    global res3
    val1 = random.randint(2, 3)
    val2 = random.randint(2, 3)
    val3 = random.randint(2, 3)
    list_val = [val1, val2, val3]
    soles = list_val.count(3)
    res3 = sum(list_val)
    print ("Tercera tirada: " + ((str(soles) + " sol. El resultado es: " + str(res3) +". "+ switch(res3))if res3 == 7 else (str(soles) + " soles. El resultado es: " + str(res3) +". "+ switch(res3))))
    time.sleep(1)
    wait()
def t4():
    global res4
    val1 = random.randint(2, 3)
    val2 = random.randint(2, 3)
    val3 = random.randint(2, 3)
    list_val = [val1, val2, val3]
    soles = list_val.count(3)
    res4 = sum(list_val)
    print ("Cuarta tirada: " + ((str(soles) + " sol. El resultado es: " + str(res4) +". "+ switch(res4))if res4 == 7 else (str(soles) + " soles. El resultado es: " + str(res4) +". "+ switch(res4))))
    time.sleep(1)
    wait()
def t5():
    global res5
    val1 = random.randint(2, 3)
    val2 = random.randint(2, 3)
    val3 = random.randint(2, 3)
    list_val = [val1, val2, val3]
    soles = list_val.count(3)
    res5 = sum(list_val)
    print ("Quinta tirada: " + ((str(soles) + " sol. El resultado es: " + str(res5) +". "+ switch(res5))if res5 == 7 else (str(soles) + " soles. El resultado es: " + str(res5) +". "+ switch(res5))))
    time.sleep(1)
    wait()
def t6():
    global res6
    val1 = random.randint(2, 3)
    val2 = random.randint(2, 3)
    val3 = random.randint(2, 3)
    list_val = [val1, val2, val3]
    soles = list_val.count(3)
    res6 = sum(list_val)
    print ("Sexta tirada: " + ((str(soles) + " sol. El resultado es: " + str(res6) +". "+ switch(res6))if res6 == 7 else (str(soles) + " soles. El resultado es: " + str(res6) +". "+ switch(res6))))
    time.sleep(1)
    wait()
def tirar():
    t1(), t2(), t3(), t4(), t5(), t6()
def graficar():
    global graf, mut
    graf = True
    if "6" in res_final or "9" in res_final:
        mut = True
    print(switch(res6))
    print(switch(res5))
    print(switch(res4))
    print(switch(res3))
    print(switch(res2))
    print(switch(res1))

def check_hex(a, b):
    global n
    i, n = 0, 0
    while ([a, b]) != (data["Hexagramas"][n]["id"]):
        n= i
        i+=1
def print_mut():
    list_tiradas = [
    ["1",int(res1)],
    ["2",int(res2)],
    ["3",int(res3)],
    ["4",int(res4)],
    ["5",int(res5)],
    ["6",int(res6)]
    ]
    global linmut
    linmut = "Lineas cambiantes: "
    for x in list_tiradas:
        if x[1] == 9:
            linmut += (x[0]+ ",")
        elif x[1] == 6:
            linmut += (x[0]+ ",")
    else:
        if len(linmut) == 20:
            print(linmut.replace("," , ".",)) # cambia la c0ma p0r un .
        else:
            a = ".".join(linmut.rsplit(",", 1))
            print(" y ".join(a.rsplit(",", 1))) # reemplaza la ultima , p0r un " y " y agrega un . al final
def verificar_1():
    split_res_final_1, split_res_final_2 = res_final[0:3], res_final[3:7] #c0rta la res_finalpuesta en 2 mitades str
    triagrama_fijo1 = (split_res_final_1.replace("9", "7")).replace("6", "8") #cambia el primer triagrama para que n0 hayan mutables para q sea mas facil
    triagrama_fijo2 = (split_res_final_2.replace("9", "7")).replace("6", "8") # l0 mism0 c0n el segund0
    list_tri_low = list((triagrama_fijo1.replace("7","1")).replace("8","0")) # c0nvierte a str binari0 l0s triagramas y desp
    list_tri_up = list((triagrama_fijo2.replace("7","1")).replace("8","0")) # hace lista triagrama l0w y up, del hexagrama fij0
    bin_tri_low = [int(list_tri_low[0]), int(list_tri_low[1]), int(list_tri_low[2])]
    bin_tri_up = [int(list_tri_up[0]), int(list_tri_up[1]), int(list_tri_up[2])]
    check_hex(bin_tri_low, bin_tri_up)
    print("           Primer Hexagrama:", data["Hexagramas"][n].get("numero"), data["Hexagramas"][n].get("nombre"))


    if mut == True:
        triagrama_mut1, triagrama_mut2 = (split_res_final_1.replace("9", "8")).replace("6", "7"), (split_res_final_2.replace("9", "8")).replace("6", "7")
        list_trim_low = list((triagrama_mut1.replace("7","1")).replace("8","0"))
        list_trim_up = list((triagrama_mut2.replace("7","1")).replace("8","0")) # aca hag0 l0 mism0 per0 c0n el mutante
        bin_trim_low = [int(list_trim_low[0]), int(list_trim_low[1]), int(list_trim_low[2])]
        bin_trim_up = [int(list_trim_up[0]), int(list_trim_up[1]), int(list_trim_up[2])]
        check_hex(bin_trim_low, bin_trim_up)
        print_mut()
        print("             Hexagrama mutante cambiando a...",data["Hexagramas"][n].get("numero"), data["Hexagramas"][n].get("nombre"))
    else:
        print("           Sin lineas mutantes.")
print ("Bienvenido al Iching virtual! \nPensa en tu pregunta y apreta cualquier tecla.")
wait()
tirar()
res_final = str(f'{res1}{res2}{res3}{res4}{res5}{res6}')

print("El resultado final es", res_final + "\n Tu hexagrama es:")
graficar()
verificar_1()
