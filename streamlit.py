import streamlit as st
import pandas as pd

st.title(" Sales Summary Dashboard")
st.subheader("Filter and explore sales data by product category")

data = {
    "Product":  ["Laptop", "Mouse", "Desk Chair", "Monitor", "Keyboard", "Webcam", "Headphones"],
    "Category": ["Electronics", "Accessories", "Furniture", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Sales":    [12500, 350, 4200, 8900, 520, 780, 1350],
}

df = pd.DataFrame(data)

st.sidebar.header(" Filter Options")
categories = ["All"] + sorted(df["Category"].unique().tolist())
selected_category = st.sidebar.selectbox("Select a Category", categories)

filtered_df = df if selected_category == "All" else df[df["Category"] == selected_category]

st.markdown(f"### Showing results for: `{selected_category}`")

st.dataframe(filtered_df, use_container_width=True)

st.markdown("###  Sales Chart")
st.line_chart(filtered_df.set_index("Product")["Sales"])