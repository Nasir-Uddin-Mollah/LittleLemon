Little Lemon API Paths
=======================

Menu API
--------
GET    http://127.0.0.1:8000/restaurant/menu/items/
POST   http://127.0.0.1:8000/restaurant/menu/items/
GET    http://127.0.0.1:8000/restaurant/menu/items/<id>/
PUT    http://127.0.0.1:8000/restaurant/menu/items/<id>/
PATCH  http://127.0.0.1:8000/restaurant/menu/items/<id>/
DELETE http://127.0.0.1:8000/restaurant/menu/items/<id>/

Booking API
-----------
GET    http://127.0.0.1:8000/restaurant/booking/tables/
POST   http://127.0.0.1:8000/restaurant/booking/tables/
GET    http://127.0.0.1:8000/restaurant/booking/tables/<id>/
PUT    http://127.0.0.1:8000/restaurant/booking/tables/<id>/
PATCH  http://127.0.0.1:8000/restaurant/booking/tables/<id>/
DELETE http://127.0.0.1:8000/restaurant/booking/tables/<id>/

Booking requests require this HTTP header:
Authorization: Token <token>

Authentication
--------------
POST   http://127.0.0.1:8000/restaurant/api-token-auth/
POST   http://127.0.0.1:8000/auth/token/login/
POST   http://127.0.0.1:8000/auth/token/logout/
POST   http://127.0.0.1:8000/auth/users/
GET    http://127.0.0.1:8000/auth/users/

Replace <id> with a menu or booking ID. The Django server must be running locally.
