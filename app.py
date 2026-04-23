# app.py

import streamlit as st
import logic
import ui


st.title(" Stock Risk Analyzer")

stock = st.text_input("Enter Stock Symbol (e.g., RELIANCE.NS, TSLA)")

if st.button("Analyze"):

    try:
        prices = logic.get_stock_data(stock)

        if len(prices) < 2:
            st.error("Not enough data.")
        else:
            returns = logic.compute_returns(prices)

            mean, var, std_dev, max_r, min_r = logic.calculate_statistics(returns)
            risk = logic.classify_risk(std_dev)
            lower, upper = logic.probability_range(mean, std_dev)

            # Metrics
            st.subheader(" Key Metrics")
            st.write(f"Mean Return: {mean:.4f} ({mean*100:.2f}%)")
            st.write(f"Volatility: {std_dev:.4f} ({std_dev*100:.2f}%)")
            st.write(f"Max Return: {max_r:.4f}")
            st.write(f"Min Return: {min_r:.4f}")
            st.write(f"Risk Level: {risk}")
            st.write(f"95% of returns lie between {lower:.4f} and {upper:.4f}")

            # Graphs
            st.subheader(" Visualizations")

            fig1 = ui.plot_price(prices)
            st.pyplot(fig1)

            interpretation = logic.interpret_results(mean, std_dev)
            st.info(interpretation)
            
            st.write(f"Most returns (~95%) lie between {lower:.4f} and {upper:.4f}")

            fig2 = ui.plot_returns_with_curve(returns, mean, std_dev)
            st.pyplot(fig2)

    except Exception as e:
        st.error(f"Error: {e}")
