from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
print(Fore.RED + '\nSome red text')
print(Back.GREEN + 'and with a green background')
print(Style.BRIGHT + 'and in Bright text\n')

print(Fore.CYAN + 'Some cyan text')
print(Back.BLUE + 'and with a blue background')
print(Style.DIM + 'and in Dim text\n')

print('Back to normal now')
