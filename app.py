from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Add your OpenAI API key here
api_key = "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"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        news_headline = request.form['headline']
        option = request.form['option']

        if option == 'multiperspective':
            # Call OpenAI API to generate Multi-Perspective Reporting
            output = generate_multi_perspective_report(news_headline)
        elif option == 'timeline':
            # Call OpenAI API to generate a timeline
            output = generate_timeline(news_headline)
        else:
            output = "Invalid option selected."

        return render_template('index1.html', headline=news_headline, output=output)

    return render_template('index1.html', headline=None, output=None)

def generate_multi_perspective_report(news_headline):
    openai.api_key = api_key

    # Define your prompt for OpenAI based on the user's news headline
    prompt = f"Generate Multi-Perspective Reporting for the news: {news_headline}."
    
    # Call the OpenAI API to generate the report
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )

    return response.choices[0].text

def generate_timeline(news_headline):
    openai.api_key = api_key

    # Define your prompt for OpenAI based on the user's news headline
    prompt = f"Generate a timeline for the news: {news_headline}."
    
    # Call the OpenAI API to generate the timeline
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150  # Adjust as needed
    )

    return response.choices[0].text

if __name__ == '__main__':
    app.run(debug=True)
