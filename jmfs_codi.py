# Representació temporal i freqüencial de senyals d'àudio.
import wave as readwave
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
from numpy.fft import fft     # Importem la funció fft
"""
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=150                               # Freqüència de la sinusoide 
fx1=4000                             # Freqüència de la sinusoide
fx2=7000                             # Freqüència de la sinusoide  
A=4                                  # Amplitud de la sinusoide
PI=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T

# Freq 1 
x = A * np.cos(2 * PI * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int((fm/2)*5*Tx)                       # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show() 

sd.play(x,fm)           # Reproducció d'àudio

N=5000                   # Dimensió de la transformada discreta
X=fft(x[0:Ls],N)         # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)           # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,20*np.log10((abs(X))/(max(abs(X))))) # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,(k/N)*fm)                  # Representació de la relació de l'index k i la freqüència en Hz
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('k-Hz')                    # Etiqueta de la k
plt.show()                            # Per mostrar els grafics

# Freq 2 
x1 = A * np.cos(2 * PI * fx1 * t)     # Senyal sinusoidal
sf.write('so_exemple2.wav', x1, fm)   # Escriptura del senyal a un fitxer en format wav

Tx1=1/fx1                                 # Període del senyal
Ls1=int((fm/2)*5*Tx1)                     # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls1], x1[0:Ls1])             # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()

sd.play(x1, fm)               # Reproducció d'àudio

N=5000                        # Dimensió de la transformada discreta
X1=fft(x1[0 : Ls1], N)        # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,20*np.log10((abs(X1))/(max(abs(X1))))) # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls1} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('dB')                      # Etiqueta del dB
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,(k/N)*fm)                  # Representació de la relació de l'index k i la freqüència en Hz
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('k-Hz')                    # Etiqueta de la k
plt.show()                            # Per mostrar els grafics


# Freq 3 
x2 = A * np.cos(2 * PI * fx2 * t)     # Senyal sinusoidal
sf.write('so_exemple3.wav', x2, fm)   # Escriptura del senyal a un fitxer en format wav

Tx2=1/fx2                             # Període del senyal
Ls2=int((fm/2)*5*Tx2)                 # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                            # Nova figura
plt.plot(t[0:Ls2], x2[0:Ls2])            # Representació del senyal en funció del temps
plt.xlabel('t en segons')                # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')  # Títol del gràfic
plt.show() 

sd.play(x2, fm)            # Reproducció d'àudio

N=5000                     # Dimensió de la transformada discreta
X2=fft(x2[0:Ls2], N)       # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)             # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,20*np.log10((abs(X2))/(max(abs(X2))))) # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls2} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('dB')                      # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,(k/N)*fm)                  # Representació de la relació de l'index k i la freqüència en Hz
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('k-Hz')                    # Etiqueta de la k
plt.show()                            # Per mostrar els grafics
"""
# NOTES:
# 4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). Llegeix el fitxer d'àudio i comprova:
obj = readwave.open('luzbel44.wav','r')
# Nombre de canals
print( "Number of channels",obj.getnchannels())
# Freqüència de mostratge.
print ( "Frame rate.",obj.getframerate())
# Nombre de mostres de senyal.
print ("Number of frames",obj.getnframes())
obj.close()

# Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.
x3, fm1 = sf.read('luzbel44.wav')
t1 = np.arange(len(x3))/fm1
fx3 = 44100
Tx3=1/fx3                                 # Període del senyal        
plt.figure(0)                             # Nova figura
plt.plot(t1,x3)                           # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('Audio wav luzbel44.wav')       # Títol del gràfic
plt.show()                                # Mostrar el grafic
sd.play(x3,fm1)                           # Reproducció d'àudio

N=5000                     # Dimensió de la transformada discreta
X3=fft(x3[0:fm1],N)        # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)             # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,20*np.log10((abs(X3))/(max(abs(X3))))) # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={fm1} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('dB')                      # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,(k/N)*fm1)                 # Representació de la relació de l'index k i la freqüència en Hz
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('k-Hz')                    # Etiqueta de la k
plt.show()                            # Per mostrar els grafics

# Representa la seva transformada en dB en funció de la freqüència, en el marge.

# Quines son les freqüències més importants del segment triat?
