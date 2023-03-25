from pandas import read_csv
import streamlit as st
from json import loads

st.markdown('''
    # Exibidor de arquivos

    ## Suba um arquivo e vejamos o que acontece
''')

arquivo = st.file_uploader(
    "Suba seu arquivo aqui",
    type=['jpg', 'png', 'py', 'mp3', 'mp4', 'csv', 'json', 'txt']
)

if arquivo:
    print(arquivo.type) # Print é importante para ajustar a questão da tipagem
    match arquivo.type.split('/'):
        case 'application', 'json':
            st.json(loads(arquivo.read()))
        case 'image', _:
            st.image(arquivo)
        case 'application', 'octet-stream':
            st.code(arquivo.read().decode('utf-8'))
        case 'text', 'plain':
            st.code(arquivo.read().decode('utf-8'))
        case 'text', 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
            st.line_chart(df)
        case 'audio', _:
            st.audio(arquivo)
        case 'video', _:
            st.video(arquivo)
else:
    st.error("Ainda não tenho arquivo!!!")