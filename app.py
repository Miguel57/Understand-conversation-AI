import streamlit as st
import f_gpt3_secrets as f_gpt3


# define parameters
LIST_MODE = ["TITLE" ,"SUMMARY", "TAGS", "SENTIMENT"]
# Select Engine ---> Ada, Babbage, Curie, Davinci
ENGINE = "Davinci"


Name_app = "Understand conversation"
REPO = "https://github.com/juan-csv/Understand-conversation-AI"

description_app = f"[{Name_app}]({REPO}) "\
                    f"structures data in title, summary, tags, sentiment "\
                    f"given a fragment of a conversation using GPT3. "

EXAMPLE = "Agent: For calling customer service. My name is Vanessa, how may help you. Client: I was calling to order place and white. Agent: We happy to send out a replacement card out for you. Agent: Your 16, digit card number. Client: I dont know the Cardinals. Agent: Thank you verify your first and last name please. Client: Patricia Covington. Agent: How you spell your last name? Client: C O V I N G T O and. Agent: And you said your first name. Client: Letricia. Agent: L a T. Client: R I C I. Agent: Z. Agent: It's not pulling up anything C O N C I N G T O. Client: Know C O V as in Victor, Agent: S when? Client: I N G T O N E. Agent: I put the extra letter and I was wondering what I was doing wrong key verify your data birth for the reserve anson. Client: Uh huh made since 1995. Agent: Thing with this card last owner damage. Client: It was last. Agent: Thinking to verify your address we like a new cards remote out to. Client: 1918 Arlington avenue saint, Louis Missouri 63112 apartment a. Agent: You. Okay. Thank you Mrs. Could send him before? I cant see your car. I need to inform you that this call will be personally cancel excuse me. It will take three to five business days for your new card to arrive in the mail would you like him for counselors car now. Client: Yes maam. Agent: Thank you your card is now been council your my name is Alison team will be transferred to your new card you have 121 instead of benefits available and a dollar and 0.38 and cash benefits. Client: Okay. Thank you. I have you. Agent: Or anything else? I can assist you with today. Client: Know you have a good day. Agent: I was coming soon. Thank you for calling customer service and have a nice day. Client: Thank you, bye, bye. Thank you bye."
# Add \n in any "."
EXAMPLE = EXAMPLE.replace("Agent","\nAgent")
EXAMPLE = EXAMPLE.replace("Client","\nClient")[1:]



st.set_page_config(
    page_title=Name_app,
    layout="wide",
    initial_sidebar_state="expanded"
)



#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
# sidebar information
st.sidebar.markdown("<h3 style='text-align: center; font-size:56px;'<p>&#129302;</p></h3>", unsafe_allow_html=True)
st.sidebar.markdown("-----------------------------------")
st.sidebar.markdown(description_app)
st.sidebar.markdown("Made with 💙 by [juan-csv](https://github.com/juan-csv)")

#CONTACT
########
st.sidebar.markdown("-----------------------------------")
expander = st.sidebar.expander('Contact', expanded=True)
expander.write("I'd love your feedback :smiley: Want to collaborate? Develop a project? Find me on [LinkedIn] (https://www.linkedin.com/in/juan-camilo-lopez-montes-125875105/)")
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------

# add title
st.title(Name_app)

# divide interface in two columns
col1, col2 = st.columns([6,4])

with col1:
    # create input text
    input_text = st.text_area("Input text:", value=EXAMPLE, height=500)
    # create button
    process = st.button("Process")

with col2:
    if process:
        head_text = st.text("Processing...")

        # get result in json format
        res = dict()
        res["ENGINE"] = ENGINE
        total_price = 0
        Res = ""
        for MODE in LIST_MODE:
            response, price = f_gpt3.get_ingerence_GPT3(input_text, MODE, ENGINE)
            Res += f"{MODE} : {response} \n\n"
            res[MODE] = response
            total_price += price
        res["PRICE"] = total_price

        st.markdown(f"**TITLE** : {res['TITLE']}", unsafe_allow_html=True)
        st.markdown(f"**SUMMARY** : {res['SUMMARY']}", unsafe_allow_html=True)
        st.markdown(f"**TAGS** : {res['TAGS']}", unsafe_allow_html=True)
        st.markdown(f"**SENTIMENT** : {res['SENTIMENT']}", unsafe_allow_html=True)
        # show result
        st.success(Res)
        head_text.text("Done!!!")