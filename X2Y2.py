# 📚 Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import PIL
from PIL import Image

theme_plotly = None # None or streamlit

X2Y2 = PIL.Image.open('X2Y21.jpeg')

# Title
st.set_page_config(page_title='Evaluating the Activities of X2Y2 Users', page_icon=X2Y2 , layout='wide')
st.title('Evaluating the Activities of X2Y2 Users')

# Content
c1, c2 = st.columns(2)

c1.image(Image.open('Image/X2Y25.jpg'))


st.subheader('📃 Introduction')


st.write(
    """
🔘 **X2Y2 NFT Marketplace**

NFT marketplaces have emerged as a popular platform for NFT enthusiasts to buy and sell their digital assets. These marketplaces have made it easier for users to trade
NFTs, which has led to the rise of several platforms in the market. One such platform that has gained popularity among users is X2Y2.
X2Y2 is a decentralized NFT marketplace that aims to give back to the community by providing a platform where users can trade their digital assets without any 
intermediaries. The platform is built by a team of highly experienced professionals who have expertise in blockchain solutions. The X2Y2 marketplace offers several 
features that make it stand out from other platforms. It provides users with a secure and transparent environment for trading their NFTs, ensuring that all 
transactions are recorded on the blockchain. Additionally, X2Y2 offers low transaction fees, making it an affordable option for users looking to buy or sell their 
digital assets.
In recent times, X2Y2 has witnessed an increase in user activity as more people are joining the platform to trade their NFTs. The marketplace's user-friendly interface
and efficient trading system have contributed significantly to its growing popularity among NFT enthusiasts.
In this dashboard, we will analyze the activity of users on the X2Y2 marketplace and provide insights into its performance. We will examine various metrics such as 
user engagement, transaction volume, and trading patterns to gain a better understanding of how the platform operates and what makes it unique compared to other NFT 
marketplaces.



    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
**In this dashboard, the transaction status of users in the X2Y2 market is reviewed.**
    """
)


#---------------------------------------------------------------------------------------------------------
# dash_style
with open('style.css')as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
	
# flipside API
@st.cache(ttl=600)
def get_data(query1):
     if query1 == 'yesterday data':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/ed420b19-45a3-4624-8357-53eaacabab68/data/latest')
     elif query1 == 'X2Y2 Statistical Data':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/01088e5b-3de7-4b40-8130-05ac7676db93/data/latest')
     elif query1 == 'NFT Collection':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/85d9dabd-8742-4358-a87e-56371bb61a22/data/latest')
     elif query1 == 'NFT Sales':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/818c65d2-deb0-466c-970a-90916f561639/data/latest')
     elif query1 == 'Average daily price of X2Y2 token':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9c29d9d0-16c4-46e8-af48-ead55bc8afec/data/latest')
     elif query1 == 'Top User A':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7a6a3e34-168b-47a7-ad01-aef9bae0235c/data/latest')
     elif query1 == 'Top User B':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/738d9ade-643a-41fb-a4b2-575ed3c466b1/data/latest')
     elif query1 == 'Top User C':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f3da6ed8-8035-4388-a001-ecb2d92eb543/data/latest')
     elif query1 == 'Top User D':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/15779677-1ac8-47b3-bf15-4546a4c47a27/data/latest')
     elif query1 == 'Top User E':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/0bb1c8a8-d1bd-4f85-bbfe-68c17b537b3f/data/latest')
     elif query1 == 'Optimism TX Status':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/880cf7d7-70ab-4cff-b926-3b6df8a28c59/data/latest')
     elif query1 == 'Arbitrum TX Status Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a7c937c0-1a3f-4d47-8e9f-daece6bcab95/data/latest')
     elif query1 == 'Optimism TX Status Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ef59f00d-7aff-42ea-9c8c-f7da9bf07f31/data/latest')
     elif query1 == 'Arbitrum TX Status Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8007648b-997a-4647-9900-ebb983e78c23/data/latest')
     elif query1 == 'Optimism TX Status Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/73494d91-353c-4d8a-aa52-d6eb9f112e10/data/latest')
     elif query1 == 'Top 20 Events Based on TXs Count Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eb082222-8ccf-4e35-ae4d-238f1fa70f2d/data/latest')
     elif query1 == 'Top 20 Events Based on TXs Count Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c4cf84bd-d545-4620-ba8d-2949ac7b929b/data/latest')
     elif query1 == 'Classification of Activity of Addresses Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/06ff575c-8b6b-43ca-b973-21e2dd759071/data/latest')
     elif query1 == 'Classification of Activity of Addresses Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/bb5316a1-9a0e-42d2-aef9-b9e82b0dc36d/data/latest')
     elif query1 == 'Status of Total Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a2b49ba0-adb2-4834-bd8a-6d8c6fbff7ba/data/latest')
     elif query1 == 'Heat Map of Transactions Arbitrum':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/450b8565-460f-4913-a299-4a4b4fd98bee/data/latest')
     elif query1 == 'Heat Map of Transactions Optimism':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ecacbbd4-fd7f-417a-99b4-80fd0a4fef8f/data/latest')
     return None

yesterday_data = get_data('yesterday data')
X2Y2_Statistical_Data = get_data('X2Y2 Statistical Data')
NFT_Collection = get_data('NFT Collection')
NFT_Sales = get_data('NFT Sales')
Average_daily_price_of_X2Y2_token = get_data('Average daily price of X2Y2 token')
Top_User_A = get_data('Top User A')
Top_User_B = get_data('Top User B')
Top_User_C = get_data('Top User C')
Top_User_D = get_data('Top User D')
Top_User_E = get_data('Top User E')
Optimism_TX_Status = get_data('Optimism TX Status')
Arbitrum_TX_Status_Weekly = get_data('Arbitrum TX Status Weekly')
Optimism_TX_Status_Weekly = get_data('Optimism TX Status Weekly')
Arbitrum_TX_Status_Monthly = get_data('Arbitrum TX Status Monthly')
Optimism_TX_Status_Monthly = get_data('Optimism TX Status Monthly')
Top_20_Events_Based_on_TXs_Count_Arbitrum = get_data('Top 20 Events Based on TXs Count Arbitrum')
Top_20_Events_Based_on_TXs_Count_Optimism = get_data('Top 20 Events Based on TXs Count Optimism')
Classification_of_Activity_of_Addresses_Arbitrum = get_data('Classification of Activity of Addresses Arbitrum')
Classification_of_Activity_of_Addresses_Optimism = get_data('Classification of Activity of Addresses Optimism')
Status_of_Total_Transactions = get_data('Status of Total Transactions')
Heat_Map_of_Transactions_Optimism = get_data('Heat Map of Transactions Optimism')
Heat_Map_of_Transactions_Arbitrum = get_data('Heat Map of Transactions Arbitrum')

st.subheader('📊 Data Analysis')
st.write(
    """
**👓Overview**
    """
)
df = yesterday_data
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(label='Current Sales Volume (ETH)', value=df['CURRENT_VOLUME'])
with c2:
    st.metric(label='Current NFT Sales Count', value=df['CURRENT_SALES_COUNT']) 	
with c3:
    st.metric(label='Current Purchasers Count', value=df['PURCHASER'])     
with c4:
    st.metric(label='Current Sellers Count', value=df['SELLER'])    

df = X2Y2_Statistical_Data
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(label='Total NFT Sales Volume (ETH)', value=df['VOLUME'])
with c2:
    st.metric(label='Total NFT Sales Count', value=df['SALES_COUNT'])   	
with c3:  
    st.metric(label='Total Unique NFT Purchasers Count', value=df['PURCHASER']) 
with c4:
    st.metric(label='Total Unique NFT Sellers Count', value=df['SELLER']) 

c1, c2, c3, c4 = st.columns(4)
   
with c1:
    st.metric(label='Total Transactions Fee Collected (ETH)', value=df['TX_FEE_VOL']) 

df = NFT_Collection
with c2:
    st.metric(label='Total NFT Project Count', value=df['Total NFT Project Count'])  
    

st.write(
    """
**📈Trending Overview.**
    """
)
df = NFT_Sales
c1, c2 = st.columns(2)
            
with c1:
     fig = px.line(df, x='DATE', y='VOLUME', title='X2Y2 Sales Volume', log_y=False)
     fig.update_layout(showlegend=True, xaxis_title=None, legend_title=False, yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
with c2:
     fig = px.line(df, x='DATE', y='SALES_COUNT', title='X2Y2 Sales Count', log_y=False)
     fig.update_layout(showlegend=True, xaxis_title=None, legend_title=False, yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

c1, c2 = st.columns(2)
            
with c1:
     fig = px.line(df, x='DATE', y='SELLER', title='X2Y2 Sellers Count', log_y=False)
     fig.update_layout(showlegend=True, xaxis_title=None, legend_title=False, yaxis_title='Address Count', xaxis={'categoryorder':'total ascending'})
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
with c2:
     fig = px.line(df, x='DATE', y='PURCHASER', title='X2Y2 Purchasers Count', log_y=False)
     fig.update_layout(showlegend=True, xaxis_title=None, legend_title=False, yaxis_title='Address Count', xaxis={'categoryorder':'total ascending'})
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

c1, c2 = st.columns(2)
            
with c1:
     fig = px.line(df, x='DATE', y='TX_FEE_VOL', title='Daily Transaction Fees in X2Y2', log_y=False)
     fig.update_layout(showlegend=True, xaxis_title=None, legend_title=False, yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
with c2:
     df = Average_daily_price_of_X2Y2_token
     fig = px.line(df, x='DATE', y='AVERAGE_PRICE', title='Average Daily Price of X2Y2 Token', log_y=False)
     fig.update_layout(showlegend=True, xaxis_title=None, legend_title=False, yaxis_title='$USD', xaxis={'categoryorder':'total ascending'})
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	


st.write(
    """
**👨‍💻 Top Users Identifying.**
    """
)


c1, c2 = st.columns(2)
            
with c1:
    df = Top_User_A
    fig = px.bar(df, x='PROJECT_NAME', y='VOLUME', color='VOLUME', title='Top 10 NFT Projects with the Largest Sales Volumes', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Volume', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with c2:
    df = Top_User_B
    fig = px.bar(df, x='PROJECT_NAME', y='TX_FEE_VOL', color='TX_FEE_VOL', title='Top 10 NFT Projects with the Most Tx Fee Used', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='TX Fees', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
	
c1, c2 = st.columns(2)
            
with c1:
    df = Top_User_C
    fig = px.bar(df, x='PROJECT_NAME', y='SALES_COUNT', color='SALES_COUNT', title='Top 10 NFT Projects With the Most Sale Count', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Sales Count', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with c2:
    df = Top_User_D
    fig = px.bar(df, x='PROJECT_NAME', y='SELLER', color='SELLER', title='Top 10 NFT Projects with the Highest Number of Unique Sellers', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Seller Count', yaxis_title='Address Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
	
c1, c2 = st.columns(2)
            
with c1:
    df = Top_User_E
    fig = px.bar(df, x='PROJECT_NAME', y='PURCHASER', color='PURCHASER', title='Top 10 NFT Projects with the Highest Number of Unique Purchasers', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Purchaser Count', yaxis_title='Address Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		

#-----------------------------------------------------------------------------------------------------------
          
#-----------------------------------------------------------------------------------------------------------
st.subheader('🔍 Conclusion')
st.write(
   """
**
In this dashboard, we took a quick look at the activity of users in the X2Y2 NFT marketplace.**
   """
)
#-------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")
    #c1.image(Image.open('Images/analyst2.JPG'))
with c2:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")
    #c2.image(Image.open('Images/metricsdao.JPG'))
with c3:
    st.info('**[My github](https://github.com/Emanoel91)**', icon="😺")
    #c3.image(Image.open('Images/metricsdao.JPG'))	

	


