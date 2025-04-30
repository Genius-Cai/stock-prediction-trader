# Stock Prediction Trader

This project is a stock prediction application built using Python and Flask. It utilizes machine learning techniques to predict stock prices based on historical data.

## Project Structure

```
stock-prediction-trader
├── src
│   ├── app.py                # Entry point of the application
│   ├── data
│   │   ├── data_loader.py    # Handles loading and retrieving stock data
│   │   └── preprocess.py      # Processes raw stock data for model training
│   ├── models
│   │   ├── model.py          # Contains the stock prediction model
│   │   └── train.py          # Trains the stock model and saves it
│   ├── predictions
│   │   └── predict.py        # Makes predictions using the trained model
│   └── utils
│       └── helpers.py        # Utility functions for logging and saving results
├── js
│   └── quant.js              # JavaScript utility functions for frontend
├── requirements.txt           # Lists project dependencies
├── .gitignore                 # Specifies files to ignore in Git
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/Genius-Cai/stock-prediction-trader.git
   cd stock-prediction-trader
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```
   python src/app.py
   ```

2. Access the application in your web browser at `http://127.0.0.1:5000`.

3. Use the provided endpoints to load data, preprocess it, train the model, and make predictions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.