import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
warnings.filterwarnings("ignore")
from PIL import Image
import altair as alt





#st.set_page_config(layout="wide")
image = Image.open('market.jpg')

st.image(image, caption='Market by google images')

supermar = pd.read_csv(r'/Users/jaimesastrecrespo/DAFT_1022/module_2/Project_Week_5/supermar_clean2.csv')
supermar.head()

#cleaning done in script try_project.ipynb, imported the clean data

########################################################

######### STREAMLIT #######

colors = ["#14171A"]
sns.set_palette(sns.color_palette(colors))

#sns.cubehelix_palette(start=2, rot=0, dark=0, light=.95, reverse=True, as_cmap=True)
# st.set_page_config(layout="wide")

st.markdown("# Supermarket Sales Analysis ")   ## Main Title
expander_bar = st.expander("About this project")
expander_bar.markdown("""
* This is a sales analysis from the supermarkets in Naypyitaw, Yangon and Mandalay.
    * We will see:
        * Correlation matrix of our dataset.
        * Where are our target cities of this dashboard.
        * How are the ratings and what can affect the ratings of the customers.
        * Differences between sales accross City, payment methods, and gender.
        * Customer behaviour showing per days.
        * Differences in product line by Male/Female.
        * Finding the product line which generates more income.
        * Looking for the hour of the day when is the busiest moment.
        * Monthly trend.
        * Full dynamic chart.
* **Python libraries:** pandas, streamlit, numpy, matplotlib, seaborn, warnings, altair and Image.
""")


st.write('---')



result2 = st.button("Click here to see the correlation matrix to know more about the variables ")
st.write(result2)

if result2: 
    
    st.markdown("### Correlation ")   ## Main Title
    fig, ax = plt.subplots()
    sns.heatmap(supermar.corr(), ax=ax)
    st.write(fig)


result0 = st.button("Click here to see where are our target cities ")

st.write(result0)

if result0: 
    st.map(supermar, zoom = 5)
### Fig 1: Distribution of Rating with button

st.markdown(' ### Press the button to see the distribution of rating')

result = st.button("Click here ")

st.write(result)

if result: 

    fig = plt.figure()
    sns.distplot(supermar['Rating'])
    plt.axvline(x=np.mean(supermar['Rating']), c='red', ls='--', label='mean')
    plt.axvline(x=np.percentile(supermar['Rating'],25),c='green', ls='--', label = '25th percentile:Q1')
    plt.axvline(x=np.percentile(supermar['Rating'],75),c='orange', ls='--',label = '75th percentile:Q3' )
    plt.legend()
    st.pyplot(fig)
    flag = True

else:
    st.write("Come on, click please")
    flag = False

st.write('---')
    ### Fig 2: Does Total and quantity affect the ratings that the customers provide? with slectbox and if statement

st.markdown("### Does Total and quantity affect the ratings that the customers provide?")   ## Main Title

option = st.selectbox(
    'Choose what you want to see',
    ('total', 'quantity'))

if option == 'total':
    fig2 = plt.figure()
    sns.regplot(x="Rating",
            y="total", 
            data=supermar)
    st.pyplot(fig2)

elif option == 'quantity':
    fig2 = plt.figure()
    sns.regplot(x="Rating",
            y="quantity", 
            data=supermar)
    st.pyplot(fig2)

st.write('---')
### Fig 3 : Is there any difference in aggregate sales across City, etc? with slectbox and if statement

st.markdown("### Differences in aggregate sales accross City, Payment method and gender ")   ## Main Title

option = st.selectbox(
    'Choose what you want to see',
    ('city', 'payment', 'gender'))

if option == 'city':
    fig3 = plt.figure()
    sns.countplot(supermar['city'])
    supermar['city'].value_counts()
    st.pyplot(fig3)
    

elif option == 'payment':
    fig3 = plt.figure()
    sns.countplot(supermar['payment'])
    supermar['payment'].value_counts()
    st.pyplot(fig3)
    
elif option == 'gender':
    fig3 = plt.figure()
    sns.countplot(supermar['gender'])
    supermar['gender'].value_counts()
    st.pyplot(fig3)


st.write('You selected:', option)

  

st.write('---')  



######### 

st.sidebar.write("### Hello 😀!")
st.sidebar.write("You can set up different display options here below")
st.sidebar.write("")
st.sidebar.write("##### Please, first go through the main screen. You'll be asked to use the side bar at some point.")  



### Sidedbar days selection
unique_day = supermar.day_name.unique()
selected_day = st.sidebar.multiselect("Select one or more options:",unique_day,unique_day)

all_options1 = st.sidebar.checkbox("Select all days")

if all_options1:
    selected_day = unique_day



### Sidedbar month selection
unique_month = supermar.month.unique()
selected_month = st.sidebar.multiselect('month', unique_month,unique_month)

all_options2 = st.sidebar.checkbox("Select all months ")

if all_options2:
    selected_month = unique_month

# Sidebar - gender selection
unique_gen = supermar.gender.unique()
selected_gen = st.sidebar.multiselect('gender', unique_gen,unique_gen)

all_options3 = st.sidebar.checkbox("Select both genders ")

if all_options3:
    selected_gen = unique_gen


# Sidebar - product line selection
unique_prod = supermar.product_line.unique()
select_line = st.sidebar.multiselect('product_line', unique_prod,unique_prod)

all_options4 = st.sidebar.checkbox("Select all lines of product ")

if all_options4:
    select_line = unique_prod


# Sidebar - city selection
unique_city = supermar.city.unique()
selected_city = st.sidebar.multiselect('city', unique_city,unique_city)

all_options5 = st.sidebar.checkbox("Select all cities ")

if all_options5:
    selected_city = unique_city

# Sidebar - customer type selection
unique_customer = supermar.customer_type.unique()
selected_customer = st.sidebar.multiselect('customer_type', unique_customer,unique_customer)

all_options6 = st.sidebar.checkbox("Select all type of customer ")

if all_options6:
    selected_customer = unique_customer


df2 = supermar.loc[(supermar['day_name'].isin(selected_day)) &(supermar['gender'].isin(selected_gen))
                &(supermar['product_line'].isin(select_line))& (supermar['city'].isin(selected_city)) 
                & (supermar['month'].isin(selected_month))& (supermar['customer_type'].isin(selected_customer))]




st.markdown("### Customers behaviour showing the total amount of money spend per day")   ## Main Title
st.markdown("##### Please, select options in your sidebar to display what you want")   




st.bar_chart(df2, x="day_name", y="total")


st.write('---')

st.markdown("### Differences in product line by Male/Female ")   ## Main Title
if len(df2) >0:
    fig4 = plt.figure()
    plt.title('Total transaction by Gender')
    sns.countplot(df2['product_line'], hue = df2.gender)
    plt.xticks(rotation = 45)
    st.pyplot(fig4)
 



st.write('---')

## Which product line generates most income?


st.markdown("### Which product line generates more income?")
col2, col3 = st.columns((2,2))
cat=df2[["product_line", "total"]].groupby(['product_line'], as_index=False).sum().sort_values(by='total', ascending=False)
if len(cat) >0:

    fig5 = plt.figure()
    sns.barplot(x='product_line', y='total', data=cat)
    plt.xticks(rotation = 45)
    col2.pyplot(fig5)

expander_bar = st.expander("Click to visualize if it's the same result with the gross income instead of the total amount per ticket")
cat2=df2[["product_line", "quantity"]].groupby(['product_line'], as_index=False).sum().sort_values(by='quantity', ascending=False)
if len(cat) >0:

    fig5 = plt.figure()
    sns.barplot(x='product_line', y='quantity', data=cat2)
    plt.xticks(rotation = 45)
    col3.pyplot(fig5)

st.write('---')

 ## Which hour of the day is the busiest?

st.markdown("### Couple of trends : per month and hour")
col4, col5 = st.columns((2,2))
if len(cat) >0:
    fig6 = plt.figure()
    plt.title('Which hour of the day is the busiest?')
    sns.lineplot(x="Hour",  y = 'quantity',data =df2).set_title("Product Sales per Hour")
    col4.pyplot(fig6)


#trend of the months

if len(cat) >0:
    fig6 = plt.figure()
    plt.title('Monthly trend ')
    sns.lineplot(x="month",  y = 'total',data =df2).set_title("Monthly trend by mean")
    col5.pyplot(fig6)



# Full chart of the dataset

c = alt.Chart(df2).mark_point().encode(
    alt.X('Month_day'),
    alt.Y('total'),
    alt.Size('city'),
    alt.Color('city'),
    alt.OpacityValue(0.7),
    tooltip = [alt.Tooltip('city'),
               alt.Tooltip('total'),
               alt.Tooltip('tax5'),
               alt.Tooltip('quantity'),
               alt.Tooltip('customer_type'),
               alt.Tooltip('product_line'),
               alt.Tooltip('payment')
              ]
              
).interactive()


st.markdown("### Here you can see a full stack chart")

st.altair_chart(c, use_container_width=True)


