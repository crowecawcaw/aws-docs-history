# Query Using the SQL Query Editor for AWS Config

(AWS CLI)

The AWS CLI is a unified tool to manage your AWS services. With just one tool to
download and configure, you can control multiple AWS services from the command line
and use scripts to automate them. For more information about the AWS CLI and for
instructions on installing the AWS CLI tools, see the following in the
_AWS Command Line Interface User Guide_.

- [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md")
- [Getting Set Up with the
  AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md")
  If necessary, enter `aws configure` to configure the AWS CLI to use an AWS
  Region where advanced queries are available.

## Considerations

**Prerequisites**

If you are using the one of the following AWS managed policies, you will have
the necessary permissions to run and save a query: [AWSServiceRoleForConfig](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForConfig "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForConfig") (service-linked role) or [AWS_ConfigRole](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS_ConfigRole "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS_ConfigRole").

Otherwise, you must have the permissions included in the [AWSConfigUserAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSConfigUserAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSConfigUserAccess") AWS managed policy.

**List of properties that you can query**

An updated list of properties and their data types is available in [GitHub](https://github.com/awslabs/aws-config-resource-schema "https://github.com/awslabs/aws-config-resource-schema").

**Advanced queries and aggregators**

To run a query on an aggregator, create an aggregator. For more information, see
[Creating Aggregators for AWS Config](aggregated-create.md "aggregated-create.md").

If you already have an aggregator set up, in the query scope, choose the
aggregator to run an advanced query on that aggregator. When you select an
aggregator, consider adding the AWS account ID and AWS Region in the query
statement to view that information in the results.

## Query Resource Configuration

Data

###### To query your resource configuration data using the query editor (AWS CLI) for

a single account and Region

1. Open a command prompt or a terminal window.
2. Enter the following command to query your resource configuration
   data.

```
aws configservice select-resource-config --expression "`SELECT resourceId WHERE resourceType='AWS::EC2::Instance'`"
```

Depending on your query, the output looks like the following.

```
{
    "QueryInfo": {
        "SelectFields": [
            {
                "Name": "resourceId"
            }
        ]
    },
    "Results": [
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}"
    ]
}
```

###### To query your resource configuration data using the query editor (AWS CLI) for

multiple accounts and Regions

1. Open a command prompt or a terminal window.
2. Enter the following command to query your resource configuration
   data.

```
aws configservice select-aggregate-resource-config --expression "`SELECT resourceId WHERE resourceType='AWS::EC2::Instance'`" --configuration-aggregator-name `my-aggregator`
```

Depending on your query, the output looks like the following.

```
{
    "QueryInfo": {
        "SelectFields": [
            {
                "Name": "resourceId"
            }
        ]
    },
    "Results": [
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}",
        "{\"resourceId\":\"`ResourceId`\"}"
    ]
}
```

###### Note

While using the `AWS::IAM::User`,
`AWS::IAM::Group`, `AWS::IAM::Role`, and
`AWS::IAM::Policy` resource types in an advanced query,
use `awsRegion = 'global'`.

## Save a Query

1. Open a command prompt or a terminal window.
2. Enter the following command to save a query.

```
aws configservice put-stored-query --stored-query "{\"QueryName\": \"cli-test\", \"Expression\": `\"SELECT *\", \"Description\": \"cli test query\" }"
 --tags "[{ \"Key\": \"first-tag\", \"Value\": \"\" }, { \"Key\": \"second-tag\", \"Value\": \"non-empty-tag-value\" }]"`
```

3. Depending on your query, the output looks like the following.

```
{
    "QueryArn": "arn:aws:config:eu-central-1:`Account ID`:stored-query/cli-test/query-e65mijt4rmam5pab"
}
```

###### Note

`--tags` is optional. When you pass the tags, the saved
tags will not be returned by either `list-stored-queries` or
`get-stored-query`. You must use
`list-tag-for-resources` to retrieve the associated tags
for a saved query.

`--description` is optional while creating or updating a
query.

## View all the Saved Queries

1. Enter the following command to view the list of all saved queries.

```
aws configservice list-stored-queries
```

2. Depending on your query, the output looks like the following.

```
{
    "StoredQueryMetadata": [
        {
            "QueryId": "query-e65mijt4rmam5pab",
            "QueryArn": "arn:aws:config:eu-central-1:`Account ID`:stored-query/cli-test/query-e65mijt4rmam5pab",
            "QueryName": "cli-test"
        },
        {
            "QueryId": "query-rltwlewlqfivadxq",
            "QueryArn": "arn:aws:config:eu-central-1:`Account ID`:stored-query/cli-test-2/query-rltwlewlqfivadxq",
            "QueryName": "cli-test-2",
            "Description": "cli test query"
        }
    ]
}
}
```

## Get Details of a Saved Query

1. Enter the following command to get details of a specific saved
   query.

```
aws configservice get-stored-query --query-name cli-test
```

2. Depending on your query, the output looks like the following.

```
{
    "StoredQuery": {
        "QueryId": "query-e65mijt4rmam5pab",
        "QueryArn": "arn:aws:config:eu-central-1:`Account ID`:stored-query/cli-test/query-e65mijt4rmam5pab",
        "QueryName": "cli-test",
        "Description": "cli test query",
        "Expression": "SELECT *"
    }
}
```

## Delete a Saved Query

- Enter the following command to delete your saved query.

```
aws configservice delete-stored-query --query-name cli-test
```

If successful, the command runs with no additional output.
