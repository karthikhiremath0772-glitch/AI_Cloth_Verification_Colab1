import streamlit as st

st.set_page_config(page_title="AI Cloth Verification", layout="centered")

st.title("✅ AI Cloth Verification")
st.write("🎉 Streamlit app is running correctly!")

# Example workflow UI
st.subheader("Upload Cloth Image for Verification")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.success("Image uploaded successfully ✅")

st.subheader("Next Steps")
st.write("""
- Later, we will connect the **AI model** here.
- For now, you can upload an image and see it displayed.
""")
# Paste your full streamlit_app.py code here
