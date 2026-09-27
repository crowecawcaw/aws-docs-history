

# Data retrieval APIs for Amazon CloudWatch
<a name="amazoncloudwatch"></a>

Amazon CloudWatch provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="cloudwatch-BatchGetServiceLevelIndicatorReport"></a>[BatchGetServiceLevelIndicatorReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Batch get service level indicator report | Read | 
| <a name="cloudwatch-BatchGetServiceLevelObjectiveBudgetReport"></a>[BatchGetServiceLevelObjectiveBudgetReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Batch retrieve a service level objective budget report | Read | 
| <a name="cloudwatch-DescribeAlarmHistory"></a>[DescribeAlarmHistory](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html) | Retrieve the history for the specified alarm | Read | 
| <a name="cloudwatch-DescribeAlarms"></a>[DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) | Describe all alarms, currently owned by the user's account | Read | 
| <a name="cloudwatch-DescribeAlarmsForMetric"></a>[DescribeAlarmsForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmsForMetric.html) | Describe all alarms configured on the specified metric, currently owned by the user's account | Read | 
| <a name="cloudwatch-DescribeAnomalyDetectors"></a>[DescribeAnomalyDetectors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAnomalyDetectors.html) | List the anomaly detection models that you have created in your account | Read | 
| <a name="cloudwatch-DescribeInsightRules"></a>[DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html) | Describe all insight rules, currently owned by the user's account | Read | 
| <a name="cloudwatch-GenerateQuery"></a>[GenerateQuery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-query-assist.html) | Generate a Metrics Insights or Logs Insights query string from a natural language prompt | Read | 
| <a name="cloudwatch-GenerateQueryResultsSummary"></a>[GenerateQueryResultsSummary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-Results-Summary.html) | Generate a summary of CloudWatch LogInsights query results in natural language using generative AI | Read | 
| <a name="cloudwatch-GetAccessGrant"></a>[GetAccessGrant](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAccessGrant.html) | Get an access grant | Read | 
| <a name="cloudwatch-GetAccessProfile"></a>[GetAccessProfile](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAccessProfile.html) | Get an access profile | Read | 
| <a name="cloudwatch-GetAgentGraph"></a>[GetAgentGraph](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAgentGraph.html) | Get an agent graph | Read | 
| <a name="cloudwatch-GetAlarmMuteRule"></a>[GetAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetAlarmMuteRule.html) | Get an alarm mute rule | Read | 
| <a name="cloudwatch-GetAlert"></a>[GetAlert](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetAlert.html) | Get an alert | Read | 
| <a name="cloudwatch-GetContextGraph"></a>[GetContextGraph](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetContextGraph.html) | Get a context graph | Read | 
| <a name="cloudwatch-GetDashboard"></a>[GetDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDashboard.html) | Display the details of the CloudWatch dashboard you specify | Read | 
| <a name="cloudwatch-GetDataset"></a>[GetDataset](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDataset.html) | Get a dataset | Read | 
| <a name="cloudwatch-GetDomain"></a>[GetDomain](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetDomain.html) | Get a domain | Read | 
| <a name="cloudwatch-GetDomainAccessGrantForOrganization"></a>[GetDomainAccessGrantForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetDomainAccessGrantForOrganization.html) | Get a domain access grant for an organization | Read | 
| <a name="cloudwatch-GetDomainForOrganization"></a>[GetDomainForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetDomainForOrganization.html) | Get a domain for an organization | Read | 
| <a name="cloudwatch-GetIngestionEndpoint"></a>[GetIngestionEndpoint](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetIngestionEndpoint.html) | Get an ingestion endpoint | Read | 
| <a name="cloudwatch-GetInsightRuleReport"></a>[GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html) | Return the top-N report of unique contributors over a time range for a given insight rule | Read | 
| <a name="cloudwatch-GetIntegration"></a>[GetIntegration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetIntegration.html) | Get an integration | Read | 
| <a name="cloudwatch-GetIntelligenceConfiguration"></a>[GetIntelligenceConfiguration](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetIntelligenceConfiguration.html) | Get an intelligence configuration | Read | 
| <a name="cloudwatch-GetMetricData"></a>[GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) | Retrieve batch amounts of CloudWatch classic metric data and perform metric math on retrieved data; and grants permission to retrieve OTLP metric data using PromQL | Read | 
| <a name="cloudwatch-GetMetricStatistics"></a>[GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) | Retrieve statistics for the specified metric | Read | 
| <a name="cloudwatch-GetMetricStream"></a>[GetMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStream.html) | Return the details of a CloudWatch metric stream | Read | 
| <a name="cloudwatch-GetMetricWidgetImage"></a>[GetMetricWidgetImage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricWidgetImage.html) | Retrieve snapshots of metric widgets | Read | 
| <a name="cloudwatch-GetOTelEnrichment"></a>[GetOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html) | Retrieve the status of OTel Enrichment of vended metrics for PromQL querying | Read | 
| <a name="cloudwatch-GetOmniDashboard"></a>[GetOmniDashboard](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetOmniDashboard.html) | Get an omni dashboard | Read | 
| <a name="cloudwatch-GetOmniThread"></a>[GetOmniThread](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetOmniThread.html) | Get an omni thread | Read | 
| <a name="cloudwatch-GetPreferences"></a>[GetPreferences](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetPreferences.html) | Get preferences | Read | 
| <a name="cloudwatch-GetRecords"></a>[GetRecords](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetRecords.html) | Fetch logs, metrics, and traces | Read | 
| <a name="cloudwatch-GetService"></a>[GetService](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Retrieve information about a service | Read | 
| <a name="cloudwatch-GetServiceData"></a>[GetServiceData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html) | Retrieve service data | Read | 
| <a name="cloudwatch-GetServiceLevelObjective"></a>[GetServiceLevelObjective](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Retrieve information about service level objective | Read | 
| <a name="cloudwatch-GetSpace"></a>[GetSpace](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpace.html) | Get a space | Read | 
| <a name="cloudwatch-GetSpaceCredentials"></a>[GetSpaceCredentials](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpaceCredentials.html) | Get space credentials | Read | 
| <a name="cloudwatch-GetSpaceCredentialsForOrganization"></a>[GetSpaceCredentialsForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetSpaceCredentialsForOrganization.html) | Get space credentials for an organization | Read | 
| <a name="cloudwatch-GetTelemetryQueryResults"></a>[GetTelemetryQueryResults](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetTelemetryQueryResults.html) | Get telemetry query results | Read | 
| <a name="cloudwatch-GetTopologyDiscoveryStatus"></a>[GetTopologyDiscoveryStatus](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html) | Retrieve a CloudWatch topology discovery status | Read | 
| <a name="cloudwatch-GetTopologyMap"></a>[GetTopologyMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | Retrieve a CloudWatch topology map | Read | 
| <a name="cloudwatch-GetView"></a>[GetView](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_GetView.html) | Get a view | Read | 
| <a name="cloudwatch-ListAccessGrants"></a>[ListAccessGrants](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAccessGrants.html) | List access grants | List | 
| <a name="cloudwatch-ListAccessProfiles"></a>[ListAccessProfiles](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAccessProfiles.html) | List access profiles | List | 
| <a name="cloudwatch-ListAlarmMuteRules"></a>[ListAlarmMuteRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListAlarmMuteRules.html) | Retrieve a list of alarm mute rules owned by the user's account | List | 
| <a name="cloudwatch-ListAlertContributors"></a>[ListAlertContributors](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAlertContributors.html) | List alert contributors | List | 
| <a name="cloudwatch-ListAlerts"></a>[ListAlerts](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListAlerts.html) | List alerts | List | 
| <a name="cloudwatch-ListDashboards"></a>[ListDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListDashboards.html) | Return a list of all CloudWatch dashboards in your account | List | 
| <a name="cloudwatch-ListDomainAccessGrantsForOrganization"></a>[ListDomainAccessGrantsForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListDomainAccessGrantsForOrganization.html) | List domain access grants for an organization | List | 
| <a name="cloudwatch-ListDomains"></a>[ListDomains](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListDomains.html) | List domains | List | 
| <a name="cloudwatch-ListEntitiesForMetric"></a>[ListEntitiesForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html) | Retrieve all the entities that are emitting a given metric | List | 
| <a name="cloudwatch-ListIngestionEndpoints"></a>[ListIngestionEndpoints](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListIngestionEndpoints.html) | List ingestion endpoints | List | 
| <a name="cloudwatch-ListIntegrations"></a>[ListIntegrations](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListIntegrations.html) | List integrations | List | 
| <a name="cloudwatch-ListManagedInsightRules"></a>[ListManagedInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListManagedInsightRules.html) | List available managed Insight Rules for a given Resource ARN | Read | 
| <a name="cloudwatch-ListMetricStreams"></a>[ListMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetricStreams.html) | Return a list of all CloudWatch metric streams in your account | List | 
| <a name="cloudwatch-ListMetrics"></a>[ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html) | Retrieve a list of valid metrics stored for the AWS account owner | List | 
| <a name="cloudwatch-ListOmniDashboards"></a>[ListOmniDashboards](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListOmniDashboards.html) | List omni dashboards | List | 
| <a name="cloudwatch-ListOmniThreads"></a>[ListOmniThreads](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListOmniThreads.html) | List omni threads | List | 
| <a name="cloudwatch-ListServiceLevelObjectives"></a>[ListServiceLevelObjectives](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | List service level objectives | List | 
| <a name="cloudwatch-ListServices"></a>[ListServices](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html#ApplicationSignals-PreviewSDK) | List services | List | 
| <a name="cloudwatch-ListSpaceAccess"></a>[ListSpaceAccess](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListSpaceAccess.html) | List access to a space | List | 
| <a name="cloudwatch-ListSpaces"></a>[ListSpaces](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListSpaces.html) | List spaces | List | 
| <a name="cloudwatch-ListSpacesForOrganization"></a>[ListSpacesForOrganization](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListSpacesForOrganization.html) | List spaces for an organization | List | 
| <a name="cloudwatch-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.html) | List tags for an Amazon CloudWatch resource | List | 
| <a name="cloudwatch-ListTelemetryFields"></a>[ListTelemetryFields](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListTelemetryFields.html) | List telemetry fields | List | 
| <a name="cloudwatch-ListTelemetryQuerySessions"></a>[ListTelemetryQuerySessions](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListTelemetryQuerySessions.html) | List telemetry query sessions | List | 
| <a name="cloudwatch-ListViews"></a>[ListViews](https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_ListViews.html) | List views | List | 