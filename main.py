import streamlit as st
import os
import time

st.set_page_config(layout="wide")

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
