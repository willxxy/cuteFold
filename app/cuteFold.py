from stmol import showmol
import streamlit as st
import pandas as pd
import numpy as np
import py3Dmol


st.title("cuteFold")
xyzview = py3Dmol.view(query='pdb:1A2C')
xyzview.setStyle({'cartoon': {'color': 'spectrum'}})
showmol(xyzview, height=500, width=800)
