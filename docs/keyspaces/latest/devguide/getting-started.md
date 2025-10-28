# Create a keyspace in Amazon Keyspaces

In this section, you create a keyspace using the
console, `cqlsh`, or the AWS CLI.

###### Note

Before you begin, make sure that you have configured
all the [tutorial prerequisites](getting-started.md "getting-started.md").

A _keyspace_ groups related tables that are relevant for one or
more applications. A keyspace contains one or more tables and defines the replication
strategy for all the tables it contains. For more information about keyspaces, see the
following topics:

- Data definition language (DDL) statements in the CQL language reference: [Keyspaces](cql.ddl.md "cql.ddl.md")
- [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md")
  In this tutorial we create a single-Region keyspace, and the replication strategy of
  the keyspace is `SingleRegionStrategy`. Using
  `SingleRegionStrategy`, Amazon Keyspaces replicates data across three [Availability
  Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") in one AWS Region. To learn how to create multi-Region keyspaces, see
  [Create a multi-Region keyspace in Amazon Keyspaces](keyspaces-mrr-create.md "keyspaces-mrr-create.md").

###### To create a keyspace using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**.
3. Choose **Create keyspace**.
4. In the **Keyspace name** box, enter
   `catalog` as the name for your
   keyspace.

**Name constraints:**

    * The name can't be empty.
    * Allowed characters: alphanumeric characters and underscore ( `_` ).
    * Maximum length is 48 characters.

5.  Under **AWS Regions**, confirm that **Single-Region replication** is the
    replication strategy for the keyspace.
6.  To create the keyspace, choose **Create
    keyspace**.
7.  Verify that the keyspace `catalog` was created by doing
    the following:

        1. In the navigation pane, choose **Keyspaces**.
        2. Locate your keyspace `catalog` in the list of keyspaces.

    The following procedure creates a keyspace using CQL.

###### To create a keyspace using CQL

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update `us-east-1` with your
   own Region.

```
cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
```

The output of that command should look like this.

```
`Connected to Amazon Keyspaces at cassandra.us-east-1.amazonaws.com:9142
[cqlsh 6.1.0 | Cassandra 3.11.2 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh current consistency level is ONE.`
```

2. Create your keyspace using the following CQL command.

```
CREATE KEYSPACE catalog WITH REPLICATION = {'class': 'SingleRegionStrategy'};
```

`SingleRegionStrategy` uses a replication factor of three and
replicates data across three AWS Availability Zones in its Region.

###### Note

Amazon Keyspaces defaults all input to lowercase unless you enclose it in
quotation marks. 3. Verify that your keyspace was created.

```
SELECT * from system_schema.keyspaces;
```

The output of this command should look similar to this.

```
`cqlsh> SELECT * from system_schema.keyspaces;

 keyspace_name | durable_writes | replication
-------------------------+----------------+-------------------------------------------------------------------------------------
 system_schema | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
 system_schema_mcs | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
 system | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
 system_multiregion_info | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
 catalog | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}

(5 rows)`
```

The following procedure creates a keyspace using the AWS CLI.

###### To create a keyspace using the AWS CLI

1. To confirm that your environment is setup, you can run the following command in CloudShell.

```
aws keyspaces help
```

2. Create your keyspace using the following AWS CLI statement.

```
aws keyspaces create-keyspace --keyspace-name 'catalog'
```

3. Verify that your keyspace was created with the following AWS CLI statement

```
aws keyspaces get-keyspace --keyspace-name 'catalog'
```

The output of this command should look similar to this example.

```
`{
 "keyspaceName": "catalog",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/catalog/",
 "replicationStrategy": "SINGLE_REGION"
}`
```
