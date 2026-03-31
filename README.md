# Campuz - Modern Academic Communication Platform

![Campuz Logo](https://via.placeholder.com/150x50/7C3AED/EC4899?text=Campuz)

> All-in-one Academic Platform for Modern Colleges

Campuz is a comprehensive academic communication and management platform designed specifically for Indian colleges. It unifies fragmented academic systems by combining attendance tracking, marks management, fees, communication, and updates into a single, modern platform with an Instagram-inspired UI.

## 🎯 Core Vision

Campuz solves the problems of fragmented academic systems, communication gaps, and outdated interfaces by providing a unified, visually appealing platform that feels like modern social media but is built specifically for academic and institutional use.

## 🧱 Tech Stack

- **Frontend**: HTML5, Tailwind CSS, JavaScript (ES6+)
- **Backend**: Django (Python) with Django REST Framework
- **Database**: MongoDB (using Djongo for Django integration)
- **Authentication**: JWT-based authentication
- **API**: RESTful APIs
- **Styling**: Tailwind CSS with custom design system

## 🎨 Design System

- **Theme**: Dark Mode (default)
- **Primary Colors**: Purple (#7C3AED), Pink (#EC4899)
- **Background**: Deep dark (#0F172A or #020617)
- **Accent Gradients**: Purple → Pink
- **Typography**: Inter (modern sans-serif)
- **UI Inspiration**: Instagram-style layout with cards, rounded edges
- **Design Elements**:
  - Soft shadows
  - Glassmorphism effects (subtle blur + transparency)
  - Smooth hover animations
  - Rounded corners (xl)
  - Minimalist icons

## 📱 Key Features

### 1. Landing Page
- Hero section with compelling tagline
- Problem/solution showcase
- Features grid with icons
- Call-to-action buttons for Login/Register
- Gradient highlights and animations

### 2. Authentication System
- JWT-based authentication
- Role-based access (Student, Faculty, Admin)
- Clean UI with floating labels
- Secure password handling

### 3. User Dashboard
- Personalized dashboard for each user role
- Academic information display
- Notifications panel
- Profile summary cards
- Hover animations and modern UI

### 4. Academic Feed
- Instagram-style vertical scrolling feed
- Post types: Notices, Events
- Interactive features: Like, Comment, Save
- Clean post cards with timestamps and icons

### 5. AI College Bot
- Chat interface for academic queries
- Message bubbles and input box
- Scrollable conversation UI
- Dummy responses (ready for AI integration)

### 6. Advanced Search Panel
- Search functionality for Students, Faculty, Departments
- Role-based access restrictions
- Admin/HOD privileged views

### 7. Admin Panel
- User management
- Post and announcement management
- Role-based access control
- Clean dashboard with tables and actions

### 8. Additional Features
- Notification system with bell icon dropdown
- Dark mode toggle (default dark)
- Smooth animations (fade, slide, scale)
- Optimized performance
- Reusable components

## 🗄️ Database Schema (MongoDB Collections)

### Users Collection
```json
{
  "_id": ObjectId,
  "name": "String",
  "email": "String (unique)",
  "role": "String (student|faculty|admin)",
  "department": "String",
  "enrollment_no": "String (optional)",
  "password": "String (hashed)",
  "created_at": "DateTime",
  "profile_image": "String (optional)"
}
```

### Posts Collection
```json
{
  "_id": ObjectId,
  "title": "String",
  "content": "String",
  "type": "String (notice|event)",
  "author_id": "ObjectId (ref: Users)",
  "created_at": "DateTime",
  "likes": ["ObjectId (ref: Users)"],
  "comments": [{
    "user_id": "ObjectId (ref: Users)",
    "content": "String",
    "created_at": "DateTime"
  }],
  "saved_by": ["ObjectId (ref: Users)"]
}
```

### Departments Collection
```json
{
  "_id": ObjectId,
  "name": "String",
  "hod_id": "ObjectId (ref: Users)",
  "description": "String (optional)"
}
```

### Messages Collection (Bot)
```json
{
  "_id": ObjectId,
  "user_id": "ObjectId (ref: Users)",
  "message": "String",
  "response": "String",
  "timestamp": "DateTime"
}
```

### AcademicRecords Collection
```json
{
  "_id": ObjectId,
  "user_id": "ObjectId (ref: Users)",
  "subjects": [{
    "name": "String",
    "marks": "Number",
    "attendance": "Number (%)"
  }],
  "fees": {
    "total": "Number",
    "paid": "Number",
    "pending": "Number"
  },
  "semester": "String"
}
```

## 📁 Project Structure

```
campuz-application/
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
├── academics/                   # Academic management app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── migrations/
├── backend/                     # Backend configuration (if separate)
├── bot/                         # AI College Bot app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── serializers.py
├── campuz/                      # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── frontend/                    # Frontend assets
│   ├── index.html              # Landing page
│   ├── dashboard.html          # User dashboard
│   ├── feed.html               # Academic feed
│   ├── js/                     # JavaScript files
│   │   ├── api.js
│   │   ├── auth.js
│   │   ├── dashboard.js
│   │   └── feed.js
│   └── styles/                 # Additional styles (if needed)
├── posts/                       # Posts management app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── migrations/
└── users/                       # User management app
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── serializers.py
    ├── permissions.py
    └── migrations/
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- MongoDB (local installation or cloud instance like MongoDB Atlas)
- Git
- Modern web browser

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd campuz-application
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **MongoDB Setup:**
   - Install MongoDB locally or use MongoDB Atlas
   - Create a database named `campuz_db`
   - Update database settings in `campuz/settings.py`

5. **Django Configuration:**
   - Navigate to the project root
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

6. **Create superuser (Admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data (optional):**
   ```bash
   python manage.py loaddata sample_data.json
   ```

### Frontend Setup

The frontend is built with vanilla HTML, CSS (Tailwind), and JavaScript. No additional setup required beyond serving the static files.

### Running the Application

1. **Start Django development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   - Frontend: Open `http://127.0.0.1:8000/frontend/index.html`
   - API endpoints: `http://127.0.0.1:8000/api/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📡 API Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration
- `POST /api/auth/refresh/` - Refresh JWT token

### Users
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile
- `GET /api/users/search/` - Search users (role-based)

### Posts
- `GET /api/posts/` - Get all posts (feed)
- `POST /api/posts/` - Create new post
- `GET /api/posts/{id}/` - Get specific post
- `PUT /api/posts/{id}/` - Update post
- `DELETE /api/posts/{id}/` - Delete post
- `POST /api/posts/{id}/like/` - Like/unlike post
- `POST /api/posts/{id}/comment/` - Add comment

### Academic Records
- `GET /api/academics/records/` - Get academic records
- `POST /api/academics/records/` - Create academic record
- `PUT /api/academics/records/{id}/` - Update record

### Bot
- `POST /api/bot/chat/` - Send message to bot
- `GET /api/bot/history/` - Get chat history

### Admin
- `GET /api/admin/users/` - Manage users
- `GET /api/admin/posts/` - Manage posts
- `GET /api/admin/departments/` - Manage departments

## 🧪 Sample Data

The application includes sample data for testing:

### Demo Users
- **Admin**: admin@campuz.edu (password: admin123)
- **Faculty**: faculty@campuz.edu (password: faculty123)
- **Student**: student@campuz.edu (password: student123)

### Sample Content
- Pre-loaded posts and notices
- Academic records for demo users
- Department information
- Bot conversation examples

## 🔧 Development

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Comment complex logic

### Testing
```bash
# Run Django tests
python manage.py test

# Run with coverage
coverage run manage.py test
coverage report
```

### Linting
```bash
# Install and run flake8
pip install flake8
flake8 .
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Ensure all tests pass
- Update documentation for new features
- Follow the existing code style
- Add tests for new functionality

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by modern social media platforms
- Built for the academic community
- Special thanks to the Django and MongoDB communities

## 📞 Support

For support, email support@campuz.edu or create an issue in the repository.

---

**Built with ❤️ for modern education**
