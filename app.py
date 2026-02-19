import pandas as pd
import streamlit as st

#SIDEBAR
st.sidebar.image("Menú.png")
opcion=st.sidebar.selectbox("Seleccione a donde se quiere dirigir:",["Home","Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if opcion == "Home":

#PORTADA(HOME)
    st.title("Trabajo Practico Python")
    st.image("Python.png")
    st.write("")
    st.write("")
    st.write("**Elaborado por:** Kaori Sakaguchi")
    st.write("**Curso:** Python Fundamentals")
    st.write("**Módulo:** 1")
    st.write("**Año de elaboración:** 2026")
    st.subheader("**OBJETIVO:** ")
    st.write("Es crear una aplicación en streamlit que donde podamos aplicar los fundamentos básicos que se ha ido aprendiendo en el módulo 1 del curso de python")

elif opcion=="Ejercicio 1":


    #EJERCICIO 1
    #Descripción
    #Desarrollar un verificador simple donde el usuario ingrese un presupuesto y un gasto,
    #y el sistema determine si el gasto está dentro o fuera del presupuesto.
    st.title("**Ejercicio 1:** Variables y Condicionales")
    st.write("Este módulo nos ayudará a verificar si el presupuesto puede aceptar el gasto registrado")
    presupuesto = st.number_input("**Ingrese el presupuesto:** ")
    gasto= st.number_input("**Ingrese el gasto** ")

    if st.button("Verificar"):
        Validación=presupuesto-gasto

        if gasto <=presupuesto:
            st.success("El gasto está dentro del presupuesto")
            st.write("La diferencia entre el presupuesto y el gasto es:",Validación)
        else:
            st.warning("El gasto excede lo presupuestado")
            st.write("La diferencia entre el presupuesto y el gasto es:",Validación)

elif opcion=="Ejercicio 2":
    #EJERCICIO 2
    #Descripción
    #Crear una estructura que permita registrar actividades financieras. Cada actividad
    #debe almacenarse como un diccionario dentro de una lista.

    st.title("Ejercicio 2 - Registro de actividades")
    if "actividades" not in st.session_state:
        st.session_state.actividades = []

    nombre=st.text_input("Nombre de la actividad")
    tipo=st.selectbox("Tipo de actividad", ["","gasto","Inversión"])
    presupuesto = st.number_input("presupuesto")
    gasto= st.number_input("gasto")


    if st.button("Agregar actividad"):
        actividad={"nombre":nombre,"tipo":tipo,"presupuesto":presupuesto,"gasto":gasto}
        st.session_state.actividades.append(actividad)
        st.success("Actividad agregada correctamente")

    st.write("Lista de actividades registradas")
    st.write(st.session_state.actividades)

    st.write("Estado de actividad")
    for act in st.session_state.actividades:
        if act["gasto"] <= act["presupuesto"]:
            st.write(act["nombre"],"esta dentro del presupuesto")
        else:
            st.write(act["nombre"],"excedio el presupuesto")

elif opcion=="Ejercicio 3":
    #EJERCICIO 3: Descripción
    #Crear una función que calcule el retorno esperado de cada actividad y aplicar ese
    #cálculo utilizando programación funcional (map y lambda).
    st.title("Ejercicio 3 - Cálculo de Retorno")
    if "actividades" not in st.session_state:
        st.session_state.actividades = []
    tasa=st.number_input("Ingrese la tasa (Tiene que estar en decimales (10%=0.10))")
    meses=st.number_input("Ingrese la cantidad de meses")
    if st.button("Calculo de retorno"):
        if len(st.session_state.actividades)>0:
            df=pd.DataFrame(st.session_state.actividades)
            df["Retorno"]= df["presupuesto"]*tasa*meses
            st.write("Resultados del retorno esperado es:")
            st.dataframe(df)
        else:
            st.warning("No hay actividades registradas")

else:
    #DESCRIPCIÓN
    #Implementar una clase que modele una actividad financiera con atributos y métodos propios.
    st.title("Ejercicio 4 - Programación orientada a objetos")
    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto = gasto

        def esta_dentro_del_presupuesto(self):
            return self.gasto <= self.presupuesto

        def mostrar_info(self):
            return f"La actividad: {self.nombre} que es una {self.tipo}"

    objetos = []

    for act in st.session_state.actividades:
        nueva_actividad = Actividad(
            act["nombre"],
            act["tipo"],
            act["presupuesto"],
            act["gasto"]
        )
        objetos.append(nueva_actividad)

    if len(objetos) == 0:
        st.warning("No hay actividades registradas")
    else:
        for obj in objetos:
            st.write(obj.mostrar_info())
            if obj.esta_dentro_del_presupuesto():
                st.success("Está dentro del presupuesto")
            else:
                st.warning("Superó lo presupuestado")

