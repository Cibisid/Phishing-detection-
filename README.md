Machine Learning-Enhanced Phishing Detection Browser Extension
Real-time phishing detection using Machine Learning (XGBoost) integrated with a lightweight Chrome Extension and Flask API backend.

 Live Demo
The Machine Learning model API is live and accessible here:

https://phishing-detection-3-5sjx.onrender.com/

 How to Access and Use the Project
Follow these simple steps to access and use the phishing detection project:

1. Access the Live API
Simply click on the link above or visit: https://phishing-detection-3-5sjx.onrender.com/

The API endpoint is publicly hosted and ready for use.

You can send a URL to this API, and it will return whether the website is legitimate or phishing based on the trained Machine Learning model.

2. Set Up Locally (Optional if you want to run backend yourself)
Step 1: Clone the Repository

git clone https://github.com/Cibisid/phishing-detection-extension.git

Step 2: Install the Dependencies

pip install -r requirements.txt
Step 3: Run the Flask Backend

python app.py
By default, this will start a local server at: http://127.0.0.1:5000/

3. Load the Chrome Extension
Open Google Chrome.

Go to chrome://extensions/

Enable Developer Mode (top right corner).

Click Load Unpacked.

Select the extension/ folder from your project directory.

4. How to Use the Chrome Extension
After loading, the extension icon will appear on your Chrome toolbar.

Visit any website:

The extension will automatically analyze the website.

It shows:

Risk Percentage (Green/Yellow/Red Bar)

SSL Status

Domain Age

Content Risk Check

If suspicious, you can Report Phishing directly from the extension popup.

5. Quick Notes
The Chrome Extension uses the Flask API for phishing prediction.

Make sure the Flask server is running if testing locally.

The hosted API (Render.com) can be used without local setup.
