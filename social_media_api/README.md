## API Endpoints

### Posts
- `GET /api/posts/`: List all posts.
- `POST /api/posts/`: Create a new post.
- `GET /api/posts/{id}/`: Retrieve a post by ID.
- `PUT /api/posts/{id}/`: Update a post.
- `DELETE /api/posts/{id}/`: Delete a post.

### Comments
- `GET /api/comments/`: List all comments.
- `POST /api/comments/`: Create a new comment.
- `GET /api/comments/{id}/`: Retrieve a comment by ID.
- `PUT /api/comments/{id}/`: Update a comment.
- `DELETE /api/comments/{id}/`: Delete a comment.

## Features
- **Pagination:** Enabled for posts and comments.
- **Search:** Available for posts (search by `title` or `content`).
### Follow Management
- **Follow a User:** `POST /accounts/follow/<user_id>/`
- **Unfollow a User:** `POST /accounts/unfollow/<user_id>/`
### Feed
- **Get User Feed:** `GET /posts/feed/`

POST /posts/<int:pk>/like/      - Like a post
POST /posts/<int:pk>/unlike/    - Unlike a post
GET  /notifications/            - Fetch unread notifications
POST /notifications/<int:pk>/read/ - Mark notification as read

Request: POST /posts/1/like/
Response: {"message": "Post liked successfully"}
