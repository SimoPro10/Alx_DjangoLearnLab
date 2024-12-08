# Authentication System Documentation

## Overview
This system enables users to register, log in, log out, and manage their profiles.

## Features
- User registration with email validation.
- Secure login and logout.
- Profile management.

## URLs
- `/register` - User registration page.
- `/login` - Login page.
- `/logout` - Logout page.
- `/profile` - Profile management page.

## Testing
- Ensure all views render correctly.
- Validate user data on form submissions.
- Confirm CSRF protection.

## Security Notes
- Passwords are hashed using Django’s default hashing mechanism.
- CSRF tokens protect against attacks.
