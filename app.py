from garazas import Garazas
import numpy
import django

garazas = Garazas()

if __name__ == "__main__":
    while True:
        veiksmas = int(input("1 - įvesti automobilį, 2 - įvesti elektromobilį, 3 - peržiūrėti, 4 - išeiti: "))
        match veiksmas:
            case 1:
                garazas.prideti_auto()
            case 2:
                garazas.prideti_elektro()
            case 3:
                garazas.atvaizduoti_auto()
            case 4:
                break
