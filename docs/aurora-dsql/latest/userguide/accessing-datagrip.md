# Use JetBrains DataGrip to access Aurora DSQL

JetBrains DataGrip is a cross-platform IDE for working with SQL and databases, including
PostgreSQL. DataGrip includes a robust GUI with an intelligent SQL editor. To download DataGrip, go
to the [download page](https://www.jetbrains.com/datagrip/download "https://www.jetbrains.com/datagrip/download") on the
_JetBrains_ website.

###### To set up a new Aurora DSQL connection in JetBrains DataGrip

1. Choose **New Data Source** and choose PostgreSQL.
2. In the **Data Sources/General** tab, enter the following
   information:
   1. **Host** – Use your cluster endpoint.

   **Port** – Aurora DSQL uses the PostgreSQL default:
   `5432`

   **Database** – Aurora DSQL uses the PostgreSQL default of
   `postgres`

   **Authentication** – Choose `User &
 Password` .

   **Username** – Enter `admin`.

   **Password** – [Generate a
   token](SECTION_authentication-token.md "SECTION_authentication-token.md") and paste it into this field.

   **URL** – Don't modify this field. It will be
   auto-populated based on the other fields.

3. **Password** – Provide this by generating an
   authentication token. Copy the resulting output of the token generator and paste it into the
   password field.

###### Note

You must set SSL mode in the client connections. Aurora DSQL supports `PGSSLMODE=require
 and PGSSLMODE=verify-full`. Aurora DSQL enforces SSL communication on the server side and
rejects non-SSL connections. For the `verify-full` option you will need to install
the SSL certificates locally. For more information see [SSL/TLS
certificates](configure-root-certificates.md "configure-root-certificates.md"). 4. You should be connected to your cluster and can start running SQL statements:

###### Important

Some views provided by DataGrip for PostgreSQL databases (such as Sessions) don't apply to
Aurora DSQL databases because of their unique architecture. While accessible, these screens don't provide
reliable information about the actual sessions connected to the database.
