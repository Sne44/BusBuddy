# 🚌 BusBuddy: Full-Stack Bus Ticket Reservation System

![Python version 3.10+](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Django version 4.0+](https://img.shields.io/badge/Django-4.0+-092E20?style=for-the-badge&logo=django)
![Front-End HTML/CSS](https://img.shields.io/badge/Frontend-HTML%20%26%20CSS-E34F26?style=for-the-badge&logo=html5)
![Status: MVP Complete](https://img.shields.io/badge/Status-MVP%20Complete-success?style=for-the-badge)

## 🌟 Project Overview

**BusBuddy** is a complete, real-world proof-of-concept for a modern bus ticket reservation platform. Built entirely with **Django**, this project demonstrates proficiency in full-stack development, secure user authentication, complex relational data management, and the implementation of a functional e-commerce pipeline.

The application allows users to view available routes, book seats, simulate payment processing, and track all bookings via a personalized dashboard.

## ✨ Key Features & Technical Highlights

This project emphasizes robust backend architecture and professional best practices:

* **Full-Stack Architecture:** Developed the entire stack from database schema design to frontend templating.
* **Django ORM & Relational Design:** Implemented a structured database schema with models for `Route`, `Bus`, `Trip`, and `Booking`, demonstrating effective use of Foreign Keys and database migrations.
* **Secure Authentication & Authorization:** Utilizes Django's built-in system with custom authorization logic to ensure users can only access their personal booking history (`Booking.objects.filter(user=request.user)`).
* **E-commerce Workflow:** Created a multi-step booking pipeline:
    1.  Trip Selection (Bus List View)
    2.  Booking Creation (Initial record, `is_paid=False`)
    3.  Simulated Payment Gateway (Updates `is_paid=True`)
* **Personalized Dashboard:** A custom view allows logged-in users to review their paid and pending bookings in a responsive, tabular format.
* **Advanced Debugging:** Successfully resolved a critical model configuration error by refactoring Foreign Keys to use `settings.AUTH_USER_MODEL`, highlighting rigorous debugging methodology.

## 🛠️ Tech Stack

* **Backend Framework:** Django 4.x
* **Programming Language:** Python 3.x
* **Database:** SQLite (local development)
* **Frontend:** HTML5, CSS3, Django Templating Language (DTL)

## 🚀 Getting Started (Local Setup)

To run BusBuddy locally, follow these steps:

### 1. Clone the Repository

```bash
git clone [https://github.com/Sne44/BusBuddy.git](https://github.com/Sne44/BusBuddy.git)
cd BusBuddy
