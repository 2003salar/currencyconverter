# Currency Converter
#### Video Demo:  <https://youtu.be/qzUncfadpkY>
#### Description:
Currency Converter is a web application from which users can convert and get up-to-date currency rates. This application is built using Flask, programming languages Python and a portion of JavaScript, languages HTML and CSS for aesthetics and markup, and Jinja. Additionally, for storing data inside this application, SQLite, a lite version of SQL, is used to store users' login information and histories. Currency Converter is built from 12 HTML files and they are: 
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

Each of these files has the functionality that their names suggest. In the file called *calculator.html*, users can select a source and a target currency respectively, in addition to its amount, to get the converted and update rates. Furthermore, *layout.html* is the file where the core HTML has been embedded and is extended using Jinja syntax in other HTML files as well. Modifying or deleting accounts can be done in files *change_password.html* and *delete.html* respectively.

In terms of styling, in this application, Bootstrap 5 has been used to style the front end of this particular project. JavaScript is used for validating the users' inputs in the *input* tags, but it is not invoked as much as other languages in this application. 

#### What does Convert Currency do?
This web application is solely built to convert arbitrary currencies of the users. In this application, [ExchangeRate-API](https://www.exchangerate-api.com/) has given the author access to the API of currencies and their updated rates which can indicate that the rates are reliable and accurate. Users can get the standard rate of United States dollars (USD) on their homepage against other currencies. Moreover, if they want to convert currencies, they can achieve that by visiting the Rate Calculator page. Additionally, their conversion histories are saved and can be accessed on the History page. Furthermore, users can change and even delete their account information on the Account page.  

#### What features does Currency Convert have?
Besides the functionality that Currency Convert has, users can contact the author of this web application for feedback, suggestions or criticism.  

#### How to use Currency Converter?
**NOTE**: *Make sure to download requirements.txt modules to run this file.*
First, download the repository. Next, on your terminal window, within the repository run:

**flask run**

After registering for a free account you can use this application anywhere and anytime.  


