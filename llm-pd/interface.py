import streamlit as st
import pandas as pd

from agent import query_agent, create_agent


def write_response(response_dict: dict):

     # Check if the response is a table.
    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)

    # Check if the response is an answer.
    if "answer" in response_dict:
        st.write(response_dict["answer"])

   
st.title("👨‍💻 Chat with your CSV")

st.write("Please upload your CSV file below.")

data = st.file_uploader("Upload a CSV")

query = st.text_area("Insert your query")

if st.button("Submit Query", type="primary"):
    # Create an agent from the CSV file.
    agent = create_agent(data)
    
    # Query the agent.
    response = query_agent(agent=agent, query=query)

    # Write the response to the Streamlit app.
    write_response(response)