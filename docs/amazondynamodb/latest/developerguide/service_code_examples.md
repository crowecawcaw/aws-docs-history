# Code examples for DynamoDB using AWS SDKs

The following code examples show how to use DynamoDB with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

_AWS community contributions_ are examples that were created and are maintained by multiple teams across AWS. To provide feedback, use the mechanism provided in the linked repositories.

For a complete list of AWS SDK developer guides and code examples, see
[Using DynamoDB with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using DynamoDB.

.NET

**SDK for .NET (v4)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/DynamoDB#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/DynamoDB#code-examples").

```

using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;
using Microsoft.Extensions.DependencyInjection;

namespace DynamoDBActions;

/// <summary>
/// A simple example that demonstrates basic DynamoDB operations.
/// </summary>
public class HelloDynamoDB
{
    /// <summary>
    /// HelloDynamoDB lists the existing DynamoDB tables for the default user.
    /// </summary>
    /// <param name="args">Command line arguments</param>
    /// <returns>Async task.</returns>
    static async Task Main(string[] args)
    {
        // Set up dependency injection for Amazon DynamoDB.
        using var host = Microsoft.Extensions.Hosting.Host.CreateDefaultBuilder(args)
            .ConfigureServices((_, services) =>
                services.AddAWSService<IAmazonDynamoDB>()
            )
            .Build();

        // Now the client is available for injection.
        var dynamoDbClient = host.Services.GetRequiredService<IAmazonDynamoDB>();

        try
        {
            var request = new ListTablesRequest();
            var tableNames = new List<string>();

            var paginatorForTables = dynamoDbClient.Paginators.ListTables(request);

            await foreach (var tableName in paginatorForTables.TableNames)
            {
                tableNames.Add(tableName);
            }

            Console.WriteLine("Welcome to the DynamoDB Hello Service example. " +
                              "\nLet's list your DynamoDB tables:");
            tableNames.ForEach(table =>
            {
                Console.WriteLine($"Table: {table}");
            });
        }
        catch (AmazonDynamoDBException ex)
        {
            Console.WriteLine($"An Amazon DynamoDB service error occurred while listing tables. {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred while listing tables. {ex.Message}");
        }
    }
}



```

- For API details, see
  [ListTables](../../../goto/DotNetSDKV4/dynamodb-2012-08-10/ListTables.md "../../../goto/DotNetSDKV4/dynamodb-2012-08-10/ListTables.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/dynamodb/hello_dynamodb#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/dynamodb/hello_dynamodb#code-examples").

Code for the CMakeLists.txt CMake file.

```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS dynamodb)

# Set this project's name.
project("hello_dynamodb")

# Set the C++ standard to use to build this target.
# At least C++ 11 is required for the AWS SDK for C++.
set(CMAKE_CXX_STANDARD 11)

# Use the MSVC variable to determine if this is a Windows build.
set(WINDOWS_BUILD ${MSVC})

if (WINDOWS_BUILD) # Set the location where CMake can find the installed libraries for the AWS SDK.
    string(REPLACE ";" "/aws-cpp-sdk-all;" SYSTEM_MODULE_PATH "${CMAKE_SYSTEM_PREFIX_PATH}/aws-cpp-sdk-all")
    list(APPEND CMAKE_PREFIX_PATH ${SYSTEM_MODULE_PATH})
endif ()

# Find the AWS SDK for C++ package.
find_package(AWSSDK REQUIRED COMPONENTS ${SERVICE_COMPONENTS})

if (WINDOWS_BUILD AND AWSSDK_INSTALL_AS_SHARED_LIBS)
     # Copy relevant AWS SDK for C++ libraries into the current binary directory for running and debugging.

     # set(BIN_SUB_DIR "/Debug") # if you are building from the command line you may need to uncomment this
                                    # and set the proper subdirectory to the executables' location.

     AWSSDK_CPY_DYN_LIBS(SERVICE_COMPONENTS "" ${CMAKE_CURRENT_BINARY_DIR}${BIN_SUB_DIR})
endif ()

add_executable(${PROJECT_NAME}
        hello_dynamodb.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the hello_dynamodb.cpp source file.

```
#include <aws/core/Aws.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/ListTablesRequest.h>
#include <iostream>

/*
 *  A "Hello DynamoDB" starter application which initializes an Amazon DynamoDB (DynamoDB) client and lists the
 *  DynamoDB tables.
 *
 *  main function
 *
 *  Usage: 'hello_dynamodb'
 *
 */

int main(int argc, char **argv) {
    Aws::SDKOptions options;
    // Optionally change the log level for debugging.
//   options.loggingOptions.logLevel = Utils::Logging::LogLevel::Debug;
    Aws::InitAPI(options); // Should only be called once.

    int result = 0;
    {
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";

        Aws::DynamoDB::DynamoDBClient dynamodbClient(clientConfig);
        Aws::DynamoDB::Model::ListTablesRequest listTablesRequest;
        listTablesRequest.SetLimit(50);
        do {
            const Aws::DynamoDB::Model::ListTablesOutcome &outcome = dynamodbClient.ListTables(
                    listTablesRequest);
            if (!outcome.IsSuccess()) {
                std::cout << "Error: " << outcome.GetError().GetMessage() << std::endl;
                result = 1;
                break;
            }

            for (const auto &tableName: outcome.GetResult().GetTableNames()) {
                std::cout << tableName << std::endl;
            }

            listTablesRequest.SetExclusiveStartTableName(
                    outcome.GetResult().GetLastEvaluatedTableName());

        } while (!listTablesRequest.GetExclusiveStartTableName().empty());
    }


    Aws::ShutdownAPI(options); // Should only be called once.
    return result;
}


```

- For API details, see
  [ListTables](../../../goto/SdkForCpp/dynamodb-2012-08-10/ListTables.md "../../../goto/SdkForCpp/dynamodb-2012-08-10/ListTables.md")
  in _AWS SDK for C++ API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/dynamodb#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/dynamodb#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.model.ListTablesRequest;
import software.amazon.awssdk.services.dynamodb.model.ListTablesResponse;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class ListTables {
    public static void main(String[] args) {
        System.out.println("Listing your Amazon DynamoDB tables:\n");
        Region region = Region.US_EAST_1;
        DynamoDbClient ddb = DynamoDbClient.builder()
                .region(region)
                .build();
        listAllTables(ddb);
        ddb.close();
    }

    public static void listAllTables(DynamoDbClient ddb) {
        boolean moreTables = true;
        String lastName = null;

        while (moreTables) {
            try {
                ListTablesResponse response = null;
                if (lastName == null) {
                    ListTablesRequest request = ListTablesRequest.builder().build();
                    response = ddb.listTables(request);
                } else {
                    ListTablesRequest request = ListTablesRequest.builder()
                            .exclusiveStartTableName(lastName).build();
                    response = ddb.listTables(request);
                }

                List<String> tableNames = response.tableNames();
                if (tableNames.size() > 0) {
                    for (String curName : tableNames) {
                        System.out.format("* %s\n", curName);
                    }
                } else {
                    System.out.println("No tables found!");
                    System.exit(0);
                }

                lastName = response.lastEvaluatedTableName();
                if (lastName == null) {
                    moreTables = false;
                }

            } catch (DynamoDbException e) {
                System.err.println(e.getMessage());
                System.exit(1);
            }
        }
        System.out.println("\nDone!");
    }
}


```

- For API details, see
  [ListTables](../../../goto/SdkForJavaV2/dynamodb-2012-08-10/ListTables.md "../../../goto/SdkForJavaV2/dynamodb-2012-08-10/ListTables.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/dynamodb#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/dynamodb#code-examples").

For more details on working with DynamoDB in AWS SDK for JavaScript, see [Programming DynamoDB with JavaScript](programming-with-javascript.md "programming-with-javascript.md").

```
import { ListTablesCommand, DynamoDBClient } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({});

export const main = async () => {
  const command = new ListTablesCommand({});

  const response = await client.send(command);
  console.log(response.TableNames.join("\n"));
  return response;
};


```

- For API details, see
  [ListTables](../../../AWSJavaScriptSDK/v3/latest/client/dynamodb/command/ListTablesCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/dynamodb/command/ListTablesCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/dynamodb#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/dynamodb#code-examples").

```

import boto3

# Create a DynamoDB client using the default credentials and region
dynamodb = boto3.client("dynamodb")

# Initialize a paginator for the list_tables operation
paginator = dynamodb.get_paginator("list_tables")

# Create a PageIterator from the paginator
page_iterator = paginator.paginate(Limit=10)

# List the tables in the current AWS account
print("Here are the DynamoDB tables in your account:")

# Use pagination to list all tables
table_names = []

for page in page_iterator:
    for table_name in page.get("TableNames", []):
        print(f"- {table_name}")
        table_names.append(table_name)

if not table_names:
    print("You don't have any DynamoDB tables in your account.")
else:
    print(f"\nFound {len(table_names)} tables.")



```

- For API details, see
  [ListTables](../../../goto/boto3/dynamodb-2012-08-10/ListTables.md "../../../goto/boto3/dynamodb-2012-08-10/ListTables.md")
  in _AWS SDK for Python (Boto3) API Reference_.

Ruby

**SDK for Ruby**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/dynamodb#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/dynamodb#code-examples").

```

require 'aws-sdk-dynamodb'
require 'logger'

# DynamoDBManager is a class responsible for managing DynamoDB operations
# such as listing all tables in the current AWS account.
class DynamoDBManager
  def initialize(client)
    @client = client
    @logger = Logger.new($stdout)
  end

  # Lists and prints all DynamoDB tables in the current AWS account.
  def list_tables
    @logger.info('Here are the DynamoDB tables in your account:')

    paginator = @client.list_tables(limit: 10)
    table_names = []

    paginator.each_page do |page|
      page.table_names.each do |table_name|
        @logger.info("- #{table_name}")
        table_names << table_name
      end
    end

    if table_names.empty?
      @logger.info("You don't have any DynamoDB tables in your account.")
    else
      @logger.info("\nFound #{table_names.length} tables.")
    end
  end
end

if $PROGRAM_NAME == __FILE__
  dynamodb_client = Aws::DynamoDB::Client.new
  manager = DynamoDBManager.new(dynamodb_client)
  manager.list_tables
end



```

- For API details, see
  [ListTables](../../../goto/SdkForRubyV3/dynamodb-2012-08-10/ListTables.md "../../../goto/SdkForRubyV3/dynamodb-2012-08-10/ListTables.md")
  in _AWS SDK for Ruby API Reference_.

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
