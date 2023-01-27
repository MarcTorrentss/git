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

st.markdown("✅ With a journey in the world of industrial automation and in the energy sector, I have discovered my passion for data.")
st.markdown("🔜 After doing a Master in Big Data and Data Science and a Data Analyst Bootcamp, I am currently looking to specialize as a data scientist / data analyst / data engineer.")

st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("## 📍 Contact Information")
st.markdown("✉️ mtorrentsdomenech@gmail.com")
st.markdown("🔗[Linkedin](https://www.linkedin.com/in/mtorrents/)")
st.markdown("🔗[Github](https://github.com/MarcTorrentss)")

st.text("") # Espacio
st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("## 👨🏻‍💼 Work Experience")

st.text("") # Espacio

col4, col5, col6 = st.columns((2.5,0.5,6))
with col4:
    st.markdown("**January 2021 - June 2022**")
    ee = Image.open('ee.jpeg')
    st.image(ee)
with col5:
    st.write('')
with col6:
    st.markdown("### Energy Manager")
    st.markdown("##### [Engipro Energy](http://www.engipro-energy.com/es/) in Mataró, Barcelona")
    st.markdown("Consultancy dedicated to energy management and contracting, energy engineering and energy certification processes.")
    with st.expander("Performed functions"):
            st.markdown('''* Energy audits, energy and photovoltaic efficiency studies in industrial plants and hotels.
* Data management and development of digital tools that allow analyzing and tangibly optimizing the environmental and economic costs of companies.
* Control, management and monitoring of energy consumption, creation of Dashboards and control of results in PowerBI.
* Writing reports and presentations to clients.
''')

st.text("") # Espacio

col7, col8, col9 = st.columns((2.5,0.5,6))
with col7:
    st.markdown("**September 2019 - January 2021**")
    g = Image.open('g.png')
    st.image(g)
with col8:
    st.write('')
with col9:
    st.markdown("### Energy Manager")
    st.markdown("##### [Greenflex](https://www.greenflex.com/es/) in Barcelona")
    st.markdown("Efficiency and energy management at the Spanish headquarters in Barcelona in a French company of the Total group.")
    with st.expander("Performed functions"):
            st.markdown('''* Energy audits, studies of energy efficiency measures, renewables and sustainability in industry and retail.
* Data management and development of digital tools that allow analyzing and tangibly optimizing the environmental and economic costs of companies.
* Control and management of energy consumption, writing reports and presentations to clients.
''')

st.text("") # Espacio

col10, col11, col12 = st.columns((2.5,0.5,6))
with col10:
    st.markdown("**March 2018 - July 2019**")
    ra = Image.open('ra.png')
    st.image(ra)
with col11:
    st.write('')
with col12:
    st.markdown("### Intern Engineering")
    st.markdown("##### [Rockwell Automation](https://www.rockwellautomation.com/es-es.html) in Barcelona")
    st.markdown("Intern in the CSM after-sales department at the Spanish headquarters in Barcelona of one of the leading multinational companies in industrial automation.")
    with st.expander("Performed functions"):
            st.markdown('''* Compilation, preparation and maintenance of the necessary documentation for training courses and execution of automation projects, logistics management and equipment maintenance.
* Support in industrial automation projects (PLCs, servomotors, screens, industrial communications...)
''')

st.text("") # Espacio
st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

col13, col14, col15 = st.columns((4,2,4))
with col13:
    st.markdown("## 🎯Skills")
    st.markdown("#### Big Data y Data Science")
    with st.expander("Programming languages"):
        st.markdown('''* Python
* R
* PL-SQL
* T-SQL''')
    with st.expander("Programming software"):
        st.markdown('''* Jupyter
* Visual Studio Code
* Colab
* RStudio
* MySQL Workbench
* Oracle SQL Developer
* Dbeaver
* pgAdmin''')
    with st.expander("Visualization software"):
        st.markdown('''* PowerBI
* Tableau
* Qlik''')
    st.markdown("#### Industrial Automation")
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
with col14:
    st.write('')
with col15:
    st.markdown("## 🗣️Languages")
    st.markdown("#### Catalan")
    st.markdown("Native")
    st.markdown("#### Spanish")
    st.markdown("Native")
    st.markdown("#### English")
    st.markdown("B2")

st.text("") # Espacio
st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("## 📚 Education")

col16, col17, col18 = st.columns((2.5,0.5,6))
with col16:
    st.markdown("**November 2022 - Present**")
    uh = Image.open('uh.jpg')
    st.image(uh)
with col17:
    st.write('')
with col18:
    st.markdown("### Bootcamp Data Analytics")
    st.markdown("##### [Upgrade Hub](https://www.upgrade-hub.com/landing-data/?utm_source=google-search&utm_medium=cpc&utm_campaign=Search_ES_Todos_Marca_GA-041&pkw=Upgrade%20hub&utm_term=Upgrade%20hub&matchtype=b&device=c&utm_content=534085417910&placement=&network=g&gclid=Cj0KCQiAm5ycBhCXARIsAPldzoVaEphzsWy90kGmWK11hp7W3iY0OaXNAAt-luc41ksLZpxc8RpK98UaAnMdEALw_wcB)")
    with st.expander("Course breakdown"):
            st.markdown('''* 1. Data collection
    
    *Python, SQL, scripts y APIS*
    
* 2. Visualizations and how to communicate data analysis
    
    *Exploratory Data Analysis (EDA), Data Storytelling, Testing Hypothesis and Business Intelligence: Power BI.*
    
* 3. Machine learning
    
    *life cycle in Machine Learning, Supervised and unsupervised learning, Hyper-parameter optimization, Time series and linear optimization*
''')

st.text("") # Espacio

col19, col20, col21 = st.columns((2.5,0.5,6))
with col19:
    st.markdown("**November 2021 - October 2022**")
    ub = Image.open('ub.jpg')
    st.image(ub)
with col20:
    st.write('')
with col21:
    st.markdown("### Master in Big Data and Data Science")
    st.markdown("##### [IL3 - Universidad de Barcelona](https://www.il3.ub.edu/master-big-data-science)")
    with st.expander("Course breakdown"):
            st.markdown('''* - 1. Big data tools

- 2. Fundamentals of Statistics
    
    *BBDD, Cloud and Git / R and Python / PowerBI, Tableau and Qlik*
    
- 3. Data management and digital data
    
    *APIs and Web Scrapping / Data quality and preparation*
    
- 4. Advanced data mining techniques
    
    *Multivariate analysis, PCE, discriminant, cluster and TCL*
    
- 5. Advanced prediction techniques
    
    *Supervised and unsupervised models*
    
    *Training validation and cross validation*
    
    *Linear and logistic regression, GLM, Ridge, PLS and SSTT*
    
- 6. Machine Learning Techniques
    
    *Supervised and assembled algorithms*
    
- 7. Advanced Machine Learning techniques
- 8. Project management
- 9. Final project
''')

st.text("") # Espacio

col22, col23, col24 = st.columns((2.5,0.5,6))
with col22:
    st.markdown("**September 2014 - june 2019**")
    tc = Image.open('tc.png')
    st.image(tc)
with col23:
    st.write('')
with col24:
    st.markdown("### Industrial Electronics and Automatic Engineering Degree")
    st.markdown("##### [TecnoCampus, Universitat Pompeu Fabra](https://www.tecnocampus.cat/es/grau/grau-en-enginyeria-electronica-industrial-i-automatica)")

st.text("") # Espacio
st.text("") # Espacio

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("## Personal Aptitudes")
st.markdown('''* Working I am a constant person, neat, orderly, responsible, self-taught, hardworking and eager to learn.
* In personal / work relationships I am a respectful, sincere, communicative, committed, empathetic person who knows how to work as a team.''')
