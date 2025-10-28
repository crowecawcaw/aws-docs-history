# Understanding SQL Server

to PostgreSQL conversion settings

SQL Server to PostgreSQL conversion settings in DMS Schema Conversion include the
following:

- To convert applicable database objects using generative AI enable the
  **Generative AI** setting. Objects
  successfully converted using generative AI will be clearly identified with
  **Action Item 7744**, which states: "This
  conversion uses machine learning models that generate predictions based on
  patterns in data." For more information, see
  [Converting database objects
  with generative AI](schema-conversion-convert.md "schema-conversion-convert.md").
- In SQL Server, you can use indexes with the same name in different tables.
  However, in PostgreSQL, all index names that you use in the schema must be
  unique. To make sure that DMS Schema Conversion generates unique names for all your
  indexes, select **Generate unique names for
  indexes**.
- PostgreSQL versions 10 and earlier don't support procedures. If you aren't
  familiar with using procedures in PostgreSQL, AWS DMS can convert SQL Server
  procedures to PostgreSQL functions. To do so, select **Convert
  procedures to functions**.
- Your source SQL Server database can store the output of `EXEC`
  in a table. DMS Schema Conversion creates temporary tables and an additional procedure to
  emulate this feature. To use this emulation, select **Create
  additional routines to handle open datasets**.
- You can define the template to use for the schema names in the converted
  code. For **Schema names**, choose one of the following
  options:
  - **DB** – Uses the SQL Server database name as a
    schema name in PostgreSQL.
  - **SCHEMA** – Uses the SQL Server schema name as a
    schema name in PostgreSQL.
  - **DB_SCHEMA** – Uses a combination of the SQL
    Server database and schema names as a schema name in
    PostgreSQL.

- You can keep the letter case in the names of source operands. To avoid
  conversion of operand names to lowercase, select **Avoid casting to
  lowercase for case-sensitive operations**. This option is
  applicable only if the case-sensitivity feature is enabled in the source
  database.
- You can keep the parameter names from your source database. DMS Schema Conversion can
  add double quotation marks to the names of parameters in the converted code.
  To do so, select **Keep original parameter names**.
- You can keep a length of routine parameters from your source database.
  DMS Schema Conversion creates domains and uses them to specify a length of routine
  parameters. To do so, select **Preserve parameter
  lengths**.
- To convert unsupported built-in objects to stub objects, enable the
  **Convert unsupported built-in objects to stub
  objects** setting:
  - When enabled, DMS SC replaces unsupported built-in objects with
    corresponding stub objects in the target database. This feature
    converts code sections that would normally be enclosed by migration
    issue 7811 or 7904. It creates stub objects based on the type of the
    source built-in objects `PROCEDURE` for procedures,
    `VIEW` for views or tables.

  Conversion of a source database object with a call of an
  unsupported object results in a call of a stub object and migration
  issue 7822.

  You can choose to create stub objects in a separate schema by
  enabling the **Create stub objects in a separate
  schema** option. When selected, stub objects are
  created in a special schema named `aws_sqlserver_stub` in
  the target database. If not selected, they are created in the same
  schema as the calling objects.
  - Stub routines are named based on the fully qualified name of the
    original built-in. For stub views, the naming convention includes
    the system schema name
    `system_schema_name$builtin_view_name`.

  During re-conversion, DMS SC checks for existing stub routines in
  the target database. If a routine with the same name and input
  parameters already exists, it is not overwritten.

  After conversion, review and implement custom code for stub
  routines as needed.

- `CITEXT` datatype for all string datatypes setting in DMS
  Schema Conversion include the following:
  - To use the `CITEXT` datatype for case-insensitive
    string operations when converting from SQL Server to PostgreSQL,
    enable the **Use CITEXT for all string datatypes**
    setting. This option helps maintain consistent behavior when
    migrating from a case-insensitive SQL Server to a case-sensitive
    PostgreSQL environment.
  - When enabled, DMS SC converts all relevant string datatypes from
    the source SQL Server database to `CITEXT` in PostgreSQL.
    This eliminates the need for explicit LOWER () function calls in
    conditions and automatically casts string expressions in conditional
    operations to `CITEXT`.
  - To determine if your SQL Server instance is case-sensitive, run
    the following query:

  ```
  SELECT SERVERPROPERTY('COLLATION');
  ```

  A result containing 'CI' indicates case-insensitive, while 'CS'
  indicates case-sensitive.
  - The `CITEXT` conversion may not apply in scenarios
    where explicit case-sensitive collate settings are used at the
    server, database, or column level.

  To use this feature, ensure that the `CITEXT` module is
  installed and available in your target PostgreSQL database.
  - When using the `CITEXT` datatype conversion, consider
    the following best practices:
    - Enable this feature when migrating from a case-insensitive
      SQL Server to maintain consistent behavior in
      PostgreSQL.
    - Review your application code to ensure it doesn't rely on
      case-sensitive string operations.
    - Thoroughly test your application after migration to verify
      that case-insensitive behavior is maintained as
      expected.
