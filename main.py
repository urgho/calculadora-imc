import streamlit as st

#Criar barra lateral
with st.sidebar:
    st.title("Calculadora IMC")

    st.header("O que é IMC?")
    st.markdown("""
O Índice de Massa Corporal (IMC) é uma das principais ferramentas, adotada inclusive pela Organização Mundial de Saúde (OMS), para calcular o chamado “peso ideal”. Obtido a partir do peso e da altura do indivíduo, o IMC também aponta níveis de magreza e obesidade, que são usados para nortear o trabalho de profissionais de saúde e de educadores físicos.
\nPara obter o IMC, basta dividir o seu peso (em quilos) pela altura (em metros) elevada ao quadrado (altura x altura). De acordo com o indicador, o peso considerado saudável é aquele situado entre 18,5 e 24,9.
""")

#Fazendo a calculadora
    st.write("""
    - **Abaixo do Peso**: IMCA menor que 18.5
    - **Peso ideal**: IMC entre 18.5 e 25
    - **Sobrepeso**: IMC entre 25 e 29.9
    - **Obesidade**: IMC entre 30 e 39.9
    - **Obesidade Mórbida**: IMC acima de 40
    """)

st.title("Calculadora IMC")

#Entrada de dados peso
peso = st.number_input(label = "Digite seu peso [KG]", min_value= 0.0, step= 0.1, format = "%.1f"  )
altura = st.number_input(label = "Digite sua altura [Metros]", min_value= 0.0, step= 0.1, format = "%.2f"  )

#Realizar o calculo de IMC
if st.button("Calcular seu IMC"):
    if (peso > 0) and (altura > 0):
        imc = peso/(altura**2)
        imcIdeal = 21.7
        imcDelta = imc - imcIdeal

        if (imc < 18.5):
            classe = "Abaixo do Peso"
        
        elif (imc < 25):
            classe = "Peso ideal"
        
        elif (imc < 30):
            classe = "Sobrepeso"

        elif (imc < 40):
            classe = "Obesidade"
        
        else:
            classe = "Obeso(a) Mórbido(a)"
        st.success("Calculo realizado com sucesso!")
        
        #Escrever os valores
        st.write(f"Seu IMC é: ***{imc:.2f}***")
        st.write(f"Classificação: **{classe}**")
        st.write(f"Comparação com seu IMC ideal (21.7): **{imcDelta:.2f}**")
        

        #Dividir a linha em duas colunas
        col1, col2 = st.columns(2)

        col1.metric("Classificação de Peso", classe, f"{imcDelta:.2f}", delta_color="inverse")
        col2.metric("IMC", f"{imc:.2f}", f"{imcDelta:.2f}", delta_color="off")
        

        #Criar uma linha
        st.divider()

        st.image("./imc.png")

else:
    #Mensagem de Erro
    st.error("Por favor inserir valores válidos para o peso e altura.") 