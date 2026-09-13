

# Use `PutAlarmMuteRule` with an AWS SDK
<a name="example_cloudwatch_PutAlarmMuteRule_section"></a>

The following code examples show how to use `PutAlarmMuteRule`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Send OpenTelemetry metrics and alarm on them with PromQL](example_cloudwatch_Scenario_OTelMetrics_section.md) 

------
#### [ .NET ]

**SDK for .NET (v4)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples). 

```
    /// <summary>
    /// Create or update an alarm mute rule. While a mute rule is active the targeted
    /// alarms keep evaluating and keep transitioning between states, but their configured
    /// actions do not fire. This is the supported way to suppress notifications during a
    /// known maintenance window, instead of disabling alarm actions and relying on
    /// someone to turn them back on.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <param name="expression">When the rule activates. For a recurring window, use a
    /// five-field cron expression, cron(Minutes Hours Day-of-month Month Day-of-week),
    /// such as cron(0 2 * * SUN) for every Sunday at 2:00 AM. Note that this is five
    /// fields, not the six that Amazon EventBridge uses. For a one-time window, use
    /// at(yyyy-MM-ddThh:mm), such as at(2026-09-05T02:00).</param>
    /// <param name="duration">How long the mute window lasts once it activates, in
    /// ISO 8601 duration format, from PT1M (one minute) to P15D (15 days). For example,
    /// PT2H is two hours and P2DT12H is two days and 12 hours.</param>
    /// <param name="timezone">The time zone the expression is evaluated in, such as
    /// America/Los_Angeles.</param>
    /// <param name="alarmNames">The names of up to 100 alarms to mute. If null or empty,
    /// the rule applies to all alarms in the account.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutAlarmMuteRule(string name, string expression, string duration,
        string timezone, List<string>? alarmNames = null)
    {
        var request = new PutAlarmMuteRuleRequest
        {
            Name = name,
            Description = "A mute rule created by the AWS SDK for .NET example.",
            Rule = new Rule
            {
                Schedule = new Schedule
                {
                    Expression = expression,
                    Duration = duration,
                    Timezone = timezone
                }
            }
        };

        if (alarmNames != null && alarmNames.Any())
        {
            request.MuteTargets = new MuteTargets { AlarmNames = alarmNames };
        }

        var response = await _amazonCloudWatch.PutAlarmMuteRuleAsync(request);

        _logger.LogInformation($"Put alarm mute rule {name}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAlarmMuteRule) in *AWS SDK for .NET API Reference*. 

------
#### [ C\+\+ ]

**SDK for C\+\+**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cloudwatch#code-examples). 
Include the required files.  

```
#include <aws/core/Aws.h>
#include <aws/monitoring/CloudWatchClient.h>
#include <aws/monitoring/model/MuteTargets.h>
#include <aws/monitoring/model/PutAlarmMuteRuleRequest.h>
#include <aws/monitoring/model/Rule.h>
#include <aws/monitoring/model/Schedule.h>
#include <iostream>
```
Create the alarm mute rule.  

```
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";
        Aws::CloudWatch::CloudWatchClient cw(clientConfig);

        // For a recurring window, use a five-field cron expression,
        // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five
        // fields, not the six that Amazon EventBridge uses. For a one-time window, use
        // an at expression such as at(2026-09-05T02:00).
        Aws::CloudWatch::Model::Schedule schedule;
        schedule.SetExpression("cron(0 2 * * SUN)");
        // The duration is in ISO 8601 duration format, from PT1M (one minute) to
        // P15D (15 days).
        schedule.SetDuration("PT2H");
        schedule.SetTimezone("America/Los_Angeles");

        Aws::CloudWatch::Model::Rule rule;
        rule.SetSchedule(schedule);

        // Target up to 100 alarms. If MuteTargets is not set, the rule applies to every
        // alarm in the account.
        Aws::CloudWatch::Model::MuteTargets muteTargets;
        muteTargets.AddAlarmNames(alarm_name);

        Aws::CloudWatch::Model::PutAlarmMuteRuleRequest request;
        request.SetName(mute_rule_name);
        request.SetDescription("A mute rule created by the AWS SDK for C++.");
        request.SetRule(rule);
        request.SetMuteTargets(muteTargets);

        auto outcome = cw.PutAlarmMuteRule(request);
        if (!outcome.IsSuccess()) {
            std::cerr << "Failed to put alarm mute rule: "
                      << outcome.GetError().GetMessage() << std::endl;
        } else {
            std::cout << "Successfully put alarm mute rule " << mute_rule_name
                      << std::endl;
        }
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutAlarmMuteRule) in *AWS SDK for C\+\+ API Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples). 

```
    /**
     * Creates or updates an alarm mute rule. While a mute rule is active the targeted
     * alarms keep evaluating and keep transitioning between states, but their configured
     * actions do not fire. This is the supported way to suppress notifications during a
     * known maintenance window instead of disabling alarm actions and hoping someone
     * remembers to turn them back on.
     *
     * @param cw         the CloudWatch client
     * @param name       the name of the mute rule
     * @param expression when the rule activates. For a recurring window, use a
     *                   five-field cron expression,
     *                   {@code cron(Minutes Hours Day-of-month Month Day-of-week)},
     *                   such as {@code cron(0 2 * * SUN)} for every Sunday at 2:00 AM.
     *                   Note that this is five fields, not the six that Amazon
     *                   EventBridge uses. For a one-time window, use
     *                   {@code at(yyyy-MM-ddThh:mm)}, such as
     *                   {@code at(2026-09-05T02:00)}.
     * @param duration   how long the mute window lasts once it activates, in ISO 8601
     *                   duration format, from {@code PT1M} (one minute) to
     *                   {@code P15D} (15 days). For example, {@code PT2H} is two hours
     *                   and {@code P2DT12H} is two days and 12 hours.
     * @param timezone   the time zone the expression is evaluated in, such as
     *                   {@code America/Los_Angeles}
     * @param alarmNames the names of up to 100 alarms to mute. If empty, the rule
     *                   applies to all alarms in the account.
     */
    public static void putAlarmMuteRule(CloudWatchClient cw, String name, String expression, String duration,
            String timezone, List<String> alarmNames) {
        try {
            Schedule schedule = Schedule.builder()
                    .expression(expression)
                    .duration(duration)
                    .timezone(timezone)
                    .build();

            PutAlarmMuteRuleRequest.Builder request = PutAlarmMuteRuleRequest.builder()
                    .name(name)
                    .description("Mute rule created by the AWS SDK for Java 2.x example.")
                    .rule(Rule.builder().schedule(schedule).build());

            if (alarmNames != null && !alarmNames.isEmpty()) {
                request.muteTargets(MuteTargets.builder().alarmNames(alarmNames).build());
            }

            cw.putAlarmMuteRule(request.build());
            System.out.printf("Put alarm mute rule %s.%n", name);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAlarmMuteRule) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cloudwatch#code-examples). 

```
import { PutAlarmMuteRuleCommand } from "@aws-sdk/client-cloudwatch";
import { client } from "../libs/client.js";

// Create or update an alarm mute rule. While a mute rule is active the targeted alarms
// keep evaluating and keep transitioning between states, but their configured actions
// do not fire. This is the supported way to suppress notifications during a known
// maintenance window, instead of disabling alarm actions and hoping someone remembers
// to turn them back on.
const run = async () => {
  const command = new PutAlarmMuteRuleCommand({
    Name: process.env.CLOUDWATCH_MUTE_RULE_NAME, // Set CLOUDWATCH_MUTE_RULE_NAME to the name of the mute rule.
    Description: "Suppress checkout CPU pages during Sunday patching.",
    Rule: {
      Schedule: {
        // For a recurring window, use a five-field cron expression,
        // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five
        // fields, not the six that Amazon EventBridge uses. For a one-time window, use
        // an at expression such as "at(2026-09-05T02:00)".
        Expression: "cron(0 2 * * SUN)",
        // How long the mute window lasts once it activates, in ISO 8601 duration
        // format, from PT1M (one minute) to P15D (15 days).
        Duration: "PT2H",
        Timezone: "America/Los_Angeles",
      },
    },
    // Target up to 100 alarms by name. Omit MuteTargets to mute every alarm in the
    // account.
    MuteTargets: {
      AlarmNames: [process.env.CLOUDWATCH_ALARM_NAME], // Set CLOUDWATCH_ALARM_NAME to the name of an existing alarm.
    },
  });

  try {
    return await client.send(command);
  } catch (err) {
    console.error(err);
  }
};

export default run();
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/PutAlarmMuteRuleCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples). 

```
suspend fun putAlarmMuteRule(
    muteRuleName: String,
    expressionVal: String,
    durationVal: String,
    alarmNamesVal: List<String>,
    timezoneVal: String = "America/Los_Angeles",
) {
    // For a recurring window, use a five-field cron expression,
    // cron(Minutes Hours Day-of-month Month Day-of-week), such as cron(0 2 * * SUN).
    // Note that this is five fields, not the six that Amazon EventBridge uses. For a
    // one-time window, use at(yyyy-MM-ddThh:mm), such as at(2026-09-05T02:00). The
    // duration is in ISO 8601 duration format, from PT1M (one minute) to P15D (15 days).
    val scheduleOb =
        Schedule {
            expression = expressionVal
            duration = durationVal
            timezone = timezoneVal
        }

    val request =
        PutAlarmMuteRuleRequest {
            name = muteRuleName
            description = "A mute rule created by the Kotlin SDK"
            rule =
                Rule {
                    schedule = scheduleOb
                }
            // Target up to 100 alarms. If muteTargets is omitted, the rule applies to
            // every alarm in the account.
            if (alarmNamesVal.isNotEmpty()) {
                muteTargets =
                    MuteTargets {
                        alarmNames = alarmNamesVal
                    }
            }
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putAlarmMuteRule(request)
        println("Successfully put alarm mute rule $muteRuleName")
    }
}
```
+  For API details, see [PutAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

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


    def put_alarm_mute_rule(
        self,
        name,
        expression,
        duration,
        alarm_names=None,
        timezone=None,
        description=None,
    ):
        """
        Creates or updates an alarm mute rule. While a mute rule is active the targeted
        alarms keep evaluating and keep transitioning between states, but their
        configured actions do not fire. This is the supported way to suppress
        notifications during a known maintenance window instead of disabling alarm
        actions and hoping someone remembers to turn them back on.

        :param name: The name of the mute rule.
        :param expression: When the rule activates. For a recurring window, use a
                           five-field cron expression,
                           'cron(Minutes Hours Day-of-month Month Day-of-week)', such as
                           'cron(0 2 * * SUN)' for every Sunday at 2:00 AM. Note that
                           this is five fields, not the six that Amazon EventBridge
                           uses. For a one-time window, use 'at(yyyy-MM-ddThh:mm)',
                           such as 'at(2026-09-05T02:00)'.
        :param duration: How long the mute window lasts once it activates, in ISO 8601
                         duration format, from 'PT1M' (one minute) to 'P15D' (15 days).
                         For example, 'PT2H' is two hours and 'P2DT12H' is two days and
                         12 hours.
        :param alarm_names: The names of up to 100 alarms to mute. If omitted, the rule
                            applies to all alarms in the account.
        :param timezone: The time zone the expression is evaluated in, such as
                         'America/Los_Angeles'.
        :param description: The description of the mute rule.
        """
        schedule = {"Expression": expression, "Duration": duration}
        if timezone is not None:
            schedule["Timezone"] = timezone

        kwargs = {"Name": name, "Rule": {"Schedule": schedule}}
        if alarm_names is not None:
            kwargs["MuteTargets"] = {"AlarmNames": alarm_names}
        if description is not None:
            kwargs["Description"] = description

        try:
            self.cloudwatch_client.put_alarm_mute_rule(**kwargs)
            logger.info("Put alarm mute rule %s.", name)
        except ClientError:
            logger.exception("Couldn't put alarm mute rule %s.", name)
            raise
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutAlarmMuteRule) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ Ruby ]

**SDK for Ruby**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples). 

```
# Creates or updates an alarm mute rule. While a mute rule is active the targeted alarms
# keep evaluating and keep transitioning between states, but their configured actions do
# not fire. This is the supported way to suppress notifications during a known
# maintenance window, instead of disabling alarm actions and relying on someone to turn
# them back on.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @param schedule [Hash] The mute window, mirroring the +rule.schedule+ shape:
#   * +:expression+ [String] When the rule activates. For a recurring window, use a
#     five-field cron expression,
#     'cron(Minutes Hours Day-of-month Month Day-of-week)', such as
#     'cron(0 2 * * SUN)' for every Sunday at 2:00 AM. Note that this is five fields,
#     not the six that Amazon EventBridge uses. For a one-time window, use
#     'at(yyyy-MM-ddThh:mm)', such as 'at(2026-09-05T02:00)'.
#   * +:duration+ [String] How long the mute window lasts once it activates, in ISO 8601
#     duration format, from 'PT1M' (one minute) to 'P15D' (15 days). For example,
#     'PT2H' is two hours and 'P2DT12H' is two days and 12 hours.
#   * +:timezone+ [String] The time zone the expression is evaluated in, such as
#     'America/Los_Angeles'.
# @param alarm_names [Array] The names of up to 100 alarms to mute. If empty, the rule
#   applies to all alarms in the account.
# @param description [String] A description of the mute rule.
# @return [Boolean] true if the mute rule was created or updated; otherwise, false.
def alarm_mute_rule_created_or_updated?(
  cloudwatch_client,
  name,
  schedule,
  alarm_names,
  description
)
  params = {
    name: name,
    description: description,
    rule: {
      schedule: {
        expression: schedule[:expression],
        duration: schedule[:duration],
        timezone: schedule[:timezone]
      }
    }
  }
  params[:mute_targets] = { alarm_names: alarm_names } unless alarm_names.empty?

  cloudwatch_client.put_alarm_mute_rule(params)
  true
rescue StandardError => e
  puts "Error putting alarm mute rule: #{e.message}"
  false
end
```
+  For API details, see [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAlarmMuteRule) in *AWS SDK for Ruby API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudWatch with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.