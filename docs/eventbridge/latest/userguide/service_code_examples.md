# Code examples for EventBridge using AWS SDKs

The following code examples show how to use EventBridge with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using EventBridge with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using EventBridge.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples").

```

using Amazon.EventBridge;
using Amazon.EventBridge.Model;

namespace EventBridgeActions;

public static class HelloEventBridge
{
    static async Task Main(string[] args)
    {
        var eventBridgeClient = new AmazonEventBridgeClient();

        Console.WriteLine($"Hello Amazon EventBridge! Following are some of your EventBuses:");
        Console.WriteLine();

        // You can use await and any of the async methods to get a response.
        // Let's get the first five event buses.
        var response = await eventBridgeClient.ListEventBusesAsync(
            new ListEventBusesRequest()
            {
                Limit = 5
            });

        foreach (var eventBus in response.EventBuses)
        {
            Console.WriteLine($"\tEventBus: {eventBus.Name}");
            Console.WriteLine($"\tArn: {eventBus.Arn}");
            Console.WriteLine($"\tPolicy: {eventBus.Policy}");
            Console.WriteLine();
        }
    }
}


```

- For API details, see
  [ListEventBuses](../../../goto/DotNetSDKV3/eventbridge-2015-10-07/ListEventBuses.md "../../../goto/DotNetSDKV3/eventbridge-2015-10-07/ListEventBuses.md")
  in _AWS SDK for .NET API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/eventbridge#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/eventbridge#code-examples").

```
/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 */
public class HelloEventBridge {
    public static void main(String[] args) {
        Region region = Region.US_WEST_2;
        EventBridgeClient eventBrClient = EventBridgeClient.builder()
                .region(region)
                .build();

        listBuses(eventBrClient);
        eventBrClient.close();
    }

    public static void listBuses(EventBridgeClient eventBrClient) {
        try {
            ListEventBusesRequest busesRequest = ListEventBusesRequest.builder()
                    .limit(10)
                    .build();

            ListEventBusesResponse response = eventBrClient.listEventBuses(busesRequest);
            List<EventBus> buses = response.eventBuses();
            for (EventBus bus : buses) {
                System.out.println("The name of the event bus is: " + bus.name());
                System.out.println("The ARN of the event bus is: " + bus.arn());
            }

        } catch (EventBridgeException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [ListEventBuses](../../../goto/SdkForJavaV2/eventbridge-2015-10-07/ListEventBuses.md "../../../goto/SdkForJavaV2/eventbridge-2015-10-07/ListEventBuses.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/eventbridge#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/eventbridge#code-examples").

```
import aws.sdk.kotlin.services.eventbridge.EventBridgeClient
import aws.sdk.kotlin.services.eventbridge.model.ListEventBusesRequest
import aws.sdk.kotlin.services.eventbridge.model.ListEventBusesResponse

suspend fun main() {
    listBusesHello()
}

suspend fun listBusesHello() {
    val request =
        ListEventBusesRequest {
            limit = 10
        }

    EventBridgeClient.fromEnvironment { region = "us-west-2" }.use { eventBrClient ->
        val response: ListEventBusesResponse = eventBrClient.listEventBuses(request)
        response.eventBuses?.forEach { bus ->
            println("The name of the event bus is ${bus.name}")
            println("The ARN of the event bus is ${bus.arn}")
        }
    }
}


```

- For API details, see
  [ListEventBuses](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello EventBridge](example_eventbridge_Hello_section.md "example_eventbridge_Hello_section.md")
  - [Learn the basics](example_eventbridge_Scenario_GettingStarted_section.md "example_eventbridge_Scenario_GettingStarted_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [DeleteRule](example_eventbridge_DeleteRule_section.md "example_eventbridge_DeleteRule_section.md")
    - [DescribeRule](example_eventbridge_DescribeRule_section.md "example_eventbridge_DescribeRule_section.md")
    - [DisableRule](example_eventbridge_DisableRule_section.md "example_eventbridge_DisableRule_section.md")
    - [EnableRule](example_eventbridge_EnableRule_section.md "example_eventbridge_EnableRule_section.md")
    - [ListRuleNamesByTarget](example_eventbridge_ListRuleNamesByTarget_section.md "example_eventbridge_ListRuleNamesByTarget_section.md")
    - [ListRules](example_eventbridge_ListRules_section.md "example_eventbridge_ListRules_section.md")
    - [ListTargetsByRule](example_eventbridge_ListTargetsByRule_section.md "example_eventbridge_ListTargetsByRule_section.md")
    - [PutEvents](example_eventbridge_PutEvents_section.md "example_eventbridge_PutEvents_section.md")
    - [PutRule](example_eventbridge_PutRule_section.md "example_eventbridge_PutRule_section.md")
    - [PutTargets](example_eventbridge_PutTargets_section.md "example_eventbridge_PutTargets_section.md")
    - [RemoveTargets](example_eventbridge_RemoveTargets_section.md "example_eventbridge_RemoveTargets_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Create and trigger a rule](example_eventbridge_Scenario_createAndTriggerARule_section.md "example_eventbridge_Scenario_createAndTriggerARule_section.md")
  - [Send event notifications to EventBridge](example_s3_Scenario_PutBucketNotificationConfiguration_section.md "example_s3_Scenario_PutBucketNotificationConfiguration_section.md")
  - [Use scheduled events to invoke a Lambda function](example_cross_LambdaScheduledEvents_section.md "example_cross_LambdaScheduledEvents_section.md")
