# Setting

table-level autovacuum parameters

You can set autovacuum-related [storage parameters](https://www.postgresql.org/docs/current/static/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS "https://www.postgresql.org/docs/current/static/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS") at a table level, which can be better than altering the behavior
of the entire database. For large tables, you might need to set aggressive settings and you
might not want to make autovacuum behave that way for all tables.

The following query shows which tables currently have table-level options in place.

```
SELECT relname, reloptions
FROM pg_class
WHERE reloptions IS NOT null;
```

An example where this might be useful is on tables that are much larger than the rest of
your tables. Suppose that you have one 300-GB table and 30 other tables less than 1 GB. In
this case, you might set some specific parameters for your large table so you don't alter
the behavior of your entire system.

```
ALTER TABLE mytable set (autovacuum_vacuum_cost_delay=0);
```

Doing this turns off the cost-based autovacuum delay for this table at the expense of more
resource usage on your system. Normally, autovacuum pauses for
`autovacuum_vacuum_cost_delay` each time `autovacuum_cost_limit` is
reached. For more details, see the PostgreSQL documentation about [cost-based vacuuming](https://www.postgresql.org/docs/current/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-VACUUM-COST "https://www.postgresql.org/docs/current/static/runtime-config-resource.html#RUNTIME-CONFIG-RESOURCE-VACUUM-COST").
