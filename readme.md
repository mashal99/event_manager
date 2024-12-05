Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

Welcome to the Event Manager Company! This document outlines the steps I followed to complete the assignment objectives, which included improving the project, resolving critical issues, and increasing test coverage. Below are the details of my journey, along with links to each resolved issue.

Steps to Complete the Assignment

1. Setup and Familiarization
Forked and Cloned Repository: Forked the Event Manager Repository and cloned it locally.
Docker Setup: Configured the project using Docker. Verified the application by accessing:
API Documentation at http://localhost/docs.
Database via PGAdmin at http://localhost:5050.
Codebase Exploration: Analyzed key files including user_routes.py, user_service.py, and user_model.py. Used Swagger UI to explore API endpoints and functionality.
2. Resolving Issues
Below are the issues I resolved as part of the assignment, along with the approach taken:

1. Username Validation

Problem: Improper validation allowed invalid usernames (e.g., containing special characters or exceeding length constraints).
Solution: Enhanced validation logic in user_schemas.py to enforce stricter rules. Added tests for edge cases in test_user_routes.py.
Issue Link: #1 - Username Validation
2. Password Validation

Problem: Passwords were not following best security practices (e.g., lacking complexity requirements).
Solution: Implemented password strength validation in user_service.py. Added checks for minimum length and complexity (uppercase, lowercase, numbers, special characters).
Issue Link: #2 - Password Validation
3. Profile Field Edge Cases

Problem: Simultaneous or partial updates to profile fields (e.g., bio, profile picture) caused inconsistencies.
Solution: Improved logic in user_service.py to handle partial updates. Enhanced error handling for edge cases.
Issue Link: #3 - Profile Field Edge Cases
4. OAuth Token Generation

Problem: Tokens were not being generated correctly under certain conditions.
Solution: Fixed logic in oauth.py and jwt_service.py to ensure proper token creation and expiration handling.
Issue Link: #4 - OAuth Token Generation Issue
5. Test Coverage Improvement

Problem: Existing tests lacked coverage for critical scenarios.
Solution: Wrote additional unit tests and integration tests, increasing test coverage to 90%. Verified the tests using pytest --cov=app tests/.
Issue Link: #5 - Test Coverage Improvement
6. Instructor Video Issue

Problem: Resolved the specific issue demonstrated in the instructor video regarding user profile updates.
Solution: Debugged and corrected logic in user_service.py. Added corresponding tests in test_user_routes.py.
Issue Link: #6 - Instructor Video Issue
3. Testing and Database Management
Ran Tests: Executed the test suite using:
docker compose exec fastapi pytest
Increased Test Coverage: Used coverage tools to identify untested code and implemented new tests to achieve 90% coverage.
Database Management: Dropped and re-ran migrations to ensure a clean schema:
docker compose exec fastapi alembic upgrade head
4. Collaboration and Git Workflow
GitHub Issues: Enabled GitHub issues to track progress for each task.
Branching and Pull Requests:
Created branches for each issue using git checkout -b <branch-name>.
Merged changes into the main branch via pull requests.
Documentation: Documented issues, resolutions, and testing outcomes for easy reference.
Reflection on the Assignment

This assignment was a tremendous learning experience. It helped me:

Strengthen Technical Skills: Working with FastAPI, SQLAlchemy, and Docker deepened my understanding of REST API development and database migrations.
Improve Testing Practices: Writing comprehensive tests for edge cases and integrating pytest for test automation improved the project's reliability and my debugging skills.
Embrace Collaboration: Using GitHub for issue tracking and pull requests honed my version control and team collaboration skills.
Challenges like debugging the token generation logic and handling database inconsistencies pushed me to think critically and improve my problem-solving abilities. Overall, this assignment was an invaluable step toward becoming a proficient software developer.

Links to Issues

#1 - Username Validation
#2 - Password Validation
#3 - Profile Field Edge Cases
#4 - OAuth Token Generation Issue
#5 - Test Coverage Improvement
#6 - Instructor Video Issue
Project Deployment

Find the DockerHub deployment image here.