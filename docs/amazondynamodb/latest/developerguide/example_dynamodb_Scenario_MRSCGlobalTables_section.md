# Create and manage DynamoDB global tables with Multi-Region Strong Consistency using an AWS SDK

The following code examples show how to create and manage DynamoDB global tables with Multi-Region Strong Consistency (MRSC).

- Create a table with Multi-Region Strong Consistency.
- Verify MRSC configuration and replica status.
- Test strong consistency across Regions with immediate reads.
- Perform conditional writes with MRSC guarantees.
- Clean up MRSC global table resources.

Bash

**AWS CLI with Bash script**

Create a table with Multi-Region Strong Consistency.

```
# Step 1: Create a new table in us-east-2 (primary region for MRSC)
# Note: Table must be empty when enabling MRSC
aws dynamodb create-table \
    --table-name MusicTable \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --region us-east-2

# Wait for table to become active
aws dynamodb wait table-exists --table-name MusicTable --region us-east-2

# Step 2: Add replica and witness with Multi-Region Strong Consistency
# MRSC requires exactly three replicas in supported regions
aws dynamodb update-table \
    --table-name MusicTable \
    --replica-updates '[{"Create": {"RegionName": "us-east-1"}}]' \
    --global-table-witness-updates '[{"Create": {"RegionName": "us-west-2"}}]' \
    --multi-region-consistency STRONG \
    --region us-east-2


```

Verify MRSC configuration and replica status.

```
# Verify the global table configuration and MRSC setting
aws dynamodb describe-table \
    --table-name MusicTable \
    --region us-east-2 \
    --query 'Table.{TableName:TableName,TableStatus:TableStatus,MultiRegionConsistency:MultiRegionConsistency,Replicas:Replicas[*],GlobalTableWitnesses:GlobalTableWitnesses[*].{Region:RegionName,Status:ReplicaStatus}}'


```

Test strong consistency with immediate reads across Regions.

```
# Write an item to the primary region
aws dynamodb put-item \
    --table-name MusicTable \
    --item '{"Artist": {"S":"The Beatles"},"SongTitle": {"S":"Hey Jude"},"Album": {"S":"The Beatles 1967-1970"},"Year": {"N":"1968"}}' \
    --region us-east-2

# Read the item from replica region to verify strong consistency (cannot read or write to witness)
# No wait time needed - MRSC provides immediate consistency
echo "Reading from us-east-1 (immediate consistency):"
aws dynamodb get-item \
    --table-name MusicTable \
    --key '{"Artist": {"S":"The Beatles"},"SongTitle": {"S":"Hey Jude"}}' \
    --consistent-read \
    --region us-east-1


```

Perform conditional writes with MRSC guarantees.

```
# Perform a conditional update from a different region
# This demonstrates that conditions work consistently across all regions
aws dynamodb update-item \
    --table-name MusicTable \
    --key '{"Artist": {"S":"The Beatles"},"SongTitle": {"S":"Hey Jude"}}' \
    --update-expression "SET #rating = :rating" \
    --condition-expression "attribute_exists(Artist)" \
    --expression-attribute-names '{"#rating": "Rating"}' \
    --expression-attribute-values '{":rating": {"N":"5"}}' \
    --region us-east-1


```

Clean up MRSC global table resources.

```
# Remove replica tables (must be done before deleting the primary table)
aws dynamodb update-table \
    --table-name MusicTable \
    --replica-updates '[{"Delete": {"RegionName": "us-east-1"}}]' \
    --global-table-witness-updates '[{"Delete": {"RegionName": "us-west-2"}}]' \
    --region us-east-2

# Wait for replicas to be deleted
echo "Waiting for replicas to be deleted..."
sleep 30

# Delete the primary table
aws dynamodb delete-table \
    --table-name MusicTable \
    --region us-east-2


```

- For API details, see the following topics in _AWS CLI Command Reference_.
  - [CreateTable](../../../goto/aws-cli/dynamodb-2012-08-10/CreateTable.md "../../../goto/aws-cli/dynamodb-2012-08-10/CreateTable.md")
  - [DeleteTable](../../../goto/aws-cli/dynamodb-2012-08-10/DeleteTable.md "../../../goto/aws-cli/dynamodb-2012-08-10/DeleteTable.md")
  - [DescribeTable](../../../goto/aws-cli/dynamodb-2012-08-10/DescribeTable.md "../../../goto/aws-cli/dynamodb-2012-08-10/DescribeTable.md")
  - [GetItem](../../../goto/aws-cli/dynamodb-2012-08-10/GetItem.md "../../../goto/aws-cli/dynamodb-2012-08-10/GetItem.md")
  - [PutItem](../../../goto/aws-cli/dynamodb-2012-08-10/PutItem.md "../../../goto/aws-cli/dynamodb-2012-08-10/PutItem.md")
  - [UpdateItem](../../../goto/aws-cli/dynamodb-2012-08-10/UpdateItem.md "../../../goto/aws-cli/dynamodb-2012-08-10/UpdateItem.md")
  - [UpdateTable](../../../goto/aws-cli/dynamodb-2012-08-10/UpdateTable.md "../../../goto/aws-cli/dynamodb-2012-08-10/UpdateTable.md")

Java

**SDK for Java 2.x**

Create a regional table ready for MRSC conversion using AWS SDK for Java 2.x.

```
    public static CreateTableResponse createRegionalTable(final DynamoDbClient dynamoDbClient, final String tableName) {

        if (dynamoDbClient == null) {
            throw new IllegalArgumentException("DynamoDB client cannot be null");
        }
        if (tableName == null || tableName.trim().isEmpty()) {
            throw new IllegalArgumentException("Table name cannot be null or empty");
        }

        try {
            LOGGER.info("Creating regional table: " + tableName + " (must be empty for MRSC)");

            CreateTableRequest createTableRequest = CreateTableRequest.builder()
                .tableName(tableName)
                .attributeDefinitions(
                    AttributeDefinition.builder()
                        .attributeName("Artist")
                        .attributeType(ScalarAttributeType.S)
                        .build(),
                    AttributeDefinition.builder()
                        .attributeName("SongTitle")
                        .attributeType(ScalarAttributeType.S)
                        .build())
                .keySchema(
                    KeySchemaElement.builder()
                        .attributeName("Artist")
                        .keyType(KeyType.HASH)
                        .build(),
                    KeySchemaElement.builder()
                        .attributeName("SongTitle")
                        .keyType(KeyType.RANGE)
                        .build())
                .billingMode(BillingMode.PAY_PER_REQUEST)
                .build();

            CreateTableResponse response = dynamoDbClient.createTable(createTableRequest);
            LOGGER.info("Regional table creation initiated. Status: "
                + response.tableDescription().tableStatus());

            return response;

        } catch (DynamoDbException e) {
            LOGGER.severe("Failed to create regional table: " + tableName + " - " + e.getMessage());
            throw DynamoDbException.builder()
                .message("Failed to create regional table: " + tableName)
                .cause(e)
                .build();
        }
    }


```

Convert a regional table to MRSC with replicas and witness using AWS SDK for Java 2.x.

```
    public static UpdateTableResponse convertToMRSCWithWitness(
        final DynamoDbClient dynamoDbClient,
        final String tableName,
        final Region replicaRegion,
        final Region witnessRegion) {

        if (dynamoDbClient == null) {
            throw new IllegalArgumentException("DynamoDB client cannot be null");
        }
        if (tableName == null || tableName.trim().isEmpty()) {
            throw new IllegalArgumentException("Table name cannot be null or empty");
        }
        if (replicaRegion == null) {
            throw new IllegalArgumentException("Replica region cannot be null");
        }
        if (witnessRegion == null) {
            throw new IllegalArgumentException("Witness region cannot be null");
        }

        try {
            LOGGER.info("Converting table to MRSC with replica in " + replicaRegion.id() + " and witness in "
                + witnessRegion.id());

            // Create replica update using ReplicationGroupUpdate
            ReplicationGroupUpdate replicaUpdate = ReplicationGroupUpdate.builder()
                .create(CreateReplicationGroupMemberAction.builder()
                    .regionName(replicaRegion.id())
                    .build())
                .build();

            // Create witness update
            GlobalTableWitnessGroupUpdate witnessUpdate = GlobalTableWitnessGroupUpdate.builder()
                .create(CreateGlobalTableWitnessGroupMemberAction.builder()
                    .regionName(witnessRegion.id())
                    .build())
                .build();

            UpdateTableRequest updateTableRequest = UpdateTableRequest.builder()
                .tableName(tableName)
                .replicaUpdates(List.of(replicaUpdate))
                .globalTableWitnessUpdates(List.of(witnessUpdate))
                .multiRegionConsistency(MultiRegionConsistency.STRONG)
                .build();

            UpdateTableResponse response = dynamoDbClient.updateTable(updateTableRequest);
            LOGGER.info("MRSC conversion initiated. Status: "
                + response.tableDescription().tableStatus());
            LOGGER.info("UpdateTableResponse full object: " + response);
            return response;

        } catch (DynamoDbException e) {
            LOGGER.severe("Failed to convert table to MRSC: " + tableName + " - " + e.getMessage());
            throw DynamoDbException.builder()
                .message("Failed to convert table to MRSC: " + tableName)
                .cause(e)
                .build();
        }
    }


```

Describe an MRSC global table configuration using AWS SDK for Java 2.x.

```
    public static DescribeTableResponse describeMRSCTable(final DynamoDbClient dynamoDbClient, final String tableName) {

        if (dynamoDbClient == null) {
            throw new IllegalArgumentException("DynamoDB client cannot be null");
        }
        if (tableName == null || tableName.trim().isEmpty()) {
            throw new IllegalArgumentException("Table name cannot be null or empty");
        }

        try {
            LOGGER.info("Describing MRSC global table: " + tableName);

            DescribeTableRequest request =
                DescribeTableRequest.builder().tableName(tableName).build();

            DescribeTableResponse response = dynamoDbClient.describeTable(request);

            LOGGER.info("Table status: " + response.table().tableStatus());
            LOGGER.info("Multi-region consistency: " + response.table().multiRegionConsistency());

            if (response.table().replicas() != null
                && !response.table().replicas().isEmpty()) {
                LOGGER.info("Number of replicas: " + response.table().replicas().size());
                response.table()
                    .replicas()
                    .forEach(replica -> LOGGER.info(
                        "Replica region: " + replica.regionName() + ", Status: " + replica.replicaStatus()));
            }

            if (response.table().globalTableWitnesses() != null
                && !response.table().globalTableWitnesses().isEmpty()) {
                LOGGER.info("Number of witnesses: "
                    + response.table().globalTableWitnesses().size());
                response.table()
                    .globalTableWitnesses()
                    .forEach(witness -> LOGGER.info(
                        "Witness region: " + witness.regionName() + ", Status: " + witness.witnessStatus()));
            }

            return response;

        } catch (ResourceNotFoundException e) {
            LOGGER.severe("Table not found: " + tableName + " - " + e.getMessage());
            throw DynamoDbException.builder()
                .message("Table not found: " + tableName)
                .cause(e)
                .build();
        } catch (DynamoDbException e) {
            LOGGER.severe("Failed to describe table: " + tableName + " - " + e.getMessage());
            throw DynamoDbException.builder()
                .message("Failed to describe table: " + tableName)
                .cause(e)
                .build();
        }
    }


```

Add test items to verify MRSC strong consistency using AWS SDK for Java 2.x.

```
    public static PutItemResponse putTestItem(
        final DynamoDbClient dynamoDbClient,
        final String tableName,
        final String artist,
        final String songTitle,
        final String album,
        final String year) {

        if (dynamoDbClient == null) {
            throw new IllegalArgumentException("DynamoDB client cannot be null");
        }
        if (tableName == null || tableName.trim().isEmpty()) {
            throw new IllegalArgumentException("Table name cannot be null or empty");
        }
        if (artist == null || artist.trim().isEmpty()) {
            throw new IllegalArgumentException("Artist cannot be null or empty");
        }
        if (songTitle == null || songTitle.trim().isEmpty()) {
            throw new IllegalArgumentException("Song title cannot be null or empty");
        }

        try {
            LOGGER.info("Adding test item to MRSC global table: " + tableName);

            Map<String, AttributeValue> item = new HashMap<>();
            item.put("Artist", AttributeValue.builder().s(artist).build());
            item.put("SongTitle", AttributeValue.builder().s(songTitle).build());

            if (album != null && !album.trim().isEmpty()) {
                item.put("Album", AttributeValue.builder().s(album).build());
            }
            if (year != null && !year.trim().isEmpty()) {
                item.put("Year", AttributeValue.builder().n(year).build());
            }

            PutItemRequest putItemRequest =
                PutItemRequest.builder().tableName(tableName).item(item).build();

            PutItemResponse response = dynamoDbClient.putItem(putItemRequest);
            LOGGER.info("Test item added successfully with strong consistency");

            return response;

        } catch (DynamoDbException e) {
            LOGGER.severe("Failed to add test item to table: " + tableName + " - " + e.getMessage());
            throw DynamoDbException.builder()
                .message("Failed to add test item to table: " + tableName)
                .cause(e)
                .build();
        }
    }


```

Read items with consistent reads from MRSC replicas using AWS SDK for Java 2.x.

```
    public static GetItemResponse getItemWithConsistentRead(
        final DynamoDbClient dynamoDbClient, final String tableName, final String artist, final String songTitle) {

        if (dynamoDbClient == null) {
            throw new IllegalArgumentException("DynamoDB client cannot be null");
        }
        if (tableName == null || tableName.trim().isEmpty()) {
            throw new IllegalArgumentException("Table name cannot be null or empty");
        }
        if (artist == null || artist.trim().isEmpty()) {
            throw new IllegalArgumentException("Artist cannot be null or empty");
        }
        if (songTitle == null || songTitle.trim().isEmpty()) {
            throw new IllegalArgumentException("Song title cannot be null or empty");
        }

        try {
            LOGGER.info("Reading item from MRSC global table with consistent read: " + tableName);

            Map<String, AttributeValue> key = new HashMap<>();
            key.put("Artist", AttributeValue.builder().s(artist).build());
            key.put("SongTitle", AttributeValue.builder().s(songTitle).build());

            GetItemRequest getItemRequest = GetItemRequest.builder()
                .tableName(tableName)
                .key(key)
                .consistentRead(true)
                .build();

            GetItemResponse response = dynamoDbClient.getItem(getItemRequest);

            if (response.hasItem()) {
                LOGGER.info("Item found with strong consistency - no wait time needed");
            } else {
                LOGGER.info("Item not found");
            }

            return response;

        } catch (DynamoDbException e) {
            LOGGER.severe("Failed to read item from table: " + tableName + " - " + e.getMessage());
            throw DynamoDbException.builder()
                .message("Failed to read item from table: " + tableName)
                .cause(e)
                .build();
        }
    }


```

Perform conditional updates with MRSC guarantees using AWS SDK for Java 2.x.

```
    public static UpdateItemResponse performConditionalUpdate(
        final DynamoDbClient dynamoDbClient,
        final String tableName,
        final String artist,
        final String songTitle,
        final String rating) {

        if (dynamoDbClient == null) {
            throw new IllegalArgumentException("DynamoDB client cannot be null");
        }
        if (tableName == null || tableName.trim().isEmpty()) {
            throw new IllegalArgumentException("Table name cannot be null or empty");
        }
        if (artist == null || artist.trim().isEmpty()) {
            throw new IllegalArgumentException("Artist cannot be null or empty");
        }
        if (songTitle == null || songTitle.trim().isEmpty()) {
            throw new IllegalArgumentException("Song title cannot be null or empty");
        }
        if (rating == null || rating.trim().isEmpty()) {
            throw new IllegalArgumentException("Rating cannot be null or empty");
        }

        try {
            LOGGER.info("Performing conditional update on MRSC global table: " + tableName);

            Map<String, AttributeValue> key = new HashMap<>();
            key.put("Artist", AttributeValue.builder().s(artist).build());
            key.put("SongTitle", AttributeValue.builder().s(songTitle).build());

            Map<String, String> expressionAttributeNames = new HashMap<>();
            expressionAttributeNames.put("#rating", "Rating");

            Map<String, AttributeValue> expressionAttributeValues = new HashMap<>();
            expressionAttributeValues.put(
                ":rating", AttributeValue.builder().n(rating).build());

            UpdateItemRequest updateItemRequest = UpdateItemRequest.builder()
                .tableName(tableName)
                .key(key)
                .updateExpression("SET #rating = :rating")
                .conditionExpression("attribute_exists(Artist)")
                .expressionAttributeNames(expressionAttributeNames)
                .expressionAttributeValues(expressionAttributeValues)
                .build();

            UpdateItemResponse response = dynamoDbClient.updateItem(updateItemRequest);
            LOGGER.info("Conditional update successful - demonstrates strong consistency");

            return response;

        } catch (ConditionalCheckFailedException e) {
            LOGGER.warning("Conditional check failed: " + e.getMessage());
            throw e;
        } catch (DynamoDbException e) {
            LOGGER.severe("Failed to perform conditional update: " + tableName + " - " + e.getMessage());
            throw DynamoDbException.builder()
                .message("Failed to perform conditional update: " + tableName)
                .cause(e)
                .build();
        }
    }


```

Wait for MRSC replicas and witnesses to become active using AWS SDK for Java 2.x.

````
    public static void waitForMRSCReplicasActive(
        final DynamoDbClient dynamoDbClient, final String tableName, final int maxWaitTimeSeconds)
        throws InterruptedException {

        if (dynamoDbClient == null) {
            throw new IllegalArgumentException("DynamoDB client cannot be null");
        }
        if (tableName == null || tableName.trim().isEmpty()) {
            throw new IllegalArgumentException("Table name cannot be null or empty");
        }
        if (maxWaitTimeSeconds <= 0) {
            throw new IllegalArgumentException("Max wait time must be positive");
        }

        try {
            LOGGER.info("Waiting for MRSC replicas and witnesses to become active: " + tableName);

            final long startTime = System.currentTimeMillis();
            final long maxWaitTimeMillis = maxWaitTimeSeconds * 1000L;
            int backoffSeconds = 5; // Start with 5 second intervals
            final int maxBackoffSeconds = 30; // Cap at 30 seconds

            while (System.currentTimeMillis() - startTime < maxWaitTimeMillis) {
                DescribeTableResponse response = describeMRSCTable(dynamoDbClient, tableName);

                boolean allActive = true;
                StringBuilder statusReport = new StringBuilder();

                if (response.table().multiRegionConsistency() == null
|| !MultiRegionConsistency.STRONG .toString() .equals(response.table().multiRegionConsistency().toString())) { allActive = false; statusReport .append("MultiRegionConsistency: ") .append(response.table().multiRegionConsistency()) .append(" "); } if (response.table().replicas() == null
|| response.table().replicas().isEmpty()) { allActive = false; statusReport.append("No replicas found. "); } if (response.table().globalTableWitnesses() == null
|| response.table().globalTableWitnesses().isEmpty()) { allActive = false; statusReport.append("No witnesses found. "); } // Check table status if (!"ACTIVE".equals(response.table().tableStatus().toString())) { allActive = false; statusReport .append("Table: ") .append(response.table().tableStatus()) .append(" "); } // Check replica status if (response.table().replicas() != null) { for (var replica : response.table().replicas()) { if (!"ACTIVE".equals(replica.replicaStatus().toString())) { allActive = false; statusReport .append("Replica(") .append(replica.regionName()) .append("): ") .append(replica.replicaStatus()) .append(" "); } } } // Check witness status if (response.table().globalTableWitnesses() != null) { for (var witness : response.table().globalTableWitnesses()) { if (!"ACTIVE".equals(witness.witnessStatus().toString())) { allActive = false; statusReport .append("Witness(") .append(witness.regionName()) .append("): ") .append(witness.witnessStatus()) .append(" "); } } } if (allActive) { LOGGER.info("All MRSC replicas and witnesses are now active: " + tableName); return; } LOGGER.info("Waiting for MRSC components to become active. Status: " + statusReport.toString()); LOGGER.info("Next check in " + backoffSeconds + " seconds..."); tempWait(backoffSeconds); // Exponential backoff with cap backoffSeconds = Math.min(backoffSeconds * 2, maxBackoffSeconds); } throw DynamoDbException.builder() .message("Timeout waiting for MRSC replicas to become active after " + maxWaitTimeSeconds + " seconds") .build(); } catch (DynamoDbException | InterruptedException e) { LOGGER.severe("Failed to wait for MRSC replicas to become active: " + tableName + " - " + e.getMessage()); throw e; } } ``` Clean up MRSC replicas and witnesses using AWS SDK for Java 2.x. ``` public static UpdateTableResponse cleanupMRSCReplicas( final DynamoDbClient dynamoDbClient, final String tableName, final Region replicaRegion, final Region witnessRegion) { if (dynamoDbClient == null) { throw new IllegalArgumentException("DynamoDB client cannot be null"); } if (tableName == null || tableName.trim().isEmpty()) { throw new IllegalArgumentException("Table name cannot be null or empty"); } if (replicaRegion == null) { throw new IllegalArgumentException("Replica region cannot be null"); } if (witnessRegion == null) { throw new IllegalArgumentException("Witness region cannot be null"); } try { LOGGER.info("Cleaning up MRSC replicas and witnesses for table: " + tableName); // Remove replica using ReplicationGroupUpdate ReplicationGroupUpdate replicaUpdate = ReplicationGroupUpdate.builder() .delete(DeleteReplicationGroupMemberAction.builder() .regionName(replicaRegion.id()) .build()) .build(); // Remove witness GlobalTableWitnessGroupUpdate witnessUpdate = GlobalTableWitnessGroupUpdate.builder() .delete(DeleteGlobalTableWitnessGroupMemberAction.builder() .regionName(witnessRegion.id()) .build()) .build(); UpdateTableRequest updateTableRequest = UpdateTableRequest.builder() .tableName(tableName) .replicaUpdates(List.of(replicaUpdate)) .globalTableWitnessUpdates(List.of(witnessUpdate)) .build(); UpdateTableResponse response = dynamoDbClient.updateTable(updateTableRequest); LOGGER.info("MRSC cleanup initiated - removing replica and witness. Response: " + response); return response; } catch (DynamoDbException e) { LOGGER.severe("Failed to cleanup MRSC replicas: " + tableName + " - " + e.getMessage()); throw DynamoDbException.builder() .message("Failed to cleanup MRSC replicas: " + tableName) .cause(e) .build(); } } ``` Complete MRSC workflow demonstration using AWS SDK for Java 2.x. ``` public static void demonstrateCompleteMRSCWorkflow( final DynamoDbClient primaryClient, final DynamoDbClient replicaClient, final String tableName, final Region replicaRegion, final Region witnessRegion) throws InterruptedException { if (primaryClient == null) { throw new IllegalArgumentException("Primary DynamoDB client cannot be null"); } if (replicaClient == null) { throw new IllegalArgumentException("Replica DynamoDB client cannot be null"); } if (tableName == null || tableName.trim().isEmpty()) { throw new IllegalArgumentException("Table name cannot be null or empty"); } if (replicaRegion == null) { throw new IllegalArgumentException("Replica region cannot be null"); } if (witnessRegion == null) { throw new IllegalArgumentException("Witness region cannot be null"); } try { LOGGER.info("=== Starting Complete MRSC Workflow Demonstration ==="); // Step 1: Create an empty single-Region table LOGGER.info("Step 1: Creating empty single-Region table"); createRegionalTable(primaryClient, tableName); // Use the existing GlobalTableOperations method for basic table waiting LOGGER.info("Intermediate step: Waiting for table [" + tableName + "] to become active before continuing"); GlobalTableOperations.waitForTableActive(primaryClient, tableName); // Step 2: Convert to MRSC with replica and witness LOGGER.info("Step 2: Converting to MRSC with replica and witness"); convertToMRSCWithWitness(primaryClient, tableName, replicaRegion, witnessRegion); // Wait for MRSC conversion to complete using MRSC-specific waiter LOGGER.info("Waiting for MRSC conversion to complete..."); waitForMRSCReplicasActive(primaryClient, tableName); LOGGER.info("Intermediate step: Waiting for table [" + tableName + "] to become active before continuing"); GlobalTableOperations.waitForTableActive(primaryClient, tableName); // Step 3: Verify MRSC configuration LOGGER.info("Step 3: Verifying MRSC configuration"); describeMRSCTable(primaryClient, tableName); // Step 4: Test strong consistency with data operations LOGGER.info("Step 4: Testing strong consistency with data operations"); // Add test item to primary region putTestItem(primaryClient, tableName, "The Beatles", "Hey Jude", "The Beatles 1967-1970", "1968"); // Immediately read from replica region (no wait needed with MRSC) LOGGER.info("Reading from replica region immediately (strong consistency):"); GetItemResponse getResponse = getItemWithConsistentRead(replicaClient, tableName, "The Beatles", "Hey Jude"); if (getResponse.hasItem()) { LOGGER.info("✓ Strong consistency verified - item immediately available in replica region"); } else { LOGGER.warning("✗ Item not found in replica region"); } // Test conditional update from replica region LOGGER.info("Testing conditional update from replica region:"); performConditionalUpdate(replicaClient, tableName, "The Beatles", "Hey Jude", "5"); LOGGER.info("✓ Conditional update successful - demonstrates strong consistency"); // Step 5: Cleanup LOGGER.info("Step 5: Cleaning up resources"); cleanupMRSCReplicas(primaryClient, tableName, replicaRegion, witnessRegion); // Wait for cleanup to complete using basic table waiter LOGGER.info("Waiting for replica cleanup to complete..."); GlobalTableOperations.waitForTableActive(primaryClient, tableName); // "Halt" until replica/witness cleanup is complete DescribeTableResponse cleanupVerification = describeMRSCTable(primaryClient, tableName); int backoffSeconds = 5; // Start with 5 second intervals while (cleanupVerification.table().multiRegionConsistency() != null) { LOGGER.info("Waiting additional time (" + backoffSeconds + " seconds) for MRSC cleanup to complete..."); tempWait(backoffSeconds); // Exponential backoff with cap backoffSeconds = Math.min(backoffSeconds * 2, 30); cleanupVerification = describeMRSCTable(primaryClient, tableName); } // Delete the primary table deleteTable(primaryClient, tableName); LOGGER.info("=== MRSC Workflow Demonstration Complete ==="); LOGGER.info(""); LOGGER.info("Key benefits of Multi-Region Strong Consistency (MRSC):"); LOGGER.info("- Immediate consistency across all regions (no eventual consistency delays)"); LOGGER.info("- Simplified application logic (no need to handle eventual consistency)"); LOGGER.info("- Support for conditional writes and transactions across regions"); LOGGER.info("- Consistent read operations from any region without waiting"); } catch (DynamoDbException | InterruptedException e) { LOGGER.severe("MRSC workflow failed: " + e.getMessage()); throw e; } } ``` <br>• For API details, see the following topics in *AWS SDK for Java 2.x API Reference*. + [CreateTable](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/CreateTable.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/CreateTable.md") + [DeleteTable](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/DeleteTable.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/DeleteTable.md") + [DescribeTable](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeTable.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/DescribeTable.md") + [GetItem](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/GetItem.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/GetItem.md") + [PutItem](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/PutItem.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/PutItem.md") + [UpdateItem](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateItem.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateItem.md") + [UpdateTable](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateTable.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/UpdateTable.md") For a complete list of AWS SDK developer guides and code examples, see [Using DynamoDB with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md"). This topic also includes information about getting started and details about previous SDK versions.
````
