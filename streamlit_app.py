import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

st.set_page_config(layout="wide")


st.title("🌍 Real World Summary Graph 🌐")
st.write(
    "Click on the nodes to know the information and the challenges."
)


# Sample Data
elements = {
    # "nodes": [
    #     {"data": {"id": 1, "label": "PERSON", "name": "Streamlit"}},
    #     {"data": {"id": 2, "label": "PERSON", "name": "Hello"}},
    #     {"data": {"id": 3, "label": "PERSON", "name": "World"}},
    #     {"data": {"id": 4, "label": "POST", "content": "x"}},
    #     {"data": {"id": 5, "label": "POST", "content": "y"}},
    # ],
    # "edges": [
    #     {"data": {"id": 6, "label": "FOLLOWS", "source": 1, "target": 2}},
    #     {"data": {"id": 7, "label": "FOLLOWS", "source": 2, "target": 3}},
    #     {"data": {"id": 8, "label": "POSTED", "source": 3, "target": 4}},
    #     {"data": {"id": 9, "label": "POSTED", "source": 1, "target": 5}},
    #     {"data": {"id": 10, "label": "QUOTES", "source": 5, "target": 4}},
    # ],
   
  "nodes": [
    {"data":{ "id": 1, "label":"CORE", "name": "data_harmonized" }},
    {"data":{ "id": 2, "label": "HEALTH", "name":"patients" }},
    {"data":{ "id": 3, "label":"CURES", "name": "physicians" }},
    {"data":{ "id": 4, "label":"PREVENTION", "name": "institutions" }},
    {"data":{ "id": 5, "label":"PREVENTION", "name": "trial_registries" }},
    {"data":{ "id": 6, "label":"CURES", "name": "pharmacy" }},
    {"data":{ "id": 7, "label":"FINANCIAL", "name": "countries" }},
    {"data":{ "id": 8, "label":"FINANCIAL", "name": "claims" }},
    {"data":{ "id": 9, "label":"HEALTH", "name": "labbiomarkers" }}
  ],
  "links": [
    {"data":{ "id": 10,  "source": 1, "target": 2, "label": "INTERACT_WITH" }},
    {"data":{  "id": 11, "source": 1, "target": 3, "label": "INTERACT_WITH" }},
    {"data":{  "id": 12, "source": 1, "target": 4, "label": "INTERACT_WITH" }},
    {"data":{  "id": 13, "source": 1, "target": 5, "label": "INTERACT_WITH" }},
    {"data":{  "id": 14, "source": 2, "target": 6, "label": "INTERACT_WITH" }},
    {"data":{  "id": 15, "source": 3, "target": 6, "label": "INTERACT_WITH" }},
    {"data":{  "id": 16, "source": 3, "target": 7, "label": "INTERACT_WITH" }},
    {"data":{ "id": 17,  "source": 5, "target": 7, "label": "INTERACT_WITH" }},
    {"data":{ "id": 18,  "source": 5, "target": 8, "label": "INTERACT_WITH" }},
    {"data":{ "id": 19,  "source": 4, "target": 8, "label": "INTERACT_WITH" }},
    {"data":{ "id": 20,  "source": 4, "target": 9, "label": "INTERACT_WITH" }},
    {"data":{ "id": 21,  "source": 2, "target": 9, "label": "INTERACT_WITH" }}
  ]



}

# Style node & edge groups
node_styles = [
    NodeStyle("CORE", "#FF7F3E", "name", "core"),
    NodeStyle("HEALTH", "#2A629A", "name", "health"),
    NodeStyle("CURES", "#2A079A", "name", "cures"),
    NodeStyle("PREVENTION", "#2A620A", "name", "prevention"),
    NodeStyle("FINANCIAL", "#1A629A", "name", "financial")
]

edge_styles = [
    EdgeStyle("INTERACT_WITH", caption='label', directed=True),
    # EdgeStyle("INTERACT_WITH", caption='label', directed=True),
    # EdgeStyle("INTERACT_WITH", caption='label', directed=True),
]

# Render the component
st.markdown("### st-link-analysis: Example")
st_link_analysis(elements, "cose", node_styles, edge_styles)