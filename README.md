# Booking Bot

This project is an automated bot built with Python and Selenium to search for the best hotel deals on Booking.com. The bot navigates the website, filters results, and presents a summary of the best options with prices and ratings in a formatted table.

---

## Features
- Automatically navigates to Booking.com and searches for hotels based on user-provided inputs.
- Supports changing the currency to USD.
- Filters results by star rating (e.g., 3, 4, or 5 stars).
- Sorts results by price (lowest first).
- Outputs hotel names, prices, and ratings in a clean table format.

---

## File Structure
bot_learn/
│
├── booking/
│ ├── booking.py
│ ├── booking_filtration.py
│ └── booking_report.py
│
├── main.py
└── README.md

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bot_learn.git
   cd bot_learn
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Open `main.py` and set your desired parameters:
   - `place_to_book`: The location you want to search for hotels.
   - `check_in_date`: The check-in date in the format 'YYYY-MM-DD'.
   - `check_out_date`: The check-out date in the format 'YYYY-MM-DD'.
   - `adults`: The number of adults for the booking.

2. Run the bot:
   ```bash
   python main.py
   ```

3. Follow the prompts in the console to interact with the bot.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a new pull request.

---

