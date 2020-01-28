import math
import helpers


class QueueMMS:
    def __init__(self, nombre_serveurs, taux_arr, taux_ser):
        err = None
        err_msg = ''
        if nombre_serveurs <= 0:
            err = True
            err_msg = err_msg + 'Le nombre de serveur doit etre strictement superieur à 0\n'
        if taux_arr <= 0:
            err = True
            err_msg = err_msg + 'Le taux d\'arrivé des clients doit etre strictement superieur à 0\n'
        if taux_ser <= 0:
            err = True
            err_msg = err_msg + 'Le taux de service doit etre strictement superieur à 0\n'
        if err is True:
            print(err_msg)
            exit(-1)
        self.s = nombre_serveurs
        self.taux_arr = taux_arr
        self.taux_ser = taux_ser
        self.u = self.taux_arr / self.taux_ser
        self.rho = self.u / self.s
        if self.rho >= 1:
            print('La condition du stabilité du système n\'est pas satisfaite\n')
            exit(-1)
        self.p0 = 1 / (helpers.taylor_exp(self.u, self.s - 1) + (self.s *
                                                                  pow(self.u, self.s))/(math.factorial(self.s)*(self.s - self.u)))
    
    # Probabilté pour que n client soit dans le système Pn
    def pn(self, n):
        if n == 0:
            return self.p0
        else:
            return self.p0 * ((self.taux_arr ** n) / (math.factorial(n) * (self.taux_ser ** n)))
    
    # Taux d'entrée
    def taux_en(self):
        return self.taux_arr

    # Nombre moyen de clients dans la file Nf
    def nb_moyen_clients_file(self):
        return (self.rho * self.pn(self.s)) / ((1 - self.rho) ** 2)

    # Nombre moyen de clients dans le système Ns
    def nb_moyen_clients_system(self):
        return self.nb_moyen_clients_file() + self.taux_en() / self.taux_ser

    # Temps d'attente moyen dans la file Tf
    def temps_attente_moyen_file(self):
        return self.nb_moyen_clients_file() / self.taux_en()

    # Temps de séjour moyen dans le système Ts
    def temps_sejour_moyen_systeme(self):
        return self.temps_attente_moyen_file() + (1 / self.taux_ser)
