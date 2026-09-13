

# Send OpenTelemetry metrics to CloudWatch and alarm on them with PromQL using an AWS SDK
<a name="example_cloudwatch_Scenario_OTelMetrics_section"></a>

The following code examples show how to:
+ Send OTLP metrics to the CloudWatch metrics endpoint with an OpenTelemetry Collector.
+ Start OpenTelemetry enrichment so CloudWatch correlates those metrics with your resources.
+ Create an alarm that evaluates a PromQL query across every series the query returns.
+ Inspect the individual series, called contributors, that put the alarm in ALARM state.
+ Mute the alarm for a maintenance window, then clean up.

------
#### [ .NET ]

**SDK for .NET (v4)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples). 
Wrapper methods for the CloudWatch OpenTelemetry actions.  

```
/// <summary>
/// Wrapper class for the OpenTelemetry features of Amazon CloudWatch: turning on OTel
/// enrichment so that CloudWatch vended metrics are queryable with PromQL, alarming on a
/// PromQL query, inspecting the individual series (contributors) that put a PromQL alarm
/// into ALARM, and muting alarm actions on a schedule.
///
/// Note that OTLP metric ingestion is not an AWS SDK operation. To send OpenTelemetry
/// metrics to CloudWatch, point an OpenTelemetry collector or the AWS Distro for
/// OpenTelemetry (ADOT) SDK at the CloudWatch OTLP metrics endpoint,
/// https://monitoring.{region}.amazonaws.com/v1/metrics. The operations here cover
/// everything you do after those metrics land in CloudWatch.
/// </summary>
public class CloudWatchOTelWrapper
{
    private readonly IAmazonCloudWatch _amazonCloudWatch;
    private readonly ILogger<CloudWatchOTelWrapper> _logger;

    /// <summary>
    /// Constructor for the CloudWatch OpenTelemetry wrapper.
    /// </summary>
    /// <param name="amazonCloudWatch">The injected CloudWatch client.</param>
    /// <param name="logger">The injected logger for the wrapper.</param>
    public CloudWatchOTelWrapper(IAmazonCloudWatch amazonCloudWatch, ILogger<CloudWatchOTelWrapper> logger)
    {
        _logger = logger;
        _amazonCloudWatch = amazonCloudWatch;
    }


    /// <summary>
    /// Turn on OTel enrichment for the account. Once enrichment is running, CloudWatch
    /// vended metrics that carry a resource identifier dimension, such as the Amazon EC2
    /// CPUUtilization metric with its InstanceId dimension, are decorated with resource
    /// ARN and resource tag labels and become queryable with PromQL.
    ///
    /// Resource tags on telemetry must already be enabled for the account before you
    /// call this operation.
    /// </summary>
    /// <returns>True if successful.</returns>
    public async Task<bool> StartOTelEnrichment()
    {
        var response = await _amazonCloudWatch.StartOTelEnrichmentAsync(
            new StartOTelEnrichmentRequest());

        _logger.LogInformation("Started OTel enrichment for this account.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }

    /// <summary>
    /// Get the current OTel enrichment status for the account.
    /// </summary>
    /// <returns>The status, either Running or Stopped.</returns>
    public async Task<OTelEnrichmentStatus> GetOTelEnrichmentStatus()
    {
        var response = await _amazonCloudWatch.GetOTelEnrichmentAsync(
            new GetOTelEnrichmentRequest());

        _logger.LogInformation($"OTel enrichment status is {response.Status}.");
        return response.Status;
    }

    /// <summary>
    /// Create an alarm that evaluates a PromQL query.
    ///
    /// A PromQL alarm differs from a classic metric alarm in a few ways. The query can
    /// match many series at once, and each matching series is tracked separately as a
    /// contributor. Instead of counting breaching periods, you specify durations: a
    /// contributor moves to ALARM after it breaches continuously for the pending period,
    /// and back to OK after it stops breaching for the recovery period. A PromQL alarm
    /// starts in the OK state rather than INSUFFICIENT_DATA.
    ///
    /// EvaluationCriteria is a union and is mutually exclusive with the classic
    /// MetricName and Metrics properties. When you use it you must also set
    /// EvaluationInterval, and you must not set Period, Statistic, Threshold,
    /// ComparisonOperator, EvaluationPeriods, DatapointsToAlarm, or TreatMissingData.
    /// </summary>
    /// <param name="alarmName">The name of the alarm, unique within the Region.</param>
    /// <param name="query">The PromQL query to evaluate, such as
    /// avg(cpu_utilization_percent) &gt; 80. The comparison belongs in the query itself;
    /// there is no separate threshold property.</param>
    /// <param name="evaluationInterval">How often, in seconds, to run the query. Valid
    /// values are 10, 20, 30, and any multiple of 60, up to 3600.</param>
    /// <param name="pendingPeriod">How long, in seconds, a contributor must breach
    /// continuously before it moves to ALARM.</param>
    /// <param name="recoveryPeriod">How long, in seconds, a contributor must stop
    /// breaching before it moves back to OK.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutPromQLMetricAlarm(string alarmName, string query,
        int evaluationInterval = 60, int pendingPeriod = 300, int recoveryPeriod = 120)
    {
        var response = await _amazonCloudWatch.PutMetricAlarmAsync(
            new PutMetricAlarmRequest
            {
                AlarmName = alarmName,
                AlarmDescription = "A PromQL alarm created by the AWS SDK for .NET example.",
                EvaluationCriteria = new EvaluationCriteria
                {
                    PromQLCriteria = new AlarmPromQLCriteria
                    {
                        Query = query,
                        PendingPeriod = pendingPeriod,
                        RecoveryPeriod = recoveryPeriod
                    }
                },
                EvaluationInterval = evaluationInterval
            });

        _logger.LogInformation($"Created PromQL alarm {alarmName} for query {query}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }

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

    /// <summary>
    /// Get the full configuration of an alarm mute rule, including its schedule, the
    /// alarms it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <returns>The mute rule.</returns>
    public async Task<GetAlarmMuteRuleResponse> GetAlarmMuteRule(string name)
    {
        var response = await _amazonCloudWatch.GetAlarmMuteRuleAsync(
            new GetAlarmMuteRuleRequest
            {
                AlarmMuteRuleName = name
            });

        _logger.LogInformation($"Mute rule {response.Name} is {response.Status}.");
        return response;
    }

    /// <summary>
    /// List the alarm mute rules in the account, optionally filtered to the rules that
    /// target one alarm.
    /// </summary>
    /// <param name="alarmName">When specified, only rules that target this alarm are
    /// returned.</param>
    /// <returns>The list of mute rule summaries.</returns>
    public async Task<List<AlarmMuteRuleSummary>> ListAlarmMuteRules(string? alarmName = null)
    {
        var results = new List<AlarmMuteRuleSummary>();
        string? nextToken = null;

        do
        {
            var response = await _amazonCloudWatch.ListAlarmMuteRulesAsync(
                new ListAlarmMuteRulesRequest
                {
                    AlarmName = alarmName,
                    NextToken = nextToken
                });

            if (response.AlarmMuteRuleSummaries != null)
            {
                results.AddRange(response.AlarmMuteRuleSummaries);
            }

            nextToken = response.NextToken;
        } while (!string.IsNullOrEmpty(nextToken));

        _logger.LogInformation($"Got {results.Count} alarm mute rules.");
        return results;
    }

    /// <summary>
    /// Delete an alarm mute rule. The alarms it targeted resume firing their actions.
    /// </summary>
    /// <param name="name">The name of the mute rule.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAlarmMuteRule(string name)
    {
        var response = await _amazonCloudWatch.DeleteAlarmMuteRuleAsync(
            new DeleteAlarmMuteRuleRequest
            {
                AlarmMuteRuleName = name
            });

        _logger.LogInformation($"Deleted alarm mute rule {name}.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }

    /// <summary>
    /// Turn off OTel enrichment for the account. Existing PromQL alarms are not deleted,
    /// but vended metrics stop being enriched with resource ARN and tag labels, so
    /// queries that select on those labels stop matching.
    /// </summary>
    /// <returns>True if successful.</returns>
    public async Task<bool> StopOTelEnrichment()
    {
        var response = await _amazonCloudWatch.StopOTelEnrichmentAsync(
            new StopOTelEnrichmentRequest());

        _logger.LogInformation("Stopped OTel enrichment for this account.");
        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
+ For API details, see the following topics in *AWS SDK for .NET API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarms)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListAlarmMuteRules)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StopOTelEnrichment)

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples). 
A wrapper class for the CloudWatch OpenTelemetry SDK methods.  

```
import software.amazon.awssdk.services.cloudwatch.CloudWatchClient;
import software.amazon.awssdk.services.cloudwatch.model.AlarmContributor;
import software.amazon.awssdk.services.cloudwatch.model.AlarmMuteRuleSummary;
import software.amazon.awssdk.services.cloudwatch.model.AlarmPromQLCriteria;
import software.amazon.awssdk.services.cloudwatch.model.CloudWatchException;
import software.amazon.awssdk.services.cloudwatch.model.DeleteAlarmMuteRuleRequest;
import software.amazon.awssdk.services.cloudwatch.model.DescribeAlarmContributorsRequest;
import software.amazon.awssdk.services.cloudwatch.model.DescribeAlarmContributorsResponse;
import software.amazon.awssdk.services.cloudwatch.model.EvaluationCriteria;
import software.amazon.awssdk.services.cloudwatch.model.GetAlarmMuteRuleRequest;
import software.amazon.awssdk.services.cloudwatch.model.GetAlarmMuteRuleResponse;
import software.amazon.awssdk.services.cloudwatch.model.GetOTelEnrichmentRequest;
import software.amazon.awssdk.services.cloudwatch.model.ListAlarmMuteRulesRequest;
import software.amazon.awssdk.services.cloudwatch.model.ListAlarmMuteRulesResponse;
import software.amazon.awssdk.services.cloudwatch.model.MuteTargets;
import software.amazon.awssdk.services.cloudwatch.model.PutAlarmMuteRuleRequest;
import software.amazon.awssdk.services.cloudwatch.model.PutMetricAlarmRequest;
import software.amazon.awssdk.services.cloudwatch.model.Rule;
import software.amazon.awssdk.services.cloudwatch.model.Schedule;
import software.amazon.awssdk.services.cloudwatch.model.StartOTelEnrichmentRequest;
import software.amazon.awssdk.services.cloudwatch.model.StopOTelEnrichmentRequest;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class CloudWatchOTelActions {


    /**
     * Turns on OTel enrichment for the account. Once enrichment is running, CloudWatch
     * vended metrics that carry a resource identifier dimension, such as the EC2
     * CPUUtilization metric with its InstanceId dimension, are decorated with resource
     * ARN and resource tag labels and become queryable with PromQL.
     *
     * <p>Resource tags on telemetry must already be enabled for the account before you
     * call this operation.
     *
     * @param cw the CloudWatch client
     */
    public static void startOTelEnrichment(CloudWatchClient cw) {
        try {
            cw.startOTelEnrichment(StartOTelEnrichmentRequest.builder().build());
            System.out.println("Started OTel enrichment for this account.");

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }


    /**
     * Gets the current OTel enrichment status for the account.
     *
     * @param cw the CloudWatch client
     * @return the status, either {@code Running} or {@code Stopped}
     */
    public static String getOTelEnrichmentStatus(CloudWatchClient cw) {
        try {
            String status = cw.getOTelEnrichment(GetOTelEnrichmentRequest.builder().build())
                    .statusAsString();
            System.out.printf("OTel enrichment status is %s.%n", status);
            return status;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return null;
        }
    }


    /**
     * Turns off OTel enrichment for the account. Existing PromQL alarms are not
     * deleted, but vended metrics stop being enriched with resource ARN and tag labels,
     * so queries that select on those labels stop matching.
     *
     * @param cw the CloudWatch client
     */
    public static void stopOTelEnrichment(CloudWatchClient cw) {
        try {
            cw.stopOTelEnrichment(StopOTelEnrichmentRequest.builder().build());
            System.out.println("Stopped OTel enrichment for this account.");

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }


    /**
     * Creates an alarm that evaluates a PromQL query.
     *
     * <p>A PromQL alarm differs from a classic metric alarm in a few ways. The query
     * can match many series at once, and each matching series is tracked separately as
     * a contributor. Instead of counting breaching periods, you specify durations: a
     * contributor moves to ALARM after it breaches continuously for the pending period,
     * and back to OK after it stops breaching for the recovery period. A PromQL alarm
     * starts in the OK state rather than INSUFFICIENT_DATA.
     *
     * <p>{@link EvaluationCriteria} is a union and is mutually exclusive with the
     * classic {@code metricName} and {@code metrics} parameters. When you use it you
     * must also set {@code evaluationInterval}, and you must not set {@code period},
     * {@code statistic}, {@code threshold}, {@code comparisonOperator},
     * {@code evaluationPeriods}, {@code datapointsToAlarm}, or
     * {@code treatMissingData}.
     *
     * @param cw                 the CloudWatch client
     * @param alarmName          the name of the alarm, unique within the Region
     * @param query              the PromQL query to evaluate, such as
     *                           {@code avg(cpu_utilization_percent) > 80}. The
     *                           comparison belongs in the query itself; there is no
     *                           separate threshold parameter.
     * @param evaluationInterval how often, in seconds, to run the query. Valid values
     *                           are 10, 20, 30, and any multiple of 60, up to 3600.
     * @param pendingPeriod      how long, in seconds, a contributor must breach
     *                           continuously before it moves to ALARM
     * @param recoveryPeriod     how long, in seconds, a contributor must stop breaching
     *                           before it moves back to OK
     */
    public static void putPromQLMetricAlarm(CloudWatchClient cw, String alarmName, String query,
            int evaluationInterval, int pendingPeriod, int recoveryPeriod) {
        try {
            AlarmPromQLCriteria promQLCriteria = AlarmPromQLCriteria.builder()
                    .query(query)
                    .pendingPeriod(pendingPeriod)
                    .recoveryPeriod(recoveryPeriod)
                    .build();

            PutMetricAlarmRequest request = PutMetricAlarmRequest.builder()
                    .alarmName(alarmName)
                    .alarmDescription("PromQL alarm created by the AWS SDK for Java 2.x example.")
                    .evaluationCriteria(EvaluationCriteria.builder()
                            .promQLCriteria(promQLCriteria)
                            .build())
                    .evaluationInterval(evaluationInterval)
                    .build();

            cw.putMetricAlarm(request);
            System.out.printf("Created PromQL alarm %s for query %s.%n", alarmName, query);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }


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


    /**
     * Gets the full configuration of an alarm mute rule, including its schedule, the
     * alarms it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
     *
     * @param cw   the CloudWatch client
     * @param name the name of the mute rule
     * @return the mute rule
     */
    public static GetAlarmMuteRuleResponse getAlarmMuteRule(CloudWatchClient cw, String name) {
        try {
            GetAlarmMuteRuleResponse response = cw.getAlarmMuteRule(GetAlarmMuteRuleRequest.builder()
                    .alarmMuteRuleName(name)
                    .build());

            System.out.printf("Mute rule %s is %s.%n", response.name(), response.statusAsString());
            return response;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return null;
        }
    }


    /**
     * Lists the alarm mute rules in the account, optionally filtered to the rules that
     * target one alarm.
     *
     * @param cw        the CloudWatch client
     * @param alarmName when non-null, only rules that target this alarm are returned
     * @return the list of mute rule summaries
     */
    public static List<AlarmMuteRuleSummary> listAlarmMuteRules(CloudWatchClient cw, String alarmName) {
        List<AlarmMuteRuleSummary> summaries = new ArrayList<>();
        try {
            String nextToken = null;
            do {
                ListAlarmMuteRulesRequest request = ListAlarmMuteRulesRequest.builder()
                        .alarmName(alarmName)
                        .nextToken(nextToken)
                        .build();

                ListAlarmMuteRulesResponse response = cw.listAlarmMuteRules(request);
                summaries.addAll(response.alarmMuteRuleSummaries());
                nextToken = response.nextToken();
            } while (nextToken != null && !nextToken.isEmpty());

            for (AlarmMuteRuleSummary summary : summaries) {
                System.out.printf("%s (%s)%n", summary.alarmMuteRuleArn(), summary.statusAsString());
            }
            return summaries;

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
            return summaries;
        }
    }


    /**
     * Deletes an alarm mute rule. The alarms it targeted resume firing their actions.
     *
     * @param cw   the CloudWatch client
     * @param name the name of the mute rule
     */
    public static void deleteAlarmMuteRule(CloudWatchClient cw, String name) {
        try {
            cw.deleteAlarmMuteRule(DeleteAlarmMuteRuleRequest.builder()
                    .alarmMuteRuleName(name)
                    .build());

            System.out.printf("Deleted alarm mute rule %s.%n", name);

        } catch (CloudWatchException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListAlarmMuteRules)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StopOTelEnrichment)

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cloudwatch#code-examples). 
Create a class that wraps the CloudWatch OpenTelemetry operations.  

```
import logging
import time

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


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


    def start_otel_enrichment(self):
        """
        Turns on OTel enrichment for the account. Once enrichment is running,
        CloudWatch vended metrics that carry a resource identifier dimension, such as
        the EC2 CPUUtilization metric with its InstanceId dimension, are decorated with
        resource ARN and resource tag labels and become queryable with PromQL.

        Resource tags on telemetry must already be enabled for the account before you
        call this operation.
        """
        try:
            # Boto3 splits the OTel prefix when it converts the StartOTelEnrichment
            # operation name to snake case, so the method is start_o_tel_enrichment.
            self.cloudwatch_client.start_o_tel_enrichment()
            logger.info("Started OTel enrichment for this account.")
        except ClientError:
            logger.exception("Couldn't start OTel enrichment.")
            raise


    def get_otel_enrichment_status(self):
        """
        Gets the current OTel enrichment status for the account.

        :return: The status, either 'Running' or 'Stopped'.
        """
        try:
            response = self.cloudwatch_client.get_o_tel_enrichment()
        except ClientError:
            logger.exception("Couldn't get the OTel enrichment status.")
            raise
        else:
            status = response["Status"]
            logger.info("OTel enrichment status is %s.", status)
            return status


    def create_promql_alarm(
        self,
        alarm_name,
        query,
        evaluation_interval,
        pending_period=300,
        recovery_period=120,
        description=None,
        alarm_actions=None,
    ):
        """
        Creates an alarm that evaluates a PromQL query.

        A PromQL alarm differs from a classic metric alarm in a few ways. The query can
        match many series at once, and each matching series is tracked separately as a
        *contributor*. Instead of counting breaching periods, you specify durations: a
        contributor moves to ALARM after it breaches continuously for the pending
        period, and back to OK after it stops breaching for the recovery period. A
        PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA.

        The PromQL evaluation parameters live in the EvaluationCriteria union, which is
        mutually exclusive with the classic MetricName and Metrics parameters. When you
        use EvaluationCriteria you must also set EvaluationInterval, and you must not
        set Period, Statistic, Threshold, ComparisonOperator, EvaluationPeriods,
        DatapointsToAlarm, or TreatMissingData.

        :param alarm_name: The name of the alarm. Must be unique within the Region.
        :param query: The PromQL query to evaluate, such as
                      'avg(cpu_utilization_percent) > 80'. The comparison belongs in
                      the query itself; there is no separate threshold parameter.
        :param evaluation_interval: How often, in seconds, to run the query. Valid
                                    values are 10, 20, 30, and any multiple of 60, up
                                    to 3600.
        :param pending_period: How long, in seconds, a contributor must breach
                               continuously before it moves to ALARM.
        :param recovery_period: How long, in seconds, a contributor must stop breaching
                                before it moves back to OK.
        :param description: The description of the alarm.
        :param alarm_actions: A list of ARNs to notify when the alarm fires, such as an
                              Amazon SNS topic.
        """
        promql_criteria = {
            "Query": query,
            "PendingPeriod": pending_period,
            "RecoveryPeriod": recovery_period,
        }
        kwargs = {
            "AlarmName": alarm_name,
            "EvaluationCriteria": {"PromQLCriteria": promql_criteria},
            "EvaluationInterval": evaluation_interval,
        }
        if description is not None:
            kwargs["AlarmDescription"] = description
        if alarm_actions is not None:
            kwargs["AlarmActions"] = alarm_actions

        try:
            self.cloudwatch_client.put_metric_alarm(**kwargs)
            logger.info("Created PromQL alarm %s for query %s.", alarm_name, query)
        except ClientError:
            logger.exception("Couldn't create PromQL alarm %s.", alarm_name)
            raise


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


    def get_alarm_mute_rule(self, name):
        """
        Gets the full configuration of an alarm mute rule, including its schedule, the
        alarms it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.

        :param name: The name of the mute rule.
        :return: The mute rule.
        """
        try:
            response = self.cloudwatch_client.get_alarm_mute_rule(
                AlarmMuteRuleName=name
            )
        except ClientError:
            logger.exception("Couldn't get alarm mute rule %s.", name)
            raise
        else:
            logger.info("Got alarm mute rule %s.", name)
            return response


    def list_alarm_mute_rules(self, alarm_name=None, statuses=None):
        """
        Lists alarm mute rules in the account.

        :param alarm_name: When specified, only rules that target this alarm are
                           returned.
        :param statuses: When specified, only rules in these statuses are returned.
                         Valid values are 'SCHEDULED', 'ACTIVE', and 'EXPIRED'.
        :return: The list of mute rule summaries.
        """
        summaries = []
        try:
            next_token = None
            while True:
                kwargs = {}
                if alarm_name is not None:
                    kwargs["AlarmName"] = alarm_name
                if statuses is not None:
                    kwargs["Statuses"] = statuses
                if next_token is not None:
                    kwargs["NextToken"] = next_token
                response = self.cloudwatch_client.list_alarm_mute_rules(**kwargs)
                summaries.extend(response.get("AlarmMuteRuleSummaries", []))
                next_token = response.get("NextToken")
                if not next_token:
                    break
        except ClientError:
            logger.exception("Couldn't list alarm mute rules.")
            raise
        else:
            logger.info("Got %s alarm mute rules.", len(summaries))
            return summaries


    def delete_alarm_mute_rule(self, name):
        """
        Deletes an alarm mute rule.

        :param name: The name of the mute rule.
        """
        try:
            self.cloudwatch_client.delete_alarm_mute_rule(AlarmMuteRuleName=name)
            logger.info("Deleted alarm mute rule %s.", name)
        except ClientError:
            logger.exception("Couldn't delete alarm mute rule %s.", name)
            raise


    def stop_otel_enrichment(self):
        """
        Turns off OTel enrichment for the account. Existing PromQL alarms are not
        deleted, but vended metrics stop being enriched with resource ARN and tag
        labels, so queries that select on those labels stop matching.
        """
        try:
            self.cloudwatch_client.stop_o_tel_enrichment()
            logger.info("Stopped OTel enrichment for this account.")
        except ClientError:
            logger.exception("Couldn't stop OTel enrichment.")
            raise


    def delete_alarms(self, alarm_names):
        """
        Deletes the specified alarms.

        :param alarm_names: The names of the alarms to delete.
        """
        try:
            self.cloudwatch_client.delete_alarms(AlarmNames=alarm_names)
            logger.info("Deleted alarms %s.", ", ".join(alarm_names))
        except ClientError:
            logger.exception("Couldn't delete alarms %s.", ", ".join(alarm_names))
            raise
```
Use the wrapper class to alarm on OpenTelemetry metrics with a PromQL query, inspect the contributors to the alarm, and mute it.  

```
def usage_demo():
    """
    Walks through the OpenTelemetry metrics workflow in CloudWatch: turn on
    enrichment, alarm on a PromQL query, inspect the contributors that matched, mute
    the alarm for a maintenance window, then clean up.

    This scenario assumes OpenTelemetry metrics are already flowing into the account,
    either from an OpenTelemetry collector, the CloudWatch agent, or the ADOT SDK.
    """
    print("-" * 88)
    print("Welcome to the Amazon CloudWatch OpenTelemetry metrics demo!")
    print("-" * 88)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    cw = CloudWatchOTelWrapper.from_client()

    alarm_name = "doc-example-promql-high-cpu"
    mute_rule_name = "doc-example-maintenance-window"

    print("Checking whether OTel enrichment is on for this account.")
    status = cw.get_otel_enrichment_status()
    started_enrichment_here = False
    if status == "Stopped":
        print("Enrichment is stopped. Starting it so vended metrics accept PromQL.")
        cw.start_otel_enrichment()
        started_enrichment_here = True
    else:
        print("Enrichment is already running. Leaving it alone.")

    query = 'avg by (host_name) (cpu_utilization_percent{service_name="checkout"}) > 80'
    print(f"\nCreating a PromQL alarm on: {query}")
    cw.create_promql_alarm(
        alarm_name,
        query,
        evaluation_interval=30,
        pending_period=300,
        recovery_period=120,
        description="Average CPU over 80% per host for the checkout service.",
    )
    print(
        "The alarm evaluates every 30 seconds. A host moves to ALARM after breaching "
        "for 300 seconds straight, and back to OK after 120 seconds clean."
    )

    print("\nWaiting a moment for the first evaluation, then listing contributors.")
    time.sleep(30)
    contributors = cw.describe_alarm_contributors(alarm_name)
    if not contributors:
        print(
            "No contributors yet. The query matched no series, which usually means "
            "no OTel metrics with these labels have arrived. Send some OTel metrics "
            "through the OTLP endpoint and run this again."
        )
    for contributor in contributors:
        labels = ", ".join(
            f"{key}={value}"
            for key, value in sorted(contributor["ContributorAttributes"].items())
        )
        print(f"  {contributor['ContributorId']}: {labels}")
        print(f"    reason: {contributor['StateReason']}")

    print(f"\nMuting {alarm_name} for a weekly two-hour maintenance window.")
    cw.put_alarm_mute_rule(
        mute_rule_name,
        expression="cron(0 2 * * SUN)",
        duration="PT2H",
        alarm_names=[alarm_name],
        timezone="America/Los_Angeles",
        description="Suppress checkout CPU pages during Sunday patching.",
    )
    rule = cw.get_alarm_mute_rule(mute_rule_name)
    print(f"Mute rule status is {rule.get('Status')}.")
    print(
        "While the window is active the alarm keeps evaluating and still changes "
        "state; only its actions are suppressed."
    )

    print(f"\nMute rules targeting {alarm_name}:")
    for summary in cw.list_alarm_mute_rules(alarm_name=alarm_name):
        print(f"  {summary.get('AlarmMuteRuleArn')} ({summary.get('Status')})")

    print("\nCleaning up.")
    cw.delete_alarm_mute_rule(mute_rule_name)
    cw.delete_alarms([alarm_name])
    if started_enrichment_here:
        print("Stopping OTel enrichment, since this demo started it.")
        cw.stop_otel_enrichment()

    print("\nThanks for watching!")
    print("-" * 88)
```
Configure an OpenTelemetry Collector to send the OTLP metrics that this example alarms on to the CloudWatch metrics endpoint. Metric ingestion over OTLP is not an AWS SDK operation, so this half of the example is collector configuration rather than SDK code.  

```
# Purpose
#
# An OpenTelemetry Collector configuration that sends OTLP metrics to the Amazon
# CloudWatch metrics endpoint. Once metrics land in CloudWatch they are queryable with
# PromQL in Query Studio, and you can alarm on them with the PromQL alarm operations
# shown in cloudwatch_otel.py.
#
# Metric ingestion over OTLP is deliberately NOT an AWS SDK operation. There is no
# boto3 call that sends OTLP metrics. You send them with one of the following, in
# rough order of how integrated the CloudWatch experience is:
#
#   1. The CloudWatch agent (recommended). An AWS-managed OpenTelemetry Collector with
#      CloudWatch components pre-built. Adds entity correlation, runtime metrics, and
#      Container Insights support.
#   2. An upstream OpenTelemetry Collector. What this file configures.
#   3. A custom OpenTelemetry Collector build.
#   4. The AWS Distro for OpenTelemetry (ADOT) SDK, with no collector at all.
#
# Prerequisites
#
# * An OpenTelemetry Collector release that includes the sigv4authextension. The
#   contrib distribution does. See
#   https://github.com/open-telemetry/opentelemetry-collector-releases/releases
# * AWS credentials the collector can resolve. On Amazon EC2, attach the
#   CloudWatchAgentServerPolicy managed policy to the instance role. On Amazon EKS,
#   bind that policy to the collector's service account with IRSA. On premises, run
#   `aws configure` for an IAM user that has the same policy.
#
# Run the collector with:
#
#   otelcol-contrib --config otlp_collector_config.yaml
#
# Then point your instrumented application at http://localhost:4318.
#
# For more information, see
# https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html

receivers:
  # The CloudWatch OTLP endpoints are HTTP 1.1 only and do not support gRPC. You can
  # still accept gRPC from your applications here and let the collector translate, but
  # this example keeps the receiver HTTP-only to mirror what is sent upstream.
  otlp:
    protocols:
      http:
        endpoint: "0.0.0.0:4318"

processors:
  # Batch to stay inside the endpoint's per-request limits: 1 MB uncompressed and
  # 1,000 datapoints, counted as the sum across ResourceMetrics, ScopeMetrics, and
  # Metrics. A batch of 200 leaves comfortable headroom.
  batch:
    send_batch_size: 200
    timeout: 10s

exporters:
  otlphttp:
    tls:
      insecure: false
    # Pattern: https://monitoring.{region}.amazonaws.com/v1/metrics
    endpoint: "https://monitoring.us-east-1.amazonaws.com/v1/metrics"
    # Only gzip and none are supported.
    compression: gzip
    auth:
      authenticator: sigv4auth

extensions:
  # SigV4 is the recommended authentication method, and the only one supported for
  # traces. For hosts outside AWS you can instead use the bearertokenauth extension
  # against the metrics or logs endpoints; see
  # https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLP-MetricsBearerTokenAuth.html
  sigv4auth:
    # The metrics endpoint signs as "monitoring". The logs endpoint signs as "logs"
    # and the traces endpoint as "xray".
    service: "monitoring"
    region: "us-east-1"

service:
  extensions: [sigv4auth]
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp]

# Endpoint limits worth designing around, all per account and Region:
#
#   Maximum TPS                  500
#   New series creation rate     1,000,000 per 10-minute window
#   Maximum request size         1 MB uncompressed
#   Maximum datapoint count      1,000 per request
#   Maximum metadata size        40 KB of labels and values per series per datapoint
#   Maximum label count          150 across Resource, Scope, and Datapoint attributes
#   Timestamp window             at most 10 minutes in the future, 14 days in the past
#
# Exceeding the TPS or new-series limits returns 429. The size, count, metadata,
# label, and timestamp limits return 400, and a request whose metrics are only
# partially invalid returns 200 with the valid metrics ingested.
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAlarms)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListAlarmMuteRules)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/StopOTelEnrichment)

------
#### [ Ruby ]

**SDK for Ruby**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples). 
Define methods that call the CloudWatch OpenTelemetry operations.  

```
# Turns on OTel enrichment for the account. Once enrichment is running, CloudWatch vended
# metrics that carry a resource identifier dimension, such as the Amazon EC2
# CPUUtilization metric with its InstanceId dimension, are decorated with resource ARN
# and resource tag labels and become queryable with PromQL.
#
# Resource tags on telemetry must already be enabled for the account before you call
# this operation.
#
# Note that the Ruby SDK renders the OTel prefix as +o_tel+, so the method is
# +start_o_tel_enrichment+ rather than +start_otel_enrichment+.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if enrichment was started; otherwise, false.
def otel_enrichment_started?(cloudwatch_client)
  cloudwatch_client.start_o_tel_enrichment
  true
rescue StandardError => e
  puts "Error starting OTel enrichment: #{e.message}"
  false
end

# Gets the current OTel enrichment status for the account.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [String, nil] 'Running' or 'Stopped', or nil if the status could not be read.
def otel_enrichment_status(cloudwatch_client)
  cloudwatch_client.get_o_tel_enrichment.status
rescue StandardError => e
  puts "Error getting OTel enrichment status: #{e.message}"
  nil
end

# Creates or updates an alarm that evaluates a PromQL query.
#
# A PromQL alarm differs from a classic metric alarm in a few ways. The query can match
# many series at once, and each matching series is tracked separately as a contributor.
# Instead of counting breaching periods, you specify durations: a contributor moves to
# ALARM after it breaches continuously for the pending period, and back to OK after it
# stops breaching for the recovery period. A PromQL alarm starts in the OK state rather
# than INSUFFICIENT_DATA.
#
# The +evaluation_criteria+ union is mutually exclusive with the classic +metric_name+
# and +metrics+ parameters. When you use it you must also set +evaluation_interval+, and
# you must not set +period+, +statistic+, +threshold+, +comparison_operator+,
# +evaluation_periods+, +datapoints_to_alarm+, or +treat_missing_data+.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm, unique within the Region.
# @param criteria [Hash] The PromQL criteria, mirroring the +prom_ql_criteria+ shape:
#   * +:query+ [String] The PromQL query to evaluate, such as
#     'avg(cpu_utilization_percent) > 80'. The comparison belongs in the query itself;
#     there is no separate threshold parameter.
#   * +:pending_period+ [Integer] How long, in seconds, a contributor must breach
#     continuously before it moves to ALARM.
#   * +:recovery_period+ [Integer] How long, in seconds, a contributor must stop
#     breaching before it moves back to OK.
# @param evaluation_interval [Integer] How often, in seconds, to run the query. Valid
#   values are 10, 20, 30, and any multiple of 60, up to 3600.
# @param alarm_description [String] A description of the alarm.
# @return [Boolean] true if the alarm was created or updated; otherwise, false.
def promql_alarm_created_or_updated?(
  cloudwatch_client,
  alarm_name,
  criteria,
  evaluation_interval,
  alarm_description
)
  cloudwatch_client.put_metric_alarm(
    alarm_name: alarm_name,
    alarm_description: alarm_description,
    evaluation_criteria: {
      prom_ql_criteria: {
        query: criteria[:query],
        pending_period: criteria[:pending_period],
        recovery_period: criteria[:recovery_period]
      }
    },
    evaluation_interval: evaluation_interval
  )
  true
rescue StandardError => e
  puts "Error creating PromQL alarm: #{e.message}"
  false
end

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

# Gets the full configuration of an alarm mute rule, including its schedule, the alarms
# it targets, and whether it is currently SCHEDULED, ACTIVE, or EXPIRED.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @return [Aws::CloudWatch::Types::GetAlarmMuteRuleOutput, nil] The mute rule, or nil on
#   error.
def alarm_mute_rule(cloudwatch_client, name)
  cloudwatch_client.get_alarm_mute_rule(alarm_mute_rule_name: name)
rescue StandardError => e
  puts "Error getting alarm mute rule: #{e.message}"
  nil
end

# Lists the alarm mute rules in the account, optionally filtered to the rules that
# target one alarm.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String, nil] When given, only rules that target this alarm are
#   returned.
# @return [Array] The mute rule summaries, as
#   Aws::CloudWatch::Types::AlarmMuteRuleSummary.
def alarm_mute_rules(cloudwatch_client, alarm_name = nil)
  summaries = []
  next_token = nil

  loop do
    response = cloudwatch_client.list_alarm_mute_rules(
      alarm_name: alarm_name,
      next_token: next_token
    )
    summaries.concat(response.alarm_mute_rule_summaries)
    next_token = response.next_token
    break if next_token.nil? || next_token.empty?
  end

  summaries
rescue StandardError => e
  puts "Error listing alarm mute rules: #{e.message}"
  []
end

# Deletes an alarm mute rule. The alarms it targeted resume firing their actions.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param name [String] The name of the mute rule.
# @return [Boolean] true if the mute rule was deleted; otherwise, false.
def alarm_mute_rule_deleted?(cloudwatch_client, name)
  cloudwatch_client.delete_alarm_mute_rule(alarm_mute_rule_name: name)
  true
rescue StandardError => e
  puts "Error deleting alarm mute rule: #{e.message}"
  false
end

# Turns off OTel enrichment for the account. Existing PromQL alarms are not deleted, but
# vended metrics stop being enriched with resource ARN and tag labels, so queries that
# select on those labels stop matching.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if enrichment was stopped; otherwise, false.
def otel_enrichment_stopped?(cloudwatch_client)
  cloudwatch_client.stop_o_tel_enrichment
  true
rescue StandardError => e
  puts "Error stopping OTel enrichment: #{e.message}"
  false
end
```
Alarm on OpenTelemetry metrics with a PromQL query, inspect the contributors to the alarm, and mute it.  

```
# Turns on OpenTelemetry enrichment if the account doesn't already have it on. Enrichment
# is an account-wide setting, so an example should only turn it off again if it was the
# one that turned it on.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if this call started enrichment; otherwise, false.
def enrichment_started_by_example?(cloudwatch_client)
  puts 'Checking whether OTel enrichment is on for this account.'
  status = otel_enrichment_status(cloudwatch_client)
  if status == 'Stopped'
    puts 'Enrichment is stopped. Starting it so vended metrics accept PromQL.'
    return otel_enrichment_started?(cloudwatch_client)
  end

  puts "Enrichment status is '#{status}'. Leaving it alone."
  false
end

# Prints the contributors to a PromQL alarm, one line per matched series.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the PromQL alarm.
def report_alarm_contributors(cloudwatch_client, alarm_name)
  puts "\nContributors for '#{alarm_name}':"
  contributors = alarm_contributors(cloudwatch_client, alarm_name)
  if contributors.empty?
    puts '  None yet. The query matched no series, which usually means no OTel metrics ' \
         'with these labels have arrived.'
    return
  end

  contributors.each do |contributor|
    labels = contributor.contributor_attributes.sort.map { |k, v| "#{k}=#{v}" }.join(', ')
    puts "  #{contributor.contributor_id}: #{labels}"
    puts "    reason: #{contributor.state_reason}"
  end
end

# Mutes an alarm for a recurring weekly maintenance window.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param mute_rule_name [String] The name of the mute rule to create.
# @param alarm_name [String] The name of the alarm to mute.
def mute_alarm_for_maintenance(cloudwatch_client, mute_rule_name, alarm_name)
  puts "\nMuting '#{alarm_name}' for a weekly two-hour maintenance window."
  schedule = {
    expression: 'cron(0 2 * * SUN)',
    duration: 'PT2H',
    timezone: 'America/Los_Angeles'
  }
  return unless alarm_mute_rule_created_or_updated?(
    cloudwatch_client,
    mute_rule_name,
    schedule,
    [alarm_name],
    'Suppress checkout CPU pages during Sunday patching.'
  )

  rule = alarm_mute_rule(cloudwatch_client, mute_rule_name)
  puts "Mute rule status is #{rule.status}." unless rule.nil?
  puts 'While the window is active the alarm keeps evaluating and still changes ' \
       'state; only its actions are suppressed.'
end

# Removes the mute rule and the alarm, and stops enrichment if this example started it.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm to delete.
# @param mute_rule_name [String] The name of the mute rule to delete.
# @param started_here [Boolean] Whether this example started OTel enrichment.
def clean_up(cloudwatch_client, alarm_name, mute_rule_name, started_here)
  puts "\nCleaning up."
  alarm_mute_rule_deleted?(cloudwatch_client, mute_rule_name)
  cloudwatch_client.delete_alarms(alarm_names: [alarm_name])
  return unless started_here

  puts 'Stopping OTel enrichment, since this example started it.'
  otel_enrichment_stopped?(cloudwatch_client)
end

# Walks through the OpenTelemetry metrics workflow in CloudWatch: turn on enrichment,
# alarm on a PromQL query, inspect the contributors that matched, mute the alarm for a
# maintenance window, then clean up.
#
# This scenario assumes OpenTelemetry metrics are already flowing into the account,
# either from an OpenTelemetry collector, the CloudWatch agent, or the ADOT SDK.
def run_me
  alarm_name = 'doc-example-promql-high-cpu'
  mute_rule_name = 'doc-example-maintenance-window'
  query = 'avg by (host_name) (cpu_utilization_percent{service_name="checkout"}) > 80'
  # Replace us-east-1 with the AWS Region you're using for Amazon CloudWatch.
  region = 'us-east-1'

  cloudwatch_client = Aws::CloudWatch::Client.new(region: region)
  started_here = enrichment_started_by_example?(cloudwatch_client)

  puts "\nCreating a PromQL alarm on: #{query}"
  criteria = { query: query, pending_period: 300, recovery_period: 120 }
  unless promql_alarm_created_or_updated?(
    cloudwatch_client,
    alarm_name,
    criteria,
    30,
    'Average CPU over 80% per host for the checkout service.'
  )
    puts "Could not create alarm '#{alarm_name}'. Stopping."
    return
  end
  puts 'The alarm evaluates every 30 seconds. A host moves to ALARM after breaching ' \
       'for 300 seconds straight, and back to OK after 120 seconds clean.'

  report_alarm_contributors(cloudwatch_client, alarm_name)
  mute_alarm_for_maintenance(cloudwatch_client, mute_rule_name, alarm_name)

  puts "\nMute rules targeting '#{alarm_name}':"
  alarm_mute_rules(cloudwatch_client, alarm_name).each do |summary|
    puts "  #{summary.alarm_mute_rule_arn} (#{summary.status})"
  end

  clean_up(cloudwatch_client, alarm_name, mute_rule_name, started_here)
end
```
+ For API details, see the following topics in *AWS SDK for Ruby API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarms)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListAlarmMuteRules)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StopOTelEnrichment)

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudWatch with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.