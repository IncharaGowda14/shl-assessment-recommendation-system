import streamlit as st
from recommender import recommend_assessments

st.set_page_config(
    page_title="SHL Recommendation System",
    layout="wide"
)

st.title("SHL Assessment Recommendation System")

st.write(
    "Enter a job description or hiring query "
    "to get relevant SHL assessments."
)

query = st.text_area(
    "Enter Job Description or Hiring Query"
)

if st.button("Recommend Assessments"):

    if query.strip() == "":
        st.warning("Please enter a query.")
    else:

        results = recommend_assessments(query)

        st.subheader("Recommended Assessments")

        for item in results:

            with st.container():

                st.markdown(f"## {item['name']}")

                st.write(f"**Test Type:** {item['test_type']}")
                st.write(f"**Duration:** {item['duration']}")
                st.write(
                    f"**Remote Support:** "
                    f"{item['remote_support']}"
                )
                st.write(
                    f"**Adaptive Support:** "
                    f"{item['adaptive_support']}"
                )
                st.write(f"**Match Score:** {item['score']}")

                st.markdown(
                    f"[Open Assessment]({item['url']})"
                )

                st.divider()