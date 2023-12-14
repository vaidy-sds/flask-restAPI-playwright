# flask-restAPI


Goals
- [x] Create Rest API with Flask
- [x] Create a docker image
- [ ] Flask smorest integration
- [ ] Sqlalchemy integration
- [ ] JWT authentication
- [ ] Alembic & Flask-Migrate integration
- [ ] Automate API tests with Playwright
- [ ] CI/CD integration with git actions


Docker commands:
docker build -t flask-smorest-api .
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api
```