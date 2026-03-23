# Common Language Runtime for T-SQL

This topic provides reference information about migrating Microsoft SQL Server’s Common Language Runtime (CLR) objects to Amazon Aurora PostgreSQL. You can understand the differences in functionality between SQL Server’s CLR capabilities and alternatives. The topic explains that while Aurora PostgreSQL doesn’t support .NET code directly, it offers Perl as an alternative for creating similar database objects.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                     |
| ------------------------------ | ---------------------------------- | ------------------------- | --------------------------------------------------- |
| One star feature compatibility | No automation                      | N/A                       | Migrating CLR objects requires a full code rewrite. |

## SQL Server Usage

SQL Server provides the capability of implementing .NET objects in the database using the Common Runtime Library (CLR). The CLR enables development of functionality that would be complicated using T-SQL.

The CLR provides robust solutions for string manipulation, date manipulation, and calling external services such as Windows Communication Foundation (WCF) services and web services.

You can create the following objects with the `EXTERNAL NAME` clause:

- Procedures. For more information, see [CLR Stored Procedures](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/clr-stored-procedures?redirectedfrom=MSDN "https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/clr-stored-procedures?redirectedfrom=MSDN") in the _SQL Server documentation_.
- Functions. For more information, see [Create CLR Functions](https://docs.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-clr-functions?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/user-defined-functions/create-clr-functions?view=sql-server-2017") in the _SQL Server documentation_.
- Triggers. For more information, see [Create CLR Triggers](https://docs.microsoft.com/en-us/sql/relational-databases/triggers/create-clr-triggers?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/triggers/create-clr-triggers?view=sql-server-2017") in the _SQL Server documentation_.
- Types. For more information, see [CLR User-Defined Types](https://docs.microsoft.com/en-us/sql/relational-databases/clr-integration-database-objects-user-defined-types/clr-user-defined-types?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/clr-integration-database-objects-user-defined-types/clr-user-defined-types?view=sql-server-2017") in the _SQL Server documentation_.
- User-defined aggregate functions. For more information, see [CLR User-Defined Aggregates](https://docs.microsoft.com/en-us/sql/relational-databases/clr-integration-database-objects-user-defined-functions/clr-user-defined-aggregates?view=sql-server-2017 "https://docs.microsoft.com/en-us/sql/relational-databases/clr-integration-database-objects-user-defined-functions/clr-user-defined-aggregates?view=sql-server-2017") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) doesn’t support .NET code. However, you can create Perl functions. In this case, convert all C# code to PL/pgSQL or PL/Perl.

To use PL/Perl language, install the Perl extension:

```
CREATE EXTENSION plperl;
```

After you install the Perl extension, you can create functions using Perl code. Specify `plperl` in the `LANGUAGE` clause.

You can create the following objects with Perl:

- Functions.
- Void functions or procedures.
- Triggers.
- Event Triggers.
- Values for session level.

### Examples

The following example creates a function that returns the greater value of two integers.

```
CREATE FUNCTION perl_max (integer, integer) RETURNS integer AS $$
  if ($_[0] > $_[1]) { return $_[0]; }
  return $_[1];
$$ LANGUAGE plperl;
```

For more information, see [PL/Perl — Perl Procedural Language](https://www.postgresql.org/docs/13/plperl.html "https://www.postgresql.org/docs/13/plperl.html") in the _PostgreSQL documentation_.
