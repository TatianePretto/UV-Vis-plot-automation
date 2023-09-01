import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os
import pandas as pd
from scipy import stats
from scipy.signal import savgol_filter
from sklearn.linear_model import LinearRegression


### Bandgap indireto
folder_path = r"xxxxxx" # substitua pelo caminho para a pasta desejada
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        # use o pandas para ler o arquivo txt e criar um DataFrame
        data = pd.read_csv(file_path, delimiter=",", decimal = '.').values
        energy = data[:, 0]
        absorption = data[:, 1]
        ## Calcule a energia do fóton para cada comprimento de onda 
        h = 4.135667696e-15  # Planck's constant in eV*s
        c = 299792458  # Speed of light in m/s
        energy_photon = h * c / (energy * 1e-9)  # Energy of photon in eV ---- esse é o x

        ##Calcule a absorção multiplicada pela energia do fóton elevada a um expoente:
        n = 1/2  # Exponent
        absorption_energy = (absorption * energy_photon) ** n #### esse é o y

        ### para observar como ficou o plot do gráfico
        #### xlim e ylim são para deixar o gráfico iniciando em (0,0)
        plt.plot(energy_photon, absorption_energy)
        plt.xlim(0)
        plt.ylim(0)
        plt.show()

        # encontrando o índice do valor máximo da curva de tauc
        idx_max = np.argmax(absorption_energy)
        x_max = energy_photon[idx_max]
        y_max = absorption_energy[idx_max]

        plt.plot(energy_photon, absorption_energy)
        plt.plot(energy_photon[idx_max], absorption_energy[idx_max], 'ro')
        plt.show()

        #### a partir da derivada

        #### cálculo da derivada
        dy = np.diff(absorption_energy, 1)
        dx = np.diff(energy_photon, 1)

        plt.plot(energy_photon[:-1], dy/dx, label="dy/dx", color='red')
        plt.plot(energy_photon, absorption_energy, label="WTF")
        plt.xlabel("Energia (eV)")
        plt.ylabel(r"$(\alpha$h$\nu)^2$")
        plt.title("Tauc plot - Indireto")
        plt.legend()
        plt.grid()
        plt.show()

        ### smooth da derivada
        dydx_smooth = savgol_filter(dy/dx, 101, 3)

        ## máximo da derivada
        maxindex_dydx = np.argmax(dydx_smooth)

        plt.plot(energy_photon, absorption_energy)
        plt.plot(energy_photon[:-1], dydx_smooth, label = "dy/dx smooth", color = 'red')
        plt.scatter(energy_photon[maxindex_dydx], absorption_energy[maxindex_dydx], marker='x', color='k', label="x = " + str(energy_photon[maxindex_dydx]))
        plt.xlabel("Energia (eV)")
        plt.ylabel(r"$(\alpha$h$\nu)^2$")
        plt.title("Tauc plot - Indireto")
        plt.legend()
        plt.show()

        # Defina o intervalo para traçar a reta
        x_linear = energy_photon[max(idx_max - 10, 0):min(idx_max + 10, len(energy_photon))]
        y_linear = absorption_energy[max(idx_max - 10, 0):min(idx_max + 10, len(absorption_energy))]

        a, b, r_value, p_value, stderr = stats.linregress(x_linear, y_linear)
        E_bandgap = round(-b/a, 2)

        def f(x, a, b):
            return a*x + b

        visualization_x = np.linspace(E_bandgap, energy_photon[idx_max+5], 2)

        plt.scatter(E_bandgap, 0, marker='x', color='red', label="Bandgap = " + str(E_bandgap) + "eV")
        plt.plot(energy_photon, absorption_energy, color='#FFA500', linewidth=3)
        plt.plot(visualization_x, f(visualization_x, a, b), color='#4B0082', linewidth=3)
        plt.axvline(x=E_bandgap, color='#4B0082', linestyle='--')
        plt.xlabel("Energia (eV)")
        plt.ylabel(r"$(\alpha$h$\nu)^2$")
        plt.title("Tauc plot - Indireto")
        plt.xlim(0)
        plt.ylim(0)
        plt.grid(False)
        plt.legend()

        # salva o gráfico com um nome distinto usando o nome do arquivo original mais a string "direto"
        new_filename = filename[:-4] + 'indireto' + '.png'
        plt.savefig(os.path.join(folder_path, new_filename), dpi=300, bbox_inches='tight')
        plt.clf()  # limpa a figura para o próximo gráfico

#### Bandgap direto ##### 
folder_path = r"xxxxxx" # substitua pelo caminho para a pasta desejada
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        # use o pandas para ler o arquivo txt e criar um DataFrame
        data = pd.read_csv(file_path, delimiter="\t", decimal = '.').values
        energy = data[:, 0]
        absorption = data[:, 1]
        ## Calcule a energia do fóton para cada comprimento de onda 
        h = 4.135667696e-15  # Planck's constant in eV*s
        c = 299792458  # Speed of light in m/s
        energy_photon = h * c / (energy * 1e-9)  # Energy of photon in eV ---- esse é o x

        ##Calcule a absorção multiplicada pela energia do fóton elevada a um expoente:
        n = 2  # Exponent
        absorption_energy = (absorption * energy_photon) ** n #### esse é o y

        ### para observar como ficou o plot do gráfico
        #### xlim e ylim são para deixar o gráfico iniciando em (0,0)
        plt.plot(energy_photon, absorption_energy)
        plt.xlim(0)
        plt.ylim(0)
        plt.show()

        # encontrando o índice do valor máximo da curva de tauc
        idx_max = np.argmax(absorption_energy)
        x_max = energy_photon[idx_max]
        y_max = absorption_energy[idx_max]

        plt.plot(energy_photon, absorption_energy)
        plt.plot(energy_photon[idx_max], absorption_energy[idx_max], 'ro')
        plt.show()

        #### a partir da derivada

        #### cálculo da derivada
        dy = np.diff(absorption_energy, 1)
        dx = np.diff(energy_photon, 1)

        plt.plot(energy_photon[:-1], dy/dx, label="dy/dx", color='red')
        plt.plot(energy_photon, absorption_energy, label="WTF")
        plt.xlabel("Energia (eV)")
        plt.ylabel("\u03B1h\u03BD)\u00B9\u2044\u2082")
        plt.title("Tauc plot - Direto")
        plt.legend()
        plt.grid()
        plt.show()

        ### smooth da derivada
        dydx_smooth = savgol_filter(dy/dx, 101, 3)

        ## máximo da derivada
        maxindex_dydx = np.argmax(dydx_smooth)

        plt.plot(energy_photon, absorption_energy)
        plt.plot(energy_photon[:-1], dydx_smooth, label = "dy/dx smooth", color = 'red')
        plt.scatter(energy_photon[maxindex_dydx], absorption_energy[maxindex_dydx], marker='x', color='k', label="x = " + str(energy_photon[maxindex_dydx]))
        plt.xlabel("Energia (eV)")
        plt.ylabel("\u03B1h\u03BD)\u00B9\u2044\u2082")
        plt.title("Tauc plot - Direto")
        plt.legend()
        plt.show()

        # Defina o intervalo para traçar a reta
        x_linear = energy_photon[max(idx_max - 10, 0):min(idx_max + 10, len(energy_photon))]
        y_linear = absorption_energy[max(idx_max - 10, 0):min(idx_max + 10, len(absorption_energy))]

        a, b, r_value, p_value, stderr = stats.linregress(x_linear, y_linear)
        E_bandgap = round(-b/a, 2)


        def f(x, a, b):
            return a*x + b

        visualization_x = np.linspace(E_bandgap, energy_photon[idx_max+5], 2)

        plt.scatter(E_bandgap, 0, marker='x', color='red', label="Bandgap = " + str(E_bandgap) + "eV")
        plt.plot(energy_photon, absorption_energy, color='#FFA500', linewidth=3)
        plt.plot(visualization_x, f(visualization_x, a, b), color='#4B0082', linewidth=3)
        plt.axvline(x=E_bandgap, color='#4B0082', linestyle='--')
        plt.xlabel("Energia (eV)")
        plt.ylabel("(\u03B1h\u03BD)\u00B9\u2044\u2082")
        plt.title("Tauc plot - Direto")
        plt.xlim(0)
        plt.ylim(0)
        plt.grid(False)
        plt.legend()


        # salva o gráfico com um nome distinto usando o nome do arquivo original mais a string "direto"
        new_filename = filename[:-4] + 'direto' + '.png'
        plt.savefig(os.path.join(folder_path, new_filename), dpi=300, bbox_inches='tight')
        plt.clf()  # limpa a figura para o próximo gráfico
