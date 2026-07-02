# CTZ Hands-on Experiments

**Sri Harish B** | **212223220110**

Hands-on work covering backend web frameworks and database systems --
building a Course Management System from a single Django app up through
REST APIs and framework comparisons, alongside a parallel track of
relational database exercises.

## Repository Layout

```
CTZ_Hands-on-Experiments/
├── Backend/
│   ├── Handson_01_Django_Project_Setup/
│   ├── Handson_02_Django_Models_ORM_Admin/
│   ├── Handson_03_Django_REST_Framework/
│   ├── Handson_04_Flask_Basics/
│   └── Handson_05_Flask_SQLAlchemy/
└── Database/
    ├── Hand_on-1/   Database design & normalisation
    ├── Hand_on-2/   DML, filtering, joins & aggregation
    ├── Hand_on-3/   Subqueries, views, stored procedures & transactions
    └── Hand_on-4/   Query performance & indexing
```

## Backend

The same Course Management domain (Departments, Courses, Students,
Enrollments) is rebuilt across frameworks, with each hands-on extending
the previous one:

| # | Topic | Stack |
|---|-------|-------|
| 1 | Web framework foundations & Django project setup | Django |
| 2 | Django models, ORM & admin interface | Django, SQLite |
| 3 | Django REST views, serializers & viewsets | Django REST Framework |
| 4 | Flask app structure, routing & blueprints | Flask |
| 5 | Flask with SQLAlchemy ORM | Flask, SQLAlchemy |

Each folder has its own README with setup steps, endpoints and learning
outcomes for that hands-on.

## Database

| # | Topic | Stack |
|---|-------|-------|
| 1 | Database design & normalisation (1NF/2NF/3NF) | PostgreSQL / MySQL |
| 2 | DML, filtering, joins & aggregation | PostgreSQL / MySQL |
| 3 | Subqueries, views, stored procedures & transactions | PostgreSQL / MySQL |
| 4 | Query performance & indexing, N+1 problem | PostgreSQL, psycopg2 |

## Notes

Every folder is self-contained with its own `requirements.txt` (where
applicable) and `.gitignore`. Virtual environments and database files are
not tracked -- each hands-on's README covers the setup and run commands
needed to bring it up locally.

