import streamlit as st
import pandas as pd
import numpy as np
import time

from math import *
from math import radians as Deg
from fractions import Fraction


# CSS Style
st.html(f"""
<style>
        div[data-testid='column'] {{
        text-align: center;
        float: center;
        }}

        div.stButton>button[kind='secondary']{{
        border: 1px solid grey;
        width:80px;
        font-size:5px;
        }}

        div.stButton>button[kind='secondary']:hover{{
        border:1px solid grey;
        color:grey;
        }}

        div.stButton>button[kind='secondary']:active{{
        border:1px solid grey;
        color:white;
        }}

        div.stButton>button[kind='primary']{{
        width:80px;
        color:white;
        }}

        div.stButton>button[kind='primary']:hover{{
        color:white;
        }}
        
        div.stDataFrame {{
        text-align: center;
        }}
</style>""")


## Session State ##
if 'input' not in st.session_state:
    st.session_state.input=''
if 'disable_button' not in st.session_state:
    st.session_state.disable_button=False
if 'angle_change' not in st.session_state:
    st.session_state.angle_change='Radians'
if 'fractions' not in st.session_state:
    st.session_state.fractions=False


## Functions Calculator ##
def add_7():
    st.session_state.input+='7'
def add_4():
    st.session_state.input+='4'
def add_1():
    st.session_state.input+='1'
def add_percent():
    st.session_state.input+='%'
def add_8():
    st.session_state.input+='8'
def add_5():
    st.session_state.input+='5'
def add_2():
    st.session_state.input+='2'
def add_0():
    st.session_state.input+='0'
def add_9():
    st.session_state.input+='9'
def add_6():
    st.session_state.input+='6'
def add_3():
    st.session_state.input+='3'
def add_x():
    st.session_state.input+='x'
def add_y():
    st.session_state.input+='y'
def add_dot():
    st.session_state.input+='.'
def add_plus():
    st.session_state.input+='+'
def add_minus():
    st.session_state.input+='-'
def add_multiply():
    st.session_state.input+='×'
def add_divide():
    st.session_state.input+='÷'
def add_root():
    st.session_state.input+='√('
def add_exponent():
    st.session_state.input+='^'
def add_parenthese():
    st.session_state.input+='('
def add_parenthese2():
    st.session_state.input+=')'
def delete():
    st.session_state.input=st.session_state.input[:-1]
def add_sin():
    if st.session_state.angle_change=='Degrees':  
        st.session_state.input+='sin(Deg('   # Add degree sine function
    else:
        st.session_state.input+='sin('       # Add radian sine function
def add_cos():
    if st.session_state.angle_change=='Degrees':
        st.session_state.input+='cos(Deg('   # Add degree cosine function
    else:
        st.session_state.input+='cos('       # Add radian cosine function
def add_tan():
    if st.session_state.angle_change=='Degrees':
        st.session_state.input+='tan(Deg('   # Add degree tangent function
    else:
        st.session_state.input+='tan('       # Add radian tangent function
def clear_all():
    st.session_state.pop('input')
    st.session_state.disable_button=False
def add_pi():
    st.session_state.input+='π'
def add_log():
    st.session_state.input+='log('
def add_abs():
    st.session_state.input+='abs('
def add_factorial():
    st.session_state.input+='n!('
def add_fraction():
    st.session_state.input+='(1/'
def add_e():
    st.session_state.input+='e'


def calculate():
    # Replace all math operators
    st.session_state.input=st.session_state.input.replace('×','*')
    st.session_state.input=st.session_state.input.replace('÷','/')
    st.session_state.input=st.session_state.input.replace('√(','sqrt(')
    st.session_state.input=st.session_state.input.replace('^','**')
    st.session_state.input=st.session_state.input.replace('π','pi')
    st.session_state.input=st.session_state.input.replace('n!(','factorial(')
    st.session_state.input=st.session_state.input.replace('%','/100')

    try:
        st.session_state.input=eval(st.session_state.input)
        st.session_state.input="%g"%(float(st.session_state.input))

        if st.session_state.fractions:
            if len(st.session_state.input[st.session_state.input.find('.')+1:])>=5:
               st.session_state.input="%s"%(Fraction(st.session_state.input).limit_denominator(10))
            else:
                st.session_state.input="%s"%(Fraction(st.session_state.input))

    except ZeroDivisionError:
        st.session_state.input='Math ERROR - Click [AC] to Reset'
    except:
        st.session_state.input='Syntax ERROR - Click [AC] to Reset'
    st.session_state.disable_button=True


# STREAMLIT
st.write("")
st.title("Metode Secant")
st.write("")
st.write("**Masukkan fungsi f(x) :**")


## CALCULATOR DISPLAY ##
container=st.container(border=True)
container.write(f"<p align='left'><span style='font-size:40px;'>{st.session_state.input}</span></p>",unsafe_allow_html=True)
container.divider()


## Columns for sorting button Calculator ##
col1,col2,col3,col4,col5,col6,col7=container.columns([1,1,1,1,1,1,1])

with col1:
   st.button(label='7',on_click=add_7,disabled=st.session_state.disable_button)
   st.button(label='4',on_click=add_4,disabled=st.session_state.disable_button)
   st.button(label='1',on_click=add_1,disabled=st.session_state.disable_button)
   st.button(label='%',on_click=add_percent,disabled=st.session_state.disable_button)

with col2:
    st.button(label='8',on_click=add_8,disabled=st.session_state.disable_button)
    st.button(label='5',on_click=add_5,disabled=st.session_state.disable_button)
    st.button(label='2',on_click=add_2,disabled=st.session_state.disable_button)
    st.button(label='0',on_click=add_0,disabled=st.session_state.disable_button)

with col3:
    st.button(label='9',on_click=add_9,disabled=st.session_state.disable_button)
    st.button(label='6',on_click=add_6,disabled=st.session_state.disable_button)
    st.button(label='3',on_click=add_3,disabled=st.session_state.disable_button)
    st.button(label='.',on_click=add_dot,disabled=st.session_state.disable_button)

with col4:
    st.button(label='**+**',on_click=add_plus,disabled=st.session_state.disable_button)
    st.button(label='**-**',on_click=add_minus,disabled=st.session_state.disable_button)
    st.button(label='×',on_click=add_multiply,disabled=st.session_state.disable_button)
    st.button(label='÷',on_click=add_divide,disabled=st.session_state.disable_button)

with col5:
    st.button(label='√',on_click=add_root,disabled=st.session_state.disable_button)
    st.button(label='xʸ',on_click=add_exponent,disabled=st.session_state.disable_button)
    st.button(label='(',on_click=add_parenthese,disabled=st.session_state.disable_button)
    st.button(label=')',on_click=add_parenthese2,disabled=st.session_state.disable_button)

with col6:
    st.button(label='DEL',type='primary',on_click=delete,disabled=st.session_state.disable_button)
    st.button(label='sin',type='primary',on_click=add_sin,disabled=st.session_state.disable_button)
    st.button(label='cos',type='primary',on_click=add_cos,disabled=st.session_state.disable_button)
    st.button(label='tan',type='primary',on_click=add_tan,disabled=st.session_state.disable_button)

with col7:
    st.button(label='AC',type='primary',on_click=clear_all)
    st.button(label='e',type='primary',on_click=add_e,disabled=st.session_state.disable_button)
    st.button(label='x',type='primary',on_click=add_x,disabled=st.session_state.disable_button)
    st.button(label='y',type='primary',on_click=add_y,disabled=st.session_state.disable_button)


# MAIN
import numpy as np

def secant_nm(fx, Ximin, Xi, epsilon):
    def f(x):
        f = eval(fx)
        return f

    # Replace all math operators
    fx=fx.replace('×','*')
    fx=fx.replace('÷','/')
    fx=fx.replace('√(','sqrt(')
    fx=fx.replace('^','**')
    fx=fx.replace('π','pi')
    fx=fx.replace('n!(','factorial(')
    fx=fx.replace('%','/100')

    try:
        i = 0
        arrHasil = []
        while True:
            i += 1
            fXimin = f(Ximin)
            fXi = f(Xi)

            Xiplus = Ximin - (fXimin / ((fXimin - fXi) / (Ximin - Xi)))
            persen = np.abs(((Xiplus - Xi) / Xiplus) * 100)

            arrHasil.append([i, Ximin, Xi, fXimin, fXi, Xiplus, f(Xiplus), persen if i > 1 else "-"])

            if persen < epsilon:
                # print()
                # print(f"Akar ditemukan dengan konvergensi pada iterasi ke {i}: {Xiplus}")
                break
            
            Ximin = Xi
            Xi = Xiplus

            if persen == 0:
                break

        return arrHasil
    
    except Exception as e:
        print(f"Error: {e}")


st.write("")

# input streamlit
st.text_input("**Masukkan nilai awal Ximin :**", key="Ximin")
st.text_input("**Masukkan nilai awal Xi :**", key="Xi")
st.text_input("**Masukkan nilai toleransi (epsilon) :**", key="epsilon")

try:
    # INPUT
    fx = st.session_state.input
    Ximin = float(st.session_state.Ximin)
    Xi = float(st.session_state.Xi)
    epsilon = float(st.session_state.epsilon)

    st.write("")

    hasil_iterasi = secant_nm(fx, Ximin, Xi, epsilon)
    
    # progresbar
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Loading... {i+1}%')
        bar.progress(i + 1)
        time.sleep(0.02)
    'Complate!!'

    # hasil tabel
    df = pd.DataFrame(hasil_iterasi, columns=['Iterasi', 'x(i-1)', 'xi', 'f(x(i-1))', 'f(xi)', 'x(i+1)', 'f(x(i+1))', '|∈a|%'])

    st.write("")
    st.write("**Tabel Hasil**")
    st.dataframe(df, hide_index=True, width=1000, height=500, use_container_width=True)

except ValueError:
    st.error("Masukkan nilai yang valid.")
