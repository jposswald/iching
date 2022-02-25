from random import randint
import random, time, json
def main():
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

        main.graf = False ##esto inicia sin el "modo graf"
        main.mut  = False # inicia sin modo mutante

        apurado = True
        def esperar():
            if apurado == False:
                time.sleep(1)
                wait()
                pass

        # el switch para las lineas

        six =  "───OO─── ||  ───  ───  ||────────|"
        sept=  "──────── ||  ────────  ||────────|"
        huit=  "───  ─── ||  ───  ───  ||───  ───|"
        neuf=  "───XX─── ||  ────────  ||───  ───|"
         # Lodibujito
        sept_fij=  "                  ──────── ||"
        huit_fij=  "                  ───  ─── ||"
        def seis():
            if main.graf == True:
                return  six
            return "Linea yin cambiante a yang."
        def siete():
            if main.graf == False:
                return "Linea yang estable."
            elif main.mut == False:
                return sept_fij
            else: return sept
        def ocho(): # apr0vech0 el switch y l0 reus0 despues para que grafique segun el numer0 q aparece
            if main.graf == False:
                return "Linea yin estable."
            elif main.mut == False:
                return huit_fij
            else: return huit
        def nueve():
            if main.graf == True:
                return neuf
            return "Linea yang cambiante a yin."

        switcher = {6: seis, 7: siete, 8: ocho, 9: nueve}

        def switch(lineas):
            return switcher.get(lineas)()
        ### definiendo las tiradas, esta es la random
        def tirar_1():
            texts = ["Primera tirada: ", "Segunda tirada: ", "Tercera tirada: ", "Cuarta tirada: ", "Quinta tirada: ", "Sexta tirada: ",]
            global resp_final_l, res_final
            i,x = 0, 1
            dic_respuesta = {} #aca se van a guardar las respuestas
            res_final = ""
            while i != 6:
                val1 = random.randint(2, 3)
                val2 = random.randint(2, 3)
                val3 = random.randint(2, 3)
                dic_respuesta["res"+str(x)] = sum([val1, val2, val3])
                soles = [val1, val2, val3].count(3)
                resp_final_l= sorted(dic_respuesta.items())
                print ((texts[i] +"1 sol. El resultado es: 7. "+ switch(resp_final_l[i][1]))if resp_final_l[i][1] == 7 else (texts[i] + "Ningun sol. El resultado es: 6. "+ switch(resp_final_l[i][1])) if resp_final_l[i][1] == 6 else (texts[i] + str(soles) + " soles. El resultado es: " + str(resp_final_l[i][1]) +". "+ switch(resp_final_l[i][1])))
                res_final += str(resp_final_l[i][1])
                i,x = i+1 ,x +1
                esperar()

        def check_input(txt): #se asegura que el input sea c0rrect0 para el m0d0 2
            while True:
                try:
                    inp = int(input(txt))
                except ValueError:
                        print("Error: Valor incorrecto, volve a intentar.")
                        txt = ""
                        continue
                else:
                    if (inp >= 0 and inp <= 3) and isinstance(inp, int):
                        return inp
                        break
                    else:
                        print("Error: El numero debe estar entre 0 y 3.")

        def tirar_2(): #tirada2
            texts = ["Primera tirada: ", "Segunda tirada: ", "Tercera tirada: ", "Cuarta tirada: ", "Quinta tirada: ", "Sexta tirada: ",]
            global resp_final_l, res_final
            i,x = 0, 1
            dic_respuesta = {} #aca se van a guardar las respuestas
            res_final = ""
            while i != 6:
                inp_res = check_input(texts[i])
                dic_respuesta["res"+str(x)] = inp_res + 6
                soles = dic_respuesta["res"+str(x)] - 6
                resp_final_l= sorted(dic_respuesta.items())
                print (("1 sol. El resultado es: 7. "+ switch(resp_final_l[i][1]))if resp_final_l[i][1] == 7 else ( "Ningun sol. El resultado es: 6. "+ switch(resp_final_l[i][1])) if resp_final_l[i][1] == 6 else (str(soles) + " soles. El resultado es: " + str(resp_final_l[i][1]) +". "+ switch(resp_final_l[i][1])))
                res_final += str(resp_final_l[i][1])
                i,x = i+1 ,x +1
                if apurado == False:
                    time.sleep(1)
        def convertir(text, dic): #esta mierda es para el m0d0 3, para que sea valid0 tant0 678 c0m0 012
            for i, v in dic.items():
                text = text.replace(i, v)
            return text
        def check_input_avanzado(txt): #se encarga del input del m0d0 3
            while True:
                    inp = input(txt)
                    if   (inp[0]) in "6789" and len(inp) == 6 and inp.isdigit():
                        return inp
                        break
                    elif (inp[0]) in "0123" and len(inp) == 6 and inp.isdigit():
                        return convertir(inp, { "0": "6", "1": "7", "2":"8" , "3":"9"})
                        break
                    else:
                        print("Entrada incorrecta. Debe tener 6 digitos.")
        def tirar_3():
            global resp_final_l, res_final
            res_final = str(check_input_avanzado("Escribi los numeros de la tirada:  (Ej: 678978 o 012312)\n\n"))
            if apurado == False:
                wait()

        def graficar():
            global mut
            main.graf = True
            if "6" in res_final or "9" in res_final:
                main.mut = True
            for asd in range(5,-1,-1):
                print(switch(int(res_final[asd])))

        def check_hex(a, b): #se fija el hexagrama y l0 c0mpara c0n la entry que esta en el j.s0n
            global n
            i, n = 0, 0
            while ([a, b]) != (data["Hexagramas"][n]["id"]):
                n= i
                i+=1

        def print_mut(): #se encarga de cambiar las lineas mutantes
            list_tiradas = []
            for c, v in enumerate(res_final):
                list_tiradas.append([])
                list_tiradas[c].extend([str(c+1),v])
            global linmut
            linmut = "Lineas cambiantes: "
            for x in list_tiradas:
                if int(x[1]) == 9:
                    linmut += (x[0]+ ",")
                elif int(x[1]) == 6:
                    linmut += (x[0]+ ",")
            else:
                if len(linmut) == 20:
                    print(linmut.replace("," , ".",)) # cambia la c0ma p0r un .
                else:
                    a = ".".join(linmut.rsplit(",", 1))
                    print(" y ".join(a.rsplit(",", 1))) # reemplaza la ultima , p0r un " y " y agrega un . al final
        def get_hex():
            triagrama_low, triagrama_up = res_final[0:3], res_final[3:7] #c0rta la res_finalpuesta en 2 mitades str
            triagrama_fijo_low = (triagrama_low.replace("9", "7")).replace("6", "8") #cambia el primer triagrama para que n0 hayan mutables para q sea mas facil
            triagrama_fijo_up = (triagrama_up.replace("9", "7")).replace("6", "8") # l0 mism0 c0n el segund0
            list_tri_low = list((triagrama_fijo_low.replace("7","1")).replace("8","0")) # c0nvierte a str binari0 l0s triagramas y desp
            list_tri_up = list((triagrama_fijo_up.replace("7","1")).replace("8","0")) # hace lista triagrama l0w y up, del hexagrama fij0
            bin_tri_low = [int(list_tri_low[0]), int(list_tri_low[1]), int(list_tri_low[2])]
            bin_tri_up = [int(list_tri_up[0]), int(list_tri_up[1]), int(list_tri_up[2])]
            check_hex(bin_tri_low, bin_tri_up)
            print("           Primer Hexagrama:", data["Hexagramas"][n].get("numero"), data["Hexagramas"][n].get("nombre"))
            if main.mut == True:
                triagrama_mut_low, triagrama_mut_up = (triagrama_low.replace("9", "8")).replace("6", "7"), (triagrama_up.replace("9", "8")).replace("6", "7")
                list_trim_low = list((triagrama_mut_low.replace("7","1")).replace("8","0"))
                list_trim_up = list((triagrama_mut_up.replace("7","1")).replace("8","0")) # aca hag0 l0 mism0 per0 c0n el mutante
                bin_trim_low = [int(list_trim_low[0]), int(list_trim_low[1]), int(list_trim_low[2])]
                bin_trim_up = [int(list_trim_up[0]), int(list_trim_up[1]), int(list_trim_up[2])]
                check_hex(bin_trim_low, bin_trim_up)
                print_mut()
                print("             Hexagrama mutante cambiando a...",data["Hexagramas"][n].get("numero"), data["Hexagramas"][n].get("nombre"))
            else:
                print("           Sin lineas mutantes.")

        def input_init(txt): #c0mienza el script. pide un input y segun la respuesta ejecuta l0s diferentes c0dig0s.
                while True:
                        inp_inicial = str(input(txt))
                        if inp_inicial == "1":
                            tirar_1(), graficar(), get_hex(),
                            break
                        elif inp_inicial == "2":
                            tirar_2(), graficar(), get_hex(),
                            break
                        elif inp_inicial == "3":
                            tirar_3(), graficar(), get_hex()
                            break
                        elif inp_inicial.casefold() in ["ayuda", "4", "help", "?"]:
                            print("ayudaaaaaaaaaaaa")
                            txt = ""
                            continue
                        elif inp_inicial.casefold() in ["salir", "exit"]:
                            exit()
                        else:
                            print("Entrada erronea. Presiona ayuda para ver comandos disponibles.")
                            txt = ""
                            continue

        texto = ("""Bienvenido al Iching virtual! \nPor favor, selecciona el modo que quieras presionando el numero correspondiente:
        \n1: Consulta Virtual. (Las tiradas son generadas digitalmente por este programa.)
        \n2: Lectura Fisica. (Con tus monedas reales, ingresas la cantidad de soles.)
        \n3: Modo Lectura Avanzada. (Para usuarios avanzados, se introduce solo los numeros del 6 al 9.)
        \n4: Ayuda.

        """)
        input_init(texto)

if __name__ == '__main__':
  main()
