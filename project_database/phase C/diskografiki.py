import pymysql
con = pymysql.connect(host='localhost',user='root',password=None,db='diskografiki',charset='utf8')


def question_a ():
    print('Απάντηση ερωτήματος 1')
    print('1.  Όνομα_Τίτλος,Όνομα_καλλιτέχνη,αριθμός_τραγουδιών,πωλήσεις')
    print('')
    cur=con.cursor()
    cur.execute("SELECT Όνομα_Τίτλος,Όνομα_καλλιτέχνη,αριθμός_τραγουδιών,πωλήσεις FROM paragwgh where αριθμός_τραγουδιών=1 group by Όνομα_Τίτλος order by πωλήσεις desc ")
    for r in cur:
        print(r)
    cur.close()

def question_b ():
    print('Απάντηση ερωτήματος 2')
    print('2.  τραγούδι, καλλιτεχνικό_όνομα')
    print('')
    cur=con.cursor()
    cur.execute("SELECT hxografisi.τραγούδι,καλλιτεχνικό_όνομα FROM ermineuths inner join ergazetai on ermineuths.Αρ_ταυτ=ergazetai.Αρ_ταυτ inner join hxografisi on ergazetai.κωδ_ηχογράφησης=hxografisi.κωδικός_ηχογράφησης group by hxografisi.τραγούδι order by καλλιτεχνικό_όνομα ")
    for r in cur:
        print(r)
    cur.close()

def question_c ():
    print('Απάντηση ερωτήματος 3')
    print('3.  Αρ_ταυτ, Όνομα, τηλέφωνο, μισθός, κατηγορία_μουσικής, είδος')
    print('')
    cur=con.cursor()
    cur.execute("select ergazomenos.Αρ_ταυτ,Όνομα,τηλέφωνο,μισθός,mousikos.κατηγορία_μουσικής,mousikos.είδος from ergazomenos inner join mousikos on ergazomenos.Αρ_ταυτ=mousikos.Αρ_ταυτ WHERE κατηγορία_μουσικής LIKE '%Rock%' and( είδος like '%guitar%' or είδος like '%composer%'  or είδος like '%songwriter%') ")
    for r in cur:
        print(r)
    cur.close()

def question_d ():
    print('Απάντηση ερωτήματος 4')
    print('4. Όνομα, μισθός, καλλιτεχνικό_όνομα, αριθμός_βραβείων ')
    print('')
    cur=con.cursor()
    cur.execute("SELECT distinct ergazomenos.Όνομα,ergazomenos.μισθός,ermineuths.καλλιτεχνικό_όνομα,ermineuths.αριθμός_βραβείων FROM ergazomenos inner join ermineuths on ergazomenos.Αρ_ταυτ=ermineuths.Αρ_ταυτ inner join kanei on ermineuths.Αρ_ταυτ=kanei.καλλιτέχνης inner join synavlia on kanei.όνομα=synavlia.τίτλος where έτος_υπογραφής_συμβολαίου+διάρκεια_συμβολαίου=2017 and synavlia.αριθμός_εισητηρίων>5000 and ermineuths.αριθμός_βραβείων>1 ")
    for r in cur:
        print(r)
    cur.close()


    
def question_e ():
    print('Απάντηση ερωτήματος 5')
    print('5.  χώρα,τοποθεσία,Μ.Ο(αριθμός_εισητηρίων)')
    print('')
    cur=con.cursor()
    cur.execute("select χώρα,τοποθεσία, avg(αριθμός_εισητηρίων)  from synavlia group by τοποθεσία order by αριθμός_εισητηρίων desc")
    for r in cur:
        print(r)
    cur.close()

def question_f ():
    print('Απάντηση ερωτήματος 6')
    print('6.  Όνομα_Τίτλος, αριθμός_τραγουδιών, sum(χρονική_διάρκεια)')
    print('')
    cur=con.cursor()
    cur.execute("SELECT paragwgh.Όνομα_Τίτλος ,paragwgh.αριθμός_τραγουδιών, sum(χρονική_διάρκεια) FROM hxografisi join apoteleitai ON hxografisi.κωδικός_ηχογράφησης=apoteleitai.κωδ_ηχογράφησης join paragwgh on apoteleitai.τίτλος_παραγωγής=paragwgh.Όνομα_Τίτλος group by paragwgh.Όνομα_Τίτλος order by sum(χρονική_διάρκεια)")
    for r in cur:
        print(r)
    cur.close()

def question_g ():
    print('Απάντηση ερωτήματος 7')
    print('7.  τραγούδι, count(κωδικός_ηχογράφησης)')
    print('')
    cur=con.cursor()
    cur.execute(" SELECT τραγούδι,count(κωδικός_ηχογράφησης) FROM `hxografisi` group by τραγούδι having count(κωδικός_ηχογράφησης)>3")
    for r in cur:
        print(r)
    cur.close()

def question_h ():
    print('Απάντηση ερωτήματος 8')
    print('8. * FROM ermineuths ')
    print('')
    cur=con.cursor()
    cur.execute(" SELECT * FROM `ermineuths` where είδος_μουσικής LIKE '%Rock%' order by αριθμός_βραβείων desc ")
    for r in cur:
        print(r)
    cur.close()




def main_menu():

    print('1: Εμφάνισε τα singles ταξινομημένα σύμφωνα με τις πωλήσεις.')
    print('2: Εμφάνισε όλα τα τραγούδια μαζί με τους ερμηνευτές τους.')
    print('3: Βρες τους εργαζομένους που είτε παίζουν κιθάρα,είτε είναι συνθέτες,είτε στιχουργοί και ειδικεύονται στη Rock μουσική.')
    print('4: Από τους ερμηνευτές που το συμβόλαιο τους λήγει το 2017 βρες αυτούς που έχουν πάνω από ένα βραβείο και έχουν πουλήσει πάνω από 5000 εισητήρια σε κάποια συναυλία τους.')
    print('5: Ταξινόμησε τις πόλεις των συναυλιών σύμφωνα με τον μέσο όρο εισιτηρίων.')
    print('6: Βρες για κάθε παραγωγή το σύνολο των ωρών ηχογράφησης που χρειάστηκε.')
    print('7: Βρες τα τραγούδια που χρειάστηκαν πάνω από 3 μέρες ηχογράφησης.')
    print('8: Βρες τους καλλιτέχνες που ασχολούνται με τη Rock ταξινομημένους σύμφωνα με τα βραβεία που έχουν λάβει.')
    answer = ' '
    while not answer in '1 2 3 4 5 6 7 8'.split():
        answer = input('επιλογή.....')
        if answer == '': return 0
    else:
        return answer




while True:
        print('')
        answer = main_menu()
        if not answer: break
        elif answer == '1': question_a()
        elif answer == '2': question_b()
        elif answer == '3': question_c()
        elif answer == '4': question_d()
        elif answer == '5': question_e()
        elif answer == '6': question_f()
        elif answer == '7': question_g()
        elif answer == '8': question_h()
