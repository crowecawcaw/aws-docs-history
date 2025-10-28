# Using the `neptune-export` command-line

tool to export data from Neptune

You can use the following steps to export data from your Neptune DB cluster to Amazon S3
using the `neptune-export` command-line utility:

## Prerequisites for using

the `neptune-export` command-line utility

###### Before you start

- **Have version 8 of the JDK**   –  
  You need version 8 of the [Java
  SE Development Kit (JDK)](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html "https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html") installed.
- **Download the neptune-export
  utility**   –   Download and install the
  [neptune-export.jar](https://s3.amazonaws.com/aws-neptune-customer-samples/neptune-export/bin/neptune-export.jar "https://s3.amazonaws.com/aws-neptune-customer-samples/neptune-export/bin/neptune-export.jar") file.
- **Make sure `neptune-export` has access to
  your Neptune VPC**   –   Run neptune-export
  from a location where it can access the VPC where your Neptune DB cluster
  is located.

For example, you can run it on an Amazon EC2 instance within the Neptune
VPC, or in a separate VPC that is peered with the Neptune VPC, or on
a separate bastion host.

- **Make sure the VPC security groups grant access to
  `neptune-export`**   –   Check that
  the VPC security group(s) attached to the Neptune VPC allow access to
  your DB cluster from the IP address or security group associated with
  the `neptune-export` environment.
- **Set up the necessary IAM permissions**
    –   If your database has AWS Identity and Access Management (IAM) database
  authentication enabled, make sure that the role under which
  `neptune-export` runs is associated with an IAM policy
  that allows connections to Neptune. For information about Neptune
  policies, see [Using IAM policies](security-iam-access-manage.md "security-iam-access-manage.md").

If you want to use the `clusterId` export parameter in
your query requests, the role under which `neptune-export`
runs requires the following IAM permissions:

    + `rds:DescribeDBClusters`
    + `rds:DescribeDBInstances`
    + `rds:ListTagsForResource`

If you want to export from a cloned cluster, the role under which
`neptune-export` runs requires the following IAM permissions:

    + `rds:AddTagsToResource`
    + `rds:DescribeDBClusters`
    + `rds:DescribeDBInstances`
    + `rds:ListTagsForResource`
    + `rds:DescribeDBClusterParameters`
    + `rds:DescribeDBParameters`
    + `rds:ModifyDBParameterGroup`
    + `rds:ModifyDBClusterParameterGroup`
    + `rds:RestoreDBClusterToPointInTime`
    + `rds:DeleteDBInstance`
    + `rds:DeleteDBClusterParameterGroup`
    + `rds:DeleteDBParameterGroup`
    + `rds:DeleteDBCluster`
    + `rds:CreateDBInstance`
    + `rds:CreateDBClusterParameterGroup`
    + `rds:CreateDBParameterGroup`

To publish the exported data to Amazon S3, the role under which
`neptune-export` runs requires the following IAM permissions for
the Amazon S3 location(s):

    + `s3:PutObject`
    + `s3:PutObjectTagging`
    + `s3:GetObject`

- **Set the `SERVICE_REGION` environment variable**
    –   Set the `SERVICE_REGION` environment variable
  to identify the Region where your DB cluster is located (see [Connecting to Neptune](iam-auth-connecting-gremlin-java.md "iam-auth-connecting-gremlin-java.md")
  for a list of Region identifiers).

## Running the `neptune-export`

utility to initiate an export operation

Use the following command to run neptune-export from the command line and start an
export operation:

```
java -jar neptune-export.jar nesvc \
  --root-path `(path to a local directory)` \
  --json `(the JSON file that defines the export)`
```

The command has two parameters:

###### Parameters for neptune-export when starting an export

- **`--root-path`**   –  
  Path to a local directory where export files are written before being published
  to Amazon S3.
- **`--json`**   –  
  A JSON object that defines the export.

## Example commands using the

`neptune-export` command line utility

To export property-graph data directly from your source DB cluster:

```
java -jar neptune-export.jar nesvc \
  --root-path /home/ec2-user/neptune-export \
  --json '{
            "command": "export-pg",
            "outputS3Path" : "s3://`(your Amazon S3 bucket)`/neptune-export",
            "params": {
              "endpoint" : "`(your neptune DB cluster endpoint)`"
            }
          }'
```

To export RDF data directly from your source DB cluster:

```
java -jar neptune-export.jar nesvc \
  --root-path /home/ec2-user/neptune-export \
  --json '{
            "command": "export-rdf",
            "outputS3Path" : "s3://`(your Amazon S3 bucket)`/neptune-export",
            "params": {
              "endpoint" : "`(your neptune DB cluster endpoint)`"
            }
          }'
```

If you omit the `command` request parameter, the `neptune-export`
utility exports property-graph data from Neptune by default.

To export from a clone of your DB cluster:

```
java -jar neptune-export.jar nesvc \
  --root-path /home/ec2-user/neptune-export \
  --json '{
            "command": "export-pg",
            "outputS3Path" : "s3://(your Amazon S3 bucket)/neptune-export",
            "params": {
              "endpoint" : "(your neptune DB cluster endpoint)",
              "cloneCluster" : true
            }
          }'
```

To export from your DB cluster using IAM authentication:

```
java -jar neptune-export.jar nesvc \
  --root-path /home/ec2-user/neptune-export \
  --json '{
            "command": "export-pg",
            "outputS3Path" : "s3://`(your Amazon S3 bucket)`/neptune-export",
            "params": {
              "endpoint" : "`(your neptune DB cluster endpoint)`"
              "useIamAuth" : true
            }
          }'
```
