# Using a MySQL database as a source in DMS Schema Conversion

You can use MySQL databases as a migration source in DMS Schema Conversion.

You can use DMS Schema Conversion to convert database code objects from MySQL Database to the following targets:

- PostgreSQL
- Aurora PostgreSQL
  The privileges required for MySQL as a source are as follows:

- `SELECT ON *.*`
- `SHOW VIEW ON *.*`

## MySQL to PostgreSQL conversion settings

For information about editing DMS Schema Conversion settings, see
[Specifying schema conversion settings for
migration projects](schema-conversion-settings.md "schema-conversion-settings.md").

MySQL to PostgreSQL conversion settings include the following:

- **Comments in converted SQL code**:
  Set this setting to add comments in the converted code for the action items of
  the selected severity and higher.

Valid values:

    + **Errors only**
    + **Errors and warnings**
    + **All messages**
