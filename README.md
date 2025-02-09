Django Restaurant API
This is a Django-based restaurant project that allows users to register, login, view the menu, place orders, and receive AI-powered recommendations. Admins can manage the food menu and orders.
Features
- User Authentication (JWT-based login)
- Menu Management (Admin-only)
- Order Management (Customers can place orders, Admins can update order status)
- AI-Powered Recommendations
Setup Instructions
Prerequisites
- Docker
- Docker Compose
- Python 3.9+
- PostgreSQL

1. Clone the Repository & Start Docker
git clone https://github.com/gokulraj1990/restaurant.git
cd restaurant-api
docker-compose up --build -d  # Build and run in detached mode

2. Run Migrations & Create Superuser
docker exec -it restaurant-web python manage.py migrate
docker exec -it restaurant-web python manage.py createsuperuser

Superuser Details:
• Username: admin
• Email: admin@example.com
• Password: adminpass
• Bypass password validation: y

Admin Capabilities
• Manage users
• Add, update, and delete food items
• View all orders
• Update order status
• Get food recommendations
• Logout

Customer Capabilities
• Register an account
• Login to the system
• View and browse menu items
• Place an order
• View order history and status
• Get food recommendations
• Logout

API Endpoints
Register User (Customer Only) (POST)
**URL**: `http://127.0.0.1:8000/api/register/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Body** (JSON or Form-Data):
[{'username': 'testuser', 'password': 'testpassword', 'email': 'test@example.com'}]
**Expected Response**: `201 Created`
{'id': 1, 'username': 'testuser', 'email': 'test@example.com', 'is_customer': True, 'is_admin': False}

Login & Get JWT Token (POST)
**URL**: `http://127.0.0.1:8000/api/login/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Body** (JSON or Form-Data):
[{'username': 'admin', 'password': 'adminpass'}]
**Expected Response**: `200 OK`
{'message': 'Login successful'}

View User Profile (GET)
**URL**: `http://127.0.0.1:8000/api/users/me/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Expected Response**: `200 OK`
{'id': 1, 'username': 'testuser', 'email': 'test@example.com', 'profile_picture': None}

List All Food Items (GET)
**URL**: `http://127.0.0.1:8000/api/food-items/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Expected Response**: `200 OK`
[{'id': 1, 'name': 'Burger', 'description': 'Juicy beef burger', 'price': 5.99, 'category': 'Fast Food'}]

Add Food Item (Admin Only) (POST)
**URL**: `http://127.0.0.1:8000/api/food-items/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Body** (JSON or Form-Data):
[{'name': 'Burger', 'description': 'Juicy beef burger', 'price': 5.99, 'category': 'Fast Food'}]
**Expected Response**: `201 Created`
{'id': 1, 'name': 'Burger', 'description': 'Juicy beef burger', 'price': 5.99, 'category': 'Fast Food', 'image': 'http://127.0.0.1:8000/media/food_images/burger.jpg'}

Update Food Item (Admin Only) (PUT)
**URL**: `http://127.0.0.1:8000/api/food-items/1/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Body** (JSON or Form-Data):
[{'name': 'Cheeseburger', 'description': 'Delicious cheeseburger', 'price': 6.99}]
**Expected Response**: `200 OK`
{'id': 1, 'name': 'Cheeseburger', 'description': 'Delicious cheeseburger', 'price': 6.99}

Place an Order (Customer Only) (POST)
**URL**: `http://127.0.0.1:8000/api/orders/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Body** (JSON or Form-Data):
[{'food_items': [1], 'quantity': 2}]
**Expected Response**: `201 Created`
{'id': 1, 'customer': 'testuser', 'status': 'Pending', 'total_price': 11.98}

List Orders (GET)
**URL**: `http://127.0.0.1:8000/api/orders/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Expected Response**: `200 OK`
[{'id': 1, 'customer': 'testuser', 'status': 'Pending', 'total_price': 11.98}]

Update Order Status (Admin Only) (PATCH)
**URL**: `http://127.0.0.1:8000/api/orders/1/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Body** (JSON or Form-Data):
[{'status': 'Completed'}]
**Expected Response**: `200 OK`
{'id': 1, 'customer': 'testuser', 'status': 'Completed', 'total_price': 11.98}

Get Food Recommendations (GET)
**URL**: `http://127.0.0.1:8000/api/recommendations/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Expected Response**: `200 OK`
[{'id': 3, 'name': 'Pizza', 'description': 'Best-selling pizza', 'price': 10.99}]

Logout (Clear JWT Cookies) (POST)
**URL**: `http://127.0.0.1:8000/api/logout/`
**Headers**:
- Content-Type: application/json
- Include Cookies
**Expected Response**: `200 OK`
{'message': 'Logged out successfully'}
