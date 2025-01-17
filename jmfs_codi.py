# Pràctica 1 : Anàlisi fitxer de so
# Autor : Joan Marc Fuentes Soler 
# Grup : 12
# Representació temporal i freqüencial de senyals d'àudio.

import wave as readwave
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd      # Importem el mòdul sounddevice per accedir a la tarja de so
from numpy.fft import fft     # Importem la funció fft

# 1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. 
# Al menys considera 4 kHz, a banda d'una freqüència pròpia en el marge audible.Comenta els resultats.

T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
A=4                                  # Amplitud de la sinusoide
PI=np.pi                             # Valor del número pi
L = int(fm*T)                        # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T

# Freqüència 150 Hz 
fx=150                               # Freqüència de la sinusoide 
x = A * np.cos(2 * PI * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                              # Període del senyal
Ls=int(fm*5*Tx)                      # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                                        # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                           # Representació del senyal en funció del temps
plt.xlabel('t en segons')                            # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide fx = 150Hz')   # Títol del gràfic
plt.show() 
sd.play(x,fm)            # Reproducció d'àudio

N=5000                   # Dimensió de la transformada discreta
X=fft(x[0:Ls],N)         # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)           # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

# Freqüència 4kHz
fx=4000                              # Freqüència de la sinusoide
x = A * np.cos(2 * PI * fx * t)     # Senyal sinusoidal
sf.write('so_exemple2.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx1=1/fx                             # Període del senyal
Ls=int(fm*5*Tx)                     # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                                      # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                      # Representació del senyal en funció del temps
plt.xlabel('t en segons')                          # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide fx = 4kHz')  # Títol del gràfic
plt.show()                                         # Per mostrar els grafics
sd.play(x,fm)                                     # Reproducció d'àudio

N=5000                        # Dimensió de la transformada discreta
X1=fft(x[0:Ls], N)          # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                   # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))   # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els gràfics

# Freqüència 6,5kHz
fx=6500                              # Freqüència de la sinusoide 
x = A * np.cos(2 * PI * fx * t)     # Senyal sinusoidal
sf.write('so_exemple3.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                             # Període del senyal
Ls=int(fm*5*Tx)                     # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                                         # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                         # Representació del senyal en funció del temps
plt.xlabel('t en segons')                             # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide fx = 6,5kHz')   # Títol del gràfic
plt.show()                                            # Per mostrar els grafics
sd.play(x,fm)                                       # Reproducció d'àudio

N=5000                         # Dimensió de la transformada discreta
X=fft(x[0:Ls],N)            # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                 # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                   # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))   # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

#2. Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat (x_r, fm = sf.read('nom_fitxer.wav')).
    #Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.
    #Explica el resultat del apartat anterior.

# Freqüència 1 fx = 150 Hz 
x_r,fm = sf.read('so_exemple1.wav')     # Escriptura del senyal a un fitxer en format wav
Tm = 1/fm                                 # Període de mostratge
t = Tm*np.arange(len(x_r))                       # Vector amb els valors de la variable temporal, de 0 a T
sf.write('Nou_so_exemple1.wav',x_r,fm)
fx = 150                                  # Freqüèencia del senyal
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                         # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])            # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide fx = 150 Hz')  # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 
sd.play(x_r,fm)                           # Reproducció d'àudio

N=5000                                # Dimensió de la transformada discreta
X=fft(x_r[0:Ls],N)                # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                        # Vector amb els valors 0≤  k<N
plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                  # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))  # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els gràfics 

#3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de 0 a fm/2 en Hz.

T= 2.5                               
fm=8000                             
fx=150                               
A=4                                  
pi=np.pi                           
L =int(fm*T)                     
Tm=1/fm                              
t=Tm*np.arange(L)                   
x = A * np.cos(2 * pi * fx * t)     
sf.write('Nou_so_exemple1.wav',x,fm)  
Tx=1/fx                                   
Ls=int(fm*Tx*5) 


plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls],x[0:Ls])                 # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide fx = 150Hz')  # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 
sd.play(x,fm)                             # Reproducció d'àudio

N=5000                         # Dimensió de la transformada discreta
X=fft(x[0:Ls],N)               # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                 # Vector amb els valors 0≤k<N

fk = k[0:N//2+1]*fm/N
XdB = 20*np.log10(np.abs(X)/max(np.abs(X[0:N//2+1])))
plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(fk,XdB[0:N//2+1])            # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('dB')                      # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Hz')                      # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

# 4. Tria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). Llegeix el fitxer d'àudio i comprova:

obj = readwave.open('luzbel44.wav','r')                   # Obrim el fitxer
print( "Nombre de canals:",obj.getnchannels())            # Nombre de canals
if(obj.getnchannels()==1): {print("Mono")}               
else: {print("Stereo")}
print ( "Freqüència de mostratge:",obj.getframerate())    # Freqüència de mostratge.
print ("Nombre de mostres de senyal: ",obj.getnframes())  # Nombre de mostres de senyal.
obj.close()                                               # Sortim del fitxer

# Tria un segment de senyal de 25ms i insereix una gráfica amb la seva evolució temporal.

T= 25e-3                            # Durada de T segons
x,fm = sf.read('luzbel44.wav')      # Lectura del fitxer
L = int(fm*T)                       # Nombre de mostres del senyal digital
Tm=1/fm                             # Període de mostratge
t=Tm*np.arange(L)                   # Vector amb els valors de la variable temporal, de 0 a T
sf.write('fluzbel44.wav',x, fm)

plt.figure(0)                                                    # Nova figura
plt.plot(t[0:L],x[0:L])                                          # Representació del senyal en funció del temps
plt.xlabel('t en segons')                                        # Etiqueta eix temporal
plt.title(f'Fragment audio: "luzbel44.wav" Durada:{T} segons')   # Títol del gràfic
plt.show()                                                       # Mostrar el grafic

# Representa la seva transformada en dB en funció de la freqüència, en el marge.

N=5000                                      # Dimensió de la transformada discreta
X=fft(x[0:L],N)                          # Càlcul de la transformada de 5 períodes de la sinusoide
k=np.arange(N)                              # Vector amb els valors 0≤k<N
fk = k[0:N//2+1]*fm/N
XdB = 20*np.log10(np.abs(X)/max(np.abs(X[0:N//2+1])))
plt.figure(1)                               # Nova figura
plt.subplot(211)                            # Espai per representar els dB
plt.plot(fk,XdB[0:N//2+1])                # Representació dels dB en funció de les mostres 
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('Modul dB')                      # Etiqueta de mòdul
plt.subplot(212)                            # Espai per representar la fase
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])))       # Representació de la fase de la transformad, desenroscada
plt.xlabel('Hz')                            # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')                   # Etiqueta de l'eix de coordenades
plt.show()                                  # Per mostrar els gràfics