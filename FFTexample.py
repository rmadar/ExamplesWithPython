import ROOT
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as ft


## ====================================================================
##
## Author: Romain Madar (romain.madar@gmail.com)
## Date  : 11/07/17
##
## Example of FFT manipulation using scipy.fftpack
##  - (tmax-tmin)/N = dt gives the time resolution for x(t)
##  - 1/dt = fmax gives the largest frequency of the FT[x](f)
##  - N/(tmax-tmin) = df gives the frequency resolution for FT[x](f)
##
## Normalization is properly handled only when inverser FT is called.
## In order to plot properly normalized spectrum, one has to divide
## FT[x](f) by sqrt(N) (due to the discrete nature of the DFT).
##
## ====================================================================


#-----------------
# Temporal signal
#-----------------
Npx      = 10000
dT       = 200
time     = np.linspace(-dT/2,dT/2,Npx)
x_period = np.cos(3*2*np.pi*time)
x_noise  = np.random.uniform(0,0.2,Npx)
x_envlop = np.exp( - (np.abs(time)/2)**2 ) + 0.3*np.exp( - (np.abs(time-5)/2)**2 ) + 0.3* np.exp( - (np.abs(time+5)/2)**2 )
signal   = (x_period+x_noise) * x_envlop
autocorr = np.correlate(signal,signal,'same')
Energy   = np.sum( signal*signal.conj() )


#---------------------------------------------
# General FFT (complex input & complex output)
#---------------------------------------------
x_fft           = ft.fft(signal)
Corr_fft        = ft.fft(autocorr)
x_fft_norm      = x_fft    / np.sqrt( len(x_fft) )
Corr_fft_norm   = Corr_fft / np.sqrt(len(Corr_fft))
freq            = ft.fftfreq( signal.size, d=time[1]-time[0])
EnergyFreqSpace = np.sum( x_fft_norm*x_fft_norm.conj() )
print '\nEnergy in time and frequency using general FFT:'
print '-------------------------------------------------'
print ' Sum[x^2(t)] = ' + str(Energy)
print ' Sum[X^2(f)] = ' + str(EnergyFreqSpace.real)


#---------------------------------------------------------------------------
# Real signal FFT (real input and complex output but no negative frequencies
# because Im[FFT](f) = -Im[FFT](-f) & Re[FFT](f) = Re[FFT](-f) )
#---------------------------------------------------------------------------
x_rfft          = ft.rfft(signal)
Corr_rfft       = ft.rfft(autocorr)
rfreq           = ft.rfftfreq(signal.size, d=time[1]-time[0])
x_rfft_norm     = x_rfft    / np.sqrt( len(x_rfft) )
Corr_rfft_norm  = Corr_rfft / np.sqrt(len(Corr_rfft))
EnergyFreqSpace = ( x_rfft_norm[0]*x_rfft_norm[0].conj() + 2 * np.sum(x_rfft_norm[1:]*x_rfft_norm[1:].conj()) )
print '\nEnergy in time and frequency using real FFT:'
print '----------------------------------------------'
print ' Sum[x^2(t)] = ' + str(Energy)
print ' Sum[X^2(f)] = ' + str(EnergyFreqSpace)


#---------------------------------------------------
# Print some details about time/frequency resolution
#---------------------------------------------------
print '\nTime and freqency precision:'
print '-----------------------------'
print ' N    = {:.1e}'                    .format(Npx)
print ' dT   = {:.1e} s   [ = Tmax-Tmin ]'.format(dT)
print ' dt   = {:.1e} s   [ = dT/N ]'     .format(time[1]-time[0])
print ' df   = {:.1e} Hz  [ = 1/dT ]'     .format(rfreq[1]-rfreq[0])
print ' fmax = {:.1e} Hz  [ = 0.5*N/dT ]' .format(np.amax(rfreq))
print '\n'


#-------------------------------------------------
# Plot of x(t) and FFT[x](f)
# Plot of AutoCorr[x](tau) and FFT[AutoCorr[x]](f)
#-------------------------------------------------
plt.subplot(221)
plt.xlim(-15,15)
plt.plot(time,signal)
plt.subplot(222)
plt.xlim(0,5)
plt.plot(rfreq,x_rfft_norm)
plt.subplot(223)
plt.xlim(-15,15)
plt.plot(time,autocorr)
plt.subplot(224)
plt.xlim(0,5)
plt.plot(rfreq,Corr_rfft_norm)
plt.show()


