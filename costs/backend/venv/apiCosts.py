from unicodedata import category
from fastapi import FastAPI 
import uvicorn 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import psycopg2


app = FastAPI()

conn = psycopg2.connect(
    dbname="db_costs_api",
    user="postgres",
    password="3867",
    host="localhost"
)

def create_projects_table():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM   information_schema.tables 
            WHERE  table_schema = 'public'
            AND    table_name = 'projects'
        )
    """)
    table_exists = cursor.fetchone()[0]

    if table_exists:
        print("Tabela já existe.")
    else:
        cursor.execute("""
            CREATE TABLE projects (
                id SERIAL PRIMARY KEY,
                name_client VARCHAR(255),
                name_project VARCHAR(255) NOT NULL,
                budget NUMERIC NOT NULL,
                category_id INTEGER NOT NULL, 
                category_name VARCHAR(255) NOT NULL
            )
        """)
        conn.commit()
        print("Tabela criada.")


create_projects_table()

class Category(BaseModel):
    id: int
    name: str

class Project(BaseModel):
    id: int
    name_client: str
    name_project: str
    budget: float
    category: Category
    
projects = []

categories = [
    {"id": 1, "name": "Infra"},
    {"id": 2, "name": "Desenvolvimento"},
    {"id": 3, "name": "Design"},
    {"id": 4, "name": "Planejamento"}
]

@app.get("/projects", response_model=List[Project])
async def read_projects():
    cursor = conn.cursor()
    cursor.execute("SELECT id, COALESCE(name_client, 'Desconsiderar') AS name_client, name_project, budget, category_id, category_name FROM projects;")
    projects = []
    for project_data in cursor.fetchall():
        id, name_client, name_project, budget, category_id, category_name = project_data     
        category = Category(id=category_id, name=category_name)
        project = Project(id=id, name_client=name_client, name_project=name_project, budget=budget, category=category)
        projects.append(project)
    return projects


@app.post("/projects")
def create_project(project: Project):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (name_client, name_project, budget, category_id, category_name) VALUES (%s, %s, %s, %s, %s)", (project.name_client, project.name_project, project.budget, project.category.id, project.category.name))
    conn.commit()
    return projects

@app.get("/categories", response_model=List[Category])
async def read_categories():
    return categories

# Permite solicitações de qualquer origem (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, port=5000)