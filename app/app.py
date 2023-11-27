import streamlit as st

def main():
    st.header("Image and text classification")

    task_options = ["Choose any option", "Sentiment Analysis", "Image Recognition"]
    task = st.selectbox("Choose a task", task_options)

    if task == "Choose any option":
        st.warning("Please choose a valid option.")
    elif task == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")
        sentiment_model_options = ["Perceptron", "Backpropagation", "DNN", "RNN", "LSTM"]
        selected_sentiment_model = st.radio("Select a sentiment analysis model", sentiment_model_options)
        if st.button("Analyze Sentiment"):
            if selected_sentiment_model:
                st.success(f"Sentiment analysis using selected model: {selected_sentiment_model}")
            else:
                st.warning("Please select a sentiment analysis model.")

    elif task == "Image Recognition":
        st.subheader("Image Recognition")
        image_model_options = ["CNN"]
        selected_image_model = st.radio("Select an image recognition model", image_model_options)
        if st.button("Recognize Image"):
            if selected_image_model:
                st.success(f"Image recognition using selected model: {selected_image_model}")
            else:
                st.warning("Please select an image recognition model.")

if __name__ == "__main__":
    main()
 