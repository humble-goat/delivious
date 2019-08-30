import subprocess
clear = lambda: subprocess.call('cls||clear', shell=True)
start_over = lambda: Main

fin_str = []
forbidden_list = [',', ';', '.', '/', '?', '<', '>', '"', ':', '{',
                  '[', ']', '}', '-', '_', '`', '+', '=', '!', '@',
                  '#', '$', '%', '^', '&', '*', '(', ')', '~', '', ' ']

with open("Delivious.nfo", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

print('Hey you!'
      '\nWhat are you thing you\'re doing?'
      '\nIn the name of the King Delos freeze!'
      '\n')

accepted_answer = ['y', 'yes', 'yay', 'nah', 'no', 'n']
yes = list(accepted_answer[:-3])
no = list(accepted_answer[3:])


def _desymbolize(what):
    fin_str.clear()
    for i in what:
        if i in forbidden_list:
            i = str('')
            fin_str.append(i)
        fin_str.append(i)


name = str(input('State your name now, or die unamed!\n'))
_desymbolize(name)


def _game_over():
    quit()


fin = str().join(fin_str)

if fin in list(forbidden_list):
    print('Die parent 2 malester')
    _game_over()

print('So you call yourself', fin)
choice = str(input('\nIs that correct?\n'))

if choice in list(accepted_answer):
    _desymbolize(choice.lower())
    choice = str().join(fin_str)

    if choice in yes:
        print('I take that as a yes')
        start_over
    elif choice in no:
        name = str(input('So what is it then?\n'))
    else:
        print('This is your last chance to restate your name')
        choice = str(input())
else:
    print('Die imbecile!')
    _game_over()

if choice in list(forbidden_list):
    print('Are you some kind of a special retard? Answer the question don\'t paint symbols')
    print('Are you', fin, '?')
    choice = str(input())


class Main:
    print(f"Psst {name}!")
    str(input())
    with open("start.nfo", "r", encoding="utf-8") as file:
        for line in file:
            print('Clogger:', line.strip())
            str(input())
        said = str(input('Clogger: Do you remember these?\n'))
        if said in yes:
            clear
            print('Copper: Hey!')
        else:
            start_over