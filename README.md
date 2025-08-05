Tree API (Flask)

A simple RESTful API to manage hierarchical tree structures using Python and Flask.
This project fulfills a take-home assessment and is structured like a lightweight production API.

---

📦 Project Structure

treeapi/
├── app.py               # Main Flask app with GET/POST endpoints
├── test_app.py          # Unit tests using Flask's test client
├── tree_data.json       # Persistent storage for tree nodes
├── requirements.txt     # Python dependencies
├── README.txt           # Instructions (this file)
└── venv/ (optional)     # Python virtual environment (not pushed to GitHub)

---

🚀 How to Run the Server

1. Create a virtual environment in the correct directory:

   python3 -m venv venv
   
3. Open a terminal and activate your virtual environment (if used):
   source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Start the Flask server:
   python app.py

6. Visit:
   http://127.0.0.1:5000/api/tree

---

🧪 How to Test the API (In a Second Terminal)

1. Open a second terminal and activate the virtual environment:
   source venv/bin/activate

2. Add a root node:
   curl -X POST http://127.0.0.1:5000/api/tree -H "Content-Type: application/json" -d "{\"label\": \"root\", \"parentId\": null}"

3. Add a child node:
   curl -X POST http://127.0.0.1:5000/api/tree -H "Content-Type: application/json" -d "{\"label\": \"child1\", \"parentId\": 1}"

4. View the full tree structure:
   curl http://127.0.0.1:5000/api/tree

---

🧪 How to Run Automated Tests

Tests are written in test_app.py using Python's unittest framework.
These use Flask's built-in test client, so you DO NOT need to run the server during tests.

To run the tests:
   python test_app.py

Expected output:
   ...
   ----------------------------------------------------------------------
   Ran 3 tests in X.XXXs

   OK

---

📁 Important Notes

- `tree_data.json` is your local persistent "database"
- It is reset during unit tests, so you can safely run tests without affecting live data
- File should be empty (`[]`) when starting from scratch

---

