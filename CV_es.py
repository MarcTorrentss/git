#-----------------------------LIBRERIAS---------------------------------------------
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import plotly_express as px
from PIL import Image
import plotly.graph_objs as go
import streamlit.components.v1 as components
from unicodedata import name 

#------------------------CONFIGURACION DE PAGINA------------------------------------
st.set_page_config(page_title="CV", layout="centered", page_icon="📋")

#--------------------------EMPIEZA NUESTRA APP------------------------------------------
st.markdown("<h1 style='text-align: center; '>Marc Torrents</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; '>Currículum Vitae</h2>", unsafe_allow_html=True)
st.text("") # Espacio
me = Image.open('me.jpeg')
col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')
with col2:
    st.image(me)
with col3:
    st.write(' ')

st.text("") # Espacio

st.markdown("✅ Con un recorrido en el mundo de la automatización industrial y en el sector de la energía he descubierto mi pasión por los datos.")
st.markdown("🔜 Después de realizar un Máster en Big Data y Data Science y un Bootcamp de Data Analyst actualmente busco especializarme como data scientist / data analyst / data engineer.")

st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("## 📍 Información de contacto")
st.markdown("✉️ mtorrentsdomenech@gmail.com")
st.markdown("🔗[Linkedin](https://www.linkedin.com/in/mtorrents/)")
st.markdown("🔗[Github](https://github.com/MarcTorrentss)")

st.text("") # Espacio
st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("## 👨🏻‍💼 Experiencia laboral")

st.text("") # Espacio

col4, col5, col6 = st.columns((2.5,0.5,6))
with col4:
    st.markdown("**febrero 2023 - Actualidad**")
    ntt = Image.open('ntt data.png')
    st.image(ntt)
with col5:
    st.write('')
with col6:
    st.markdown("### Junior Data Analyst")
    st.markdown("##### [NTT Data](https://es.nttdata.com/) en Barcelona")
    st.markdown("Multinacional especializada en servicios de consultoría tecnológica.")
    st.markdown("Dentro de NTT formo parte del departamento de ExO (Experience Optimitzation) en el que se lideran proyectos y servicios de canales digitales.")
    with st.expander("Funciones realizadas"):
            st.markdown('''* Implementación de analítica en APP y WEB y qa.
* Procesos ETL sobre los datos.
* Creación de dashboards en Adobe Analytics / Google Analytics o reportings Power BI de los diferentes flujos de etiquetado.
* Control y predicción del consumo de licencias de las herramientas de analítica.''')

st.text("") # Espacio

col7, col8, col9 = st.columns((2.5,0.5,6))
with col7:
    st.markdown("**enero 2021 - junio 2022**")
    ee = Image.open('ee.jpeg')
    st.image(ee)
with col8:
    st.write('')
with col9:
    st.markdown("### Energy Manager")
    st.markdown("##### [Engipro Energy](http://www.engipro-energy.com/es/) en Mataró, Barcelona alrededores")
    st.markdown("Consultoria dedicada a la gestión y contratación energética, ingenieria energética y procesos de certificaciones energéticas.")
    with st.expander("Funciones realizadas"):
            st.markdown('''* Auditorías energéticas, estudios de eficiencia energética y fotovoltaica en plantas industriales y hoteles.
* Gestión de datos y desarrollo de herramientas digitales que permiten analizar y optimizar de manera tangible los costes medioambientales y económicos de las empresas.
* Control, gestión y monitorización de consumos energéticos, creación de Dashboards y control de resultados en PowerBI.
* Redacción de informes y presentaciones a los clientes.
''')

st.text("") # Espacio

col10, col11, col12 = st.columns((2.5,0.5,6))
with col10:
    st.markdown("**septiembre 2019 - enero 2021**")
    g = Image.open('g.png')
    st.image(g)
with col11:
    st.write('')
with col12:
    st.markdown("### Energy Manager")
    st.markdown("##### [Greenflex](https://www.greenflex.com/es/) en Barcelona")
    st.markdown("Eficiencia y gestión energética en la sede española de Barcelona en una empresa francesa del grupo Total.")
    with st.expander("Funciones realizadas"):
            st.markdown('''* Auditorías energéticas, estudios de medidas de eficiencia energética, renovables y sostenibilidad en industria y retail.
* Gestión de datos y desarrollo de herramientas digitales que permiten analizar y optimizar de manera tangible los costes medioambientales y económicos de las empresas.
* Control y gestión de consumos energéticos, redacción de informes y presentaciones a los clientes.
''')

st.text("") # Espacio

col13, col14, col15 = st.columns((2.5,0.5,6))
with col13:
    st.markdown("**marzo 2018 - julio 2019**")
    ra = Image.open('ra.png')
    st.image(ra)
with col14:
    st.write('')
with col15:
    st.markdown("### Intern Engineering")
    st.markdown("##### [Rockwell Automation](https://www.rockwellautomation.com/es-es.html) en Barcelona")
    st.markdown("Interno en el departamento de postventa CSM en la sede española de Barcelona de una de las empresa multinacional líder en la automatización industrial.")
    with st.expander("Funciones realizadas"):
            st.markdown('''* Recopilación, preparación y mantenimiento de la documentación necesaria para cursos de formación y ejecución de proyectos de automatización y gestión logística y mantenimiento de los equipos.
* Apoyo en proyectos de automatización industrial (PLCs, servomotores, pantallas, comunicaciones industriales..).
''')

st.text("") # Espacio
st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

col16, col17, col18 = st.columns((4,2,4))
with col16:
    st.markdown("## 🎯Competencias")
    st.markdown("#### Big Data y Data Science")
    with st.expander("Lenguages de programación"):
        st.markdown('''* Python
* R
* PL-SQL
* T-SQL''')
    with st.expander("Software de programación"):
        st.markdown('''* Jupyter
* Visual Studio Code
* Colab
* RStudio
* MySQL Workbench
* Oracle SQL Developer
* Dbeaver
* pgAdmin''')
    with st.expander("Software de analítica"):
        st.markdown('''* Tealium
* Adobe Analytics
* Google Analytics
* GTM4''')
    with st.expander("Software de visualización"):
        st.markdown('''* PowerBI
* Tableau
* Qlik''')
    st.markdown("#### Automatización Industrial")
    with st.expander("Hardware ROK"):
        st.markdown('''* PanelView (SCADA)
* ControlLogix
* CompactLogix
* PointIO
* FlexIO
* PowerFlex
* Kinetix
* SLC500
* PLC5''')
    with st.expander("Software ROK"):
        st.markdown('''* FactoyTalkView Studio
* RStudio5000
* RSLogix5000
* RSLogix500
* RSLogix5
* RSLinx
* Motion analizer
* Integrated Architecture Builder
* LogixEmulate.''')
    st.markdown("#### Microsoft")
    with st.expander("Software"):
        st.markdown('''* PowerBI
* Excel
* Word
* PowerPoint
* Outlock
* OneDrive
* OneNote
* Skype
* Teams''')
with col17:
    st.write('')
with col18:
    st.markdown("## 🗣️Idiomas")
    st.markdown("#### Catalan")
    st.markdown("Nativo")
    st.markdown("#### Español")
    st.markdown("Nativo")
    st.markdown("#### Inglés")
    st.markdown("B2")

st.text("") # Espacio
st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("## 📚 Educación")

col19, col20, col21 = st.columns((2.5,0.5,6))
with col19:
    st.markdown("**noviembre 2022 - actualidad**")
    uh = Image.open('uh.jpg')
    st.image(uh)
with col20:
    st.write('')
with col21:
    st.markdown("### Bootcamp Data Analytics")
    st.markdown("##### [Upgrade Hub](https://www.upgrade-hub.com/landing-data/?utm_source=google-search&utm_medium=cpc&utm_campaign=Search_ES_Todos_Marca_GA-041&pkw=Upgrade%20hub&utm_term=Upgrade%20hub&matchtype=b&device=c&utm_content=534085417910&placement=&network=g&gclid=Cj0KCQiAm5ycBhCXARIsAPldzoVaEphzsWy90kGmWK11hp7W3iY0OaXNAAt-luc41ksLZpxc8RpK98UaAnMdEALw_wcB)")
    with st.expander("Temario del curso"):
            st.markdown('''* 1. Recopilación de data
    
    *Python, SQL, scripts y APIS*
    
* 2. Visualizaciones y cómo comunicar el análisis de datos
    
    *Exploratory Data Analysis (EDA), Data Storytelling, Testing de Hypothesis y Business Intelligence: Power BI.*
    
* 3. Machine learning
    
    *Ciclo de vida en Machine Learning, Aprendizaje supervisado y no supervisado, Optimización de hyper-parámetros, Series temporales y optimización lineal*
''')

st.text("") # Espacio

col22, col23, col24 = st.columns((2.5,0.5,6))
with col22:
    st.markdown("**noviembre 2021 - octubre 2022**")
    ub = Image.open('ub.jpg')
    st.image(ub)
with col23:
    st.write('')
with col24:
    st.markdown("### Máster en Big Data y Data Science")
    st.markdown("##### [IL3 - Universidad de Barcelona](https://www.il3.ub.edu/master-big-data-science)")
    with st.expander("Temario del curso"):
            st.markdown('''* 1. Herramientas de big data

* 2. Fundamentos de Estadística
    
    *BBDD, Cloud y Git / R y Python / PowerBI, Tableau y Qlik*
    
* 3. Gestión de datos y datos digitales
    
    *APIs y Web Scrapping / Calidad y preparación de datos*
    
* 4. Técnicas avanzadas de minería de datos
    
    *Análisis multivariante, PCE, discriminante, cluster y  TCL*
    
* 5. Técnicas avanzadas de predicción
    
    *Modelos supervisados y no supervisados*
    
    *Training validation y cross validation*
    
    *Regresión lineal y logística, GLM , Ridge, PLS y SSTT*
    
* 6. Técnicas de Machine Learning
    
    *Algoritmos supervisados y ensamblados*
    
* 7. Técnicas avanzadas de Machine Learning

* 8. Gestión de proyectos

* 9. Trabajo final de máster
''')

st.text("") # Espacio

col25, col26, col27 = st.columns((2.5,0.5,6))
with col25:
    st.markdown("**septiembre 2014 - junio 2019**")
    tc = Image.open('tc.png')
    st.image(tc)
with col26:
    st.write('')
with col27:
    st.markdown("### Grado en Ingeniería Electrónica Industrial y Automática")
    st.markdown("##### [TecnoCampus, Universitat Pompeu Fabra](https://www.tecnocampus.cat/es/grau/grau-en-enginyeria-electronica-industrial-i-automatica)")

st.text("") # Espacio
st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("## 📋Aptitudes Personales")
st.markdown('''* Trabajando soy una persona constante, pulcra, ordenada, responsable, autodidacta, trabajadora y con muchas ganas de aprender.
* En relaciones personales / laborales soy una persona respetuosa, sincera, comunicativa, comprometida, empática y que sabe trabajar en equipo.''')
