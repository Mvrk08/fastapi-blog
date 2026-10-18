from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app =FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


blog = {
    "site": {
        "name": "FastAPI Blog",
        "tagline": "Thoughts, stories, and ideas.",
        "author": "Aman",
        "description": "A blog about FastAPI and Python web development."
    },

    "posts": {
        "post1": {
            "title": "Getting Started with FastAPI",
            "slug": "getting-started-with-fastapi",
            "author": "Aman",
            "date": "2026-10-10",
            "category": "FastAPI",
            "reading_time": 3,
            "excerpt": "Learn how to build your first API using FastAPI.",
            "content": "FastAPI is a modern Python framework for building APIs. It is easy to use, fast, and supports automatic API documentation. You can get started by installing FastAPI and running your application with Uvicorn.",
            "tags": ["FastAPI", "Python", "API"],
            "published": True
        },

        "post2": {
            "title": "Building Your First REST API",
            "slug": "building-your-first-rest-api",
            "author": "Aman",
            "date": "2026-10-11",
            "category": "Web Development",
            "reading_time": 4,
            "excerpt": "Understand how to create REST endpoints with FastAPI.",
            "content": "A REST API allows applications to communicate using HTTP methods such as GET, POST, PUT, and DELETE. FastAPI makes it simple to define endpoints, validate request data, and return JSON responses. Start with a simple GET route and gradually add more functionality.",
            "tags": ["REST API", "FastAPI", "Backend"],
            "published": True
        }
    }
}





@app.get("/",include_in_schema=False,name="home")
@app.get("/posts", include_in_schema=False,name="posts ")
def home(request:Request):
    return templates.TemplateResponse(request,"home.html",{"blogs":blog,"title":"home"})



@app.get("/api/posts")
def get_information():
    return blog["posts"]



@app.get("/api/posts")
def get_post():
    return blog["posts"]

