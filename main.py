import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


##Function to get response from LLAMA 2 MODEL

def getLLamaresponse(input_text,no_words,blog_style):
    ##LLAMA2 Response
    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        max_new_tokens=256,
        temperature=0.01
    )
    ##prompt template
    template = f"""
    Write a blog {blog_style} job profile for a topic {input_text}
    within {no_words} words.
    """

    prompt=PromptTemplate(input_variables=['blog_style','text','n_words'],template=template)
    ##generate the response from LLAMA

    response=llm(prompt.format(blog_style=blog_style,text=input_text,n_words=no_words))
    print(response)
    return response
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed'
                   )
st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter your blog Topic")


## Creating two more columns for additional 2 fields


col1,col2=st.columns([5,5])


with col1:
    no_words=st.text_input("No of words")


with col2:
    blog_style=st.selectbox('Writinng the blog for',('Researchers','Data Scientist','Common People'),index=0)
submit=st.button("Generate")



##Final Response

if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))
