import pip._vendor.requests
import time
from os import walk
path = '/data/data/com.termux/files/home/runoupas'


print('+-+-+-+ +-+-+ +-+-+-+\n|R|U|N| |O|U| |P|A|S|\n+-+-+-+ +-+-+ +-+-+-+\n')

filenames = next(walk(path), (None, None, []))[2]
print('Tu roules en quoi ?')
i = 1
for car in filenames:
    print(str(i) + '. ' + car)
    i = i + 1
print(str(i) + '. ' + 'Ajouter une caisse')
choice = input()

if int(choice) == i:
    print("Quel est ta plaque d'immatriculation ? (AA111BB)")
    plate = input()
    r=pip._vendor.requests.get('https://www.yakarouler.com/car_search/immat?immat=' + plate + '&name=undefined&redirect=true')
    data = r.text
    finder_start = data.find('<h2 class="title-car">')
    car = data[finder_start+22:data.find('</h2>')]
    model = car[:car.find('(')]
    rpath =  path + "/" +  model
    open(rpath, 'w').close()
    f = open(rpath, "w")
    f.write(car)
elif int(choice) < i:
    print("Quel est la plaque d'immatriculation ? (AA111BB)")
    plate = input()
    r=pip._vendor.requests.get('https://www.yakarouler.com/car_search/immat?immat=' + plate + '&name=undefined&redirect=true')
    data = r.text
    finder_start = data.find('<h2 class="title-car">')
    car = data[finder_start+22:data.find('</h2>')]
    model = car[:car.find('(')]
    tab = car.split()
    for spec in tab:
        if '(' in spec and 'kw' not in spec:
            gen = spec
        elif '.' in spec:
            size = spec
        elif 'cv' in spec or 'CV' in spec:
            hp = spec
    print("\nC'est un(e) " + model + "de " + hp)
    f = open(path + "/" + filenames[int(choice)-1], "r")
    mycar = f.read()
    for spec in mycar.split():
         if 'cv' in spec or 'CV' in spec:
            myhp = spec
    hp = int(hp[:-2])
    myhp = int(myhp[:-2])
    if myhp > hp+15:
        print(' _____ _   _ __  __ _____   _     _____ ')
        print('|  ___| | | |  \/  | ____| | |   | ____|')
        print('| |_  | | | | |\/| |  _|   | |   |  _|  ')
        print('|  _| | |_| | |  | | |___  | |___| |___ ')
        print('|_|    \___/|_|  |_|_____| |_____|_____|')
    elif myhp < hp-15:
        print('  ____ _ _____ ____ _____   __  __  ___  ____ _____ ')
        print(' / ___( ) ____/ ___|_   _| |  \/  |/ _ \|  _ \_   _|')
        print('| |   |/|  _| \___ \ | |   | |\/| | | | | |_) || |  ')
        print('| |___  | |___ ___) || |   | |  | | |_| |  _ < | |  ')
        print(' \____| |_____|____/ |_|   |_|  |_|\___/|_| \_\|_|  ')
    else:
        print('      _  ___  _   _   _    ____  _     _____ ')
        print('     | |/ _ \| | | | / \  | __ )| |   | ____|')
        print('  _  | | | | | | | |/ _ \ |  _ \| |   |  _|  ')
        print(' | |_| | |_| | |_| / ___ \| |_) | |___| |___ ')
        print('  \___/ \___/ \___/_/   \_\____/|_____|_____|')
    time.sleep(60)
else:
    print('error')
