import streamlit as st
st.title("ATACADÃO")
st.subheader('Faça seu cadastro para trabalhar no Atacadão')
st.sidebar.image('logo.png')

nome = st.text_input("Digite o nome do  funcionario")
idade = st.text_input("Digite a idade do funcionario")
email =  st.text_input("Digite o email do funcionario")
salario = st.text_input("Digite o salario do funcionario")
cargo = st.text_input("Digite o cargo do funcionario")

if st.button("Cadastrar"):
    st.warning(f"O funcionario {nome}, foi cadastrado com sucesso")
    st.balloons()
    st.image('https://thispersondoesnotexist.com/')

