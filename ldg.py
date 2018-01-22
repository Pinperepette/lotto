import datetime

def LDG():    
    giorno_dell_anno = datetime.date.today().strftime("%j")
    anno_part_A = datetime.date.today().strftime("%Y")
    anno_part_B = len(anno_part_A)
    anno_part_C = (anno_part_A[anno_part_B -2]+anno_part_A[anno_part_B -1])
    lotto = (giorno_dell_anno + anno_part_C)
    return (lotto)
def Calcola(x):
    A = x[0]
    B = x[1]
    C = x[2]
    D = x[3]
    E = x[4]
    lota = (A + B + C)
    lotaint= int(lota)
    lotb = ("20" + D + E)
    lotbint= int(lotb)
    start_date = ("01/01/" + D + E)
    date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y")
    end_date = date_1 + datetime.timedelta(days=lotaint -1)
    return (end_date.strftime('%Y-%m-%d'))
