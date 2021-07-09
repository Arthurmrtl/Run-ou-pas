import pip._vendor.requests
import time


print('+-+-+-+ +-+-+ +-+-+-+\n|R|U|N| |O|U| |P|A|S|\n+-+-+-+ +-+-+ +-+-+-+\n')
print("1. Est-ce que je le fume ?")
print("2. Enregistrer ma voiture")
choice = input()


if int(choice) == 1:
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
        elif 'cv' in spec:
            hp = spec
    print("\nC'est un(e) " + model + "de " + hp)
    f = open("data", "r")
    mycar = f.read()
    for spec in mycar.split():
         if 'cv' in spec:
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

if int(choice) == 2:
    print("Quel est ta plaque d'immatriculation ? (AA111BB)")
    plate = input()
    r=pip._vendor.requests.get('https://www.yakarouler.com/car_search/immat?immat=' + plate + '&name=undefined&redirect=true')
    data = r.text
    finder_start = data.find('<h2 class="title-car">')
    car = data[finder_start+22:data.find('</h2>')]
    open('data', 'w').close()
    f = open("data", "w")
    f.write(car)