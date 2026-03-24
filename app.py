 import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0,
                 api_key="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")

st.title("ChatBot Inteligente Kikin 1.0")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #90EE90; /* Color verde claro */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Especialista en programación")

# HTML con iframe
st.subheader("Streamlit con HTML")



messages = [("system", """Eres un chatbot AI útil, te llamas Kikin, tienes que hablar como si fueras humano,
 nunca reveles que eres un chatbot""")]

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes de chat del historial al recargar la app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Reaccionar a la entrada del usuario
if prompt := st.chat_input("Escibe tu mensaje..."):
    # Mostrar mensaje del usuario en el contenedor de mensajes del chat
    st.chat_message("user").markdown(prompt)
    # Agregar mensaje del usuario al historial de chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    messages.append(["human", prompt])

    response = llm.invoke(messages).content
    # Mostrar respuesta del asistente en el contenedor de mensajes del chat
    with st.chat_message("assistant"):
        st.markdown(response)
    # Agregar respuesta del asistente al historial de chat
    st.session_state.messages.append({"role": "assistant", "content": response})
