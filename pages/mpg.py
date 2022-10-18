import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import plotly.express as px

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# MPG 🚗")
st.sidebar.markdown("# MPG 🚗")

st.write("""
### 자동차 연비
""")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"
# data = pd.read_csv(url)
# data

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    # def lowercase(x): return str(x).lower()
    # data.rename(lowercase, axis="columns", inplace=True)
    return data

data_load_state = st.text("Loding data...")
data = load_data(url)
data_load_state.text("Done! (using st.cache)")


st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(data.model_year.min(),data.model_year.max())))
   )

# Sidebar - origin
sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   data = data[data.model_year == selected_year]

if len(selected_origin) > 0:
   data = data[data.origin.isin(selected_origin)]

st.dataframe(data)

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])

fig, ax = plt.subplots(figsize=(10, 3))
sns.countplot(data=data, x="origin").set_title("지역별 자동차 연비")
st.pyplot(fig)

pxh = px.histogram(data, x="origin", title="지역별 자동차 연비 데이터 수")
st.plotly_chart(pxh)

pxh1 = px.scatter(data, x="mpg", y="horsepower", color="origin", title="지역별 연비와 마력의 상관관계")
st.plotly_chart(pxh1)
