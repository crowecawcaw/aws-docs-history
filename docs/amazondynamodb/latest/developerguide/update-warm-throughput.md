

# Increase your existing DynamoDB table's warm throughput
<a name="update-warm-throughput"></a>

After you've checked your DynamoDB table's current warm throughput value, you can update it with the following steps:

## AWS Management Console
<a name="warm-throughput-update-console"></a>

To check your DynamoDB table's warm throughput value using the DynamoDB console:

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/).

1. In the left navigation pane, choose Tables.

1. On the **Tables** page, choose your desired table.

1. In the **Warm throughput** field, select **Edit**.

1. On the **Edit warm throughput** page, choose **Increase warm throughput**.

1. Adjust the **read units per second** and **write units pers second**. These two settings define the throughput your table can instantly handle.

1. Select **Save**.

1. Your **read units per second** and **write units per second** will be updated in the **Warm throughput** field when the request finishes processing.
**Note**  
Updating your warm throughput value is an asynchronous task. The `Status` will change from `UPDATING` to `ACTIVE` when the update is complete.

## AWS CLI
<a name="warm-throughput-update-CLI"></a>

The following AWS CLI example shows you how to update your DynamoDB table's warm throughput value.

1. Run the `update-table` operation on your DynamoDB table.

   ```
   aws dynamodb update-table \
       --table-name GameScores \
       --warm-throughput ReadUnitsPerSecond=12345,WriteUnitsPerSecond=4567 \
       --global-secondary-index-updates \
           "[
               {
                   \"Update\": {
                       \"IndexName\": \"GameTitleIndex\",
                       \"WarmThroughput\": {
                           \"ReadUnitsPerSecond\": 88,
                           \"WriteUnitsPerSecond\": 77
                       }
                   }
               }
           ]" \
       --region us-east-1
   ```

1. You’ll receive a response similar to the one below. Your `WarmThroughput` settings will be displayed as `ReadUnitsPerSecond` and `WriteUnitsPerSecond`. The `Status` will be `UPDATING` when the warm throughput value is being updated, and `ACTIVE` when the new warm throughput value is set.

   ```
   {
       "TableDescription": {
           "AttributeDefinitions": [
               {
                   "AttributeName": "GameTitle",
                   "AttributeType": "S"
               },
               {
                   "AttributeName": "TopScore",
                   "AttributeType": "N"
               },
               {
                   "AttributeName": "UserId",
                   "AttributeType": "S"
               }
           ],
           "TableName": "GameScores",
           "KeySchema": [
               {
                   "AttributeName": "UserId",
                   "KeyType": "HASH"
               },
               {
                   "AttributeName": "GameTitle",
                   "KeyType": "RANGE"
               }
           ],
           "TableStatus": "ACTIVE",
           "CreationDateTime": 1730242189.965,
           "ProvisionedThroughput": {
               "NumberOfDecreasesToday": 0,
               "ReadCapacityUnits": 20,
               "WriteCapacityUnits": 10
           },
           "TableSizeBytes": 0,
           "ItemCount": 0,
           "TableArn": "arn:aws:dynamodb:us-east-1:XXXXXXXXXXXX:table/GameScores",
           "TableId": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
           "GlobalSecondaryIndexes": [
               {
                   "IndexName": "GameTitleIndex",
                   "KeySchema": [
                       {
                           "AttributeName": "GameTitle",
                           "KeyType": "HASH"
                       },
                       {
                           "AttributeName": "TopScore",
                           "KeyType": "RANGE"
                       }
                   ],
                   "Projection": {
                       "ProjectionType": "INCLUDE",
                       "NonKeyAttributes": [
                           "UserId"
                       ]
                   },
                   "IndexStatus": "ACTIVE",
                   "ProvisionedThroughput": {
                       "NumberOfDecreasesToday": 0,
                       "ReadCapacityUnits": 50,
                       "WriteCapacityUnits": 25
                   },
                   "IndexSizeBytes": 0,
                   "ItemCount": 0,
                   "IndexArn": "arn:aws:dynamodb:us-east-1:XXXXXXXXXXXX:table/GameScores/index/GameTitleIndex",
                   "WarmThroughput": {
                       "ReadUnitsPerSecond": 50,
                       "WriteUnitsPerSecond": 25,
                       "Status": "UPDATING"
                   }
               }
           ],
           "DeletionProtectionEnabled": false,
           "WarmThroughput": {
               "ReadUnitsPerSecond": 12300,
               "WriteUnitsPerSecond": 4500,
               "Status": "UPDATING"
           }
       }
   }
   ```

## AWS SDK
<a name="warm-throughput-update-SDK"></a>

The following SDK examples shows you how to update your DynamoDB table's warm throughput value.

------
#### [ Java ]

**SDK for Java 2.x**  
Update warm throughput setting on an existing DynamoDB table using AWS SDK for Java 2.x.  

```
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.model.GlobalSecondaryIndexUpdate;
import software.amazon.awssdk.services.dynamodb.model.UpdateGlobalSecondaryIndexAction;
import software.amazon.awssdk.services.dynamodb.model.UpdateTableRequest;
import software.amazon.awssdk.services.dynamodb.model.WarmThroughput;

    public static WarmThroughput buildWarmThroughput(final Long readUnitsPerSecond, final Long writeUnitsPerSecond) {
        return WarmThroughput.builder()
            .readUnitsPerSecond(readUnitsPerSecond)
            .writeUnitsPerSecond(writeUnitsPerSecond)
            .build();
    }

    /**
     * Updates a DynamoDB table with warm throughput settings for both the table and a global secondary index.
     *
     * @param ddb The DynamoDB client
     * @param tableName The name of the table to update
     * @param tableReadUnitsPerSecond Read units per second for the table
     * @param tableWriteUnitsPerSecond Write units per second for the table
     * @param globalSecondaryIndexName The name of the global secondary index to update
     * @param globalSecondaryIndexReadUnitsPerSecond Read units per second for the GSI
     * @param globalSecondaryIndexWriteUnitsPerSecond Write units per second for the GSI
     */
    public static void updateDynamoDBTable(
        final DynamoDbClient ddb,
        final String tableName,
        final Long tableReadUnitsPerSecond,
        final Long tableWriteUnitsPerSecond,
        final String globalSecondaryIndexName,
        final Long globalSecondaryIndexReadUnitsPerSecond,
        final Long globalSecondaryIndexWriteUnitsPerSecond) {

        final WarmThroughput tableWarmThroughput =
            buildWarmThroughput(tableReadUnitsPerSecond, tableWriteUnitsPerSecond);
        final WarmThroughput gsiWarmThroughput =
            buildWarmThroughput(globalSecondaryIndexReadUnitsPerSecond, globalSecondaryIndexWriteUnitsPerSecond);

        final GlobalSecondaryIndexUpdate globalSecondaryIndexUpdate = GlobalSecondaryIndexUpdate.builder()
            .update(UpdateGlobalSecondaryIndexAction.builder()
                .indexName(globalSecondaryIndexName)
                .warmThroughput(gsiWarmThroughput)
                .build())
            .build();

        final UpdateTableRequest request = UpdateTableRequest.builder()
            .tableName(tableName)
            .globalSecondaryIndexUpdates(globalSecondaryIndexUpdate)
            .warmThroughput(tableWarmThroughput)
            .build();

        try {
            ddb.updateTable(request);
        } catch (DynamoDbException e) {
            System.err.println(e.getMessage());
            throw e;
        }

        System.out.println(SUCCESS_MESSAGE);
    }
```
+  For API details, see [UpdateTable](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateTable) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
Update warm throughput setting on an existing DynamoDB table using AWS SDK for JavaScript.  

```
import { DynamoDBClient, UpdateTableCommand } from "@aws-sdk/client-dynamodb";

export async function updateDynamoDBTableWarmThroughput(
  tableName,
  tableReadUnits,
  tableWriteUnits,
  gsiName,
  gsiReadUnits,
  gsiWriteUnits,
  region = "us-east-1"
) {
  try {
    const ddbClient = new DynamoDBClient({ region: region });

    // Construct the update table request
    const updateTableRequest = {
      TableName: tableName,
      GlobalSecondaryIndexUpdates: [
        {
            Update: {
                IndexName: gsiName,
                WarmThroughput: {
                    ReadUnitsPerSecond: gsiReadUnits,
                    WriteUnitsPerSecond: gsiWriteUnits,
                },
            },
        },
      ],
      WarmThroughput: {
          ReadUnitsPerSecond: tableReadUnits,
          WriteUnitsPerSecond: tableWriteUnits,
      },
    };

    const command = new UpdateTableCommand(updateTableRequest);
    const response = await ddbClient.send(command);
    console.log(`Table updated successfully! Response: ${JSON.stringify(response)}`);
    return response;
  } catch (error) {
    console.error(`Error updating table: ${error}`);
    throw error;
  }
}

// Example usage (commented out for testing)
/*
updateDynamoDBTableWarmThroughput(
  'example-table',
  5, 5,
  'example-index',
  2, 2
);
*/
```
+  For API details, see [UpdateTable](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/dynamodb/command/UpdateTableCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
Update warm throughput setting on an existing DynamoDB table using AWS SDK for Python (Boto3).  

```
from boto3 import client
from botocore.exceptions import ClientError


def update_dynamodb_table_warm_throughput(
    table_name,
    table_read_units,
    table_write_units,
    gsi_name,
    gsi_read_units,
    gsi_write_units,
    region_name="us-east-1",
):
    """
    Updates the warm throughput of a DynamoDB table and a global secondary index.

    :param table_name: The name of the table to update.
    :param table_read_units: The new read units per second for the table's warm throughput.
    :param table_write_units: The new write units per second for the table's warm throughput.
    :param gsi_name: The name of the global secondary index to update.
    :param gsi_read_units: The new read units per second for the GSI's warm throughput.
    :param gsi_write_units: The new write units per second for the GSI's warm throughput.
    :param region_name: The AWS Region name to target. defaults to us-east-1
    :return: The response from the update_table operation
    """
    try:
        ddb = client("dynamodb", region_name=region_name)

        # Update the table's warm throughput
        table_warm_throughput = {
            "ReadUnitsPerSecond": table_read_units,
            "WriteUnitsPerSecond": table_write_units,
        }

        # Update the global secondary index's warm throughput
        gsi_warm_throughput = {
            "ReadUnitsPerSecond": gsi_read_units,
            "WriteUnitsPerSecond": gsi_write_units,
        }

        # Construct the global secondary index update
        global_secondary_index_update = [
            {"Update": {"IndexName": gsi_name, "WarmThroughput": gsi_warm_throughput}}
        ]

        # Construct the update table request
        update_table_request = {
            "TableName": table_name,
            "GlobalSecondaryIndexUpdates": global_secondary_index_update,
            "WarmThroughput": table_warm_throughput,
        }

        # Update the table
        response = ddb.update_table(**update_table_request)
        print("Table updated successfully!")
        return response  # Make sure to return the response
    except ClientError as e:
        print(f"Error updating table: {e}")
        raise e
```
+  For API details, see [UpdateTable](https://docs.aws.amazon.com/goto/boto3/dynamodb-2012-08-10/UpdateTable) in *AWS SDK for Python (Boto3) API Reference*. 

------