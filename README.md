# Event & Workshop Management System
## Milestone 4 – Authentication, User Accounts, and Security

---

> **Starter Repository**
> This repository is the base for Milestone 4. Clone it, add your updated Django project files, and continue building on top of your previous work. Your Milestone 3 project should already include:
> - Templates
> - Event forms
> - Event registration
> - Database-backed event pages
> - Working navigation and layouts

---

# 1. Overview

In Milestone 3, you built:
- Django templates
- Template inheritance
- Event forms
- Registration forms
- POST request handling
- Database-backed workflows

In Milestone 4, you will add user authentication and security features using Django’s built-in authentication system.

By the end of this Milestone, users should be able to:
- Create accounts
- Log in
- Log out
- Access protected pages
- Associate created content with authenticated users

This Milestone introduces one of the most important concepts in modern web development:
- user identity
- access control
- protected routes
- authenticated workflows

Your application will now begin functioning like a true multi-user web platform.

---

# 2. Learning Objectives

By completing this Milestone, you should be able to:

- Create user accounts with Django authentication
- Log users in and out
- Use Django’s built-in User model
- Protect views using authentication decorators
- Restrict application features to authenticated users
- Display different content based on authentication status
- Associate database records with users
- Understand basic authentication security concepts
- Continue using Git and GitHub workflows

---

# 3. AI Usage Expectations

Artificial Intelligence (AI) tools are permitted and encouraged for this project when used appropriately.

You may use:
- ChatGPT
- Claude
- Gemini
- Copilot Chat
- Other instructor-approved AI chat tools

You are expected to:
- Read and understand all submitted code
- Test AI-generated suggestions
- Evaluate AI responses critically
- Make your own decisions about what to keep or reject
- **Use AI tools and the official Django documentation to determine how to implement tasks that are not fully detailed in this README.** This is intentional. Part of this milestone is practicing how to find, evaluate, and apply technical guidance on your own.

You may NOT:
- Submit code you cannot explain
- Blindly copy AI-generated code
- Use AI as a replacement for learning

---

# 4. Project Scenario

Your Event & Workshop Management System currently allows visitors to:
- View events
- Add events
- Register for events

In this Milestone, users should:
- Create accounts
- Log in and log out
- Access protected pages
- Create events only while logged in
- View ownership information associated with events or registrations

You will use Django’s built-in authentication system instead of creating your own password system manually.

---

# 5. Set Up Your Local Repository

Clone this starter repository:

```bash
git clone <your-repository-url>
cd <repository-folder>
```

Bring your working Milestone 3 project into this repository before continuing.

---

## Adding Your Milestone 3 Files

This repository is a base — you need to bring in a working Django project from Milestone 3 before continuing.

You have two options:

### Option A — Copy your own Milestone 3 files (5 points extra credit)

Copy your completed Milestone 3 project into this repository.

### Option B — Request starter files from the instructor

If you do not have working Milestone 3 files, request starter files from your instructor.

---

## Activate Your Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install Django if needed:

```bash
pip install django
```

---

# 6. Authentication Overview

Django includes a built-in authentication system that already provides:
- User accounts
- Password hashing
- Login handling
- Logout handling
- Session management
- Authentication decorators

You will use Django’s built-in system rather than building authentication manually.

This is important because:
- password security is difficult
- storing plain-text passwords is dangerous
- Django’s authentication system is already secure and well-tested

---

# 7. Create a Registration Page

Users should be able to create accounts. To do this you will need three things working together: a form, a view, and a URL entry. You will also need a template to render the registration page. Use the Django documentation or an AI tool to see how to connect all three.

---

## Create a Registration Form

Open:

```text
events/forms.py
```

Add:

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
```

---

# 8. Add Login and Logout

Django already includes built-in login and logout views. You do not need to write these views yourself.

Hints to get you started:
- In `urls.py`, you can include Django's built-in auth URLs using `django.contrib.auth.urls`
- In `settings.py`, set `LOGIN_REDIRECT_URL` to control where users land after logging in
- In `settings.py`, set `LOGOUT_REDIRECT_URL` to control where users land after logging out

Use the Django documentation or an AI tool to see how to wire these into your project.

---

# 9. Protect the Add Event View

Only logged-in users should be allowed to create events.

Hints to get you started:
- Import `login_required` from `django.contrib.auth.decorators`
- Apply the `@login_required` decorator directly above your view function
- You can optionally set `login_url` in the decorator to control where unauthenticated users are redirected

Use the Django documentation or an AI tool to see the full syntax and options.

---

# 10. Required Security Checks

Your project MUST include:
- Passwords handled through Django authentication
- CSRF protection on forms
- Protected Add Event view
- Authentication-based navigation
- Proper login/logout functionality

> **Note on CSRF:** Django handles CSRF protection automatically. You simply need to include `{% csrf_token %}` inside every HTML `<form>` tag in your templates. No additional configuration is required.

---

# 11. Submission Requirements

## REQUIRED Deliverables

Your submitted project MUST include:
- Working user registration
- Working login/logout
- Protected Add Event page
- Authentication-aware navigation
- User-linked event creation
- GitHub commit history (provided in GitHub)

### Implementation Hints

**Authentication-aware navigation** — In your templates, use `{% if user.is_authenticated %}` to show or hide navigation links such as Login, Logout, and Add Event based on whether a user is signed in.

**User-linked event creation** — When saving a new event, assign the logged-in user to the record before calling `.save()`. Access the current user through `request.user`. Use the Django documentation or an AI tool to see how to assign a ForeignKey to `request.user` in a view.

---

# 12. Reflection and AI Interaction Log

Update `interaction.log` and `reflection.txt` with your experience completing this milestone. Your reflection should be thoughtful and specific. Consider addressing the following questions:

- What did you find most difficult about implementing authentication?
- Which part of this milestone took the most time, and why?
- How did you use AI tools during this assignment? Were the suggestions accurate? Did you have to evaluate or correct anything?
- What would you do differently if you were starting this milestone over?
- What does it mean for a route or view to be "protected," and why does it matter?

---

# 13. Optional Deployment Assignment

This optional assignment is worth 10 points.

For this assignment, deploy your Django application to a public hosting service. A good beginner-friendly option is Render.com. Be aware that deployment can take time because of build steps, database setup, static file configuration, and occasional platform delays.

If you prefer a different hosting provider, you may use another low-cost service in the roughly $5 to $10 per month range that supports Django and MySQL hosting. Use your own research or AI tools to compare options and choose a service that fits your needs. The goal is to give you real deployment experience without making the assignment dependent on one specific vendor.

To complete this assignment successfully, your deployed application should:
- Be reachable online
- Allow registration, login, and logout in the hosted environment
- Continue to support database-backed features after deployment
- Load static files and templates correctly

Remember that deployment is optional and should only be attempted after all other work for this assignment is complete.

---

# 14. Looking Ahead

In future improvements, you could:
- Add email notifications
- Create API endpoints
- Add role-based permissions
- Build richer user dashboards
