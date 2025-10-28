# Enable time to live (TTL) in DynamoDB

###### Note

To assist in debugging and verification of proper operation of the TTL feature, the
values provided for the item TTL are logged in plaintext in DynamoDB diagnostic
logs.

You can enable TTL in the Amazon DynamoDB Console, the AWS Command Line Interface (AWS CLI), or using the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md") with any of the supposed AWS SDKs. It takes approximately one hour to
enable TTL across all partitions.

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. Choose **Tables**, and then choose the table that you
   want to modify.
3. In the **Additional settings** tab, in the **Time
   to Live (TTL)** section, choose **Turn on** to
   enable TTL.
4. When enabling TTL on a table, DynamoDB requires you to identify a specific
   attribute name that the service will look for when determining if an item is
   eligible for expiration. The TTL attribute name, shown below, is case
   sensitive and must match the attribute defined in your read and write
   operations. A mismatch will cause expired items to go undeleted. Renaming
   the TTL attribute requires you to disable TTL and then re-enable it with the
   new attribute going forward. TTL will continue to process deletions for
   approximately 30 minutes once it is disabled. TTL must be reconfigured on
   restored tables.

![Case-sensitive TTL attribute name that DynamoDB uses to determine an item's eligiblity for expiration.](images/EnableTTL-Settings.png) 5. (Optional) You can perform a test by simulating the date and time of the
expiration and matching a few items. This provides you with a sample list of
items and confirms that there are items containing the TTL attribute name
provided along with the expiration time.
After TTL is enabled, the TTL attribute is marked **TTL** when you view items on the DynamoDB console. You can view the date
and time that an item expires by hovering your pointer over the attribute.

Python
You can enable TTL with code, using the [UpdateTimeToLive](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_time_to_live.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/update_time_to_live.html") operation.

```
import boto3


def enable_ttl(table_name, ttl_attribute_name):
    """
    Enables TTL on DynamoDB table for a given attribute name
        on success, returns a status code of 200
        on error, throws an exception

    :param table_name: Name of the DynamoDB table
    :param ttl_attribute_name: The name of the TTL attribute being provided to the table.
    """
    try:
        dynamodb = boto3.client('dynamodb')

        # Enable TTL on an existing DynamoDB table
        response = dynamodb.update_time_to_live(
            TableName=table_name,
            TimeToLiveSpecification={
                'Enabled': True,
                'AttributeName': ttl_attribute_name
            }
        )

        # In the returned response, check for a successful status code.
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("TTL has been enabled successfully.")
        else:
            print(f"Failed to enable TTL, status code {response['ResponseMetadata']['HTTPStatusCode']}")
    except Exception as ex:
        print("Couldn't enable TTL in table %s. Here's why: %s" % (table_name, ex))
        raise


# your values
enable_ttl('your-table-name', 'expirationDate')
```

You can confirm TTL is enabled by using the [DescribeTimeToLive](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_time_to_live.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/describe_time_to_live.html") operation, which describes the TTL
status on a table. The `TimeToLive` status is either
`ENABLED` or `DISABLED`.

```
# create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# set the table name
table_name = 'YourTable'

# describe TTL
response = dynamodb.describe_time_to_live(TableName=table_name)
```

JavaScript
You can enable TTL with code, using the [UpdateTimeToLiveCommand](../../../AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-dynamodb/Class/UpdateTimeToLiveCommand.md "../../../AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-client-dynamodb/Class/UpdateTimeToLiveCommand.md") operation.

```
import { DynamoDBClient, UpdateTimeToLiveCommand } from "@aws-sdk/client-dynamodb";

const enableTTL = async (tableName, ttlAttribute) => {

    const client = new DynamoDBClient({});

    const params = {
        TableName: tableName,
        TimeToLiveSpecification: {
            Enabled: true,
            AttributeName: ttlAttribute
        }
    };

    try {
        const response = await client.send(new UpdateTimeToLiveCommand(params));
        if (response.$metadata.httpStatusCode === 200) {
            console.log(`TTL enabled successfully for table ${tableName}, using attribute name ${ttlAttribute}.`);
        } else {
            console.log(`Failed to enable TTL for table ${tableName}, response object: ${response}`);
        }
        return response;
    } catch (e) {
        console.error(`Error enabling TTL: ${e}`);
        throw e;
    }
};

// call with your own values
enableTTL('ExampleTable', 'exampleTtlAttribute');
```

1. Enable TTL on the `TTLExample` table.

```
aws dynamodb update-time-to-live --table-name TTLExample --time-to-live-specification "Enabled=true, AttributeName=ttl"
```

2. Describe TTL on the `TTLExample` table.

```
aws dynamodb describe-time-to-live --table-name TTLExample
{
    "TimeToLiveDescription": {
        "AttributeName": "ttl",
        "TimeToLiveStatus": "ENABLED"
    }
}
```

3. Add an item to the `TTLExample` table with the Time to Live attribute
   set using the BASH shell and the AWS CLI.

```
EXP=`date -d '+5 days' +%s`
aws dynamodb put-item --table-name "TTLExample" --item '{"id": {"N": "1"}, "ttl": {"N": "'$EXP'"}}'
```

This example starts with the current date and adds 5 days to it to create an
expiration time. Then, it converts the expiration time to epoch time format to
finally add an item to the "`TTLExample`" table.

###### Note

One way to set expiration values for Time to Live is to calculate the number of
seconds to add to the expiration time. For example, 5 days is 432,000 seconds.
However, it is often preferable to start with a date and work from there.

It is fairly simple to get the current time in epoch time format, as in the
following examples.

- Linux Terminal: `date +%s`
- Python: `import time; int(time.time())`
- Java: `System.currentTimeMillis() / 1000L`
- JavaScript: `Math.floor(Date.now() / 1000)`

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  TTLExampleTable:
    Type: AWS::DynamoDB::Table
    Description: "A DynamoDB table with TTL Specification enabled"
    Properties:
      AttributeDefinitions:
        - AttributeName: "Album"
          AttributeType: "S"
        - AttributeName: "Artist"
          AttributeType: "S"
      KeySchema:
        - AttributeName: "Album"
          KeyType: "HASH"
        - AttributeName: "Artist"
          KeyType: "RANGE"
      ProvisionedThroughput:
        ReadCapacityUnits: "5"
        WriteCapacityUnits: "5"
      TimeToLiveSpecification:
        AttributeName: "TTLExampleAttribute"
        Enabled: true
```

Additional details on using TTL within your AWS CloudFormation templates can be found [here](../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-timetolivespecification.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-timetolivespecification.md").
