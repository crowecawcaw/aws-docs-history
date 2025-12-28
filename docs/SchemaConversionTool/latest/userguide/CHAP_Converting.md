# Updating and refreshing converted schemas in AWS SCT

You can update both the source schema and the target schema
in your AWS Schema Conversion Tool project.

- **Source** –
  If you update the schema for your source database,
  AWS SCT replaces the schema in your project with
  the latest schema from your source database. Using this functionality, you can
  update your project if changes have been made to the schema of your source
  database.
- **Target** –
  If you update the schema for your target Amazon RDS DB instance,
  AWS SCT replaces the schema in your
  project with the latest schema from your target DB instance. If you haven't
  applied any schema to your target DB instance, AWS SCT clears the
  converted schema from your project. You can then convert the schema from your
  source database for a clean target DB instance.
  You update the schema in your AWS SCT project by choosing **Refresh
  from Database**.

###### Note

When you refresh your schema, AWS SCT loads metadata only as it is needed. To fully load
all of your database's schema, open the context (right-click) menu for your schema, and choose
**Load schema**. For example, you can use this option to load metadata for your database
all at once, and then work offline.
