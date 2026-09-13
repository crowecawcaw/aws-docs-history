

# Use `DescribeAlarmContributors` with an AWS SDK
<a name="example_cloudwatch_DescribeAlarmContributors_section"></a>

The following code examples show how to use `DescribeAlarmContributors`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Send OpenTelemetry metrics and alarm on them with PromQL](example_cloudwatch_Scenario_OTelMetrics_section.md) 

------
#### [ .NET ]

**SDK for .NET (v4)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples). 

```
    /// <summary>
    /// Get the contributors for a PromQL alarm. Each contributor is one series that the
    /// alarm's query matched, identified by its label set. This is how you find out which
    /// hosts, services, or pods are breaching, rather than only that something is.
    /// </summary>
    /// <param name="alarmName">The name of the PromQL alarm.</param>
    /// <returns>The list of contributors.</returns>
    public async Task<List<AlarmContributor>> DescribeAlarmContributors(string alarmName)
    {
        var results = new List<AlarmContributor>();
        string? nextToken = null;

        do
        {
            var response = await _amazonCloudWatch.DescribeAlarmContributorsAsync(
                new DescribeAlarmContributorsRequest
                {
                    AlarmName = alarmName,
                    NextToken = nextToken
                });

            if (response.AlarmContributors != null)
            {
                results.AddRange(response.AlarmContributors);
            }

            nextToken = response.NextToken;
        } while (!string.IsNullOrEmpty(nextToken));

        _logger.LogInformation($"Got {results.Count} contributors for alarm {alarmName}.");
        return results;
    }
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmContributors) in *AWS SDK for .NET API Reference*. 

------
#### [ C\+\+ ]

**SDK for C\+\+**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cloudwatch#code-examples). 
Include the required files.  

```
#include <aws/core/Aws.h>
#include <aws/monitoring/CloudWatchClient.h>
#include <aws/monitoring/model/AlarmContributor.h>
#include <aws/monitoring/model/DescribeAlarmContributorsRequest.h>
#include <iostream>
```
Describe the contributors to a PromQL alarm.  

```
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";
        Aws::CloudWatch::CloudWatchClient cw(clientConfig);

        Aws::CloudWatch::Model::DescribeAlarmContributorsRequest request;
        request.SetAlarmName(alarm_name);

        // Collect every page before reporting. A page can come back empty while still
        // carrying a next token, so the loop must keep going until the token is empty
        // rather than stopping at the first empty page.
        Aws::Vector<Aws::CloudWatch::Model::AlarmContributor> contributors;
        bool failed = false;
        bool done = false;
        while (!done) {
            auto outcome = cw.DescribeAlarmContributors(request);
            if (!outcome.IsSuccess()) {
                std::cerr << "Failed to describe alarm contributors: "
                          << outcome.GetError().GetMessage() << std::endl;
                failed = true;
                break;
            }

            const auto &page = outcome.GetResult().GetAlarmContributors();
            contributors.insert(contributors.end(), page.begin(), page.end());

            const auto &next_token = outcome.GetResult().GetNextToken();
            request.SetNextToken(next_token);
            done = next_token.empty();
        }

        if (!failed) {
            if (contributors.empty()) {
                std::cout << "No contributors yet. The query matched no series, "
                             "which usually means no OTel metrics with these labels "
                             "have arrived."
                          << std::endl;
            }
            else {
                std::cout << "Contributors for alarm " << alarm_name << ":" << std::endl;
                for (const auto &contributor : contributors) {
                    std::cout << "  " << contributor.GetContributorId() << ": ";
                    bool first = true;
                    for (const auto &label : contributor.GetContributorAttributes()) {
                        if (!first) {
                            std::cout << ", ";
                        }
                        std::cout << label.first << "=" << label.second;
                        first = false;
                    }
                    std::cout << std::endl;
                    std::cout << "    reason: " << contributor.GetStateReason()
                              << std::endl;
                }
            }
        }
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmContributors) in *AWS SDK for C\+\+ API Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples). 

```
    /**
     * Gets the contributors for a PromQL alarm. Each contributor is one series that the
     * alarm's query matched, identified by its label set. This is how you find out which
     * hosts, services, or pods are breaching, rather than only that something is.
     *
     * @param cw        the CloudWatch client
     * @param alarmName the name of the PromQL alarm
     * @return the list of contributors
     */
    public static List<AlarmContributor> describeAlarmContributors(CloudWatchClient cw, String alarmName) {
        List<AlarmContributor> contributors = new ArrayList<>();
        try {
            String nextToken = null;
            do {
                DescribeAlarmContributorsRequest request = DescribeAlarmContributorsRequest.builder()
                        .alarmName(alarmName)
                        .nextToken(nextToken)
                        .build();

                DescribeAlarmContributorsResponse response = cw.describeAlarmContributors(request);
                contributors.addAll(response.alarmContributors());
                nextToken = response.nextToken();
            } while (nextToken != null && !nextToken.isEmpty());

            for (AlarmContributor contributor : contributors) {
                StringBuilder labels = new StringBuilder();
                for (Map.Entry<String, String> attribute : contributor.contributorAttributes().entrySet()) {
                    if (labels.length() > 0) {
                        labels.append(", ");
                    }
                    labels.append(attribute.getKey()).append("=").append(attribute.getValue());
                }
                System.out.printf("%s: %s%n", contributor.contributorId(), labels);
                System.out.printf("  reason: %s%n", contributor.stateReason());
            }
            return contributors;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return contributors;
        }
    }
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cloudwatch#code-examples). 

```
import { DescribeAlarmContributorsCommand } from "@aws-sdk/client-cloudwatch";
import { client } from "../libs/client.js";

// Get the contributors for a PromQL alarm. Each contributor is one series that the
// alarm's query matched, identified by its label set. This is how you find out which
// hosts, services, or pods are breaching, rather than only that something is.
const run = async () => {
  const contributors = [];
  let nextToken;

  try {
    do {
      const command = new DescribeAlarmContributorsCommand({
        AlarmName: process.env.CLOUDWATCH_ALARM_NAME, // Set CLOUDWATCH_ALARM_NAME to the name of an existing PromQL alarm.
        NextToken: nextToken,
      });
      const response = await client.send(command);
      contributors.push(...(response.AlarmContributors ?? []));
      nextToken = response.NextToken;
    } while (nextToken);

    for (const contributor of contributors) {
      const labels = Object.entries(contributor.ContributorAttributes)
        .map(([key, value]) => `${key}=${value}`)
        .join(", ");
      console.log(`${contributor.ContributorId}: ${labels}`);
      console.log(`  reason: ${contributor.StateReason}`);
    }
    return contributors;
  } catch (err) {
    console.error(err);
  }
};

export default run();
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/DescribeAlarmContributorsCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples). 

```
suspend fun describeAlarmContributors(alarmNameVal: String): List<AlarmContributor> {
    val contributors = mutableListOf<AlarmContributor>()

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        var token: String? = null
        do {
            val response =
                cwClient.describeAlarmContributors(
                    DescribeAlarmContributorsRequest {
                        alarmName = alarmNameVal
                        nextToken = token
                    },
                )

            response.alarmContributors?.let { contributors.addAll(it) }
            token = response.nextToken
        } while (token != null)

        if (contributors.isEmpty()) {
            println(
                "No contributors yet. The query matched no series, which usually means no " +
                    "OTel metrics with these labels have arrived",
            )
        }

        contributors.forEach { contributor ->
            val labels =
                contributor.contributorAttributes
                    ?.entries
                    ?.sortedBy { it.key }
                    ?.joinToString(", ") { "${it.key}=${it.value}" }
            println("${contributor.contributorId}: $labels")
            println("  reason: ${contributor.stateReason}")
        }
    }
    return contributors
}
```
+  For API details, see [DescribeAlarmContributors](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cloudwatch#code-examples). 

```
class CloudWatchOTelWrapper:
    """Encapsulates the OpenTelemetry-oriented Amazon CloudWatch operations."""

    def __init__(self, cloudwatch_client):
        """
        :param cloudwatch_client: A Boto3 CloudWatch client. The OpenTelemetry
                                  operations are only available on the client
                                  interface, not on the higher-level
                                  ``boto3.resource("cloudwatch")`` interface.
        """
        self.cloudwatch_client = cloudwatch_client

    @classmethod
    def from_client(cls):
        """
        Creates a wrapper backed by a default CloudWatch client.

        :return: A CloudWatchOTelWrapper.
        """
        return cls(boto3.client("cloudwatch"))


    def describe_alarm_contributors(self, alarm_name):
        """
        Gets the contributors for a PromQL alarm. Each contributor is one series that
        the alarm's query matched, identified by its label set. This is how you find out
        *which* hosts, services, or pods are breaching, rather than only that something
        is.

        :param alarm_name: The name of the PromQL alarm.
        :return: The list of contributors. Each contributor has a ContributorId, a
                 ContributorAttributes map of the labels that identify the series, a
                 StateReason, and the time it last changed state.
        """
        contributors = []
        try:
            next_token = None
            while True:
                kwargs = {"AlarmName": alarm_name}
                if next_token is not None:
                    kwargs["NextToken"] = next_token
                response = self.cloudwatch_client.describe_alarm_contributors(**kwargs)
                contributors.extend(response["AlarmContributors"])
                next_token = response.get("NextToken")
                if not next_token:
                    break
        except ClientError:
            logger.exception("Couldn't get contributors for alarm %s.", alarm_name)
            raise
        else:
            logger.info(
                "Got %s contributors for alarm %s.", len(contributors), alarm_name
            )
            return contributors
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmContributors) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ Ruby ]

**SDK for Ruby**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples). 

```
# Gets the contributors for a PromQL alarm. Each contributor is one series that the
# alarm's query matched, identified by its label set. This is how you find out which
# hosts, services, or pods are breaching, rather than only that something is.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the PromQL alarm.
# @return [Array] The contributors, as Aws::CloudWatch::Types::AlarmContributor.
def alarm_contributors(cloudwatch_client, alarm_name)
  contributors = []
  next_token = nil

  loop do
    response = cloudwatch_client.describe_alarm_contributors(
      alarm_name: alarm_name,
      next_token: next_token
    )
    contributors.concat(response.alarm_contributors)
    next_token = response.next_token
    break if next_token.nil? || next_token.empty?
  end

  contributors
rescue StandardError => e
  puts "Error getting alarm contributors: #{e.message}"
  []
end
```
+  For API details, see [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors) in *AWS SDK for Ruby API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudWatch with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.