import streamlit as st
from streamlit_extras.bottom_container import bottom
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain_mistralai.chat_models import ChatMistralAI
import os
import urllib.parse
import streamlit.components.v1 as components


def init_session():
    # Session State initializations
    if 'key' not in st.session_state:
        st.session_state.key = 0

def share_buttons(content):
    # LinkedIn & X (Twitter) share button
    linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote('https://www.linkedin.com/')}&title={urllib.parse.quote('Hi👋🏾')}&summary={urllib.parse.quote(content)}"
    twitter_url = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(content)}"
    
    st.write(f"[![Share on LinkedIn](https://img.shields.io/badge/Share%20on-LinkedIn-blue?style=plastic)]({linkedin_url}) "+f" [![Share on X](https://img.shields.io/badge/Share%20on-X-black?style=plastic)]({twitter_url}) ")


def main():
    #Main Header  contents
    st.set_page_config(page_title="Bodhi", page_icon="🌳")
    init_session() #Initialize session

    # Add tabs to the sidebar
    st.sidebar.title('Welcome 👋🏾')
    st.sidebar.header('Buildspace - Project Bodhi')
    st.sidebar.write('[![Twitter](https://img.shields.io/badge/Follow-black?style=plastic&logo=X)](https://x.com/_the_real_ng_/) [![Instagram](https://img.shields.io/badge/Connect-pink?logo=instagram&style=plastic)](https://www.instagram.com/nikki_builds/) [![Linkedin](https://img.shields.io/badge/Connect-blue?style=plastic&logo=Linkedin)](https://www.linkedin.com/in/nikhil-gnanavel/)')
    st.sidebar.write(' ')
    st.sidebar.image("assets/face logo.jpg")
    st.sidebar.header("About:")
    st.sidebar.code('''Heyo 😁,
Nikhil here. 
Thanks for taking time to check this out.
If you like this project and want to see some more cool GenAI projects, 
hit me up through the feedback page below 👇🏾''')

    tabs = ["Bodhi : Content-to-template generator", "Feedback"]
    tab = st.sidebar.selectbox('', options=tabs,label_visibility="collapsed")  

    if tab == 'Bodhi : Content-to-template generator':
        app_page()
    elif tab == 'Feedback':
        feedback()    

def app_page():
    st.header('Buildspace - Project Bodhi')
    st.write('Drop your content and template in this window to generate an automatic post! 🤖📟')
    tab1, tab2 = st.tabs(["Content", "Template"])

    with tab1: 
        content_inp = st.text_area("Enter your content",key=1)
        st.write(f"Character count: {len(content_inp)}")

    with tab2:
        template_inp = st.text_area("Enter your template",key=2)
        st.write(f"Character count: {len(template_inp)}")
    
    models = ["gpt-4","mistral-large-latest"]
    option = st.selectbox("Select your model:",models)

    if st.button("Generate Content"):
        
        with st.spinner(f"Generating content from {option}..."):
            if option == "gpt-4":
                output_content = model_gpt(content_inp, template_inp)
                                                
            elif option == "mistral-large-latest":
                output_content = model_Mistral(content_inp, template_inp)
                #output_content = "This is MistralAI"
            else:
                output_content = "Error! Error! Try a different model. Report error via DM or Github"
            st.session_state.generated_content = output_content
        
        
        st.subheader("Generated Content:")
        st.write("Here is your output 👇🏾 Share responsibly ❤")
        st.code(output_content, language="markdown")
        
        st.subheader("Share your generated content:")
        share_buttons(output_content)
            
    
def feedback():
    # Replace 'YOUR_TALLY_FORM_URL' with the actual URL of your Tally form
    tally_form_url = """
    <iframe data-tally-src="https://tally.so/embed/w2rdMV?transparentBackground=1&dynamicHeight=1" loading="lazy" width="100%" height="2004" frameborder="0" marginheight="0" marginwidth="0" title="Progress Update"></iframe><script>var d=document,w="https://tally.so/widgets/embed.js",v=function(){"undefined"!=typeof Tally?Tally.loadEmbeds():d.querySelectorAll("iframe[data-tally-src]:not([src])").forEach((function(e){e.src=e.dataset.tallySrc}))};if("undefined"!=typeof Tally)v();else if(d.querySelector('script[src="'+w+'"]')==null){var s=d.createElement("script");s.src=w,s.onload=v,s.onerror=v,d.body.appendChild(s);}</script>
    """
    # Embed the Tally form using an iframe
    components.html(tally_form_url,height=2200,width = 800, scrolling = True)

def model_gpt(user_content,user_template):
    # Set up the language model
    chat_model = ChatOpenAI(model="gpt-4",temperature=1,max_tokens=100, top_p=1, frequency_penalty=0,presence_penalty=0)
    
    # Create the chat prompt
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=("Make my content in form of the template. Do not perform any other action.")),
        HumanMessagePromptTemplate.from_template("Content = \"{content_model}\" \ntemplate = \"{template_model}\""),
    ])

    # Format the messages with user input
    messages = prompt.format_messages(
        content_model=user_content,
        template_model=user_template
    )

    # Generate the response
    response = chat_model(messages)

    return response.content

def model_Mistral(user_content,user_template):
    # Set up the language model
    chat_model = ChatMistralAI(model="mistral-large-latest",temperature=1,max_tokens=300, top_p=1, frequency_penalty=0,presence_penalty=0)
    
    # Create the chat prompt
    prompt = ChatPromptTemplate.from_messages([
        SystemMessage(content=("Make my content in form of the template. Do not perform any other action.")),
        HumanMessagePromptTemplate.from_template("Content = \"{content_model}\" \ntemplate = \"{template_model}\""),
    ])

    # Format the messages with user input
    messages = prompt.format_messages(
        content_model=user_content,
        template_model=user_template
    )

    # Generate the response
    response = chat_model(messages)

    return response.content

if __name__ == "__main__":
    # Access secrets from the secrets.toml file
    os.environ["OPENAI_API_KEY"] = st.secrets["api_keys"]["OPENAI_API_KEY"]
    os.environ["MISTRAL_API_KEY"] = st.secrets["api_keys"]["MISTRAL_API_KEY"]
    main()
