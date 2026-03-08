IND vs AUS Fantasy Cricket Team Builder
A high-performance, web-based fantasy sports application that allows users to draft an 11-player cricket squad for an India vs Australia match. This project demonstrates state management, real-time validation logic, and responsive UI design.

🚀 Key Features
Squad Building: Select exactly 11 players from a pool of 24 international cricketers.

Real-time Credit System: Automated logic to ensure the team stays within the 100.0 credit limit.

Role Validation: Filter players by roles (WK, BAT, AR, BOWL) to build a balanced team.

Leadership Selection: Interactive Captain (2x points) and Vice-Captain (1.5x points) selection with instant visual feedback.

Persistence: Uses Browser LocalStorage to maintain team data across selection screens.

🛠️ Tech Stack
Frontend: HTML5, CSS3 (Bootstrap 5), JavaScript (ES6+).

Backend: Flask (Python).

Architecture: Client-side heavy logic with a Flask routing layer.

📂 Project Structure
app.py: Flask server handling routes.

templates/: HTML views (Home, Builder, Selection).

static/: CSS styling and visual assets.

🏁 How to Run
Clone this repository.

Install Flask: pip install flask

Run the application: python app.py.

Visit http://127.0.0.1:5000 in your browser.