# Flight Reservation System 

A comprehensive flight reservation and management system built with Python and MySQL. This application allows users to manage flight bookings, passenger information, food orders, and luggage services.

## Project Overview

The **Flight Reservation System** is designed to handle various airline operations including passenger registration, flight management, food ordering, and baggage management. The system connects to a MySQL database to store and retrieve passenger and flight information.

## Features

### User Management
- **Account Creation**: Create new user accounts with validation
  - Name validation
  - Email validation (proper format checking)
  - Phone number validation (10 digits)
  - Password validation (minimum 6 characters)
- **User Login**: Secure login with email and password authentication

### View Records
- **Passenger Arrival/Departure List**: Display all registered passengers with their flight details
- **Available Flights**: Browse available flights in the system
- **Food Menu**: View all available food items with prices
- **Ticket Prices**: Display ticket pricing for different classes
  - Economy Class: AED 2500 per person
  - Business Class: AED 4067 per person
  - First Class: AED 5960 per person
- **Baggage Allowances**: Display permissible weights by class
  - Economy Class: 30kg
  - Business Class: 35kg
  - First Class: 40kg

### Edit Records
- **Add New Passenger**: Register passengers with complete information
  - Passenger ID, name, DOB, email, phone, address
  - Departure and arrival locations
  - Flight selection
  - Ticket class selection
  - Food ordering
- **Add Extra Luggage**: Add additional baggage for passengers with extra charges
  - 5kg additional: AED 150
  - 10kg additional: AED 300
  - 15kg additional: AED 500
- **Food Menu Management**:
  - Add new food items with prices
  - Delete food items from the menu

### Data Visualization
- **Food Price Distribution Chart**: Pie chart showing the price range distribution of available food items

## Technical Stack

- **Language**: Python 3.x
- **Database**: MySQL
- **Libraries**:
  - `mysql-connector-python`: Database connectivity
  - `matplotlib`: Data visualization
  - `tabulate`: Formatted table display

## Database Requirements

The system requires the following MySQL database and tables:

### Database Connection Details
```
Host: localhost
User: root
Password: 123
Database: flight_reservation_system
Port: 3306
```

### Required Tables
1. **login**: User account information
2. **passenger**: Basic passenger flight information
3. **passenger_details**: Detailed passenger information
4. **flights**: Available flight information
5. **food**: Available food items on the menu

## Installation & Setup

### Prerequisites
- Python 3.x installed
- MySQL server running locally
- Required Python packages

### Installation Steps

1. **Clone or download the project**
```bash
cd "Flight management system"
```

2. **Install required dependencies**
```bash
pip install mysql-connector-python matplotlib tabulate
```

3. **Set up MySQL Database**
- Ensure MySQL is running on localhost
- Create database named `flight_reservation_system`
- Tables will be auto-created on first run

4. **Run the application**
```bash
python "Flight reservation system.py"
```

## Usage

### First-Time Users
1. Run the application
2. Select "N" (No) when asked if you have an account
3. Create a new account with your details
4. Log in with your credentials

### Main Menu Options
```
1. View Records
   - View passenger lists, flights, food menu, and pricing
   
2. Edit Records
   - Add new passengers
   - Add extra luggage
   - Manage food menu
   
3. Quit
   - Exit the application
```

## Available Food Items

The system includes diverse food options with varying price points:
- Hash brown + Salad
- Meatballs + Spaghetti
- Chicken biryani
- Club sandwich
- Cup noodles
- Ramen noodles
- Caesar salad
- Green salad
- Samosa chat
- Chocolate pudding
- Cut fruits
- Pastries
- Brownies

## Key Functions

| Function | Purpose |
|----------|---------|
| `create_login()` | Initialize login table |
| `createacc()` | Register new user account |
| `login()` | Authenticate user |
| `add_passenger()` | Add new passenger record |
| `add_food()` | Add food item to menu |
| `delete_food()` | Remove food item from menu |
| `luggagebill()` | Calculate and add luggage charges |
| `ViewRecords()` | Display system information |
| `EditRecords()` | Modify system data |

## Data Validation

The system includes comprehensive input validation:
- **Names**: Required, non-empty strings
- **Email**: Must contain '@' and valid domain
- **Phone**: Must be exactly 10 digits
- **Passwords**: Minimum 6 characters
- **Dates**: YYYY-MM-DD format validation
- **IDs**: Numeric validation

## File Structure

```
Flight management system/
├── Flight reservation system.py  # Main application file
├── Source code SQL.pdf           # Database schema reference
└── README.md                     # This file
```

## Notes

- The system validates all user inputs to prevent invalid data entry
- All data is persisted in the MySQL database
- The application includes error handling for database operations
- Users can navigate back to the main menu from most operations
- Ticket prices and luggage allowances are pre-defined

## Security Considerations

- Passwords are stored in the database (consider hashing for production)
- Email and password validation is performed client-side
- SQL injection risks exist in current implementation (use parameterized queries in production)

## Future Enhancements

- Implement password hashing for better security
- Add flight search and filtering options
- Implement booking cancellations
- Add payment gateway integration
- Create admin dashboard
- Generate booking confirmations via email
- Add user profile management

## Troubleshooting

### Database Connection Error
- Ensure MySQL server is running
- Verify connection credentials in the code
- Check that the database exists

### Missing Tables
- Tables are auto-created on first run
- If tables don't exist, restart the application

### Python Dependencies
```bash
pip install --upgrade mysql-connector-python matplotlib tabulate
```

## License

This project is for educational purposes.

---

**Project Name**: Flight Reservation System - Emirates Airlines  
**Created**: 2026  
**Version**: 1.0

