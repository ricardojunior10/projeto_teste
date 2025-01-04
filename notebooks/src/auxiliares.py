import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, mannwhitneyu



def analise_shapiro(dataframe, alfa=0.05):
    print('Teste de Shapiro-Wilk')
    for coluna in dataframe.columns:
        estatistica_sw, valor_p_sw = shapiro(dataframe[coluna], nan_policy='omit')
        print(f'{estatistica_sw=:.3f}')
        if valor_p_sw > alfa:
            print(f'{coluna} segue uma distribuição normal (valor p: {valor_p_sw:.3f})')
        else:
            print(f'{coluna} não segue uma distribuição normal (valor p: {valor_p_sw:.3f})')




def analise_levene(dataframe, alfa=0.05, centro='mean'):
    print('Teste de Levene')
    estatistica_levene, valor_p_levene = levene(*[dataframe[coluna] for coluna in dataframe.columns], 
                                                center=centro,
                                                nan_policy='omit')
    print(f'{estatistica_levene=:.3f}')
    if valor_p_levene > alfa:
        print(f'Variâncias iguais (valor p: {valor_p_levene:.3f})')
    else:
        print(f'Ao menos uma variância é diferente (valor p: {valor_p_levene:.3f})')



def analise_mannwhitneyu(dataframe, 
                         alfa=0.05, 
                         alternativa='two-side',
                        ):
    print('Teste de Mann-Whitney')
    estatistica_mw, valor_p_mw = mannwhitneyu(
        *[dataframe[coluna] for coluna in dataframe.columns],
        nan_policy='omit',
        alternative=alternativa
    )

    print(f'{estatistica_mw:.3f}')
    if valor_p_mw > alfa:
        print(f'Não rejeita a hipótese nula (valor p: {valor_p_mw:.3f})')
    else:
        print(f'Rejeita a hipotese nula (valor p: {valor_p_mw:.3f})')


