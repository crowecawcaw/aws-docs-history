# Code examples for Amazon SQS using AWS SDKs

The following code examples show how to use Amazon SQS with an AWS software development kit (SDK).

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon SQS with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Amazon SQS.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/TopicsAndQueues#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/cross-service/TopicsAndQueues#code-examples").

```

using Amazon.SQS;
using Amazon.SQS.Model;

namespace SQSActions;

public static class HelloSQS
{
    static async Task Main(string[] args)
    {
        var sqsClient = new AmazonSQSClient();

        Console.WriteLine($"Hello Amazon SQS! Following are some of your queues:");
        Console.WriteLine();

        // You can use await and any of the async methods to get a response.
        // Let's get the first five queues.
        var response = await sqsClient.ListQueuesAsync(
            new ListQueuesRequest()
            {
                MaxResults = 5
            });

        foreach (var queue in response.QueueUrls)
        {
            Console.WriteLine($"\tQueue Url: {queue}");
            Console.WriteLine();
        }
    }
}


```

- For API details, see
  [ListQueues](../../../goto/DotNetSDKV3/sqs-2012-11-05/ListQueues.md "../../../goto/DotNetSDKV3/sqs-2012-11-05/ListQueues.md")
  in _AWS SDK for .NET API Reference_.

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/hello_sqs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/sqs/hello_sqs#code-examples").

Code for the CMakeLists.txt CMake file.

```
# Set the minimum required version of CMake for this project.
cmake_minimum_required(VERSION 3.13)

# Set the AWS service components used by this project.
set(SERVICE_COMPONENTS sqs)

# Set this project's name.
project("hello_sqs")

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

if(WINDOWS_BUILD AND AWSSDK_INSTALL_AS_SHARED_LIBS)
    # Copy relevant AWS SDK for C++ libraries into the current binary directory for running and debugging.

    # set(BIN_SUB_DIR "/Debug") # If you are building from the command line you may need to uncomment this
    # and set the proper subdirectory to the executables' location.

    AWSSDK_CPY_DYN_LIBS(SERVICE_COMPONENTS "" ${CMAKE_CURRENT_BINARY_DIR}${BIN_SUB_DIR})
endif()

add_executable(${PROJECT_NAME}
        hello_sqs.cpp)

target_link_libraries(${PROJECT_NAME}
        ${AWSSDK_LINK_LIBRARIES})


```

Code for the hello_sqs.cpp source file.

```
#include <aws/core/Aws.h>
#include <aws/sqs/SQSClient.h>
#include <aws/sqs/model/ListQueuesRequest.h>
#include <iostream>

/*
 *  A "Hello SQS" starter application that initializes an Amazon Simple Queue Service
 *  (Amazon SQS) client and lists the SQS queues in the current account.
 *
 *  main function
 *
 *  Usage: 'hello_sqs'
 *
 */

int main(int argc, char **argv) {
    Aws::SDKOptions options;
    // Optionally change the log level for debugging.
//   options.loggingOptions.logLevel = Utils::Logging::LogLevel::Debug;
    Aws::InitAPI(options); // Should only be called once.
    {
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";

        Aws::SQS::SQSClient sqsClient(clientConfig);

        Aws::Vector<Aws::String> allQueueUrls;
        Aws::String nextToken; // Next token is used to handle a paginated response.
        do {
            Aws::SQS::Model::ListQueuesRequest request;

            Aws::SQS::Model::ListQueuesOutcome outcome = sqsClient.ListQueues(request);

            if (outcome.IsSuccess()) {
                const Aws::Vector<Aws::String> &pageOfQueueUrls = outcome.GetResult().GetQueueUrls();
                if (!pageOfQueueUrls.empty()) {
                    allQueueUrls.insert(allQueueUrls.cend(), pageOfQueueUrls.cbegin(),
                                        pageOfQueueUrls.cend());
                }
            }
            else {
                std::cerr << "Error with SQS::ListQueues. "
                          << outcome.GetError().GetMessage()
                          << std::endl;
                break;
            }
            nextToken = outcome.GetResult().GetNextToken();
        } while (!nextToken.empty());


        std::cout << "Hello Amazon SQS! You have " << allQueueUrls.size() << " queue"
                  << (allQueueUrls.size() == 1 ? "" : "s") << " in your account."
                  << std::endl;

        if (!allQueueUrls.empty()) {
            std::cout << "Here are your queue URLs." << std::endl;
            for (const Aws::String &queueUrl: allQueueUrls) {
                std::cout << "  * " << queueUrl << std::endl;
            }
        }
    }

    Aws::ShutdownAPI(options); // Should only be called once.
    return 0;
}


```

- For API details, see
  [ListQueues](../../../goto/SdkForCpp/sqs-2012-11-05/ListQueues.md "../../../goto/SdkForCpp/sqs-2012-11-05/ListQueues.md")
  in _AWS SDK for C++ API Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/sqs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/sqs#code-examples").

```

package main

import (
	"context"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/sqs"
)

// main uses the AWS SDK for Go V2 to create an Amazon Simple Queue Service
// (Amazon SQS) client and list the queues in your account.
// This example uses the default settings specified in your shared credentials
// and config files.
func main() {
	ctx := context.Background()
	sdkConfig, err := config.LoadDefaultConfig(ctx)
	if err != nil {
		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
		fmt.Println(err)
		return
	}
	sqsClient := sqs.NewFromConfig(sdkConfig)
	fmt.Println("Let's list the queues for your account.")
	var queueUrls []string
	paginator := sqs.NewListQueuesPaginator(sqsClient, &sqs.ListQueuesInput{})
	for paginator.HasMorePages() {
		output, err := paginator.NextPage(ctx)
		if err != nil {
			log.Printf("Couldn't get queues. Here's why: %v\n", err)
			break
		} else {
			queueUrls = append(queueUrls, output.QueueUrls...)
		}
	}
	if len(queueUrls) == 0 {
		fmt.Println("You don't have any queues!")
	} else {
		for _, queueUrl := range queueUrls {
			fmt.Printf("\t%v\n", queueUrl)
		}
	}
}



```

- For API details, see
  [ListQueues](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.ListQueues "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/sqs#Client.ListQueues")
  in _AWS SDK for Go API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sqs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/sqs#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.sqs.SqsClient;
import software.amazon.awssdk.services.sqs.model.SqsException;
import software.amazon.awssdk.services.sqs.paginators.ListQueuesIterable;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloSQS {
    public static void main(String[] args) {
        SqsClient sqsClient = SqsClient.builder()
                .region(Region.US_WEST_2)
                .build();

        listQueues(sqsClient);
        sqsClient.close();
    }

    public static void listQueues(SqsClient sqsClient) {
        try {
            ListQueuesIterable listQueues = sqsClient.listQueuesPaginator();
            listQueues.stream()
                    .flatMap(r -> r.queueUrls().stream())
                    .forEach(content -> System.out.println(" Queue URL: " + content.toLowerCase()));

        } catch (SqsException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [ListQueues](../../../goto/SdkForJavaV2/sqs-2012-11-05/ListQueues.md "../../../goto/SdkForJavaV2/sqs-2012-11-05/ListQueues.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/sqs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/sqs#code-examples").

Initialize an Amazon SQS client and list queues.

```
import { SQSClient, paginateListQueues } from "@aws-sdk/client-sqs";

export const helloSqs = async () => {
  // The configuration object (`{}`) is required. If the region and credentials
  // are omitted, the SDK uses your local configuration if it exists.
  const client = new SQSClient({});

  // You can also use `ListQueuesCommand`, but to use that command you must
  // handle the pagination yourself. You can do that by sending the `ListQueuesCommand`
  // with the `NextToken` parameter from the previous request.
  const paginatedQueues = paginateListQueues({ client }, {});
  const queues = [];

  for await (const page of paginatedQueues) {
    if (page.QueueUrls?.length) {
      queues.push(...page.QueueUrls);
    }
  }

  const suffix = queues.length === 1 ? "" : "s";

  console.log(
    `Hello, Amazon SQS! You have ${queues.length} queue${suffix} in your account.`,
  );
  console.log(queues.map((t) => `  * ${t}`).join("\n"));
};


```

- For API details, see
  [ListQueues](../../../AWSJavaScriptSDK/v3/latest/client/sqs/command/ListQueuesCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/sqs/command/ListQueuesCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sqs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/sqs#code-examples").

```
package com.kotlin.sqs

import aws.sdk.kotlin.services.sqs.SqsClient
import aws.sdk.kotlin.services.sqs.paginators.listQueuesPaginated
import kotlinx.coroutines.flow.transform

suspend fun main() {
    listTopicsPag()
}

suspend fun listTopicsPag() {
    SqsClient.fromEnvironment { region = "us-east-1" }.use { sqsClient ->
        sqsClient
            .listQueuesPaginated { }
            .transform { it.queueUrls?.forEach { queue -> emit(queue) } }
            .collect { queue ->
                println("The Queue URL is $queue")
            }
    }
}


```

- For API details, see
  [ListQueues](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

Swift

**SDK for Swift**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sqs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/swift/example_code/sqs#code-examples").

The `Package.swift` file.

```
import PackageDescription

let package = Package(
    name: "sqs-basics",
    // Let Xcode know the minimum Apple platforms supported.
    platforms: [
        .macOS(.v13),
        .iOS(.v15)
    ],
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        .package(
            url: "https://github.com/awslabs/aws-sdk-swift",
            from: "1.0.0"),
        .package(
            url: "https://github.com/apple/swift-argument-parser.git",
            branch: "main"
        )
    ],
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products
        // from dependencies.
        .executableTarget(
            name: "sqs-basics",
            dependencies: [
                .product(name: "AWSSQS", package: "aws-sdk-swift"),
                .product(name: "ArgumentParser", package: "swift-argument-parser")
            ],
            path: "Sources")

    ]
)


```

The Swift source code, `entry.swift`.

```
import ArgumentParser
import AWSClientRuntime
import AWSSQS
import Foundation

struct ExampleCommand: ParsableCommand {
    @Argument(help: "The URL of the Amazon SQS queue to delete")
    var queueUrl: String
    @Option(help: "Name of the Amazon Region to use (default: us-east-1)")
    var region = "us-east-1"

    static var configuration = CommandConfiguration(
        commandName: "deletequeue",
        abstract: """
        This example shows how to delete an Amazon SQS queue.
        """,
        discussion: """
        """
    )

    /// Called by ``main()`` to run the bulk of the example.
    func runAsync() async throws {
        let config = try await SQSClient.SQSClientConfiguration(region: region)
        let sqsClient = SQSClient(config: config)

        do {
            _ = try await sqsClient.deleteQueue(
                input: DeleteQueueInput(
                    queueUrl: queueUrl
                )
            )
        } catch _ as AWSSQS.QueueDoesNotExist {
            print("Error: The specified queue doesn't exist.")
            return
        }
    }
}

/// The program's asynchronous entry point.
@main
struct Main {
    static func main() async {
        let args = Array(CommandLine.arguments.dropFirst())

        do {
            let command = try ExampleCommand.parse(args)
            try await command.runAsync()
        } catch {
            ExampleCommand.exit(withError: error)
        }
    }
}


```

- For API details, see
  [ListQueues](<https://sdk.amazonaws.com/swift/api/awssqs/latest/documentation/awssqs/sqsclient/listqueues(input:)> "https://sdk.amazonaws.com/swift/api/awssqs/latest/documentation/awssqs/sqsclient/listqueues(input:)")
  in _AWS SDK for Swift API reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Amazon SQS](example_sqs_Hello_section.md "example_sqs_Hello_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [AddPermission](example_sqs_AddPermission_section.md "example_sqs_AddPermission_section.md")
    - [ChangeMessageVisibility](example_sqs_ChangeMessageVisibility_section.md "example_sqs_ChangeMessageVisibility_section.md")
    - [ChangeMessageVisibilityBatch](example_sqs_ChangeMessageVisibilityBatch_section.md "example_sqs_ChangeMessageVisibilityBatch_section.md")
    - [CreateQueue](example_sqs_CreateQueue_section.md "example_sqs_CreateQueue_section.md")
    - [DeleteMessage](example_sqs_DeleteMessage_section.md "example_sqs_DeleteMessage_section.md")
    - [DeleteMessageBatch](example_sqs_DeleteMessageBatch_section.md "example_sqs_DeleteMessageBatch_section.md")
    - [DeleteQueue](example_sqs_DeleteQueue_section.md "example_sqs_DeleteQueue_section.md")
    - [GetQueueAttributes](example_sqs_GetQueueAttributes_section.md "example_sqs_GetQueueAttributes_section.md")
    - [GetQueueUrl](example_sqs_GetQueueUrl_section.md "example_sqs_GetQueueUrl_section.md")
    - [ListDeadLetterSourceQueues](example_sqs_ListDeadLetterSourceQueues_section.md "example_sqs_ListDeadLetterSourceQueues_section.md")
    - [ListQueues](example_sqs_ListQueues_section.md "example_sqs_ListQueues_section.md")
    - [PurgeQueue](example_sqs_PurgeQueue_section.md "example_sqs_PurgeQueue_section.md")
    - [ReceiveMessage](example_sqs_ReceiveMessage_section.md "example_sqs_ReceiveMessage_section.md")
    - [RemovePermission](example_sqs_RemovePermission_section.md "example_sqs_RemovePermission_section.md")
    - [SendMessage](example_sqs_SendMessage_section.md "example_sqs_SendMessage_section.md")
    - [SendMessageBatch](example_sqs_SendMessageBatch_section.md "example_sqs_SendMessageBatch_section.md")
    - [SetQueueAttributes](example_sqs_SetQueueAttributes_section.md "example_sqs_SetQueueAttributes_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Create a messaging application](example_cross_SQSMessageApp_section.md "example_cross_SQSMessageApp_section.md")
  - [Create a messenger application](example_cross_StepFunctionsMessenger_section.md "example_cross_StepFunctionsMessenger_section.md")
  - [Create an Amazon Textract explorer application](example_cross_TextractExplorer_section.md "example_cross_TextractExplorer_section.md")
  - [Create and publish to a FIFO topic](example_sns_PublishFifoTopic_section.md "example_sns_PublishFifoTopic_section.md")
  - [Detect people and objects in a video](example_cross_RekognitionVideoDetection_section.md "example_cross_RekognitionVideoDetection_section.md")
  - [Manage large messages using S3](example_sqs_Scenario_SqsExtendedClient_section.md "example_sqs_Scenario_SqsExtendedClient_section.md")
  - [Process S3 event notifications](example_s3_Scenario_ProcessS3EventNotification_section.md "example_s3_Scenario_ProcessS3EventNotification_section.md")
  - [Publish messages to queues](example_sqs_Scenario_TopicsAndQueues_section.md "example_sqs_Scenario_TopicsAndQueues_section.md")
  - [Send and receive batches of messages](example_sqs_Scenario_SendReceiveBatch_section.md "example_sqs_Scenario_SendReceiveBatch_section.md")
  - [Use the AWS Message Processing Framework for .NET with Amazon SQS](example_cross_MessageProcessingFrameworkTutorial_section.md "example_cross_MessageProcessingFrameworkTutorial_section.md")
  - [Use the Amazon SQS Java Messaging Library to work with the JMS interface](example_sqs_Scenario_UseJMS_section.md "example_sqs_Scenario_UseJMS_section.md")
  - [Work with queue tags](example_sqs_Scenario_WorkWithTags_section.md "example_sqs_Scenario_WorkWithTags_section.md")

- [Serverless examples](service_code_examples_serverless_examples.md "service_code_examples_serverless_examples.md")
  - [Invoke a Lambda function from an Amazon SQS trigger](example_serverless_SQS_Lambda_section.md "example_serverless_SQS_Lambda_section.md")
  - [Reporting batch item failures for Lambda functions with an Amazon SQS trigger](example_serverless_SQS_Lambda_batch_item_failures_section.md "example_serverless_SQS_Lambda_batch_item_failures_section.md")
