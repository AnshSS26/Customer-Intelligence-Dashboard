import streamlit as st
import pandas as pd
import joblib

# Loading Models
model = joblib.load("clv_model.pkl")
kmeans = joblib.load("customer_segmentation_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(
    page_title="Customer Intelligence Dashboard",
    page_icon="🛒",
    layout="centered"
)




st.sidebar.title("About")

st.sidebar.write("""
This application predicts:

• Customer Lifetime Value (CLV)

• Customer Segment

using Machine Learning.
""")




st.title("🛒 Customer Intelligence Dashboard")

st.markdown(
    "Estimate **Customer Lifetime Value (CLV)** and identify customer segments using Machine Learning."
)
st.divider()



col1, col2 = st.columns(2)

with col1:

    orders = st.number_input(
        "Number of Orders",
        min_value=1,
        value=5
    )

    avg_items = st.number_input(
        "Average Items per Order",
        min_value=1,
        value=3
    )

with col2:

    avg_order_value = st.number_input(
        "Average Order Value (₹)",
        min_value=1.0,
        value=1000.0
    )

    recency = st.number_input(
        "Days Since Last Purchase",
        min_value=0,
        value=30
    )
total_items = orders * avg_items
total_spend = orders * avg_order_value




# Calculate derived features
total_items = orders * avg_items
total_spend = orders * avg_order_value


#if st.button("Predict"):
predict = st.button(
    "Predict Customer Insights"
)

if predict:
    with st.spinner("Generating AI Insights..."):
    time.sleep(1)

st.toast("Insights Ready 🚀", icon="🤖")

    # Data for CLV Model
    user_data = pd.DataFrame({

        "Total_Orders": [orders],
        "Total_Items": [total_items],
        "Recency": [recency]

    })

    # Predict CLV
    predicted_clv = model.predict(user_data)[0]

    # Scale data for K-Means
    scaled_data = scaler.transform(user_data)

    # Predict Customer Segment
    cluster = kmeans.predict(scaled_data)[0]

    # Segment Labels
    segment_names = {
        0: "Low Value Customer",
        1: "Premium Customer",
        2: "Regular Customer"
    }

    # Results
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted CLV",
            f"₹ {predicted_clv:,.0f}"
        )

    with col2:
        st.metric(
            "Customer Segment",
            segment_names[cluster]
        )

    st.subheader("Recommendation")

    if cluster == 1:
        st.success(
            "This customer belongs to the Premium segment. Offer exclusive rewards, loyalty benefits, and early access to new products."
        )

    elif cluster == 2:
        st.info(
            "This customer is a Regular buyer. Personalized offers and product recommendations can increase future purchases."
        )

    else:
        st.warning(
            "This customer belongs to the Low Value segment. Discounts and re-engagement campaigns may help improve retention."
        )

    st.subheader("Customer Summary")

    st.write(f"**Number of Orders:** {orders}")
    st.write(f"**Average Order Value:** ₹ {avg_order_value:,.2f}")
    st.write(f"**Average Items per Order:** {avg_items}")
    st.write(f"**Estimated Total Spend:** ₹ {total_spend:,.2f}")
    st.write(f"**Estimated Total Items Purchased:** {total_items}")
    st.write(f"**Days Since Last Purchase:** {recency}")

st.divider()

st.caption(
    "Developed using Python • Scikit-Learn • Streamlit"
)
