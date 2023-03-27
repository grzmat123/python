import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import numpy as np

kalibracja=pd.read_csv("kalibracja.txt", delim_whitespace=True, skipinitialspace=True)
wsp = np.polyfit(kalibracja['stezenie'], kalibracja['abs'], 1)
poly1d_fn = np.poly1d(wsp)
#kalibracja.plot(x='stezenie', style='o', poly1d_fn(x), '--k')
plt.plot(kalibracja['stezenie'], kalibracja['abs'], 'go', kalibracja['stezenie'], poly1d_fn(kalibracja['stezenie']), '--k')
plt.xlabel(r'Concentration [$\mu $mol/L]')
plt.xlim(0, 45)
plt.ylabel('Absorbance [a.u.]')

#plt.show()
plt.savefig('kalibracja.png', dpi = 600)


widmo=pd.read_csv("widmo.txt",
           delim_whitespace=True,
           skipinitialspace=True)

#print(data["abs"])
#plt.figure()
widmo.plot(x='fala', y='abs', label='Spectrum', style='r-')
plt.xlabel('Wavelength [nm]')
plt.ylabel('Absorbance [a.u.]')
#plt.show()
plt.savefig('widmo.png', dpi = 600)

prad=pd.read_csv("prad.txt", delim_whitespace=True, skipinitialspace=True)
#plt.ylim(3.5,7.5)

wykresy = prad.plot(x='czas', subplots=True, style='o-')

wykresy[0].set_ylim(3.5,7.5)
wykresy[0].axhline(6.6,color='red',ls='--', lw=1)
trans = transforms.blended_transform_factory(
    wykresy[0].get_yticklabels()[0].get_transform(), wykresy[0].transData)
wykresy[0].text(0,6.6, "{:.1f}".format(6.6), color="red", transform=trans, 
        ha="right", va="center", fontsize=7)
#wykresy[0].plot([0, 120], [6.6, 6.6], 'k-', lw=1,dashes=[2, 2])
wykresy[1].set_ylim(3.5,7.5)
wykresy[1].axhline(6.6,color='red',ls='--', lw=1)
trans = transforms.blended_transform_factory(
    wykresy[1].get_yticklabels()[0].get_transform(), wykresy[1].transData)
wykresy[1].text(0,6.6, "{:.1f}".format(6.6), color="red", transform=trans, 
        ha="right", va="center", fontsize=7)
wykresy[2].set_ylim(3.5,7.5)
wykresy[2].axhline(6.6,color='red',ls='--', lw=1)
trans = transforms.blended_transform_factory(
    wykresy[2].get_yticklabels()[0].get_transform(), wykresy[2].transData)
wykresy[2].text(0,6.6, "{:.1f}".format(6.6), color="red", transform=trans, 
        ha="right", va="center", fontsize=7)
wykresy[3].set_ylim(3.5,7.5)
wykresy[3].axhline(6.6,color='red',ls='--', lw=1)
trans = transforms.blended_transform_factory(
    wykresy[3].get_yticklabels()[0].get_transform(), wykresy[3].transData)
wykresy[3].text(0,6.6, "{:.1f}".format(6.6), color="red", transform=trans, 
        ha="right", va="center", fontsize=7)
wykresy[4].set_ylim(3.5,7.5)
wykresy[4].axhline(6.6,color='red',ls='--', lw=1)
trans = transforms.blended_transform_factory(
    wykresy[4].get_yticklabels()[0].get_transform(), wykresy[4].transData)
wykresy[4].text(0,6.6, "{:.1f}".format(6.6), color="red", transform=trans, 
        ha="right", va="center", fontsize=7)
#plt.plot([0, 120], [6.6, 6.6], 'k-', lw=1,dashes=[2, 2])
#plt.legend(loc='best')
plt.xlabel('Time [min]')
plt.ylabel('Current [mA]', position=(2.5,5.9), rotation=0)

#plt.text(0.06, 0.5, 'Current [mA]', ha='center', va='center', rotation='vertical')
#plt.show()
plt.savefig('prad.png', dpi = 600)



normalized=pd.read_csv("normalized.txt", delim_whitespace=True, skipinitialspace=True)
normalized.plot(x='czas', style=['X','o','s','^','*'])
plt.xlabel('Time [min]')
plt.ylabel('Normalized concentration')
#plt.show()
plt.savefig('normal.png', dpi = 600)



katalizatory=pd.read_csv("dane_popr.txt", delim_whitespace=True, skipinitialspace=True)

#plt.text(0.5, 0.04, 'common xlabel', ha='center', va='center')


plt.subplot(3, 2, 5)
plt.plot(katalizatory['czas'], katalizatory['Fe'], 'ro', katalizatory['czas'], katalizatory['Fem'], 'o')
#plt.ylabel(r'Concentration [$\mu $mol/L]')
plt.xlabel('Time [min]')
plt.ylim(8,32.5)
plt.legend(['Fe experimental', 'Fe model'], prop={'size': 7})

plt.subplot(3, 2, 6)
plt.plot(katalizatory['czas'], katalizatory['Fe2'], 'ro', katalizatory['czas'], katalizatory['Fe2m'], 'o')
#plt.ylabel(r'Concentration [$\mu $mol/L]')
plt.xlabel('Time [min]')
plt.legend(['Fe experimental (repeated)', 'Fe model (repeated)'], prop={'size': 7})

plt.subplot(3, 2, 3)
plt.plot(katalizatory['czas'], katalizatory['Co'], 'ro', katalizatory['czas'], katalizatory['Com'], 'o')
plt.ylabel(r'Concentration [$\mu $mol/L]')
#plt.xlabel('Time [min]')
plt.ylim(8,32.5)
plt.legend(['Co experimental', 'Co model'], prop={'size': 7})

plt.subplot(3, 2, 4)
plt.plot(katalizatory['czas'], katalizatory['Ni'], 'ro', katalizatory['czas'], katalizatory['Nim'], 'o')
#plt.ylabel(r'Concentration [$\mu $mol/L]', fontsize=8)
#plt.xlabel('Time [min]')
plt.ylim(8,32.5)
plt.legend(['Ni experimental', 'Ni model'], prop={'size': 7})

plt.subplot(3, 2, 1)
plt.plot(katalizatory['czas'], katalizatory['Mn'], 'ro', katalizatory['czas'], katalizatory['Mnm'], 'o')
#plt.ylabel(r'Concentration [$\mu $mol/L]')
#plt.xlabel('Time [min]')
plt.ylim(8,32.5)
plt.legend(['Mn experimental', 'Mn model'], prop={'size': 7})

plt.subplot(3, 2, 2)
plt.plot(katalizatory['czas'], katalizatory['Ce'], 'ro', katalizatory['czas'], katalizatory['Cem'], 'o')
#plt.ylabel(r'Concentration [$\mu $mol/L]')
#plt.xlabel('Time [min]')
plt.ylim(8,32.5)
plt.legend(['Ce experimental', 'Ce model'], prop={'size': 7})

#plt.show()
plt.savefig('model.png', dpi = 600)
