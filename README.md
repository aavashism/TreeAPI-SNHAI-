Tree API (Flask)

A simple RESTful API to manage hierarchical tree structures using Python and Flask. This project fulfills a take-home assessment and is structured like a lightweight production API.

---

## Project Structure

treeapi/
├── app.py             # Main Flask app with GET/POST endpoints
├── test_app.py        # Unit tests using Flask's test client
├── tree_data.json     # Persistent storage for tree nodes
├── requirements.txt   # Python dependencies
├── README.md          # Instructions (this file)
└── venv/              # Optional: Python virtual environment (not pushed to GitHub)

---

## How to Run the Server

1. Create a virtual environment:
   python3 -m venv venv

2. Activate the environment:
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Start the server:
   python app.py

Visit: http://127.0.0.1:5000/api/tree

---

## How to Test the API (In a Second Terminal)

1. Add a root node:
   curl -X POST http://127.0.0.1:5000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "root", "parentId": null}'

2. Add a child node:
   curl -X POST http://127.0.0.1:5000/api/tree \
     -H "Content-Type: application/json" \
     -d '{"label": "child1", "parentId": 1}'

3. View the tree:
   curl http://127.0.0.1:5000/api/tree

---

## How to Run Automated Tests

Run the following:
   python test_app.py

You should see:
   ...
   Ran 3 tests in X.XXXs

   OK

---

## Notes

- tree_data.json is used for persistent storage
- It is reset during unit tests to avoid interference
- To start from scratch, clear the file or set it to []
- File should be empty (`[]`) when starting from scratch

---

