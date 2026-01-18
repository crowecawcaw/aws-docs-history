# Step 5: Copy data to

DynamoDB

In this step, you will copy data from the Hive table (`hive_features`)
to a new table in DynamoDB.

1.  Open the DynamoDB console at
    [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2.  Choose **Create Table**.
3.  On the **Create DynamoDB table** page, do the
    following:
    1. In **Table**, type
       `Features`.
    2. For **Primary key**, in the **Partition
       key** field, type `Id`. Set the
       data type to **Number**.

    Clear **Use Default Settings**. For
    **Provisioned Capacity**, type the
    following:

        * **Read Capacity
         Units**—`10`
        * **Write Capacity
         Units**—`10`Choose **Create**.

4.  At the Hive prompt, enter the following HiveQL statement:

```
CREATE EXTERNAL TABLE ddb_features
    (feature_id   BIGINT,
    feature_name  STRING,
    feature_class STRING,
    state_alpha   STRING,
    prim_lat_dec  DOUBLE,
    prim_long_dec DOUBLE,
    elev_in_ft    BIGINT)
STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
TBLPROPERTIES(
    "dynamodb.table.name" = "Features",
    "dynamodb.column.mapping"="feature_id:Id,feature_name:Name,feature_class:Class,state_alpha:State,prim_lat_dec:Latitude,prim_long_dec:Longitude,elev_in_ft:Elevation"
);
```

You have now established a mapping between Hive and the Features table in
DynamoDB. 5. Enter the following HiveQL statement to import data to DynamoDB:

```
INSERT OVERWRITE TABLE ddb_features
SELECT
    feature_id,
    feature_name,
    feature_class,
    state_alpha,
    prim_lat_dec,
    prim_long_dec,
    elev_in_ft
FROM hive_features;
```

Hive will submit a MapReduce job, which will be processed by your Amazon EMR
cluster. It will take several minutes to complete the job. 6. Verify that the data has been loaded into DynamoDB:

    1. In the DynamoDB console navigation pane, choose
     **Tables**.
    2. Choose the Features table, and then choose the
     **Items** tab to view the data.

###### Next step

[Step 6: Query the data
in the DynamoDB table](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")
