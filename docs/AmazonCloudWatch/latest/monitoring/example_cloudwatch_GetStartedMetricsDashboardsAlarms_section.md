

# Learn core operations for CloudWatch using an AWS SDK
<a name="example_cloudwatch_GetStartedMetricsDashboardsAlarms_section"></a>

The following code examples show how to:
+ List CloudWatch namespaces and metrics.
+ Start OpenTelemetry enrichment so CloudWatch correlates incoming OTLP metrics with the resources that produced them.
+ See how OTLP metrics reach the CloudWatch metrics endpoint. Metric ingestion over OTLP is not an AWS SDK operation.
+ Create an alarm that evaluates a PromQL query.
+ Inspect the alarm's contributors, the individual series that the query matched.
+ Get statistics for a metric and chart it on a dashboard.
+ Mute the alarm for a maintenance window, then clean up.

------
#### [ .NET ]

**SDK for .NET (v4)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/CloudWatch#code-examples). 
Run an interactive scenario at a command prompt.  

```
public class CloudWatchScenario
{
    /*
    Before running this .NET code example, set up your development environment, including your credentials.

    This scenario demonstrates the Amazon CloudWatch OpenTelemetry (OTel) experience.
    CloudWatch ingests OpenTelemetry metrics natively, and this example walks through what
    you do with them: turning on enrichment so CloudWatch can correlate incoming OTLP
    metrics with the resources that produced them, alarming on those metrics with a PromQL
    query, and finding out which individual series drove the alarm.

    A PromQL alarm works differently from a classic metric alarm. Rather than watching one
    metric and counting breaching periods, it evaluates a query that can match many series
    at once, and tracks each matching series separately as a contributor.

    Note that sending OTLP metrics to CloudWatch is not an AWS SDK operation. Metrics
    arrive over the OTLP protocol through the CloudWatch agent, an OpenTelemetry
    Collector, or an ADOT SDK. Everything this scenario does is configuration and querying
    around that ingestion path.

    This .NET example performs the following tasks:
        1. List metrics and namespaces from CloudWatch.
        2. Start OpenTelemetry enrichment for the account.
        3. Explain how OTLP metrics reach CloudWatch.
        4. Create an alarm that evaluates a PromQL query.
        5. Inspect the contributors to the PromQL alarm.
        6. Get metric statistics and chart the metric on a dashboard.
        7. Mute the alarm for a maintenance window.
        8. Clean up resources.
    */

    private static ILogger logger = null!;
    private static CloudWatchWrapper _cloudWatchWrapper = null!;
    private static CloudWatchOTelWrapper _otelWrapper = null!;
    private static IConfiguration _configuration = null!;

    private const string DefaultQuery = "avg by (host) (system_cpu_utilization) > 80";

    // Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
    private const int EvaluationInterval = 60;
    private const int PendingPeriod = 300;
    private const int RecoveryPeriod = 120;

    private static string _alarmName = null!;
    private static string _dashboardName = null!;
    private static string _muteRuleName = null!;

    // Tracks whether this run turned enrichment on, so that cleanup only turns off
    // enrichment that this run started.
    private static bool _startedEnrichment;
    private static bool _dashboardCreated;
    private static string _region = null!;

    static async Task Main(string[] args)
    {
        // Set up dependency injection for the Amazon service.
        using var host = Host.CreateDefaultBuilder(args)
            .ConfigureLogging(logging =>
                logging.AddFilter("System", LogLevel.Debug)
                    .AddFilter<DebugLoggerProvider>("Microsoft", LogLevel.Information)
                    .AddFilter<ConsoleLoggerProvider>("Microsoft", LogLevel.Trace))
            .ConfigureServices((_, services) =>
            services.AddAWSService<IAmazonCloudWatch>()
            .AddTransient<CloudWatchWrapper>()
            .AddTransient<CloudWatchOTelWrapper>()
        )
        .Build();

        _configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("settings.json") // Load settings from .json file.
            .AddJsonFile("settings.local.json",
                true) // Optionally, load local settings.
            .Build();

        logger = LoggerFactory.Create(builder => { builder.AddConsole(); })
            .CreateLogger<CloudWatchScenario>();

        _cloudWatchWrapper = host.Services.GetRequiredService<CloudWatchWrapper>();
        _otelWrapper = host.Services.GetRequiredService<CloudWatchOTelWrapper>();

        // A metric widget must name its region, because a dashboard can chart
        // metrics from several.
        _region = host.Services.GetRequiredService<IAmazonCloudWatch>()
            .Config.RegionEndpoint.SystemName;

        // Suffix the resource names so repeated runs do not collide.
        var suffix = Random.Shared.Next(1000, 9999).ToString();
        _alarmName = $"doc-example-promql-alarm-{suffix}";
        _dashboardName = $"doc-example-dashboard-{suffix}";
        _muteRuleName = $"doc-example-mute-rule-{suffix}";

        Console.WriteLine(new string('-', 80));
        Console.WriteLine("Welcome to the Amazon CloudWatch Basics scenario.");
        Console.WriteLine(new string('-', 80));
        Console.WriteLine(
            "\nCloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through" +
            "\nthat experience: it turns on OTel enrichment so CloudWatch can correlate incoming" +
            "\nOTLP metrics with the resources that produced them, alarms on those metrics with a" +
            "\nPromQL query, and shows you which individual series drove the alarm." +
            "\n" +
            "\nA PromQL alarm works differently from a classic metric alarm. Rather than watching" +
            "\none metric and counting breaching periods, it evaluates a query that can match many" +
            "\nseries at once, and tracks each one separately as a contributor.\n");

        try
        {
            var namespaces = await ListMetricsAndNamespaces();
            await StartOTelEnrichment();
            ExplainOtlpIngestion();
            await CreatePromQlAlarm();
            await InspectAlarmContributors();
            await GetStatisticsAndChartMetric(namespaces);
            await MuteAlarmForMaintenance();
            await CleanUp();

            Console.WriteLine(new string('-', 80));
            Console.WriteLine("CloudWatch Basics scenario is complete.");
            Console.WriteLine(new string('-', 80));
        }
        catch (Exception ex)
        {
            Console.WriteLine(new string('-', 80));
            logger.LogError(ex, "There was a problem executing the scenario.");
            await CleanUp();
            Console.WriteLine(new string('-', 80));
        }
    }

    /// <summary>
    /// List the metrics and namespaces already present in the account, to orient the
    /// reader before any configuration happens.
    /// </summary>
    /// <returns>The distinct namespaces found.</returns>
    private static async Task<List<string>> ListMetricsAndNamespaces()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("1. List metrics and namespaces");
        Console.WriteLine(
            "\nBefore configuring anything, let's see what CloudWatch is already collecting in" +
            "\nthis account by calling ListMetrics.\n");

        var metrics = await _cloudWatchWrapper.ListMetrics();

        // Order by metric count descending, so the most-populated namespace comes first.
        // Step 6 charts a metric from that namespace, and a busy namespace is the one most
        // likely to have datapoints worth looking at.
        var namespaceCounts = metrics
            .GroupBy(m => m.Namespace)
            .Select(g => new { Namespace = g.Key, Count = g.Count() })
            .OrderByDescending(n => n.Count)
            .ToList();
        var namespaces = namespaceCounts.Select(n => n.Namespace).ToList();

        Console.WriteLine($"\tFound {metrics.Count} metrics across {namespaces.Count} namespaces:");
        foreach (var entry in namespaceCounts.Take(10))
        {
            Console.WriteLine($"\t  {entry.Namespace} ({entry.Count} metrics)");
        }

        if (!namespaces.Any())
        {
            Console.WriteLine(
                "\tNo metrics found in this account. The statistics and dashboard steps later on" +
                "\n\tneed an existing metric, so they will be skipped.");
        }

        Console.WriteLine(new string('-', 80));
        return namespaces;
    }

    /// <summary>
    /// Start OTel enrichment, but only if it is not already running. Enrichment is what
    /// makes CloudWatch attach AWS resource context to incoming OTLP metrics.
    /// </summary>
    private static async Task StartOTelEnrichment()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("2. Start OpenTelemetry enrichment");
        Console.WriteLine(
            "\nEnrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics" +
            "\nyou send it. Without it, your metrics arrive as opaque series with no connection to" +
            "\nthe resources that emitted them." +
            "\n" +
            "\nWe check the current state first, and only start enrichment if it isn't already on.\n");

        var status = await _otelWrapper.GetOTelEnrichmentStatus();
        Console.WriteLine($"\tEnrichment status: {status}");

        if (status != OTelEnrichmentStatus.Running)
        {
            // Record the attempt before making it. We already know enrichment was not running,
            // so stopping it during cleanup is always safe, and a call that starts enrichment
            // but then fails to report back (a timeout, say) would otherwise leave it running.
            _startedEnrichment = true;
            await _otelWrapper.StartOTelEnrichment();

            status = await _otelWrapper.GetOTelEnrichmentStatus();
            Console.WriteLine($"\tEnrichment status: {status}");
            Console.WriteLine(
                "\n\tNote: this run started enrichment, so the cleanup step will stop it again.");
        }
        else
        {
            Console.WriteLine(
                "\n\tEnrichment was already running, so we will leave it alone. The cleanup step" +
                "\n\twill not stop it, because other workloads in this account may depend on it.");
        }

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Explain that OTLP metric ingestion is not an AWS SDK operation. This step makes no
    /// service call; naming the gap explicitly is the point.
    /// </summary>
    private static void ExplainOtlpIngestion()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("3. Send OTLP metrics to CloudWatch");
        Console.WriteLine(
            "\nThis step is not an AWS SDK operation, and that's worth being explicit about." +
            "\nMetrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an" +
            "\nOpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call." +
            "\n" +
            "\nPoint your collector at the CloudWatch metrics endpoint, which follows the pattern" +
            "\n\thttps://monitoring.<region>.amazonaws.com/v1/metrics" +
            "\n" +
            "\nThe endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp" +
            "\nexporter rather than otlp. The metrics endpoint signs as \"monitoring\".\n");
        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Create an alarm whose evaluation is a PromQL query.
    /// </summary>
    private static async Task CreatePromQlAlarm()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("4. Create a PromQL alarm");
        Console.WriteLine(
            "\nNow we alarm on those metrics. The comparison goes inside the query itself: a" +
            "\nPromQL alarm has no separate threshold, comparison operator, statistic, or period.\n");

        Console.WriteLine($"Enter a PromQL query, or press <ENTER> for the default\n[{DefaultQuery}]:");
        var input = Console.ReadLine();
        var query = string.IsNullOrWhiteSpace(input) ? DefaultQuery : input.Trim();

        await _otelWrapper.PutPromQLMetricAlarm(_alarmName, query,
            EvaluationInterval, PendingPeriod, RecoveryPeriod);

        Console.WriteLine($"\tCreated alarm {_alarmName}:");
        Console.WriteLine($"\t  query:              {query}");
        Console.WriteLine($"\t  evaluationInterval: {EvaluationInterval} seconds");
        Console.WriteLine($"\t  pendingPeriod:      {PendingPeriod} seconds");
        Console.WriteLine($"\t  recoveryPeriod:     {RecoveryPeriod} seconds");
        Console.WriteLine(
            "\n\tA PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is" +
            "\n\tanother way it differs from a classic alarm.");

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Show which individual series the alarm's query matched. This is the step with no
    /// classic-alarm equivalent.
    /// </summary>
    private static async Task InspectAlarmContributors()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("5. Inspect the alarm's contributors");
        Console.WriteLine(
            "\nEach contributor is one series the query matched, identified by its label set." +
            "\nThis is how you find out which host is unhealthy rather than only that something" +
            "\nis. Classic alarms have no equivalent.\n");

        var contributors = await _otelWrapper.DescribeAlarmContributors(_alarmName);

        if (!contributors.Any())
        {
            Console.WriteLine(
                "\tNo contributors yet. The query matched no series, which usually means no OTel" +
                "\n\tmetrics with these labels have arrived. Once your collector is sending data," +
                "\n\teach matching series appears here with its labels and why it breached.");
        }
        else
        {
            Console.WriteLine($"\tFound {contributors.Count} contributors:");
            foreach (var contributor in contributors)
            {
                var labels = string.Join(", ",
                    contributor.ContributorAttributes.Select(a => $"{a.Key}={a.Value}"));
                Console.WriteLine($"\t  {contributor.ContributorId}: {labels}");
                Console.WriteLine($"\t    reason: {contributor.StateReason}");
            }
        }

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Get statistics for an existing metric and chart it on a dashboard, so the reader can
    /// see what the alarm is evaluating.
    /// </summary>
    /// <param name="namespaces">The namespaces discovered in step 1.</param>
    private static async Task GetStatisticsAndChartMetric(List<string> namespaces)
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("6. Get statistics and chart the metric on a dashboard");
        Console.WriteLine("\nStatistics and dashboards are how you see what the alarm is evaluating.\n");

        if (!namespaces.Any())
        {
            Console.WriteLine("\tSkipping statistics and dashboard because no metrics exist yet.");
            Console.WriteLine(new string('-', 80));
            return;
        }

        var metricNamespace = namespaces.First();
        var metrics = await _cloudWatchWrapper.ListMetrics(metricNamespace);
        var metric = metrics.FirstOrDefault();

        if (metric != null)
        {
            var datapoints = await _cloudWatchWrapper.GetMetricStatistics(
                metricNamespace, metric.MetricName, new List<string> { "Average", "Maximum" },
                metric.Dimensions, 1, 3600);

            Console.WriteLine(
                $"\tStatistics for {metricNamespace} {metric.MetricName} over the last day:");
            Console.WriteLine($"\t  Datapoints: {datapoints.Count}");
            foreach (var datapoint in datapoints.Take(3))
            {
                Console.WriteLine(
                    $"\t  {datapoint.Timestamp:u} average {datapoint.Average}, maximum {datapoint.Maximum}");
            }

            var dashboardBody = BuildDashboardBody(metricNamespace, metric, _region);
            var validationMessages = await _cloudWatchWrapper.PutDashboard(_dashboardName, dashboardBody);
            _dashboardCreated = true;

            if (validationMessages.Any())
            {
                foreach (var message in validationMessages)
                {
                    Console.WriteLine($"\tDashboard validation message: {message.Message}");
                }
            }

            Console.WriteLine($"\tCreated dashboard {_dashboardName}.");

            var dashboard = await _cloudWatchWrapper.GetDashboard(_dashboardName);
            Console.WriteLine($"\tRead the dashboard back, {dashboard.Length} characters of widget JSON.");
        }
        else
        {
            Console.WriteLine($"\tNo metrics found in namespace {metricNamespace}, skipping.");
        }

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Build a single-widget dashboard body that charts the given metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric to chart.</param>
    /// <param name="metric">The metric to chart.</param>
    /// <param name="region">The region the metric is in. A metric widget must name its
    /// region, because a dashboard can chart metrics from several.</param>
    internal static string BuildDashboardBody(string metricNamespace, Metric metric, string region)
    {
        var dimensionParts = string.Concat(
            metric.Dimensions.Select(d => $", \"{d.Name}\", \"{d.Value}\""));

        return $@"{{
    ""widgets"": [
        {{
            ""type"": ""text"",
            ""x"": 0, ""y"": 0, ""width"": 24, ""height"": 2,
            ""properties"": {{
                ""markdown"": ""This dashboard was created programmatically by an AWS SDK code example.""
            }}
        }},
        {{
            ""type"": ""metric"",
            ""x"": 0, ""y"": 2, ""width"": 12, ""height"": 6,
            ""properties"": {{
                ""metrics"": [[ ""{metricNamespace}"", ""{metric.MetricName}""{dimensionParts} ]],
                ""view"": ""timeSeries"",
                ""stat"": ""Average"",
                ""period"": 300,
                ""region"": ""{region}"",
                ""title"": ""{metric.MetricName}""
            }}
        }}
    ]
}}";
    }

    /// <summary>
    /// Create a mute rule so the alarm's actions are suppressed during a maintenance
    /// window, then read it back and find it in the account's rules.
    /// </summary>
    private static async Task MuteAlarmForMaintenance()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("7. Mute the alarm for a maintenance window");
        Console.WriteLine(
            "\nWhile a mute rule is active the targeted alarms keep evaluating and keep changing" +
            "\nstate, but their actions do not fire. This is the supported way to suppress" +
            "\nnotifications during planned maintenance, instead of disabling alarm actions and" +
            "\nhoping someone remembers to turn them back on.\n");

        // The expression is a five-field cron expression,
        // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields,
        // not the six that Amazon EventBridge uses. For a one-time window, use
        // at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration from
        // PT1M to P15D, so PT2H rather than 2h.
        const string expression = "cron(0 2 * * SUN)";
        const string duration = "PT2H";
        const string timezone = "America/Los_Angeles";

        await _otelWrapper.PutAlarmMuteRule(_muteRuleName, expression, duration, timezone,
            new List<string> { _alarmName });

        Console.WriteLine($"\tCreated mute rule {_muteRuleName}:");
        Console.WriteLine($"\t  schedule: {expression} for {duration}");
        Console.WriteLine($"\t  timezone: {timezone}");
        Console.WriteLine($"\t  targets:  {_alarmName}");
        Console.WriteLine(
            "\n\tNote the two formats here. The expression is a five-field cron expression, five" +
            "\n\trather than the six Amazon EventBridge uses. The duration is an ISO 8601" +
            "\n\tduration, so 'PT2H' and not '2h'." +
            "\n" +
            "\n\tAlso note that MuteTargets is set explicitly. If you leave it out, the rule" +
            "\n\tapplies to every alarm in the account.");

        var muteRule = await _otelWrapper.GetAlarmMuteRule(_muteRuleName);
        Console.WriteLine(
            $"\tRead the rule back: status {muteRule.Status}, mute type {muteRule.MuteType}.");

        var summaries = await _otelWrapper.ListAlarmMuteRules(_alarmName);
        Console.WriteLine($"\tFound {summaries.Count} mute rules targeting this alarm.");

        // Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
        var match = summaries.FirstOrDefault(s =>
            s.AlarmMuteRuleArn.EndsWith($"/{_muteRuleName}") ||
            s.AlarmMuteRuleArn.EndsWith($":{_muteRuleName}"));

        if (match != null)
        {
            Console.WriteLine($"\t  matched by ARN: {match.AlarmMuteRuleArn} ({match.Status})");
        }

        Console.WriteLine(new string('-', 80));
    }

    /// <summary>
    /// Delete the resources the scenario created. Each deletion is attempted independently
    /// so that one failure does not leave the remaining resources behind.
    /// </summary>
    private static async Task CleanUp()
    {
        Console.WriteLine(new string('-', 80));
        Console.WriteLine("8. Clean up");
        Console.WriteLine("\nDelete the resources this scenario created? (y/n)");

        var response = Console.ReadLine();
        if (!string.Equals(response?.Trim(), "y", StringComparison.OrdinalIgnoreCase))
        {
            Console.WriteLine(
                "\tSkipping cleanup. Note that the alarm, dashboard, and mute rule are still in" +
                "\n\tyour account, and enrichment may still be running.");
            Console.WriteLine(new string('-', 80));
            return;
        }

        try
        {
            await _otelWrapper.DeleteAlarmMuteRule(_muteRuleName);
            Console.WriteLine($"\tDeleted mute rule {_muteRuleName}.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"\tCould not delete the mute rule: {ex.Message}");
        }

        try
        {
            await _cloudWatchWrapper.DeleteAlarms(new List<string> { _alarmName });
            Console.WriteLine($"\tDeleted alarm {_alarmName}.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"\tCould not delete the alarm: {ex.Message}");
        }

        if (_dashboardCreated)
        {
            try
            {
                await _cloudWatchWrapper.DeleteDashboards(new List<string> { _dashboardName });
                Console.WriteLine($"\tDeleted dashboard {_dashboardName}.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"\tCould not delete the dashboard: {ex.Message}");
            }
        }

        if (_startedEnrichment)
        {
            try
            {
                await _otelWrapper.StopOTelEnrichment();
                Console.WriteLine("\tStopped OTel enrichment, because this run started it.");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"\tCould not stop OTel enrichment: {ex.Message}");
            }
        }
        else
        {
            Console.WriteLine(
                "\tLeft OTel enrichment running, because it was already on before this run.");
        }

        Console.WriteLine(new string('-', 80));
    }
}
```
Wrapper methods used by the scenario for the CloudWatch OpenTelemetry actions.  

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
```
Wrapper methods used by the scenario for the metric, statistic, and dashboard actions.  

```
/// <summary>
/// Wrapper class for Amazon CloudWatch methods.
/// </summary>
public class CloudWatchWrapper
{
    private readonly IAmazonCloudWatch _amazonCloudWatch;
    private readonly ILogger<CloudWatchWrapper> _logger;

    /// <summary>
    /// Constructor for the CloudWatch wrapper.
    /// </summary>
    /// <param name="amazonCloudWatch">The injected CloudWatch client.</param>
    /// <param name="logger">The injected logger for the wrapper.</param>
    public CloudWatchWrapper(IAmazonCloudWatch amazonCloudWatch, ILogger<CloudWatchWrapper> logger)

    {
        _logger = logger;
        _amazonCloudWatch = amazonCloudWatch;
    }

    /// <summary>
    /// List metrics available, optionally within a namespace.
    /// </summary>
    /// <param name="metricNamespace">Optional CloudWatch namespace to use when listing metrics.</param>
    /// <param name="filter">Optional dimension filter.</param>
    /// <param name="metricName">Optional metric name filter.</param>
    /// <returns>The list of metrics.</returns>
    public async Task<List<Metric>> ListMetrics(string? metricNamespace = null, DimensionFilter? filter = null, string? metricName = null)
    {
        var results = new List<Metric>();
        var paginateMetrics = _amazonCloudWatch.Paginators.ListMetrics(
            new ListMetricsRequest
            {
                Namespace = metricNamespace,
                Dimensions = filter != null ? new List<DimensionFilter> { filter } : null,
                MetricName = metricName
            });
        // Get the entire list using the paginator.
        await foreach (var metric in paginateMetrics.Metrics)
        {
            results.Add(metric);
        }

        return results;
    }

    /// <summary>
    /// Wrapper to get statistics for a specific CloudWatch metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <param name="statistics">The list of statistics to include.</param>
    /// <param name="dimensions">The list of dimensions to include.</param>
    /// <param name="days">The number of days in the past to include.</param>
    /// <param name="period">The period for the data.</param>
    /// <returns>A list of DataPoint objects for the statistics.</returns>
    public async Task<List<Datapoint>> GetMetricStatistics(string metricNamespace,
        string metricName, List<string> statistics, List<Dimension> dimensions, int days, int period)
    {
        var metricStatistics = await _amazonCloudWatch.GetMetricStatisticsAsync(
            new GetMetricStatisticsRequest()
            {
                Namespace = metricNamespace,
                MetricName = metricName,
                Dimensions = dimensions,
                Statistics = statistics,
                StartTime = DateTime.UtcNow.AddDays(-days),
                EndTime = DateTime.UtcNow,
                Period = period
            });

        return metricStatistics.Datapoints ?? new List<Datapoint>();
    }

    /// <summary>
    /// Wrapper to create or add to a dashboard with metrics.
    /// </summary>
    /// <param name="dashboardName">The name for the dashboard.</param>
    /// <param name="dashboardBody">The metric data in JSON for the dashboard.</param>
    /// <returns>A list of validation messages for the dashboard.</returns>
    public async Task<List<DashboardValidationMessage>> PutDashboard(string dashboardName,
        string dashboardBody)
    {
        // Updating a dashboard replaces all contents.
        // Best practice is to include a text widget indicating this dashboard was created programmatically.
        var dashboardResponse = await _amazonCloudWatch.PutDashboardAsync(
            new PutDashboardRequest()
            {
                DashboardName = dashboardName,
                DashboardBody = dashboardBody
            });

        return dashboardResponse.DashboardValidationMessages ?? new List<DashboardValidationMessage>();
    }


    /// <summary>
    /// Get information on a dashboard.
    /// </summary>
    /// <param name="dashboardName">The name of the dashboard.</param>
    /// <returns>A JSON object with dashboard information.</returns>
    public async Task<string> GetDashboard(string dashboardName)
    {
        var dashboardResponse = await _amazonCloudWatch.GetDashboardAsync(
            new GetDashboardRequest()
            {
                DashboardName = dashboardName
            });

        return dashboardResponse.DashboardBody;
    }


    /// <summary>
    /// Get a list of dashboards.
    /// </summary>
    /// <returns>A list of DashboardEntry objects.</returns>
    public async Task<List<DashboardEntry>> ListDashboards()
    {
        var results = new List<DashboardEntry>();
        var paginateDashboards = _amazonCloudWatch.Paginators.ListDashboards(
            new ListDashboardsRequest());
        // Get the entire list using the paginator.
        await foreach (var data in paginateDashboards.DashboardEntries)
        {
            results.Add(data);
        }

        return results;
    }

    /// <summary>
    /// Wrapper to add metric data to a CloudWatch metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricData">A data object for the metric data.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutMetricData(string metricNamespace,
        List<MetricDatum> metricData)
    {
        var putDataResponse = await _amazonCloudWatch.PutMetricDataAsync(
            new PutMetricDataRequest()
            {
                MetricData = metricData,
                Namespace = metricNamespace,
            });

        return putDataResponse.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Get an image for a metric graphed over time.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metric">The name of the metric.</param>
    /// <param name="stat">The name of the stat to chart.</param>
    /// <param name="period">The period to use for the chart.</param>
    /// <returns>A memory stream for the chart image.</returns>
    public async Task<MemoryStream> GetTimeSeriesMetricImage(string metricNamespace, string metric, string stat, int period)
    {
        var metricImageWidget = new
        {
            title = "Example Metric Graph",
            view = "timeSeries",
            stacked = false,
            period = period,
            width = 1400,
            height = 600,
            metrics = new List<List<object>>
                { new() { metricNamespace, metric, new { stat } } }
        };

        var metricImageWidgetString = JsonSerializer.Serialize(metricImageWidget);
        var imageResponse = await _amazonCloudWatch.GetMetricWidgetImageAsync(
            new GetMetricWidgetImageRequest()
            {
                MetricWidget = metricImageWidgetString
            });

        return imageResponse.MetricWidgetImage;
    }

    /// <summary>
    /// Save a metric image to a file.
    /// </summary>
    /// <param name="memoryStream">The MemoryStream for the metric image.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <returns>The path to the file.</returns>
    public string SaveMetricImage(MemoryStream memoryStream, string metricName)
    {
        var metricFileName = $"{metricName}_{DateTime.Now.Ticks}.png";
        using var sr = new StreamReader(memoryStream);
        // Writes the memory stream to a file.
        File.WriteAllBytes(metricFileName, memoryStream.ToArray());
        var filePath = Path.Join(AppDomain.CurrentDomain.BaseDirectory,
            metricFileName);
        return filePath;
    }

    /// <summary>
    /// Get data for CloudWatch metrics.
    /// </summary>
    /// <param name="minutesOfData">The number of minutes of data to include.</param>
    /// <param name="useDescendingTime">True to return the data descending by time.</param>
    /// <param name="endDateUtc">The end date for the data, in UTC.</param>
    /// <param name="maxDataPoints">The maximum data points to include.</param>
    /// <param name="dataQueries">Optional data queries to include.</param>
    /// <returns>A list of the requested metric data.</returns>
    public async Task<List<MetricDataResult>> GetMetricData(int minutesOfData, bool useDescendingTime, DateTime? endDateUtc = null,
        int maxDataPoints = 0, List<MetricDataQuery>? dataQueries = null)
    {
        var metricData = new List<MetricDataResult>();
        // If no end time is provided, use the current time for the end time.
        endDateUtc ??= DateTime.UtcNow;
        var timeZoneOffset = TimeZoneInfo.Local.GetUtcOffset(endDateUtc.Value.ToLocalTime());
        var startTimeUtc = endDateUtc.Value.AddMinutes(-minutesOfData);
        // The timezone string should be in the format +0000, so use the timezone offset to format it correctly.
        var timeZoneString = $"{timeZoneOffset.Hours:D2}{timeZoneOffset.Minutes:D2}";
        // Add the plus sign for positive offsets.
        timeZoneString = timeZoneString.StartsWith('-') ? timeZoneString : "+" + timeZoneString;
        var paginatedMetricData = _amazonCloudWatch.Paginators.GetMetricData(
            new GetMetricDataRequest()
            {
                StartTime = startTimeUtc,
                EndTime = endDateUtc.Value,
                LabelOptions = new LabelOptions { Timezone = timeZoneString },
                ScanBy = useDescendingTime ? ScanBy.TimestampDescending : ScanBy.TimestampAscending,
                MaxDatapoints = maxDataPoints,
                MetricDataQueries = dataQueries,
            });

        if (paginatedMetricData.MetricDataResults != null)
        {
            await foreach (var data in paginatedMetricData.MetricDataResults)
            {
                metricData.Add(data);
            }
        }

        return metricData;
    }

    /// <summary>
    /// Add a metric alarm to send an email when the metric passes a threshold.
    /// </summary>
    /// <param name="alarmDescription">A description of the alarm.</param>
    /// <param name="alarmName">The name for the alarm.</param>
    /// <param name="comparison">The type of comparison to use.</param>
    /// <param name="metricName">The name of the metric for the alarm.</param>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="threshold">The threshold value for the alarm.</param>
    /// <param name="alarmActions">Optional actions to execute when in an alarm state.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutMetricEmailAlarm(string alarmDescription, string alarmName, ComparisonOperator comparison,
        string metricName, string metricNamespace, double threshold, List<string> alarmActions = null!)
    {
        try
        {
            var putEmailAlarmResponse = await _amazonCloudWatch.PutMetricAlarmAsync(
                new PutMetricAlarmRequest()
                {
                    AlarmActions = alarmActions,
                    AlarmDescription = alarmDescription,
                    AlarmName = alarmName,
                    ComparisonOperator = comparison,
                    Threshold = threshold,
                    Namespace = metricNamespace,
                    MetricName = metricName,
                    EvaluationPeriods = 1,
                    Period = 10,
                    Statistic = new Statistic("Maximum"),
                    DatapointsToAlarm = 1,
                    TreatMissingData = "ignore"
                });
            return putEmailAlarmResponse.HttpStatusCode == HttpStatusCode.OK;
        }
        catch (LimitExceededException lex)
        {
            _logger.LogError(lex, $"Unable to add alarm {alarmName}. Alarm quota has already been reached.");
        }

        return false;
    }

    /// <summary>
    /// Add specific email actions to a list of action strings for a CloudWatch alarm.
    /// </summary>
    /// <param name="accountId">The AccountId for the alarm.</param>
    /// <param name="region">The region for the alarm.</param>
    /// <param name="emailTopicName">An Amazon Simple Notification Service (SNS) topic for the alarm email.</param>
    /// <param name="alarmActions">Optional list of existing alarm actions to append to.</param>
    /// <returns>A list of string actions for an alarm.</returns>
    public List<string> AddEmailAlarmAction(string accountId, string region,
        string emailTopicName, List<string>? alarmActions = null)
    {
        alarmActions ??= new List<string>();
        var snsAlarmAction = $"arn:aws:sns:{region}:{accountId}:{emailTopicName}";
        alarmActions.Add(snsAlarmAction);
        return alarmActions;
    }

    /// <summary>
    /// Describe the current alarms, optionally filtered by state.
    /// </summary>
    /// <param name="stateValue">Optional filter for alarm state.</param>
    /// <returns>The list of alarm data.</returns>
    public async Task<List<MetricAlarm>> DescribeAlarms(StateValue? stateValue = null)
    {
        List<MetricAlarm> alarms = new List<MetricAlarm>();
        var paginatedDescribeAlarms = _amazonCloudWatch.Paginators.DescribeAlarms(
            new DescribeAlarmsRequest()
            {
                StateValue = stateValue
            });

        await foreach (var data in paginatedDescribeAlarms.MetricAlarms)
        {
            alarms.Add(data);
        }
        return alarms;
    }

    /// <summary>
    /// Describe the current alarms for a specific metric.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The name of the metric.</param>
    /// <returns>The list of alarm data.</returns>
    public async Task<List<MetricAlarm>> DescribeAlarmsForMetric(string metricNamespace, string metricName)
    {
        var alarmsResult = await _amazonCloudWatch.DescribeAlarmsForMetricAsync(
            new DescribeAlarmsForMetricRequest()
            {
                Namespace = metricNamespace,
                MetricName = metricName
            });

        return alarmsResult.MetricAlarms ?? new List<MetricAlarm>();
    }

    /// <summary>
    /// Describe the history of an alarm for a number of days in the past.
    /// </summary>
    /// <param name="alarmName">The name of the alarm.</param>
    /// <param name="historyDays">The number of days in the past.</param>
    /// <returns>The list of alarm history data.</returns>
    public async Task<List<AlarmHistoryItem>> DescribeAlarmHistory(string alarmName, int historyDays)
    {
        List<AlarmHistoryItem> alarmHistory = new List<AlarmHistoryItem>();
        var paginatedAlarmHistory = _amazonCloudWatch.Paginators.DescribeAlarmHistory(
            new DescribeAlarmHistoryRequest()
            {
                AlarmName = alarmName,
                EndDate = DateTime.UtcNow,
                HistoryItemType = HistoryItemType.StateUpdate,
                StartDate = DateTime.UtcNow.AddDays(-historyDays)
            });

        await foreach (var data in paginatedAlarmHistory.AlarmHistoryItems)
        {
            alarmHistory.Add(data);
        }
        return alarmHistory;
    }

    /// <summary>
    /// Delete a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAlarms(List<string> alarmNames)
    {
        var deleteAlarmsResult = await _amazonCloudWatch.DeleteAlarmsAsync(
            new DeleteAlarmsRequest()
            {
                AlarmNames = alarmNames
            });

        return deleteAlarmsResult.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Disable the actions for a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DisableAlarmActions(List<string> alarmNames)
    {
        var disableAlarmActionsResult = await _amazonCloudWatch.DisableAlarmActionsAsync(
            new DisableAlarmActionsRequest()
            {
                AlarmNames = alarmNames
            });

        return disableAlarmActionsResult.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Enable the actions for a list of alarms from CloudWatch.
    /// </summary>
    /// <param name="alarmNames">A list of names of alarms.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> EnableAlarmActions(List<string> alarmNames)
    {
        var enableAlarmActionsResult = await _amazonCloudWatch.EnableAlarmActionsAsync(
            new EnableAlarmActionsRequest()
            {
                AlarmNames = alarmNames
            });

        return enableAlarmActionsResult.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Add an anomaly detector for a single metric.
    /// </summary>
    /// <param name="anomalyDetector">A single metric anomaly detector.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> PutAnomalyDetector(SingleMetricAnomalyDetector anomalyDetector)
    {
        var putAlarmDetectorResult = await _amazonCloudWatch.PutAnomalyDetectorAsync(
            new PutAnomalyDetectorRequest()
            {
                SingleMetricAnomalyDetector = anomalyDetector
            });

        return putAlarmDetectorResult.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Describe anomaly detectors for a metric and namespace.
    /// </summary>
    /// <param name="metricNamespace">The namespace of the metric.</param>
    /// <param name="metricName">The metric of the anomaly detectors.</param>
    /// <returns>The list of detectors.</returns>
    public async Task<List<AnomalyDetector>> DescribeAnomalyDetectors(string metricNamespace, string metricName)
    {
        List<AnomalyDetector> detectors = new List<AnomalyDetector>();
        var paginatedDescribeAnomalyDetectors = _amazonCloudWatch.Paginators.DescribeAnomalyDetectors(
            new DescribeAnomalyDetectorsRequest()
            {
                MetricName = metricName,
                Namespace = metricNamespace
            });

        await foreach (var data in paginatedDescribeAnomalyDetectors.AnomalyDetectors)
        {
            detectors.Add(data);
        }

        return detectors;
    }

    /// <summary>
    /// Delete a single metric anomaly detector.
    /// </summary>
    /// <param name="anomalyDetector">The anomaly detector to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteAnomalyDetector(SingleMetricAnomalyDetector anomalyDetector)
    {
        var deleteAnomalyDetectorResponse = await _amazonCloudWatch.DeleteAnomalyDetectorAsync(
            new DeleteAnomalyDetectorRequest()
            {
                SingleMetricAnomalyDetector = anomalyDetector
            });

        return deleteAnomalyDetectorResponse.HttpStatusCode == HttpStatusCode.OK;
    }

    /// <summary>
    /// Delete a list of CloudWatch dashboards.
    /// </summary>
    /// <param name="dashboardNames">List of dashboard names to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteDashboards(List<string> dashboardNames)
    {
        var deleteDashboardsResponse = await _amazonCloudWatch.DeleteDashboardsAsync(
            new DeleteDashboardsRequest()
            {
                DashboardNames = dashboardNames
            });

        return deleteDashboardsResponse.HttpStatusCode == HttpStatusCode.OK;
    }
}
```
Example settings.json values for the scenario.  

```
{
  "dashboardName": "example-new-dashboard",
  "exampleAlarmName": "example-metric-alarm",
  "accountId": "1234567890",
  "region": "us-east-1",
  "emailTopic": "Default_CloudWatch_Alarms_Topic",
  "customMetricNamespace": "example-namespace",
  "customMetricName": "example-custom-metric",
  "dashboardExampleBody": {
    "widgets": [
      {
        "height": 6,
        "width": 6,
        "y": 0,
        "x": 0,
        "type": "text",
        "properties": {
          "markdown": "# Code Example Dashboard \nThis dashboard was created by example code.\n"
        }
      },
      {
        "height": 8,
        "width": 8,
        "y": 0,
        "x": 6,
        "type": "metric",
        "properties": {
          "metrics": [
            [
              "AWS/Billing",
              "EstimatedCharges",
              "Currency",
              "USD",
              { "region": "us-east-1" }
            ]
          ],
          "view": "timeSeries",
          "region": "us-east-1",
          "stat": "Maximum",
          "period": 86400,
          "yAxis": {
            "left": {
              "min": 0,
              "max": 100
            }
          },
          "stacked": false,
          "title": "Estimated Billing",
          "setPeriodToTimeRange": false,
          "liveData": true,
          "sparkline": true,
          "trend": true
        }
      },
      {
        "height": 8,
        "width": 8,
        "y": 0,
        "x": 14,
        "type": "metric",
        "properties": {
          "metrics": [
            [ "AWS/Usage", "CallCount", "Type", "API", "Resource", "ListMetrics", "Service", "CloudWatch", "Class", "None" ],
            [ "...", "GetMetricStatistics", ".", ".", ".", "." ],
            [ "...", "GetMetricData", ".", ".", ".", "." ],
            [ "...", "PutDashboard", ".", ".", ".", "." ],
            [ "...", "PutMetricData", ".", ".", ".", "." ]
          ],
          "view": "timeSeries",
          "yAxis": {
            "left": {
              "min": 0,
              "max": 200
            }
          },
          "stacked": false,
          "region": "us-east-1",
          "stat": "Sum",
          "period": 300,
          "title": "CloudWatch Usage",
          "setPeriodToTimeRange": false,
          "liveData": true,
          "sparkline": true,
          "trend": true
        }
      }
    ]
  }
}
```
+ For API details, see the following topics in *AWS SDK for .NET API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteAlarms)
  + [DeleteDashboards](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DeleteDashboards)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetDashboard](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetDashboard)
  + [GetMetricStatistics](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetMetricStatistics)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListAlarmMuteRules)
  + [ListDashboards](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListDashboards)
  + [ListMetrics](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/ListMetrics)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutDashboard](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutDashboard)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StopOTelEnrichment)

------
#### [ C\+\+ ]

**SDK for C\+\+**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cloudwatch#code-examples). 
Run an interactive scenario at a command prompt.  

```
#include <aws/core/Aws.h>
#include <aws/core/utils/json/JsonSerializer.h>
#include <aws/monitoring/CloudWatchClient.h>
#include <aws/monitoring/model/AlarmPromQLCriteria.h>
#include <aws/monitoring/model/DeleteAlarmMuteRuleRequest.h>
#include <aws/monitoring/model/DeleteAlarmsRequest.h>
#include <aws/monitoring/model/DeleteDashboardsRequest.h>
#include <aws/monitoring/model/DescribeAlarmContributorsRequest.h>
#include <aws/monitoring/model/EvaluationCriteria.h>
#include <aws/monitoring/model/GetAlarmMuteRuleRequest.h>
#include <aws/monitoring/model/GetDashboardRequest.h>
#include <aws/monitoring/model/GetMetricStatisticsRequest.h>
#include <aws/monitoring/model/GetOTelEnrichmentRequest.h>
#include <aws/monitoring/model/ListAlarmMuteRulesRequest.h>
#include <aws/monitoring/model/ListMetricsRequest.h>
#include <aws/monitoring/model/MuteTargets.h>
#include <aws/monitoring/model/PutAlarmMuteRuleRequest.h>
#include <aws/monitoring/model/PutDashboardRequest.h>
#include <aws/monitoring/model/PutMetricAlarmRequest.h>
#include <aws/monitoring/model/Rule.h>
#include <aws/monitoring/model/Schedule.h>
#include <aws/monitoring/model/StartOTelEnrichmentRequest.h>
#include <aws/monitoring/model/StopOTelEnrichmentRequest.h>
#include <chrono>
#include <iostream>
#include <map>
#include <random>

namespace {
    const Aws::String DASHES(80, '-');
    const char DEFAULT_QUERY[] = "avg by (host) (system_cpu_utilization) > 80";

    // Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600
    // seconds.
    const int EVALUATION_INTERVAL = 60;
    const int PENDING_PERIOD = 300;
    const int RECOVERY_PERIOD = 120;

    //! Wait for the reader before moving to the next step.
    void pressEnter() {
        std::cout << "Press Enter to continue..." << std::endl;
        std::cin.get();
    }

    //! List the account's metrics and report how they are spread across namespaces.
    /*!
      \param client: A CloudWatch client.
      \param metric: Receives the first metric found, for later steps to chart.
      \return bool: Function succeeded.
     */
    bool listMetricsAndNamespaces(const Aws::CloudWatch::CloudWatchClient &client,
                                  Aws::CloudWatch::Model::Metric &metric) {
        std::cout << "1. List metrics and namespaces" << std::endl << std::endl;
        std::cout << "Before configuring anything, let's see what CloudWatch is already"
                  << std::endl
                  << "collecting in this account." << std::endl << std::endl;

        std::map<Aws::String, int> counts;
        int metricCount = 0;
        bool haveMetric = false;

        Aws::CloudWatch::Model::ListMetricsRequest request;
        bool done = false;
        while (!done) {
            auto outcome = client.ListMetrics(request);
            if (!outcome.IsSuccess()) {
                std::cerr << "Failed to list metrics: " << outcome.GetError().GetMessage()
                          << std::endl;
                return false;
            }

            for (const auto &found : outcome.GetResult().GetMetrics()) {
                ++counts[found.GetNamespace()];
                ++metricCount;
                if (!haveMetric) {
                    metric = found;
                    haveMetric = true;
                }
            }

            const auto &nextToken = outcome.GetResult().GetNextToken();
            request.SetNextToken(nextToken);
            // This account may have a very large number of metrics, so stop once there
            // are enough to give the reader a sense of what is there.
            done = nextToken.empty() || metricCount >= 500;
        }

        std::cout << "Found " << metricCount << " metrics across " << counts.size()
                  << " namespaces:" << std::endl;
        for (const auto &entry : counts) {
            std::cout << "  " << entry.first << " (" << entry.second << " metrics)"
                      << std::endl;
        }
        if (!haveMetric) {
            std::cout << "No metrics found in this account. The statistics and dashboard"
                      << std::endl
                      << "steps later on need an existing metric, so they will be "
                         "skipped."
                      << std::endl;
        }

        return true;
    }

    //! Start OTel enrichment, but only if it is not already running.
    /*!
      \param client: A CloudWatch client.
      \param startedEnrichment: Set to true if this run started enrichment, so that
             cleanup only stops what this run turned on.
      \return bool: Function succeeded.
     */
    bool startOTelEnrichment(const Aws::CloudWatch::CloudWatchClient &client,
                             bool &startedEnrichment) {
        std::cout << "2. Start OpenTelemetry enrichment" << std::endl << std::endl;
        std::cout << "Enrichment is what lets CloudWatch attach AWS resource context to"
                  << std::endl
                  << "the OTLP metrics you send it. Without it, your metrics arrive as"
                  << std::endl
                  << "opaque series with no connection to the resources that emitted "
                     "them."
                  << std::endl << std::endl;

        Aws::CloudWatch::Model::GetOTelEnrichmentRequest getRequest;
        auto getOutcome = client.GetOTelEnrichment(getRequest);
        if (!getOutcome.IsSuccess()) {
            std::cerr << "Failed to get OTel enrichment status: "
                      << getOutcome.GetError().GetMessage() << std::endl;
            return false;
        }

        auto status = getOutcome.GetResult().GetStatus();
        std::cout << "Enrichment status: "
                  << Aws::CloudWatch::Model::OTelEnrichmentStatusMapper::
                         GetNameForOTelEnrichmentStatus(status)
                  << std::endl;

        if (status == Aws::CloudWatch::Model::OTelEnrichmentStatus::Running) {
            std::cout << std::endl
                      << "Enrichment was already running, so it will be left alone. The"
                      << std::endl
                      << "cleanup step will not stop it, because other workloads in this"
                      << std::endl
                      << "account may depend on it." << std::endl;
            return true;
        }

        Aws::CloudWatch::Model::StartOTelEnrichmentRequest startRequest;
        auto startOutcome = client.StartOTelEnrichment(startRequest);
        if (!startOutcome.IsSuccess()) {
            std::cerr << "Failed to start OTel enrichment: "
                      << startOutcome.GetError().GetMessage() << std::endl;
            return false;
        }
        startedEnrichment = true;

        auto afterOutcome = client.GetOTelEnrichment(getRequest);
        if (afterOutcome.IsSuccess()) {
            std::cout << "Enrichment status: "
                      << Aws::CloudWatch::Model::OTelEnrichmentStatusMapper::
                             GetNameForOTelEnrichmentStatus(
                                 afterOutcome.GetResult().GetStatus())
                      << std::endl;
        }
        std::cout << std::endl
                  << "Note: this run started enrichment, so the cleanup step will stop it"
                  << std::endl
                  << "again." << std::endl;

        return true;
    }

    //! Explain how OTLP metrics reach CloudWatch. There is no SDK call for this step.
    void explainOtlpIngestion() {
        std::cout << "3. Send OTLP metrics to CloudWatch" << std::endl << std::endl;
        std::cout << "This step is not an AWS SDK operation, and that is worth being"
                  << std::endl
                  << "explicit about. Metrics reach CloudWatch over the OTLP protocol,"
                  << std::endl
                  << "through the CloudWatch agent, an OpenTelemetry Collector, or an "
                     "ADOT"
                  << std::endl
                  << "SDK. There is no PutOTelMetrics API to call." << std::endl
                  << std::endl;
        std::cout << "Point your collector at the CloudWatch metrics endpoint, which"
                  << std::endl
                  << "follows the pattern" << std::endl
                  << "  https://monitoring.<region>.amazonaws.com/v1/metrics" << std::endl
                  << std::endl;
        std::cout << "The endpoint is HTTP/1.1 only and does not support gRPC, so use an"
                  << std::endl
                  << "otlphttp exporter rather than otlp. The metrics endpoint signs as"
                  << std::endl
                  << "\"monitoring\"." << std::endl;
    }

    //! Create an alarm that evaluates a PromQL query.
    /*!
      \param client: A CloudWatch client.
      \param alarmName: The name of the alarm to create.
      \param query: The PromQL query to evaluate.
      \return bool: Function succeeded.
     */
    bool createPromQLAlarm(const Aws::CloudWatch::CloudWatchClient &client,
                           const Aws::String &alarmName, const Aws::String &query) {
        std::cout << "4. Create a PromQL alarm" << std::endl << std::endl;
        std::cout << "The comparison goes inside the query itself: a PromQL alarm has no"
                  << std::endl
                  << "separate threshold, comparison operator, statistic, or period."
                  << std::endl << std::endl;

        Aws::CloudWatch::Model::AlarmPromQLCriteria promQLCriteria;
        promQLCriteria.SetQuery(query);
        promQLCriteria.SetPendingPeriod(PENDING_PERIOD);
        promQLCriteria.SetRecoveryPeriod(RECOVERY_PERIOD);

        Aws::CloudWatch::Model::EvaluationCriteria evaluationCriteria;
        evaluationCriteria.SetPromQLCriteria(promQLCriteria);

        // EvaluationCriteria is mutually exclusive with the classic MetricName and
        // Metrics fields. When you use it you must also set EvaluationInterval, and you
        // must not set Period, Statistic, Threshold, ComparisonOperator,
        // EvaluationPeriods, DatapointsToAlarm, or TreatMissingData.
        Aws::CloudWatch::Model::PutMetricAlarmRequest request;
        request.SetAlarmName(alarmName);
        request.SetAlarmDescription(
            "A PromQL alarm created by the AWS SDK for C++ Basics scenario.");
        request.SetEvaluationCriteria(evaluationCriteria);
        request.SetEvaluationInterval(EVALUATION_INTERVAL);
        request.SetActionsEnabled(false);

        auto outcome = client.PutMetricAlarm(request);
        if (!outcome.IsSuccess()) {
            std::cerr << "Failed to create PromQL alarm: "
                      << outcome.GetError().GetMessage() << std::endl;
            return false;
        }

        std::cout << "Created alarm " << alarmName << ":" << std::endl;
        std::cout << "  query:              " << query << std::endl;
        std::cout << "  evaluationInterval: " << EVALUATION_INTERVAL << " seconds"
                  << std::endl;
        std::cout << "  pendingPeriod:      " << PENDING_PERIOD << " seconds" << std::endl;
        std::cout << "  recoveryPeriod:     " << RECOVERY_PERIOD << " seconds"
                  << std::endl << std::endl;
        std::cout << "A PromQL alarm starts in the OK state rather than "
                     "INSUFFICIENT_DATA,"
                  << std::endl
                  << "which is another way it differs from a classic alarm." << std::endl;

        return true;
    }

    //! Report the alarm's contributors, one per series the query matched.
    /*!
      \param client: A CloudWatch client.
      \param alarmName: The name of the alarm.
      \return bool: Function succeeded.
     */
    bool inspectAlarmContributors(const Aws::CloudWatch::CloudWatchClient &client,
                                 const Aws::String &alarmName) {
        std::cout << "5. Inspect the alarm's contributors" << std::endl << std::endl;
        std::cout << "Each contributor is one series the query matched, identified by its"
                  << std::endl
                  << "label set. This is how you find out which host is unhealthy rather"
                  << std::endl
                  << "than only that something is. Classic alarms have no equivalent."
                  << std::endl << std::endl;

        Aws::Vector<Aws::CloudWatch::Model::AlarmContributor> contributors;
        Aws::CloudWatch::Model::DescribeAlarmContributorsRequest request;
        request.SetAlarmName(alarmName);

        bool done = false;
        while (!done) {
            auto outcome = client.DescribeAlarmContributors(request);
            if (!outcome.IsSuccess()) {
                std::cerr << "Failed to describe alarm contributors: "
                          << outcome.GetError().GetMessage() << std::endl;
                return false;
            }

            const auto &page = outcome.GetResult().GetAlarmContributors();
            contributors.insert(contributors.end(), page.begin(), page.end());

            const auto &nextToken = outcome.GetResult().GetNextToken();
            request.SetNextToken(nextToken);
            // A page can come back empty while still carrying a token, so keep going
            // until the token itself is gone rather than stopping at the first empty
            // page.
            done = nextToken.empty();
        }

        if (contributors.empty()) {
            std::cout << "No contributors yet. The query matched no series, which usually"
                      << std::endl
                      << "means no OTel metrics with these labels have arrived. Once your"
                      << std::endl
                      << "collector is sending data, each matching series appears here"
                      << std::endl
                      << "with its labels and the reason it breached." << std::endl;
            return true;
        }

        std::cout << "Found " << contributors.size() << " contributors:" << std::endl;
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
            std::cout << "    reason: " << contributor.GetStateReason() << std::endl;
        }

        return true;
    }

    //! Build a single-widget dashboard body that charts the given metric.
    /*!
      \param metric: The metric to chart.
      \param region: The region the metric is in. A metric widget must name its
       region, because a dashboard can chart metrics from several.
      \return Aws::String: The dashboard body, as JSON.
     */
    Aws::String buildDashboardBody(const Aws::CloudWatch::Model::Metric &metric,
                                   const Aws::String &region) {
        const auto &dimensions = metric.GetDimensions();

        // A metric is specified in a widget as a flat array,
        // [namespace, metricName, dimensionName, dimensionValue, ...].
        Aws::Utils::Array<Aws::Utils::Json::JsonValue> metricSpec(
            2 + 2 * dimensions.size());
        metricSpec[0].AsString(metric.GetNamespace());
        metricSpec[1].AsString(metric.GetMetricName());
        size_t index = 2;
        for (const auto &dimension : dimensions) {
            metricSpec[index++].AsString(dimension.GetName());
            metricSpec[index++].AsString(dimension.GetValue());
        }

        Aws::Utils::Array<Aws::Utils::Json::JsonValue> metricsArray(1);
        metricsArray[0].AsArray(metricSpec);

        Aws::Utils::Json::JsonValue textProperties;
        textProperties.WithString(
            "markdown",
            "This dashboard was created programmatically by an AWS SDK code example.");

        Aws::Utils::Json::JsonValue textWidget;
        textWidget.WithString("type", "text")
            .WithInteger("x", 0)
            .WithInteger("y", 0)
            .WithInteger("width", 24)
            .WithInteger("height", 2)
            .WithObject("properties", textProperties);

        Aws::Utils::Json::JsonValue metricProperties;
        metricProperties.WithArray("metrics", metricsArray)
            .WithString("view", "timeSeries")
            .WithString("stat", "Average")
            .WithInteger("period", 300)
            .WithString("region", region)
            .WithString("title", metric.GetMetricName());

        Aws::Utils::Json::JsonValue metricWidget;
        metricWidget.WithString("type", "metric")
            .WithInteger("x", 0)
            .WithInteger("y", 2)
            .WithInteger("width", 12)
            .WithInteger("height", 6)
            .WithObject("properties", metricProperties);

        Aws::Utils::Array<Aws::Utils::Json::JsonValue> widgets(2);
        widgets[0] = textWidget;
        widgets[1] = metricWidget;

        Aws::Utils::Json::JsonValue body;
        body.WithArray("widgets", widgets);

        return body.View().WriteCompact();
    }

    //! Get statistics for a metric and chart it on a dashboard.
    /*!
      \param client: A CloudWatch client.
      \param metric: The metric to chart. If its name is empty, this step is skipped.
      \param dashboardName: The name of the dashboard to create.
      \param dashboardCreated: Set to true if a dashboard was created, so that cleanup
             only deletes a dashboard that exists.
      \return bool: Function succeeded.
     */
    bool getStatisticsAndChartMetric(const Aws::CloudWatch::CloudWatchClient &client,
                                     const Aws::CloudWatch::Model::Metric &metric,
                                     const Aws::String &dashboardName,
                                     const Aws::String &region,
                                     bool &dashboardCreated) {
        std::cout << "6. Get statistics and chart the metric on a dashboard" << std::endl
                  << std::endl;
        std::cout << "Statistics and dashboards are how you see what the alarm is"
                  << std::endl << "evaluating." << std::endl << std::endl;

        if (metric.GetMetricName().empty()) {
            std::cout << "Skipping statistics and dashboard because no metrics exist yet."
                      << std::endl;
            return true;
        }

        const auto now = std::chrono::system_clock::now();
        Aws::CloudWatch::Model::GetMetricStatisticsRequest statsRequest;
        statsRequest.SetNamespace(metric.GetNamespace());
        statsRequest.SetMetricName(metric.GetMetricName());
        statsRequest.SetDimensions(metric.GetDimensions());
        statsRequest.SetStartTime(Aws::Utils::DateTime(now - std::chrono::hours(24)));
        statsRequest.SetEndTime(Aws::Utils::DateTime(now));
        statsRequest.SetPeriod(3600);
        statsRequest.AddStatistics(Aws::CloudWatch::Model::Statistic::Average);
        statsRequest.AddStatistics(Aws::CloudWatch::Model::Statistic::Maximum);

        auto statsOutcome = client.GetMetricStatistics(statsRequest);
        if (!statsOutcome.IsSuccess()) {
            std::cerr << "Failed to get metric statistics: "
                      << statsOutcome.GetError().GetMessage() << std::endl;
            return false;
        }

        const auto &datapoints = statsOutcome.GetResult().GetDatapoints();
        std::cout << "Statistics for " << metric.GetNamespace() << " "
                  << metric.GetMetricName() << " over the last day:" << std::endl;
        std::cout << "  Datapoints: " << datapoints.size() << std::endl;
        size_t shown = 0;
        for (const auto &datapoint : datapoints) {
            if (shown++ >= 3) {
                break;
            }
            std::cout << "  " << datapoint.GetTimestamp().ToGmtString(
                                     Aws::Utils::DateFormat::ISO_8601)
                      << " average " << datapoint.GetAverage() << ", maximum "
                      << datapoint.GetMaximum() << std::endl;
        }

        Aws::CloudWatch::Model::PutDashboardRequest putRequest;
        putRequest.SetDashboardName(dashboardName);
        putRequest.SetDashboardBody(buildDashboardBody(metric, region));

        auto putOutcome = client.PutDashboard(putRequest);
        if (!putOutcome.IsSuccess()) {
            std::cerr << "Failed to put dashboard: " << putOutcome.GetError().GetMessage()
                      << std::endl;
            return false;
        }
        dashboardCreated = true;

        for (const auto &message :
             putOutcome.GetResult().GetDashboardValidationMessages()) {
            std::cout << "Dashboard validation message: " << message.GetMessage()
                      << std::endl;
        }
        std::cout << "Created dashboard " << dashboardName << "." << std::endl;

        Aws::CloudWatch::Model::GetDashboardRequest getRequest;
        getRequest.SetDashboardName(dashboardName);
        auto getOutcome = client.GetDashboard(getRequest);
        if (getOutcome.IsSuccess()) {
            std::cout << "Read the dashboard back, "
                      << getOutcome.GetResult().GetDashboardBody().size()
                      << " characters of widget JSON." << std::endl;
        }

        return true;
    }

    //! Mute the alarm for a recurring maintenance window.
    /*!
      \param client: A CloudWatch client.
      \param muteRuleName: The name of the mute rule to create.
      \param alarmName: The alarm to target.
      \return bool: Function succeeded.
     */
    bool muteAlarmForMaintenance(const Aws::CloudWatch::CloudWatchClient &client,
                                 const Aws::String &muteRuleName,
                                 const Aws::String &alarmName) {
        std::cout << "7. Mute the alarm for a maintenance window" << std::endl
                  << std::endl;
        std::cout << "While a mute rule is active the targeted alarms keep evaluating and"
                  << std::endl
                  << "keep changing state, but their actions do not fire. This is the"
                  << std::endl
                  << "supported way to suppress notifications during planned maintenance,"
                  << std::endl
                  << "instead of disabling alarm actions and hoping someone remembers to"
                  << std::endl
                  << "turn them back on." << std::endl << std::endl;

        // The expression is a five-field cron expression,
        // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five
        // fields, not the six that Amazon EventBridge uses. For a one-time window, use
        // at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration
        // from PT1M to P15D, so PT2H rather than 2h.
        const Aws::String expression("cron(0 2 * * SUN)");
        const Aws::String duration("PT2H");
        const Aws::String timezone("America/Los_Angeles");

        Aws::CloudWatch::Model::Schedule schedule;
        schedule.SetExpression(expression);
        schedule.SetDuration(duration);
        schedule.SetTimezone(timezone);

        Aws::CloudWatch::Model::Rule rule;
        rule.SetSchedule(schedule);

        // Target up to 100 alarms. If MuteTargets is not set, the rule applies to every
        // alarm in the account.
        Aws::CloudWatch::Model::MuteTargets muteTargets;
        muteTargets.AddAlarmNames(alarmName);

        Aws::CloudWatch::Model::PutAlarmMuteRuleRequest putRequest;
        putRequest.SetName(muteRuleName);
        putRequest.SetDescription(
            "A mute rule created by the AWS SDK for C++ Basics scenario.");
        putRequest.SetRule(rule);
        putRequest.SetMuteTargets(muteTargets);

        auto putOutcome = client.PutAlarmMuteRule(putRequest);
        if (!putOutcome.IsSuccess()) {
            std::cerr << "Failed to put alarm mute rule: "
                      << putOutcome.GetError().GetMessage() << std::endl;
            return false;
        }

        std::cout << "Created mute rule " << muteRuleName << ":" << std::endl;
        std::cout << "  schedule: " << expression << " for " << duration << std::endl;
        std::cout << "  timezone: " << timezone << std::endl;
        std::cout << "  targets:  " << alarmName << std::endl << std::endl;
        std::cout << "Note the two formats here. The expression is a five-field cron"
                  << std::endl
                  << "expression, five rather than the six Amazon EventBridge uses. The"
                  << std::endl
                  << "duration is an ISO 8601 duration, so \"PT2H\" and not \"2h\"."
                  << std::endl << std::endl;
        std::cout << "Also note that MuteTargets is set explicitly. If you leave it out,"
                  << std::endl
                  << "the rule applies to every alarm in the account." << std::endl;

        Aws::CloudWatch::Model::GetAlarmMuteRuleRequest getRequest;
        getRequest.SetAlarmMuteRuleName(muteRuleName);
        auto getOutcome = client.GetAlarmMuteRule(getRequest);
        if (getOutcome.IsSuccess()) {
            const auto &result = getOutcome.GetResult();
            std::cout << "Read the rule back: status "
                      << Aws::CloudWatch::Model::AlarmMuteRuleStatusMapper::
                             GetNameForAlarmMuteRuleStatus(result.GetStatus())
                      << ", mute type " << result.GetMuteType() << "." << std::endl;
        }

        Aws::Vector<Aws::CloudWatch::Model::AlarmMuteRuleSummary> summaries;
        Aws::CloudWatch::Model::ListAlarmMuteRulesRequest listRequest;
        listRequest.SetAlarmName(alarmName);
        bool done = false;
        while (!done) {
            auto listOutcome = client.ListAlarmMuteRules(listRequest);
            if (!listOutcome.IsSuccess()) {
                std::cerr << "Failed to list alarm mute rules: "
                          << listOutcome.GetError().GetMessage() << std::endl;
                return false;
            }

            const auto &page = listOutcome.GetResult().GetAlarmMuteRuleSummaries();
            summaries.insert(summaries.end(), page.begin(), page.end());

            const auto &nextToken = listOutcome.GetResult().GetNextToken();
            listRequest.SetNextToken(nextToken);
            done = nextToken.empty();
        }

        std::cout << "Found " << summaries.size()
                  << " mute rules targeting this alarm." << std::endl;
        // Mute rule summaries carry no name field, only an ARN, so match on the ARN
        // suffix.
        for (const auto &summary : summaries) {
            const auto &arn = summary.GetAlarmMuteRuleArn();
            const Aws::String slashSuffix = "/" + muteRuleName;
            const Aws::String colonSuffix = ":" + muteRuleName;
            if ((arn.size() >= slashSuffix.size() &&
                 arn.compare(arn.size() - slashSuffix.size(), slashSuffix.size(),
                             slashSuffix) == 0) ||
                (arn.size() >= colonSuffix.size() &&
                 arn.compare(arn.size() - colonSuffix.size(), colonSuffix.size(),
                             colonSuffix) == 0)) {
                std::cout << "  matched by ARN: " << arn << " ("
                          << Aws::CloudWatch::Model::AlarmMuteRuleStatusMapper::
                                 GetNameForAlarmMuteRuleStatus(summary.GetStatus())
                          << ")" << std::endl;
            }
        }

        return true;
    }

    //! Delete everything the scenario created.
    /*!
      \param client: A CloudWatch client.
      \param alarmName: The alarm to delete.
      \param dashboardName: The dashboard to delete.
      \param muteRuleName: The mute rule to delete.
      \param dashboardCreated: Whether a dashboard was created.
      \param startedEnrichment: Whether this run started OTel enrichment.
      \return bool: Every deletion succeeded.
     */
    bool cleanUp(const Aws::CloudWatch::CloudWatchClient &client,
                 const Aws::String &alarmName, const Aws::String &dashboardName,
                 const Aws::String &muteRuleName, bool dashboardCreated,
                 bool startedEnrichment) {
        std::cout << "8. Clean up" << std::endl << std::endl;

        // Each deletion is attempted independently so that one failure does not leave
        // the remaining resources behind.
        bool result = true;

        Aws::CloudWatch::Model::DeleteAlarmMuteRuleRequest muteRuleRequest;
        muteRuleRequest.SetAlarmMuteRuleName(muteRuleName);
        auto muteRuleOutcome = client.DeleteAlarmMuteRule(muteRuleRequest);
        if (muteRuleOutcome.IsSuccess()) {
            std::cout << "Deleted mute rule " << muteRuleName << "." << std::endl;
        } else {
            std::cerr << "Could not delete the mute rule: "
                      << muteRuleOutcome.GetError().GetMessage() << std::endl;
            result = false;
        }

        Aws::CloudWatch::Model::DeleteAlarmsRequest alarmRequest;
        alarmRequest.AddAlarmNames(alarmName);
        auto alarmOutcome = client.DeleteAlarms(alarmRequest);
        if (alarmOutcome.IsSuccess()) {
            std::cout << "Deleted alarm " << alarmName << "." << std::endl;
        } else {
            std::cerr << "Could not delete the alarm: "
                      << alarmOutcome.GetError().GetMessage() << std::endl;
            result = false;
        }

        if (dashboardCreated) {
            Aws::CloudWatch::Model::DeleteDashboardsRequest dashboardRequest;
            dashboardRequest.AddDashboardNames(dashboardName);
            auto dashboardOutcome = client.DeleteDashboards(dashboardRequest);
            if (dashboardOutcome.IsSuccess()) {
                std::cout << "Deleted dashboard " << dashboardName << "." << std::endl;
            } else {
                std::cerr << "Could not delete the dashboard: "
                          << dashboardOutcome.GetError().GetMessage() << std::endl;
                result = false;
            }
        }

        if (!startedEnrichment) {
            std::cout << "Left OTel enrichment running, because it was already on before"
                      << std::endl << "this run." << std::endl;
            return result;
        }

        Aws::CloudWatch::Model::StopOTelEnrichmentRequest stopRequest;
        auto stopOutcome = client.StopOTelEnrichment(stopRequest);
        if (stopOutcome.IsSuccess()) {
            std::cout << "Stopped OTel enrichment, because this run started it."
                      << std::endl;
        } else {
            std::cerr << "Could not stop OTel enrichment: "
                      << stopOutcome.GetError().GetMessage() << std::endl;
            result = false;
        }

        return result;
    }
} // namespace

//! Run the Amazon CloudWatch Basics scenario.
/*!
  \param query: The PromQL query to alarm on.
  \param clientConfig: AWS client configuration.
  \return bool: Function succeeded.
 */
bool runCloudWatchScenario(const Aws::String &query,
                           const Aws::Client::ClientConfiguration &clientConfig) {
    Aws::CloudWatch::CloudWatchClient client(clientConfig);

    // Suffix the resource names so repeated runs do not collide.
    std::mt19937 generator(std::random_device{}());
    const int suffix = std::uniform_int_distribution<int>(1000, 9999)(generator);
    const Aws::String alarmName =
        "doc-example-promql-alarm-" + std::to_string(suffix);
    const Aws::String dashboardName = "doc-example-dashboard-" + std::to_string(suffix);
    const Aws::String muteRuleName = "doc-example-mute-rule-" + std::to_string(suffix);

    Aws::CloudWatch::Model::Metric metric;
    bool startedEnrichment = false;
    bool dashboardCreated = false;
    bool result = true;

    std::cout << DASHES << std::endl;
    std::cout << "Welcome to the Amazon CloudWatch Basics scenario." << std::endl
              << std::endl;
    std::cout << "CloudWatch now ingests OpenTelemetry metrics natively. This scenario"
              << std::endl
              << "walks through that experience: it turns on OTel enrichment so"
              << std::endl
              << "CloudWatch can correlate incoming OTLP metrics with the resources that"
              << std::endl
              << "produced them, alarms on those metrics with a PromQL query, and shows"
              << std::endl
              << "you which individual series drove the alarm." << std::endl << std::endl;
    std::cout << "A PromQL alarm works differently from a classic metric alarm. Rather"
              << std::endl
              << "than watching one metric and counting breaching periods, it evaluates"
              << std::endl
              << "a query that can match many series at once, and tracks each one"
              << std::endl << "separately as a contributor." << std::endl;
    std::cout << DASHES << std::endl;
    pressEnter();

    // Every step prompts for Enter before the next one, but only while the scenario is
    // still healthy. Once a step fails the remaining steps are skipped, so there is
    // nothing left to wait for and the run goes straight to cleanup.
    if (!listMetricsAndNamespaces(client, metric)) {
        result = false;
    }
    std::cout << DASHES << std::endl;
    if (result) {
        pressEnter();
    }

    if (result && !startOTelEnrichment(client, startedEnrichment)) {
        result = false;
    }
    std::cout << DASHES << std::endl;
    if (result) {
        pressEnter();
    }

    if (result) {
        explainOtlpIngestion();
        std::cout << DASHES << std::endl;
        pressEnter();
    }

    if (result && !createPromQLAlarm(client, alarmName, query)) {
        result = false;
    }
    std::cout << DASHES << std::endl;
    if (result) {
        pressEnter();
    }

    if (result && !inspectAlarmContributors(client, alarmName)) {
        result = false;
    }
    std::cout << DASHES << std::endl;
    if (result) {
        pressEnter();
    }

    if (result && !getStatisticsAndChartMetric(client, metric, dashboardName,
                                               clientConfig.region,
                                               dashboardCreated)) {
        result = false;
    }
    std::cout << DASHES << std::endl;
    if (result) {
        pressEnter();
    }

    if (result && !muteAlarmForMaintenance(client, muteRuleName, alarmName)) {
        result = false;
    }
    std::cout << DASHES << std::endl;
    if (result) {
        pressEnter();
    }

    // Clean up regardless of whether an earlier step failed, so a partial run does not
    // leave resources behind.
    if (!cleanUp(client, alarmName, dashboardName, muteRuleName, dashboardCreated,
                 startedEnrichment)) {
        result = false;
    }
    std::cout << DASHES << std::endl;

    std::cout << "This concludes the Amazon CloudWatch Basics scenario." << std::endl;
    std::cout << DASHES << std::endl;

    return result;
}
```
+ For API details, see the following topics in *AWS SDK for C\+\+ API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteAlarms)
  + [DeleteDashboards](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DeleteDashboards)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetDashboard](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetDashboard)
  + [GetMetricStatistics](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetMetricStatistics)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListAlarmMuteRules)
  + [ListDashboards](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListDashboards)
  + [ListMetrics](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/ListMetrics)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutDashboard](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutDashboard)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/StopOTelEnrichment)

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/cloudwatch#code-examples). 
Run an interactive scenario demonstrating the CloudWatch OpenTelemetry experience.  

```
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import software.amazon.awssdk.services.cloudwatch.model.AlarmContributor;
import software.amazon.awssdk.services.cloudwatch.model.AlarmMuteRuleSummary;
import software.amazon.awssdk.services.cloudwatch.model.Dimension;
import software.amazon.awssdk.services.cloudwatch.model.GetAlarmMuteRuleResponse;

import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

/**
 * Before running this Java V2 code example, set up your development environment,
 * including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * This scenario demonstrates the Amazon CloudWatch OpenTelemetry (OTel) experience.
 * CloudWatch ingests OpenTelemetry metrics natively, and this example walks through what
 * you do with them: turning on enrichment so CloudWatch can correlate incoming OTLP
 * metrics with the resources that produced them, alarming on those metrics with a PromQL
 * query, and finding out which individual series drove the alarm.
 *
 * A PromQL alarm works differently from a classic metric alarm. Rather than watching one
 * metric and counting breaching periods, it evaluates a query that can match many series
 * at once, and tracks each matching series separately as a contributor.
 *
 * Note that sending OTLP metrics to CloudWatch is not an AWS SDK operation. Metrics
 * arrive over the OTLP protocol through the CloudWatch agent, an OpenTelemetry
 * Collector, or an ADOT SDK. Everything this scenario does is configuration and querying
 * around that ingestion path.
 *
 * This Java code example performs the following tasks:
 *
 * 1. List metrics and namespaces from Amazon CloudWatch.
 * 2. Start OpenTelemetry enrichment for the account.
 * 3. Explain how OTLP metrics reach CloudWatch.
 * 4. Create an alarm that evaluates a PromQL query.
 * 5. Inspect the contributors to the PromQL alarm.
 * 6. Get metric statistics and chart the metric on a dashboard.
 * 7. Mute the alarm for a maintenance window.
 * 8. Clean up the Amazon CloudWatch resources.
 */
public class CloudWatchScenario {
    public static final String DASHES = new String(new char[80]).replace("\0", "-");

    private static final String DEFAULT_QUERY = "avg by (host) (system_cpu_utilization) > 80";

    // Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
    private static final int EVALUATION_INTERVAL = 60;
    private static final int PENDING_PERIOD = 300;
    private static final int RECOVERY_PERIOD = 120;

    static CloudWatchActions cwActions = new CloudWatchActions();

    private static final Logger logger = LoggerFactory.getLogger(CloudWatchScenario.class);
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws Throwable {

        // Suffix the resource names so repeated runs do not collide.
        String suffix = String.valueOf(new Random().nextInt(9000) + 1000);
        String alarmName = "doc-example-promql-alarm-" + suffix;
        String dashboardName = "doc-example-dashboard-" + suffix;
        String muteRuleName = "doc-example-mute-rule-" + suffix;

        logger.info(DASHES);
        logger.info("Welcome to the Amazon CloudWatch Basics scenario.");
        logger.info("""
            CloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through
            that experience: it turns on OTel enrichment so CloudWatch can correlate incoming
            OTLP metrics with the resources that produced them, alarms on those metrics with a
            PromQL query, and shows you which individual series drove the alarm.

            A PromQL alarm works differently from a classic metric alarm. Rather than watching
            one metric and counting breaching periods, it evaluates a query that can match many
            series at once, and tracks each one separately as a contributor.

            Let's get started...
            """);
        waitForInputToContinue(scanner);

        try {
            runScenario(alarmName, dashboardName, muteRuleName);
        } catch (RuntimeException e) {
            e.printStackTrace();
        }
        logger.info(DASHES);
    }

    private static void runScenario(String alarmName, String dashboardName, String muteRuleName)
            throws Throwable {

        // Tracks whether this run turned enrichment on, so that cleanup only turns off
        // enrichment that this run started.
        boolean startedEnrichment = false;

        logger.info(DASHES);
        logger.info("""
            1. List metrics and namespaces

            Before configuring anything, let's see what CloudWatch is already collecting in
            this account by calling ListMetrics.
            """);
        waitForInputToContinue(scanner);

        ArrayList<String> namespaces = cwActions.listNameSpacesAsync().join();
        logger.info("Found {} namespaces in this account:", namespaces.size());
        namespaces.stream().limit(10).forEach(namespace -> logger.info("  {}", namespace));
        if (namespaces.isEmpty()) {
            logger.info("""
                No metrics found in this account. The statistics and dashboard steps later on
                need an existing metric, so they will be skipped.
                """);
        }
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            2. Start OpenTelemetry enrichment

            Enrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics
            you send it. Without it, your metrics arrive as opaque series with no connection to
            the resources that emitted them.

            We check the current state first, and only start enrichment if it isn't already on.
            """);
        waitForInputToContinue(scanner);

        String status = cwActions.getOTelEnrichmentStatusAsync().join();
        logger.info("Enrichment status: {}", status);

        if (!"Running".equalsIgnoreCase(status)) {
            cwActions.startOTelEnrichmentAsync().join();
            startedEnrichment = true;
            status = cwActions.getOTelEnrichmentStatusAsync().join();
            logger.info("Enrichment status: {}", status);
            logger.info("""
                Note: this run started enrichment, so the cleanup step will stop it again.
                """);
        } else {
            logger.info("""
                Enrichment was already running, so we will leave it alone. The cleanup step
                will not stop it, because other workloads in this account may depend on it.
                """);
        }
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            3. Send OTLP metrics to CloudWatch

            This step is not an AWS SDK operation, and that's worth being explicit about.
            Metrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an
            OpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call.

            Point your collector at the CloudWatch metrics endpoint, which follows the pattern
            https://monitoring.<region>.amazonaws.com/v1/metrics

            The endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp
            exporter rather than otlp. The metrics endpoint signs as "monitoring".
            """);
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            4. Create a PromQL alarm

            Now we alarm on those metrics. The comparison goes inside the query itself: a
            PromQL alarm has no separate threshold, comparison operator, statistic, or period.
            """);
        logger.info("Enter a PromQL query, or press <ENTER> for the default");
        logger.info("[{}]:", DEFAULT_QUERY);
        String queryInput = scanner.nextLine();
        String query = queryInput == null || queryInput.isBlank() ? DEFAULT_QUERY : queryInput.trim();

        cwActions.putPromQLMetricAlarmAsync(alarmName, query, EVALUATION_INTERVAL,
                PENDING_PERIOD, RECOVERY_PERIOD).join();
        logger.info("Created alarm {}:", alarmName);
        logger.info("  query:              {}", query);
        logger.info("  evaluationInterval: {} seconds", EVALUATION_INTERVAL);
        logger.info("  pendingPeriod:      {} seconds", PENDING_PERIOD);
        logger.info("  recoveryPeriod:     {} seconds", RECOVERY_PERIOD);
        logger.info("""

            A PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is
            another way it differs from a classic alarm.
            """);
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            5. Inspect the alarm's contributors

            Each contributor is one series the query matched, identified by its label set. This
            is how you find out which host is unhealthy rather than only that something is.
            Classic alarms have no equivalent.
            """);
        waitForInputToContinue(scanner);

        List<AlarmContributor> contributors = cwActions.describeAlarmContributorsAsync(alarmName).join();
        if (contributors.isEmpty()) {
            logger.info("""
                No contributors yet. The query matched no series, which usually means no OTel
                metrics with these labels have arrived. Once your collector is sending data,
                each matching series appears here with its labels and the reason it breached.
                """);
        } else {
            logger.info("Found {} contributors:", contributors.size());
            for (AlarmContributor contributor : contributors) {
                StringBuilder labels = new StringBuilder();
                for (Map.Entry<String, String> attribute : contributor.contributorAttributes().entrySet()) {
                    if (labels.length() > 0) {
                        labels.append(", ");
                    }
                    labels.append(attribute.getKey()).append("=").append(attribute.getValue());
                }
                logger.info("  {}: {}", contributor.contributorId(), labels);
                logger.info("    reason: {}", contributor.stateReason());
            }
        }
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            6. Get statistics and chart the metric on a dashboard

            Statistics and dashboards are how you see what the alarm is evaluating.
            """);
        waitForInputToContinue(scanner);

        boolean dashboardCreated = false;
        if (!namespaces.isEmpty()) {
            String namespace = namespaces.get(0);
            ArrayList<String> metrics = cwActions.listMetsAsync(namespace).join();
            if (metrics != null && !metrics.isEmpty()) {
                String metricName = metrics.get(0);
                String startDate = Instant.now().minus(24, ChronoUnit.HOURS).toString();
                Dimension dimension = null;
                try {
                    dimension = cwActions.getSpecificMetAsync(namespace).join();
                    cwActions.getAndDisplayMetricStatisticsAsync(namespace, metricName,
                            "Average", startDate, dimension).join();
                } catch (RuntimeException e) {
                    logger.info("Could not get statistics for {}/{}: {}", namespace, metricName,
                            e.getMessage());
                }

                // Chart the metric this run just discovered. Reading the widgets from a
                // file would chart metrics that may not exist in this account.
                try {
                    String dashboardBody = buildDashboardBody(namespace, metricName, dimension,
                            cwActions.getRegion());
                    cwActions.createDashboardAsync(dashboardName, dashboardBody).join();
                    dashboardCreated = true;
                    cwActions.listDashboardsAsync().join();
                } catch (RuntimeException e) {
                    logger.info("Could not create the dashboard: {}", e.getMessage());
                }
            } else {
                logger.info("No metrics found in namespace {}, skipping statistics and the "
                        + "dashboard.", namespace);
            }
        } else {
            logger.info("Skipping statistics and dashboard because no metrics exist yet.");
        }
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("""
            7. Mute the alarm for a maintenance window

            While a mute rule is active the targeted alarms keep evaluating and keep changing
            state, but their actions do not fire. This is the supported way to suppress
            notifications during planned maintenance, instead of disabling alarm actions and
            hoping someone remembers to turn them back on.
            """);
        waitForInputToContinue(scanner);

        // The expression is a five-field cron expression,
        // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields,
        // not the six that Amazon EventBridge uses. For a one-time window, use
        // at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration from
        // PT1M to P15D, so PT2H rather than 2h.
        String expression = "cron(0 2 * * SUN)";
        String duration = "PT2H";
        String timezone = "America/Los_Angeles";

        cwActions.putAlarmMuteRuleAsync(muteRuleName, expression, duration, timezone,
                List.of(alarmName)).join();
        logger.info("Created mute rule {}:", muteRuleName);
        logger.info("  schedule: {} for {}", expression, duration);
        logger.info("  timezone: {}", timezone);
        logger.info("  targets:  {}", alarmName);
        logger.info("""

            Note the two formats here. The expression is a five-field cron expression, five
            rather than the six Amazon EventBridge uses. The duration is an ISO 8601 duration,
            so 'PT2H' and not '2h'.

            Also note that muteTargets is set explicitly. If you leave it out, the rule applies
            to every alarm in the account.
            """);

        GetAlarmMuteRuleResponse muteRule = cwActions.getAlarmMuteRuleAsync(muteRuleName).join();
        logger.info("Read the rule back: status {}, mute type {}.", muteRule.statusAsString(),
                muteRule.muteType());

        List<AlarmMuteRuleSummary> summaries = cwActions.listAlarmMuteRulesAsync(alarmName).join();
        logger.info("Found {} mute rules targeting this alarm.", summaries.size());
        // Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
        summaries.stream()
                .filter(summary -> summary.alarmMuteRuleArn().endsWith("/" + muteRuleName)
                        || summary.alarmMuteRuleArn().endsWith(":" + muteRuleName))
                .findFirst()
                .ifPresent(summary -> logger.info("  matched by ARN: {} ({})",
                        summary.alarmMuteRuleArn(), summary.statusAsString()));
        waitForInputToContinue(scanner);

        logger.info(DASHES);
        logger.info("8. Clean up");
        logger.info("Delete the resources this scenario created? (y/n)");
        String cleanUp = scanner.nextLine();
        if (cleanUp == null || !cleanUp.trim().equalsIgnoreCase("y")) {
            logger.info("""
                Skipping cleanup. Note that the alarm, dashboard, and mute rule are still in
                your account, and enrichment may still be running.
                """);
            logger.info(DASHES);
            logger.info("This concludes the Amazon CloudWatch Basics scenario.");
            return;
        }

        // Each deletion is attempted independently so that one failure does not leave the
        // remaining resources behind.
        try {
            cwActions.deleteAlarmMuteRuleAsync(muteRuleName).join();
        } catch (RuntimeException e) {
            logger.info("Could not delete the mute rule: {}", e.getMessage());
        }

        try {
            cwActions.deleteCWAlarmAsync(alarmName).join();
            logger.info("Deleted alarm {}.", alarmName);
        } catch (RuntimeException e) {
            logger.info("Could not delete the alarm: {}", e.getMessage());
        }

        if (dashboardCreated) {
            try {
                cwActions.deleteDashboardAsync(dashboardName).join();
                logger.info("Deleted dashboard {}.", dashboardName);
            } catch (RuntimeException e) {
                logger.info("Could not delete the dashboard: {}", e.getMessage());
            }
        }

        if (startedEnrichment) {
            try {
                cwActions.stopOTelEnrichmentAsync().join();
                logger.info("Stopped OTel enrichment, because this run started it.");
            } catch (RuntimeException e) {
                logger.info("Could not stop OTel enrichment: {}", e.getMessage());
            }
        } else {
            logger.info("""
                Left OTel enrichment running, because it was already on before this run.
                """);
        }

        logger.info(DASHES);
        logger.info("This concludes the Amazon CloudWatch Basics scenario.");
        logger.info(DASHES);
    }

    /**
     * Builds a single-widget dashboard body that charts the given metric.
     *
     * @param metricNamespace the namespace of the metric to chart
     * @param metricName      the name of the metric to chart
     * @param dimension       a dimension to narrow the metric to, or null for none
     * @param region          the Region the metric is in. A metric widget must name its
     *                        Region, because a dashboard can chart metrics from several.
     * @return the dashboard body, as JSON
     */
    static String buildDashboardBody(String metricNamespace, String metricName,
            Dimension dimension, String region) {
        String dimensionParts = dimension == null ? ""
                : String.format(", \"%s\", \"%s\"", dimension.name(), dimension.value());

        return String.format("""
            {
                "widgets": [
                    {
                        "type": "text",
                        "x": 0, "y": 0, "width": 24, "height": 2,
                        "properties": {
                            "markdown": "This dashboard was created programmatically by an AWS SDK code example."
                        }
                    },
                    {
                        "type": "metric",
                        "x": 0, "y": 2, "width": 12, "height": 6,
                        "properties": {
                            "metrics": [[ "%s", "%s"%s ]],
                            "view": "timeSeries",
                            "stat": "Average",
                            "period": 300,
                            "region": "%s",
                            "title": "%s"
                        }
                    }
                ]
            }
            """, metricNamespace, metricName, dimensionParts, region, metricName);
    }

    private static void waitForInputToContinue(Scanner scanner) {
        while (true) {
            logger.info("");
            logger.info("Press <ENTER> to continue:");
            String input = scanner.nextLine();

            if (input == null || input.trim().isEmpty()) {
                logger.info("Continuing with the program...");
                logger.info("");
                break;
            } else {
                logger.info("Invalid input. Please try again.");
            }
        }
    }
}
```
A wrapper class for the CloudWatch SDK methods that the scenario calls.  

```
public class CloudWatchActions {

    private static CloudWatchAsyncClient cloudWatchAsyncClient;

    private static final Logger logger = LoggerFactory.getLogger(CloudWatchActions.class);

    /**
     * Retrieves an asynchronous CloudWatch client instance.
     *
     * <p>
     * This method ensures that the CloudWatch client is initialized with the following configurations:
     * <ul>
     *     <li>Maximum concurrency: 100</li>
     *     <li>Connection timeout: 60 seconds</li>
     *     <li>Read timeout: 60 seconds</li>
     *     <li>Write timeout: 60 seconds</li>
     *     <li>API call timeout: 2 minutes</li>
     *     <li>API call attempt timeout: 90 seconds</li>
     *     <li>Retry strategy: STANDARD</li>
     * </ul>
     * </p>
     *
     * @return the asynchronous CloudWatch client instance
     */
    private static CloudWatchAsyncClient getAsyncClient() {
        if (cloudWatchAsyncClient == null) {
            SdkAsyncHttpClient httpClient = NettyNioAsyncHttpClient.builder()
                .maxConcurrency(100)
                .connectionTimeout(Duration.ofSeconds(60))
                .readTimeout(Duration.ofSeconds(60))
                .writeTimeout(Duration.ofSeconds(60))
                .build();

            ClientOverrideConfiguration overrideConfig = ClientOverrideConfiguration.builder()
                .apiCallTimeout(Duration.ofMinutes(2))
                .apiCallAttemptTimeout(Duration.ofSeconds(90))
                .retryStrategy(RetryMode.STANDARD)
                .build();

            cloudWatchAsyncClient = CloudWatchAsyncClient.builder()
                .httpClient(httpClient)
                .overrideConfiguration(overrideConfig)
                .build();
        }
        return cloudWatchAsyncClient;
    }

    /**
     * Returns the Region the client resolved, which a dashboard's metric widgets must name.
     *
     * @return the Region ID, such as us-east-1
     */
    public String getRegion() {
        return getAsyncClient().serviceClientConfiguration().region().id();
    }

    /**
     * Deletes an Anomaly Detector.
     *
     * @param fileName the name of the file containing the Anomaly Detector configuration
     * @return a CompletableFuture that represents the asynchronous deletion of the Anomaly Detector
     */
    public CompletableFuture<DeleteAnomalyDetectorResponse> deleteAnomalyDetectorAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser); // Return the root node
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
            String customMetricName = rootNode.findValue("customMetricName").asText();

            SingleMetricAnomalyDetector singleMetricAnomalyDetector = SingleMetricAnomalyDetector.builder()
                .metricName(customMetricName)
                .namespace(customMetricNamespace)
                .stat("Maximum")
                .build();

            DeleteAnomalyDetectorRequest request = DeleteAnomalyDetectorRequest.builder()
                .singleMetricAnomalyDetector(singleMetricAnomalyDetector)
                .build();

            return getAsyncClient().deleteAnomalyDetector(request);
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Failed to delete the Anomaly Detector", exception);
            } else {
                logger.info("Successfully deleted the Anomaly Detector.");
            }
        });
    }

    /**
     * Deletes a CloudWatch alarm.
     *
     * @param alarmName the name of the alarm to be deleted
     * @return a {@link CompletableFuture} representing the asynchronous operation to delete the alarm
     * the {@link DeleteAlarmsResponse} is returned when the operation completes successfully,
     * or a {@link RuntimeException} is thrown if the operation fails
     */
    public CompletableFuture<DeleteAlarmsResponse> deleteCWAlarmAsync(String alarmName) {
        DeleteAlarmsRequest request = DeleteAlarmsRequest.builder()
            .alarmNames(alarmName)
            .build();

        return getAsyncClient().deleteAlarms(request)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete the alarm:{} " + alarmName, exception);
                } else {
                    logger.info("Successfully deleted alarm {} ", alarmName);
                }
            });
    }

    /**
     * Deletes the specified dashboard.
     *
     * @param dashboardName the name of the dashboard to be deleted
     * @return a {@link CompletableFuture} representing the asynchronous operation of deleting the dashboard
     * @throws RuntimeException if the dashboard deletion fails
     */
    public CompletableFuture<DeleteDashboardsResponse> deleteDashboardAsync(String dashboardName) {
        DeleteDashboardsRequest dashboardsRequest = DeleteDashboardsRequest.builder()
            .dashboardNames(dashboardName)
            .build();

        return getAsyncClient().deleteDashboards(dashboardsRequest)
            .whenComplete((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete the dashboard: " + dashboardName, exception);
                } else {
                    logger.info("{} was successfully deleted.", dashboardName);
                }
            });
    }


    /**
     * Retrieves and saves a custom metric image to a file.
     *
     * @param fileName the name of the file to save the metric image to
     * @return a {@link CompletableFuture} that completes when the image has been saved to the file
     */
    public CompletableFuture<Void> downloadAndSaveMetricImageAsync(String fileName) {
        logger.info("Getting Image data for custom metric.");
        String myJSON = """
              {
                  "title": "Example Metric Graph",
                  "view": "timeSeries",
                  "stacked ": false,
                  "period": 10,
                  "width": 1400,
                  "height": 600,
                  "metrics": [
                      [
                      "AWS/Billing",
                      "EstimatedCharges",
                      "Currency",
                      "USD"
                     ]
                  ]
              }
            """;

        GetMetricWidgetImageRequest imageRequest = GetMetricWidgetImageRequest.builder()
            .metricWidget(myJSON)
            .build();

        return getAsyncClient().getMetricWidgetImage(imageRequest)
            .thenCompose(response -> {
                SdkBytes sdkBytes = response.metricWidgetImage();
                byte[] bytes = sdkBytes.asByteArray();
                return CompletableFuture.runAsync(() -> {
                    try {
                        File outputFile = new File(fileName);
                        try (FileOutputStream outputStream = new FileOutputStream(outputFile)) {
                            outputStream.write(bytes);
                        }
                    } catch (IOException e) {
                        throw new RuntimeException("Failed to write image to file", e);
                    }
                });
            })
            .whenComplete((result, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Error getting and saving metric image", exception);
                } else {
                    logger.info("Image data saved successfully to {}", fileName);
                }
            });
    }


    /**
     * Describes the anomaly detectors based on the specified JSON file.
     *
     * @param fileName the name of the JSON file containing the custom metric namespace and name
     * @return a {@link CompletableFuture} that completes when the anomaly detectors have been described
     * @throws RuntimeException if there is a failure during the operation, such as when reading or parsing the JSON file,
     *                          or when describing the anomaly detectors
     */
    public CompletableFuture<Void> describeAnomalyDetectorsAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser);
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            try {
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                DescribeAnomalyDetectorsRequest detectorsRequest = DescribeAnomalyDetectorsRequest.builder()
                    .maxResults(10)
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                return getAsyncClient().describeAnomalyDetectors(detectorsRequest).thenAccept(response -> {
                    List<AnomalyDetector> anomalyDetectorList = response.anomalyDetectors();
                    for (AnomalyDetector detector : anomalyDetectorList) {
                        logger.info("Metric name: {} ", detector.singleMetricAnomalyDetector().metricName());
                        logger.info("State: {} ", detector.stateValue());
                    }
                });
            } catch (RuntimeException e) {
                throw new RuntimeException("Failed to describe anomaly detectors", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error describing anomaly detectors", exception);
            }
        });
    }


    /**
     * Adds an anomaly detector for the given file.
     *
     * @param fileName the name of the file containing the anomaly detector configuration
     * @return a {@link CompletableFuture} that completes when the anomaly detector has been added
     */
    public CompletableFuture<Void> addAnomalyDetectorAsync(String fileName) {
        CompletableFuture<JsonNode> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                return new ObjectMapper().readTree(parser); // Return the root node
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        return readFileFuture.thenCompose(rootNode -> {
            try {
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                SingleMetricAnomalyDetector singleMetricAnomalyDetector = SingleMetricAnomalyDetector.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .stat("Maximum")
                    .build();

                PutAnomalyDetectorRequest anomalyDetectorRequest = PutAnomalyDetectorRequest.builder()
                    .singleMetricAnomalyDetector(singleMetricAnomalyDetector)
                    .build();

                return getAsyncClient().putAnomalyDetector(anomalyDetectorRequest).thenAccept(response -> {
                    logger.info("Added anomaly detector for metric {}", customMetricName);
                });
            } catch (Exception e) {
                throw new RuntimeException("Failed to create anomaly detector", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error adding anomaly detector", exception);
            }
        });
    }


    /**
     * Retrieves the alarm history for a given alarm name and date range.
     *
     * @param fileName the path to the JSON file containing the alarm name
     * @param date     the date to start the alarm history search (in the format "yyyy-MM-dd'T'HH:mm:ss'Z'")
     * @return a {@code CompletableFuture<Void>} that completes when the alarm history has been retrieved and processed
     */
    public CompletableFuture<Void> getAlarmHistoryAsync(String fileName, String date) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.findValue("exampleAlarmName").asText(); // Return alarmName from the JSON file
            } catch (IOException e) {
                throw new RuntimeException("Failed to read or parse the file", e);
            }
        });

        // Use the alarm name to describe alarm history with a paginator.
        return readFileFuture.thenCompose(alarmName -> {
            try {
                Instant start = Instant.parse(date);
                Instant endDate = Instant.now();
                DescribeAlarmHistoryRequest historyRequest = DescribeAlarmHistoryRequest.builder()
                    .startDate(start)
                    .endDate(endDate)
                    .alarmName(alarmName)
                    .historyItemType(HistoryItemType.ACTION)
                    .build();

                // Use the paginator to paginate through alarm history pages.
                DescribeAlarmHistoryPublisher historyPublisher = getAsyncClient().describeAlarmHistoryPaginator(historyRequest);
                CompletableFuture<Void> future = historyPublisher
                    .subscribe(response -> response.alarmHistoryItems().forEach(item -> {
                        logger.info("History summary: {}", item.historySummary());
                        logger.info("Timestamp: {}", item.timestamp());
                    }))
                    .whenComplete((result, exception) -> {
                        if (exception != null) {
                            logger.error("Error occurred while getting alarm history: " + exception.getMessage(), exception);
                        } else {
                            logger.info("Successfully retrieved all alarm history.");
                        }
                    });

                // Return the future to the calling code for further handling
                return future;
            } catch (Exception e) {
                throw new RuntimeException("Failed to process alarm history", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error completing alarm history processing", exception);
            }
        });
    }



    /**
     * Checks for a metric alarm in AWS CloudWatch.
     *
     * @param fileName the name of the file containing the JSON configuration for the custom metric
     * @return a {@link CompletableFuture} that completes when the check for the metric alarm is complete
     */
    public CompletableFuture<Void> checkForMetricAlarmAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                DescribeAlarmsForMetricRequest metricRequest = DescribeAlarmsForMetricRequest.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                return checkForAlarmAsync(metricRequest, customMetricName, 10);

            } catch (IOException e) {
                throw new RuntimeException("Failed to parse JSON content", e);
            }
        }).whenComplete((result, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Error checking metric alarm", exception);
            }
        });
    }

    // Recursive method to check for the alarm.

    /**
     * Checks for the existence of an alarm asynchronously for the specified metric.
     *
     * @param metricRequest    the request to describe the alarms for the specified metric
     * @param customMetricName the name of the custom metric to check for an alarm
     * @param retries          the number of retries to perform if no alarm is found
     * @return a {@link CompletableFuture} that completes when an alarm is found or the maximum number of retries has been reached
     */
    private static CompletableFuture<Void> checkForAlarmAsync(DescribeAlarmsForMetricRequest metricRequest, String customMetricName, int retries) {
        if (retries == 0) {
            return CompletableFuture.completedFuture(null).thenRun(() ->
                logger.info("No Alarm state found for {} after 10 retries.", customMetricName)
            );
        }

        return (getAsyncClient().describeAlarmsForMetric(metricRequest).thenCompose(response -> {
            if (response.hasMetricAlarms()) {
                logger.info("Alarm state found for {}", customMetricName);
                return CompletableFuture.completedFuture(null); // Alarm found, complete the future
            } else {
                return CompletableFuture.runAsync(() -> {
                    try {
                        Thread.sleep(20000);
                        logger.info(".");
                    } catch (InterruptedException e) {
                        throw new RuntimeException("Interrupted while waiting to retry", e);
                    }
                }).thenCompose(v -> checkForAlarmAsync(metricRequest, customMetricName, retries - 1)); // Recursive call
            }
        }));
    }


    /**
     * Adds metric data for an alarm asynchronously.
     *
     * @param fileName the name of the JSON file containing the metric data
     * @return a CompletableFuture that asynchronously returns the PutMetricDataResponse
     */
    public CompletableFuture<PutMetricDataResponse> addMetricDataForAlarmAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();
                Instant instant = Instant.now();

                // Create MetricDatum objects.
                MetricDatum datum1 = MetricDatum.builder()
                    .metricName(customMetricName)
                    .unit(StandardUnit.NONE)
                    .value(1001.00)
                    .timestamp(instant)
                    .build();

                MetricDatum datum2 = MetricDatum.builder()
                    .metricName(customMetricName)
                    .unit(StandardUnit.NONE)
                    .value(1002.00)
                    .timestamp(instant)
                    .build();

                List<MetricDatum> metricDataList = new ArrayList<>();
                metricDataList.add(datum1);
                metricDataList.add(datum2);

                // Build the PutMetricData request.
                PutMetricDataRequest request = PutMetricDataRequest.builder()
                    .namespace(customMetricNamespace)
                    .metricData(metricDataList)
                    .build();

                // Send the request asynchronously.
                return getAsyncClient().putMetricData(request);

            } catch (IOException e) {
                CompletableFuture<PutMetricDataResponse> failedFuture = new CompletableFuture<>();
                failedFuture.completeExceptionally(new RuntimeException("Failed to parse JSON content", e));
                return failedFuture;
            }
        }).whenComplete((response, exception) -> {
            if (exception != null) {
                logger.error("Failed to put metric data: " + exception.getMessage(), exception);
            } else {
                logger.info("Added metric values for metric.");
            }
        });
    }


    /**
     * Retrieves custom metric data from the AWS CloudWatch service.
     *
     * @param fileName the name of the file containing the custom metric information
     * @return a {@link CompletableFuture} that completes when the metric data has been retrieved
     */
    public CompletableFuture<Void> getCustomMetricDataAsync(String fileName) {
        CompletableFuture<String> readFileFuture = CompletableFuture.supplyAsync(() -> {
            try {
                // Read values from the JSON file.
                JsonParser parser = new JsonFactory().createParser(new File(fileName));
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(parser);
                return rootNode.toString(); // Return JSON as a string for further processing
            } catch (IOException e) {
                throw new RuntimeException("Failed to read file", e);
            }
        });

        return readFileFuture.thenCompose(jsonContent -> {
            try {
                // Parse the JSON string to extract relevant values.
                com.fasterxml.jackson.databind.JsonNode rootNode = new ObjectMapper().readTree(jsonContent);
                String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
                String customMetricName = rootNode.findValue("customMetricName").asText();

                // Set the current time and date range for metric query.
                Instant nowDate = Instant.now();
                long hours = 1;
                long minutes = 30;
                Instant endTime = nowDate.plus(hours, ChronoUnit.HOURS).plus(minutes, ChronoUnit.MINUTES);

                Metric met = Metric.builder()
                    .metricName(customMetricName)
                    .namespace(customMetricNamespace)
                    .build();

                MetricStat metStat = MetricStat.builder()
                    .stat("Maximum")
                    .period(60)  // Assuming period in seconds
                    .metric(met)
                    .build();

                MetricDataQuery dataQuery = MetricDataQuery.builder()
                    .metricStat(metStat)
                    .id("foo2")
                    .returnData(true)
                    .build();

                List<MetricDataQuery> dq = new ArrayList<>();
                dq.add(dataQuery);

                GetMetricDataRequest getMetricDataRequest = GetMetricDataRequest.builder()
                    .maxDatapoints(10)
                    .scanBy(ScanBy.TIMESTAMP_DESCENDING)
                    .startTime(nowDate)
                    .endTime(endTime)
                    .metricDataQueries(dq)
                    .build();

                // Call the async method for CloudWatch data retrieval.
                return getAsyncClient().getMetricData(getMetricDataRequest);

            } catch (IOException e) {
                throw new RuntimeException("Failed to parse JSON content", e);
            }
        }).thenAccept(response -> {
            List<MetricDataResult> data = response.metricDataResults();
            for (MetricDataResult item : data) {
                logger.info("The label is: {}", item.label());
                logger.info("The status code is: {}", item.statusCode().toString());
            }
        }).exceptionally(exception -> {
            throw new RuntimeException("Failed to get metric data", exception);
        });
    }


    /**
     * Describes the CloudWatch alarms of the 'METRIC_ALARM' type.
     *
     * @return a {@link CompletableFuture} that represents the asynchronous operation
     * of describing the CloudWatch alarms. The future completes when the
     * operation is finished, either successfully or with an error.
     */
    public CompletableFuture<Void> describeAlarmsAsync() {
        List<AlarmType> typeList = new ArrayList<>();
        typeList.add(AlarmType.METRIC_ALARM);
        DescribeAlarmsRequest alarmsRequest = DescribeAlarmsRequest.builder()
            .alarmTypes(typeList)
            .maxRecords(10)
            .build();

        return getAsyncClient().describeAlarms(alarmsRequest)
            .thenAccept(response -> {
                List<MetricAlarm> alarmList = response.metricAlarms();
                for (MetricAlarm alarm : alarmList) {
                    logger.info("Alarm name: {}", alarm.alarmName());
                    logger.info("Alarm description: {} ", alarm.alarmDescription());
                }
            })
            .whenComplete((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to describe alarms: {}", ex.getMessage());
                } else {
                    logger.info("Successfully described alarms.");
                }
            });
    }

    /**
     * Creates an alarm based on the configuration provided in a JSON file.
     *
     * @param fileName the name of the JSON file containing the alarm configuration
     * @return a CompletableFuture that represents the asynchronous operation of creating the alarm
     * @throws RuntimeException if an exception occurs while reading the JSON file or creating the alarm
     */
    public CompletableFuture<String> createAlarmAsync(String fileName) {
        com.fasterxml.jackson.databind.JsonNode rootNode;
        try {
            JsonParser parser = new JsonFactory().createParser(new File(fileName));
            rootNode = new ObjectMapper().readTree(parser);
        } catch (IOException e) {
            throw new RuntimeException("Failed to read the alarm configuration file", e);
        }

        // Extract values from the JSON node.
        String customMetricNamespace = rootNode.findValue("customMetricNamespace").asText();
        String customMetricName = rootNode.findValue("customMetricName").asText();
        String alarmName = rootNode.findValue("exampleAlarmName").asText();
        String emailTopic = rootNode.findValue("emailTopic").asText();
        String accountId = rootNode.findValue("accountId").asText();
        String region = rootNode.findValue("region").asText();

        // Create a List for alarm actions.
        List<String> alarmActions = new ArrayList<>();
        alarmActions.add("arn:aws:sns:" + region + ":" + accountId + ":" + emailTopic);

        PutMetricAlarmRequest alarmRequest = PutMetricAlarmRequest.builder()
            .alarmActions(alarmActions)
            .alarmDescription("Example metric alarm")
            .alarmName(alarmName)
            .comparisonOperator(ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD)
            .threshold(100.00)
            .metricName(customMetricName)
            .namespace(customMetricNamespace)
            .evaluationPeriods(1)
            .period(10)
            .statistic("Maximum")
            .datapointsToAlarm(1)
            .treatMissingData("ignore")
            .build();

        // Call the putMetricAlarm asynchronously and handle the result.
        return getAsyncClient().putMetricAlarm(alarmRequest)
            .handle((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to create alarm: {}", ex.getMessage());
                    throw new RuntimeException("Failed to create alarm", ex);
                } else {
                    logger.info("{} was successfully created!", alarmName);
                    return alarmName;
                }
            });
    }

    /**
     * Adds a metric to a dashboard asynchronously.
     *
     * @param fileName      the name of the file containing the dashboard content
     * @param dashboardName the name of the dashboard to be updated
     * @return a {@link CompletableFuture} representing the asynchronous operation, which will complete with a
     * {@link PutDashboardResponse} when the dashboard is successfully updated
     */
    public CompletableFuture<PutDashboardResponse> addMetricToDashboardAsync(String fileName, String dashboardName) {
        String dashboardBody;
        try {
            dashboardBody = readFileAsString(fileName);
        } catch (IOException e) {
            throw new RuntimeException("Failed to read the dashboard file", e);
        }

        PutDashboardRequest dashboardRequest = PutDashboardRequest.builder()
            .dashboardName(dashboardName)
            .dashboardBody(dashboardBody)
            .build();

        return getAsyncClient().putDashboard(dashboardRequest)
            .handle((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to update dashboard: {}", ex.getMessage());
                    throw new RuntimeException("Error updating dashboard", ex);
                } else {
                    logger.info("{} was successfully updated.", dashboardName);
                    return response;
                }
            });
    }

    /**
     * Creates a new custom metric.
     *
     * @param dataPoint the data point to be added to the custom metric
     * @return a {@link CompletableFuture} representing the asynchronous operation of adding the custom metric
     */
    public CompletableFuture<PutMetricDataResponse> createNewCustomMetricAsync(Double dataPoint) {
        Dimension dimension = Dimension.builder()
            .name("UNIQUE_PAGES")
            .value("URLS")
            .build();

        // Set an Instant object for the current time in UTC.
        String time = ZonedDateTime.now(ZoneOffset.UTC).format(DateTimeFormatter.ISO_INSTANT);
        Instant instant = Instant.parse(time);

        // Create the MetricDatum.
        MetricDatum datum = MetricDatum.builder()
            .metricName("PAGES_VISITED")
            .unit(StandardUnit.NONE)
            .value(dataPoint)
            .timestamp(instant)
            .dimensions(dimension)
            .build();

        PutMetricDataRequest request = PutMetricDataRequest.builder()
            .namespace("SITE/TRAFFIC")
            .metricData(datum)
            .build();

        return getAsyncClient().putMetricData(request)
            .whenComplete((response, ex) -> {
                if (ex != null) {
                    throw new RuntimeException("Error adding custom metric", ex);
                } else {
                    logger.info("Successfully added metric values for PAGES_VISITED.");
                }
            });
    }

    /**
     * Lists the available dashboards.
     *
     * @return a {@link CompletableFuture} that completes when the operation is finished.
     * The future will complete exceptionally if an error occurs while listing the dashboards.
     */
    public CompletableFuture<Void> listDashboardsAsync() {
        ListDashboardsRequest listDashboardsRequest = ListDashboardsRequest.builder().build();
        ListDashboardsPublisher paginator = getAsyncClient().listDashboardsPaginator(listDashboardsRequest);
        return paginator.subscribe(response -> {
            response.dashboardEntries().forEach(entry -> {
                logger.info("Dashboard name is: {} ", entry.dashboardName());
                logger.info("Dashboard ARN is: {} ", entry.dashboardArn());
            });
        }).exceptionally(ex -> {
            logger.info("Failed to list dashboards: {} ", ex.getMessage());
            throw new RuntimeException("Error occurred while listing dashboards", ex);
        });
    }

    /**
     * Creates a new dashboard with the specified name and the metrics described by the given file.
     *
     * @param dashboardName the name of the dashboard to be created
     * @param fileName      the name of the file containing the dashboard body
     * @return a {@link CompletableFuture} representing the asynchronous operation of creating the dashboard
     * @throws IOException if there is an error reading the dashboard body from the file
     */
    public CompletableFuture<PutDashboardResponse> createDashboardWithMetricsAsync(String dashboardName, String fileName) throws IOException {
        return createDashboardAsync(dashboardName, readFileAsString(fileName));
    }


    /**
     * Creates a new dashboard with the specified name and body.
     *
     * @param dashboardName the name of the dashboard to be created
     * @param dashboardBody the dashboard body, as JSON
     * @return a {@link CompletableFuture} representing the asynchronous operation of creating the dashboard
     */
    public CompletableFuture<PutDashboardResponse> createDashboardAsync(String dashboardName, String dashboardBody) {
        PutDashboardRequest dashboardRequest = PutDashboardRequest.builder()
            .dashboardName(dashboardName)
            .dashboardBody(dashboardBody)
            .build();

        return getAsyncClient().putDashboard(dashboardRequest)
            .handle((response, ex) -> {
                if (ex != null) {
                    logger.info("Failed to create dashboard: {}", ex.getMessage());
                    throw new RuntimeException("Dashboard creation failed", ex);
                } else {
                    // Handle the normal response case
                    logger.info("{} was successfully created.", dashboardName);
                    List<DashboardValidationMessage> messages = response.dashboardValidationMessages();
                    if (messages.isEmpty()) {
                        logger.info("There are no messages in the new Dashboard.");
                    } else {
                        for (DashboardValidationMessage message : messages) {
                            logger.info("Message: {}", message.message());
                        }
                    }
                    return response; // Return the response for further use
                }
            });
    }


    /**
     * Retrieves the metric statistics for the "EstimatedCharges" metric in the "AWS/Billing" namespace.
     *
     * @param costDateWeek the start date for the metric statistics, in the format of an ISO-8601 date string (e.g., "2023-04-05")
     * @return a {@link CompletableFuture} that, when completed, contains the {@link GetMetricStatisticsResponse} with the retrieved metric statistics
     * @throws RuntimeException if the metric statistics cannot be retrieved successfully
     */
    public CompletableFuture<GetMetricStatisticsResponse> getMetricStatisticsAsync(String costDateWeek) {
        Instant start = Instant.parse(costDateWeek);
        Instant endDate = Instant.now();

        // Define dimension
        Dimension dimension = Dimension.builder()
            .name("Currency")
            .value("USD")
            .build();

        List<Dimension> dimensionList = new ArrayList<>();
        dimensionList.add(dimension);

        GetMetricStatisticsRequest statisticsRequest = GetMetricStatisticsRequest.builder()
            .metricName("EstimatedCharges")
            .namespace("AWS/Billing")
            .dimensions(dimensionList)
            .statistics(Statistic.MAXIMUM)
            .startTime(start)
            .endTime(endDate)
            .period(86400) // One day period
            .build();

        return getAsyncClient().getMetricStatistics(statisticsRequest)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    List<Datapoint> data = response.datapoints();
                    if (!data.isEmpty()) {
                        for (Datapoint datapoint : data) {
                            logger.info("Timestamp: {} Maximum value: {})", datapoint.timestamp(), datapoint.maximum());
                        }
                    } else {
                        logger.info("The returned data list is empty");
                    }
                } else {
                    throw new RuntimeException("Failed to get metric statistics: " + exception.getMessage(), exception);
                }
            });
    }


    /**
     * Retrieves and displays metric statistics for the specified parameters.
     *
     * @param nameSpace    the namespace for the metric
     * @param metVal       the name of the metric
     * @param metricOption the statistic to retrieve for the metric (e.g., "Maximum", "Average")
     * @param date         the date for which to retrieve the metric statistics, in the format "yyyy-MM-dd'T'HH:mm:ss'Z'"
     * @param myDimension  the dimension(s) to filter the metric statistics by
     * @return a {@link CompletableFuture} that completes when the metric statistics have been retrieved and displayed
     */
    public CompletableFuture<GetMetricStatisticsResponse> getAndDisplayMetricStatisticsAsync(String nameSpace, String metVal,
                                                                                             String metricOption, String date, Dimension myDimension) {

        Instant start = Instant.parse(date);
        Instant endDate = Instant.now();

        // Building the request for metric statistics.
        GetMetricStatisticsRequest statisticsRequest = GetMetricStatisticsRequest.builder()
            .endTime(endDate)
            .startTime(start)
            .dimensions(myDimension)
            .metricName(metVal)
            .namespace(nameSpace)
            .period(86400) // 1 day period
            .statistics(Statistic.fromValue(metricOption))
            .build();

        return getAsyncClient().getMetricStatistics(statisticsRequest)
            .whenComplete((response, exception) -> {
                if (response != null) {
                    List<Datapoint> data = response.datapoints();
                    if (!data.isEmpty()) {
                        for (Datapoint datapoint : data) {
                            logger.info("Timestamp: {} Maximum value: {}", datapoint.timestamp(), datapoint.maximum());
                        }
                    } else {
                        logger.info("The returned data list is empty");
                    }
                } else {
                    logger.info("Failed to get metric statistics: {} ", exception.getMessage());
                }
            })
            .exceptionally(exception -> {
                throw new RuntimeException("Error while getting metric statistics: " + exception.getMessage(), exception);
            });
    }


    /**
     * Retrieves a list of metric names for the specified namespace.
     *
     * @param namespace the namespace for which to retrieve the metric names
     * @return a {@link CompletableFuture} that, when completed, contains an {@link ArrayList} of
     * the metric names in the specified namespace
     * @throws RuntimeException if an error occurs while listing the metrics
     */
    public CompletableFuture<ArrayList<String>> listMetsAsync(String namespace) {
        ListMetricsRequest request = ListMetricsRequest.builder()
            .namespace(namespace)
            .build();

        ListMetricsPublisher metricsPaginator = getAsyncClient().listMetricsPaginator(request);
        Set<String> metSet = new HashSet<>();
        CompletableFuture<Void> future = metricsPaginator.subscribe(response -> {
            response.metrics().forEach(metric -> {
                String metricName = metric.metricName();
                metSet.add(metricName);
            });
        });

        return future
            .thenApply(ignored -> new ArrayList<>(metSet))
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to list metrics: " + exception.getMessage(), exception);
            });
    }

    /**
     * Lists the available namespaces for the current AWS account.
     *
     * @return a {@link CompletableFuture} that, when completed, contains an {@link ArrayList} of the available namespace names.
     * @throws RuntimeException if an error occurs while listing the namespaces.
     */
    public CompletableFuture<ArrayList<String>> listNameSpacesAsync() {
        ArrayList<String> nameSpaceList = new ArrayList<>();
        ListMetricsRequest request = ListMetricsRequest.builder().build();

        ListMetricsPublisher metricsPaginator = getAsyncClient().listMetricsPaginator(request);
        CompletableFuture<Void> future = metricsPaginator.subscribe(response -> {
            response.metrics().forEach(metric -> {
                String namespace = metric.namespace();
                if (!nameSpaceList.contains(namespace)) {
                    nameSpaceList.add(namespace);
                }
            });
        });

        return future
            .thenApply(ignored -> nameSpaceList)
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to list namespaces: " + exception.getMessage(), exception);
            });
    }
    /**
     * Retrieves the specific metric asynchronously.
     *
     * @param namespace the namespace of the metric to retrieve
     * @return a CompletableFuture that completes with the first dimension of the first metric found in the specified namespace,
     * or throws a RuntimeException if an error occurs or no metrics or dimensions are found
     */
    public CompletableFuture<Dimension> getSpecificMetAsync(String namespace) {
        ListMetricsRequest request = ListMetricsRequest.builder()
            .namespace(namespace)
            .build();

        return getAsyncClient().listMetrics(request).handle((response, exception) -> {
            if (exception != null) {
                logger.info("Error occurred while listing metrics: {} ", exception.getMessage());
                throw new RuntimeException("Failed to retrieve specific metric dimension", exception);
            } else {
                List<Metric> myList = response.metrics();
                if (!myList.isEmpty()) {
                    Metric metric = myList.get(0);
                    if (!metric.dimensions().isEmpty()) {
                        return metric.dimensions().get(0); // Return the first dimension
                    }
                }
                throw new RuntimeException("No metrics or dimensions found");
            }
        });
    }

    /**
     * Gets the current OTel enrichment status for the account. Enrichment is what makes
     * CloudWatch attach AWS resource context to incoming OTLP metrics, so the metrics
     * become correlatable with the rest of CloudWatch rather than opaque series.
     *
     * @return a {@link CompletableFuture} that completes with the status, such as
     * {@code Running} or {@code NotStarted}
     */
    public CompletableFuture<String> getOTelEnrichmentStatusAsync() {
        return getAsyncClient().getOTelEnrichment(GetOTelEnrichmentRequest.builder().build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to get OTel enrichment status: "
                        + exception.getMessage(), exception);
                }
                return response.statusAsString();
            });
    }

    /**
     * Turns on OTel enrichment for the account.
     *
     * @return a {@link CompletableFuture} that completes when enrichment has started
     */
    public CompletableFuture<Void> startOTelEnrichmentAsync() {
        return getAsyncClient().startOTelEnrichment(StartOTelEnrichmentRequest.builder().build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to start OTel enrichment: "
                        + exception.getMessage(), exception);
                }
                logger.info("Started OTel enrichment for this account.");
                return null;
            });
    }

    /**
     * Turns off OTel enrichment for the account. Existing PromQL alarms are not deleted,
     * but vended metrics stop being enriched, so queries that select on the added labels
     * stop matching.
     *
     * @return a {@link CompletableFuture} that completes when enrichment has stopped
     */
    public CompletableFuture<Void> stopOTelEnrichmentAsync() {
        return getAsyncClient().stopOTelEnrichment(StopOTelEnrichmentRequest.builder().build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to stop OTel enrichment: "
                        + exception.getMessage(), exception);
                }
                logger.info("Stopped OTel enrichment for this account.");
                return null;
            });
    }

    /**
     * Creates an alarm that evaluates a PromQL query.
     *
     * <p>A PromQL alarm differs from a classic metric alarm in a few ways. The query can
     * match many series at once, and each matching series is tracked separately as a
     * contributor. Instead of counting breaching periods, you specify durations: a
     * contributor moves to ALARM after it breaches continuously for the pending period,
     * and back to OK after it stops breaching for the recovery period. A PromQL alarm
     * starts in the OK state rather than INSUFFICIENT_DATA.
     *
     * <p>{@link EvaluationCriteria} is a union and is mutually exclusive with the classic
     * {@code metricName} and {@code metrics} parameters. When you use it you must also set
     * {@code evaluationInterval}, and you must not set {@code period}, {@code statistic},
     * {@code threshold}, {@code comparisonOperator}, or {@code evaluationPeriods}.
     *
     * @param alarmName          the name of the alarm, unique within the Region
     * @param query              the PromQL query to evaluate. The comparison belongs in
     *                           the query itself; there is no separate threshold.
     * @param evaluationInterval how often, in seconds, to run the query. Valid values are
     *                           10, 20, 30, and any multiple of 60, up to 3600.
     * @param pendingPeriod      how long, in seconds, a contributor must breach
     *                           continuously before it moves to ALARM
     * @param recoveryPeriod     how long, in seconds, a contributor must stop breaching
     *                           before it moves back to OK
     * @return a {@link CompletableFuture} that completes when the alarm is created
     */
    public CompletableFuture<Void> putPromQLMetricAlarmAsync(String alarmName, String query,
            int evaluationInterval, int pendingPeriod, int recoveryPeriod) {
        AlarmPromQLCriteria promQLCriteria = AlarmPromQLCriteria.builder()
            .query(query)
            .pendingPeriod(pendingPeriod)
            .recoveryPeriod(recoveryPeriod)
            .build();

        PutMetricAlarmRequest request = PutMetricAlarmRequest.builder()
            .alarmName(alarmName)
            .alarmDescription("PromQL alarm created by the AWS SDK for Java 2.x Basics scenario.")
            .evaluationCriteria(EvaluationCriteria.builder()
                .promQLCriteria(promQLCriteria)
                .build())
            .evaluationInterval(evaluationInterval)
            .build();

        return getAsyncClient().putMetricAlarm(request).handle((response, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Failed to create PromQL alarm: "
                    + exception.getMessage(), exception);
            }
            logger.info("Created PromQL alarm {} for query {}.", alarmName, query);
            return null;
        });
    }

    /**
     * Gets the contributors for a PromQL alarm. Each contributor is one series that the
     * alarm's query matched, identified by its label set. This is how you find out which
     * hosts, services, or pods are breaching, rather than only that something is.
     *
     * <p>The paging loop continues until the next token is empty. A page can come back
     * empty while still carrying a next token, so stopping at the first empty page would
     * silently drop later results.
     *
     * @param alarmName the name of the PromQL alarm
     * @return a {@link CompletableFuture} that completes with the list of contributors,
     * which is empty when the query matched no series
     */
    public CompletableFuture<List<AlarmContributor>> describeAlarmContributorsAsync(String alarmName) {
        List<AlarmContributor> contributors = new ArrayList<>();
        return collectContributorsPage(alarmName, null, contributors);
    }

    private CompletableFuture<List<AlarmContributor>> collectContributorsPage(String alarmName,
            String nextToken, List<AlarmContributor> accumulated) {
        DescribeAlarmContributorsRequest request = DescribeAlarmContributorsRequest.builder()
            .alarmName(alarmName)
            .nextToken(nextToken)
            .build();

        return getAsyncClient().describeAlarmContributors(request)
            .thenCompose(response -> {
                accumulated.addAll(response.alarmContributors());
                String token = response.nextToken();
                if (token == null || token.isEmpty()) {
                    return CompletableFuture.completedFuture(accumulated);
                }
                return collectContributorsPage(alarmName, token, accumulated);
            })
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to describe alarm contributors: "
                    + exception.getMessage(), exception);
            });
    }

    /**
     * Creates or updates an alarm mute rule. While a mute rule is active the targeted
     * alarms keep evaluating and keep changing state, but their configured actions do not
     * fire. This is the supported way to suppress notifications during planned
     * maintenance, instead of disabling alarm actions and relying on someone to turn them
     * back on.
     *
     * @param name       the name of the mute rule
     * @param expression when the rule activates. For a recurring window, a five-field
     *                   cron expression, {@code cron(Minutes Hours Day-of-month Month
     *                   Day-of-week)}, such as {@code cron(0 2 * * SUN)}. Note that this
     *                   is five fields, not the six that Amazon EventBridge uses. For a
     *                   one-time window, {@code at(yyyy-MM-ddThh:mm)}, such as
     *                   {@code at(2026-09-05T02:00)}, with no seconds.
     * @param duration   how long the window lasts once it activates, as an ISO 8601
     *                   duration from {@code PT1M} to {@code P15D}. For example,
     *                   {@code PT2H} is two hours. Plain forms such as {@code 2h} are
     *                   rejected.
     * @param timezone   a standard timezone identifier. Defaults to UTC when omitted.
     * @param alarmNames the names of up to 100 alarms to mute. If empty, the rule applies
     *                   to every alarm in the account.
     * @return a {@link CompletableFuture} that completes when the rule is written
     */
    public CompletableFuture<Void> putAlarmMuteRuleAsync(String name, String expression,
            String duration, String timezone, List<String> alarmNames) {
        Schedule schedule = Schedule.builder()
            .expression(expression)
            .duration(duration)
            .timezone(timezone)
            .build();

        PutAlarmMuteRuleRequest.Builder request = PutAlarmMuteRuleRequest.builder()
            .name(name)
            .description("Mute rule created by the AWS SDK for Java 2.x Basics scenario.")
            .rule(Rule.builder().schedule(schedule).build());

        if (alarmNames != null && !alarmNames.isEmpty()) {
            request.muteTargets(MuteTargets.builder().alarmNames(alarmNames).build());
        }

        return getAsyncClient().putAlarmMuteRule(request.build()).handle((response, exception) -> {
            if (exception != null) {
                throw new RuntimeException("Failed to put alarm mute rule: "
                    + exception.getMessage(), exception);
            }
            logger.info("Put alarm mute rule {}.", name);
            return null;
        });
    }

    /**
     * Gets the full configuration of an alarm mute rule, including its schedule, the
     * alarms it targets, and its current status.
     *
     * @param name the name of the mute rule
     * @return a {@link CompletableFuture} that completes with the mute rule
     */
    public CompletableFuture<GetAlarmMuteRuleResponse> getAlarmMuteRuleAsync(String name) {
        return getAsyncClient().getAlarmMuteRule(GetAlarmMuteRuleRequest.builder()
                .alarmMuteRuleName(name)
                .build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to get alarm mute rule: "
                        + exception.getMessage(), exception);
                }
                return response;
            });
    }

    /**
     * Lists the alarm mute rules in the account, optionally filtered to the rules that
     * target one alarm.
     *
     * <p>Note that {@link AlarmMuteRuleSummary} carries no name field, only an ARN,
     * status, mute type, and last-updated timestamp. To find a rule by name, match on the
     * ARN suffix.
     *
     * @param alarmName when non-null, only rules that target this alarm are returned
     * @return a {@link CompletableFuture} that completes with the mute rule summaries
     */
    public CompletableFuture<List<AlarmMuteRuleSummary>> listAlarmMuteRulesAsync(String alarmName) {
        List<AlarmMuteRuleSummary> summaries = new ArrayList<>();
        return collectMuteRulesPage(alarmName, null, summaries);
    }

    private CompletableFuture<List<AlarmMuteRuleSummary>> collectMuteRulesPage(String alarmName,
            String nextToken, List<AlarmMuteRuleSummary> accumulated) {
        ListAlarmMuteRulesRequest request = ListAlarmMuteRulesRequest.builder()
            .alarmName(alarmName)
            .nextToken(nextToken)
            .build();

        return getAsyncClient().listAlarmMuteRules(request)
            .thenCompose(response -> {
                accumulated.addAll(response.alarmMuteRuleSummaries());
                String token = response.nextToken();
                if (token == null || token.isEmpty()) {
                    return CompletableFuture.completedFuture(accumulated);
                }
                return collectMuteRulesPage(alarmName, token, accumulated);
            })
            .exceptionally(exception -> {
                throw new RuntimeException("Failed to list alarm mute rules: "
                    + exception.getMessage(), exception);
            });
    }

    /**
     * Deletes an alarm mute rule. The alarms it targeted resume firing their actions.
     *
     * @param name the name of the mute rule
     * @return a {@link CompletableFuture} that completes when the rule is deleted
     */
    public CompletableFuture<Void> deleteAlarmMuteRuleAsync(String name) {
        return getAsyncClient().deleteAlarmMuteRule(DeleteAlarmMuteRuleRequest.builder()
                .alarmMuteRuleName(name)
                .build())
            .handle((response, exception) -> {
                if (exception != null) {
                    throw new RuntimeException("Failed to delete alarm mute rule: "
                        + exception.getMessage(), exception);
                }
                logger.info("Deleted alarm mute rule {}.", name);
                return null;
            });
    }

    public static String readFileAsString(String file) throws IOException {
        return new String(Files.readAllBytes(Paths.get(file)));
    }
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteAlarms)
  + [DeleteDashboards](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DeleteDashboards)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetDashboard](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetDashboard)
  + [GetMetricStatistics](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricStatistics)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListAlarmMuteRules)
  + [ListDashboards](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListDashboards)
  + [ListMetrics](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/ListMetrics)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutDashboard](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutDashboard)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StopOTelEnrichment)

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cloudwatch#code-examples). 
Run an interactive scenario demonstrating the CloudWatch OpenTelemetry experience.  

```
import {
  Scenario,
  ScenarioAction,
  ScenarioInput,
  ScenarioOutput,
} from "@aws-doc-sdk-examples/lib/scenario/index.js";
import {
  CloudWatchClient,
  DeleteAlarmMuteRuleCommand,
  DeleteAlarmsCommand,
  DeleteDashboardsCommand,
  DescribeAlarmContributorsCommand,
  GetAlarmMuteRuleCommand,
  GetDashboardCommand,
  GetMetricStatisticsCommand,
  GetOTelEnrichmentCommand,
  ListAlarmMuteRulesCommand,
  ListMetricsCommand,
  PutAlarmMuteRuleCommand,
  PutDashboardCommand,
  PutMetricAlarmCommand,
  StartOTelEnrichmentCommand,
  StopOTelEnrichmentCommand,
} from "@aws-sdk/client-cloudwatch";
import { parseArgs } from "node:util";
import { fileURLToPath } from "node:url";

const DEFAULT_QUERY = "avg by (host) (system_cpu_utilization) > 80";

// Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
const EVALUATION_INTERVAL = 60;
const PENDING_PERIOD = 300;
const RECOVERY_PERIOD = 120;

/**
 * @typedef {{
 *   client: import('@aws-sdk/client-cloudwatch').CloudWatchClient,
 *   alarmName: string,
 *   dashboardName: string,
 *   muteRuleName: string,
 *   namespaces: [string, number][],
 *   metric: import('@aws-sdk/client-cloudwatch').Metric | undefined,
 *   query: string,
 *   startedEnrichment: boolean,
 *   dashboardCreated: boolean,
 *   deleteResources: boolean,
 * }} State
 */

/**
 * Used repeatedly to have the user press enter.
 * @type {ScenarioInput}
 */
const pressEnter = new ScenarioInput("continue", "Press Enter to continue", {
  type: "confirm",
});

const greet = new ScenarioOutput(
  "greet",
  `Welcome to the Amazon CloudWatch Basics scenario.

CloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through that experience: it turns on OTel enrichment so CloudWatch can correlate incoming OTLP metrics with the resources that produced them, alarms on those metrics with a PromQL query, and shows you which individual series drove the alarm.

A PromQL alarm works differently from a classic metric alarm. Rather than watching one metric and counting breaching periods, it evaluates a query that can match many series at once, and tracks each one separately as a contributor.

Note that sending OTLP metrics to CloudWatch is not an AWS SDK operation. Metrics arrive over the OTLP protocol through the CloudWatch agent, an OpenTelemetry Collector, or an ADOT SDK. Everything this scenario does is configuration and querying around that ingestion path.

Let's get started...`,
  { header: true },
);

// Step 1: List metrics and namespaces. This orients the reader before any configuration
// happens.
const displayListMetrics = new ScenarioOutput(
  "displayListMetrics",
  "1. List metrics and namespaces\n\nBefore configuring anything, let's see what CloudWatch is already collecting in this account by calling ListMetrics.",
);

const sdkListMetrics = new ScenarioAction(
  "sdkListMetrics",
  async (/** @type {State} */ state) => {
    const counts = new Map();
    let metricCount = 0;
    let nextToken;

    do {
      const response = await state.client.send(
        new ListMetricsCommand({ NextToken: nextToken }),
      );
      for (const metric of response.Metrics ?? []) {
        counts.set(metric.Namespace, (counts.get(metric.Namespace) ?? 0) + 1);
        metricCount += 1;
        // Keep the first metric we see so later steps have something to chart.
        if (!state.metric) {
          state.metric = metric;
        }
      }
      nextToken = response.NextToken;
      // This account may have a very large number of metrics, so stop once we have
      // enough to give the reader a sense of what is there.
    } while (nextToken && metricCount < 500);

    state.namespaces = [...counts.entries()].sort((a, b) => b[1] - a[1]);

    console.log(
      `\tFound ${metricCount} metrics across ${state.namespaces.length} namespaces:`,
    );
    for (const [namespace, count] of state.namespaces.slice(0, 10)) {
      console.log(`\t  ${namespace} (${count} metrics)`);
    }
    if (state.namespaces.length === 0) {
      console.log(
        "\tNo metrics found in this account. The statistics and dashboard steps later on need an existing metric, so they will be skipped.",
      );
    }
  },
);

// Step 2: Start OTel enrichment. Enrichment is what makes CloudWatch attach AWS resource
// context to incoming OTLP metrics.
const displayStartEnrichment = new ScenarioOutput(
  "displayStartEnrichment",
  "2. Start OpenTelemetry enrichment\n\nEnrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics you send it. Without it, your metrics arrive as opaque series with no connection to the resources that emitted them.\n\nWe check the current state first, and only start enrichment if it isn't already on.",
);

const sdkStartEnrichment = new ScenarioAction(
  "sdkStartEnrichment",
  async (/** @type {State} */ state) => {
    const { Status } = await state.client.send(
      new GetOTelEnrichmentCommand({}),
    );
    console.log(`\tEnrichment status: ${Status}`);

    if (Status === "Running") {
      console.log(
        "\n\tEnrichment was already running, so we will leave it alone. The cleanup step will not stop it, because other workloads in this account may depend on it.",
      );
      return;
    }

    await state.client.send(new StartOTelEnrichmentCommand({}));
    // Record that *this run* started enrichment, so cleanup only stops what it turned on.
    state.startedEnrichment = true;

    const after = await state.client.send(new GetOTelEnrichmentCommand({}));
    console.log(`\tEnrichment status: ${after.Status}`);
    console.log(
      "\n\tNote: this run started enrichment, so the cleanup step will stop it again.",
    );
  },
);

// Step 3: Explain OTLP ingestion. This step makes no service call; naming the gap
// explicitly is the point.
const displayOtlpIngestion = new ScenarioOutput(
  "displayOtlpIngestion",
  `3. Send OTLP metrics to CloudWatch

This step is not an AWS SDK operation, and that's worth being explicit about. Metrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an OpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call.

Point your collector at the CloudWatch metrics endpoint, which follows the pattern
\thttps://monitoring.<region>.amazonaws.com/v1/metrics

The endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp exporter rather than otlp. The metrics endpoint signs as "monitoring".`,
);

// Step 4: Create a PromQL alarm.
const displayCreateAlarm = new ScenarioOutput(
  "displayCreateAlarm",
  "4. Create a PromQL alarm\n\nNow we alarm on those metrics. The comparison goes inside the query itself: a PromQL alarm has no separate threshold, comparison operator, statistic, or period.",
);

const inputQuery = new ScenarioInput("query", "Enter a PromQL query:", {
  type: "input",
  default: DEFAULT_QUERY,
});

const sdkCreateAlarm = new ScenarioAction(
  "sdkCreateAlarm",
  async (/** @type {State} */ state) => {
    const query = state.query?.trim() || DEFAULT_QUERY;
    state.query = query;

    // EvaluationCriteria is a union and is mutually exclusive with the classic MetricName
    // and Metrics parameters. When you use it you must also set EvaluationInterval, and
    // you must not set Period, Statistic, Threshold, ComparisonOperator,
    // EvaluationPeriods, DatapointsToAlarm, or TreatMissingData.
    await state.client.send(
      new PutMetricAlarmCommand({
        AlarmName: state.alarmName,
        AlarmDescription:
          "A PromQL alarm created by the AWS SDK for JavaScript Basics scenario.",
        EvaluationCriteria: {
          PromQLCriteria: {
            Query: query,
            PendingPeriod: PENDING_PERIOD,
            RecoveryPeriod: RECOVERY_PERIOD,
          },
        },
        EvaluationInterval: EVALUATION_INTERVAL,
        ActionsEnabled: false,
      }),
    );

    console.log(`\tCreated alarm ${state.alarmName}:`);
    console.log(`\t  query:              ${query}`);
    console.log(`\t  evaluationInterval: ${EVALUATION_INTERVAL} seconds`);
    console.log(`\t  pendingPeriod:      ${PENDING_PERIOD} seconds`);
    console.log(`\t  recoveryPeriod:     ${RECOVERY_PERIOD} seconds`);
    console.log(
      "\n\tA PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is another way it differs from a classic alarm.",
    );
  },
);

// Step 5: Inspect the alarm's contributors. This is the step with no classic-alarm
// equivalent.
const displayContributors = new ScenarioOutput(
  "displayContributors",
  "5. Inspect the alarm's contributors\n\nEach contributor is one series the query matched, identified by its label set. This is how you find out which host is unhealthy rather than only that something is. Classic alarms have no equivalent.",
);

const sdkContributors = new ScenarioAction(
  "sdkContributors",
  async (/** @type {State} */ state) => {
    const contributors = [];
    let nextToken;

    do {
      const response = await state.client.send(
        new DescribeAlarmContributorsCommand({
          AlarmName: state.alarmName,
          NextToken: nextToken,
        }),
      );
      contributors.push(...(response.AlarmContributors ?? []));
      nextToken = response.NextToken;
      // A page can come back empty while still carrying a token, so keep going until the
      // token itself is gone rather than stopping at the first empty page.
    } while (nextToken);

    if (contributors.length === 0) {
      console.log(
        "\tNo contributors yet. The query matched no series, which usually means no OTel metrics with these labels have arrived. Once your collector is sending data, each matching series appears here with its labels and the reason it breached.",
      );
      return;
    }

    console.log(`\tFound ${contributors.length} contributors:`);
    for (const contributor of contributors) {
      const labels = Object.entries(contributor.ContributorAttributes ?? {})
        .sort(([a], [b]) => a.localeCompare(b))
        .map(([key, value]) => `${key}=${value}`)
        .join(", ");
      console.log(`\t  ${contributor.ContributorId}: ${labels}`);
      console.log(`\t    reason: ${contributor.StateReason}`);
    }
  },
);

// Step 6: Get statistics and chart the metric on a dashboard.
const displayDashboard = new ScenarioOutput(
  "displayDashboard",
  "6. Get statistics and chart the metric on a dashboard\n\nStatistics and dashboards are how you see what the alarm is evaluating.",
);

const sdkDashboard = new ScenarioAction(
  "sdkDashboard",
  async (/** @type {State} */ state) => {
    if (!state.metric) {
      console.log(
        "\tSkipping statistics and dashboard because no metrics exist yet.",
      );
      return;
    }

    const metric = state.metric;
    const stats = await state.client.send(
      new GetMetricStatisticsCommand({
        Namespace: metric.Namespace,
        MetricName: metric.MetricName,
        Dimensions: metric.Dimensions,
        StartTime: new Date(Date.now() - 24 * 60 * 60 * 1000),
        EndTime: new Date(),
        Period: 3600,
        Statistics: ["Average", "Maximum"],
      }),
    );

    const datapoints = stats.Datapoints ?? [];
    console.log(
      `\tStatistics for ${metric.Namespace} ${metric.MetricName} over the last day:`,
    );
    console.log(`\t  Datapoints: ${datapoints.length}`);
    for (const datapoint of datapoints.slice(0, 3)) {
      console.log(
        `\t  ${datapoint.Timestamp?.toISOString()} average ${datapoint.Average}, maximum ${datapoint.Maximum}`,
      );
    }

    const region = await state.client.config.region();
    const response = await state.client.send(
      new PutDashboardCommand({
        DashboardName: state.dashboardName,
        DashboardBody: buildDashboardBody(metric, region),
      }),
    );
    state.dashboardCreated = true;

    for (const message of response.DashboardValidationMessages ?? []) {
      console.log(`\tDashboard validation message: ${message.Message}`);
    }
    console.log(`\tCreated dashboard ${state.dashboardName}.`);

    const stored = await state.client.send(
      new GetDashboardCommand({ DashboardName: state.dashboardName }),
    );
    console.log(
      `\tRead the dashboard back, ${stored.DashboardBody?.length} characters of widget JSON.`,
    );
  },
);

/**
 * Build a single-widget dashboard body that charts the given metric.
 * @param {import('@aws-sdk/client-cloudwatch').Metric} metric
 * @param {string} region The region the metric is in. A metric widget must name
 *   its region, because a dashboard can chart metrics from several.
 * @returns {string} The dashboard body, as JSON.
 */
const buildDashboardBody = (metric, region) => {
  const metricSpec = [metric.Namespace, metric.MetricName];
  for (const dimension of metric.Dimensions ?? []) {
    metricSpec.push(dimension.Name, dimension.Value);
  }

  return JSON.stringify({
    widgets: [
      {
        type: "text",
        x: 0,
        y: 0,
        width: 24,
        height: 2,
        properties: {
          markdown:
            "This dashboard was created programmatically by an AWS SDK code example.",
        },
      },
      {
        type: "metric",
        x: 0,
        y: 2,
        width: 12,
        height: 6,
        properties: {
          metrics: [metricSpec],
          view: "timeSeries",
          stat: "Average",
          period: 300,
          region,
          title: metric.MetricName,
        },
      },
    ],
  });
};

// Step 7: Mute the alarm for a maintenance window.
const displayMuteRule = new ScenarioOutput(
  "displayMuteRule",
  "7. Mute the alarm for a maintenance window\n\nWhile a mute rule is active the targeted alarms keep evaluating and keep changing state, but their actions do not fire. This is the supported way to suppress notifications during planned maintenance, instead of disabling alarm actions and hoping someone remembers to turn them back on.",
);

const sdkMuteRule = new ScenarioAction(
  "sdkMuteRule",
  async (/** @type {State} */ state) => {
    // The expression is a five-field cron expression,
    // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields,
    // not the six that Amazon EventBridge uses. For a one-time window, use
    // at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration from
    // PT1M to P15D, so PT2H rather than 2h.
    const expression = "cron(0 2 * * SUN)";
    const duration = "PT2H";
    const timezone = "America/Los_Angeles";

    await state.client.send(
      new PutAlarmMuteRuleCommand({
        Name: state.muteRuleName,
        Description:
          "A mute rule created by the AWS SDK for JavaScript Basics scenario.",
        Rule: {
          Schedule: {
            Expression: expression,
            Duration: duration,
            Timezone: timezone,
          },
        },
        // Target up to 100 alarms. If MuteTargets is omitted, the rule applies to every
        // alarm in the account.
        MuteTargets: { AlarmNames: [state.alarmName] },
      }),
    );

    console.log(`\tCreated mute rule ${state.muteRuleName}:`);
    console.log(`\t  schedule: ${expression} for ${duration}`);
    console.log(`\t  timezone: ${timezone}`);
    console.log(`\t  targets:  ${state.alarmName}`);
    console.log(
      "\n\tNote the two formats here. The expression is a five-field cron expression, five rather than the six Amazon EventBridge uses. The duration is an ISO 8601 duration, so 'PT2H' and not '2h'.",
    );
    console.log(
      "\n\tAlso note that MuteTargets is set explicitly. If you leave it out, the rule applies to every alarm in the account.",
    );

    const rule = await state.client.send(
      new GetAlarmMuteRuleCommand({ AlarmMuteRuleName: state.muteRuleName }),
    );
    console.log(
      `\tRead the rule back: status ${rule.Status}, mute type ${rule.MuteType}.`,
    );

    const summaries = [];
    let nextToken;
    do {
      const response = await state.client.send(
        new ListAlarmMuteRulesCommand({
          AlarmName: state.alarmName,
          NextToken: nextToken,
        }),
      );
      summaries.push(...(response.AlarmMuteRuleSummaries ?? []));
      nextToken = response.NextToken;
    } while (nextToken);

    console.log(`\tFound ${summaries.length} mute rules targeting this alarm.`);
    // Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
    const match = summaries.find(
      (summary) =>
        summary.AlarmMuteRuleArn?.endsWith(`/${state.muteRuleName}`) ||
        summary.AlarmMuteRuleArn?.endsWith(`:${state.muteRuleName}`),
    );
    if (match) {
      console.log(
        `\t  matched by ARN: ${match.AlarmMuteRuleArn} (${match.Status})`,
      );
    }
  },
);

// Step 8: Clean up.
const askToDeleteResources = new ScenarioInput(
  "deleteResources",
  "8. Clean up\n\nDelete the resources this scenario created?",
  { type: "confirm" },
);

const displaySkipCleanUp = new ScenarioOutput(
  "displaySkipCleanUp",
  "\tSkipping cleanup. Note that the alarm, dashboard, and mute rule are still in your account, and enrichment may still be running.",
  { skipWhen: (/** @type {State} */ state) => state.deleteResources },
);

const sdkCleanUp = new ScenarioAction(
  "sdkCleanUp",
  async (/** @type {State} */ state) => {
    // Each deletion is attempted independently so that one failure does not leave the
    // remaining resources behind.
    try {
      await state.client.send(
        new DeleteAlarmMuteRuleCommand({
          AlarmMuteRuleName: state.muteRuleName,
        }),
      );
      console.log(`\tDeleted mute rule ${state.muteRuleName}.`);
    } catch (caught) {
      console.log(`\tCould not delete the mute rule: ${caught.message}`);
    }

    try {
      await state.client.send(
        new DeleteAlarmsCommand({ AlarmNames: [state.alarmName] }),
      );
      console.log(`\tDeleted alarm ${state.alarmName}.`);
    } catch (caught) {
      console.log(`\tCould not delete the alarm: ${caught.message}`);
    }

    if (state.dashboardCreated) {
      try {
        await state.client.send(
          new DeleteDashboardsCommand({
            DashboardNames: [state.dashboardName],
          }),
        );
        console.log(`\tDeleted dashboard ${state.dashboardName}.`);
      } catch (caught) {
        console.log(`\tCould not delete the dashboard: ${caught.message}`);
      }
    }

    if (!state.startedEnrichment) {
      console.log(
        "\tLeft OTel enrichment running, because it was already on before this run.",
      );
      return;
    }

    try {
      await state.client.send(new StopOTelEnrichmentCommand({}));
      console.log("\tStopped OTel enrichment, because this run started it.");
    } catch (caught) {
      console.log(`\tCould not stop OTel enrichment: ${caught.message}`);
    }
  },
  { skipWhen: (/** @type {State} */ state) => !state.deleteResources },
);

const goodbye = new ScenarioOutput(
  "goodbye",
  "This concludes the Amazon CloudWatch Basics scenario.",
);

// Suffix the resource names so repeated runs do not collide.
const suffix = Math.floor(Math.random() * 9000) + 1000;

const myScenario = new Scenario(
  "CloudWatch Basics",
  [
    greet,
    pressEnter,
    displayListMetrics,
    sdkListMetrics,
    pressEnter,
    displayStartEnrichment,
    sdkStartEnrichment,
    pressEnter,
    displayOtlpIngestion,
    pressEnter,
    displayCreateAlarm,
    inputQuery,
    sdkCreateAlarm,
    pressEnter,
    displayContributors,
    sdkContributors,
    pressEnter,
    displayDashboard,
    sdkDashboard,
    pressEnter,
    displayMuteRule,
    sdkMuteRule,
    pressEnter,
    askToDeleteResources,
    displaySkipCleanUp,
    sdkCleanUp,
    goodbye,
  ],
  {
    client: new CloudWatchClient({}),
    alarmName: `doc-example-promql-alarm-${suffix}`,
    dashboardName: `doc-example-dashboard-${suffix}`,
    muteRuleName: `doc-example-mute-rule-${suffix}`,
    namespaces: [],
    metric: undefined,
    startedEnrichment: false,
    dashboardCreated: false,
  },
);

/** @type {{ stepHandlerOptions: StepHandlerOptions }} */
export const main = async (stepHandlerOptions) => {
  await myScenario.run(stepHandlerOptions);
};

// Invoke main function if this file was run directly.
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const { values } = parseArgs({
    options: {
      yes: {
        type: "boolean",
        short: "y",
      },
    },
  });
  main({ confirmAll: values.yes });
}
```
+ For API details, see the following topics in *AWS SDK for JavaScript API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/DeleteAlarmMuteRuleCommand)
  + [DeleteAlarms](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/DeleteAlarmsCommand)
  + [DeleteDashboards](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/DeleteDashboardsCommand)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/DescribeAlarmContributorsCommand)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/GetAlarmMuteRuleCommand)
  + [GetDashboard](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/GetDashboardCommand)
  + [GetMetricStatistics](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/GetMetricStatisticsCommand)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/GetOTelEnrichmentCommand)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/ListAlarmMuteRulesCommand)
  + [ListDashboards](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/ListDashboardsCommand)
  + [ListMetrics](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/ListMetricsCommand)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/PutAlarmMuteRuleCommand)
  + [PutDashboard](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/PutDashboardCommand)
  + [PutMetricAlarm](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/PutMetricAlarmCommand)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/StartOTelEnrichmentCommand)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch/command/StopOTelEnrichmentCommand)

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/cloudwatch#code-examples). 
Run an interactive scenario demonstrating the CloudWatch OpenTelemetry experience.  

```
/**
 Before running this Kotlin code example, set up your development environment,
 including your credentials.

 For more information, see the following documentation topic:
 https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html

 This scenario demonstrates the Amazon CloudWatch OpenTelemetry (OTel) experience.
 CloudWatch ingests OpenTelemetry metrics natively, and this example walks through what
 you do with them: turning on enrichment so CloudWatch can correlate incoming OTLP
 metrics with the resources that produced them, alarming on those metrics with a PromQL
 query, and finding out which individual series drove the alarm.

 A PromQL alarm works differently from a classic metric alarm. Rather than watching one
 metric and counting breaching periods, it evaluates a query that can match many series
 at once, and tracks each matching series separately as a contributor.

 Note that sending OTLP metrics to CloudWatch is not an AWS SDK operation. Metrics
 arrive over the OTLP protocol through the CloudWatch agent, an OpenTelemetry
 Collector, or an ADOT SDK. Everything this scenario does is configuration and querying
 around that ingestion path.

 This Kotlin code example performs the following tasks:

 1. List metrics and namespaces from Amazon CloudWatch.
 2. Start OpenTelemetry enrichment for the account.
 3. Explain how OTLP metrics reach CloudWatch.
 4. Create an alarm that evaluates a PromQL query.
 5. Inspect the contributors to the PromQL alarm.
 6. Get metric statistics and chart the metric on a dashboard.
 7. Mute the alarm for a maintenance window.
 8. Clean up the Amazon CloudWatch resources.
 */

val DASHES: String = "-".repeat(80)

private const val REGION = "us-east-1"

private const val DEFAULT_QUERY = "avg by (host) (system_cpu_utilization) > 80"

// Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
private const val EVALUATION_INTERVAL = 60
private const val PENDING_PERIOD = 300
private const val RECOVERY_PERIOD = 120

val scenarioScanner = Scanner(System.`in`)

suspend fun main() {
    // Suffix the resource names so repeated runs do not collide.
    val suffix = (Random().nextInt(9000) + 1000).toString()
    val alarmName = "doc-example-promql-alarm-$suffix"
    val dashboardName = "doc-example-dashboard-$suffix"
    val muteRuleName = "doc-example-mute-rule-$suffix"

    println(DASHES)
    println("Welcome to the Amazon CloudWatch Basics scenario.")
    println(
        """
        CloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through
        that experience: it turns on OTel enrichment so CloudWatch can correlate incoming
        OTLP metrics with the resources that produced them, alarms on those metrics with a
        PromQL query, and shows you which individual series drove the alarm.

        A PromQL alarm works differently from a classic metric alarm. Rather than watching
        one metric and counting breaching periods, it evaluates a query that can match many
        series at once, and tracks each one separately as a contributor.

        Let's get started...
        """.trimIndent(),
    )
    waitForInputToContinue()

    // Tracks whether this run turned enrichment on, so that cleanup only turns off
    // enrichment that this run started.
    var startedEnrichment = false
    var dashboardCreated = false

    println(DASHES)
    println(
        """
        1. List metrics and namespaces

        Before configuring anything, let's see what CloudWatch is already collecting in
        this account by calling ListMetrics.
        """.trimIndent(),
    )
    waitForInputToContinue()

    val namespaces = listNameSpaces()
    println("Found ${namespaces.size} namespaces in this account:")
    namespaces.take(10).forEach { println("  $it") }
    if (namespaces.isEmpty()) {
        println(
            """
            No metrics found in this account. The statistics and dashboard steps later on
            need an existing metric, so they will be skipped.
            """.trimIndent(),
        )
    }
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        2. Start OpenTelemetry enrichment

        Enrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics
        you send it. Without it, your metrics arrive as opaque series with no connection to
        the resources that emitted them.

        We check the current state first, and only start enrichment if it isn't already on.
        """.trimIndent(),
    )
    waitForInputToContinue()

    val status = getOTelEnrichmentStatus()
    if (status !is OTelEnrichmentStatus.Running) {
        // Record the attempt before making it. We already know enrichment was not running, so
        // stopping it during cleanup is always safe, and a start that succeeds but fails to
        // report back would otherwise leave it running.
        startedEnrichment = true
        startOTelEnrichment()

        val newStatus = getOTelEnrichmentStatus()
        println(
            "Note: this run started enrichment (status is now ${newStatus?.value}), so the " +
                "cleanup step will stop it again.",
        )
    } else {
        println(
            """
            Enrichment was already running, so we will leave it alone. The cleanup step
            will not stop it, because other workloads in this account may depend on it.
            """.trimIndent(),
        )
    }
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        3. Send OTLP metrics to CloudWatch

        This step is not an AWS SDK operation, and that's worth being explicit about.
        Metrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an
        OpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call.

        Point your collector at the CloudWatch metrics endpoint, which follows the pattern
        https://monitoring.<region>.amazonaws.com/v1/metrics

        The endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp
        exporter rather than otlp. The metrics endpoint signs as "monitoring".
        """.trimIndent(),
    )
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        4. Create a PromQL alarm

        Now we alarm on those metrics. The comparison goes inside the query itself: a
        PromQL alarm has no separate threshold, comparison operator, statistic, or period.
        """.trimIndent(),
    )
    println("Enter a PromQL query, or press <ENTER> for the default")
    println("[$DEFAULT_QUERY]:")
    val queryInput = scenarioScanner.nextLine()
    val query = if (queryInput.isBlank()) DEFAULT_QUERY else queryInput.trim()

    putPromQlMetricAlarm(alarmName, query, EVALUATION_INTERVAL, PENDING_PERIOD, RECOVERY_PERIOD)
    println("Created alarm $alarmName:")
    println("  query:              $query")
    println("  evaluationInterval: $EVALUATION_INTERVAL seconds")
    println("  pendingPeriod:      $PENDING_PERIOD seconds")
    println("  recoveryPeriod:     $RECOVERY_PERIOD seconds")
    println(
        """
        A PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is
        another way it differs from a classic alarm.
        """.trimIndent(),
    )
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        5. Inspect the alarm's contributors

        Each contributor is one series the query matched, identified by its label set. This
        is how you find out which host is unhealthy rather than only that something is.
        Classic alarms have no equivalent.
        """.trimIndent(),
    )
    waitForInputToContinue()

    describeAlarmContributors(alarmName)
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        6. Get statistics and chart the metric on a dashboard

        Statistics and dashboards are how you see what the alarm is evaluating.
        """.trimIndent(),
    )
    waitForInputToContinue()

    if (namespaces.isNotEmpty()) {
        val namespace = namespaces[0]
        val metrics = listMets(namespace)
        if (metrics != null && metrics.isNotEmpty()) {
            val metricName = metrics[0]
            val startDate = Instant.now().minus(24, ChronoUnit.HOURS).toString()
            var dimension: Dimension? = null
            try {
                dimension = getSpecificMet(namespace)
                if (dimension != null) {
                    getAndDisplayMetricStatistics(namespace, metricName, "Average", startDate, dimension)
                }
            } catch (e: Exception) {
                println("Could not get statistics for $namespace/$metricName: ${e.message}")
            }

            // Chart the metric this run just discovered. Reading the widgets from a file
            // would chart metrics that may not exist in this account.
            try {
                createDashboard(dashboardName, buildDashboardBody(namespace, metricName, dimension, REGION))
                dashboardCreated = true
                listDashboards()
            } catch (e: Exception) {
                println("Could not create the dashboard: ${e.message}")
            }
        } else {
            println("No metrics found in namespace $namespace, skipping statistics and the dashboard.")
        }
    } else {
        println("Skipping statistics and dashboard because no metrics exist yet.")
    }
    waitForInputToContinue()

    println(DASHES)
    println(
        """
        7. Mute the alarm for a maintenance window

        While a mute rule is active the targeted alarms keep evaluating and keep changing
        state, but their actions do not fire. This is the supported way to suppress
        notifications during planned maintenance, instead of disabling alarm actions and
        hoping someone remembers to turn them back on.
        """.trimIndent(),
    )
    waitForInputToContinue()

    // The expression is a five-field cron expression,
    // cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields,
    // not the six that Amazon EventBridge uses. For a one-time window, use
    // at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration from
    // PT1M to P15D, so PT2H rather than 2h.
    val expression = "cron(0 2 * * SUN)"
    val duration = "PT2H"
    val timezone = "America/Los_Angeles"

    putAlarmMuteRule(muteRuleName, expression, duration, listOf(alarmName), timezone)
    println("Created mute rule $muteRuleName:")
    println("  schedule: $expression for $duration")
    println("  timezone: $timezone")
    println("  targets:  $alarmName")
    println(
        """
        Note the two formats here. The expression is a five-field cron expression, five
        rather than the six Amazon EventBridge uses. The duration is an ISO 8601 duration,
        so 'PT2H' and not '2h'.

        Also note that muteTargets is set explicitly. If you leave it out, the rule applies
        to every alarm in the account.
        """.trimIndent(),
    )

    val muteRule = getAlarmMuteRule(muteRuleName)
    println("Read the rule back: status ${muteRule.status?.value}, mute type ${muteRule.muteType}.")

    val summaries = listAlarmMuteRules(alarmName)
    println("Found ${summaries.size} mute rules targeting this alarm.")
    // Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
    summaries
        .firstOrNull { summary ->
            summary.alarmMuteRuleArn?.endsWith("/$muteRuleName") == true ||
                summary.alarmMuteRuleArn?.endsWith(":$muteRuleName") == true
        }?.let { summary ->
            println("  matched by ARN: ${summary.alarmMuteRuleArn} (${summary.status?.value})")
        }
    waitForInputToContinue()

    println(DASHES)
    println("8. Clean up")
    println("Delete the resources this scenario created? (y/n)")
    val cleanUp = scenarioScanner.nextLine()
    if (!cleanUp.trim().equals("y", ignoreCase = true)) {
        println(
            """
            Skipping cleanup. Note that the alarm, dashboard, and mute rule are still in
            your account, and enrichment may still be running.
            """.trimIndent(),
        )
        println(DASHES)
        println("This concludes the Amazon CloudWatch Basics scenario.")
        return
    }

    // Each deletion is attempted independently so that one failure does not leave the
    // remaining resources behind.
    try {
        deleteAlarmMuteRule(muteRuleName)
    } catch (e: Exception) {
        println("Could not delete the mute rule: ${e.message}")
    }

    try {
        deleteAlarm(alarmName)
    } catch (e: Exception) {
        println("Could not delete the alarm: ${e.message}")
    }

    if (dashboardCreated) {
        try {
            deleteDashboard(dashboardName)
        } catch (e: Exception) {
            println("Could not delete the dashboard: ${e.message}")
        }
    }

    if (startedEnrichment) {
        try {
            stopOTelEnrichment()
            println("Stopped OTel enrichment, because this run started it.")
        } catch (e: Exception) {
            println("Could not stop OTel enrichment: ${e.message}")
        }
    } else {
        println("Left OTel enrichment running, because it was already on before this run.")
    }

    println(DASHES)
    println("This concludes the Amazon CloudWatch Basics scenario.")
    println(DASHES)
}

private fun waitForInputToContinue() {
    while (true) {
        println("")
        println("Press <ENTER> to continue:")
        val input = scenarioScanner.nextLine()
        if (input.trim().isEmpty()) {
            println("Continuing with the program...")
            println("")
            break
        }
        println("Invalid input. Please try again.")
    }
}

suspend fun deleteAlarm(alarmNameVal: String) {
    val request =
        DeleteAlarmsRequest {
            alarmNames = listOf(alarmNameVal)
        }

    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        cwClient.deleteAlarms(request)
        println("Successfully deleted alarm $alarmNameVal")
    }
}

suspend fun deleteDashboard(dashboardName: String) {
    val dashboardsRequest =
        DeleteDashboardsRequest {
            dashboardNames = listOf(dashboardName)
        }
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        cwClient.deleteDashboards(dashboardsRequest)
        println("$dashboardName was successfully deleted.")
    }
}

suspend fun listDashboards() {
    CloudWatchClient { region = "us-east-1" }.use { cwClient ->
        cwClient
            .listDashboardsPaginated({})
            .transform { it.dashboardEntries?.forEach { obj -> emit(obj) } }
            .collect { obj ->
                println("Name is ${obj.dashboardName}")
                println("Dashboard ARN is ${obj.dashboardArn}")
            }
    }
}

suspend fun createDashboard(
    dashboardNameVal: String,
    dashboardBodyVal: String,
) {
    val dashboardRequest =
        PutDashboardRequest {
            dashboardName = dashboardNameVal
            dashboardBody = dashboardBodyVal
        }

    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val response = cwClient.putDashboard(dashboardRequest)
        println("$dashboardNameVal was successfully created.")
        val messages = response.dashboardValidationMessages
        if (messages != null) {
            if (messages.isEmpty()) {
                println("There are no messages in the new Dashboard")
            } else {
                for (message in messages) {
                    println("Message is: ${message.message}")
                }
            }
        }
    }
}

/**
 * Builds a single-widget dashboard body that charts the given metric.
 *
 * A metric widget must name its Region, because a dashboard can chart metrics from several.
 */
fun buildDashboardBody(
    metricNamespace: String,
    metricName: String,
    dimension: Dimension?,
    region: String,
): String {
    val dimensionParts =
        if (dimension == null) "" else ", \"${dimension.name}\", \"${dimension.value}\""

    return """
        {
            "widgets": [
                {
                    "type": "text",
                    "x": 0, "y": 0, "width": 24, "height": 2,
                    "properties": {
                        "markdown": "This dashboard was created programmatically by an AWS SDK code example."
                    }
                },
                {
                    "type": "metric",
                    "x": 0, "y": 2, "width": 12, "height": 6,
                    "properties": {
                        "metrics": [[ "$metricNamespace", "$metricName"$dimensionParts ]],
                        "view": "timeSeries",
                        "stat": "Average",
                        "period": 300,
                        "region": "$region",
                        "title": "$metricName"
                    }
                }
            ]
        }
    """.trimIndent()
}

suspend fun getAndDisplayMetricStatistics(
    nameSpaceVal: String,
    metVal: String,
    metricOption: String,
    date: String,
    myDimension: Dimension,
) {
    val start = Instant.parse(date)
    val endDate = Instant.now()
    val statisticsRequest =
        GetMetricStatisticsRequest {
            endTime =
                aws.smithy.kotlin.runtime.time
                    .Instant(endDate)
            startTime =
                aws.smithy.kotlin.runtime.time
                    .Instant(start)
            dimensions = listOf(myDimension)
            metricName = metVal
            namespace = nameSpaceVal
            period = 86400
            statistics = listOf(Statistic.fromValue(metricOption))
        }

    CloudWatchClient { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.getMetricStatistics(statisticsRequest)
        val data = response.datapoints
        if (data != null) {
            if (data.isNotEmpty()) {
                for (datapoint in data) {
                    println("Timestamp: ${datapoint.timestamp} Maximum value: ${datapoint.maximum}")
                }
            } else {
                println("The returned data list is empty")
            }
        }
    }
}

suspend fun listMets(namespaceVal: String?): ArrayList<String>? {
    val metList = ArrayList<String>()
    val request =
        ListMetricsRequest {
            namespace = namespaceVal
        }
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val reponse = cwClient.listMetrics(request)
        reponse.metrics?.forEach { metrics ->
            val data = metrics.metricName
            if (!metList.contains(data)) {
                metList.add(data!!)
            }
        }
    }
    return metList
}

suspend fun getSpecificMet(namespaceVal: String?): Dimension? {
    val request =
        ListMetricsRequest {
            namespace = namespaceVal
        }
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val response = cwClient.listMetrics(request)
        val myList = response.metrics
        if (myList != null) {
            return myList[0].dimensions?.get(0)
        }
    }
    return null
}

suspend fun listNameSpaces(): ArrayList<String> {
    val nameSpaceList = ArrayList<String>()
    CloudWatchClient.fromEnvironment { region = REGION }.use { cwClient ->
        val response = cwClient.listMetrics(ListMetricsRequest {})
        response.metrics?.forEach { metrics ->
            val data = metrics.namespace
            if (!nameSpaceList.contains(data)) {
                nameSpaceList.add(data!!)
            }
        }
    }
    return nameSpaceList
}
```
The OpenTelemetry functions that the scenario calls.  

```
suspend fun getOTelEnrichmentStatus(): OTelEnrichmentStatus? {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response = cwClient.getOTelEnrichment(GetOTelEnrichmentRequest {})
        val status = response.status
        when (status) {
            is OTelEnrichmentStatus.Running ->
                println("OTel enrichment is running. Vended metrics are queryable with PromQL")
            is OTelEnrichmentStatus.Stopped ->
                println("OTel enrichment is stopped. Start it to enrich vended metrics")
            else -> println("OTel enrichment status is ${status?.value}")
        }
        return status
    }
}

suspend fun startOTelEnrichment() {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.startOTelEnrichment(StartOTelEnrichmentRequest {})
        println("Successfully started OTel enrichment for this account")
    }
}

suspend fun putPromQlMetricAlarm(
    alarmNameVal: String,
    queryVal: String,
    evaluationIntervalVal: Int = 60,
    pendingPeriodVal: Int = 300,
    recoveryPeriodVal: Int = 120,
) {
    // The comparison belongs in the query itself. A PromQL alarm has no separate
    // threshold, comparison operator, statistic, period, or evaluation periods.
    //
    // Note that the Kotlin SDK spells this AlarmPromQlCriteria, with a lowercase l in
    // "Ql". Every other AWS SDK spells it PromQL, so don't be thrown by the difference
    // when comparing this example against the other language versions.
    val promQlCriteria =
        AlarmPromQlCriteria {
            query = queryVal
            pendingPeriod = pendingPeriodVal
            recoveryPeriod = recoveryPeriodVal
        }

    // EvaluationCriteria is a union and is mutually exclusive with the classic
    // metricName and metrics parameters. When you use it, you must also set
    // evaluationInterval.
    val request =
        PutMetricAlarmRequest {
            alarmName = alarmNameVal
            alarmDescription = "A PromQL alarm created by the Kotlin SDK"
            evaluationCriteria = EvaluationCriteria.PromQlCriteria(promQlCriteria)
            evaluationInterval = evaluationIntervalVal
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.putMetricAlarm(request)
        println("Successfully created PromQL alarm $alarmNameVal for query $queryVal")
    }
}

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

suspend fun getAlarmMuteRule(muteRuleName: String): GetAlarmMuteRuleResponse {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        val response =
            cwClient.getAlarmMuteRule(
                GetAlarmMuteRuleRequest {
                    alarmMuteRuleName = muteRuleName
                },
            )

        println("Mute rule ${response.name} is ${response.status?.value}")
        println("  ARN: ${response.alarmMuteRuleArn}")
        println("  schedule: ${response.rule?.schedule?.expression} for ${response.rule?.schedule?.duration}")
        response.muteTargets?.alarmNames?.let { println("  muted alarms: ${it.joinToString(", ")}") }
        return response
    }
}

suspend fun listAlarmMuteRules(alarmNameVal: String? = null): List<AlarmMuteRuleSummary> {
    val summaries = mutableListOf<AlarmMuteRuleSummary>()

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        var token: String? = null
        do {
            val response =
                cwClient.listAlarmMuteRules(
                    ListAlarmMuteRulesRequest {
                        alarmName = alarmNameVal
                        nextToken = token
                    },
                )

            response.alarmMuteRuleSummaries?.let { summaries.addAll(it) }
            token = response.nextToken
        } while (token != null)

        summaries.forEach { summary ->
            println("${summary.alarmMuteRuleArn} (${summary.status?.value})")
        }
    }
    return summaries
}

suspend fun deleteAlarmMuteRule(muteRuleName: String) {
    val request =
        DeleteAlarmMuteRuleRequest {
            alarmMuteRuleName = muteRuleName
        }

    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.deleteAlarmMuteRule(request)
        println("Successfully deleted alarm mute rule $muteRuleName")
    }
}

suspend fun stopOTelEnrichment() {
    CloudWatchClient.fromEnvironment { region = "us-east-1" }.use { cwClient ->
        cwClient.stopOTelEnrichment(StopOTelEnrichmentRequest {})
        println("Successfully stopped OTel enrichment for this account")
    }
}
```
+ For API details, see the following topics in *AWS SDK for Kotlin API reference*.
  + [DeleteAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DeleteAlarms](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DeleteDashboards](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [DescribeAlarmContributors](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetDashboard](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetMetricStatistics](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [GetOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [ListAlarmMuteRules](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [ListDashboards](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [ListMetrics](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [PutAlarmMuteRule](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [PutDashboard](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [PutMetricAlarm](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [StartOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html)
  + [StopOTelEnrichment](https://sdk.amazonaws.com/kotlin/api/latest/index.html)

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cloudwatch#code-examples). 
Run an interactive scenario demonstrating the CloudWatch OpenTelemetry experience.  

```
from collections import Counter
from datetime import datetime, timedelta, timezone
import json
import logging
import random
import sys
import boto3
from botocore.exceptions import ClientError

from cloudwatch_basics import CloudWatchWrapper
from cloudwatch_otel import CloudWatchOTelWrapper

logger = logging.getLogger(__name__)

DEFAULT_QUERY = "avg by (host) (system_cpu_utilization) > 80"

# Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
EVALUATION_INTERVAL = 60
PENDING_PERIOD = 300
RECOVERY_PERIOD = 120

DASHES = "-" * 80


class CloudWatchScenario:
    """Runs an interactive scenario that shows how to use Amazon CloudWatch."""

    def __init__(self, cloudwatch_wrapper, otel_wrapper):
        """
        :param cloudwatch_wrapper: An object that wraps CloudWatch metric, statistic,
                                   and dashboard actions.
        :param otel_wrapper: An object that wraps CloudWatch OTel enrichment, PromQL
                             alarm, and alarm mute rule actions.
        """
        self.cloudwatch_wrapper = cloudwatch_wrapper
        self.otel_wrapper = otel_wrapper

        # Suffix the resource names so repeated runs do not collide.
        suffix = random.randint(1000, 9999)
        self.alarm_name = f"doc-example-promql-alarm-{suffix}"
        self.dashboard_name = f"doc-example-dashboard-{suffix}"
        self.mute_rule_name = f"doc-example-mute-rule-{suffix}"

        # Tracks whether this run turned enrichment on, so that cleanup only turns off
        # enrichment that this run started.
        self.started_enrichment = False
        self.dashboard_created = False

    def run_scenario(self):
        """Runs the eight steps of the scenario in order."""
        print(DASHES)
        print("Welcome to the Amazon CloudWatch Basics scenario.")
        print(
            "\nCloudWatch now ingests OpenTelemetry metrics natively. This scenario walks\n"
            "through that experience: it turns on OTel enrichment so CloudWatch can\n"
            "correlate incoming OTLP metrics with the resources that produced them, alarms\n"
            "on those metrics with a PromQL query, and shows you which individual series\n"
            "drove the alarm.\n"
            "\nA PromQL alarm works differently from a classic metric alarm. Rather than\n"
            "watching one metric and counting breaching periods, it evaluates a query that\n"
            "can match many series at once, and tracks each one separately as a contributor."
        )
        print(DASHES)

        namespaces = self.list_metrics_and_namespaces()
        self.start_otel_enrichment()
        self.explain_otlp_ingestion()
        self.create_promql_alarm()
        self.inspect_alarm_contributors()
        self.get_statistics_and_chart_metric(namespaces)
        self.mute_alarm_for_maintenance()

    def list_metrics_and_namespaces(self):
        """
        Lists the metrics and namespaces already present in the account, to orient the
        reader before any configuration happens.

        :return: A Counter of namespace to metric count, most common first.
        """
        print("1. List metrics and namespaces")
        print(
            "\nBefore configuring anything, let's see what CloudWatch is already\n"
            "collecting in this account by calling ListMetrics.\n"
        )

        namespaces = Counter()
        metric_count = 0
        for metric in self.cloudwatch_wrapper.list_all_metrics():
            namespaces[metric.namespace] += 1
            metric_count += 1
            # This account may have a very large number of metrics, so stop once we
            # have enough to give the reader a sense of what is there.
            if metric_count >= 500:
                break

        print(f"\tFound {metric_count} metrics across {len(namespaces)} namespaces:")
        for namespace, count in namespaces.most_common(10):
            print(f"\t  {namespace} ({count} metrics)")

        if not namespaces:
            print(
                "\tNo metrics found in this account. The statistics and dashboard steps\n"
                "\tlater on need an existing metric, so they will be skipped."
            )

        print(DASHES)
        return namespaces

    def start_otel_enrichment(self):
        """
        Starts OTel enrichment, but only if it is not already running. Enrichment is
        what makes CloudWatch attach AWS resource context to incoming OTLP metrics.
        """
        print("2. Start OpenTelemetry enrichment")
        print(
            "\nEnrichment is what lets CloudWatch attach AWS resource context to the OTLP\n"
            "metrics you send it. Without it, your metrics arrive as opaque series with no\n"
            "connection to the resources that emitted them.\n"
            "\nWe check the current state first, and only start enrichment if it isn't\n"
            "already on.\n"
        )

        status = self.otel_wrapper.get_otel_enrichment_status()
        print(f"\tEnrichment status: {status}")

        if status != "Running":
            self.otel_wrapper.start_otel_enrichment()
            self.started_enrichment = True
            status = self.otel_wrapper.get_otel_enrichment_status()
            print(f"\tEnrichment status: {status}")
            print(
                "\n\tNote: this run started enrichment, so the cleanup step will stop it\n"
                "\tagain."
            )
        else:
            print(
                "\n\tEnrichment was already running, so we will leave it alone. The cleanup\n"
                "\tstep will not stop it, because other workloads in this account may\n"
                "\tdepend on it."
            )

        print(DASHES)

    @staticmethod
    def explain_otlp_ingestion():
        """
        Explains that OTLP metric ingestion is not an AWS SDK operation. This step makes
        no service call; naming the gap explicitly is the point.
        """
        print("3. Send OTLP metrics to CloudWatch")
        print(
            "\nThis step is not an AWS SDK operation, and that's worth being explicit\n"
            "about. Metrics reach CloudWatch over the OTLP protocol, through the CloudWatch\n"
            "agent, an OpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics\n"
            "API to call.\n"
            "\nPoint your collector at the CloudWatch metrics endpoint, which follows the\n"
            "pattern\n"
            "\thttps://monitoring.<region>.amazonaws.com/v1/metrics\n"
            "\nThe endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp\n"
            "exporter rather than otlp. The metrics endpoint signs as 'monitoring'.\n"
            "\nSee otlp_collector_config.yaml in this folder for a working collector\n"
            "configuration."
        )
        print(DASHES)

    def create_promql_alarm(self):
        """Creates an alarm whose evaluation is a PromQL query."""
        print("4. Create a PromQL alarm")
        print(
            "\nNow we alarm on those metrics. The comparison goes inside the query itself:\n"
            "a PromQL alarm has no separate threshold, comparison operator, statistic, or\n"
            "period.\n"
        )

        query = (
            input(
                f"Enter a PromQL query, or press ENTER for [{DEFAULT_QUERY}]: "
            ).strip()
            or DEFAULT_QUERY
        )

        self.otel_wrapper.create_promql_alarm(
            self.alarm_name,
            query,
            EVALUATION_INTERVAL,
            pending_period=PENDING_PERIOD,
            recovery_period=RECOVERY_PERIOD,
            description="A PromQL alarm created by the Boto3 Basics scenario.",
        )

        print(f"\tCreated alarm {self.alarm_name}:")
        print(f"\t  query:              {query}")
        print(f"\t  evaluationInterval: {EVALUATION_INTERVAL} seconds")
        print(f"\t  pendingPeriod:      {PENDING_PERIOD} seconds")
        print(f"\t  recoveryPeriod:     {RECOVERY_PERIOD} seconds")
        print(
            "\n\tA PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which\n"
            "\tis another way it differs from a classic alarm."
        )
        print(DASHES)

    def inspect_alarm_contributors(self):
        """
        Shows which individual series the alarm's query matched. This is the step with
        no classic-alarm equivalent.
        """
        print("5. Inspect the alarm's contributors")
        print(
            "\nEach contributor is one series the query matched, identified by its label\n"
            "set. This is how you find out which host is unhealthy rather than only that\n"
            "something is. Classic alarms have no equivalent.\n"
        )

        contributors = self.otel_wrapper.describe_alarm_contributors(self.alarm_name)

        if not contributors:
            print(
                "\tNo contributors yet. The query matched no series, which usually means no\n"
                "\tOTel metrics with these labels have arrived. Once your collector is\n"
                "\tsending data, each matching series appears here with its labels and the\n"
                "\treason it breached."
            )
        else:
            print(f"\tFound {len(contributors)} contributors:")
            for contributor in contributors:
                labels = ", ".join(
                    f"{key}={value}"
                    for key, value in sorted(
                        contributor.get("ContributorAttributes", {}).items()
                    )
                )
                print(f"\t  {contributor['ContributorId']}: {labels}")
                print(f"\t    reason: {contributor.get('StateReason')}")

        print(DASHES)

    def get_statistics_and_chart_metric(self, namespaces):
        """
        Gets statistics for an existing metric and charts it on a dashboard, so the
        reader can see what the alarm is evaluating.

        :param namespaces: The Counter of namespaces discovered in step 1.
        """
        print("6. Get statistics and chart the metric on a dashboard")
        print(
            "\nStatistics and dashboards are how you see what the alarm is evaluating.\n"
        )

        if not namespaces:
            print("\tSkipping statistics and dashboard because no metrics exist yet.")
            print(DASHES)
            return

        namespace = namespaces.most_common(1)[0][0]
        metric = next(
            (
                candidate
                for candidate in self.cloudwatch_wrapper.list_all_metrics()
                if candidate.namespace == namespace
            ),
            None,
        )

        if metric is None:
            print(f"\tNo metrics found in namespace {namespace}, skipping.")
            print(DASHES)
            return

        try:
            stats = self.cloudwatch_wrapper.get_metric_statistics(
                metric.namespace,
                metric.name,
                datetime.now(timezone.utc) - timedelta(days=1),
                datetime.now(timezone.utc),
                3600,
                ["Average", "Maximum"],
            )
            datapoints = stats["Datapoints"]
            print(
                f"\tStatistics for {metric.namespace} {metric.name} over the last day:"
            )
            print(f"\t  Datapoints: {len(datapoints)}")
            for datapoint in datapoints[:3]:
                print(
                    f"\t  {datapoint['Timestamp']} average {datapoint.get('Average')}, "
                    f"maximum {datapoint.get('Maximum')}"
                )
        except ClientError as error:
            print(f"\tCould not get statistics: {error}")

        try:
            region = self.otel_wrapper.cloudwatch_client.meta.region_name
            body = self.build_dashboard_body(metric, region)
            messages = self.cloudwatch_wrapper.put_dashboard(self.dashboard_name, body)
            self.dashboard_created = True
            for message in messages:
                print(f"\tDashboard validation message: {message.get('Message')}")
            print(f"\tCreated dashboard {self.dashboard_name}.")

            stored = self.cloudwatch_wrapper.get_dashboard(self.dashboard_name)
            print(
                f"\tRead the dashboard back, {len(stored)} characters of widget JSON."
            )
        except ClientError as error:
            print(f"\tCould not create the dashboard: {error}")

        print(DASHES)

    @staticmethod
    def build_dashboard_body(metric, region):
        """
        Builds a single-widget dashboard body that charts the given metric.

        :param metric: A Boto3 CloudWatch Metric resource.
        :param region: The region the metric is in. A metric widget must name its
                       region, because a dashboard can chart metrics from several.
        :return: The dashboard body, as a JSON string.
        """
        metric_spec = [metric.namespace, metric.name]
        for dimension in metric.dimensions or []:
            metric_spec.extend([dimension["Name"], dimension["Value"]])

        return json.dumps(
            {
                "widgets": [
                    {
                        "type": "text",
                        "x": 0,
                        "y": 0,
                        "width": 24,
                        "height": 2,
                        "properties": {
                            "markdown": "This dashboard was created programmatically "
                            "by an AWS SDK code example."
                        },
                    },
                    {
                        "type": "metric",
                        "x": 0,
                        "y": 2,
                        "width": 12,
                        "height": 6,
                        "properties": {
                            "metrics": [metric_spec],
                            "view": "timeSeries",
                            "stat": "Average",
                            "period": 300,
                            "region": region,
                            "title": metric.name,
                        },
                    },
                ]
            }
        )

    def mute_alarm_for_maintenance(self):
        """
        Creates a mute rule so the alarm's actions are suppressed during a maintenance
        window, then reads it back and finds it in the account's rules.
        """
        print("7. Mute the alarm for a maintenance window")
        print(
            "\nWhile a mute rule is active the targeted alarms keep evaluating and keep\n"
            "changing state, but their actions do not fire. This is the supported way to\n"
            "suppress notifications during planned maintenance, instead of disabling alarm\n"
            "actions and hoping someone remembers to turn them back on.\n"
        )

        # The expression is a five-field cron expression,
        # cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five
        # fields, not the six that Amazon EventBridge uses. For a one-time window, use
        # at(yyyy-MM-ddThh:mm), with no seconds. The duration is an ISO 8601 duration
        # from PT1M to P15D, so PT2H rather than 2h.
        expression = "cron(0 2 * * SUN)"
        duration = "PT2H"
        tz = "America/Los_Angeles"

        self.otel_wrapper.put_alarm_mute_rule(
            self.mute_rule_name,
            expression,
            duration,
            alarm_names=[self.alarm_name],
            timezone=tz,
            description="A mute rule created by the Boto3 Basics scenario.",
        )

        print(f"\tCreated mute rule {self.mute_rule_name}:")
        print(f"\t  schedule: {expression} for {duration}")
        print(f"\t  timezone: {tz}")
        print(f"\t  targets:  {self.alarm_name}")
        print(
            "\n\tNote the two formats here. The expression is a five-field cron expression,\n"
            "\tfive rather than the six Amazon EventBridge uses. The duration is an ISO 8601\n"
            "\tduration, so 'PT2H' and not '2h'.\n"
            "\n\tAlso note that MuteTargets is set explicitly. If you leave it out, the rule\n"
            "\tapplies to every alarm in the account."
        )

        mute_rule = self.otel_wrapper.get_alarm_mute_rule(self.mute_rule_name)
        print(
            f"\tRead the rule back: status {mute_rule.get('Status')}, "
            f"mute type {mute_rule.get('MuteType')}."
        )

        summaries = self.otel_wrapper.list_alarm_mute_rules(alarm_name=self.alarm_name)
        print(f"\tFound {len(summaries)} mute rules targeting this alarm.")
        # Mute rule summaries carry no name field, only an ARN, so match on the ARN
        # suffix.
        for summary in summaries:
            arn = summary.get("AlarmMuteRuleArn", "")
            if arn.endswith(f"/{self.mute_rule_name}") or arn.endswith(
                f":{self.mute_rule_name}"
            ):
                print(f"\t  matched by ARN: {arn} ({summary.get('Status')})")
                break

        print(DASHES)

    def clean_up(self):
        """
        Deletes the resources the scenario created. Each deletion is attempted
        independently so that one failure does not leave the remaining resources behind.
        """
        print("8. Clean up")
        answer = input("Delete the resources this scenario created? (y/n) ")
        if answer.strip().lower() != "y":
            print(
                "\tSkipping cleanup. Note that the alarm, dashboard, and mute rule are\n"
                "\tstill in your account, and enrichment may still be running."
            )
            print(DASHES)
            return

        try:
            self.otel_wrapper.delete_alarm_mute_rule(self.mute_rule_name)
            print(f"\tDeleted mute rule {self.mute_rule_name}.")
        except ClientError as error:
            print(f"\tCould not delete the mute rule: {error}")

        try:
            self.otel_wrapper.delete_alarms([self.alarm_name])
            print(f"\tDeleted alarm {self.alarm_name}.")
        except ClientError as error:
            print(f"\tCould not delete the alarm: {error}")

        if self.dashboard_created:
            try:
                self.cloudwatch_wrapper.delete_dashboards([self.dashboard_name])
                print(f"\tDeleted dashboard {self.dashboard_name}.")
            except ClientError as error:
                print(f"\tCould not delete the dashboard: {error}")

        if self.started_enrichment:
            try:
                self.otel_wrapper.stop_otel_enrichment()
                print("\tStopped OTel enrichment, because this run started it.")
            except ClientError as error:
                print(f"\tCould not stop OTel enrichment: {error}")
        else:
            print(
                "\tLeft OTel enrichment running, because it was already on before this run."
            )

        print(DASHES)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    scenario = CloudWatchScenario(
        CloudWatchWrapper(boto3.resource("cloudwatch")),
        CloudWatchOTelWrapper(boto3.client("cloudwatch")),
    )
    try:
        scenario.run_scenario()
    except Exception:  # pylint: disable=broad-except
        logging.exception("Something went wrong with the scenario.")
    finally:
        scenario.clean_up()

    print("This concludes the Amazon CloudWatch Basics scenario.")


if __name__ == "__main__":
    sys.exit(main())
```
The class that wraps the CloudWatch OpenTelemetry operations the scenario calls.  

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
```
The metric, statistic, and dashboard operations the scenario calls.  

```
    def list_all_metrics(self):
        """
        Gets every metric in the account, without filtering by namespace or name. Use
        this to discover what CloudWatch is already collecting before you configure
        anything.

        :return: An iterator that yields the retrieved metrics.
        """
        try:
            metric_iter = self.cloudwatch_resource.metrics.all()
            logger.info("Got all metrics for the account.")
        except ClientError:
            logger.exception("Couldn't get metrics for the account.")
            raise
        else:
            return metric_iter


    def get_metric_statistics(self, namespace, name, start, end, period, stat_types):
        """
        Gets statistics for a metric within a specified time span. Metrics are grouped
        into the specified period.

        :param namespace: The namespace of the metric.
        :param name: The name of the metric.
        :param start: The UTC start time of the time span to retrieve.
        :param end: The UTC end time of the time span to retrieve.
        :param period: The period, in seconds, in which to group metrics. The period
                       must match the granularity of the metric, which depends on
                       the metric's age. For example, metrics that are older than
                       three hours have a one-minute granularity, so the period must
                       be at least 60 and must be a multiple of 60.
        :param stat_types: The type of statistics to retrieve, such as average value
                           or maximum value.
        :return: The retrieved statistics for the metric.
        """
        try:
            metric = self.cloudwatch_resource.Metric(namespace, name)
            stats = metric.get_statistics(
                StartTime=start, EndTime=end, Period=period, Statistics=stat_types
            )
            logger.info(
                "Got %s statistics for %s.", len(stats["Datapoints"]), stats["Label"]
            )
        except ClientError:
            logger.exception("Couldn't get statistics for %s.%s.", namespace, name)
            raise
        else:
            return stats


    def put_dashboard(self, name, body):
        """
        Creates or replaces a dashboard. The body is a JSON document describing the
        dashboard's widgets.

        :param name: The name of the dashboard.
        :param body: The dashboard body, as a JSON string.
        :return: Any validation messages the service returned. An empty list means the
                 dashboard body was accepted as written.
        """
        try:
            response = self.cloudwatch_resource.meta.client.put_dashboard(
                DashboardName=name, DashboardBody=body
            )
            logger.info("Put dashboard %s.", name)
        except ClientError:
            logger.exception("Couldn't put dashboard %s.", name)
            raise
        else:
            return response.get("DashboardValidationMessages", [])


    def get_dashboard(self, name):
        """
        Gets a dashboard's body, so you can confirm what the service actually stored.

        :param name: The name of the dashboard.
        :return: The dashboard body, as a JSON string.
        """
        try:
            response = self.cloudwatch_resource.meta.client.get_dashboard(
                DashboardName=name
            )
            logger.info("Got dashboard %s.", name)
        except ClientError:
            logger.exception("Couldn't get dashboard %s.", name)
            raise
        else:
            return response["DashboardBody"]


    def delete_dashboards(self, names):
        """
        Deletes the specified dashboards.

        :param names: The names of the dashboards to delete.
        """
        try:
            self.cloudwatch_resource.meta.client.delete_dashboards(DashboardNames=names)
            logger.info("Deleted dashboards %s.", ", ".join(names))
        except ClientError:
            logger.exception("Couldn't delete dashboards %s.", ", ".join(names))
            raise
```
+ For API details, see the following topics in *AWS SDK for Python (Boto3) API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteAlarms)
  + [DeleteDashboards](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DeleteDashboards)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetDashboard](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetDashboard)
  + [GetMetricStatistics](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetMetricStatistics)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListAlarmMuteRules)
  + [ListDashboards](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListDashboards)
  + [ListMetrics](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/ListMetrics)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutDashboard](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutDashboard)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/StopOTelEnrichment)

------
#### [ Ruby ]

**SDK for Ruby**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudwatch#code-examples). 
Run an interactive scenario demonstrating the CloudWatch OpenTelemetry experience.  

```
DASHES = ('-' * 80).freeze
DEFAULT_QUERY = 'avg by (host) (system_cpu_utilization) > 80'.freeze

# Valid evaluation intervals are 10, 20, 30, or any multiple of 60 up to 3600 seconds.
EVALUATION_INTERVAL = 60
PENDING_PERIOD = 300
RECOVERY_PERIOD = 120

# Lists the metrics and namespaces already present in the account, to orient the reader
# before any configuration happens.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Hash] A hash of namespace to the metrics found in it, most populated first.
def metrics_by_namespace(cloudwatch_client)
  by_namespace = {}
  metric_count = 0

  cloudwatch_client.list_metrics.each_page do |page|
    page.metrics.each do |metric|
      (by_namespace[metric.namespace] ||= []) << metric
      metric_count += 1
    end
    # This account may have a very large number of metrics, so stop once we have enough
    # to give the reader a sense of what is there.
    break if metric_count >= 500
  end

  puts "\tFound #{metric_count} metrics across #{by_namespace.size} namespaces:"
  by_namespace
    .sort_by { |_namespace, metrics| -metrics.size }
    .first(10)
    .each { |namespace, metrics| puts "\t  #{namespace} (#{metrics.size} metrics)" }

  if by_namespace.empty?
    puts "\tNo metrics found in this account. The statistics and dashboard steps later"
    puts "\ton need an existing metric, so they will be skipped."
  end

  by_namespace
rescue StandardError => e
  puts "Error listing metrics: #{e.message}"
  {}
end

# Turns on OTel enrichment, but only if it is not already running. Enrichment is an
# account-wide setting, so this scenario only turns it off again if it was the thing that
# turned it on.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @return [Boolean] true if this run started enrichment; otherwise, false.
def enrichment_started_by_example?(cloudwatch_client)
  # The Ruby SDK renders the OTel prefix as +o_tel+, so the methods are
  # +get_o_tel_enrichment+ and +start_o_tel_enrichment+.
  status = cloudwatch_client.get_o_tel_enrichment.status
  puts "\tEnrichment status: #{status}"

  if status == 'Running'
    puts
    puts "\tEnrichment was already running, so we will leave it alone. The cleanup step"
    puts "\twill not stop it, because other workloads in this account may depend on it."
    return false
  end

  cloudwatch_client.start_o_tel_enrichment
  puts "\tEnrichment status: #{cloudwatch_client.get_o_tel_enrichment.status}"
  puts
  puts "\tNote: this run started enrichment, so the cleanup step will stop it again."
  true
rescue StandardError => e
  puts "Error starting OTel enrichment: #{e.message}"
  false
end

# Creates an alarm whose evaluation is a PromQL query.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm to create.
# @param query [String] The PromQL query to evaluate.
# @return [Boolean] true if the alarm was created; otherwise, false.
def promql_alarm_created?(cloudwatch_client, alarm_name, query)
  # The comparison belongs in the query itself. A PromQL alarm has no separate threshold,
  # comparison operator, statistic, period, or evaluation periods. Note that the Ruby SDK
  # spells the criteria member +prom_ql_criteria+.
  cloudwatch_client.put_metric_alarm(
    alarm_name: alarm_name,
    alarm_description: 'A PromQL alarm created by the AWS SDK for Ruby Basics scenario.',
    evaluation_criteria: {
      prom_ql_criteria: {
        query: query,
        pending_period: PENDING_PERIOD,
        recovery_period: RECOVERY_PERIOD
      }
    },
    evaluation_interval: EVALUATION_INTERVAL
  )
  true
rescue StandardError => e
  puts "Error creating PromQL alarm: #{e.message}"
  false
end

# Prints the contributors to a PromQL alarm. Each contributor is one series the query
# matched, identified by its label set.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the PromQL alarm.
# @return [void]
def report_alarm_contributors(cloudwatch_client, alarm_name)
  contributors = []
  next_token = nil

  loop do
    response = cloudwatch_client.describe_alarm_contributors(
      alarm_name: alarm_name,
      next_token: next_token
    )
    contributors.concat(response.alarm_contributors)
    next_token = response.next_token
    # A page can come back empty while still carrying a token, so keep going until the
    # token itself is gone rather than stopping at the first empty page.
    break if next_token.nil? || next_token.empty?
  end

  if contributors.empty?
    puts "\tNo contributors yet. The query matched no series, which usually means no"
    puts "\tOTel metrics with these labels have arrived. Once your collector is sending"
    puts "\tdata, each matching series appears here with its labels and why it breached."
    return
  end

  puts "\tFound #{contributors.size} contributors:"
  contributors.each do |contributor|
    labels = contributor.contributor_attributes.sort.map { |k, v| "#{k}=#{v}" }.join(', ')
    puts "\t  #{contributor.contributor_id}: #{labels}"
    puts "\t    reason: #{contributor.state_reason}"
  end
rescue StandardError => e
  puts "Error describing alarm contributors: #{e.message}"
end

# Builds a single-widget dashboard body that charts the given metric.
#
# @param metric [Aws::CloudWatch::Types::Metric] The metric to chart.
# @param region [String] The region the metric is in. A metric widget must name its
#   region, because a dashboard can chart metrics from several.
# @return [String] The dashboard body, as JSON.
def dashboard_body(metric, region)
  metric_spec = [metric.namespace, metric.metric_name]
  metric.dimensions.each { |dimension| metric_spec.push(dimension.name, dimension.value) }

  {
    widgets: [
      {
        type: 'text',
        x: 0, y: 0, width: 24, height: 2,
        properties: {
          markdown: 'This dashboard was created programmatically by an AWS SDK code example.'
        }
      },
      {
        type: 'metric',
        x: 0, y: 2, width: 12, height: 6,
        properties: {
          metrics: [metric_spec],
          view: 'timeSeries',
          stat: 'Average',
          period: 300,
          region: region,
          title: metric.metric_name
        }
      }
    ]
  }.to_json
end

# Gets statistics for an existing metric and charts it on a dashboard, so the reader can
# see what the alarm is evaluating.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param dashboard_name [String] The name of the dashboard to create.
# @param by_namespace [Hash] The namespaces and metrics discovered in step 1.
# @return [Boolean] true if a dashboard was created; otherwise, false.
def chart_metric_on_dashboard(cloudwatch_client, dashboard_name, by_namespace)
  if by_namespace.empty?
    puts "\tSkipping statistics and dashboard because no metrics exist yet."
    return false
  end

  metric = by_namespace.max_by { |_namespace, metrics| metrics.size }.last.first

  stats = cloudwatch_client.get_metric_statistics(
    namespace: metric.namespace,
    metric_name: metric.metric_name,
    dimensions: metric.dimensions,
    start_time: Time.now - (60 * 60 * 24),
    end_time: Time.now,
    period: 3600,
    statistics: %w[Average Maximum]
  )
  puts "\tStatistics for #{metric.namespace} #{metric.metric_name} over the last day:"
  puts "\t  Datapoints: #{stats.datapoints.size}"
  stats.datapoints.first(3).each do |datapoint|
    puts "\t  #{datapoint.timestamp} average #{datapoint.average}, maximum #{datapoint.maximum}"
  end

  response = cloudwatch_client.put_dashboard(
    dashboard_name: dashboard_name,
    dashboard_body: dashboard_body(metric, cloudwatch_client.config.region)
  )
  response.dashboard_validation_messages.each do |message|
    puts "\tDashboard validation message: #{message.message}"
  end
  puts "\tCreated dashboard #{dashboard_name}."

  stored = cloudwatch_client.get_dashboard(dashboard_name: dashboard_name)
  puts "\tRead the dashboard back, #{stored.dashboard_body.length} characters of widget JSON."
  true
rescue StandardError => e
  puts "Error getting statistics or creating the dashboard: #{e.message}"
  false
end

# Creates a mute rule so the alarm's actions are suppressed during a maintenance window,
# then reads it back and finds it in the account's rules.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param mute_rule_name [String] The name of the mute rule to create.
# @param alarm_name [String] The name of the alarm to mute.
# @return [void]
def mute_alarm_for_maintenance(cloudwatch_client, mute_rule_name, alarm_name)
  # The expression is a five-field cron expression,
  # cron(Minutes Hours Day-of-month Month Day-of-week). Note that this is five fields, not
  # the six that Amazon EventBridge uses. For a one-time window, use at(yyyy-MM-ddThh:mm),
  # with no seconds. The duration is an ISO 8601 duration from PT1M to P15D, so PT2H
  # rather than 2h.
  expression = 'cron(0 2 * * SUN)'
  duration = 'PT2H'
  timezone = 'America/Los_Angeles'

  cloudwatch_client.put_alarm_mute_rule(
    name: mute_rule_name,
    description: 'A mute rule created by the AWS SDK for Ruby Basics scenario.',
    rule: {
      schedule: {
        expression: expression,
        duration: duration,
        timezone: timezone
      }
    },
    # Target up to 100 alarms. If mute_targets is omitted, the rule applies to every alarm
    # in the account.
    mute_targets: { alarm_names: [alarm_name] }
  )

  puts "\tCreated mute rule #{mute_rule_name}:"
  puts "\t  schedule: #{expression} for #{duration}"
  puts "\t  timezone: #{timezone}"
  puts "\t  targets:  #{alarm_name}"
  puts
  puts "\tNote the two formats here. The expression is a five-field cron expression, five"
  puts "\trather than the six Amazon EventBridge uses. The duration is an ISO 8601"
  puts "\tduration, so 'PT2H' and not '2h'."
  puts
  puts "\tAlso note that mute_targets is set explicitly. If you leave it out, the rule"
  puts "\tapplies to every alarm in the account."

  rule = cloudwatch_client.get_alarm_mute_rule(alarm_mute_rule_name: mute_rule_name)
  puts "\tRead the rule back: status #{rule.status}, mute type #{rule.mute_type}."

  summaries = cloudwatch_client.list_alarm_mute_rules(alarm_name: alarm_name)
                               .alarm_mute_rule_summaries
  puts "\tFound #{summaries.size} mute rules targeting this alarm."
  # Mute rule summaries carry no name field, only an ARN, so match on the ARN suffix.
  match = summaries.find do |summary|
    summary.alarm_mute_rule_arn.end_with?("/#{mute_rule_name}", ":#{mute_rule_name}")
  end
  puts "\t  matched by ARN: #{match.alarm_mute_rule_arn} (#{match.status})" if match
rescue StandardError => e
  puts "Error muting the alarm: #{e.message}"
end

# Deletes the resources the scenario created. Each deletion is attempted independently so
# that one failure does not leave the remaining resources behind.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param names [Hash] The alarm, dashboard, and mute rule names to delete.
# @param started_here [Boolean] Whether this run turned OTel enrichment on.
# @return [void]
def clean_up(cloudwatch_client, names, started_here)
  begin
    cloudwatch_client.delete_alarm_mute_rule(alarm_mute_rule_name: names[:mute_rule])
    puts "\tDeleted mute rule #{names[:mute_rule]}."
  rescue StandardError => e
    puts "\tCould not delete the mute rule: #{e.message}"
  end

  begin
    cloudwatch_client.delete_alarms(alarm_names: [names[:alarm]])
    puts "\tDeleted alarm #{names[:alarm]}."
  rescue StandardError => e
    puts "\tCould not delete the alarm: #{e.message}"
  end

  if names[:dashboard]
    begin
      cloudwatch_client.delete_dashboards(dashboard_names: [names[:dashboard]])
      puts "\tDeleted dashboard #{names[:dashboard]}."
    rescue StandardError => e
      puts "\tCould not delete the dashboard: #{e.message}"
    end
  end

  unless started_here
    puts "\tLeft OTel enrichment running, because it was already on before this run."
    return
  end

  begin
    cloudwatch_client.stop_o_tel_enrichment
    puts "\tStopped OTel enrichment, because this run started it."
  rescue StandardError => e
    puts "\tCould not stop OTel enrichment: #{e.message}"
  end
end

# Prints the scenario's introduction.
#
# @return [void]
def print_intro
  puts DASHES
  puts 'Welcome to the Amazon CloudWatch Basics scenario.'
  puts
  puts 'CloudWatch now ingests OpenTelemetry metrics natively. This scenario walks through'
  puts 'that experience: it turns on OTel enrichment so CloudWatch can correlate incoming'
  puts 'OTLP metrics with the resources that produced them, alarms on those metrics with a'
  puts 'PromQL query, and shows you which individual series drove the alarm.'
  puts
  puts 'A PromQL alarm works differently from a classic metric alarm. Rather than watching'
  puts 'one metric and counting breaching periods, it evaluates a query that can match many'
  puts 'series at once, and tracks each one separately as a contributor.'
  puts DASHES
end

# Explains that OTLP metric ingestion is not an AWS SDK operation. This step makes no
# service call; naming the gap explicitly is the point.
#
# @return [void]
def explain_otlp_ingestion
  puts '3. Send OTLP metrics to CloudWatch'
  puts
  puts 'This step is not an AWS SDK operation, and that\'s worth being explicit about.'
  puts 'Metrics reach CloudWatch over the OTLP protocol, through the CloudWatch agent, an'
  puts 'OpenTelemetry Collector, or an ADOT SDK. There is no PutOTelMetrics API to call.'
  puts
  puts 'Point your collector at the CloudWatch metrics endpoint, which follows the pattern'
  puts "\thttps://monitoring.<region>.amazonaws.com/v1/metrics"
  puts
  puts 'The endpoint is HTTP/1.1 only and does not support gRPC, so use an otlphttp'
  puts 'exporter rather than otlp. The metrics endpoint signs as "monitoring".'
  puts DASHES
end

# Prompts for a PromQL query and creates an alarm that evaluates it.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param alarm_name [String] The name of the alarm to create.
# @return [void]
def create_promql_alarm_step(cloudwatch_client, alarm_name)
  puts '4. Create a PromQL alarm'
  puts
  puts 'Now we alarm on those metrics. The comparison goes inside the query itself: a'
  puts 'PromQL alarm has no separate threshold, comparison operator, statistic, or period.'
  puts
  print "Enter a PromQL query, or press ENTER for [#{DEFAULT_QUERY}]: "
  input = $stdin.gets
  query = input.nil? || input.strip.empty? ? DEFAULT_QUERY : input.strip

  if promql_alarm_created?(cloudwatch_client, alarm_name, query)
    puts "\tCreated alarm #{alarm_name}:"
    puts "\t  query:              #{query}"
    puts "\t  evaluationInterval: #{EVALUATION_INTERVAL} seconds"
    puts "\t  pendingPeriod:      #{PENDING_PERIOD} seconds"
    puts "\t  recoveryPeriod:     #{RECOVERY_PERIOD} seconds"
    puts
    puts "\tA PromQL alarm starts in the OK state rather than INSUFFICIENT_DATA, which is"
    puts "\tanother way it differs from a classic alarm."
  end
  puts DASHES
end

# Runs the eight steps of the scenario in order.
def run_me
  region = 'us-east-1'
  cloudwatch_client = Aws::CloudWatch::Client.new(region: region)

  # Suffix the resource names so repeated runs do not collide.
  suffix = rand(1000..9999)
  alarm_name = "doc-example-promql-alarm-#{suffix}"
  dashboard_name = "doc-example-dashboard-#{suffix}"
  mute_rule_name = "doc-example-mute-rule-#{suffix}"

  print_intro

  puts '1. List metrics and namespaces'
  puts
  puts 'Before configuring anything, let\'s see what CloudWatch is already collecting in'
  puts 'this account by calling ListMetrics.'
  puts
  by_namespace = metrics_by_namespace(cloudwatch_client)
  puts DASHES

  puts '2. Start OpenTelemetry enrichment'
  puts
  puts 'Enrichment is what lets CloudWatch attach AWS resource context to the OTLP metrics'
  puts 'you send it. Without it, your metrics arrive as opaque series with no connection to'
  puts 'the resources that emitted them.'
  puts
  puts 'We check the current state first, and only start enrichment if it isn\'t already on.'
  puts
  started_here = enrichment_started_by_example?(cloudwatch_client)
  puts DASHES

  explain_otlp_ingestion
  create_promql_alarm_step(cloudwatch_client, alarm_name)

  puts '5. Inspect the alarm\'s contributors'
  puts
  puts 'Each contributor is one series the query matched, identified by its label set. This'
  puts 'is how you find out which host is unhealthy rather than only that something is.'
  puts 'Classic alarms have no equivalent.'
  puts
  report_alarm_contributors(cloudwatch_client, alarm_name)
  puts DASHES

  puts '6. Get statistics and chart the metric on a dashboard'
  puts
  puts 'Statistics and dashboards are how you see what the alarm is evaluating.'
  puts
  dashboard_created = chart_metric_on_dashboard(cloudwatch_client, dashboard_name, by_namespace)
  puts DASHES

  mute_alarm_step(cloudwatch_client, mute_rule_name, alarm_name)

  clean_up_step(
    cloudwatch_client,
    { alarm: alarm_name, dashboard: dashboard_created ? dashboard_name : nil,
      mute_rule: mute_rule_name },
    started_here
  )

  puts 'This concludes the Amazon CloudWatch Basics scenario.'
end

# Explains what a mute rule does, then creates one for the scenario's alarm.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param mute_rule_name [String] The name of the mute rule to create.
# @param alarm_name [String] The name of the alarm to mute.
# @return [void]
def mute_alarm_step(cloudwatch_client, mute_rule_name, alarm_name)
  puts '7. Mute the alarm for a maintenance window'
  puts
  puts 'While a mute rule is active the targeted alarms keep evaluating and keep changing'
  puts 'state, but their actions do not fire. This is the supported way to suppress'
  puts 'notifications during planned maintenance, instead of disabling alarm actions and'
  puts 'hoping someone remembers to turn them back on.'
  puts
  mute_alarm_for_maintenance(cloudwatch_client, mute_rule_name, alarm_name)
  puts DASHES
end

# Asks whether to delete the resources the scenario created, and deletes them if so.
#
# @param cloudwatch_client [Aws::CloudWatch::Client] An initialized CloudWatch client.
# @param names [Hash] The alarm, dashboard, and mute rule names to delete.
# @param started_here [Boolean] Whether this run turned OTel enrichment on.
# @return [void]
def clean_up_step(cloudwatch_client, names, started_here)
  puts '8. Clean up'
  print 'Delete the resources this scenario created? (y/n) '
  answer = $stdin.gets
  if answer.nil? || answer.strip.downcase != 'y'
    puts "\tSkipping cleanup. Note that the alarm, dashboard, and mute rule are still in"
    puts "\tyour account, and enrichment may still be running."
  else
    clean_up(cloudwatch_client, names, started_here)
  end
  puts DASHES
end
```
+ For API details, see the following topics in *AWS SDK for Ruby API Reference*.
  + [DeleteAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarmMuteRule)
  + [DeleteAlarms](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteAlarms)
  + [DeleteDashboards](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DeleteDashboards)
  + [DescribeAlarmContributors](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/DescribeAlarmContributors)
  + [GetAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetAlarmMuteRule)
  + [GetDashboard](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetDashboard)
  + [GetMetricStatistics](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricStatistics)
  + [GetOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetOTelEnrichment)
  + [ListAlarmMuteRules](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListAlarmMuteRules)
  + [ListDashboards](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListDashboards)
  + [ListMetrics](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/ListMetrics)
  + [PutAlarmMuteRule](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutAlarmMuteRule)
  + [PutDashboard](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutDashboard)
  + [PutMetricAlarm](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricAlarm)
  + [StartOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StartOTelEnrichment)
  + [StopOTelEnrichment](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StopOTelEnrichment)

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudWatch with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.