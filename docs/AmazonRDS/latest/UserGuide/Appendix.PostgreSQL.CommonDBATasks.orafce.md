

# Using functions from the orafce extension
<a name="Appendix.PostgreSQL.CommonDBATasks.orafce"></a>

The orafce extension provides functions and operators that emulate a subset of functions and packages from an Oracle database. The orafce extension makes it easier for you to port an Oracle application to PostgreSQL. RDS for PostgreSQL versions 9.6.6 and higher support this extension. For more information about orafce, see [orafce](https://github.com/orafce/orafce) on GitHub.

**Note**  
RDS for PostgreSQL doesn't support the `utl_file` package that is part of the orafce extension. This is because the `utl_file` schema functions provide read and write operations on operating-system text files, which requires superuser access to the underlying host. As a managed service, RDS for PostgreSQL doesn't provide host access.

**To use the orafce extension**

1. Connect to the DB instance with the primary user name that you used to create the DB instance. 

   If you want to turn on orafce for a different database in the same DB instance, use the `/c dbname` psql command. Using this command, you change from the primary database after initiating the connection.

1. Turn on the orafce extension with the `CREATE EXTENSION` statement.

   ```
   CREATE EXTENSION orafce;
   ```

1. Transfer ownership of the oracle schema to the rds\_superuser role with the `ALTER SCHEMA` statement.

   ```
   ALTER SCHEMA oracle OWNER TO rds_superuser;
   ```

   If you want to see the list of owners for the oracle schema, use the `\dn` psql command.