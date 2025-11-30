# Using dynamic masking with Aurora PostgreSQL

Dynamic data masking is a security feature that protects sensitive data in Aurora PostgreSQL databases by controlling
how data appears to users at query time. Aurora implements it through the `pg_columnmask` extension.
`pg_columnmask` provides column-level data protection that complements PostgreSQL's native
row-level security and granular access control mechanisms.

With `pg_columnmask`, you create masking policies that determine data visibility based on user roles.
When users query tables with masking policies, Aurora PostgreSQL applies the appropriate masking function
at query time based on the user's role and policy weight. The underlying data remains unchanged in storage.

`pg_columnmask` supports the following capabilities:

- **Built-in and custom masking functions** – Use pre-built functions
  for common patterns like email and text masking, or create your own custom functions to protects sensitive
  data (PII) through SQL-based masking policies.
- **Multiple masking strategies** – Completely hide information,
  replace partial values with wildcards, or define custom masking approaches.
- **Policy prioritization** – Define multiple policies for a single column.
  Use weights to determine which masking policy should be used when multiple policies apply to a column.
  Aurora PostgreSQL applies policies based on weight and user role membership.
  `pg_columnmask` is available on Aurora PostgreSQL version 16.10 and higher, and version 17.6 and higher.
  It is available is available at no additional cost.
