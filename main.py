import streamlit as st


st.title("Bissoni Record's")

st.header("Perguntas: ")

opcoes = ['sim', 'não', 'hmmmm']

pergunta1 = st.radio('Você sabia que eu te amo?', opcoes, 2)

if pergunta1 == opcoes[0]:
    st.write(':fire::sparkling_heart::fire: Weeeeeeeeeeeeeeeeeeeeeeeee :fire::sparkling_heart::fire:')
elif pergunta1 == opcoes[1]:
    st.write('TU TÁ DE SACANAGEM LUIZA BISSONI?')
else:
    st.write('')


aquela_carinha = """
░░░░░░░░░░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄▄
░░░█░░░░▄▀█▀▀▄░░▀▀▀▄░░░░▐█░░░░░░░░░▄▀█▀▀▄░░░▀█▄
░░█░░░░▀░▐▌░░▐▌░░░░░▀░░░▐█░░░░░░░░▀░▐▌░░▐▌░░░░█▀
░▐▌░░░░░░░▀▄▄▀░░░░░░░░░░▐█▄▄░░░░░░░░░▀▄▄▀░░░░░▐▌
░█░░░░░░░░░░░░░░░░░░░░░░░░░▀█░░░░░░░░░░░░░░░░░░█
▐█░░░░░░░░░░░░░░░░░░░░░░░░░░█▌░░░░░░░░░░░░░░░░░█
▐█░░░░░░░░░░░░░░░░░░░░░░░░░░█▌░░░░░░░░░░░░░░░░░█
░█░░░░░░░░░░░░░░░░░░░░█▄░░░▄█░░░░░░░░░░░░░░░░░░█
░▐▌░░░░░░░░░░░░░░░░░░░░▀███▀░░░░░░░░░░░░░░░░░░▐▌
░░█░░░░░░░░░░░░░░░░░▀▄░░░░░░░░░░▄▀░░░░░░░░░░░░█
░░░█░░░░░░░░░░░░░░░░░░▀▄▄▄▄▄▄▄▀▀░░░░░░░░░░░░░█
"""


pergunta2 = st.radio('Ctz?', opcoes, 2)
if pergunta2 == opcoes[0]:
    st.write(aquela_carinha)
elif pergunta2 == opcoes[1]:
    st.write(':angry::angry::angry:É OQQQQQQQ????:angry::angry::angry:')
else:
    st.write('')

