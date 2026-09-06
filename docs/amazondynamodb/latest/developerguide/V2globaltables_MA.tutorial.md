

# Tutorials: Creating multi-account global tables
<a name="V2globaltables_MA.tutorial"></a>

This section provides step-by-step instructions for creating DynamoDB global tables that span across multiple AWS accounts.

## Create a multi-account global table using the DynamoDB console
<a name="create-ma-gt-console"></a>

Follow these steps to create a multi-account global table using the AWS Management Console. The following example creates a global table with replica tables in the United States.

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/) for the first account (say {{111122223333}}).

1. For this example, choose **US East (Ohio)** from the Region selector in the navigation bar.

1. In the navigation pane on the left side of the console, choose **Tables**.

1. Choose **Create Table**.

1. On the **Create table** page:

   1. For **Table name**, enter **MusicTable**.

   1. For **Partition key**, enter **Artist**.

   1. For **Sort key**, enter **SongTitle**.

   1. Keep the other default settings and choose **Create table**.

1. Add the following resource policy to the table

------
#### [ JSON ]

****  

   ```
   {
   "Version":"2012-10-17",		 	 	 
   "Statement": [
       {
           "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
           "Effect": "Allow",
           "Action": [
               "dynamodb:ReadDataForReplication",
               "dynamodb:WriteDataForReplication",
               "dynamodb:ReplicateSettings"
           ],
           "Resource": "arn:aws:dynamodb:us-east-2:{{111122223333}}:table/MusicTable",
           "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
           "Condition": {
               "StringEquals": {
                   "aws:SourceAccount": ["{{444455556666}}","{{111122223333}}"],
                   "aws:SourceArn": [
                       "arn:aws:dynamodb:us-east-1:{{444455556666}}:table/MusicTable",
                       "arn:aws:dynamodb:us-east-2:{{111122223333}}:table/MusicTable"
                   ]
               }
           }
       },
       {
           "Sid": "AllowTrustedAccountsToJoinThisGlobalTable",
           "Effect": "Allow",
           "Action": [
               "dynamodb:AssociateTableReplica"
           ],
           "Resource": "arn:aws:dynamodb:us-east-2:{{111122223333}}:table/MusicTable",
           "Principal": {"AWS": ["{{444455556666}}"]}
       }
   ]
   }
   ```

------

1. This new table serves as the first replica table in a new global table. It is the prototype for other replica tables that you add later.

1. Wait for the table to become **Active**. For the newly created table, from the **Global tables** tab, navigate to **Settings Replication** and choose **Enable**.

1. Logout of this account ({{111122223333}} here).

1. Sign in to the AWS Management Console and open the DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/) for the second account (say {{444455556666}}).

1. For this example, choose **US East (N. Virginia)** from the Region selector in the navigation bar.

1. The console ensures that a table with the same name doesn't exist in the selected Region. If a table with the same name does exist, you must delete the existing table before you can create a new replica table in that Region.

1. In the drop down near **Create Table**, choose **Create from another account**

1. On the **Create table from another account** page:

   1. Add **arn:aws:dynamodb:us-east-2:{{111122223333}}:table/MusicTable** as the table arn for the source table.

   1. In the **Replica Table ARNs**, add the ARN of the source table again **arn:aws:dynamodb:us-east-2:{{111122223333}}:table/MusicTable**. If there are multiple replicas already existing as part of a Multi Account Global Table, you must add every existing replica to the ReplicaTableARN.

   1. In the **Resource-based policy** section, add the following resource policy for the table in this account ({{444455556666}}). Multi-account global table replication is bi-directional, so each replica table must grant the DynamoDB replication service and the other participating account the permissions required to replicate. This mirrors the policy you added in the first account, with the account references reversed:

      ```
      {
          "Version": "2012-10-17", 		 	 	 
          "Statement": [
              {
                  "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
                  "Effect": "Allow",
                  "Action": [
                      "dynamodb:ReadDataForReplication",
                      "dynamodb:WriteDataForReplication",
                      "dynamodb:ReplicateSettings"
                  ],
                  "Resource": "arn:aws:dynamodb:us-east-1:444455556666:table/MusicTable",
                  "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
                  "Condition": {
                      "StringEquals": {
                          "aws:SourceAccount": ["444455556666","111122223333"],
                          "aws:SourceArn": [
                              "arn:aws:dynamodb:us-east-1:444455556666:table/MusicTable",
                              "arn:aws:dynamodb:us-east-2:111122223333:table/MusicTable"
                          ]
                      }
                  }
              }
          ]
      }
      ```

   1. Keep the other default settings and choose **Submit**.

1. The **Global tables** tab for the Music table (and for any other replica tables) shows that the table has been replicated in multiple Regions.

1. To test replication:

   1. You can use any of the regions where a replica exists for this table

   1. Choose **Explore table items**.

   1. Choose **Create item**.

   1. Enter **item\_1** for **Artist** and **Song Value 1** for **SongTitle**.

   1. Choose **Create item**.

   1. Verify replication by switching to the other regions:

   1. Verify that the Music table contains the item you created.

## Create a multi-account global table using the AWS CLI
<a name="ma-gt-cli"></a>

The following examples show how to create a multi-account global table using the AWS CLI. These examples demonstrate the complete workflow for setting up cross-account replication.

------
#### [ CLI ]

Use the following AWS CLI commands to create a multi-account global table with cross-account replication.

```
# STEP 1: Setting resource policy for the table in account 111122223333

cat > /tmp/source-resource-policy.json << 'EOF'
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:ReadDataForReplication",
                "dynamodb:WriteDataForReplication",
                "dynamodb:ReplicateSettings"
            ],
            "Resource": "arn:aws:dynamodb:us-east-2:111122223333:table/MusicTable",
            "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": ["444455556666","111122223333"],
                    "aws:SourceArn": [
                        "arn:aws:dynamodb:us-east-1:444455556666:table/MusicTable",
                        "arn:aws:dynamodb:us-east-2:111122223333:table/MusicTable"
                    ]
                }
            }
        },
        {
            "Sid": "AllowTrustedAccountsToJoinThisGlobalTable",
            "Effect": "Allow",
            "Action": [
                "dynamodb:AssociateTableReplica"
            ],
            "Resource": "arn:aws:dynamodb:us-east-2:111122223333:table/MusicTable",
            "Principal": {"AWS": ["444455556666"]}
        }
    ]
}
EOF

# Step 2: Create a new table (MusicTable) in US East (Ohio), 
#   with DynamoDB Streams enabled (NEW_AND_OLD_IMAGES),
#   and Settings Replication ENABLED on the account 111122223333

aws dynamodb create-table \
    --table-name MusicTable \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --stream-specification StreamEnabled=true,StreamViewType=NEW_AND_OLD_IMAGES \
    --global-table-settings-replication-mode ENABLED \
    --resource-policy file:///tmp/source-resource-policy.json \
    --region us-east-2 


# Step 3: Creating replica table in account 444455556666

# Resource policy for account 444455556666
cat > /tmp/dest-resource-policy.json << 'EOF'
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "DynamoDBActionsNeededForSteadyStateReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:ReadDataForReplication",
                "dynamodb:WriteDataForReplication",
                "dynamodb:ReplicateSettings"
            ],
            "Resource": "arn:aws:dynamodb:us-east-1:444455556666:table/MusicTable",
            "Principal": {"Service": ["replication.dynamodb.amazonaws.com"]},
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": ["444455556666","111122223333"],
                    "aws:SourceArn": [
                        "arn:aws:dynamodb:us-east-1:444455556666:table/MusicTable",
                        "arn:aws:dynamodb:us-east-2:111122223333:table/MusicTable"
                    ]
                }
            }
        }
    ]
}
EOF

# Execute the replica table creation
aws dynamodb create-table \
    --table-name MusicTable \
    --global-table-source-arn "arn:aws:dynamodb:us-east-2:111122223333:table/MusicTable" \
    --resource-policy file:///tmp/dest-resource-policy.json \
    --global-table-settings-replication-mode ENABLED \
    --region us-east-1

# Step 4: View the list of replicas created using describe-table
aws dynamodb describe-table \
    --table-name MusicTable \
    --region us-east-2 \
    --query 'Table.{TableName:TableName,TableStatus:TableStatus,MultiRegionConsistency:MultiRegionConsistency,Replicas:Replicas[*].{Region:RegionName,Status:ReplicaStatus}}'

# Step 5: To verify that replication is working, add a new item to the Music table in US East (Ohio)
aws dynamodb put-item \
    --table-name MusicTable \
    --item '{"Artist": {"S":"item_1"},"SongTitle": {"S":"Song Value 1"}}' \
    --region us-east-2

# Step 6: Wait for a few seconds, and then check to see whether the item has been 
# successfully replicated to US East (N. Virginia) and Europe (Ireland)
aws dynamodb get-item \
    --table-name MusicTable \
    --key '{"Artist": {"S":"item_1"},"SongTitle": {"S":"Song Value 1"}}' \
    --region us-east-1

aws dynamodb get-item \
    --table-name MusicTable \
    --key '{"Artist": {"S":"item_1"},"SongTitle": {"S":"Song Value 1"}}' \
    --region us-east-2

# Step 7: Delete the replica table in US East (N. Virginia) Region
aws dynamodb delete-table \
    --table-name MusicTable \
    --region us-east-1

# Clean up: Delete the primary table
aws dynamodb delete-table \
    --table-name MusicTable \
    --region us-east-2
```

------