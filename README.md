This document describes the API endpoints in the FastAPI backend and the React UI components that consume these APIs to display investor and commitment data. install the dependencies based upon requirements.txt pip install -r requirements.txt
prerequisite: run the create_ddl.py to create databse and tables once. run upload_to_db.py to ingest the data to databse tables . note:used sqlite database for quick development
API Endpoints: to start the application: uvicorn main:app --reload Base URL: FastAPI app is running on http://localhost:8000
React UI Components :start the react front end by npm start from the ui->investor-assets
Menu Component (Optional) Provides navigation tabs/buttons to switch between Investors table and Commitments table views.
Running the Application FastAPI backend serves API endpoints.
React frontend consumes APIs and renders tables as per UI designs.
Backend should enable CORS to allow frontend requests.
Recommended to run backend on http://localhost:8000 and frontend development server on http://localhost:3000 with proxy configured.
Notes All amounts are displayed in human-readable format with billion (B) and million (M) suffix.
Dates are formatted as Month Day, Year for UI consistency.
The investor commitment breakdown API allows filtering by asset class for detailed views.
