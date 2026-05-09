import streamlit as st
import requests

st.title("SHL Assessment Recommendation System")

query = st.text_area(
    "Enter Job Description or Hiring Query"
)

if st.button("Recommend Assessments"):

    response = requests.post(
        "http://127.0.0.1:8000/recommend",
        json={"query": query}
    )

    data = response.json()

    st.subheader("Recommended Assessments")

    for item in data["recommendations"]:

        st.markdown(f"### {item['name']}")

        st.write(f"Type: {item['test_type']}")
        st.write(f"Duration: {item['duration']}")
        st.write(f"Remote Support: {item['remote_support']}")
        st.write(f"Adaptive Support: {item['adaptive_support']}")
        st.write(f"Score: {round(item['score'], 3)}")

        st.markdown(f"[Assessment Link]({item['url']})")