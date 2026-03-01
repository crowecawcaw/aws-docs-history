# Addressing object ownership differences after upgrade

Babelfish versions 4.6 and later, and 5.2 and later include a change to object
ownership handling through the TDS endpoint. When you create new objects through the TDS
endpoint, these objects are now owned by the schema owner instead of the current user.
This ownership change might affect permissions behavior for new objects compared to
existing objects when you upgrade from versions earlier than 4.6 or 5.2.

To resolve these ownership differences, Babelfish provides the
`sys.generate_alter_ownership_statements()` function. This function
generates SQL statements that align object ownership with schema ownership.

Be aware of the following limitations when addressing object ownership:

- Users with CREATE permissions granted through the PostgreSQL endpoint can't
  create objects through the TDS endpoint in those schemas.
- Modifying permissions on T-SQL objects through the PostgreSQL endpoint is not
  recommended and might cause incorrect T-SQL behavior.
- Access permissions might differ between old and new objects because of their
  ownership mismatch. For example, consider a schema owned by `sch_own`
  that includes objects owned by `dbo`. In this case, objects owned by
  `dbo` that were created before the upgrade might have different
  access permissions compared to objects owned by `sch_own` that were
  created after the upgrade. This may affect operations like SELECT and
  INSERT.
  If your DB cluster includes objects created in Babelfish versions earlier than 4.6
  or 5.2, consider aligning their ownership.

###### To address object ownership differences

1. Connect to the `babelfish_db` database in your DB cluster using the
   PostgreSQL endpoint.
2. Run the following command:

```
SELECT * from sys.generate_alter_ownership_statements();
```

This generates a list of SQL statements intended to standardize ownership
among the objects. 3. Execute the generated statements on a test environment first to validate their
effect before applying on your production environment.
We recommend that you execute these statements to achieve a consistent object
ownership model across your database.
