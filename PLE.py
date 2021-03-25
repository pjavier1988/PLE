import pandas as pd
import numpy as np
import pulp
import itertools


#Definicion de Conjuntos
Docentes = ["ING. M. V","ING. J. Y","DRA. MARIA L","ING. R. B","ING. M. F", "ING. R. G","LCDO. K. Z"]
Materias = ["CALCULO DE UNA VARIABLE","INTRODUCC. C. COMPUT.","ANTROPOLOGIA","ALGEBRA LINEAL","CALCULO 1 VARIABLE PR","COMUNICA. ORAL Y ES.","LOGICA","ALGEBRA LINEAL PR","TEORIA CRITICA"]
Periodos = ["1","2","3","4","5","6","7"]
Periodos2 = {"0": "07:00-09:00", "1": "09:00-11:00", "2": "11:00-13:00", "3": "13:00-15:00", "4": "15:00-17:00",
             "5": "17:00-19:00", "6": "19:00-21:00"}
Dias=["1","2","3","4","5"]
Dias2={0: "Lunes", 1: "Martes", 2: "Miercoles", 3: "Jueves", 4: "Viernes", 5:"Sabado"}
Ciclos=["1","2","3","4","5","6","7","8","9","10"]
Ciclos2={0:"1",1:"1",2:"1",3:"1",4:"1",5:"1",6:"1",7:"1",8:"2"}
Creditos=[3, 2, 1, 2, 2, 2, 1, 1,1]

#Definicion de los tamaños de los conjuntos
numero_de_docentes=np.size(Docentes)
numero_de_materias=np.size(Materias)
numero_de_periodos=len(Periodos2.keys())

numero_de_dias=len(Dias2.keys())
#numero_de_ciclos=np.size(Ciclos)
numero_de_ciclos=2
Tijl=np.zeros((numero_de_docentes,numero_de_dias,numero_de_periodos))
Materias2=np.zeros((numero_de_ciclos,numero_de_materias))
'''Días en los que los docentes pueden ser asignados
1 tiene disponibilidad
-10 no tiene disponibilidad
Este criterio se eligió porque se necesita maximizar la función
'''
#Docente 1 Lunes
Tijl[0][0][0]=1
Tijl[0][0][1]=1
Tijl[0][0][2]=-10
Tijl[0][0][3]=-10
Tijl[0][0][4]=1
Tijl[0][0][5]=1
Tijl[0][0][6]=1
#Docente 1 Martes
Tijl[0][1][0]=-10
Tijl[0][1][1]=-10
Tijl[0][1][2]=-10
Tijl[0][1][3]=-10
Tijl[0][1][4]=-10
Tijl[0][1][5]=-10
Tijl[0][1][6]=-10
#Docente 1 Miercoles
Tijl[0][2][0]=-10
Tijl[0][2][1]=-10
Tijl[0][2][2]=1
Tijl[0][2][3]=1
Tijl[0][2][4]=1
Tijl[0][2][5]=1
Tijl[0][2][6]=1
#Docente 1 Jueves
Tijl[0][3][0]=-10
Tijl[0][3][1]=-10
Tijl[0][3][2]=-10
Tijl[0][3][3]=-10
Tijl[0][3][4]=-10
Tijl[0][3][5]=-10
Tijl[0][3][6]=-10
#Docente 1 Viernes
Tijl[0][4][0]=-10
Tijl[0][4][1]=-10
Tijl[0][4][2]=1
Tijl[0][4][3]=1
Tijl[0][4][4]=-10
Tijl[0][4][5]=-10
Tijl[0][4][6]=-10
#Docente 1 Sabado
Tijl[0][5][0]=1
Tijl[0][5][1]=1
Tijl[0][5][2]=-10
Tijl[0][5][3]=-10
Tijl[0][5][4]=-10
Tijl[0][5][5]=-10
Tijl[0][5][6]=-10

#Docente 2 Lunes
Tijl[1][0][0]=-10
Tijl[1][0][1]=-10
Tijl[1][0][2]=-10
Tijl[1][0][3]=-10
Tijl[1][0][4]=-10
Tijl[1][0][5]=-10
Tijl[1][0][6]=-10
#Docente 2 Martes
Tijl[1][1][0]=-10
Tijl[1][1][1]=1
Tijl[1][1][2]=1
Tijl[1][1][3]=1
Tijl[1][1][4]=-10
Tijl[1][1][5]=-10
Tijl[1][1][6]=-10
#Docente 2 Miercoles
Tijl[1][2][0]=1
Tijl[1][2][1]=1
Tijl[1][2][2]=-10
Tijl[1][2][3]=-10
Tijl[1][2][4]=-10
Tijl[1][2][5]=-10
Tijl[1][2][6]=-10
#Docente 1 Jueves
Tijl[1][3][0]=1
Tijl[1][3][1]=1
Tijl[1][3][2]=1
Tijl[1][3][3]=-10
Tijl[1][3][4]=-10
Tijl[1][3][5]=-10
Tijl[1][3][6]=-10
#Docente 1 Viernes
Tijl[1][4][0]=1
Tijl[1][4][1]=1
Tijl[1][4][2]=-10
Tijl[1][4][3]=-10
Tijl[1][4][4]=1
Tijl[1][4][5]=1
Tijl[1][4][6]=1
#Docente 1 Sabado
Tijl[1][5][0]=-10
Tijl[1][5][1]=-10
Tijl[1][5][2]=-10
Tijl[1][5][3]=-10
Tijl[1][5][4]=-10
Tijl[1][5][5]=-10
Tijl[1][5][6]=-10

#Docente 3 Lunes
Tijl[2][0][0] = 1
Tijl[2][0][1] = 1
Tijl[2][0][2] = -10
Tijl[2][0][3] = -10
Tijl[2][0][4] = 1
Tijl[2][0][5]=1
Tijl[2][0][6]=1
#Docente 3 Martes
Tijl[2][1][0]=1
Tijl[2][1][1]=-10
Tijl[2][1][2]=-10
Tijl[2][1][3]=-10
Tijl[2][1][4]=1
Tijl[2][1][5]=-10
Tijl[2][1][6]=-10
#Docente 3 Miercoles
Tijl[2][2][0]=-10
Tijl[2][2][1]=-10
Tijl[2][2][2]=1
Tijl[2][2][3]=1
Tijl[2][2][4]=1
Tijl[2][2][5]=1
Tijl[2][2][6]=1
#Docente 3 Jueves
Tijl[2][3][0]=-10
Tijl[2][3][1]=-10
Tijl[2][3][2]=-10
Tijl[2][3][3]=-10
Tijl[2][3][4]=1
Tijl[2][3][5]=1
Tijl[2][3][6]=1
#Docente 3 Viernes
Tijl[2][4][0]=-10
Tijl[2][4][1]=-10
Tijl[2][4][2]=1
Tijl[2][4][3]=1
Tijl[2][4][4]=-10
Tijl[2][4][5]=-10
Tijl[2][4][6]=-10
#Docente 3 Sabado
Tijl[2][5][0]=1
Tijl[2][5][1]=1
Tijl[2][5][2]=-10
Tijl[2][5][3]=-10
Tijl[2][5][4]=-10
Tijl[2][5][5]=-10
Tijl[2][5][6]=-10


#Docente 4 Lunes
Tijl[3][0][0] = 1
Tijl[3][0][1] = 1
Tijl[3][0][2] = -10
Tijl[3][0][3] = -10
Tijl[3][0][4] = 1
Tijl[3][0][5]=1
Tijl[3][0][6]=1
#Docente 4 Martes
Tijl[3][1][0]=1
Tijl[3][1][1]=-10
Tijl[3][1][2]=-10
Tijl[3][1][3]=-10
Tijl[3][1][4]=1
Tijl[3][1][5]=-10
Tijl[3][1][6]=-10
#Docente 4 Miercoles
Tijl[3][2][0]=-10
Tijl[3][2][1]=-10
Tijl[3][2][2]=1
Tijl[3][2][3]=1
Tijl[3][2][4]=1
Tijl[3][2][5]=1
Tijl[3][2][6]=1
#Docente 4 Jueves
Tijl[3][3][0]=-10
Tijl[3][3][1]=-10
Tijl[3][3][2]=-10
Tijl[3][3][3]=-10
Tijl[3][3][4]=1
Tijl[3][3][5]=1
Tijl[3][3][6]=1
#Docente 4 Viernes
Tijl[3][4][0]=-10
Tijl[3][4][1]=-10
Tijl[3][4][2]=1
Tijl[3][4][3]=1
Tijl[3][4][4]=-10
Tijl[3][4][5]=-10
Tijl[3][4][6]=-10
#Docente 4 Sabado
Tijl[3][5][0]=1
Tijl[3][5][1]=1
Tijl[3][5][2]=-10
Tijl[3][5][3]=-10
Tijl[3][5][4]=-10
Tijl[3][5][5]=-10
Tijl[3][5][6]=-10

#Docente 5 Lunes
Tijl[4][0][0] = 1
Tijl[4][0][1] = 1
Tijl[4][0][2] = -10
Tijl[4][0][3] = -10
Tijl[4][0][4] = 1
Tijl[4][0][5]=1
Tijl[4][0][6]=1
#Docente 5 Martes
Tijl[4][1][0]=1
Tijl[4][1][1]=-10
Tijl[4][1][2]=-10
Tijl[4][1][3]=1
Tijl[4][1][4]=1
Tijl[4][1][5]=-10
Tijl[4][1][6]=-10
#Docente 5 Miercoles
Tijl[4][2][0]=-10
Tijl[4][2][1]=-10
Tijl[4][2][2]=1
Tijl[4][2][3]=1
Tijl[4][2][4]=1
Tijl[4][2][5]=1
Tijl[4][2][6]=1
#Docente 4 Jueves
Tijl[4][3][0]=-10
Tijl[4][3][1]=-10
Tijl[4][3][2]=-10
Tijl[4][3][3]=-10
Tijl[4][3][4]=1
Tijl[4][3][5]=1
Tijl[4][3][6]=1
#Docente 5 Viernes
Tijl[4][4][0]=-10
Tijl[4][4][1]=-10
Tijl[4][4][2]=1
Tijl[4][4][3]=1
Tijl[4][4][4]=-10
Tijl[4][4][5]=-10
Tijl[4][4][6]=-10
#Docente 5 Sabado
Tijl[4][5][0]=1
Tijl[4][5][1]=1
Tijl[4][5][2]=-10
Tijl[4][5][3]=-10
Tijl[4][5][4]=-10
Tijl[4][5][5]=-10
Tijl[4][5][6]=-10


#Docente 6 Lunes
Tijl[5][0][0] = 1
Tijl[5][0][1] = 1
Tijl[5][0][2] = -10
Tijl[5][0][3] = -10
Tijl[5][0][4] = 1
Tijl[5][0][5]=1
Tijl[5][0][6]=1
#Docente 6 Martes
Tijl[5][1][0]=1
Tijl[5][1][1]=-10
Tijl[5][1][2]=-10
Tijl[5][1][3]=1
Tijl[5][1][4]=1
Tijl[5][1][5]=-10
Tijl[5][1][6]=-10
#Docente 6 Miercoles
Tijl[5][2][0]=-10
Tijl[5][2][1]=-10
Tijl[5][2][2]=1
Tijl[5][2][3]=1
Tijl[5][2][4]=1
Tijl[5][2][5]=-10
Tijl[5][2][6]=-10
#Docente 6 Jueves
Tijl[5][3][0]=-10
Tijl[5][3][1]=-10
Tijl[5][3][2]=-10
Tijl[5][3][3]=-10
Tijl[5][3][4]=1
Tijl[5][3][5]=1
Tijl[5][3][6]=1
#Docente 6 Viernes
Tijl[5][4][0]=-10
Tijl[5][4][1]=-10
Tijl[5][4][2]=1
Tijl[5][4][3]=1
Tijl[5][4][4]=-10
Tijl[5][4][5]=-10
Tijl[5][4][6]=-10
#Docente 6 Sabado
Tijl[5][5][0]=1
Tijl[5][5][1]=1
Tijl[5][5][2]=-10
Tijl[5][5][3]=-10
Tijl[5][5][4]=-10
Tijl[5][5][5]=-10
Tijl[5][5][6]=-10




#Docente 7 Lunes
Tijl[6][0][0] = 1
Tijl[6][0][1] = 1
Tijl[6][0][2] = -10
Tijl[6][0][3] = -10
Tijl[6][0][4] = 1
Tijl[6][0][5]=1
Tijl[6][0][6]=1
#Docente 7 Martes
Tijl[6][1][0]=1
Tijl[6][1][1]=-10
Tijl[6][1][2]=-10
Tijl[6][1][3]=1
Tijl[6][1][4]=1
Tijl[6][1][5]=-10
Tijl[6][1][6]=-10
#Docente 7 Miercoles
Tijl[6][2][0]=-10
Tijl[6][2][1]=-10
Tijl[6][2][2]=1
Tijl[6][2][3]=1
Tijl[6][2][4]=1
Tijl[6][2][5]=1
Tijl[6][2][6]=1
#Docente 7 Jueves
Tijl[6][3][0]=-10
Tijl[6][3][1]=-10
Tijl[6][3][2]=-10
Tijl[6][3][3]=-10
Tijl[6][3][4]=1
Tijl[6][3][5]=1
Tijl[6][3][6]=1
#Docente 7 Viernes
Tijl[6][4][0]=-10
Tijl[6][4][1]=-10
Tijl[6][4][2]=1
Tijl[6][4][3]=1
Tijl[6][4][4]=1
Tijl[6][4][5]=1
Tijl[6][4][6]=-10
#Docente 7 Sabado
Tijl[6][5][0]=-10
Tijl[6][5][1]=-10
Tijl[6][5][2]=-10
Tijl[6][5][3]=-10
Tijl[6][5][4]=-10
Tijl[6][5][5]=-10
Tijl[6][5][6]=-10


'''Matriz de pertinencia de docente según materia
'''
alfa_ik=np.zeros((numero_de_docentes,numero_de_materias))
#Puntajes docente1
alfa_ik[0][0]=0.9
alfa_ik[0][1]=0
alfa_ik[0][2]=0
alfa_ik[0][3]=0
alfa_ik[0][4]=0
alfa_ik[0][5]=0
alfa_ik[0][6]=0
alfa_ik[0][7]=0
alfa_ik[0][8]=0
#Puntajes docente2
alfa_ik[1][0]=0
alfa_ik[1][1]=1
alfa_ik[1][2]=0
alfa_ik[1][3]=0
alfa_ik[1][4]=0
alfa_ik[1][5]=0
alfa_ik[1][6]=0
alfa_ik[1][7]=0
alfa_ik[1][8]=0
#Puntajes docente3
alfa_ik[2][0]=0
alfa_ik[2][1]=0
alfa_ik[2][2]=1
alfa_ik[2][3]=0
alfa_ik[2][4]=0
alfa_ik[2][5]=1
alfa_ik[2][6]=0
alfa_ik[2][7]=0.6
alfa_ik[2][8]=0
#Puntajes docente4
alfa_ik[3][0]=0
alfa_ik[3][1]=0
alfa_ik[3][2]=0
alfa_ik[3][3]=1
alfa_ik[3][4]=0
alfa_ik[3][5]=0
alfa_ik[3][6]=0
alfa_ik[3][7]=1
alfa_ik[3][8]=0
#Puntajes docente5
alfa_ik[4][0]=0
alfa_ik[4][1]=0
alfa_ik[4][2]=0
alfa_ik[4][3]=0
alfa_ik[4][4]=1
alfa_ik[4][5]=0
alfa_ik[4][6]=0
alfa_ik[4][7]=0
alfa_ik[4][8]=0
#Puntajes docente6
alfa_ik[5][0]=0
alfa_ik[5][1]=0
alfa_ik[5][2]=0
alfa_ik[5][3]=0
alfa_ik[5][4]=0
alfa_ik[5][5]=0
alfa_ik[5][6]=1
alfa_ik[5][7]=0
alfa_ik[5][8]=0
#Puntajes docente7
alfa_ik[6][0]=0
alfa_ik[6][1]=0
alfa_ik[6][2]=0
alfa_ik[6][3]=0
alfa_ik[6][4]=0
alfa_ik[6][5]=1
alfa_ik[6][6]=0
alfa_ik[6][7]=0
alfa_ik[6][8]=1

#llenar la matriz de materias



df = pd.read_excel("Disponibilidad2.xlsx")





#Definición del problema de minimización
prob = pulp.LpProblem("Asignacion Horarios",pulp.LpMaximize)

x = pulp.LpVariable.dicts("x", itertools.product(range(numero_de_docentes),
range(numero_de_dias), range(numero_de_materias), range(numero_de_periodos), range(numero_de_ciclos)), cat=pulp.LpBinary)
print("Imprimiendo Xijklm")
print(x)

#Definicion de la función objetivo
funcion_objetivo = 0
contador=0
for docente in range(numero_de_docentes):
    for dia in range(numero_de_dias):
        for materia in range(numero_de_materias):
            for periodo in range(numero_de_periodos):
                for ciclo in range(numero_de_ciclos):
                    funcion_objetivo += (x[(docente, dia, materia,periodo,ciclo)]*Tijl[docente][dia][periodo]*alfa_ik[docente][materia])


prob += funcion_objetivo
print("Imprimiendo función objetivo")
print(funcion_objetivo)


#Definición de restricciones

#Restricción 1
for dia in range(numero_de_dias):
                    prob += sum(x[(docente, dia,materia,periodo,ciclo)] for periodo in range(numero_de_periodos) for ciclo in range(numero_de_ciclos) for docente in range(numero_de_docentes) for materia in range(numero_de_materias) ) >= 1


#Restricción 1
for periodo in range(numero_de_periodos):
        for dia in range(numero_de_dias):
                    prob += sum(x[(docente, dia,materia,periodo,ciclo)] for ciclo in range(numero_de_ciclos) for docente in range(numero_de_docentes) for materia in range(numero_de_materias) ) <= 1


#Restricción 2
for docente in range(numero_de_docentes):
        for dia in range(numero_de_dias):
            for materia in range(numero_de_materias):
                    prob += sum(x[(docente, dia,materia,periodo,ciclo)]for ciclo in range(numero_de_ciclos) for periodo in range(numero_de_periodos)) <= 1


#Restricción 3
for docente in range(numero_de_docentes):
        for dia in range(numero_de_dias):
            for periodo in range(numero_de_periodos):
                    prob += sum(x[(docente, dia, materia, periodo, ciclo)]for ciclo in range(numero_de_ciclos) for materia in range(numero_de_materias)) <= 1
#Restricción 4
for materia in range(numero_de_materias):
    prob += sum(x[(docente, dia,materia,periodo,ciclo)] for dia in range(numero_de_dias)
                for periodo in range(numero_de_periodos) for docente in range(numero_de_docentes)
                for ciclo in range(numero_de_ciclos)) == Creditos[ciclo]

prob.writeLP("W modeloTesis.lp")
prob.solve(pulp.GLPK(options=['--mipgap', '1']))
print(prob.noOverlap)

solution = []

for docente in range(numero_de_docentes):
    for dia in range(numero_de_dias):
        for materia in range(numero_de_materias):
            for periodo in range(numero_de_periodos):
                for ciclo in range(numero_de_ciclos):
                    if x[(docente, dia, materia,periodo,ciclo)].value() == 1:
                        solution.append([dia,Dias2[dia],Docentes[docente], Materias[materia],Periodos2[str(periodo)],periodo,Ciclos2[materia]])

                        #print("El docente es ", Docentes[docente]+" con la materia ", Materias[materia]," el horario de ",
                              #Periodos2[str(periodo)], " el día "+Dias2[dia]+" del ciclo "+Ciclos2[materia])


df = pd.DataFrame(solution, columns=["Ind","Dia","Docente", "Materia","Hora", "Ind_Per","Ciclo"])

df.sort_values(['Ind', "Ind_Per",'Docente'], ascending=[True, True,True], inplace=True)
df = df.drop('Ind', 1)
df = df.drop('Ind_Per', 1)


print(df)
