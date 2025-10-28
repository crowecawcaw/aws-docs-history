# Code examples for CloudWatch using AWS SDKs

The following code examples show how to use CloudWatch with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using CloudWatch with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using CloudWatch.

.NET

**SDK for .NET (v4)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples").

```
using Amazon.CloudWatch;
using Amazon.CloudWatch.Model;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace CloudWatchActions;

public static class HelloCloudWatch
{
    static async Task Main(string[] args)
    {
        // Use the AWS .NET Core Setup package to set up dependency injection for the Amazon CloudWatch service.
        // Use your AWS profile name, or leave it blank to use the default profile.
        using var host = Host.CreateDefaultBuilder(args)
            .ConfigureServices((_, services) =>
                services.AddAWSService<IAmazonCloudWatch>()
            ).Build();

        // Now the client is available for injection.
        var cloudWatchClient = host.Services.GetRequiredService<IAmazonCloudWatch>();

        // You can use await and any of the async methods to get a response.
        var metricNamespace = "AWS/Billing";
        var response = await cloudWatchClient.ListMetricsAsync(new ListMetricsRequest
        {
            Namespace = metricNamespace
        });
        Console.WriteLine($"Hello Amazon CloudWatch! Following are some metrics available in the {metricNamespace} namespace:");
        Console.WriteLine();
        if (response.Metrics != null)
        {
            foreach (var metric in response.Metrics.Take(5))
            {
                Console.WriteLine($"\tMetric: {metric.MetricName}");
                Console.WriteLine($"\tNamespace: {metric.Namespace}");
                Console.WriteLine(
                    $"\tDimensions: {string.Join(", ", metric.Dimensions.Select(m => $"{m.Name}:{m.Value}"))}");
                Console.WriteLine();
            }
        }
    }
}


```

- For API details, see
  [ListMetrics](../../../goto/DotNetSDKV4/monitoring-2010-08-01/ListMetrics.md "../../../goto/DotNetSDKV4/monitoring-2010-08-01/ListMetrics.md")
  in _AWS SDK for .NET API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples").

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatch.model.ListMetricsRequest;
import software.amazon.awssdk.services.cloudwatch.paginators.ListMetricsIterable;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class HelloService {
    public static void main(String[] args) {
        final String usage = """

                Usage:
                  <namespace>\s

                Where:
                  namespace - The namespace to filter against (for example, AWS/EC2).\s
                """;

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String namespace = args[0];
        Region region = Region.US_EAST_1;
        CloudWatchClient cw = CloudWatchClient.builder()
                .region(region)
                .build();

        listMets(cw, namespace);
        cw.close();
    }

    public static void listMets(CloudWatchClient cw, String namespace) {
        try {
            ListMetricsRequest request = ListMetricsRequest.builder()
                    .namespace(namespace)
                    .build();

            ListMetricsIterable listRes = cw.listMetricsPaginator(request);
            listRes.stream()
                    .flatMap(r -> r.metrics().stream())
                    .forEach(metrics -> System.out.println(" Retrieved metric is: " + metrics.metricName()));

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}


```

- For API details, see
  [ListMetrics](../../../goto/SdkForJavaV2/monitoring-2010-08-01/ListMetrics.md "../../../goto/SdkForJavaV2/monitoring-2010-08-01/ListMetrics.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples").

```

/**
Before running this Kotlin code example, set up your development environment,
including your credentials.

For more information, see the following documentation topic:
https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html
 */
suspend fun main(args: Array<String>) {
    val usage = """
        Usage:
           <namespace>
        Where:
           namespace - The namespace to filter against (for example, AWS/EC2).
    """

    if (args.size != 1) {
        println(usage)
        exitProcess(0)
    }

    val namespace = args[0]
    listAllMets(namespace)
}

suspend fun listAllMets(namespaceVal: String?) {
    val request =
        ListMetricsRequest {
            namespace = namespaceVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient
            .listMetricsPaginated(request)
            .transform { it.metrics?.forEach { obj -> emit(obj) } }
            .collect { obj ->
                println("Name is ${obj.metricName}")
                println("Namespace is ${obj.namespace}")
            }
    }
}


```

- For API details, see
  [ListMetrics](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello CloudWatch](example_cloudwatch_Hello_section.md "example_cloudwatch_Hello_section.md")
  - [Learn the basics](example_cloudwatch_GetStartedMetricsDashboardsAlarms_section.md "example_cloudwatch_GetStartedMetricsDashboardsAlarms_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
    - [DeleteAlarms](example_cloudwatch_DeleteAlarms_section.md "example_cloudwatch_DeleteAlarms_section.md")
    - [DeleteAnomalyDetector](example_cloudwatch_DeleteAnomalyDetector_section.md "example_cloudwatch_DeleteAnomalyDetector_section.md")
    - [DeleteDashboards](example_cloudwatch_DeleteDashboards_section.md "example_cloudwatch_DeleteDashboards_section.md")
    - [DescribeAlarmHistory](example_cloudwatch_DescribeAlarmHistory_section.md "example_cloudwatch_DescribeAlarmHistory_section.md")
    - [DescribeAlarms](example_cloudwatch_DescribeAlarms_section.md "example_cloudwatch_DescribeAlarms_section.md")
    - [DescribeAlarmsForMetric](example_cloudwatch_DescribeAlarmsForMetric_section.md "example_cloudwatch_DescribeAlarmsForMetric_section.md")
    - [DescribeAnomalyDetectors](example_cloudwatch_DescribeAnomalyDetectors_section.md "example_cloudwatch_DescribeAnomalyDetectors_section.md")
    - [DisableAlarmActions](example_cloudwatch_DisableAlarmActions_section.md "example_cloudwatch_DisableAlarmActions_section.md")
    - [EnableAlarmActions](example_cloudwatch_EnableAlarmActions_section.md "example_cloudwatch_EnableAlarmActions_section.md")
    - [GetDashboard](example_cloudwatch_GetDashboard_section.md "example_cloudwatch_GetDashboard_section.md")
    - [GetMetricData](example_cloudwatch_GetMetricData_section.md "example_cloudwatch_GetMetricData_section.md")
    - [GetMetricStatistics](example_cloudwatch_GetMetricStatistics_section.md "example_cloudwatch_GetMetricStatistics_section.md")
    - [GetMetricWidgetImage](example_cloudwatch_GetMetricWidgetImage_section.md "example_cloudwatch_GetMetricWidgetImage_section.md")
    - [ListDashboards](example_cloudwatch_ListDashboards_section.md "example_cloudwatch_ListDashboards_section.md")
    - [ListMetrics](example_cloudwatch_ListMetrics_section.md "example_cloudwatch_ListMetrics_section.md")
    - [PutAnomalyDetector](example_cloudwatch_PutAnomalyDetector_section.md "example_cloudwatch_PutAnomalyDetector_section.md")
    - [PutDashboard](example_cloudwatch_PutDashboard_section.md "example_cloudwatch_PutDashboard_section.md")
    - [PutMetricAlarm](example_cloudwatch_PutMetricAlarm_section.md "example_cloudwatch_PutMetricAlarm_section.md")
    - [PutMetricData](example_cloudwatch_PutMetricData_section.md "example_cloudwatch_PutMetricData_section.md")

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Get started with alarms](example_cloudwatch_Scenario_GettingStarted_section.md "example_cloudwatch_Scenario_GettingStarted_section.md")
  - [Manage metrics and alarms](example_cloudwatch_Usage_MetricsAlarms_section.md "example_cloudwatch_Usage_MetricsAlarms_section.md")
  - [Monitor DynamoDB performance](example_cross_MonitorDynamoDB_section.md "example_cross_MonitorDynamoDB_section.md")
