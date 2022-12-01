import streamlit as st


st.title("Bissoni Record's")

st.header("Perguntas: ")

pergunta1 = st.radio('Você sabia que eu te amo?', ['sim', 'não', 'hmmm'], 2)

match pergunta1:
    case 'sim':
        st.write(':fire::sparkling_heart::fire: Weeeeeeeeeeeeeeeeeeeeeeeee :fire::sparkling_heart::fire:')
    case 'não':
        st.write(':angry::angry::angry:É OQQQQQQQ????:angry::angry::angry:')
        st.write('TU TÁ DE SACANAGEM LUIZA BISSONI?')
    case 'hmmm':
        st.write('   ...sem pressão')