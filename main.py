import streamlit as st
import mysql.connector as sql
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px

# -------------------------------This is the configuration page for our Streamlit Application---------------------------
st.set_page_config(
    page_title="Phonepe Pulse Data Visualization",
    page_icon="📱",
    layout="wide"
)



# -------------------------------This is the sidebar in a Streamlit application, helps in navigation--------------------
with st.sidebar:
    selected = option_menu("Main Menu", ["About Project", "Topmost Data", "Explore Data"],
                           icons=["gear", "bar-chart", "search"],
                           styles={"nav-link": {"font": "sans serif", "font-size": "20px", "text-align": "centre"},
                                   "nav-link-selected": {"font": "sans serif", "background-color": "#8a2be3"},
                                   "icon": {"font-size": "20px"}
                                   }
                           )



# -----------------------------------------Connecting with MySQL Workbench Database------------------------------------
hostname = "your hostname goes here"
database = "your database name goes here"
username = "your username goes here"
pwd = "your password goes here"

mydb = sql.connect(host=hostname,
                   user=username,
                   password=pwd,
                   database=database
                   )
# If buffered is True , the cursor fetches all rows from the server after an operation is executed.
cursor1 = mydb.cursor(buffered=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# -----------------------------------------------About Project Section--------------------------------------------------
if selected == "About Project":
    st.markdown('<h1 style="color:#b551fc"><center>Phonepe Pulse Data Visualization and Exploration</center></h1>',
                unsafe_allow_html=True)
    st.markdown('<h2 style="color:#b551fc"><center>A User-Friendly Tool Using Streamlit and Plotly</center></h2>',
                unsafe_allow_html=True)
    st.markdown('<div style="height: 90px;"></div>', unsafe_allow_html=True)
    st.markdown("### :violet[Technologies :] Github Cloning, Python, Pandas, MySQL, "
                "mysql-connector-python, Streamlit, and Plotly.")
    st.markdown("### :violet[Overview :] In this streamlit app users will be able to access the dashboard from "
                "a web browser and easily navigate the different visualizations and facts and figures displayed. "
                "The dashboard will provide valuable insights and information about the data in the Phonepe pulse "
                "Github repository, making it a valuable tool for data analysis and decision-making.")
    st.markdown("### :violet[Domain :] Fintech")



# -----------------------------------------------Topmost Data Section---------------------------------------------------
if selected == "Topmost Data":
    st.markdown('<h2 style="color:#b551fc">Topmost Data</h2>', unsafe_allow_html=True)
    Category = st.sidebar.selectbox("Category", ("Transactions", "Users"))
    Year = st.slider("Select a Year", min_value=2018, max_value=2022)
    Quarter = st.slider("Select a Quarter for the respective Year", min_value=1, max_value=4)

    # -------------------Top 11 transactions data for State, District and Pincode-------------------
    if Category == "Transactions":
        col1, col2 = st.columns([1, 1])
        col3, col4 = st.columns([1, 1])

        with col1:
            st.markdown('<h3 style="color:#b551fc">State-Wise</h3>', unsafe_allow_html=True)
            cursor1.execute(
                f"select state, sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total_Amount "
                f"from a_transactions where year = {Year} and quarter = {Quarter} group by state "
                f"order by Total_Amount desc "
                f"limit 11")
            df = pd.DataFrame(cursor1.fetchall(), columns=['State', 'Transactions_Count', 'Total_Amount'])
            fig = px.pie(df,
                         values='Total_Amount',
                         names='State',
                         title='Top 11 States based on Total Amount spend<br>on Phonepe'
                         )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown('<h3 style="color:#b551fc">District-Wise</h3>', unsafe_allow_html=True)
            cursor1.execute(
                f"select district , sum(Count) as Total_Count, sum(Amount) as Total_Amount "
                f"from m_transactions where year = {Year} and quarter = {Quarter} group by district "
                f"order by Total_Amount desc "
                f"limit 11")
            df = pd.DataFrame(cursor1.fetchall(), columns=['District', 'Transactions_Count', 'Total_Amount'])
            fig = px.pie(df,
                         values='Total_Amount',
                         names='District',
                         title='Top 11 Districts based on Total Amount spend<br>on Phonepe'
                         )
            st.plotly_chart(fig, use_container_width=True)

        with col3:
            st.markdown('<h3 style="color:#b551fc">Pincode-Wise</h3>', unsafe_allow_html=True)
            cursor1.execute(
                f"select pincode, sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total_Amount "
                f"from t_transactions where year = {Year} and quarter = {Quarter} group by pincode "
                f"order by Total_Amount desc "
                f"limit 11")
            df = pd.DataFrame(cursor1.fetchall(), columns=['Pincode', 'Transactions_Count', 'Total_Amount'])
            fig = px.pie(df,
                         values='Total_Amount',
                         names='Pincode',
                         title='Top 11 Pin-codes based on Total Amount spend<br>on Phonepe',
                         )
            st.plotly_chart(fig, use_container_width=True)


    # -------------------Top 11 users data for State, District, Pincode and Brand-------------------
    if Category == "Users":
        col1, col2 = st.columns([1, 1])
        col3, col4 = st.columns([1, 1])

        with col1:
            st.markdown('<h3 style="color:#b551fc">Brands-Wise</h3>', unsafe_allow_html=True)
            if Year == 2022 and (Quarter == 2 or Quarter == 3 or Quarter == 4):
                st.markdown('<h5 style="color:#ff0000">Note : No Data to Display for 2022 Quarter 2, 3 and 4</h5>',
                            unsafe_allow_html=True)
                cursor1.execute(
                    f"select brands, sum(count) as Total_Count, avg(percentage)*100 as Avg_Percentage from a_user "
                    f"where year = {Year} and quarter = {Quarter} group by brands "
                    f"order by Total_Count desc "
                    f"limit 11")
                df = pd.DataFrame(cursor1.fetchall(), columns=['Brand', 'Total_Users', 'Avg_Percentage'])
                fig = px.bar(df,
                             x="Brand",
                             y="Total_Users",
                             title='Top 11 Mobile Brands based on Total Users that use<br>Phonepe',
                             color='Avg_Percentage'
                             )
                st.plotly_chart(fig, use_container_width=True)

            else:
                cursor1.execute(
                    f"select brands, sum(count) as Total_Count, avg(percentage)*100 as Avg_Percentage from a_user "
                    f"where year = {Year} and quarter = {Quarter} group by brands "
                    f"order by Total_Count desc "
                    f"limit 11")
                df = pd.DataFrame(cursor1.fetchall(), columns=['Brand', 'Total_Users', 'Avg_Percentage'])
                fig = px.bar(df,
                             x="Brand",
                             y="Total_Users",
                             title='Top 11 Mobile Brands based on Total Users that use<br>Phonepe',
                             color='Avg_Percentage'
                             )
                st.plotly_chart(fig, use_container_width=True)

                # # This is the Pie Chart Implementation of the same data above
                # fig2 = px.pie(df,
                #               values='Total_Users',
                #               names='Brand',
                #               title='Top 11 Mobile Brands based on Total Users that use<br>Phonepe',
                #               hover_data=['Avg_Percentage'],
                #               )
                # fig2.update_traces(textposition='inside', textinfo='percent+label')
                # st.plotly_chart(fig2, use_container_width=True)

        with col2:
            st.markdown('<h3 style="color:#b551fc">District-Wise</h3>', unsafe_allow_html=True)
            cursor1.execute(
                f"select district, sum(Registered_User) as Total_Users, sum(app_opens) as Total_Appopens from m_user "
                f"where year = {Year} and quarter = {Quarter} group by district "
                f"order by Total_Users desc "
                f"limit 11")
            df = pd.DataFrame(cursor1.fetchall(), columns=['District', 'Total_Users', 'Total_Appopens'])
            df["Total_Appopens"] = df["Total_Appopens"].astype(int)
            fig = px.bar(df,
                         x="District",
                         y="Total_Users",
                         title='Top 11 Districts based on Total Users that use<br>Phonepe',
                         color='Total_Appopens'
                         )
            st.plotly_chart(fig, use_container_width=True)

        with col3:
            st.markdown('<h3 style="color:#b551fc">Pincode-Wise</h3>', unsafe_allow_html=True)
            cursor1.execute(
                f"select Pincode, sum(Registered_Users) as Total_Users from t_user "
                f"where year = {Year} and quarter = {Quarter} group by Pincode "
                f"order by Total_Users desc "
                f"limit 11")
            df = pd.DataFrame(cursor1.fetchall(), columns=['Pincode', 'Total_Users'])
            fig = px.pie(df,
                         values='Total_Users',
                         names='Pincode',
                         title='Top 11 Pin-codes based on Total Users that use<br>Phonepe',
                         )
            st.plotly_chart(fig, use_container_width=True)

        with col4:
            st.markdown('<h3 style="color:#b551fc">State-Wise</h3>', unsafe_allow_html=True)
            cursor1.execute(
                f"select state, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from m_user "
                f"where year = {Year} and quarter = {Quarter} group by state "
                f"order by Total_Users desc "
                f"limit 11")
            df = pd.DataFrame(cursor1.fetchall(), columns=['State', 'Total_Users', 'Total_Appopens'])
            fig = px.pie(df,
                         values='Total_Users',
                         names='State',
                         title='Top 11 States based on Total Users that use<br>Phonepe',
                         hover_data=['Total_Appopens']
                         )
            st.plotly_chart(fig, use_container_width=True)

# -----------------------------------------------Explore Data Section---------------------------------------------------
if selected == "Explore Data":
    st.markdown('<h2 style="color:#b551fc">Explore Data</h2>', unsafe_allow_html=True)
    Category = st.sidebar.selectbox("Category", ("Transactions", "Users"))
    Year = st.slider("Select a Year", min_value=2018, max_value=2022)
    Quarter = st.slider("Select a Quarter for the respective Year", min_value=1, max_value=4)

    # -------------------Exploration for Transactions Data-------------------
    if Category == "Transactions":
        # -------Services for which transactions are done using Phonepe-------
        st.markdown('<h2 style="color:#b551fc">Services for which transactions are done using Phonepe</h2>',
                    unsafe_allow_html=True)
        cursor1.execute(
            f"select Transaction_type, sum(Transaction_count) as Total_Transactions, "
            f"sum(Transaction_amount) as Total_Amount from a_transactions where year= {Year} and quarter = {Quarter} "
            f"group by transaction_type "
            f"order by Transaction_type")
        df = pd.DataFrame(cursor1.fetchall(), columns=['Transaction_Type', 'Total_Transactions', 'Total_Amount'])

        fig = px.bar(df,
                     title='Services for which Phonepe was used for Transactions',
                     x="Transaction_Type",
                     y="Total_Transactions",
                     color='Total_Amount'
                     )
        st.plotly_chart(fig, use_container_width=True)


        # -------Districts total transactions that are done using Phonepe in a particular State-------
        st.markdown('<h2 style="color:#b551fc">Districts total transactions that are done using Phonepe in a '
                    'particular State</h2>', unsafe_allow_html=True)
        st.markdown('<h3 style="color:#54C8D6">Select a State to continue : </h3>',
                    unsafe_allow_html=True)
        states = st.selectbox("States",
                              ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam',
                               'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                               'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
                               'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                               'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                               'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana',
                               'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'])

        cursor1.execute(
            f"select State, District, sum(count) as Total_Transactions, sum(amount) as Total_Amount "
            f"from m_transactions where year = {Year} and quarter = {Quarter} and State = '{states}' "
            f"group by State, District,year,quarter "
            f"order by state,district")

        df = pd.DataFrame(cursor1.fetchall(), columns=['State', 'District', 'Total_Transactions', 'Total_Amount'])
        fig = px.bar(df,
                     title=states,
                     x="District",
                     y="Total_Transactions",
                     color='Total_Amount'
                     )
        st.plotly_chart(fig, use_container_width=True)


        # -------State data based on Transactions Count-------
        st.markdown('<h2 style="color:#b551fc">State data based on Transactions Count</h2>', unsafe_allow_html=True)
        cursor1.execute(
            f"select state, sum(count) as Total_Transactions, sum(amount) as Total_Amount from m_transactions"
            f" where year = {Year} and quarter = {Quarter} group by state "
            f"order by state")
        df1 = pd.DataFrame(cursor1.fetchall(), columns=['State', 'Total_Transactions', 'Total_Amount'])
        df1["Total_Transactions"] = df1["Total_Transactions"].astype(int)
        df2 = pd.read_csv('States.csv')
        df1["State"] = df2

        fig = px.choropleth(df1,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_Transactions',
                            title='Transaction Count based Data'
                            )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)


        # -------State data based on Transactions Amount-------
        st.markdown('<h2 style="color:#b551fc">State data based on Transactions Amount</h2>', unsafe_allow_html=True)
        cursor1.execute(
            f"select state, sum(count) as Total_Transactions, sum(amount) as Total_Amount from m_transactions "
            f"where year = {Year} and quarter = {Quarter} group by state "
            f"order by state")
        df1 = pd.DataFrame(cursor1.fetchall(), columns=['State', 'Total_Transactions', 'Total_Amount'])
        df2 = pd.read_csv('States.csv')
        df1["State"] = df2

        fig = px.choropleth(df1,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_Amount',
                            title='Transaction Amount based Data'
                            )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

    # -------------------Exploration for User Data------------------
    if Category == "Users":
        # -------State data based on App Opens-------
        st.markdown('<h2 style="color:#b551fc">State data based on App Opens</h2>', unsafe_allow_html=True)
        cursor1.execute(
            f"select state, sum(Registered_user) as Total_Users, sum(App_opens) as Total_Appopens from m_user "
            f"where year = {Year} and quarter = {Quarter} group by state "
            f"order by state")
        df1 = pd.DataFrame(cursor1.fetchall(), columns=['State', 'Total_Users', 'Total_Appopens'])
        df1["Total_Appopens"] = df1["Total_Appopens"].astype(float)
        df2 = pd.read_csv('States.csv')
        df1["State"] = df2

        fig = px.choropleth(df1,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_Appopens'
                            )

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)


        # -------Districts total users that use Phonepe in a particular State-------
        st.markdown('<h2 style="color:#b551fc">Districts total users that use Phonepe in a particular State</h2>',
                    unsafe_allow_html=True)
        st.markdown('<h3 style="color:#54C8D6">Select a State to continue : </h3>',
                    unsafe_allow_html=True)
        states = st.selectbox("States",
                              ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam',
                               'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                               'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
                               'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                               'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                               'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana',
                               'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'])

        cursor1.execute(
            f"select State,District,sum(Registered_user) as Total_Users, sum(App_opens) as Total_App_opens "
            f"from m_user where year = {Year} and quarter = {Quarter} and state = '{states}' "
            f"group by State, District,year,quarter "
            f"order by state,district")

        df = pd.DataFrame(cursor1.fetchall(), columns=['State', 'District', 'Total_Users', 'Total_App_opens'])
        fig = px.bar(df,
                     title=states,
                     x="District",
                     y="Total_Users",
                     )
        st.plotly_chart(fig, use_container_width=True)
