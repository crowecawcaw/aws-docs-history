# Code examples for Support using AWS SDKs

The following code examples show how to use Support with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Support with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Support.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Support#code-examples").

```

using Amazon.AWSSupport;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

public static class HelloSupport
{
    static async Task Main(string[] args)
    {
        // Use the AWS .NET Core Setup package to set up dependency injection for the AWS Support service.
        // Use your AWS profile name, or leave it blank to use the default profile.
        // You must have one of the following AWS Support plans: Business, Enterprise On-Ramp, or Enterprise. Otherwise, an exception will be thrown.
        using var host = Host.CreateDefaultBuilder(args)
            .ConfigureServices((_, services) =>
                services.AddAWSService<IAmazonAWSSupport>()
            ).Build();

        // Now the client is available for injection.
        var supportClient = host.Services.GetRequiredService<IAmazonAWSSupport>();

        // You can use await and any of the async methods to get a response.
        var response = await supportClient.DescribeServicesAsync();
        Console.WriteLine($"\tHello AWS Support! There are {response.Services.Count} services available.");
    }
}


```

- For API details, see
  [DescribeServices](../../../goto/DotNetSDKV3/support-2013-04-15/DescribeServices.md "../../../goto/DotNetSDKV3/support-2013-04-15/DescribeServices.md")
  in _AWS SDK for .NET API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.support.SupportClient;
import software.amazon.awssdk.services.support.model.Category;
import software.amazon.awssdk.services.support.model.DescribeServicesRequest;
import software.amazon.awssdk.services.support.model.DescribeServicesResponse;
import software.amazon.awssdk.services.support.model.Service;
import software.amazon.awssdk.services.support.model.SupportException;
import java.util.ArrayList;
import java.util.List;

/**
 * Before running this Java (v2) code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * In addition, you must have the AWS Business Support Plan to use the AWS
 * Support Java API. For more information, see:
 *
 * https://aws.amazon.com/premiumsupport/plans/
 *
 * This Java example performs the following task:
 *
 * 1. Gets and displays available services.
 *
 *
 * NOTE: To see multiple operations, see SupportScenario.
 */

public class HelloSupport {
    public static void main(String[] args) {
        Region region = Region.US_WEST_2;
        SupportClient supportClient = SupportClient.builder()
                .region(region)
                .build();

        System.out.println("***** Step 1. Get and display available services.");
        displayServices(supportClient);
    }

    // Return a List that contains a Service name and Category name.
    public static void displayServices(SupportClient supportClient) {
        try {
            DescribeServicesRequest servicesRequest = DescribeServicesRequest.builder()
                    .language("en")
                    .build();

            DescribeServicesResponse response = supportClient.describeServices(servicesRequest);
            List<Service> services = response.services();

            System.out.println("Get the first 10 services");
            int index = 1;
            for (Service service : services) {
                if (index == 11)
                    break;

                System.out.println("The Service name is: " + service.name());

                // Display the Categories for this service.
                List<Category> categories = service.categories();
                for (Category cat : categories) {
                    System.out.println("The category name is: " + cat.name());
                }
                index++;
            }

        } catch (SupportException e) {
            System.out.println(e.getLocalizedMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [DescribeServices](../../../goto/SdkForJavaV2/support-2013-04-15/DescribeServices.md "../../../goto/SdkForJavaV2/support-2013-04-15/DescribeServices.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples").

Invoke `main()` to run the example.

```
import {
  DescribeServicesCommand,
  SupportClient,
} from "@aws-sdk/client-support";

// Change the value of 'region' to your preferred AWS Region.
const client = new SupportClient({ region: "us-east-1" });

const getServiceCount = async () => {
  try {
    const { services } = await client.send(new DescribeServicesCommand({}));
    return services.length;
  } catch (err) {
    if (err.name === "SubscriptionRequiredException") {
      throw new Error(
        "You must be subscribed to the AWS Support plan to use this feature.",
      );
    }
    throw err;
  }
};

export const main = async () => {
  try {
    const count = await getServiceCount();
    console.log(`Hello, AWS Support! There are ${count} services available.`);
  } catch (err) {
    console.error("Failed to get service count: ", err.message);
  }
};


```

- For API details, see
  [DescribeServices](../../../AWSJavaScriptSDK/v3/latest/client/support/command/DescribeServicesCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/support/command/DescribeServicesCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples").

```

/**
Before running this Kotlin code example, set up your development environment,
including your credentials.

For more information, see the following documentation topic:
https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html

In addition, you must have the AWS Business Support Plan to use the AWS Support Java API. For more information, see:

https://aws.amazon.com/premiumsupport/plans/

This Kotlin example performs the following task:

1. Gets and displays available services.
 */

suspend fun main() {
    displaySomeServices()
}

// Return a List that contains a Service name and Category name.
suspend fun displaySomeServices() {
    val servicesRequest =
        DescribeServicesRequest {
            language = "en"
        }

    SupportClient.fromEnvironment { region = "us-west-2" }.use { supportClient ->
        val response = supportClient.describeServices(servicesRequest)
        println("Get the first 10 services")
        var index = 1

        response.services?.forEach { service ->
            if (index == 11) {
                return@forEach
            }

            println("The Service name is: " + service.name)

            // Get the categories for this service.
            service.categories?.forEach { cat ->
                println("The category name is ${cat.name}")
                index++
            }
        }
    }
}



```

- For API details, see
  [DescribeServices](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/support#code-examples").

```
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def hello_support(support_client):
    """
    Use the AWS SDK for Python (Boto3) to create an AWS Support client and count
    the available services in your account.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param support_client: A Boto3 Support Client object.
    """
    try:
        print("Hello, AWS Support! Let's count the available Support services:")
        response = support_client.describe_services()
        print(f"There are {len(response['services'])} services available.")
    except ClientError as err:
        if err.response["Error"]["Code"] == "SubscriptionRequiredException":
            logger.info(
                "You must have a Business, Enterprise On-Ramp, or Enterprise Support "
                "plan to use the AWS Support API. \n\tPlease upgrade your subscription to run these "
                "examples."
            )
        else:
            logger.error(
                "Couldn't count services. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise


if __name__ == "__main__":
    hello_support(boto3.client("support"))


```

- For API details, see
  [DescribeServices](../../../goto/boto3/support-2013-04-15/DescribeServices.md "../../../goto/boto3/support-2013-04-15/DescribeServices.md")
  in _AWS SDK for Python (Boto3) API Reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Support](example_support_Hello_section.md "example_support_Hello_section.md")
  - [Learn the basics](example_support_Scenario_GetStartedSupportCases_section.md "example_support_Scenario_GetStartedSupportCases_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [AddAttachmentsToSet](example_support_AddAttachmentsToSet_section.md "example_support_AddAttachmentsToSet_section.md")
    - [AddCommunicationToCase](example_support_AddCommunicationToCase_section.md "example_support_AddCommunicationToCase_section.md")
    - [CreateCase](example_support_CreateCase_section.md "example_support_CreateCase_section.md")
    - [DescribeAttachment](example_support_DescribeAttachment_section.md "example_support_DescribeAttachment_section.md")
    - [DescribeCases](example_support_DescribeCases_section.md "example_support_DescribeCases_section.md")
    - [DescribeCommunications](example_support_DescribeCommunications_section.md "example_support_DescribeCommunications_section.md")
    - [DescribeServices](example_support_DescribeServices_section.md "example_support_DescribeServices_section.md")
    - [DescribeSeverityLevels](example_support_DescribeSeverityLevels_section.md "example_support_DescribeSeverityLevels_section.md")
    - [DescribeTrustedAdvisorCheckRefreshStatuses](example_support_DescribeTrustedAdvisorCheckRefreshStatuses_section.md "example_support_DescribeTrustedAdvisorCheckRefreshStatuses_section.md")
    - [DescribeTrustedAdvisorCheckResult](example_support_DescribeTrustedAdvisorCheckResult_section.md "example_support_DescribeTrustedAdvisorCheckResult_section.md")
    - [DescribeTrustedAdvisorCheckSummaries](example_support_DescribeTrustedAdvisorCheckSummaries_section.md "example_support_DescribeTrustedAdvisorCheckSummaries_section.md")
    - [DescribeTrustedAdvisorChecks](example_support_DescribeTrustedAdvisorChecks_section.md "example_support_DescribeTrustedAdvisorChecks_section.md")
    - [RefreshTrustedAdvisorCheck](example_support_RefreshTrustedAdvisorCheck_section.md "example_support_RefreshTrustedAdvisorCheck_section.md")
    - [ResolveCase](example_support_ResolveCase_section.md "example_support_ResolveCase_section.md")
