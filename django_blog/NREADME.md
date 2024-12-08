# Blog Post Management

## Features
1. View all blog posts.
2. View detailed blog posts.
3. Create, edit, and delete posts (authenticated users only).

## URL Patterns
- `/` - List all posts.
- `/post/<int:pk>/` - View post details.
- `/post/new/` - Create a new post.
- `/post/<int:pk>/edit/` - Edit a post (author only).
- `/post/<int:pk>/delete/` - Delete a post (author only).

## Permissions
- Only authenticated users can create posts.
- Only post authors can edit or delete their posts.
