import glob
import pandas as pd
import sys

spectra_filenames = glob.glob(f'*.dpt')
sample = []
for file in spectra_filenames:
    sample.append(file[0:3])
sample = pd.Series(sample)
sample.to_csv('CLASSES.CSV', index=False, header=False, sep=';')

wavenumber_series = pd.read_csv(spectra_filenames[0], names=['wavenumber','transmittance'],sep='\t')['wavenumber']
spectra_df = pd.DataFrame(columns=wavenumber_series)
spectra_df.to_csv('NUMEROS DE ONDA.csv', index=False, sep=';')

for file in spectra_filenames:
    spectrum_df = pd.read_csv(file, names=['wavenumber','transmittance'], sep='\t',index_col=0).transpose()
    spectra_df = pd.concat([spectra_df, spectrum_df], axis=0)
    file_index = spectra_filenames.index(file)+1
    print(f'file {file_index} of {len(spectra_filenames)}')
spectra_df.to_csv(f'ESPECTROS.csv', header=False, index=False, sep=';')


