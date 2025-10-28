# Bulk import data into an existing Neptune Analytics graph

Neptune Analytics now allows you to efficiently import large datasets into an already provisioned graph database using the
`StartImportTask` API. This API facilitates the direct loading of data from an Amazon S3 bucket into an
**empty** Neptune Analytics graph. This is designed for loading data into existing empty clusters.

Two common use cases for using this feature:

1. Bulk importing data multiple times without provisioning a new graph for each dataset. This helps during the
   development phase of a project where datasets are being converted into Neptune Analytics compatible load formats.
2. Use cases where graph provisioning privileges need to be separated from data operation privileges. For example,
   scenarios where graph provisioning needs to be done by only by the infrastructure team, and data loading and
   querying is done by the data engineering team.

For use cases where you want to create a new graph loaded with data, use the
`CreateGraphUsingImportTask` API instead.

For incrementally loading data from Amazon S3 you can use the loader integration with the openCypher `CALL` clause.
For more information see [Batch load](batch-load.md "batch-load.md").

**Prerequisites**

- An empty Amazon Neptune Analytics graph.
- Data stored in an Amazon Amazon S3 bucket in the same region as the graph.
- An IAM role with permissions to access the Amazon S3 bucket. For more information, see
  [Create your IAM role for Amazon S3 access](bulk-import-create-from-s3.md#create-iam-role-for-s3-access "bulk-import-create-from-s3.md#create-iam-role-for-s3-access").
  **Important considerations**

- **Data integrity**: The `StartImportTask` API is designed to work with
  graphs that are empty. If your graph contains data, you can first reset the graph using the
  [reset-graph](../apiref/API_ResetGraph.md "../apiref/API_ResetGraph.md") API.
  If the Import task finds that the graph is not empty the operation will fail. This operation will delete
  all data from the graph, so ensure you have backups if necessary. You can use the
  [create-graph-snapshot](../apiref/API_CreateGraphSnapshot.md "../apiref/API_CreateGraphSnapshot.md") API to create snapshot of your existing graph.
- **Atomic Operation**: The data import is atomic, meaning it either completes fully
  or does not apply at all. If the import fails we would reset the state back to an empty graph.
- **Format Support**: Loading data supports the same data format as supported by
  `create-graph-using-import-task` and `neptune.load()` This API doesn’t support importing
  data from Neptune .
- **Queries**: Queries will stop working while the import is in progress. You will get
  a `Cannot execute any query until bulk import is complete` error until the import finishes.
  **Steps for bulk importing data**

1. Resetting the graph (if necessary):

If your graph is not empty, reset it using the following command:

```
aws neptune-graph reset-graph --graph-identifier <graph-id>
```

###### Note

This command will completely remove all existing data from your graph. It is recommended that you take a
graph snapshot before performing this action. 2. Start the import task:

To load data into your Neptune graph, use the `start-import-task` command as follows:

```
aws neptune-graph start-import-task \
--graph-identifier <graph-id> \
--source <s3-path-to-data> \
--format <data-format> \
--role-arn <IAM-role-ARN> \
[--fail-on-error | --no-fail-on-error]

```

    * `graph-identifier`: The unique identifier of your Neptune graph.
    * `source`: An Amazon S3 URI prefix. All object names with matching prefixes are loaded.
     See [Neptune loader request parameters](../../../neptune/latest/userguide/load-api-reference-load.md#load-api-reference-load-parameters "../../../neptune/latest/userguide/load-api-reference-load.md#load-api-reference-load-parameters") for Amazon S3 URI prefix examples.
    * `format`: The data format of the Amazon S3 data to be loaded, either `csv`,
     `openCypher`, or `ntriples`. For more information, see
     [Data formats](loading-data-formats.md "loading-data-formats.md").
    * `role-arn`: The ARN of the IAM role that Neptune Analytics can assume to access your Amazon S3 data.
    * `(--no-)fail-on-error`: (Optional) Stops the import process early if an error occurs. By default,
     the system attempts to stop at the first error.

## Troubleshooting bulk import

The following troubleshooting guidance is for common errors encountered during bulk import of data into an Amazon Neptune
graph database. It covers three main issues: the Amazon S3 bucket and the graph being in different regions, the IAM role
used not having the correct permissions, and the bulk load files in a public Amazon S3 bucket not being made public for
reading.

**Common errors**

1. The Amazon S3 bucket and your graph are in different regions.

Verify that your graph and the Amazon S3 bucket are in the same region. Neptune Analytics only supports loading data in the
same region.

```
export GRAPH_ID="<graphId>"                // Replace with your graph identifier
export S3_BUCKET_NAME="<bucketName>"        // Replace with your S3 bucket which contains your graph data files.

# Make sure your graph and S3 bucket are in the same region
aws neptune-graph get-graph --graph-identifier $GRAPH_ID
aws s3api get-bucket-location --bucket $S3_BUCKET_NAME
```

2. The IAM role used does not have the correct permissions.

Verify that you have created the IAM role correctly with read permission to Amazon S3 - see
[Create your IAM role for Amazon S3 access](bulk-import-create-from-s3.md#create-iam-role-for-s3-access "bulk-import-create-from-s3.md#create-iam-role-for-s3-access").

```
export GRAPH_EXEC_ROLE="GraphExecutionRole"
aws iam list-attached-role-policies --role-name $GRAPH_EXEC_ROLE
# Output should contain "PolicyName": "AmazonS3*Access".
```

3. The `AssumeRole` permission is not granted to Neptune Analytics through the AssumeRolePolicy.

Verify that you have attached the policy that allows Neptune Analytics to assume the IAM role to access the Amazon S3
bucket. See [Create your IAM role for Amazon S3 access](bulk-import-create-from-s3.md#create-iam-role-for-s3-access "bulk-import-create-from-s3.md#create-iam-role-for-s3-access").

```
export GRAPH_EXEC_ROLE="GraphExecutionRole"   // Replace with your IAM role.


#Check to make sure Neptune Analytics can assume this role to read from the specificed S3 bucket.
aws iam get-role --role-name $GRAPH_EXEC_ROLE --query 'Role.AssumeRolePolicyDocument' --output text
# Output should contain - SERVICE neptune-graph.amazonaws.com
```

4. The bulk load files are in a public Amazon S3 bucket, but the files themselves are not made public for reading.

When adding bulk load files to a public Amazon S3 bucket, ensure that each file's access control list (ACL) is set to
allow public reads. For example, to set this through the AWS CLI:

```
  aws s3 cp <FileSourceLocation> <FileTargetLocation> --acl public-read
```

This setting can also be done through the Amazon S3 console or the AWS SDKs. For more details, refer to the
documentation for [Configuring ACLs](../../../AmazonS3/latest/userguide/managing-acls.md "../../../AmazonS3/latest/userguide/managing-acls.md").
