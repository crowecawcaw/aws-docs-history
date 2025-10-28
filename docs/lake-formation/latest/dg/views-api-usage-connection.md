# Creating AWS Glue connections to validate

status

To create or update a AWS Glue Data Catalog view using the `CreateTable` or
`UpdateTable` operations, you must create a new type of AWS Glue
connection for validation, and provide it to the supported analytics engine. These
connections are required to use Data Catalog views with Athena or Amazon Redshift. You can create
these connections only using the AWS CLI, AWS SDKs, or AWS Glue APIs. You can't use the
AWS Management Console to create the AWS Glue connection.

###### Note

If the view definer role and the role calling `CreateTable` or `UpdateTable` are different, then both of them require `glue:PassConnection` permission in their IAM policy statement.

For more information, see the [create-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-connection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-connection.html") AWS CLI documentation.

###### AWS CLI command for creating a connection

The following is an AWS CLI command for creating a connection:

```
aws glue create-connection --region us-east-1
--endpoint-url https://glue.us-east-1.amazonaws.com
--cli-input-json file:///root/path/to/create-connection.json
```

###### AWS CLI input JSON

For Amazon Redshift:

```
{
    "CatalogId": "123456789012",
    "ConnectionInput": {
        "ConnectionType": "VIEW_VALIDATION_REDSHIFT",
        "Name": "views-preview-cluster-connection-2",
        "Description": "My first Amazon Redshift validation connection",
        "ConnectionProperties": {
            "DATABASE": "dev",
            "CLUSTER_IDENTIFIER": "glue-data-catalog-views-preview-cluster"
        }
    }
}
```

For Amazon Athena:

```
{
    "CatalogId": "123456789012",
    "ConnectionInput": {
        "ConnectionType": "VIEW_VALIDATION_ATHENA",
        "Name": "views-preview-cluster-connection-3",
        "Description": "My first Amazon Athena validation connection",
        "ConnectionProperties": {
            "WORKGROUP_NAME": "workgroup-name"
        }
    }
}
```
