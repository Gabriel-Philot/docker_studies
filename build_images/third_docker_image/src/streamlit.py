import streamlit as st
from slot import main
import redis
import json
import pandas as pd

r = redis.Redis(host='redis', port=6379)

st.title("Performance de Classes com Slots")

num_rows_options = [10, 100, 500, 2000]
num_rows = st.selectbox("Número de linhas", num_rows_options)

iterations_options = [5, 10, 50, 200]  
iterations = st.selectbox("Número de iterações", iterations_options)



if st.button("Executar"):
    time_without_slots, time_with_slots, percentage_difference, time_without_classes=main(iterations, num_rows)
    st.write("Tempo sem slots:", time_without_slots, "segundos")
    st.write("Tempo com slots:", time_with_slots, "segundos")
    st.write("Diferença percentual:", round(percentage_difference, 2), "%")
    st.write("Tempo sem classes:", time_without_classes, "segundos")
    data = {
        'num_rows': num_rows,
        'iterations': iterations,
        'time_without_slots': time_without_slots,
        'time_with_slots': time_with_slots, 
        'percentage_difference': percentage_difference,
        'time_without_classes': time_without_classes
    }
    r.rpush('results', json.dumps(data))

with st.expander("Dados persistidos", expanded=True):
  results = [json.loads(x) for x in r.lrange('results', 0, -1)]

  df = pd.DataFrame(results)

  # adicionar índice como coluna
  df['index'] = df.index

  st.write(df.set_index('index'))