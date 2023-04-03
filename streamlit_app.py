import openai as ai
import json
import streamlit as st


[my_cool_secrets]
things_i_like = ["Cognavi", "AI"]
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

print("** Loading API Key")
ai.api_key = "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"

# st.title("")
st.markdown("# Cognavi - Job Description Generator")
st.sidebar.markdown("# Job Description Generator")

with st.sidebar:
    model_used = st.selectbox(
     'GPT-3 Model',
    #  ('DaVinci', 'Curie', 'Babbage', 'Ada'))
    ('text-davinci-003', 'text-curie-001', 'text-babbage-001', 'text-ada-001'))

    # tone_used = st.selectbox('Tone',('Casual','Friendly','Professional','Formal'))

    if model_used == 'text-davinci-003':
        st.markdown("""[Davinci](https://beta.openai.com/docs/models/davinci) is the most capable model family and can perform any task the other 
        models can perform and often with less instruction. For applications requiring a lot of 
        understanding of the content, like summarization for a specific audience and creative content
         generation, Davinci is going to produce the best results. These increased 
         capabilities require more compute resources, so Davinci costs more per API call and is not as fast as the other models.
        """)

    elif model_used == 'text-curie-001':
        st.markdown("""[Curie](https://beta.openai.com/docs/models/curie) is extremely powerful, yet very fast. While Davinci is stronger when it 
        comes to analyzing complicated text, Curie is quite capable for many nuanced tasks like sentiment 
        classification and summarization. Curie is also quite good at answering questions and performing 
        Q&A and as a general service chatbot.
        """)
    elif model_used == 'text-babbage-001':
        st.markdown("""[Babbage](https://beta.openai.com/docs/models/babbage) can perform straightforward tasks like simple classification. It’s also quite 
        capable when it comes to Semantic Search ranking how well documents match up with search queries.
        """)
    else:
        st.markdown("""[Ada](https://beta.openai.com/docs/models/ada) is usually the fastest model and can perform tasks like parsing text, address 
        correction and certain kinds of classification tasks that don’t require too much nuance. 
        da’s performance can often be improved by providing more context.
        """)
    st.markdown("**Note:** Model descriptions are taken from the [OpenAI](https://beta.openai.com/docs) website")

    max_tokens = st.text_input("Maximum number of tokens:", "1949")
    st.markdown("**Important Note:** Unless the model you're using is Davinci, then please keep the total max num of tokens < 1950 to keep the model from breaking. If you're using Davinci, please keep max tokens < 3000.")

    # st.subheader("Additional Toggles:")
    # st.write("Only change these if you want to add specific parameter information to the model!")
    # temperature = st.text_input("Temperature: ", "0.99")
    # top_p = st.text_input("Top P: ", "1")


with st.form(key='my_form_to_submit'):
    role = st.text_input("Which role are you creating JD for? ", "Data Scientist")
    exp = st.text_input("Having Experience ? ", "3+ years")
    skills =  st.text_input("Having Skills ", "Python, Statistics, Analytics, NLP")
    industry_name = st.text_input("Industry Name: ", "Information Technology")
    numwords =  st.text_input("Number of words in JD ", "500")
    # tone = st.text_input("With Tone of  ", "Formal")
    tone =  st.selectbox('Tone', ("Appreciative","Assertive","Awestruck","Candid",'Casual',"Compassionate","Convincing","Critical","Enthusiastic", 'Friendly', "Formal","Informative","Inspirational","Passionate",'Professional', 'Thoughtful','Urgent'))
    submit_button = st.form_submit_button(label='Submit')

prompt = ("Write a job description for " + role + " role " + " having experience of " + exp + " with skill sets of "+ skills + " in the " + industry_name +  " industry " + " with word count of  " + numwords + " and tone " + tone)
print("###########", prompt)
if submit_button:

    response = ai.Completion.create(
        model=model_used,
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1
        # frequency_penalty=0,
        # presence_penalty=0
    )

    text = response['choices'][0]['text']
    # print("Prompt:", prompt)
    # print("Response:", text)

    st.subheader("Job Description Prompt")
    st.write(prompt)
    st.subheader("Auto-Generated Job Description")
    st.write(text)
    st.download_button(label='Download Job Description', file_name='Job_Description.txt', data=text)

    with open('Job_Description.txt', 'a') as f:
        f.write(text)
