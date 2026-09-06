

# Derived tables for ANSI SQL
<a name="chap-sql-server-aurora-pg.sql.derivedtables"></a>

This topic provides reference information about derived tables in SQL Server and PostgreSQL, focusing on their compatibility in the context of migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can understand how derived tables function similarly in both database systems, enabling you to write complex join queries.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-5.png)  |  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-5.png)  | N/A | N/A | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.sql.derivedtables.sqlserver"></a>

SQL Server implements derived tables as specified in ANSI SQL:2011. Derived tables are similar to CTEs, but the reference to another query is used inside the `FROM` clause of a query.

This feature enables you to write more sophisticated, complex join queries.

### Examples
<a name="chap-sql-server-aurora-pg.sql.derivedtables.sqlserver.examples"></a>

```
SELECT name, salary, average_salary
FROM (SELECT AVG(salary)
  FROM employee) AS workers (average_salary), employee
WHERE salary > average_salary
ORDER BY salary DESC;
```

For more information, see [FROM clause plus JOIN, APPLY, PIVOT (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/queries/from-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.sql.derivedtables.pg"></a>

PostgreSQL implements derived tables and is fully compatible with SQL Server derived tables.

### Examples
<a name="chap-sql-server-aurora-pg.sql.derivedtables.pg.examples"></a>

```
SELECT name, salary, average_salary
FROM (SELECT AVG(salary)
  FROM employee) AS workers (average_salary), employee
WHERE salary > average_salary
ORDER BY salary DESC;
```

For more information, see [Table Expressions ](https://www.postgresql.org/docs/13/queries-table-expressions.html) in the *PostgreSQL documentation*.