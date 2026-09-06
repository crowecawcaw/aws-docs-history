

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Performing database maintenance
<a name="dbmaint-long-running-dbmaint"></a>

After you create a writeable dataview, you create a scaling group general purpose cluster to run a long-running database maintenance script. For this, you use the cluster `initializationScript` attribute. The database maintenance script could run for multiple hours without being terminated. When database maintenance script is running, monitor the cluster logs for progress and any errors from the database maintenance script. After the database maintenance script completes, connect to the cluster to verify the updated kdb database and commit changes to the underlying kdb database by using the `commit_kx_database` q API. You can also automate these steps in your database maintenance script itself. 

## Steps to perform database maintenance using a scaling group general purpose cluster
<a name="dbmaint-using-sg-cluster"></a>

1. Create a general purpose cluster in the scaling group with the previously created data view and provide database maintenance script using `initializationScript` in the [CreateKxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxCluster.html) API operation. After you create the cluster, wait till the status changes to `Running`. During this time, you can monitor the logs from the cluster for progress and any errors from the database maintenance script.

1. Call the [GetKxConnectionString](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxConnectionString.html) API to get a `signedConnectionString` for the cluster.

1. Connect to the cluster and verify the kdb database state by running q commands.

1. Call the `commit_kx_database` q API with the database name to apply the changes to the source kdb database. 

1. Call the [GetKxChangset](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxChangeset.html) API operation to check the status of the commit database changeset. After the kdb database is successfully updated, you can load the updated kdb database on an existing HDB cluster by calling the [UpdateKxClusterDatabases](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxClusterDatabases.html) API operation or on a new HDB cluster by calling the [CreateKxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxCluster.html) API operation.

## Steps to perform database maintenance using `dbmaint.q`
<a name="dbmaint-using-dbmaintq"></a>

This is section shows how you can perform database maintenance on a partitioned database by using a `dbmaint.q` script. The following example explains how you can load the `dbmaint.q` script on a general purpose cluster that runs on a scaling group, add a new column to a table, and finally commit the database to create a changeset.

1. Load the [`dbmaint.q`](https://github.com/KxSystems/kdb/blob/master/utils/dbmaint.q) script by running the following command. This script contains utility functions for maintenance of partitioned database tables in kdb\+.

   ```
   q) \l /opt/kx/app/code/dbmaint/dbmaint.q
   ```

1. Load a database.

   ```
   q) \l /opt/kx/app/db/{{welcomedb}}
   ```

1. Inspect the table schema in your database.

   ```
   q) meta example
   c     | t f a
   ------| -----
   date  | d
   sym   | s   p
   time  | p
   number| j
   ```

1. Change to the database parent directory.

   ```
   q) \cd /opt/kx/app/db
   ```

1. Add a new column using the `addcol` function from the `dbmaint.q` script.

   ```
   addcol[`:{{welcomedb}};`example;`price;0h];
   ```

1. Inspect the updated table schema with the newly added column. 

   ```
   q)con "meta example"
   c     | t f a
   ------| -----
   date  | d
   sym   | s   p
   time  | p
   number| j
   price | h
   ```

1. Commit the database changes by calling the `.aws.commit_kx_changeset` q API. The API creates a changeset and returns the id, which you can use to monitor the changeset status through the FinSpace API or console.

   ```
   q) .aws.commit_kx_database["{{welcomedb}}"]
   id    | "{{UscXQcZ2htijCQlr1xNaIA}}"
   status| "PENDING"
   ```

**Note**  
The recommended way to perform a long-running database maintenance is to implement a database maintenance script and execute it as cluster initialization script. An initialization script can run for multiple hours without being interrupted which is required for long-running database maintenance tasks. When database maintenance script is running, monitor the cluster logs for progress and any errors. After the database maintenance script completes, connect to the cluster to verify the updated kdb database and commit changes to the underlying kdb database by using the commit\_kx\_database q API. You can also automate verification and commit steps in your database maintenance script itself. 