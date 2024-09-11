import streamlit as st
left_column, right_column = st.columns(2)
left_column.button('Press me!')
with right_column:
    chosen = st.radio(
	'Sorting hat',
	("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")
