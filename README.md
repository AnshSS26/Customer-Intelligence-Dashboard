# 🛒 Customer Intelligence Dashboard

A Machine Learning project that predicts **Customer Lifetime Value (CLV)** and segments customers into different business categories using purchasing behavior.

Built using the UK Online Retail dataset and deployed with Streamlit.

---

## 🚀 Features

- Predict Customer Lifetime Value (CLV)
- Segment customers into:
  - Premium Customer
  - Regular Customer
  - Low Value Customer
- Business recommendations based on customer segment
- Interactive Streamlit web application

---

## 📊 Machine Learning Workflow

1. Data Cleaning
2. Feature Engineering
3. Customer Segmentation using K-Means Clustering
4. CLV Prediction using Random Forest Regression
5. Model Evaluation
6. Streamlit Dashboard

---

## 📂 Dataset

**UK Online Retail Dataset**

The dataset contains customer purchase transactions including:

- Invoice Number
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## 📈 Models Used

### Customer Segmentation

- K-Means Clustering

### Customer Lifetime Value Prediction

- Random Forest Regressor

---

## 📌 Input Parameters

The application accepts:

- Number of Orders
- Average Order Value
- Average Items per Order
- Days Since Last Purchase

---

## 📤 Output

The dashboard provides:

- Predicted Customer Lifetime Value (CLV)
- Customer Segment
- Business Recommendation
- Customer Summary

---

## 📁 Project Structure

```
Customer_Intelligence_Dashboard/
│
├── app.py
├── Customer_Intelligence_Dashboard.ipynb
├── online_retail_II.csv
├── clv_model.pkl
├── customer_segmentation_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt

streamlit run app.py
```

---

## 📷 Dashboard

*(Add screenshots here after deployment.)*

---

## 👨‍💻 Author

**Ansh**

Commerce & Economics Graduate | Machine Learning Enthusiast