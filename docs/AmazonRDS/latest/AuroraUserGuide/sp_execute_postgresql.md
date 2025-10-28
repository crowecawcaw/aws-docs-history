# sp_execute_postgresql

You can execute PostgreSQL statements from T-SQL endpoint. This simplifies your applications as you don’t need to exit T-SQL port to execute these statements.

## Syntax

```
sp_execute_postgresql [ @stmt = ] statement
```

## Arguments

_[ @stmt ] statement_

The argument is of datatype varchar. This argument accept PG dialect statements.

###### Note

You can only pass one PG dialect statement as an argument otherwise it will raise the following error.

```
`1>`exec sp_execute_postgresql 'create extension pg_stat_statements; drop extension pg_stat_statements'
`2>`go
```

```
`Msg 33557097, Level 16, State 1, Server BABELFISH, Line 1
expected 1 statement but got 2 statements after parsing`
```

## Usage notes

### CREATE EXTENSION

Creates and loads a new extension into the current database.

```
`1>`EXEC sp_execute_postgresql 'create extension [ IF NOT EXISTS ] `<extension name>` [ WITH ] [SCHEMA `schema_name`] [VERSION `version`]';
`2>`go

```

The following example shows how to create an extension:

```
`1>`EXEC sp_execute_postgresql 'create extension pg_stat_statements with schema sys version "1.10"';
`2>`go
```

Use the following command to access extension objects:

```

`1>`select * from pg_stat_statements;
`2>`go

```

###### Note

If schema name is not provided explicitly during extension creation, by default the extensions are installed in the public schema.
You must provide the schema qualifier to access the extension objects as mentioned below:

```
`1>`select * from [public].pg_stat_statements;
`2>`go
```

###### Supported extensions

The following extensions available with Aurora PostgreSQL works with Babelfish.

- `pg_stat_statements`
- `tds_fdw`
- `fuzzystrmatch`

###### Limitations

- Users need to have sysadmin role on T-SQL and rds_superuser on postgres to install the extenstions.
- Extensions cannot be installed in user created schemas and also in dbo and guest schemas for master, tempdb and msdb database.
- CASCADE option is not supported.

## ALTER EXTENSION

You can upgrade to a new extension version using ALTER extension.

```
`1>`EXEC sp_execute_postgresql 'alter extension <extension name> UPDATE TO <new_version>';
`2>`go
```

###### Limitations

- You can upgrade the version of your extension only using the ALTER Extension statement. Other operations aren't supported.

## DROP EXTENSION

Drops the specified extension. You can also use `if exists` or `restrict` options to drop the extension.

```
`1>`EXEC sp_execute_postgresql 'drop extension <extension name>';
`2>`go
```

###### Limitations

- CASCADE option is not supported.
