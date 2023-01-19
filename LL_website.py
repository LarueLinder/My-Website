import streamlit as st
import requests
from streamlit_lottie import st_lottie

#customize the emoji later under page icon
st.set_page_config(page_title="My Webpage", page_icon=":tada;",layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local css 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>, unsafe_allow_html = True")

#local_css("style/style.css")

#load assets 
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_XMTduDVODZ.json")

##  -- header section --
with st.container():
    #customize the wave emjoi to something else later
    st.subheader("HI, I am Larue Linder 💻")
    st.title("I am a Computer Science and Financial Economics Student") # at Johns Hopkins University.")
    st.write("Education: Johns Hopkins University")
    #here do the languages proficient in 
    st.write("Languages: Java, Python, C++, R")
    #then do a dropdowon "more about me" and mention student athlete and other passions
    #have a link to my linkedin and github
    #st.write("[LinkedIn >](www.linkedin.com/in/larue-linder)")
    st.write("[Github >](https://github.com/LarueLinder)")

# --- What I do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("What I do")
        #st.write("##")
        st.write (
            """
            I am a student athlete at Johns Hopkins graduating in 2026
              - Member of the Football Team :football:
              - Member of Association For Computing Machinery
              - Passionate in Software Development, Finance, and the Intersection of Finance and Tech
              - Proven Leader

            """
        )
    
    with right_column:
        st_lottie(lottie_coding, height=200, key="coding")

# -- projects --

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    st.write(
        """
        **NFL Receiving Leaders Analysis (Python)**  
            - Link: https://laruelinder-footballproject-football-analysis-ad3w59.streamlit.app/
            
            - Used streamlit, base64, numpy, pandas, matplotlib and seaborn
            - Scrapes pro-football-focus to get the NFL leaders in receiving
            - Interactive website that presents data to the user in a table
            - Allows the user to sort by year, team, and position from the years 1990 to 2022
            - Includes an intercorrelation heatmap for users to see the correlation between stats


        **Car Data Analysis (Java)**  
            - Link: https://github.com/LarueLinder/car_data_analysis
            
            - Parses a .csv file with 2500 entries  in order to load and organize the data we care about into arrays
            - Presents the user with a menu-driven interface that allows the user to perform several data-analysis options on the loaded data
            - Allows the user to search the market of used cars based on the brand of the car, price of the car, and miles on the car
            - Allows the user to find the average price of cars between their specified years and mileage range
            - Prints to the user the best-value car based on budget, car brand, and mileage thresholds
        
        **Crazy Eights (Java)**  
            - Link: https://github.com/LarueLinder/CrazyEights
            
            - Used OOP principles to implement a fully functioning Crazy Eights card game
            - Allows for user-on-user play, machine-on-machine play, and user-on-machine play
            - Implements machine logic allowing the computer to play logical moves against a user

        
        """
    )
    
    ##ogranice my projects and stuff here 
    #maybe put github again here
    #see if theres a way to display a pdf on website -- or copy paste resume

# -- contact -- 
st.write("---")
st.header("Get In Touch With Me!")
st.write("Email: laruelinder77@gmail.com ")
st.write("LinkedIn: www.linkedin.com/in/larue-linder")
st.write("Twitter: LarueLinder_")

##maybe add linkedin see where it  goes best
