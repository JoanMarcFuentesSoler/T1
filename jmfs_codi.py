import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf



T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
PI=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * PI * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic.
import sounddevice as sd                  # Importem el mòdul sounddevice per accedir a la tarja de so
sd.play(x, fm)                            # Reproducció d'àudio

from numpy.fft import fft                 # Importem la funció fft
N=5000                                    # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)                       # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                            # Vector amb els valors 0≤  k<N

plt.figure(1)                             # Nova figura
plt.subplot(211)                          # Espai per representar el mòdul
plt.plot(k,abs(X))                        # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')  # Etiqueta del títol
plt.ylabel('|X[k]|')                     # Etiqueta de mòdul
plt.subplot(212)                         # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))       # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                    # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')                # Etiqueta de la fase en Latex
plt.show()                               # Per mostrar els grafics

# 1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera  fx=4kHz, a banda 
# d'una freqüència pròpia en el marge audible. Comenta els resultats.

# 2. Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que 
# has creat (x_r, fm = sf.read('nom_fitxer.wav')).

    #·Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.
    #·Explica el resultat del apartat anterior.

# 3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de a en Hz.

    #·Comprova que la mesura de freqüència es correspon amb la freqüència de la sinusoide que has fet servir.
    #·Com pots identificar l'amplitud de la sinusoide a partir de la representació de la transformada? Comprova-ho amb el senyal generat.

# NOTES:

# Per representar en dB has de fer servir la fórmula següent:
    # X = 20 log10 (|x|/max(|x|))

# La relació entre els valors de l'índex k i la freqüència en Hz és:
    # fk = k/n *fm

# 4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). Llegeix el fitxer d'àudio i comprova:

    #·Freqüència de mostratge.
    #·Nombre de mostres de senyal.
    #·Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
    #·Representa la seva transformada en dB en funció de la freqüència, en el marge.
    #·Quines son les freqüències més importants del segment triat?