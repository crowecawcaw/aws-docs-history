

# Querying federated databases
<a name="qerying-fed-db"></a>

 After you grant permissions, users can sign in and start querying the federated database using Amazon Redshift. Users can now use the local database name to reference the Amazon Redshift datashare in SQL queries. In Amazon Redshift, the customer table in the public schema that is shared through the datashare will have a corresponding table created as `public.customer` in the Data Catalog.

1. Before querying the federated database using Amazon Redshift, the cluster administrator creates a database from the Data Catalog database using the following command: 

   ```
   CREATE DATABASE sharedcustomerdb FROM ARN 'arn:aws:glue:{{<region>}}:111122223333:database/tahoedb' WITH DATA CATALOG SCHEMA tahoedb
   ```

1.  The cluster admin grants usage permissions on the database.

   ```
   GRANT USAGE ON DATABASE sharedcustomerdb TO IAM:user;
   ```

1.  You ( the federated user) can now log in into SQL tools to query the table. 

   ```
   Select * from sharedcustomerdb.public.customer limit 10;
   ```

 For more information, see [Querying AWS Glue Data Catalog](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2-glue.html) in Amazon Redshift Management Guide. 