# Hands-On 3 -- Subqueries, Views, Stored Procedures & Transactions

**Sri Harish B** 

## Files
- `task_1.sql` -- correlated and non-correlated subqueries
- `task_2.sql` -- views (`vw_student_enrollment_summary` and others)
- `task_3.sql` -- stored procedures (`sp_enroll_student`, `sp_transfer_student`), transactions and savepoints, with a deliberate-failure test to confirm rollback behaviour

## Setup
Run against the `college_db` schema from Hands-On 1/2:
```bash
psql -U postgres -d college_db -f task_1.sql
psql -U postgres -d college_db -f task_2.sql
psql -U postgres -d college_db -f task_3.sql
```
`task_3.sql` targets MySQL syntax for the stored procedures (`DELIMITER`,
`EXIT HANDLER`); the PostgreSQL equivalent uses `CREATE OR REPLACE FUNCTION`
with `plpgsql`.
