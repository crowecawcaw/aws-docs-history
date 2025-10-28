After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Database maintenance

Amazon FinSpace Managed kdb allows you to perform schema changes to your database like adding a new
column, updating a column type, and renaming columns, etc. You can perform the database
maintenance operations by creating a general purpose cluster with a writable dataview. A
writable dataview allows you to make updates to your kdb database locally on a cluster. To avoid
caching the whole kdb database on a cluster, you can enable on-demand caching for your dataview
segments. The dataview will only load the filesystem metadata of your database files for the
segments with on-demand caching and loads the actual file content as they are accessed by a
database maintenance operation.

You can implement a database maintenance script and run it as an initialization script. An
initialization script can run for multiple hours without being interrupted, which is required
for long-running database maintenance tasks. When database maintenance script is running,
monitor the cluster logs for progress and any errors. After the database maintenance script
completes, connect to the cluster to verify the updated kdb database and commit changes by using
the `commit_kx_database` q API. The API creates a changeset and returns the changeset
id, which you can use to monitor the changeset status through either the FinSpace API or console.
You can also automate verification and commit steps in your database maintenance script itself.
For more information, see the following sections.

###### Topics

- [Setting up for database maintenance](dbmaint-writable-database-dataviews.md "dbmaint-writable-database-dataviews.md")
- [Performing database
  maintenance](dbmaint-long-running-dbmaint.md "dbmaint-long-running-dbmaint.md")
