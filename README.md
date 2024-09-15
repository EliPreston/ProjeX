
# Projex

ProjeX is a little project webapp built with Django and TailwindCSS that I have been working on.

ProjeX allows anyone keep track of and share their different projects, the materials, and cost involved with each project. Additionally, once a user has signed up/logged in, they are able to follow users whose projects they like. When creating a project, users are also able to decide whether it is visible to anyone through choosing the "PUBLIC" tag, or only viewable by themselves by choosing the "PRIVATE" tag.

There is still a lot that I want to do in terms of cleaning up design elements, and it's missing features that I am either in the process of working on or plan on implementing as I move through my TODO list.


## Tech Stack

**Client:** Plain HTML & JS, TailwindCSS

**Server:** Django


## Run Locally

Clone the project

```bash
  git clone https://github.com/EliPreston/ProjeX.git
```

Go to the project directory

```bash
  cd ProjeX
```

Create & Activate virtual environment \
**If you don't have python3 installed, install that first**
```
  python3 -m venv .venv
  source .venv/bin/activate
```

Install dependencies
```bash
  pip install Django==5.1.1
```

Make migrations (to setup DB)
```bash
  python manage.py migrate
```

OPTIONAL: Create superuser -- lets you see backend at localhost:8000/admin once logged in
```bash
  python manage.py createsuperuser
```

Start local server (localhost:8000)
```bash
  python manage.py runserver
```

Open localhost:8000

## Features

**Implemented**:
- Account/user creation & login
- Creation of project(s) (barebones, needs work)
- Follow/Unfollow users
- Protected pages 
    - Users who are not logged in cannot create projects, view user's profiles, or view a project's page
    - Logged in users cannot view another user's projects that have been marked with the "PRIVATE" tag


**Planned/TODO**:
- User profile/account editing
- Project editing
- Ability to "Star" projects you like 
- Mark projects with tags "In Progress" or "Completed"
- Sorting/Filtering projects by tags (# of stars, completed vs in progress)
- Search projects
- Search users
- Display top starred projects on home page
