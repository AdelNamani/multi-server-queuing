import math
import helpers


class QueueMMSL:
    def __init__(self, nombre_serveurs, taux_arr, taux_ser, capacite):
        err = None
        err_msg = ''
        if nombre_serveurs <= 0:
            err = True
            err_msg = err_msg + 'Le nombre de serveur doit être strictement superieur à 0\n'
        if taux_arr <= 0:
            err = True
            err_msg = err_msg + 'Le taux d\'arrivé des clients doit être strictement superieur à 0\n'
        if taux_ser <= 0:
            err = True
            err_msg = err_msg + 'Le taux de service doit être strictement superieur à 0\n'
        if capacite < nombre_serveurs:
            err = True
            err_msg = err_msg + 'La capacité du système doit être supérieure au nombre de serveurs\n'
        if err is True:
            print(err_msg)
            exit(-1)

        self.s = nombre_serveurs
        self.taux_arr = taux_arr
        self.taux_ser = taux_ser
        self.capacite = capacite
        self.u = self.taux_arr / self.taux_ser
        self.rho = self.u / self.s
        if self.rho >= 1:
            print('La condition du stabilite du systeme n\'est pas satisfaite\n')
            exit(-1)
        self.p0 = 1 / (helpers.taylor_exp(self.u, self.s - 1) + (self.u ** self.s / math.factorial(
            self.s)) * helpers.geometric_series_sum(0, self.capacite - self.s, self.u / self.s))

    # Probabilté pour que n client soit dans le système Pn
    def pn(self, n):
        if n == 0:
            return self.p0
        elif(n > self.capacite):
            return 0
        elif(n <= self.s):
            return self.u ** n * self.p0 / math.factorial(n)
        else:
            return self.u ** n * self.p0 / (math.factorial(self.s) * pow(self.s, n - self.s))

    # Taux d'entrée
    def taux_en(self):
        return self.taux_arr * (1 - self.pn(self.capacite))

    # Nombre moyen de clients dans la file Nf
    def nb_moyen_clients_file(self):
        if(self.rho == 1):
            return (self.p0 * self.s ** self.s * (self.capacite - self.s) * (self.capacite - self.s + 1)) / (2 * math.factorial(s))
        else:
            return (self.p0 * (self.rho * self.s) ** self.s * self.rho * (1 - self.rho ** (self.capacite - self.s + 1) - (1 - self.rho) * (self.capacite - self.s + 1) * self.rho ** (self.capacite - self.s))) / (math.factorial(self.s) * pow((1 - self.rho), 2))

    # Nombre moyen de clients dans le système Ns
    def nb_moyen_clients_system(self):
        return self.nb_moyen_clients_file() + self.taux_en() / self.taux_ser

    # Temps d'attente moyen dans la file Tf
    def temps_attente_moyen_file(self):
        return self.nb_moyen_clients_file() / self.taux_en()

    # Temps de séjour moyen dans le système Ts
    def temps_sejour_moyen_systeme(self):
        return self.temps_attente_moyen_file() + (1 / self.taux_ser)
