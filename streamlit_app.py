import streamlit as st
from serialfinder import SerialNumberFinder

DATA_FILE = 'data/serial_numbers.json'

finder = SerialNumberFinder(DATA_FILE)

st.title('車輛零件比對')

car1 = st.text_input('請輸入第一輛的序號')
car2 = st.text_input('請輸入第二輛的序號')

if car1 and car2:
    comps1 = finder.get_components(car1)
    comps2 = finder.get_components(car2)

    if comps1 is None:
        st.error(f'Car serial {car1} not found')
    if comps2 is None:
        st.error(f'Car serial {car2} not found')

    if comps1 and comps2:
        set1 = set(comps1)
        set2 = set(comps2)
        only1 = set1 - set2
        only2 = set2 - set1
        both = set1 & set2

        st.markdown("<span style='color:red'>Red: only car 1</span>", unsafe_allow_html=True)
        st.markdown("<span style='color:blue'>Blue: only car 2</span>", unsafe_allow_html=True)
        st.markdown("<span style='color:green'>Green: both cars</span>", unsafe_allow_html=True)

        for comp in sorted(only1):
            serial = finder.component_serial(comp)
            st.markdown(f"<span style='color:red'>- {comp} ({serial})</span>", unsafe_allow_html=True)
        for comp in sorted(only2):
            serial = finder.component_serial(comp)
            st.markdown(f"<span style='color:blue'>- {comp} ({serial})</span>", unsafe_allow_html=True)
        for comp in sorted(both):
            serial = finder.component_serial(comp)
            st.markdown(f"<span style='color:green'>- {comp} ({serial})</span>", unsafe_allow_html=True)
