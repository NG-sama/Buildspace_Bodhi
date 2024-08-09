# Project Bodhi

## Description

Project Bodhi is a Streamlit-based web application that generates content based on user input and a specified template. It utilizes AI language models (GPT-4 and Mistral) to transform user-provided content into a desired format or style.

## Features

- Content and template input areas
- Choice between GPT-4 and Mistral AI models
- Character count for inputs
- Generated content display
- Social media sharing buttons (LinkedIn and Twitter)
- Feedback form
- Donation option

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/project-bodhi.git
   cd project-bodhi
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   Create a `secrets.toml` file in the `.streamlit` directory with the following structure:
   ```toml
   [api_keys]
   OPENAI_API_KEY = "your_openai_api_key"
   MISTRAL_API_KEY = "your_mistral_api_key"
   ```

## Usage

Run the Streamlit app:
```
streamlit run app.py
```

Navigate to the provided local URL in your web browser to use the application.

## How it works

1. Enter your content in the "Content" tab.
2. Provide a template in the "Template" tab.
3. Choose between GPT-4 and Mistral AI models.
4. Click "Generate Content" to process your input.
5. View and share the generated content via the provided social media buttons.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Feedback

Use the feedback form within the app to provide suggestions or report issues.
👉🏾[Tally form here](https://tally.so/r/w2rdMV)

## Support

If you find this project helpful, consider making a donation to support its development and maintenance.
👉🏾[Stripe link here](https://donate.stripe.com/8wM4gS7lx6mS5Ne5kk)

## License
GPL-3.0 license

## Contact

Created by Nikhil Gnanavel - feel free to contact me!

- Twitter: [@_the_real_ng_](https://twitter.com/_the_real_ng_)
- Instagram: [@nikki_builds](https://www.instagram.com/nikki_builds/)
- LinkedIn: [Nikhil Gnanavel](https://www.linkedin.com/in/nikhil-gnanavel/)
