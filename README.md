# NoteWave - Full-Stack Blog Application

NoteWave is a robust, full-stack blogging platform built with Python and the Django framework. The application features a complete user authentication system, categorized content management, and a responsive UI for a seamless writing and reading experience.

## 🚀 Features

- **User Authentication:** Secure Sign-up, Login, and Password Reset (via email simulation) functionality.
- **CRUD Operations:** Authenticated users can Create, Read, Update, and Delete their own blog posts.
- **Media Management:** Support for image uploads for blog covers.
- **Data Organization:** Relational database structure using Categories and Many-to-Many Tags.
- **Object-Level Permissions:** Strict logic ensures users can only edit or delete content they created.
- **Responsive Design:** Fully mobile-friendly interface built with Bootstrap 5 and custom CSS.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Forms:** Django-Crispy-Forms (Bootstrap 4 pack)
- **Database:** SQLite (Development)
- **Styling:** Custom CSS with Glassmorphism effects

## 📂 Project Structure

- `blog/`: Project configuration and URL routing.
- `posts/`: Core application logic, including blog models, views, and templates.
- `users/`: User management, profile updates, and authentication views.
- `media/`: Storage for user-uploaded blog images.

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/notewave-blog.git](https://github.com/your-username/notewave-blog.git)
   cd notewave-blog
