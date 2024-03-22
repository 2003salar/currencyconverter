# Currency Converter

### Video Demo: [Watch here](https://youtu.be/qzUncfadpkY)

### Description:
Currency Converter is a web application that allows users to convert and access up-to-date currency rates. The application is built using Flask, with Python for backend functionality, a portion of JavaScript for dynamic elements, and HTML/CSS for aesthetics and markup. Jinja is used for template rendering, while SQLite is employed for storing user login information and conversion histories. The application comprises 12 HTML files:

- sign_up.html
- login.html
- layout.html
- index.html
- calculator.html
- apology.html
- history.html
- account.html
- change_password.html
- contact.html
- quoted.html
- delete.html

Each file serves a specific function, such as user authentication, currency conversion, and account management. The *calculator.html* file allows users to select source and target currencies, along with the desired amount, to obtain converted rates. *Layout.html* contains the core HTML structure and is extended across other HTML files using Jinja syntax. Account modifications, such as password changes and deletions, can be performed in *change_password.html* and *delete.html* respectively.

Styling is achieved using Bootstrap 5 for frontend design. JavaScript is utilized primarily for input validation, ensuring data integrity.

### What does Currency Converter do?
Currency Converter is designed exclusively for currency conversion. Leveraging the [ExchangeRate-API](https://www.exchangerate-api.com/), the application provides access to reliable and accurate currency rates. Users can view the standard exchange rate of United States dollars (USD) against other currencies on the homepage. Additionally, they can perform currency conversions on the Rate Calculator page and access their conversion history on the History page. Account-related actions, including account information updates and deletions, can be managed on the Account page.

### Features:
In addition to its primary functionality, Currency Converter allows users to contact the author for feedback, suggestions, or criticism.

### How to use Currency Converter:
**Note:** *Ensure you have downloaded the required modules listed in requirements.txt to run this application.*

1. Clone the repository.
2. Navigate to the repository directory in your terminal.
3. Run the command: flask run
4. Register for a free account to access the application's features.
5. Enjoy using Currency Converter anytime, anywhere.

