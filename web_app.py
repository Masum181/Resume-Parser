import streamlit as st
import pymupdf
import resume
import docx2txt
import re
import csv
import os

def read_csv(file_path):
    try:
        file = open(file_path, 'r')
        file.close()
    except:
        add_csv_file("",file_path, mode='w')


st.set_page_config(
    page_title='Resume Parser',
    layout='wide'
)

def add_csv_file(data, file_path, mode='a'):
    header = ["Name", "Skill", "Email", "Phone Number", "Education", "Experience", "Related URL", "File Name"]
    
    with open(file_path, mode=mode, newline="") as f:
        writer = csv.writer(f)
        if mode=='w':
            writer.writerow(header)
        else:
            writer.writerow(data)

def create_text_format(texts):
    
    new_data = []
    for data in texts:
        new_data.append("**`{}`**".format(data))
    return new_data

def text_representation(text, name_text, file_name):
    nlp_text = resume.nlp(text)
    if  name_text == "":
        name_text = nlp_text
    else:
        name_text = resume.nlp(name_text)
    name = resume.get_name(name_text)
    
    skills = resume.get_skills(nlp_text)
    
    email = resume.get_email_address(nlp_text)
    phone_number = resume.get_mobile_num(nlp_text)
    experience = resume.get_experience(nlp_text)
    url = resume.get_url(nlp_text)
    education = resume.extracting_education(nlp_text)

    ## adding to csv file "Name", "Skill", "Email", "Phone Number", "Education", "Experience", "Related URL", "File Name"
    add_csv_file([",".join(name), ",".join(skills), ",".join(email), ",".join(phone_number), ",".join(education),",".join(experience), ",".join(url), file_name], "resume_output.csv")

    # writing data for web app
    st.write("### Skill: ")
    st.markdown(" | ".join(create_text_format(skills)))

    st.write("### Name: ")
    st.markdown(" | ".join(create_text_format(name)))

    st.write("### Email: ")
    st.markdown(" | ".join(create_text_format(email)))

    st.write("### Phone Number: ")
    st.markdown(" | ".join(create_text_format(phone_number)))

    st.write("### Experience: ")
    st.markdown(" | ".join(create_text_format(experience)))

    st.write("### Education: ")
    st.markdown(" | ".join(create_text_format(education)))

    st.write("### Related Url: ")
    st.markdown(" | ".join(create_text_format(url)))

if __name__ == "__main__":
    read_csv("resume_output.csv")
    uploaded_file = st.file_uploader("### Choose a file")
    if uploaded_file is not None:
        if 'pdf' in uploaded_file.name:
            # st.write("uploaded file successfully")
            # print(uploaded_file.type)
            # print(uploaded_file.name)

            # print(type(uploaded_file.name))
            doc = pymupdf.open(uploaded_file)
            # st.write(doc.page_count)
            # st.write(doc.metadata)

            first_page_doc = doc.load_page(0).get_text()
            first_page_doc = re.sub(r"('|’)", "", first_page_doc)

            
            text = ""
            for i in range(doc.page_count):
                text += doc.load_page(i).get_text()
            text = re.sub(r"('|’)", "", text)
            

            text_representation(text, first_page_doc, uploaded_file.name)
            
        if 'docx' in uploaded_file.name:
            text = docx2txt.process(uploaded_file)
            text = re.sub(r"('|’)", "", text)
            text_representation(text, '', uploaded_file.name)

    

        

    


    

