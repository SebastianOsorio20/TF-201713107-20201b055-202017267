print("=========================================MENU====================================")
print("| Las horas puntas son de 6:00 hasta las 9:00 y de las 19:00 hasta las 22:00 \t |")
print("| Las horas mas bajas de trafico son de 22:00 hasta las 6:00 \t\t\t |")
print("| Las horas con trafico intermedio son de 9:00 hasta las 19:00 \t\t\t |")
print("=================================================================================")

hora = int (input("Digite la hora deseada"))
trafico = 0

if 6 < hora < 10:
  trafico = 1
if 18 < hora < 23:
 trafico = 1
if 23< hora < 24:
 trafico = 2
if 0 <hora<6:
  trafico = 2

if trafico == 0:
 adjlShow(NodoAlto, weighted=True, layout="neato")
if trafico == 2 :
  adjlShow(NodoBajo, weighted=True, layout="neato")
else:
 adjlShow(NodoMedio, weighted=True, layout="neato")