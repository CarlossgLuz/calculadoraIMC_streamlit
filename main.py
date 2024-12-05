import streamlit as st

# Criar Barra Lateral
with st.sidebar:
    st.title("Calculadora IMC")

    st.header("O que é IMC")
    st.markdown("""
    O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso ideal. Desenvolvido pelo polímata Lambert Quételet no fim do século XIX, trata-se de um método fácil e rápido para a avaliação do nível de gordura de cada pessoa, sendo, por isso, um preditor internacional de obesidade adotado pela Organização Mundial da Saúde (OMS).
    """)

    # Linha com Texto
    st.write("""
    - **Abaixo do Peso:** IMC menor que 18.5
    - **Peso Ideal:** IMC entre 18.5 e 24.9
    - **Sobrepeso:** IMC entre 25 e 29.9
    - **Obesidade:** IMC entre 30 e 39.9
    - **Obesidade Mórbida:** IMC acima de 40
    """)

st.title("Calculadora IMC")

# Entrada de Dados - Peso
peso = st.number_input(label="Insira o seu Peso (KG)", min_value=0.0, step=0.10, format="%.1f")
altura = st.number_input(label="Insira a sua Altura (Metros)", min_value=0.0, step=0.10, format="%.2f")

if st.button("Calcular"):
    if (peso > 0) and (altura > 0):
        imc = peso / (altura ** 2)
        imc_ideal = 21.7
        imc_delta = imc - imc_ideal

        if imc < 18.5:
            classe = "Abaixo do Peso"
        elif imc < 24.9:
            classe = "Peso Ideal"
        elif imc < 29.9:
            classe = "Sobrepeso"
        elif imc < 40:
            classe = "Obesidade"
        else:
            classe = "Obesidade Mórbida"
        
        st.success("Calculo realizado com Sucesso!")

        # Escrever os Valores
        st.write(f"Seu *IMC* é {imc:.2f}")
        st.write(f"Comparação com IMC Ideal (21.7):  **{imc_delta:.2f}**")

        # Dividir a Linha em Colunas
        col1, col2  = st.columns(2)
        col1.metric("Classificação", classe, f"{imc_delta:.2f}", delta_color="inverse")
        col2.metric("IMC", f"{imc:.2f}", f"{imc_delta:.2f}", delta_color="off")

        st.divider()

        st.image("./obesidade.jpg")
    else:
        st.error("Insira valores Válidos para o Peso e Altura.")