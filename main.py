import QueuesMMS
import QueuesMMSL


while(True):
    print('======================================================')
    print('Veuillez indiquer le type de votre système d\'attente:')
    print('1- M/M/S')
    print('2- M/M/S/L')
    print('3- Quitter')
    choix = int(input())
    if choix == 1:
        print('Veuillez indiquer le nombre de serveur, taux d\'arrivé et taux de service séparés par des espaces:')
        s, arr, ser = list(map(float, input().split(' ')))
        queue = QueuesMMS.QueueMMS(int(s), arr, ser)
        print('Les caractéristiques de votre système MMS sont les suivants:')
        print("Nf = ", queue.nb_moyen_clients_file())
        print("Ns = ", queue.nb_moyen_clients_system())
        print("Tf = ", queue.temps_attente_moyen_file())
        print("Ts = ", queue.temps_sejour_moyen_systeme())
    elif choix == 2:
        print('Veuillez indiquer le nombre de serveur, taux d\'arrivé, taux de service et capacité séparés par des espaces:')
        s, arr, ser, c = list(map(float, input().split(' ')))
        queue = QueuesMMSL.QueueMMSL(int(s), arr, ser, int(c))
        print('Les caractéristiques de votre système MMSL sont les suivants:')
        print("Nf = ", queue.nb_moyen_clients_file())
        print("Ns = ", queue.nb_moyen_clients_system())
        print("Tf = ", queue.temps_attente_moyen_file())
        print("Ts = ", queue.temps_sejour_moyen_systeme())
    elif choix == 3:
        exit(0)
    else:
        print('Veuillez choisir une option valide !')

''' Exercice 3
queue = QueuesMMS.QueueMMS(3, 6, 3)
print('===== MMS =====')
print("Nf = ", queue.nb_moyen_clients_file())
print("Ns = ", queue.nb_moyen_clients_system())
print("Tf = ", queue.temps_attente_moyen_file())
print("Ts = ", queue.temps_sejour_moyen_systeme())

queue = QueuesMMSL.QueueMMSL(3, 6, 3,100)
print('===== MMSL =====')
print('P3=',queue.pn(3))
print("Nf = ", queue.nb_moyen_clients_file())
print("Ns = ", queue.nb_moyen_clients_system())
print("Tf = ", queue.temps_attente_moyen_file())
print("Ts = ", queue.temps_sejour_moyen_systeme())'''
