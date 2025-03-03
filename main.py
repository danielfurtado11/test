import streamlit as st
import os
import time

st.set_page_config(
    page_title="NEXI Meetings",    # ✅ Título da página (aparece na aba do navegador)
    page_icon="https://raw.githubusercontent.com/danielfurtado11/test/main/icon.png",
    layout="wide",           # ✅ "wide" (tela cheia) ou "centered" (padrão, layout centralizado)
    initial_sidebar_state="collapsed",  # ✅ Estado inicial da barra lateral ("auto", "expanded", "collapsed")
    menu_items={             # ✅ Personalizar o menu do canto superior direito
        "Get Help": "https://docs.streamlit.io",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": "Este é um app feito com Streamlit!"
    }
)


person = "Daniel"
row = st.columns(1)
row[0].image("logo2.png", width=150)
st.write("")
st.write("")
st.write("")

pages_dir = "pages"

def listar_paginas():
    return sorted([f for f in os.listdir(pages_dir) if f.endswith(".py")])


st.title("Relatórios de Reunião 📄")

paginas_disponiveis = listar_paginas()

if not paginas_disponiveis:
    st.warning("Nenhum relatório encontrado na pasta 'pages/'. Adicione novos arquivos e aguarde a atualização.")

for page in paginas_disponiveis:
    page_name = page.replace(".py", "").replace("_", " ").title()
    st.page_link(f"{pages_dir}/{page}", label=page_name)


if set(listar_paginas()) != set(paginas_disponiveis):
    st.rerun()  # Recarrega a página automaticamente se novos arquivos forem detectados
