# Student Result Website

This website provides a user-friendly interface to display student academic results and offers the functionality to download these results as a PDF document.
#Live Preview of the Website

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Now-green)](https://www.yourwebsite.com)


![image alt](https://github.com/Vikram2003-07/Result_website/blob/67d444c4c53805c525811d2d4c202b63e4c1a5c2/Screenshot%202025-05-30%20224824.png)
![image alt](https://github.com/Vikram2003-07/Result_website/blob/67d444c4c53805c525811d2d4c202b63e4c1a5c2/Screenshot%202025-05-30%20224846.png)
## Features

* **Student Details Display:** Shows student's USN and name.
* **Detailed Result Table:** Presents subject-wise marks, including Continuous Internal Evaluation (CIE), Semester End Examination (SEE), Total marks, and Grade (GR).
* **Summary Information:** Displays SGPA (Semester Grade Point Average) and Final Grade.
* **PDF Download:** Allows users to download the displayed result sheet as a formatted PDF file.
* **Responsive Design:** Adapts to various screen sizes, from desktops to mobile devices.

## Technologies Used

* **Frontend:**
    * HTML5
    * CSS3 (Custom styles and responsive design)
    * [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/) (for responsive layout and styling)
    * JavaScript
    * [html2pdf.js](https://raw.githack.com/eKoopmans/html2pdf/master/dist/html2pdf.bundle.min.js) (for client-side PDF generation)
* **Templating (Inferred):**
    * Jinja2 (based on `{{ details['Name'] }}` syntax, typically used with Python frameworks like Flask or Django)
* **Backend (Inferred):**
    * Likely Python with a web framework (e.g., Flask, Django) to handle data fetching and rendering the HTML template.

## Setup and Installation (Assumed Python/Flask Backend)

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Vikram2003-07/Result_website.git](https://github.com/Vikram2003-07/Result_website.git)
    cd Result_website
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install backend dependencies (example for Flask):**
    You would typically have a `requirements.txt` file.
    ```bash
    pip install Flask # and any other libraries your backend needs
    ```
    *Note: Ensure you have a mechanism to provide the `details` and `usn` data to the HTML template.*

4.  **Run the application:**
    ```bash
    python app.py # Or whatever your main backend file is named
    ```

5.  **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:5000/` (or the port your Flask/Django app runs on).

## Usage

1.  Enter the USN in the input field (if provided on the main page).
2.  The website will display the student's name, USN, and a detailed table of their subject-wise marks and grades.
3.  Click the "Download Result as PDF" button to generate and download a PDF version of the displayed result.
4.  Use the "Search Another USN" button to return to the search page.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

## License

(Add your license information here, e.g., MIT, Apache 2.0, etc.)
