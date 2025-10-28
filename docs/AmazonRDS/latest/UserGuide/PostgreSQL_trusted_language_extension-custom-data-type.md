# Using Custom Data Types in TLE

PostgreSQL supports commands to register new base types (also known as scalar types)
for efficiently handling complex data structures in your database. A base
type allows you to customize how the data is stored internally, and how to
convert it to and from an external textual representation. These custom data
types are helpful when extending PostgreSQL to support functional domains where
a built-in type such as number or text can't provide sufficient search
semantics.

RDS for PostgreSQL enables you to create custom data types in your trusted language extension and define functions that support SQL
and index operations for these new data types. Custom data types are available for the following versions:

- RDS for PostgreSQL 15.4 and higher 15 versions
- RDS for PostgreSQL 14.9 and higher 14 versions
- RDS for PostgreSQL 13.12 and higher 13 versions
  For more information, see [Trusted Language Base types](https://github.com/aws/pg_tle/blob/main/docs/09_datatypes.md "https://github.com/aws/pg_tle/blob/main/docs/09_datatypes.md").
