import streamlit as st
from PIL import Image,ImageFilter
st.title("🌈Image Filter ")

Uploaded_img=st.file_uploader("Upload image", type=['jpg', 'png', 'jpeg']) 

if Uploaded_img:
    filter=st.selectbox("choose filter",["Original","Blur","Grayscale","Sharpen","Contour"])
    
    
    img=Image.open(Uploaded_img)
    if filter=="Blur":
        img = img.filter(ImageFilter.BLUR)
    elif filter =="Grayscale":
        img = img.convert("L")
    elif filter =="Sharpen":
        img = img.filter(ImageFilter.SHARPEN)
    elif filter =="Contour":
        img = img.filter(ImageFilter.CONTOUR)
      
    st.image(img)

    import io

    buf = io.BytesIO()
    img.save(buf, format="PNG")


    st.download_button(
      label="⬇️ Download Image",
      data=buf.getvalue(),
      file_name="filtered_image.png",
      mime="image/png"
     )



