import streamlit as st
import os
import time

# Diretório onde estão os relatórios
pages_dir = "pages"

# Criar uma função para listar os arquivos no diretório pages/
def listar_paginas():
    return sorted([f for f in os.listdir(pages_dir) if f.endswith(".py")])

st.title("Relatórios de Reunião 📄")

# Criar links para cada página
paginas_disponiveis = listar_paginas()

if not paginas_disponiveis:
    st.warning("Nenhum relatório encontrado na pasta 'pages/'. Adicione novos arquivos e aguarde a atualização.")

for page in paginas_disponiveis:
    page_name = page.replace(".py", "").replace("_", " ").title()
    st.page_link(f"{pages_dir}/{page}", label=page_name)

# Simular atualização automática verificando mudanças a cada X segundos
with st.spinner("Verificando novos relatórios..."):
    time.sleep(5)  # Aguarda 5 segundos antes de verificar novamente
    if set(listar_paginas()) != set(paginas_disponiveis):
        st.rerun()  # Recarrega a página automaticamente se novos arquivos forem detectados
