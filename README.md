# 💰 Smart Budget Tracker

A sleek web app to manage your personal finances — track your income, expenses, and get visual insights into your spending patterns.

---

🚀 Tools and Technologies Used
<table style="width: 100%; border-collapse: collapse;"> <thead> <tr> <th>Languages</th> <th>Framework</th> <th>Database</th> <th>Charts Library</th> <th>API Usage</th> <th>IDE</th> <th>Localhost Server</th> <th>UI/UX</th> <th>OS</th> </tr> </thead> <tbody> <tr> <td> <a href="https://www.python.org/"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> </a><br> <a href="https://developer.mozilla.org/en-US/docs/Web/HTML"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"> </a><br> <a href="https://developer.mozilla.org/en-US/docs/Web/CSS"> <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"> </a><br> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"> </a> </td> <td> <a href="https://flask.palletsprojects.com/"> <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"> </a> </td> <td> <a href="https://www.sqlite.org/"> <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite"> </a> </td> <td> <a href="https://www.chartjs.org/"> <img src="https://img.shields.io/badge/chart.js-F5788D?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="Chart.js"> </a> </td> <td> <a href="https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API"> <img src="https://img.shields.io/badge/fetch--api-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="Fetch API"> </a> </td> <td> <a href="https://code.visualstudio.com/"> <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code"> </a> </td> <td> <a href="https://www.apachefriends.org/"> <img src="https://img.shields.io/badge/xampp-FB7A24?style=for-the-badge&logo=xampp&logoColor=white" alt="XAMPP"> </a> </td> <td> <a href="https://www.figma.com/"> <img src="https://img.shields.io/badge/figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white" alt="Figma"> </a> </td> <td> <a href="https://www.microsoft.com/en-us/windows/windows-11"> <img src="https://img.shields.io/badge/windows_11-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows 11"> </a> </td> </tr> </tbody> </table>

---

## ✨ Key Features

- 🔒 **Secure Budgeting System**: Uses Flask back-end with SQLite to handle transactions safely and locally.
- 📊 **Dynamic Expense Visualization**: Integrated with Chart.js to display expenses and incomes in beautiful charts.
- 🧠 **Smart Categorization**: Automatically classifies income and expense types for easier budget tracking.
- 🔄 **Real-time Update**: Instantly reflects changes via JavaScript and DOM manipulation.
- 🎯 **Responsive UI**: Clean, minimal interface designed with HTML, CSS, and a focus on usability.

---

## 📁 Project Structure
smart_budget_tracker/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── charts.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── dashboard.html
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── instance/
│   └── budget.db
├── LICENSE
├── .gitignore
├── config.py
├── run.py
├── requirements.txt
└── README.md



---

## ⚙️ Installation & Local Setup

Follow these steps to run the project locally:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/alaminO8islam/smart_budget_tracker.git
   cd smart_budget_tracker

2. **Create a Virtual Environment**
  python -m venv venv
  source venv/Scripts/activate    # Windows

3. **Install Required Packages**
  pip install -r requirements.txt

4. **Run the App**
  python run.py

5. **Visit http://127.0.0.1:5000 in your browser.**


---

## 🧪 Usage Instructions

| Page      | Purpose                  | Path         |
| --------- | ------------------------ | ------------ |
| Home      | Input income & expenses  | `/`          |
| Dashboard | View chart and summaries | `/dashboard` |

Add transactions via the homepage form.
Charts update in real-time on the dashboard.
Edit or extend functionality via routes.py and models.py.

---

## 📤 GitHub Deployment (Optional)

If you haven’t already:
git init
git remote add origin https://github.com/alaminO8islam/smart_budget_tracker.git
git add .
git commit -m "Initial commit"
git push -u origin main


---

## 🛡️ License
This project is licensed under the MIT License. 

---

## 🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m "Add your feature")

Push to the branch (git push origin feature/your-feature)

Create a pull request




