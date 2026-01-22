# 💰 Salary Prediction Web App

A machine learning web application that predicts salary based on years of experience using Simple Linear Regression. Built with Streamlit and scikit-learn.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)

## 🌟 Features

- **Interactive Web Interface**: User-friendly Streamlit interface for real-time predictions
- **Machine Learning Model**: Simple Linear Regression trained on salary data
- **Instant Predictions**: Get salary estimates based on years of experience
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🚀 Live Demo

(https://salary-prediction-app-kqjykmqdvaxjrmarjvy4dw.streamlit.app/)


## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit**: Web framework for building the interactive interface
- **scikit-learn**: Machine learning library for training the regression model
- **NumPy**: Numerical computing library
- **Joblib**: Model serialization

## 📋 Prerequisites

Before running this project, make sure you have Python 3.8 or higher installed on your system.

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/salary-prediction-app.git
   cd salary-prediction-app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Access the app**
   - The app will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

3. **Make predictions**
   - Enter the years of experience in the input field
   - Click "Predict Salary" to get the estimated salary

## 📊 Model Information

The prediction model is a Simple Linear Regression trained on historical salary data. The model learns the relationship between years of experience and salary to make predictions.

**Model Details:**
- Algorithm: Linear Regression
- Features: Years of Experience (single feature)
- Target: Salary
- Model file: `salary_model.pkl`

## 📁 Project Structure

```
salary-prediction-app/
│
├── app.py                              # Main Streamlit application
├── salary_model.pkl                     # Trained ML model
├── Simple_Linear_Regression.ipynb       # Model training notebook
├── requirements.txt                     # Project dependencies
├── README.md                           # Project documentation
├── .gitignore                          # Git ignore file
└── LICENSE                             # License file
```

## 🔄 Model Training

The model was trained using the Jupyter notebook `Simple_Linear_Regression.ipynb`. To retrain the model:

1. Open the notebook:
   ```bash
   jupyter notebook Simple_Linear_Regression.ipynb
   ```

2. Run all cells to train the model

3. The trained model will be saved as `salary_model.pkl`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Yash**
- GitHub: [@yourusername](https://github.com/yashmundhe01)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/yash-mundhe-30189819a/)


## 📧 Contact

For any questions or feedback, please reach out via yashmundhe01@gmail.com

---

⭐ If you found this project helpful, please give it a star!
