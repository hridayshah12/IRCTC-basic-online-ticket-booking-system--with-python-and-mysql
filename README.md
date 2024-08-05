IRCTC Basic Online Ticket Booking System with Python and MySQL

 
 Overview

This project is a basic online ticket booking system for IRCTC, developed using Python and MySQL. It allows users to book train tickets, order food, check train status using PNR, and manage their bookings. The system also includes a help section to guide users on how to use the portal.

 Features

- User Authentication: Users can register and log in to the portal.
- Ticket Booking: Users can book train tickets and receive a PNR.
- Food Booking: Users can order food along with their ticket bookings.
- Check Train Status: Users can check the status of their train using their PNR.
- Booking Management: Users can cancel, update, and search their booked tickets or food orders.
- Help Section: Provides guidance on how to use the portal.

 Setup and Installation

 Prerequisites

- Python 3.6.5
- MySQL Server
- mysql-connector-python library

 Installation Steps

1. Clone the Repository
   bash
   git clone https://github.com/yourusername/IRCTC-basic-online-ticket-booking-system.git
   cd IRCTC-basic-online-ticket-booking-system
   

2. Install Required Python Packages
   bash
   pip install mysql-connector-python
   

3. Set Up MySQL Database
   - Create a MySQL database and user.
   - Grant the user appropriate permissions.
   - Use the following SQL commands to set up the database schema:

     sql
     CREATE DATABASE irctc;
     USE irctc;

     CREATE TABLE user_record (
       username VARCHAR(30) PRIMARY KEY,
       password VARCHAR(30)
     );

     CREATE TABLE user_ticket (
       id INT PRIMARY KEY,
       name VARCHAR(50),
       age VARCHAR(4),
       sex VARCHAR(2),
       train VARCHAR(30),
       pnr VARCHAR(15)
     );

     CREATE TABLE user_food (
       id INT PRIMARY KEY,
       name VARCHAR(30),
       food_ordered VARCHAR(30)
     );
     

4. Update Database Configuration
   - Ensure the MySQL database connection details are correctly specified in your Python script.

     python
     db = mysql.connector.connect(
         host="localhost",
         user="your_username",
         passwd="your_password",
         charset="utf8",
         autocommit=True
     )
     

5. Run the Application
   bash
   python IRCTC_PORTAL.py
   



 Usage

- Register/Login: Users can register or log in to the portal.
- Book Tickets: Users can book train tickets and receive a PNR.
- Order Food: Users can order food with their ticket bookings.
- Check Train Status: Users can check the train status using their PNR.
- Manage Bookings: Users can cancel, update, or search their booked tickets or food orders.
- Help Section: Provides instructions on how to use the portal.

 Help

For any queries or assistance, refer to the help section within the portal.

 Contact

For any further information or queries, feel free to contact us at shahh6596@gmail.com.
