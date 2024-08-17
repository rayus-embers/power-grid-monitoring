Power Grid Monitoring Dashboard (Alpha Version)
Overview
This project is a web-based monitoring dashboard for power grid elements, such as substations, transformers, and power lines. It was developed as a mini-project during an internship and is currently in its alpha version, meaning it's functional but not fully polished. The dashboard allows users to click on different parts of an interactive SVG map to view device data (like voltage, power, or frequency) over time. The system also displays logs of important events, warnings, or alarms associated with each device.

Features
Interactive SVG Map: Clickable elements in an SVG map of the power grid that allow users to select devices.
Real-time Data Visualization: Charts display data over time (e.g., power or voltage readings) for selected devices.
Custom Time Ranges: Users can select different time ranges (7 days, 30 days, 90 days) using a custom context menu for data visualization.
Logs Display: Shows logs associated with each device, ordered by time.
Multiple Device Tracking: Add multiple devices to a single chart to compare their performance.
Dynamic Chart Updating: Chart.js is used to dynamically update the graph when new devices are added.
Technologies Used
Frontend:
HTML, CSS, JavaScript
Chart.js (for charting)
Custom context menus
Backend:
Django REST API
Database models for power grid data and logs
API Endpoints
Values Endpoint: Fetches power/voltage/frequency values for a device over a time range.
Endpoint: /api/values/
Query Parameters:
device: Device name
substation: Substation name
start_date: Start of the time range
end_date: End of the time range
days: (optional) Number of days to go back from the current date
Logs Endpoint: Fetches logs related to a specific device.
Endpoint: /api/logs/
Query Parameters:
device: Device name
substation: Substation name
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/rayus-embers/power-grid-monitoring.git
cd power-grid-monitoring
Install dependencies:

For the backend, navigate to the Django project directory and install the required Python packages:

bash
Copy code
pip install -r requirements.txt
For the frontend, make sure you have a working HTTP server to serve your static files, or run the app on localhost.

Run the Django server:

bash
Copy code
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000 to see the app.

Usage
Interactive Map: Click on a substation or device from the SVG map to display its corresponding chart.
Right-click for Time Options: Right-click on a device to bring up a custom context menu. From here, you can select time ranges (7, 30, 90 days) to filter the data shown on the graph.
View Logs: Logs for the selected device are displayed in a separate section below the graph. These logs are ordered by time, showing critical alerts and warnings.
Customizing
Adding New Devices: To add new devices or substations, you can modify the SVG map in the frontend and add new entries to the database through the Django admin interface or API.
Context Menu: You can customize the options available in the right-click context menu by modifying the JavaScript logic that generates the menu.
Data Filters: The API allows filtering data by date ranges. You can extend this functionality to include more advanced filtering options if needed.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to add tests for any new features you introduce.