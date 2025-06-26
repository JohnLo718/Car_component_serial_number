import streamlit as st
from serialfinder import SerialNumberFinder

DATA_FILE = 'data/serial_numbers.json'

finder = SerialNumberFinder(DATA_FILE)

st.title('Car Component Serial Number Finder')

component = st.text_input('Enter the component name')
if component:
    serial = finder.find(component)
    if serial:
        st.success(f'Serial number for {component}: {serial}')
    else:
        st.error('Serial number not found')

