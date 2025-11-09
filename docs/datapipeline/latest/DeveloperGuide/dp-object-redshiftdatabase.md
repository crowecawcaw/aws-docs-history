AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# RedshiftDatabase

Defines an Amazon Redshift database. `RedshiftDatabase` represents the properties
of the database used by your pipeline.

## Example

The following is an example of this object type.

```
{
  "id" : "MyRedshiftDatabase",
  "type" : "RedshiftDatabase",
  "clusterId" : "`myRedshiftClusterId`",
  "username" : "`user_name`",
  "*password" : "`my_password`",
  "databaseName" : "`database_name`"
}
```

By default, the object uses the Postgres driver, which requires the
`clusterId` field. To use the Amazon Redshift driver, specify the
Amazon Redshift database connection string from the Amazon Redshift console (starts with
"jdbc:redshift:") in the `connectionString` field instead.

## Syntax

| Required Fields | Description                                              | Slot Type |
| --------------- | -------------------------------------------------------- | --------- |
| \*password      | The password to supply.                                  | String    |
| username        | The user name to supply when connecting to the database. | String    |

| Required Group (One of the following is required) | Description                                                                                                                                                                                                                                                                                                                                        | Slot Type |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| clusterId                                         | The identifier provided by the user when the Amazon Redshift cluster was created. For example, if the<br>endpoint for your Amazon Redshift cluster is<br>mydb.example.us-east-1.redshift.amazonaws.com, the<br>correct identifier is `mydb`. In the<br>Amazon Redshift console, you can get this value from Cluster<br>Identifier or Cluster Name. | String    |
| connectionString                                  | The JDBC endpoint for connecting to an Amazon Redshift instance owned by an account different than the<br>pipeline. You can't specify both<br>`connectionString` and<br>`clusterId`.                                                                                                                                                               | String    |

| Optional Fields | Description                                                                          | Slot Type                                                        |
| --------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| databaseName    | Name of the logical database to attach to.                                           | String                                                           |
| jdbcProperties  | Pairs of the form A=B to be set as properties on JDBC connections for this database. | String                                                           |
| parent          | Parent of the current object from which slots are inherited.                         | Reference Object, for example, "parent":{"ref":"myBaseObjectId"} |
| region          | The code for the region where the database exists. For example, us-east-1.           | Enumeration                                                      |

| Runtime Fields | Description                                        | Slot Type |
| -------------- | -------------------------------------------------- | --------- |
| @version       | Pipeline version that the object was created with. | String    |

| System Fields | Description                                                                                                                                   | Slot Type |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| @error        | Error describing the ill-formed object.                                                                                                       | String    |
| @pipelineId   | ID of the pipeline to which this object belongs.                                                                                              | String    |
| @sphere       | The sphere of an object denotes its place in the lifecycle: Component Objects give rise to<br>Instance Objects which execute Attempt Objects. | String    |
