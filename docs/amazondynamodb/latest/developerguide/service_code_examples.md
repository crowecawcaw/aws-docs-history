# Code examples for DynamoDB using AWS SDKs

The following code examples show how to use DynamoDB with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

_AWS community contributions_ are examples that were created and are maintained by multiple teams across AWS. To provide feedback, use the mechanism provided in the linked repositories.

For a complete list of AWS SDK developer guides and code examples, see
[Using DynamoDB with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello DynamoDB](example_dynamodb_Hello_section.md "example_dynamodb_Hello_section.md")
  - [Learn the basics](example_dynamodb_Scenario_GettingStartedMovies_section.md "example_dynamodb_Scenario_GettingStartedMovies_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [BatchExecuteStatement](example_dynamodb_BatchExecuteStatement_section.md "example_dynamodb_BatchExecuteStatement_section.md")
    - [BatchGetItem](example_dynamodb_BatchGetItem_section.md "example_dynamodb_BatchGetItem_section.md")
    - [BatchWriteItem](example_dynamodb_BatchWriteItem_section.md "example_dynamodb_BatchWriteItem_section.md")
    - [CreateTable](example_dynamodb_CreateTable_section.md "example_dynamodb_CreateTable_section.md")
    - [DeleteItem](example_dynamodb_DeleteItem_section.md "example_dynamodb_DeleteItem_section.md")
    - [DeleteTable](example_dynamodb_DeleteTable_section.md "example_dynamodb_DeleteTable_section.md")
    - [DescribeTable](example_dynamodb_DescribeTable_section.md "example_dynamodb_DescribeTable_section.md")
    - [DescribeTimeToLive](example_dynamodb_DescribeTimeToLive_section.md "example_dynamodb_DescribeTimeToLive_section.md")
    - [ExecuteStatement](example_dynamodb_ExecuteStatement_section.md "example_dynamodb_ExecuteStatement_section.md")
    - [GetItem](example_dynamodb_GetItem_section.md "example_dynamodb_GetItem_section.md")
    - [ListTables](example_dynamodb_ListTables_section.md "example_dynamodb_ListTables_section.md")
    - [PutItem](example_dynamodb_PutItem_section.md "example_dynamodb_PutItem_section.md")
    - [Query](example_dynamodb_Query_section.md "example_dynamodb_Query_section.md")
    - [Scan](example_dynamodb_Scan_section.md "example_dynamodb_Scan_section.md")
    - [UpdateItem](example_dynamodb_UpdateItem_section.md "example_dynamodb_UpdateItem_section.md")
    - [UpdateTable](example_dynamodb_UpdateTable_section.md "example_dynamodb_UpdateTable_section.md")
    - [UpdateTimeToLive](example_dynamodb_UpdateTimeToLive_section.md "example_dynamodb_UpdateTimeToLive_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Accelerate reads with DAX](example_dynamodb_Usage_DaxDemo_section.md "example_dynamodb_Usage_DaxDemo_section.md")
  - [Advanced Global Secondary Index scenarios](example_dynamodb_Scenario_GSIAdvanced_section.md "example_dynamodb_Scenario_GSIAdvanced_section.md")
  - [Build an app to submit data to a DynamoDB table](example_cross_SubmitDataApp_section.md "example_cross_SubmitDataApp_section.md")
  - [Compare multiple values with a single attribute](example_dynamodb_Scenario_CompareMultipleValues_section.md "example_dynamodb_Scenario_CompareMultipleValues_section.md")
  - [Conditionally update an item's TTL](example_dynamodb_UpdateItemConditionalTTL_section.md "example_dynamodb_UpdateItemConditionalTTL_section.md")
  - [Connect to a local instance](example_dynamodb_local_section.md "example_dynamodb_local_section.md")
  - [Count expression operators](example_dynamodb_Scenario_ExpressionOperatorCounting_section.md "example_dynamodb_Scenario_ExpressionOperatorCounting_section.md")
  - [Create a REST API to track COVID-19 data](example_cross_ApiGatewayDataTracker_section.md "example_cross_ApiGatewayDataTracker_section.md")
  - [Create a messenger application](example_cross_StepFunctionsMessenger_section.md "example_cross_StepFunctionsMessenger_section.md")
  - [Create a serverless application to manage photos](example_cross_PAM_section.md "example_cross_PAM_section.md")
  - [Create a table with global secondary index](example_dynamodb_CreateTableWithGlobalSecondaryIndex_section.md "example_dynamodb_CreateTableWithGlobalSecondaryIndex_section.md")
  - [Create a table with warm throughput enabled](example_dynamodb_CreateTableWarmThroughput_section.md "example_dynamodb_CreateTableWarmThroughput_section.md")
  - [Create a web application to track DynamoDB data](example_cross_DynamoDBDataTracker_section.md "example_cross_DynamoDBDataTracker_section.md")
  - [Create a websocket chat application](example_cross_ApiGatewayWebsocketChat_section.md "example_cross_ApiGatewayWebsocketChat_section.md")
  - [Create an item with a TTL](example_dynamodb_PutItemTTL_section.md "example_dynamodb_PutItemTTL_section.md")
  - [Create and manage MRSC global tables](example_dynamodb_Scenario_MRSCGlobalTables_section.md "example_dynamodb_Scenario_MRSCGlobalTables_section.md")
  - [Create and manage global tables demonstrating MREC](example_dynamodb_Scenario_GlobalTableOperations_section.md "example_dynamodb_Scenario_GlobalTableOperations_section.md")
  - [Delete data using PartiQL DELETE](example_dynamodb_PartiQLDelete_section.md "example_dynamodb_PartiQLDelete_section.md")
  - [Detect PPE in images](example_cross_RekognitionPhotoAnalyzerPPE_section.md "example_cross_RekognitionPhotoAnalyzerPPE_section.md")
  - [Insert data using PartiQL INSERT](example_dynamodb_PartiQLInsert_section.md "example_dynamodb_PartiQLInsert_section.md")
  - [Invoke a Lambda function from a browser](example_cross_LambdaForBrowser_section.md "example_cross_LambdaForBrowser_section.md")
  - [Manage Global Secondary Indexes](example_dynamodb_Scenario_GSILifecycle_section.md "example_dynamodb_Scenario_GSILifecycle_section.md")
  - [Manage resource-based policies](example_dynamodb_Scenario_ResourcePolicyLifecycle_section.md "example_dynamodb_Scenario_ResourcePolicyLifecycle_section.md")
  - [Monitor DynamoDB performance](example_cross_MonitorDynamoDB_section.md "example_cross_MonitorDynamoDB_section.md")
  - [Perform advanced query operations](example_dynamodb_Scenario_AdvancedQueryTechniques_section.md "example_dynamodb_Scenario_AdvancedQueryTechniques_section.md")
  - [Perform list operations](example_dynamodb_Scenario_ListOperations_section.md "example_dynamodb_Scenario_ListOperations_section.md")
  - [Perform map operations](example_dynamodb_Scenario_MapOperations_section.md "example_dynamodb_Scenario_MapOperations_section.md")
  - [Perform set operations](example_dynamodb_Scenario_SetOperations_section.md "example_dynamodb_Scenario_SetOperations_section.md")
  - [Query a table by using batches of PartiQL statements](example_dynamodb_Scenario_PartiQLBatch_section.md "example_dynamodb_Scenario_PartiQLBatch_section.md")
  - [Query a table using PartiQL](example_dynamodb_Scenario_PartiQLSingle_section.md "example_dynamodb_Scenario_PartiQLSingle_section.md")
  - [Query a table using a Global Secondary Index](example_dynamodb_Scenarios_QueryWithGlobalSecondaryIndex_section.md "example_dynamodb_Scenarios_QueryWithGlobalSecondaryIndex_section.md")
  - [Query a table using a begins_with condition](example_dynamodb_Scenarios_QueryWithBeginsWithCondition_section.md "example_dynamodb_Scenarios_QueryWithBeginsWithCondition_section.md")
  - [Query a table using a date range](example_dynamodb_Scenarios_QueryWithDateRange_section.md "example_dynamodb_Scenarios_QueryWithDateRange_section.md")
  - [Query a table with a complex filter expression](example_dynamodb_Scenarios_QueryWithComplexFilter_section.md "example_dynamodb_Scenarios_QueryWithComplexFilter_section.md")
  - [Query a table with a dynamic filter expression](example_dynamodb_Scenarios_QueryWithDynamicFilter_section.md "example_dynamodb_Scenarios_QueryWithDynamicFilter_section.md")
  - [Query a table with a filter expression and limit](example_dynamodb_Scenarios_QueryWithFilterAndLimit_section.md "example_dynamodb_Scenarios_QueryWithFilterAndLimit_section.md")
  - [Query a table with nested attributes](example_dynamodb_Scenarios_QueryWithNestedAttributes_section.md "example_dynamodb_Scenarios_QueryWithNestedAttributes_section.md")
  - [Query a table with pagination](example_dynamodb_Scenarios_QueryWithPagination_section.md "example_dynamodb_Scenarios_QueryWithPagination_section.md")
  - [Query a table with strongly consistent reads](example_dynamodb_Scenarios_QueryWithStronglyConsistentReads_section.md "example_dynamodb_Scenarios_QueryWithStronglyConsistentReads_section.md")
  - [Query data using PartiQL SELECT](example_dynamodb_PartiQLSelect_section.md "example_dynamodb_PartiQLSelect_section.md")
  - [Query for TTL items](example_dynamodb_QueryFilteredTTL_section.md "example_dynamodb_QueryFilteredTTL_section.md")
  - [Query tables using date and time patterns](example_dynamodb_Scenario_DateTimeQueries_section.md "example_dynamodb_Scenario_DateTimeQueries_section.md")
  - [Save EXIF and other image information](example_cross_DetectLabels_section.md "example_cross_DetectLabels_section.md")
  - [Set up Attribute-Based Access Control](example_dynamodb_Scenario_ABACSetup_section.md "example_dynamodb_Scenario_ABACSetup_section.md")
  - [Understand update expression order](example_dynamodb_Scenario_UpdateExpressionOrder_section.md "example_dynamodb_Scenario_UpdateExpressionOrder_section.md")
  - [Update a table's warm throughput setting](example_dynamodb_UpdateTableWarmThroughput_section.md "example_dynamodb_UpdateTableWarmThroughput_section.md")
  - [Update an item's TTL](example_dynamodb_UpdateItemTTL_section.md "example_dynamodb_UpdateItemTTL_section.md")
  - [Update data using PartiQL UPDATE](example_dynamodb_PartiQLUpdate_section.md "example_dynamodb_PartiQLUpdate_section.md")
  - [Use API Gateway to invoke a Lambda function](example_cross_LambdaAPIGateway_section.md "example_cross_LambdaAPIGateway_section.md")
  - [Use Step Functions to invoke Lambda functions](example_cross_ServerlessWorkflows_section.md "example_cross_ServerlessWorkflows_section.md")
  - [Use a document model](example_dynamodb_MidLevelInterface_section.md "example_dynamodb_MidLevelInterface_section.md")
  - [Use a high-level object persistence model](example_dynamodb_HighLevelInterface_section.md "example_dynamodb_HighLevelInterface_section.md")
  - [Use atomic counter operations](example_dynamodb_Scenario_AtomicCounterOperations_section.md "example_dynamodb_Scenario_AtomicCounterOperations_section.md")
  - [Use conditional operations](example_dynamodb_Scenario_ConditionalOperations_section.md "example_dynamodb_Scenario_ConditionalOperations_section.md")
  - [Use expression attribute names](example_dynamodb_Scenario_ExpressionAttributeNames_section.md "example_dynamodb_Scenario_ExpressionAttributeNames_section.md")
  - [Use scheduled events to invoke a Lambda function](example_cross_LambdaScheduledEvents_section.md "example_cross_LambdaScheduledEvents_section.md")
  - [Work with Local Secondary Indexes](example_dynamodb_Scenario_LSIExamples_section.md "example_dynamodb_Scenario_LSIExamples_section.md")
  - [Work with Streams and Time-to-Live](example_dynamodb_Scenario_StreamsAndTTL_section.md "example_dynamodb_Scenario_StreamsAndTTL_section.md")
  - [Work with global tables and multi-Region replication eventual consistency (MREC)](example_dynamodb_Scenario_MultiRegionReplication_section.md "example_dynamodb_Scenario_MultiRegionReplication_section.md")
  - [Work with resource tagging](example_dynamodb_Scenario_TaggingExamples_section.md "example_dynamodb_Scenario_TaggingExamples_section.md")
  - [Work with table encryption](example_dynamodb_Scenario_EncryptionExamples_section.md "example_dynamodb_Scenario_EncryptionExamples_section.md")

- [Serverless examples](service_code_examples_serverless_examples.md "service_code_examples_serverless_examples.md")
  - [Invoke a Lambda function from a DynamoDB trigger](example_serverless_DynamoDB_Lambda_section.md "example_serverless_DynamoDB_Lambda_section.md")
  - [Reporting batch item failures for Lambda functions with a DynamoDB trigger](example_serverless_DynamoDB_Lambda_batch_item_failures_section.md "example_serverless_DynamoDB_Lambda_batch_item_failures_section.md")

- [AWS community contributions](service_code_examples_aws_community_contributions.md "service_code_examples_aws_community_contributions.md")
  - [Build and test a serverless application](example_tributary-lite_serverless-application_section.md "example_tributary-lite_serverless-application_section.md")
