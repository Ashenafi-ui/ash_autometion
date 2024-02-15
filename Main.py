import pandas as pd
import streamlit as st 
#from streamlit import  streamlit_pandas as sp

from streamlit_option_menu import option_menu
#from Pages import Data_Summary
#from pages import Data_Header

import about, account, Data_Entry, Home, Your_Post
#from pages import Option_app
#st.set_page_config(
page_title=("💻 ESL_PTSS Operational & MMP Automation System!!!"),
initial_sidebar_state="expanded",
menu_items={
           'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"}
#)

class MultiApp:
   def __init__(self):
      self.apps = []
   def add_app(self, title, func):
      self.apps.append({
           "title": title,
           "function": func
      })
   
   def run():
      
      with st.sidebar:
         app = option_menu(
            menu_title='📟 PTSS Automation',
            options=['Home', 'account','about','Your_Post','Data_Entry'],
               icons=['house-file', 'person-circle', 'trophy-fill', 'chat-title','info-cercle-fill'],
                      #icons=['🏠','🙋🏾‍♂️🔑','👨🏾‍💻', '👑', '🚀', '📊'],
            menu_icon=':📟:',
            default_index=1,
             styles={
                    "container": {"Padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

      if app== 'Home':
         Home.app()
      if app== 'account':
         account.app()
      if app== 'about':
         about.app()
      if app== 'Your_Post':
         Your_Post.app()
      if app== 'Data_Entry':
         Data_Entry.app()
      #if app== 'Data_Header':
         #Data_Header.app()



   run()

      

          
   

     