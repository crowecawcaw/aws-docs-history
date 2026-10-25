

# Getting started with a modernization job
<a name="sql-server-getting-started"></a>

After you create a SQL Server modernization job in AWS Transform and the agent starts, AWS Transform modernizes your source SQL Server schema by using the **Upload DDL files** workflow. You extract your schema definition (DDL) files with a provided script and upload them to AWS Transform. A live database connection is not required, and real data is not migrated.

This workflow targets Amazon Aurora PostgreSQL by using the supported versions, limitations, and data-handling behavior described elsewhere on this page.