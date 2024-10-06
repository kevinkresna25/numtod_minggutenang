import streamlit as st
import pandas as pd
import numpy as np
import time

# INPUTTTTTTTTTTTTTTTTTTTTTT

#checkbox
st.write("")
st.title("checkbox")
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


#listbox
st.write("")
st.title("listbox")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected: ', option

#radiobutton
st.write("")
st.title("Radio Button")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')
# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


# #progressbar
# st.write("")
# st.title("Progress Bar")
# 'Starting a long computation...'
# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)
# '...and now we\'re done!'



# MAIN
import numpy as np

def secant_nm(fx, Ximin, Xi, epsilon):
    def f(x):
        f = eval(fx)
        return f

    i = 0
    arrHasil = []
    while True:
        i += 1
        fXimin = f(Ximin)
        fXi = f(Xi)

        Xiplus = Ximin - (fXimin / ((fXimin - fXi) / (Ximin - Xi)))
        persen = np.abs(((Xiplus - Xi) / Xiplus) * 100)

        # if i > 1:
        #     print(f"Persenan: {round(persen, 15)}% pada iterasi ke {i}")

        # print(f"Akar ditemukan: {Xiplus}, pada iterasi ke {i}")

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


# STREAMLIT
st.write("")
st.title("Metode Secant")

# input streamlit
st.text_input("Masukkan fungsi f(x) :", key="fx")
st.text_input("Masukkan nilai awal Ximin :", key="Ximin")
st.text_input("Masukkan nilai awal Xi :", key="Xi")
st.text_input("Masukkan nilai toleransi (epsilon) :", key="epsilon")

try:
    fx = st.session_state.fx
    Ximin = float(st.session_state.Ximin)
    Xi = float(st.session_state.Xi)
    epsilon = float(st.session_state.epsilon)

    st.write(f"Fungsi f(x): {fx}")
    st.write(f"Nilai Ximin: {Ximin}")
    st.write(f"Nilai Xi: {Xi}")
    st.write(f"Nilai toleransi epsilon: {epsilon}")

    hasil_iterasi = secant_nm(fx, Ximin, Xi, epsilon)
    
    # hasil tabel
    df = pd.DataFrame(hasil_iterasi, columns=['Iterasi', 'x(i-1)', 'xi', 'f(x(i-1))', 'f(xi)', 'x(i+1)', 'f(x(i+1))', '|∈a|%'])

    st.dataframe(df, hide_index=True)

except ValueError:
    st.error("Masukkan nilai yang valid.")
