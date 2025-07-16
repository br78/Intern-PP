import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("Medicaldata.csv", nrows=50000)

df = load_data()

st.title("Medicare Data Analysis")

# -------- FORM SECTION -------- #
with st.form(key='filter_form'):
    st.header("Filter Options")

    # Dropdown for selecting States
    states = df['Prscrbr_State_Abrvtn'].dropna().unique()
    selected_states = st.multiselect("Select States", sorted(states), default=list(states)[:5])

    # Dropdown for selecting Specialties
    specialties = df['Prscrbr_Type'].dropna().unique()
    selected_specialties = st.multiselect("Select Specialties", sorted(specialties), default=list(specialties)[:5])

    # Slider for Total Claims Range
    min_claims, max_claims = int(df['Tot_Clms'].min()), int(df['Tot_Clms'].max())
    claims_range = st.slider("Total Claims Range", min_claims, max_claims, (min_claims, max_claims))

    # Submit button for form
    submit_button = st.form_submit_button(label="Apply Filters")

# -------- FILTER DATA AFTER FORM SUBMISSION -------- #
filtered_df = pd.DataFrame()

# Only filter when the form is submitted
if submit_button:
    # Apply filters based on user selections
    filtered_df = df[
        df['Prscrbr_State_Abrvtn'].isin(selected_states) &
        df['Prscrbr_Type'].isin(selected_specialties) &
        df['Tot_Clms'].between(claims_range[0], claims_range[1])
    ]

    st.markdown(f"### Showing {len(filtered_df)} Records After Filtering")

    # Show summary KPIs (metrics)
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg. Drug Cost", f"${filtered_df['Tot_Drug_Cst'].mean():,.2f}")
    col2.metric("Total Prescribers", f"{filtered_df['PRSCRBR_NPI'].nunique()}")
    col3.metric("Total Beneficiaries", f"{filtered_df['Tot_Benes'].sum():,.0f}")

    # Visualization - Claims by State
    st.subheader("Total Claims by State")
    state_claims = filtered_df.groupby('Prscrbr_State_Abrvtn')['Tot_Clms'].sum().reset_index()
    fig1 = px.bar(state_claims, x='Prscrbr_State_Abrvtn', y='Tot_Clms', color='Tot_Clms')
    st.plotly_chart(fig1, use_container_width=True)

    # Visualization - Top 10 Prescribers by Total Drug Cost
    st.subheader("Top 10 Prescribers by Total Drug Cost")
    top_prescribers = filtered_df.nlargest(10, 'Tot_Drug_Cst')
    fig2 = px.bar(top_prescribers, x='Prscrbr_Last_Org_Name', y='Tot_Drug_Cst', color='Tot_Drug_Cst')
    st.plotly_chart(fig2, use_container_width=True)

    # Download Filtered Data Button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_medicare_data.csv',
        mime='text/csv'
    )

