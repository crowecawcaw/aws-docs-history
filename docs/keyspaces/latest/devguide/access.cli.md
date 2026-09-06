

# Using the AWS CLI to connect to Amazon Keyspaces
<a name="access.cli"></a>

 You can use the AWS Command Line Interface (AWS CLI) to control multiple AWS services from the command line and automate them through scripts. With Amazon Keyspaces you can use the AWS CLI for data definition language (DDL) operations, such as creating a table. In addition, you can use infrastructure as code (IaC) services and tools such as AWS CloudFormation and Terraform.

Before you can use the AWS CLI with Amazon Keyspaces, you must get an access key ID and secret access key. For more information, see [Create and configure AWS credentials for Amazon Keyspaces](access.credentials.md).

For a complete listing of all the commands available for Amazon Keyspaces in the AWS CLI, see the [*AWS CLI Command Reference*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/index.html). 

**Topics**
+ [Downloading and Configuring the AWS CLI](#access.cli.installcli)
+ [Using the AWS CLI with Amazon Keyspaces](#access.cli.usingcli)

## Downloading and Configuring the AWS CLI
<a name="access.cli.installcli"></a>

The AWS CLI is available at [https://aws.amazon.com/cli](https://aws.amazon.com/cli). It runs on Windows, macOS, or Linux. After downloading the AWS CLI, follow these steps to install and configure it:

1. Go to the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)

1. Follow the instructions for [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

## Using the AWS CLI with Amazon Keyspaces
<a name="access.cli.usingcli"></a>

The command line format consists of a Amazon Keyspaces operation name followed by the parameters for that operation. The AWS CLI supports a shorthand syntax for the parameter values, as well as JSON. The following Amazon Keyspaces examples use AWS CLI shorthand syntax. For more information, see [Using shorthand syntax with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html).

The following command creates a keyspace with the name *catalog*.

```
aws keyspaces create-keyspace --keyspace-name 'catalog'
```

The command returns the resource Amazon Resource Name (ARN) in the output.

```
{
    "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/catalog/"
}
```

To confirm that the keyspace *catalog* exists, you can use the following command.

```
aws keyspaces get-keyspace --keyspace-name 'catalog'
```

The output of the command returns the following values.

```
{
    "keyspaceName": "catalog",
    "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/catalog/"
}
```

The following command creates a table with the name *book\_awards*. The partition key of the table consists of the columns `year` and `award` and the clustering key consists of the columns `category` and `rank`, both clustering columns use the ascending sort order. (For easier readability, long commands in this section are broken into separate lines.)

```
aws keyspaces create-table --keyspace-name 'catalog' --table-name 'book_awards' 
            --schema-definition 'allColumns=[{name=year,type=int},{name=award,type=text},{name=rank,type=int},
            {name=category,type=text}, {name=author,type=text},{name=book_title,type=text},{name=publisher,type=text}],
            partitionKeys=[{name=year},{name=award}],clusteringKeys=[{name=category,orderBy=ASC},{name=rank,orderBy=ASC}]'
```

This command results in the following output.

```
{
    "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/catalog/table/book_awards"
}
```

To confirm the metadata and properties of the table, you can use the following command.

```
aws keyspaces get-table --keyspace-name 'catalog' --table-name 'book_awards'
```

This command returns the following output.

```
{
    "keyspaceName": "catalog",
    "tableName": "book_awards",
    "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/catalog/table/book_awards",
    "creationTimestamp": 1645564368.628,
    "status": "ACTIVE",
    "schemaDefinition": {
        "allColumns": [
            {
                "name": "year",
                "type": "int"
            },
            {
                "name": "award",
                "type": "text"
            },
            {
                "name": "category",
                "type": "text"
            },
            {
                "name": "rank",
                "type": "int"
            },
            {
                "name": "author",
                "type": "text"
            },
            {
                "name": "book_title",
                "type": "text"
            },
            {
                "name": "publisher",
                "type": "text"
            }
        ],
        "partitionKeys": [
            {
                "name": "year"
            },
            {
                "name": "award"
            }
        ],
        "clusteringKeys": [
            {
                "name": "category",
                "orderBy": "ASC"
            },
            {
                "name": "rank",
                "orderBy": "ASC"
            }
        ],
        "staticColumns": []
    },
    "capacitySpecification": {
        "throughputMode": "PAY_PER_REQUEST",
        "lastUpdateToPayPerRequestTimestamp": 1645564368.628
    },
    "encryptionSpecification": {
        "type": "AWS_OWNED_KMS_KEY"
    },
    "pointInTimeRecovery": {
        "status": "DISABLED"
    },
    "ttl": {
        "status": "ENABLED"
    },
    "defaultTimeToLive": 0,
    "comment": {
        "message": ""
    }
}
```

When creating tables with complex schemas, it can be helpful to load the table's schema definition from a JSON file. The following is an example of this. Download the schema definition example JSON file from [schema\_definition.zip](samples/schema_definition.zip) and extract `schema_definition.json`, taking note of the path to the file. In this example, the schema definition JSON file is located in the current directory. For different file path options, see [ How to load parameters from a file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html#cli-usage-parameters-file-how).

```
aws keyspaces create-table --keyspace-name 'catalog' 
            --table-name 'book_awards' --schema-definition '{{file://schema_definition.json}}'
```

The following examples show how to create a simple table with the name *myTable* with additional options. Note that the commands are broken down into separate rows to improve readability. This command shows how to create a table and:
+ set the capacity mode of the table
+ enable Point-in-time recovery for the table
+ set the default Time to Live (TTL) value for the table to one year
+ add two tags for the table

```
aws keyspaces create-table --keyspace-name 'catalog' --table-name 'myTable' 
            --schema-definition 'allColumns=[{name=id,type=int},{name=name,type=text},{name=date,type=timestamp}],partitionKeys=[{name=id}]' 
            --capacity-specification 'throughputMode=PROVISIONED,readCapacityUnits=5,writeCapacityUnits=5' 
            --point-in-time-recovery 'status=ENABLED' 
            --default-time-to-live '31536000' 
            --tags 'key=env,value=test' 'key=dpt,value=sec'
```

This example shows how to create a new table that uses a customer managed key for encryption and has TTL enabled to allow you to set expiration dates for columns and rows. To run this sample, you must replace the resource ARN for the customer managed AWS KMS key with your own key and ensure Amazon Keyspaces has access to it.

```
aws keyspaces create-table --keyspace-name 'catalog' --table-name 'myTable' 
            --schema-definition 'allColumns=[{name=id,type=int},{name=name,type=text},{name=date,type=timestamp}],partitionKeys=[{name=id}]' 
            --encryption-specification 'type=CUSTOMER_MANAGED_KMS_KEY,kmsKeyIdentifier={{arn:aws:kms:us-east-1:111122223333:key/11111111-2222-3333-4444-555555555555}}'  
            --ttl 'status=ENABLED'
```