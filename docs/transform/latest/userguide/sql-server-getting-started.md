

# Getting started with a modernization job
<a name="sql-server-getting-started"></a>

After you create a SQL Server modernization job in AWS Transform and the agent starts, the agent asks how you want AWS Transform to access your source SQL Server schema. Your response to this first message determines which workflow runs for the remainder of the job. Choose one of the following:
+ **Connect to database** — AWS Transform connects directly to your running SQL Server. Choose this when a live network connection to the database is available and you want AWS Transform to migrate real data.
+ **Upload DDL files** — You extract your schema definition (DDL) files with a provided script and upload them to AWS Transform. Choose this when a direct database connection is not available or not desired. No live connection is required, and real data is not migrated.

Both workflows target Amazon Aurora PostgreSQL and share the same supported versions, limitations, and data-handling behavior described elsewhere on this page. Choose the workflow that matches your environment.

**Note**  
When you choose **Connect to database**, the online workflow starts. When you choose **Upload DDL files**, the offline workflow starts.