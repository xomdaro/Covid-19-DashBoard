import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from pathlib import Path

def load_css():
    css_path = Path(__file__).parent / "assets" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

from src.data_loader import baixar_dados, carregar_dados
from src.visualizer import gerar_grafico
import os

DATA_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "owid-covid-data.csv")

def main():
    st.set_page_config(page_title="COVID Dashboard", layout="wide")
    st.title("🌍 Novos casos diários de COVID-19")

    pais = st.text_input("Digite o nome do país (ex: Brazil, Portugal, United States):", "Brazil")

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    baixar_dados(DATA_URL, DATA_FILE)
    df = carregar_dados(DATA_FILE)
    print("Dados carregados com sucesso!")

    if pais not in df['location'].unique():
        st.error(f"❌ País '{pais}' não encontrado. Tente outro nome!")
    else:
        fig = gerar_grafico(df, pais)
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()