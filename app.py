import streamlit as st
from crew import run_crew
from image_generator import generate_image

st.title("Multimodal Education Creator")

topic = st.text_input("Enter Educational Topic")

if st.button("Generate"):
    if topic:
        with st.spinner("Generating content..."):
            result = run_crew(topic)

            image_prompt = f"Educational diagram of {topic}, labeled diagram, educational illustration"
            image = generate_image(image_prompt)

        st.write("-----------------------------")
        st.subheader("Educational Content")
        st.write(result.raw)

        st.write("-----------------------------")
        st.subheader("Educational Diagram")

        if image:
            st.image(image)
        else:
            st.write("Image not generated")