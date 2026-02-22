# Understanding masking behavior in DML operations

`pg_columnmask` applies consistently across all DML operations, including INSERT, UPDATE, DELETE, and MERGE statements.
When you execute these operations, Aurora PostgreSQL masks data according to a core principle –
any data read from storage is masked according to the current user's applicable policies.

Masking affects some of the following query components like:

- WHERE clauses
- JOIN conditions
- Subqueries
- RETURNING clauses
  All of these components operate on masked values, not the original data.
  While data is written to storage unmasked, users only see their masked view when reading it back.

Aurora PostgreSQL enforces all database constraints (NOT NULL, UNIQUE, CHECK, FOREIGN KEY) on the actual
stored values, not masked values. This can occasionally create apparent inconsistencies if masking
functions aren't carefully designed.

Masking works alongside column-level permissions:

- Users without SELECT privileges cannot read columns
- Users with SELECT privileges see masked values according to their applicable policies
