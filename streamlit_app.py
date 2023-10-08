
import streamlit as st
import plotly.express as px

def main_page():
    st.title("This is the title of the page")
    st.header("This is a header")
    st.subheader("This is a sub_header")
    st.markdown("This is a normal text")
    st.text("This is a normal text")
    st.code('names = list([\'Ahmed\', \'Mohamed\', \'Omar\'])')
    st.latex('y = x^2 + 2x + 3')
    
def second_page():
    st.image("cat.JPG", caption="This is a cat", width=300)
    
def third_page():
    st.checkbox("This is checkbox")
    st.radio("This is radio button", ['Choose A', 'Choose B', 'Choose C'])
    st.button("This is a submit button")
    st.selectbox("Choose your country", ['Egypt', 'USA', 'KSA', 'Dubi', 'Spain', 'Canda'])
    st.multiselect("Choose your favorite", ['Apple', 'Banana', 'Orange'])
    st.slider("Choose Range of income", 0, 5000)
    st.select_slider("What is quality of the sessions", ['Bad', 'Normal', 'Good', "Very Good", "Excellent"])
    
def fourth_page():
    df = px.data.tips()
    fig = px.bar(df, x='sex', y='total_bill', color='time', barmode='group', title='Summation of total bills across gender')
    st.plotly_chart(fig)
    
pages = {
    'الصفحة الرئيسية':main_page,
    'الصفحة التانية':second_page,
    'الصفحة الثالثة':third_page,
    'الصفحة الرابعة':fourth_page
}

page_no = st.sidebar.selectbox("Choose the page", pages.keys())
pages[page_no]()
