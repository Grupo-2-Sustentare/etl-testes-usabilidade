
from carregar_arquivo import carregar_arquivo

from wordcloud import WordCloud
from datetime import datetime as dt
import matplotlib.pyplot as plt
from nltk.corpus import stopwords 
import nltk.downloader
from nltk.tokenize import word_tokenize 
nltk.download('punkt')
nltk.download('stopwords')


base = carregar_arquivo()

print("Extraindo as palavras...")
texto_feedback = ""
for i, feedback in enumerate(base["Feedbacks"]):
    texto_feedback += f"{feedback} "

tokenized_feedback = word_tokenize(texto_feedback)

print("Removendo conectivos...")
filtrado_feedback = []
palavras_indesejadas = ["wireframe", "achei", "site", "fiquei", "pouco", "aba", "algum", 
                        "bem", "fazer", "claro", "informações", "usuário", "ficou", 
                    "poderia", "tela", "bastante", "hora", "parte", "minutos", "outras",
                    "coisa", "interface", "faz", "base", "exemplo", "navegar", "projeto",
                    "ficar"]
for plvr in tokenized_feedback:
    if str.isalpha(plvr):
        
        plvr = str.lower(plvr)
        plvr = plvr.replace("'", "")

        if (plvr not in stopwords.words("portuguese") 
            and len(plvr) >= 3
            and plvr not in palavras_indesejadas):
            filtrado_feedback.append(plvr)

print("Gerando a Wordcloud..")
wc = WordCloud(background_color="white", repeat=False)
wc.generate(' '.join(filtrado_feedback))

print("Salvando a Wordcloud..")
svg_wc = wc.to_svg(embed_font=True)
data_hora = dt.now().strftime("%d-%m-%Y %H:%M")
nome_arquivo = f'wordclouds/wordcloud-{data_hora}.svg'

f = open(nome_arquivo, "w+")
f.write(svg_wc)
f.close()
print("Sucesso!")