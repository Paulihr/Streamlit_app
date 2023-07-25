
import streamlit as st

def evaluar_credito(monto, ingresos_mensuales, edad, score_crediticio):
    # Aquí podrías colocar la lógica de evaluación de crédito según tus criterios
    # Por ejemplo, puedes usar reglas condicionales para decidir si se aprueba o no el crédito
    if monto <= 0 or ingresos_mensuales <= 0 or edad <= 0 or score_crediticio <= 0:
        return "Por favor, ingresa valores válidos."
    
    if monto > 50000 and ingresos_mensuales * 12 > monto * 2 and edad >= 18 and score_crediticio > 700:
        return "Crédito APROBADO."
    else:
        return "Crédito RECHAZADO."

def main():
    st.title("Evaluación de Crédito")
    
    st.write("Ingresa los siguientes datos para evaluar tu crédito:")
    
    monto = st.number_input("Monto del crédito:")
    ingresos_mensuales = st.number_input("Ingresos mensuales:")
    edad = st.number_input("Edad:")
    score_crediticio = st.number_input("Score crediticio:")
    
    if st.button("Evaluar"):
        resultado = evaluar_credito(monto, ingresos_mensuales, edad, score_crediticio)
        st.write(resultado)

if __name__ == "__main__":
    main()
