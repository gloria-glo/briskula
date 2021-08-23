import random
import time


class Karta:

    def __init__(self, broj, zog, punti):
        self.broj = broj
        self.zog = zog
        self.punti = punti

    def __repr__(self):
        return f'Karta({self.broj},{self.zog})'

class Spil:

    zog = ['B','D','K','S']
    broj_punti = {1:11, 2:0, 3:10, 4:0, 5:0, 6:0, 7:0, 11:2, 12:3, 13:4}

    def __init__(self):
        self.spil = []
        for broj, punti in Spil.broj_punti.items():
            for zog in Spil.zog:
                karta = Karta(broj, zog, punti)
                self.spil.append(karta)

    def shuffle(self):
        random.shuffle(self.spil)

    def igramoU(self):
        return self.spil[-1]

    def peskaj(self):
        return self.spil.pop(0)

class Igrac:

    def __init__(self, spil):

        self.uRuci = spil[0:3]
        for karta in self.uRuci:
            spil.remove(karta)
        self.dobitak = 0

    def odaberiKartu(self, izbor):
        for karta in self.uRuci:
            return self.uRuci[izbor-1]

class Comp:

    def __init__(self, spil):
        self.uRuci = spil[0:3]
        for karta in self.uRuci:
            spil.remove(karta)
        self.dobitak = 0

    def baciKartuPrvi(self, igramo_u):
        #ova funkcija odabire kartu koju komp baca, kad igra prvi
        bacena_karta = ''
        for karta in self.uRuci:

            if karta.zog != igramo_u.zog and karta.punti < 10: #ako imaš zog u kojem se igra ili jaku kariku nemoj ih bacit, nego nesto drugo
                bacena_karta = karta
            elif karta.punti < 10:    #ako imaš zog i jake karike, radije baci zog u kojem se igra ovdje se moze dogodit da ima karte koji imaju punte, a da nisu zog u kojem se igra, pa je onda dorbo stavit uvjet da baci kartu koja nije zog u kojem se igra
                bacena_karta = karta
            else:
                bacena_karta = random.choice(self.uRuci) #ako imaš jake karike i nemas zog, baci sta god. bolje bi bilo 3-u ali eto.
        return bacena_karta

    def baciKartuDrugi(self, igramo_u, igrac_igra):
        #ova funkcija odabire kartu koju komp baca kad igra drugi
        bacena_karta = ''
        for karta in self.uRuci:

            if igrac_igra.zog != igramo_u.zog and igrac_igra.punti > 0:
                if karta.zog == igrac_igra.zog and karta.punti > igrac_igra.punti:
                    bacena_karta = karta
                elif karta.zog == igramo_u.zog and karta.punti == 0:
                    bacena_karta = karta
                elif karta.zog == igramo_u.zog:
                    bacena_karta = karta
                elif karta.punti == 0:
                    bacena_karta = karta

            elif igrac_igra.zog == igramo_u.zog and igrac_igra.punti > 0:
                if karta.zog == igramo_u.zog and karta.punti > igrac_igra.punti:
                    bacena_karta = karta
                elif karta.zog != igramo_u.zog and karta.punti == 0:
                    bacena_karta = karta
                elif karta.zog != igramo_u.zog and karta.punti <= 4:
                    bacena_karta = karta
                elif karta.zog != igramo_u.zog and karta.punti == (10 or 11):
                    bacena_karta = karta

            elif igrac_igra.punti == 0:
                if karta.zog == igrac_igra.zog and karta.punti > igrac_igra.punti:
                    bacena_karta = karta
                elif karta.zog == igrac_igra.zog and karta.broj > igrac_igra.broj:
                    bacena_karta = karta
                elif karta.punti == 0:
                    bacena_karta = karta
                else:
                    bacena_karta = karta
        return bacena_karta

def pokupi (igra_prvi, igramo_u, igrac_igra, comp_igra, igrac_dobitak = 0, comp_dobitak = 0):

    #ova funkcija određuje tko je dobio, ovisno o tome tko baca prvi i u kojem zogu se igra
    if igra_prvi == 'igrac':
        if igrac_igra.zog == igramo_u.zog:
            if comp_igra.zog != igramo_u.zog:
                igrac_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'igrac'
            elif comp_igra.zog == igramo_u.zog and comp_igra.punti < igrac_igra.punti:
                igrac_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'igrac'
            elif comp_igra.zog == igramo_u.zog and comp_igra.punti > igrac_igra.punti:
                comp_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'comp'
            elif comp_igra.zog == igramo_u.zog and comp_igra.broj > igrac_igra.broj:
                comp_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'comp'
            else:
                igrac_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'igrac'

        elif igrac_igra.zog != igramo_u.zog:
            if comp_igra.zog == igramo_u.zog:
                comp_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'comp'
            elif comp_igra.zog == igrac_igra.zog and comp_igra.punti > igrac_igra.punti:
                comp_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'comp'
            elif comp_igra.zog == igrac_igra.zog and comp_igra.punti < igrac_igra.punti:
                igrac_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'igrac'
            elif comp_igra.zog == igrac_igra.zog and comp_igra.broj > igrac_igra.broj:
                comp_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'comp'
            elif comp_igra.zog == igrac_igra.zog and comp_igra.broj < igrac_igra.broj:
                igrac_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'igrac'
            elif comp_igra.zog != igrac_igra.zog:
                igrac_dobitak += igrac_igra.punti + comp_igra.punti
                igra_prvi = 'igrac'

    elif igra_prvi == 'comp':
        if comp_igra.zog == igramo_u.zog:
            if igrac_igra.zog != igramo_u.zog:
                comp_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'comp'
            elif igrac_igra.zog == igramo_u.zog and igrac_igra.punti > comp_igra.punti:
                igrac_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'igrac'
            elif igrac_igra.zog == igramo_u.zog and igrac_igra.punti < comp_igra.punti:
                comp_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'comp'
            elif igrac_igra.zog == igramo_u.zog and igrac_igra.broj > comp_igra.broj:
                igrac_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'igrac'
            elif igrac_igra.zog == igramo_u.zog and igrac_igra.broj < comp_igra.broj:
                comp_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'comp'

        elif comp_igra.zog != igramo_u.zog and comp_igra.zog != igrac_igra.zog:
            if igrac_igra.zog != igramo_u.zog:
                comp_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'comp'
            elif igrac_igra.zog == igramo_u.zog:
                igrac_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'igrac'
        elif comp_igra.zog != igramo_u.zog and igrac_igra.zog == comp_igra.zog:
            if comp_igra.punti > igrac_igra.punti:
                comp_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'comp'
            elif comp_igra.punti < igrac_igra.punti:
                igrac_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'igrac'
            elif comp_igra.broj < igrac_igra.broj:
                igrac_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'igrac'
            else:
                comp_dobitak += comp_igra.punti + igrac_igra.punti
                igra_prvi = 'comp'

    return igrac_dobitak, comp_dobitak,  igra_prvi






karte = Spil()
spil = karte.spil # ovo pristupa onom self.spil u initu - objekt.varijabla u initu za dohvatit
karte.shuffle() #promjesaj originalnu listu, nemoj vraćat ništa, jer vraća none, ništa.. samo mjesa
igramo_u = karte.igramoU()
igraci = ['comp', 'igrac']
igra_prvi = random.choice(igraci)
igrac = Igrac(spil)
comp = Comp(spil)

def ispis(igra_prvi, igramo_u, igrac_uRuci, comp_uRuci, comp_igra = None, igrac_igra = None):
    #ova funkcija radi ispis na ekran u više slučajeva, prvo kad igrač još nije igra pa imamo 2 slučaja print kad comp igra prvi, i print kad još nitko ništa ne baca

    print('=' * 28)

    if igrac_igra is None:

        print('Igra prvi...', igra_prvi, end= ' ', flush = True )
        print('\n')

        if comp_igra is None:

            print ('\n   ▒ ▒ ▒           ')
            print()
            print(f'                    {igramo_u.broj}{igramo_u.zog} ▒')


        else:
            print ('\n   ▒ ▒             ')
            print()
            print(f'       {comp_igra.broj}{comp_igra.zog}       {igramo_u.broj}{igramo_u.zog} ▒')


        print('\n')

        for karta in igrac_uRuci:
            print(f' {karta.broj}{karta.zog} ', end ='')
        print()
        for index, karta in enumerate(igrac_uRuci, start = 1):
            print(f'  {index}.', end = '')

    else:
        #ovo je slučaj kad je igrač odabrao što baca, pa je uvik isti print, bacio je igrač i bacio je komp
        print ('\n   ▒ ▒             ')
        print()
        print(f'         {comp_igra.broj}{comp_igra.zog} {igrac_igra.broj}{igrac_igra.zog}     {igramo_u.broj}{igramo_u.zog} ▒')


        print()

        for karta in igrac_uRuci:
            print(f' {karta.broj}{karta.zog} ', end ='')
        print()
        for index, karta in enumerate(igrac_uRuci, start = 1):
            print(f'  {index}.', end = '')


    print()
    print('='*28)



#main program, petlja se vrti dok ima karata u ruci

while len(igrac.uRuci) or len(comp.uRuci) != 0:
#ovo je ispis ekrana dok igrač još ništa nije bacio!
    comp_igra = comp.baciKartuPrvi(igramo_u)
    if igra_prvi == 'comp':
        ispis(igra_prvi, igramo_u, igrac.uRuci, comp.uRuci, comp_igra)
    elif igra_prvi =='igrac':
        ispis(igra_prvi, igramo_u, igrac.uRuci, comp.uRuci)

#izbor igrača nakon prvog ispisa, ovdje je uključen i zadnji scenarij kad su u ruci i jedna i dvi karte pa je izmjenjen input
    if len(igrac.uRuci) == 3:
        izbor = input('\n' f'Odaberi kartu: 1, 2 ili 3. \n')
        if int(izbor) not in (1,2,3):
            izbor = input('\n' f'Kriv unos, molim odaberi kartu: 1, 2 ili 3. \n')
    elif len(igrac.uRuci) == 2:
        izbor = input('\n' f'Odaberi kartu: 1 ili 2. \n')
        if int(izbor) not in (1,2):
            izbor = input('\n' f'Kriv unos, molim odaberi kartu: 1 ili 2. \n')
    elif len(igrac.uRuci) == 1:
        izbor = input('\n' f'Odaberi kartu: 1. \n')
        if int(izbor) != 1:
            izbor = input('\n' f' Mozete odabrati samo kartu 1. \n')
    izbor = int(izbor)

#ovdje se sad odabire karta za igrača..
    igrac_igra = igrac.odaberiKartu(izbor)
    #iz karata u ruci izbacam bacenu kartu
    igrac.uRuci.remove(igrac_igra)
    #ovdje ne navodim comp_igra = compbaca prvi jer mi je to već spremljeno...
    if igra_prvi == 'comp':
        ispis(igra_prvi, igramo_u, igrac.uRuci, comp.uRuci, comp_igra, igrac_igra)

    elif igra_prvi == 'igrac':
        comp_igra = comp.baciKartuDrugi(igramo_u, igrac_igra)
        ispis(igra_prvi, igramo_u, igrac.uRuci, comp.uRuci, comp_igra, igrac_igra)


    comp.uRuci.remove(comp_igra)

    #ovdje raspakiravam varijable, koji je dobitak kod igrača, kod komp i kakav je redosljed igre
    igrac_dobitak, comp_dobitak, igra_prvi = pokupi(igra_prvi, igramo_u, igrac_igra, comp_igra)
    igrac.dobitak += igrac_dobitak
    comp.dobitak += comp_dobitak


    #ovaj dio odnosi se na redosljed peškavanja, ako je dobio comp, onda će i redosljed bit comp i on će prvi peškat
    if  igra_prvi == 'comp' :
        if len(spil) > 0:
            comp.uRuci.append(karte.peskaj())
            igrac.uRuci.append(karte.peskaj())
    elif igra_prvi == 'igrac':
        if len(spil) > 0:
            igrac.uRuci.append(karte.peskaj())
            comp.uRuci.append(karte.peskaj())

#ovaj dio je izvan while petlje
if comp.dobitak > igrac.dobitak:
    print(f' Pobijedilo je računalo! Računalo {comp.dobitak} : Igrač {igrac.dobitak}' )
elif comp.dobitak < igrac.dobitak:
    print(f' Pobijedio je igrač. Igrač {igrac.dobitak} : Računalo {comp.dobitak} ')
else:
    print(f' Izjednačeno. Igrač i računalo imaju 60 bodova')





