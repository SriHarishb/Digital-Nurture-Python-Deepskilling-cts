# Hands-On 1 -- Database Design & Normalisation

**Sri Harish B**

## Files
- `task1.sql` -- creates `college_db` and the core tables (departments, students, courses, enrollments, professors)
- `task2.sql` -- verifies the schema against 1NF, 2NF and 3NF
- `task3.sql` -- alters and extends the schema (new columns, constraints)

## Setup
```bash
psql -U postgres -f task1.sql
psql -U postgres -d college_db -f task2.sql
psql -U postgres -d college_db -f task3.sql
```
MySQL equivalents are noted inline where the syntax differs.
