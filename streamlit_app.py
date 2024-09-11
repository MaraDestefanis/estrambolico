import streamlit as st
import os

# Configuración de Streamlit
st.set_page_config(page_title="Visualización de Mapas de Distribuidora Dimal", layout="wide")

# Configuración de colores
st.markdown("""
    <style>
    .main {
        background-color: #621300;
        color: #FFFFFF;
    }
    .sidebar .sidebar-content {
        background-color: #FFFFFF;
        color: #621300;
    }
    .sidebar .sidebar-content a {
        color: #621300;
    }
    .sidebar .sidebar-content img {
        width: 100%;
        max-width: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

# Menú lateral
with st.sidebar:
    st.image("Logo.png", width=150)
    opcion = st.radio("Seleccionar Opción", options=["Mapas", "Mapa demora", "Mapa informacion clientes", "Nombre Datos"])

# Diccionarios para las semanas y sus días correspondientes
semanas_julio = {
    "Día 1 al 7": 1,
    "Día 8 al 14": 2,
    "Día 15 al 21": 3,
    "Día 22 al 28": 4,
    "Día 29 al 31": 5
}

semanas_agosto = {
    "Día 1 al 4": 1,
    "Día 5 al 11": 2,
    "Día 12 al 18": 3,
    "Día 19 al 25": 4,
    "Día 26 al 31": 5
}

# Función para mostrar mapas
def mostrar_mapa(ruta_archivo, altura=600):
    if os.path.isfile(ruta_archivo):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                html_data = f.read()
                st.components.v1.html(html_data, height=altura, scrolling=True)
        except Exception as e:
            st.error(f"Ocurrió un error al cargar el archivo: {e}")
    else:
        st.error(f"No se encontró el archivo en la ruta: {ruta_archivo}")

# Función para seleccionar mes y semana
def seleccionar_mes_semana():
    mes = st.radio("Seleccionar Mes", options=['Julio', 'Agosto'])
    if mes == "Julio":
        semana = st.radio("Seleccionar Semana", options=list(semanas_julio.keys()))
        numero_semana = semanas_julio[semana]
        directorio_mes = 'mapas_html/Julio'
        sufijo_mes = '07'
    else:
        semana = st.radio("Seleccionar Semana", options=list(semanas_agosto.keys()))
        numero_semana = semanas_agosto[semana]
        directorio_mes = 'mapas_html/Agosto'
        sufijo_mes = '08'
    return mes, semana, numero_semana, directorio_mes, sufijo_mes

# Opción "Mapas"
if opcion == "Mapas":
    st.write("Seleccione el mes y la semana:")
    mes, semana, numero_semana, directorio_mes, sufijo_mes = seleccionar_mes_semana()

    # Usar st.expander para mostrar los mapas solo cuando se expande la sección
    with st.expander(f"Mostrar mapas para la Semana {semana}"):
        # Mostrar el mapa general semanal
        st.write(f"### Mapa Semanal por Día")
        ruta_archivo_general = os.path.join(directorio_mes, f"mapa_semana_{numero_semana}_{sufijo_mes}.html")
        mostrar_mapa(ruta_archivo_general)

        # Mostrar el mapa filtrado por camión
        st.write(f"### Mapa Filtrado por Camión")
        ruta_archivo_placa = os.path.join(directorio_mes, f"mapa_semana_{numero_semana}_{sufijo_mes}_placa.html")
        mostrar_mapa(ruta_archivo_placa)

# Opción "Mapa demora"
elif opcion == "Mapa demora":
    st.write("Seleccione el mes y la semana:")
    mes, semana, numero_semana, directorio_mes, sufijo_mes = seleccionar_mes_semana()

    with st.expander(f"Mostrar mapa para la Semana {semana}"):
        # Mostrar el mapa filtrado por duración
        st.write(f"### Mapa Filtrado por Duración")
        ruta_archivo_duracion = os.path.join(directorio_mes, f"mapa_semana_{numero_semana}_{sufijo_mes}_duracion.html")
        mostrar_mapa(ruta_archivo_duracion)

# Opción "Mapa informacion clientes"
elif opcion == "Mapa informacion clientes":
    st.write("Seleccione el mes y la semana:")
    mes, semana, numero_semana, directorio_mes, sufijo_mes = seleccionar_mes_semana()

    with st.expander(f"Mostrar mapa para la Semana {semana}"):
        # Mostrar el mapa filtrado por proyecto
        st.write(f"### Mapa Filtrado por Proyecto")
        ruta_archivo_proyecto = os.path.join(directorio_mes, f"mapa_semana_{numero_semana}_{sufijo_mes}_proyecto.html")
        mostrar_mapa(ruta_archivo_proyecto)

# Nueva opción "Nombre Datos"
elif opcion == "Nombre Datos":
    st.write("Seleccione el mes y la semana:")
    mes, semana, numero_semana, directorio_mes, sufijo_mes = seleccionar_mes_semana()

    with st.expander(f"Mostrar mapa para la Semana {semana}"):
        st.write(f"### Mapa para Nombre Datos")
        ruta_archivo_nombre_datos = os.path.join(directorio_mes, f"mapa_semana_{numero_semana}_{sufijo_mes}_nombre_datos.html") 
        mostrar_mapa(ruta_archivo_nombre_datos)
