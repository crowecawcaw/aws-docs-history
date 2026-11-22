

# Getting started with DynamoDB caching

To get started with DynamoDB caching, create a serverless cache with DynamoDB caching enabled, then install and configure the Amazon ElastiCache integration client in your application. DynamoDB caching must be enabled when you create the serverless cache.

**Topics**
+ [Creating a new serverless cache with DynamoDB caching](#ddb-caching-create-cache)
+ [Disabling DynamoDB caching](#ddb-caching-disabling)
+ [Using the ElastiCache integration client](#ddb-caching-using-client)

## Creating a new serverless cache with DynamoDB caching
<a name="ddb-caching-create-cache"></a>

You enable DynamoDB caching when you create an ElastiCache Serverless for Valkey cache. For more information about creating a serverless cache, see [Create a Valkey serverless cache](GettingStarted.serverless-valkey.step1.md).

**AWS Management Console**

To create a new serverless cache with DynamoDB caching using the ElastiCache console:

1. Open the ElastiCache console at [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/). If you are not already signed in, sign in when prompted.

1. In the left navigation pane, choose **Valkey caches**.

1. On the **Valkey caches** page, choose **Create cache**.

1. On the **Create Valkey cache** page, in the **Configuration** section, ensure that **Valkey** is selected for the engine, **Serverless** is selected as the deployment option, and **New cache** is selected as the creation method.

1. In the **Settings** section, enter your preferred values for **Name** and **Description**, and ensure that **Engine version** is set to 9 or greater.

1. In the **Default settings** section, choose **Customize default settings**.

1. In the **Integrations** section, select **DynamoDB caching**.

1. In the **Connectivity** section, configure your preferred connectivity options.

1. In the **Security** section, **Access Control** is automatically set to IAM Authentication with a default IAM user group selected. If you prefer to use a different IAM user group, select it.

1. Choose **Create**.

Your serverless cache with DynamoDB caching is displayed with a **Creating** status, and updates to **Available** status when it is ready to use.

**AWS CLI**

The following AWS CLI example creates a new serverless cache with DynamoDB caching enabled using the create-serverless-cache command.

```
aws elasticache create-serverless-cache \
    --serverless-cache-name my-ddb-cache \
    --engine valkey \
    --major-engine-version 9 \
    --integrations IntegrationType=DYNAMODB \
    --user-group-id default.iam-user-group
```

## Disabling DynamoDB caching
<a name="ddb-caching-disabling"></a>

You cannot disable DynamoDB caching on a serverless cache already configured for DynamoDB caching. If you no longer want to enable DynamoDB caching for a cache, you must create a new serverless cache from a backup and delete the existing cache.

## Using the ElastiCache integration client
<a name="ddb-caching-using-client"></a>

To enable DynamoDB caching in your application, you install the ElastiCache integration client library and configure integration settings in your application, including which Amazon DynamoDB tables to cache and the TTL settings for each table. No changes are required to code that makes requests to DynamoDB. Requests to DynamoDB tables not configured for caching are routed directly to DynamoDB.

The following example Python code enables caching for all DynamoDB tables accessed by this application:

```
import boto3
# import the ElastiCache integration client
import aws_elasticache_integration_client

ddb = boto3.client("dynamodb", region_name="us-east-1")

# enable DynamoDB caching for all tables
aws_elasticache_integration_client.install(
    client=ddb, endpoint="my-cache:6379", cache_name="my-cache"
)

# No changes required to code that accesses DynamoDB.
# The item projection will be automatically returned from the cache.
response = ddb.get_item(
    TableName="my-table",
    Key={"id": {"S": "1"}},
    ProjectionExpression="myattr_1, myattr_2"
)
```

ElastiCache integration client libraries are available for multiple languages. For more information, see [elasticache-integration-client](https://github.com/awslabs/elasticache-integration-client) on the GitHub website.