from textblob import TextBlob
import pandas as pd
# Example dataset (replace with your dataset)
data = {
    'text': [
        "I love this product, it's amazing!",
        "This is the worst service I've ever experienced.",
        "The movie was okay, nothing special.",
        "I'm neutral about this."
    ]
}

df = pd.DataFrame(data)
# Function to get sentiment polarity
def get_sentiment(text):
    analysis = TextBlob(text)
    # Return sentiment polarity which ranges from -1 to 1
    return analysis.sentiment.polarity

# Apply the function to each text in the DataFrame
df['sentiment'] = df['text'].apply(get_sentiment)

# Display the result
print(df)
