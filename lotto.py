# il lotto ha una lunghezza di 5 numeri
# i primi 3 numeri rappresentano il numero del giorno rispetto all'anno
# esempio il 01/01/2018 sarà rappresentato come 001
# il 31/12/2017 sarà rappresentato come 365
# le altre due cifre servono ad identificare l'anno 
# e altro non sono che gli ultimi due numeri dell'anno 
# # es: 2018 sarà rappresentato con 18

# importo il modulo datetime
import datetime

def lotto_del_giorno():
# definisco il giorno dell'anno
    giorno_dell_anno = datetime.date.today().strftime("%j")
# definisco l'anno
    anno_part_A = datetime.date.today().strftime("%Y")
# Conto i numeri dell'anno, in questo modo il programma avrà una valenza di più secoli
    anno_part_B = len(anno_part_A)
# Prendo gli ultimi due numeri 
    anno_part_C = (anno_part_A[anno_part_B -2]+anno_part_A[anno_part_B -1])
# assemblo i pezzi del lotto 
    lotto = (giorno_dell_anno + anno_part_C)
# stampo a video il risultato
    print ("il lotto del giorno è " + lotto)

def data_da_lotto():
    lotto = input("inserisci il lotto da traformare in data: ")
    A = lotto[0]
    B = lotto[1]
    C = lotto[2]
    D = lotto[3]
    E = lotto[4]
    lota = (A + B + C)
    lotaint= int(lota)
    lotb = ("20" + D + E)
    lotbint= int(lotb)
    start_date = ("01/01/" + D + E)
    date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")
    end_date = date_1 + datetime.timedelta(days=lotaint -1)
    print ("La data corrispondente al lotto è: ")
    print ( end_date)

print('''
    Benvenuto nel programma Lotto :
    -Per vedere il lotto del giorno digitare 1;
    -Per calcolare la data da un lotto digitare 2;
    -Per uscire dal programma puoi digitare ESC;
    ''')
scelta = input('Inserisci il numero corrispondente all\'operazione selezionata --->  ')
if scelta == "1":
    print('\nHai scelto: di vedere il lotto del giorno\n')
    lotto_del_giorno()
elif scelta == "2":
    print('\nHai Scelto: di calcolare la data dal lotto\n')
    data_da_lotto()
elif scelta == "ESC":
    print('Chiudo applicazione')