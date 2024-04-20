import pandas as pd
from datetime import datetime as dt
from carregar_arquivo import carregar_arquivo

import matplotlib as mpl
import matplotlib.pyplot as pl
import numpy as np

base = carregar_arquivo()
cores = ["red", "yellow"]
levels = [1, 2, 3]
cmap, norm = mpl.colors.from_levels_and_colors(levels=levels, colors=cores)


def gerarHistograma(colunas: list) -> pl:

    figura, eixos = pl.subplots(2, 2)
    eixoX = 0
    eixoY = 0
    i = 0
    while eixoX <= 1:
        eixoY = 0
        while eixoY <= 1:
            coluna = colunas[i]
            ocorrencias, barras = np.histogram(base[coluna["dados"]])
            reviews_ruins = ("Notas ruins: " +
                             str(len(base[base[coluna["dados"]] <= 6])))

            eixos[eixoX, eixoY].set_title(colunas[i]["titulo"])
            eixos[eixoX, eixoY].stairs(ocorrencias, barras, fill=True)
            eixos[eixoX, eixoY].text(0.7,8.5,reviews_ruins)
            eixoY += 1
            i += 1
        eixoX += 1
    figura.tight_layout()
    pl.xlabel("Nota")
    pl.ylabel("Quantidade de votos")
    return pl

print("Gerando os gráficos...")
gerarHistograma(
    [
        {"titulo": "Estoque", "dados": "Estoque"},
        {"titulo": "ListaDeCompras", "dados": "ListaDeCompras"},
        {"titulo": "NovaCompra", "dados": "NovaCompra"},
        {"titulo": "Preferencias", "dados": "Preferencias"}
    ]
)

print("Salvando os gráficos...")
data_hora = dt.now().strftime("%d-%m-%Y %H:%M")
nome_arquivo = f'gráficos/gráficos-{data_hora}.png'
pl.savefig(nome_arquivo)
print("Sucesso!")