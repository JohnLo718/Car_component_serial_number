<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
import streamlit as st

from pathlib import Path
from serialfinder import SerialNumberFinder

DATA_FILE = Path(__file__).parent / "data" / "serial_numbers.json"

finder = SerialNumberFinder(DATA_FILE)
=======
import streamlit as stfrom pathlib import Path
from serialfinder import SerialNumberFinder
DATA_FILE = Path(__file__).parent / "data" / "serial_numbers.json"
from serialfinder import SerialNumberFinder

DATA_FILE = "data/serial_numbers.json"finder = SerialNumberFinder(DATA_FILE)
>>>>>>> main

st.title("Car Component Manager")

MODE_COMPARE = "Compare serial numbers"
MODE_LIST = "List components for a car"
MODE_EDIT = "Edit car components"
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
MODE_ADD = "Add new car"
MODE_DELETE = "Delete car or component"

mode = st.selectbox(
    "Choose action", [MODE_COMPARE, MODE_LIST, MODE_EDIT, MODE_ADD, MODE_DELETE]
)
=======
MODE_ADD = "Add new car"MODE_DELETE = "Delete car or component"

mode = st.selectbox(
    "Choose action", [MODE_COMPARE, MODE_LIST, MODE_EDIT, MODE_ADD, MODE_DELETE]
mode = st.selectbox(
    "Choose action", [MODE_COMPARE, MODE_LIST, MODE_EDIT, MODE_ADD])
>>>>>>> main

if mode == MODE_COMPARE:
    car1 = st.text_input("Enter first car serial number")
    car2 = st.text_input("Enter second car serial number")
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit

=======
>>>>>>> main
    if car1 and car2:
        comps1 = finder.get_components(car1)
        comps2 = finder.get_components(car2)

        if comps1 is None:
            st.error(f"Car serial {car1} not found")
        if comps2 is None:
            st.error(f"Car serial {car2} not found")
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit

        if comps1 and comps2:
=======
    if car1 and car2:
        comps1 = finder.get_components(car1)
        comps2 = finder.get_components(car2)
        if comps1 is None:
            st.error(f'Car serial {car1} not found')
        if comps2 is None:
            st.error(f'Car serial {car2} not found')        if comps1 and comps2:
>>>>>>> main
            set1 = set(comps1)
            set2 = set(comps2)
            only1 = set1 - set2
            only2 = set2 - set1
            both = set1 & set2
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit

=======
>>>>>>> main
            st.markdown(
                "<span style='color:red'>Red: only car 1</span>", unsafe_allow_html=True
            )
            st.markdown(
                "<span style='color:blue'>Blue: only car 2</span>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<span style='color:green'>Green: both cars</span>",
                unsafe_allow_html=True,
            )

            for comp in sorted(only1):
                serial = finder.component_serial(comp)
                st.markdown(
                    f"<span style='color:red'>- {comp} ({serial})</span>",
                    unsafe_allow_html=True,
                )
            for comp in sorted(only2):
                serial = finder.component_serial(comp)
                st.markdown(
                    f"<span style='color:blue'>- {comp} ({serial})</span>",
                    unsafe_allow_html=True,
                )
            for comp in sorted(both):
                serial = finder.component_serial(comp)
                st.markdown(
                    f"<span style='color:green'>- {comp} ({serial})</span>",
                    unsafe_allow_html=True,
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
                )

=======
                )            st.markdown("<span style='color:red'>Red: only car 1</span>", unsafe_allow_html=True)
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
>>>>>>> main
elif mode == MODE_LIST:
    car = st.text_input("Enter car serial number")
    if car:
        comps = finder.get_components(car)
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
        if comps is None:
            st.error(f"Car serial {car} not found")
=======
        if comps is None:            st.error(f"Car serial {car} not found")
>>>>>>> main
        else:
            st.subheader(f"Components for {car.upper()}")
            for comp in comps:
                serial = finder.component_serial(comp)
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
                st.write(f"{comp} - {serial}")

=======
                st.write(f"{comp} - {serial}")            st.error(f'Car serial {car} not found')
        else:
            st.subheader(f'Components for {car.upper()}')
            for comp in comps:
                serial = finder.component_serial(comp)
                st.write(f'{comp} - {serial}')
>>>>>>> main
elif mode == MODE_EDIT:
    car = st.text_input("Enter car serial number to edit")
    if car:
        comps = finder.get_components(car)
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
        if comps is None:
            st.error(f"Car serial {car} not found")
=======
        if comps is None:            st.error(f"Car serial {car} not found")
>>>>>>> main
        else:
            comp = st.selectbox("Select component", comps)
            current = finder.component_serial(comp) or ""
            new_serial = st.text_input("Serial number", value=current)
            if st.button("Update component serial"):
                finder.edit_component(comp, new_serial)
                finder.save()
                st.success("Component updated")
            new_comp = st.text_input("New component name")
            new_comp_serial = st.text_input("New component serial")
            if st.button("Add component to car") and new_comp and new_comp_serial:
                finder.add_component_to_car(car, new_comp)
                finder.edit_component(new_comp, new_comp_serial)
                finder.save()
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
                st.success("Component added")

elif mode == MODE_ADD:
    car = st.text_input("New car serial")
    comps = st.text_area('Components and serials (one per line "component,serial")')
    if st.button("Add car") and car and comps:
        comp_list = []
        for line in comps.splitlines():
            if "," in line:
                name, serial = [p.strip() for p in line.split(",", 1)]
                comp_list.append(name)
                finder.edit_component(name, serial)
        if comp_list:
            finder.add_car(car, comp_list)
            finder.save()
            st.success(f"Car {car} added")
=======
                st.success("Component added")            st.error(f'Car serial {car} not found')
        else:
            comp = st.selectbox('Select component', comps)
            current = finder.component_serial(comp) or ''
            new_serial = st.text_input('Serial number', value=current)
            if st.button('Update component serial!'):
                finder.edit_component(comp, new_serial)
                finder.save()
                st.success('Component updated')
            new_comp = st.text_input('New component name')
            new_comp_serial = st.text_input('New component serial')
            if st.button('Add component to car') and new_comp and new_comp_serial:
                finder.add_component_to_car(car, new_comp)
                finder.edit_component(new_comp, new_comp_serial)
                finder.save()
                st.success('Component added')
elif mode == MODE_ADD:
    car = st.text_input("New car serial")
    comps = st.text_area('Components and serials (one per line "component,serial")')    if st.button("Add car") and car and comps:
        comp_list = []
        for line in comps.splitlines():
            if "," in line:
                name, serial = [p.strip() for p in line.split(",", 1)]    if st.button('Add car') and car and comps:
        comp_list = []
        for line in comps.splitlines():
            if ',' in line:
                name, serial = [p.strip() for p in line.split(',', 1)]                comp_list.append(name)
                finder.edit_component(name, serial)
        if comp_list:
            finder.add_car(car, comp_list)
            finder.save()            st.success(f"Car {car} added")
>>>>>>> main
        else:
            st.error("No valid components provided")

elif mode == MODE_DELETE:
    choice = st.radio("Delete target", ["Car", "Component from car"])
    if choice == "Car":
        with st.form("delete_car"):
            car = st.text_input("Car serial to delete")
            confirm = st.checkbox("I confirm deletion")
            submitted = st.form_submit_button("Delete car")
            if submitted:
                if confirm:
                    if finder.delete_car(car):
                        finder.save()
                        st.success(f"Car {car} deleted")
                    else:
                        st.error("Car not found")
                else:
                    st.warning("Deletion not confirmed")
    else:
        with st.form("delete_component"):
            car = st.text_input("Car serial")
            component = st.text_input("Component name to delete")
            confirm = st.checkbox("I confirm deletion")
            submitted = st.form_submit_button("Delete component")
            if submitted:
                if confirm:
                    if finder.delete_component_from_car(car, component):
                        finder.save()
                        st.success("Component deleted")
                    else:
                        st.error("Car or component not found")
                else:
<<<<<<< m7vm79-codex/create-car-component-serial-number-finder-with-streamlit
                    st.warning("Deletion not confirmed")
=======
                    st.warning("Deletion not confirmed")            st.success(f'Car {car} added')
        else:
            st.error('No valid components provided')
>>>>>>> main
