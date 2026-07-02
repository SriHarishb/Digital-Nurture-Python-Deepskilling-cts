# Hands-On 4 -- Query Performance & Indexing

**Sri Harish B** 

## Files
- `task_1.sql` -- baseline `EXPLAIN ANALYZE` on the target query before any indexes exist
- `task_2.sql` -- adds a B-Tree index, a composite unique index and a partial index, then re-runs `EXPLAIN` to compare query plans
- `task_3_n_plus_one_demo.py` -- reproduces the N+1 query problem against `college_db` with `psycopg2`, fixes it with a single JOIN, and times both versions

## Setup
```bash
psql -U postgres -d college_db -f task_1.sql
psql -U postgres -d college_db -f task_2.sql

pip install psycopg2-binary
python task_3_n_plus_one_demo.py
```
