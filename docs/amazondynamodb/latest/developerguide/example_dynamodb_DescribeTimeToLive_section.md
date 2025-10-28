# Use `DescribeTimeToLive` with an AWS SDK or CLI

The following code examples show how to use `DescribeTimeToLive`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Work with Streams and Time-to-Live](example_dynamodb_Scenario_StreamsAndTTL_section.md "example_dynamodb_Scenario_StreamsAndTTL_section.md")

CLI

**AWS CLI**

**To view Time to Live settings for a table**

The following `describe-time-to-live` example displays Time to Live settings for the `MusicCollection` table.

```
`aws dynamodb describe-time-to-live \
 --table-name `MusicCollection``

```

Output:

```
{
    "TimeToLiveDescription": {
        "TimeToLiveStatus": "ENABLED",
        "AttributeName": "ttl"
    }
}
```

For more information, see [Time to Live](TTL.md "TTL.md") in the _Amazon DynamoDB Developer Guide_.

- For API details, see
  [DescribeTimeToLive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-time-to-live.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/describe-time-to-live.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

Describe TTL configuration on an existing DynamoDB table using AWS SDK for Java 2.x.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.DescribeTimeToLiveRequest;
import software.amazon.awssdk.services.dynamodb.model.DescribeTimeToLiveResponse;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.model.ResourceNotFoundException;

import java.util.logging.Level;
import java.util.logging.Logger;

    public DescribeTimeToLiveResponse describeTTL(final String tableName, final Region region) {
        final DescribeTimeToLiveRequest request =
            DescribeTimeToLiveRequest.builder().tableName(tableName).build();

        try (DynamoDbClient ddb = dynamoDbClient != null
            ? dynamoDbClient
            : DynamoDbClient.builder().region(region).build()) {
            return ddb.describeTimeToLive(request);
        } catch (ResourceNotFoundException e) {
            System.err.format(TABLE_NOT_FOUND_ERROR, tableName);
            throw e;
        } catch (DynamoDbException e) {
            System.err.println(e.getMessage());
            throw e;
        }
    }


```

- For API details, see
  [DescribeTimeToLive](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeTimeToLive.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeTimeToLive.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

Describe TTL configuration on an existing DynamoDB table using AWS SDK for JavaScript.

```
import { DynamoDBClient, DescribeTimeToLiveCommand } from "@aws-sdk/client-dynamodb";

export const describeTTL = async (tableName, region) => {
    const client = new DynamoDBClient({
        region: region,
        endpoint: `https://dynamodb.${region}.amazonaws.com`
    });

    try {
        const ttlDescription = await client.send(new DescribeTimeToLiveCommand({ TableName: tableName }));

        if (ttlDescription.TimeToLiveDescription.TimeToLiveStatus === 'ENABLED') {
            console.log("TTL is enabled for table %s.", tableName);
        } else {
            console.log("TTL is not enabled for table %s.", tableName);
        }

        return ttlDescription;
    } catch (e) {
        console.error(`Error describing table: ${e}`);
        throw e;
    }
}

// Example usage (commented out for testing)
// describeTTL('your-table-name', 'us-east-1');

```

- For API details, see
  [DescribeTimeToLive](../../../AWSJavaScriptSDK/v3/latest/client/dynamodb/command/DescribeTimeToLiveCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/dynamodb/command/DescribeTimeToLiveCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Python

**SDK for Python (Boto3)**

Describe TTL configuration on an existing DynamoDB table using AWS SDK for Python (Boto3).

```
import boto3


def describe_ttl(table_name, region):
    """
    Describes TTL on an existing table, as well as a region.

    :param table_name: String representing the name of the table
    :param region: AWS Region of the table - example `us-east-1`
    :return: Time to live description.
    """
    try:
        dynamodb = boto3.resource("dynamodb", region_name=region)
        ttl_description = dynamodb.describe_time_to_live(TableName=table_name)
        print(
            f"TimeToLive for table {table_name} is status {ttl_description['TimeToLiveDescription']['TimeToLiveStatus']}"
        )

        return ttl_description
    except Exception as e:
        print(f"Error describing table: {e}")
        raise


# Enter your own table name and AWS region
describe_ttl("your-table-name", "us-east-1")


```

- For API details, see
  [DescribeTimeToLive](../../../goto/boto3/dynamodb-2012-08-10/DescribeTimeToLive.md "../../../goto/boto3/dynamodb-2012-08-10/DescribeTimeToLive.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using DynamoDB with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
