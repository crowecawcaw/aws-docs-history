# Accessing DynamoDB

You can access Amazon DynamoDB using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the DynamoDB
API.

###### Topics

- [Using the console](#ConsoleDynamoDB "#ConsoleDynamoDB")
- [Using the AWS CLI](#Tools.CLI "#Tools.CLI")
- [Using the API](#Using.API "#Using.API")
- [Using the NoSQL workbench for DynamoDB](#Using.Workbench "#Using.Workbench")
- [IP address ranges](#Using.IPRanges "#Using.IPRanges")
- [Dual-stack endpoints for Internet Protocol version 6
  (IPv6)](#dual-stackipv4-6 "#dual-stackipv4-6")

## Using the console

You can access the AWS Management Console for Amazon DynamoDB at [https://console.aws.amazon.com/dynamodb/home](https://console.aws.amazon.com/dynamodb/home "https://console.aws.amazon.com/dynamodb/home").

Here are some of the actions you can perform in the DynamoDB console:

- **Manage tables**: Create, update, and delete
  tables. The capacity calculator can help estimate capacity requirements.
- **Interact with data**: View, add, update, and
  delete items in your tables. Manage Time to Live (TTL) settings.
- **Monitor and analyze**: View dashboards, monitor
  and set up alarms, and analyze metrics and alerts for your DynamoDB
  tables.
- **Optimize and extend**: Manage secondary
  indexes, streams, triggers, reserved capacity, and other advanced features to
  enhance your DynamoDB usage.

The DynamoDB console provides a comprehensive interface for managing your DynamoDB resources. We encourage you to access the console and interact with it to learn more.

## Using the AWS CLI

You can use the AWS Command Line Interface (AWS CLI) to control multiple AWS services from the command
line and automate them through scripts. You can use the AWS CLI for ad hoc operations,
such as creating a table. You can also use it to embed Amazon DynamoDB operations within
utility scripts.

Before you can use the AWS CLI with DynamoDB, you must get an access key ID and secret
access key. For more information, see [Granting programmatic
access](SettingUp.md#SettingUp.DynamoWebService.GetCredentials "SettingUp.md#SettingUp.DynamoWebService.GetCredentials") .

For a complete listing of all the commands available for DynamoDB in the AWS CLI, see the
[AWS CLI command
reference](../../../cli/latest/reference/dynamodb/index.md "../../../cli/latest/reference/dynamodb/index.md").

###### Topics

The AWS CLI is available at [http://aws.amazon.com/cli](https://aws.amazon.com/cli "https://aws.amazon.com/cli"). It runs on Windows, macOS, or Linux. After
you download the AWS CLI, follow these steps to install and configure it:

1. Go to the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").
2. Follow the instructions for [Installing the AWS CLI](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md") and [Configuring the
   AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").
   The command line format consists of a DynamoDB operation name followed by the
   parameters for that operation. The AWS CLI supports a shorthand syntax for the
   parameter values, as well as JSON.

For example, the following command creates a table named
_Music_. The partition key is
_Artist_, and the sort key is _SongTitle_.
(For easier readability, long commands in this section are broken into separate
lines.)

```
aws dynamodb create-table \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --table-class STANDARD
```

The following commands add new items to the table. These examples use a
combination of shorthand syntax and JSON.

```
aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}}' \
    --return-consumed-capacity TOTAL

aws dynamodb put-item \
    --table-name Music \
    --item '{
        "Artist": {"S": "Acme Band"},
        "SongTitle": {"S": "Happy Day"},
        "AlbumTitle": {"S": "Songs About Life"} }' \
    --return-consumed-capacity TOTAL
```

On the command line, it can be difficult to compose valid JSON. However, the
AWS CLI can read JSON files. For example, consider the following JSON code
snippet, which is stored in a file named
_key-conditions.json_.

```
{
    "Artist": {
        "AttributeValueList": [
            {
                "S": "No One You Know"
            }
        ],
        "ComparisonOperator": "EQ"
    },
    "SongTitle": {
        "AttributeValueList": [
            {
                "S": "Call Me Today"
            }
        ],
        "ComparisonOperator": "EQ"
    }
}
```

You can now issue a `Query` request using the AWS CLI. In this
example, the contents of the _key-conditions.json_ file are
used for the `--key-conditions` parameter.

```
aws dynamodb query --table-name Music --key-conditions file://key-conditions.json
```

The AWS CLI can also interact with DynamoDB local (downloadable version) that runs
on your computer. To enable this, add the following parameter to each
command:

`--endpoint-url http://localhost:8000`

The following example uses the AWS CLI to list the tables in a local
database.

```
aws dynamodb list-tables --endpoint-url http://localhost:8000
```

If DynamoDB is using a port number other than the default (8000), modify the
`--endpoint-url` value accordingly.

###### Note

The AWS CLI can't use the DynamoDB local (downloadable version) as a default
endpoint. Therefore, you must specify `--endpoint-url` with each
command.

## Using the API

You can use the AWS Management Console and the AWS Command Line Interface to work interactively with Amazon DynamoDB.
However, to get the most out of DynamoDB, you can write application code using the AWS
SDKs.

The AWS SDKs provide broad support for DynamoDB in [Java](https://aws.amazon.com/sdk-for-java "https://aws.amazon.com/sdk-for-java"), [JavaScript in the browser](https://aws.amazon.com/sdk-for-browser "https://aws.amazon.com/sdk-for-browser"), [.NET](https://aws.amazon.com/sdk-for-net "https://aws.amazon.com/sdk-for-net"), [Node.js](https://aws.amazon.com/sdk-for-node-js "https://aws.amazon.com/sdk-for-node-js"), [PHP](https://aws.amazon.com/sdk-for-php "https://aws.amazon.com/sdk-for-php"), [Python](https://aws.amazon.com/sdk-for-python "https://aws.amazon.com/sdk-for-python"), [Ruby](https://aws.amazon.com/sdk-for-ruby "https://aws.amazon.com/sdk-for-ruby"), [C++](https://aws.amazon.com/sdk-for-cpp "https://aws.amazon.com/sdk-for-cpp"), [Go](https://aws.amazon.com/sdk-for-go "https://aws.amazon.com/sdk-for-go"), [Android](https://aws.amazon.com/mobile/sdk/ "https://aws.amazon.com/mobile/sdk/"), and [iOS](https://aws.amazon.com/mobile/sdk/ "https://aws.amazon.com/mobile/sdk/").
.

Before you can use the AWS SDKs with DynamoDB, you must get an AWS access key ID and
secret access key. For more information, see [Setting up DynamoDB (web service)](SettingUp.md "SettingUp.md") .

For a high-level overview of DynamoDB application programming with the AWS SDKs, see
[Programming with DynamoDB and the AWS SDKs](Programming.md "Programming.md").

## Using the NoSQL workbench for DynamoDB

You can also access DynamoDB by downloading and using the [NoSQL Workbench for DynamoDB](workbench.md "workbench.md").

NoSQL Workbench for Amazon DynamoDB is a cross-platform, client-side GUI application that
you can use for modern database development and operations. It's available for Windows,
macOS, and Linux. NoSQL Workbench is a visual development tool that provides data
modeling, data visualization, and query development features to help you design, create,
query, and manage DynamoDB tables. NoSQL Workbench now includes DynamoDB local as an optional
part of the installation process, which makes it easier to model your data in
DynamoDB local. To learn more about DynamoDB local and its requirements, see [Setting up DynamoDB local (downloadable version)](DynamoDBLocal.md "DynamoDBLocal.md") .

###### Note

The NoSQL Workbench for DynamoDB currently doesn't support AWS logins that are
configured with two-factor authentication (2FA).

**Data modeling**

With NoSQL Workbench for DynamoDB, you can build new data models from, or
design models based on, existing data models that satisfy your application's
data access patterns. You can also import and export the designed data model
at the end of the process. For more information, see [Building data models with NoSQL Workbench](workbench.md "workbench.md").

**Operation building**

NoSQL Workbench provides a rich graphical user interface for you to
develop and test queries. You can use the _operation
builder_ to view, explore, and query live datasets. You can
also use the structured operation builder to build and perform data plane
operations. It supports projection and condition expression, and lets you
generate sample code in multiple languages. For more information, see [Exploring datasets and building operations with
NoSQL Workbench](workbench.md "workbench.md").

## IP address ranges

Amazon Web Services (AWS) publishes its current IP address ranges in JSON format. To view the
current ranges, download [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json "https://ip-ranges.amazonaws.com/ip-ranges.json"). For more information, see [AWS IP address ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md") in the
AWS General Reference.

To find the IP address ranges that you can use to [access
to DynamoDB tables and indexes](../APIReference/API_Operations_Amazon_DynamoDB.md "../APIReference/API_Operations_Amazon_DynamoDB.md"), search the ip-ranges.json file for the
following string: `"service": "DYNAMODB"`.

###### Note

The IP address ranges do not apply to DynamoDB Streams or DynamoDB Accelerator
(DAX).

## Dual-stack endpoints for Internet Protocol version 6

(IPv6)

DynamoDB offers dual-stack endpoints that are compatible with both IPv4 and IPv6. The
endpoint naming conventions are:

- `dynamodb.`<region>`.api.aws`
- ``<account-id>`.ddb.`<region>`.api.aws`
- `streams-dynamodb.`<region>`.api.aws`
- `dax.`<region>`.api.aws`
- `dynamodb-fips.`<region>`.api.aws`

For a complete list of DynamoDB endpoints and regional availability, see [Amazon DynamoDB endpoints and
quotas](../../../general/latest/gr/ddb.md "../../../general/latest/gr/ddb.md") topic in the _AWS General Reference
guide_.

For more information regarding setting up the AWS CLI to use dual-stack endpoints,
see [Set to use dual-stack endpoints for all AWS services](../../../cli/latest/userguide/cli-configure-endpoints.md#endpoints-dual-stack "../../../cli/latest/userguide/cli-configure-endpoints.md#endpoints-dual-stack")
section in the _AWS Command Line Interface
guide_.

For more information regarding setting up your SDK clients to use dual-stack
endpoints, see [Dual-stack and FIPS endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md") topic in the _AWS SDKs and Tools guide_.

Before using DynamoDB with IPv6, you must update your IAM user role or resourced-based
policies that you use for IP address filtering to include IPv6 address ranges. IP
address filtering policies that do not account for IPv6 address can result in access
issues. For more information, see [IP address condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress") section in the _AWS
Identity and Access Management guide_.
