import streamlit as st
from pathlib import Path
from serialfinder import SerialNumberFinder

DATA_FILE = Path(__file__).parent / "data" / "serial_numbers.json"
finder = SerialNumberFinder(DATA_FILE)

st.title("Car Component Manager")

MODE_COMPARE = "Compare serial numbers"
MODE_LIST = "List components for a car"
MODE_EDIT = "Edit car components"
MODE_ADD = "Add new car"
MODE_DELETE = "Delete car or component"

mode = st.selectbox(
    "Choose action",
    [MODE_COMPARE, MODE_LIST, MODE_EDIT, MODE_ADD, MODE_DELETE],
)

if mode == MODE_COMPARE:
    car1 = st.text_input("Enter first car serial number").strip()
    car2 = st.text_input("Enter second car serial number").strip()
    if car1 and car2:
        comps1 = finder.get_components(car1)
        comps2 = finder.get_components(car2)

        if comps1 is None:
            st.error(f"Car serial {car1} not found")
        if comps2 is None:
            st.error(f"Car serial {car2} not found")

        if comps1 and comps2:
            set1 = set(comps1)
            set2 = set(comps2)
            only1 = set1 - set2
            only2 = set2 - set1
            both = set1 & set2

            st.markdown(
                "<span style='color:red'>Red: only car 1</span>",
                unsafe_allow_html=True,
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
                )

elif mode == MODE_LIST:
    car = st.text_input("Enter car serial number").strip()
    if car:
        comps = finder.get_components(car)
        if comps is None:
            st.error(f"Car serial {car} not found")
        else:
            st.subheader(f"Components for {car.upper()}")
            for comp in comps:
                serial = finder.component_serial(comp)
                st.write(f"{comp} - {serial}")

elif mode == MODE_EDIT:
    car = st.text_input("Enter car serial number to edit").strip()
    if car:
        comps = finder.get_components(car)
        if comps is None:
            st.error(f"Car serial {car} not found")
        else:
            comp = st.selectbox("Select component", comps)
            current = finder.component_serial(comp) or ""
            new_serial = st.text_input("Serial number", value=current).strip()
            if st.button("Update component serial"):
                finder.edit_component(comp, new_serial)
                err = finder.save()
                if err:
                    st.warning(f"GitHub sync failed: {err}")
                else:
                    st.success("Component updated")
            new_comp = st.text_input("New component name").strip()
            new_comp_serial = st.text_input("New component serial").strip()
            if st.button("Add component to car") and new_comp and new_comp_serial:
                finder.add_component_to_car(car, new_comp)
                finder.edit_component(new_comp, new_comp_serial)
                err = finder.save()
                if err:
                    st.warning(f"GitHub sync failed: {err}")
                else:
                    st.success("Component added")

elif mode == MODE_ADD:
    car = st.text_input("New car serial").strip()
    comps_text = st.text_area('Components and serials (one per line "component,serial")')
    if st.button("Add car") and car and comps_text:
        comp_list = []
        for line in comps_text.splitlines():
            if "," in line:
                name, serial = [p.strip() for p in line.split(",", 1)]
                comp_list.append(name)
                finder.edit_component(name, serial)
        if comp_list:
            finder.add_car(car, comp_list)
            err = finder.save()
            if err:
                st.warning(f"GitHub sync failed: {err}")
            else:
                st.success(f"Car {car} added")
        else:
            st.error("No valid components provided")

elif mode == MODE_DELETE:
    choice = st.radio("Delete target", ["Car", "Component from car"])
    if choice == "Car":
        with st.form("delete_car"):
            car = st.text_input("Car serial to delete").strip()
            confirm = st.checkbox("I confirm deletion")
            submitted = st.form_submit_button("Delete car")
            if submitted:
                if confirm:
                    if finder.delete_car(car):
                        err = finder.save()
                        if err:
                            st.warning(f"GitHub sync failed: {err}")
                        else:
                            st.success(f"Car {car} deleted")
                    else:
                        st.error("Car not found")
                else:
                    st.warning("Deletion not confirmed")
    else:
        with st.form("delete_component"):
            car = st.text_input("Car serial").strip()
            component = st.text_input("Component name to delete").strip()
            confirm = st.checkbox("I confirm deletion")
            submitted = st.form_submit_button("Delete component")
            if submitted:
                if confirm:
                    if finder.delete_component_from_car(car, component):
                        err = finder.save()
                        if err:
                            st.warning(f"GitHub sync failed: {err}")
                        else:
                            st.success("Component deleted")
                    else:
                        st.error("Car or component not found")
                else:
                    st.warning("Deletion not confirmed")
