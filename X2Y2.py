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
**In this Dashboard we compare and contrast two major L2 chains: Arbitrum & Optimism. We analysis metrics such as total and average transaction volume, average 
transaction size, active users, new users added, and many intersting metrics relevant to this comparison.**
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
     elif query1 == 'New Addresses':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/90828ee6-8f67-47de-8812-29d302b22d4c/data/latest')
     elif query1 == 'Daily Transactions Value':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ea6888d0-422a-4bce-bb77-da7ec1410cbc/data/latest')
     elif query1 == 'Weekly Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/29ad802c-4267-4cc7-8458-b48f17d6898b/data/latest')
     elif query1 == 'Monthly Transactions':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8fd56cb3-9123-407b-9c95-0f215202a1a2/data/latest')
     elif query1 == 'New Addresses Weekly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ca20a9b0-a0c5-49c9-b3d3-5a16a11e6b45/data/latest')
     elif query1 == 'New Addresses Monthly':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/37b83485-1817-4ca3-bf57-8157ff28addc/data/latest')
     elif query1 == 'Transaction Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/335e43c1-ebc8-4117-80be-b97f3d0945a7/data/latest')
     elif query1 == 'Arbitrum TX Status':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cfc29701-c6f0-4a71-b102-7f119313dda9/data/latest')
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
New_Addresses = get_data('New Addresses')
Daily_Transactions_Value = get_data('Daily Transactions Value')
Weekly_Transactions = get_data('Weekly Transactions')
Monthly_Transactions = get_data('Monthly Transactions')
New_Addresses_Weekly = get_data('New Addresses Weekly')
New_Addresses_Monthly = get_data('New Addresses Monthly')
Transaction_Overview = get_data('Transaction Overview')
Arbitrum_TX_Status = get_data('Arbitrum TX Status')
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
**99999999999999999999999999999999999999999999999999999999999999999999.**
    """
)
df = yesterday_data
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(label='Current Sales Volume (ETH)', value=df['CURRENT_VOLUME'])
with c2:
    st.metric(label='Current NFT Sales Count', value=df['CURRENT_SALES_COUNT']) 	
with c3:
    st.metric(label='Current Purchasers Count', value=df['purchaser'])     
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

st.write(
    """
**9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
    """
)
df = Top_20_Events_Based_on_TXs_Count_Arbitrum
c1, c2 = st.columns(2)
            
with c1:
    fig = px.bar(df, x='Event', y='TX Count', color='Event', title='🔵Arbitrum: Top 20 Events Based TXs Count', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
df = Top_20_Events_Based_on_TXs_Count_Optimism
with c2:
    fig = px.bar(df, x='Event', y='TX Count', color='Event', title='🔴Optimism: Top 20 Events Based TXs Count', log_y=False)
    fig.update_layout(showlegend=False, xaxis_title=None, legend_title='', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

st.write(
    """
**99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
    """
)

df = Classification_of_Activity_of_Addresses_Arbitrum
fig = px.scatter(df.sort_values(['Active Day Count', 'Address Count'], ascending=[True, True]), x='Active Day Count', y='Address Count', title='🔵Arbitrum: Classification of the Number of Days of Activity', log_x=False, log_y=True)
fig.update_layout(legend_title=None, xaxis_title='Active Day Count', yaxis_title='Address Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Classification_of_Activity_of_Addresses_Optimism
fig = px.scatter(df.sort_values(['Active Day Count', 'Address Count'], ascending=[True, True]), x='Active Day Count', y='Address Count', title='🔴Optimism: Classification of the Number of Days of Activity', log_x=False, log_y=True)
fig.update_layout(legend_title=None, xaxis_title='Active Day Count', yaxis_title='Address Count')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(
    """
**999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
    """
)

df = Status_of_Total_Transactions
c1, c2 = st.columns(2)
            
with c1:
    fig = px.bar(df, x='L2 Chain', y='Total TXs Count', color='Status', title='Status of Total Transactions', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Status', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with c2:
    fig = px.bar(df, x='L2 Chain', y='Total TX Fees', color='Status', title='Status of Total Transaction Fees', log_y=False, barmode='group')
    fig.update_layout(showlegend=True, xaxis_title=None, legend_title='Status', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.write(
    """
**9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
    """
)

df = Heat_Map_of_Transactions_Arbitrum
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TX Count', histfunc='avg', title='🔵Arbitrum: Transactions Count Heat map, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, yaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TXs Count'))
fig.update_yaxes(categoryorder='array', categoryarray=Heat_Map_of_Transactions_Arbitrum)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Heat_Map_of_Transactions_Optimism
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TX Count', histfunc='avg', title='🔴Optimism: Transactions Count Heat map, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, yaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TXs Count'))
fig.update_yaxes(categoryorder='array', categoryarray=Heat_Map_of_Transactions_Optimism)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Heat_Map_of_Transactions_Arbitrum
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TX Fees', histfunc='avg', title='🔵Arbitrum: Transaction Fees Heat map, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, yaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TX Fees'))
fig.update_yaxes(categoryorder='array', categoryarray=Heat_Map_of_Transactions_Arbitrum)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

df = Heat_Map_of_Transactions_Optimism
fig = px.density_heatmap(df, x='Hour', y='Day Name', z='TX Fees', histfunc='avg', title='🔴Optimism: Transaction Fees Heat map, Days of Week vs. Hours of Day', nbinsx=24)
fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={'dtick': 1}, yaxis={'dtick': 1}, coloraxis_colorbar=dict(title='TX Fees'))
fig.update_yaxes(categoryorder='array', categoryarray=Heat_Map_of_Transactions_Optimism)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.subheader('📊 Charts Analysis in Different Time Frames')

subtab_Daily, subtab_Weekly, subtab_Monthly = st.tabs(['Daily', 'Weekly', 'Monthly'])
with subtab_Daily:
            st.write(
                """
             **999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
                """
            )
            df = Daily_Transactions
            fig = px.line(df, x='Day', y='TX Count', color='L2 Chain', title='Total Number of Transactions', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

            df = Arbitrum_TX_Status
            c1, c2 = st.columns(2)
             
            with c1:
                fig = px.bar(df, x='Day', y='TX Count', color='STATUS', title='🔵Arbitrum: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
            df = Optimism_TX_Status
            with c2:
                fig = px.bar(df, x='Day', y='TX Count', color='STATUS', title='🔴Optimism: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)		
		
with subtab_Daily:

            df = Daily_Transactions		
            fig = px.line(df, x='Day', y='TPS', color='L2 Chain', title='Transaction per Second (TPS)', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
	    
            st.write(
                """
            **999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
                """
            )	
		
            fig = px.bar(df, x='Day', y='Total TX Fee', color='L2 Chain', title='Total Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Day', y='Average TX Fee', color='L2 Chain', title='Average Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
            st.write(
                """
            **999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
                """
            )
		
            fig = px.line(df, x='Day', y='Average TX per Address', color='L2 Chain', title='Average Transaction Count per Address', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
            fig = px.line(df, x='Day', y='Active Address', color='L2 Chain', title='Number of Active Addresses', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with subtab_Daily:
	
             df = New_Addresses
             fig = px.line(df, x='Date', y='New Address', color='L2 Chain', title='Number of New Addresses', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
with subtab_Daily:
             st.write(
                """
             **99999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
                 """
             )		
             df = Daily_Transactions_Value	
             fig = px.line(df, x='Day', y='Total TX Value', color='L2 Chain', title='Total Transactions Value', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
             fig = px.line(df, x='Day', y='Average TX Value', color='L2 Chain', title='Average Transactions Value', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)		
#----------------------------------------------------------------------------------------------------------------------------------------------------------------		
with subtab_Weekly:
            df = Weekly_Transactions
            fig = px.bar(df, x='Week', y='TX Count', color='L2 Chain', title='Total Number of Transactions', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
            df = Arbitrum_TX_Status_Weekly
            c1, c2 = st.columns(2)
             
            with c1:
                fig = px.bar(df, x='Week', y='TX Count', color='STATUS', title='🔵Arbitrum: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
            df = Optimism_TX_Status_Weekly
            with c2:
                fig = px.bar(df, x='Week', y='TX Count', color='STATUS', title='🔴Optimism: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with subtab_Weekly:
            df = Weekly_Transactions		
            fig = px.bar(df, x='Week', y='TPS', color='L2 Chain', title='Transaction per Second (TPS)', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
            fig = px.bar(df, x='Week', y='Total TX Fee', color='L2 Chain', title='Total Transaction Fees', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Week', y='Average TX Fee', color='L2 Chain', title='Average Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)			

            fig = px.line(df, x='Week', y='Average TX per Address', color='L2 Chain', title='Average Transaction Count per Address', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
            fig = px.bar(df, x='Week', y='Active Address', color='L2 Chain', title='Number of Active Addresses', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)			
		
with subtab_Weekly:
	
             df = New_Addresses_Weekly
             fig = px.bar(df, x='Week', y='New Address', color='L2 Chain', title='Number of New Addresses', log_y=False, barmode='group')
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
with subtab_Weekly:
	
             df = Weekly_Transactions	
             fig = px.bar(df, x='Week', y='Total TX Value', color='L2 Chain', title='Total Transactions Value', log_y=False, barmode='group')
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
             fig = px.line(df, x='Week', y='Average TX Value', color='L2 Chain', title='Average Transactions Value', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
#-----------------------------------------------------------------------------------------------------------------------------------------------------------	   	
with subtab_Monthly:
            df = Monthly_Transactions
            fig = px.bar(df, x='Month', y='TX Count', color='L2 Chain', title='Total Number of Transactions', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
	
            df = Arbitrum_TX_Status_Monthly
            c1, c2 = st.columns(2)
             
            with c1:
                fig = px.bar(df, x='Month', y='TX Count', color='STATUS', title='🔵Arbitrum: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
            df = Optimism_TX_Status_Monthly
            with c2:
                fig = px.bar(df, x='Month', y='TX Count', color='STATUS', title='🔴Optimism: Status of Transactions', log_y=False)
                fig.update_layout(showlegend=True, xaxis_title=None, legend_title='STATUS', yaxis_title='TXs Count', xaxis={'categoryorder':'total ascending'})
                st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	

with subtab_Monthly:
            df = Monthly_Transactions			
            fig = px.bar(df, x='Month', y='TPS', color='L2 Chain', title='Transaction per Second (TPS)', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
		
            fig = px.bar(df, x='Month', y='Total TX Fee', color='L2 Chain', title='Total Transaction Fees', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

            fig = px.line(df, x='Month', y='Average TX Fee', color='L2 Chain', title='Average Transaction Fees', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)			

            fig = px.line(df, x='Month', y='Average TX per Address', color='L2 Chain', title='Average Transaction Count per Address', log_y=False)
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
            fig = px.bar(df, x='Month', y='Active Address', color='L2 Chain', title='Number of Active Addresses', log_y=False, barmode='group')
            fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
with subtab_Monthly:
	
             df = New_Addresses_Monthly
             fig = px.bar(df, x='Month', y='New Address', color='L2 Chain', title='Number of New Addresses', log_y=False, barmode='group')
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='Addresses', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)	
	
with subtab_Monthly:
	
             df = Monthly_Transactions	
             fig = px.bar(df, x='Month', y='Total TX Value', color='L2 Chain', title='Total Transactions Value', log_y=False, barmode='group')
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
		
             fig = px.line(df, x='Month', y='Average TX Value', color='L2 Chain', title='Average Transactions Value', log_y=False)
             fig.update_layout(showlegend=True, xaxis_title=None, legend_title='L2 Chain', yaxis_title='$ETH', xaxis={'categoryorder':'total ascending'})
             st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)		
#-----------------------------------------------------------------------------------------------------------
          
#-----------------------------------------------------------------------------------------------------------
st.subheader('🔍 Conclusion')
st.write(
   """
**9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999.**
   """
)
#-------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")
    #c1.image(Image.open('Images/analyst2.JPG'))
with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")
    #c2.image(Image.open('Images/flipside.JPG'))
with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")
    #c3.image(Image.open('Images/metricsdao.JPG'))
with c4:
    st.info('**[My github](https://github.com/Emanoel91)**', icon="😺")
    #c3.image(Image.open('Images/metricsdao.JPG'))	

	


