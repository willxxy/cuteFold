from stmol import showmol
import streamlit as st
import pandas as pd
import numpy as np
import py3Dmol

st.title("cuteFold")
st.header("cuteFold is a 5 minute quiz that assesses personality traits and manifests the results into a unique profein structure.")
st.write("have fun!")
xyzview = py3Dmol.view(query='pdb:1A2C')
xyzview.setStyle({'cartoon': {'color': 'spectrum'}})
showmol(xyzview, height=500, width=500)
showmol(render_pdb_resn(viewer=render_pdb(id='1A2C'), resn_lst=['ALA', ]))
name = st.text_input("Name...", value="", max_chars=15)
