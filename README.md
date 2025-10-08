# Smart Power Scheduler – Technical Summary

**Project Overview**
The *Smart Power Scheduler* is an interactive web application designed to help users identify the most energy-efficient times to use electricity. Developed with **Streamlit**, the system automatically analyzes weekly energy consumption patterns and provides actionable recommendations for reducing energy waste. This initiative aligns with **UN Sustainable Development Goal 7 (Affordable and Clean Energy)** by promoting energy awareness and optimizing electricity consumption behavior.

---

## **Technical Architecture**

The project uses a combination of **Python**, **Streamlit**, **Pandas**, **NumPy**, **Matplotlib**, and **Scikit-learn** to handle data processing, machine learning, visualization, and user interaction. The system architecture is lightweight and self-contained, making it suitable for both local and cloud-based deployments.

1. **Frontend (User Interface):**

   * Built entirely with Streamlit for rapid development and interactive visualization.
   * Provides a clean, responsive interface for displaying consumption data, graphs, and AI-driven recommendations.
   * Automatically loads data from a local CSV file (`data/energy_data.csv`) or generates synthetic weekly energy usage data if the file is not found.

2. **Backend (Computation & Data Handling):**

   * **Data Generation or Loading:**
     The application first checks for the existence of `data/energy_data.csv`. If missing, it generates a **one-week dataset with hourly energy consumption logs**, simulating realistic patterns with higher usage around midday and lower consumption at night.
   * **Data Structure:**
     Each record contains the following columns:
     `Date`, `Month`, `Year`, `Hour`, and `Consumption (kWh)`.
   * **Preprocessing:**
     The program groups data by hour to compute **average hourly energy consumption** across the week.

3. **Machine Learning Model:**

   * A simple **Linear Regression** model (from *scikit-learn*) is used to identify the trend in energy consumption over 24 hours.
   * The model predicts energy usage patterns and determines the **optimal hour** with the lowest expected consumption, which represents the most cost-effective time to use high-energy appliances.
   * This minimal ML approach ensures fast computation and easy interpretability while maintaining reasonable prediction accuracy for trend-based analysis.

4. **Visualization:**

   * **Matplotlib** generates a dual-line chart comparing the actual average hourly energy consumption with the predicted trend.
   * The visualization helps users clearly see when consumption is highest and lowest throughout the day.

---

## **Recommendation Logic**

After training the model, the system identifies the hour of the day corresponding to the **lowest predicted energy use**. This value is presented as the “Best Time to Use Energy,” offering users a simple yet effective guideline for optimizing power usage. The recommendation is dynamically generated based on either uploaded CSV data or auto-generated weekly logs.

---

## **Data Storage & File Management**

* Energy data is stored in the `/data` directory as `energy_data.csv`.
* If no existing dataset is found, the system automatically creates one to ensure continuous functionality.
* The format and structure of this dataset make it easy to extend with real-world IoT or smart meter data in future iterations.

---

## **Future Improvements**

Planned enhancements include:

* Integration of **real-time energy price APIs** for cost-based scheduling.
* Use of **time-series forecasting models (ARIMA or LSTM)** for more accurate predictions.
* **User analytics dashboards** to track long-term energy-saving progress.
* **Mobile-friendly optimization** for better accessibility.

---

**In summary**, the Smart Power Scheduler leverages data science, machine learning, and intuitive design to provide practical recommendations for sustainable energy consumption. By combining predictive analytics and user-centric visualization, it empowers individuals to make informed decisions that contribute to a cleaner and more efficient energy future.
