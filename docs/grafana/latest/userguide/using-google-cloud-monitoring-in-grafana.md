

# Connect to a Google Cloud Monitoring data source
<a name="using-google-cloud-monitoring-in-grafana"></a>

**Note**  
 In earlier versions of Grafana, this data source was named Google Stackdriver. 

 Add the Google Cloud Monitoring data source to be able to build dashboards for your Google Cloud Monitoring metrics. 

## Adding the data source
<a name="google-adding-the-data-source"></a>

1.  Open the side menu by choosing the Grafana icon in the top header. 

1.  In the side menu, under the **Dashboards** link, you should find the **Data Sources** link. 

1.  Choose the **\+ Add data source** button in the top header. 

1.  Select **Google Cloud Monitoring** from the **Type** dropdown list. 

1.  Upload or paste in the Service Account Key file. See later in this document for steps to create a Service Account Key file. 

**Note**  
 If you don't see the **Data Sources** link in your side menu, your current user does not have the `Admin` role. 


|  Name  |  Description  | 
| --- | --- | 
|  Name  |  The data source name. This is how you refer to the data source in panels and queries.  | 
|  Default  |  Default data source means that it will be pre-selected for new panels.  | 
|  Service Account Key  |  Service account key file for a GCP Project. See the instructions later in this document about how to create it.  | 

## Authentication
<a name="google-authentication"></a>

 There are two ways to authenticate the Google Cloud Monitoring plugin
+ Upload a Google JWT file
+ Automatically retrieve credentials from Google metadata server

The latter option is only available when running Grafana on GCE virtual machine. 

### Using a Google service account key file
<a name="using-a-google-service-account-key-file"></a>

 To authenticate with the Google Cloud Monitoring API, you must create a Google Cloud Platform (GCP) Service Account for the Project that you want to show data for. A Grafana data source integrates with one GCP Project. To visualize data from multiple GCP Projects, you must create one data source per GCP Project. 

#### Enabling APIs
<a name="google-enable-apis"></a>

 The following APIs must be enabled first: 
+  [Monitoring API](https://console.cloud.google.com/apis/library/monitoring.googleapis.com) 
+  [Cloud Resource Manager API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com) 

 Choose the links listed, and then choose the **Enable** button.

#### Creating a GCP service account for a Project
<a name="create-a-gcp-service-account-for-a-project"></a>

1.  Navigate to the [APIs and Services Credentials page](https://console.cloud.google.com/apis/credentials). 

1.  Choose the **Create credentials** dropdown/button and choose the **Service account key** option. 

    {{< docs-imagebox img="/img/docs/v71/cloudmonitoring\_create\_service\_account\_button.png" class="docs-image–no-shadow" caption="Create service account button" >}} 

1.  On the **Create service account key** page, choose key type `JSON`. Then, in the **Service Account** dropdown list, choose the **New service account** option. 

    {{< docs-imagebox img="/img/docs/v71/cloudmonitoring\_create\_service\_account\_key.png" class="docs-image–no-shadow" caption="Create service account key" >}} 

1.  Some new fields will appear. Fill in a name for the service account in the **Service account name** field and then choose the **Monitoring Viewer** role from the **Role** dropdown list. 

    {{< docs-imagebox img="/img/docs/v71/cloudmonitoring\_service\_account\_choose\_role.png" class="docs-image–no-shadow" caption="Choose role" >}} 

1.  Choose the **Create** button. A JSON key file will be created and downloaded to your computer. Store this file in a secure place as it allows access to your Google Cloud Monitoring data. 

1.  Upload it to Grafana on the data source **Configuration** page. You can either upload the file or paste in the contents of the file. 

    {{< docs-imagebox img="/img/docs/v71/cloudmonitoring\_grafana\_upload\_key.png" class="docs-image–no-shadow" caption="Upload service key file to Grafana" >}} 

1.  The file contents will be encrypted and saved in the Grafana database. Don’t forget to save after uploading the file\! 

    {{< docs-imagebox img="/img/docs/v71/cloudmonitoring\_grafana\_key\_uploaded.png" class="docs-image–no-shadow" caption="Service key file is uploaded to Grafana" >}} 

## Using the query editor
<a name="google-using-the-query-editor"></a>

 The Google Cloud Monitoring query editor allows you to build two types of queries - **Metric** and **Service Level Objective (SLO)**. Both types return time series data. 

### Metric queries
<a name="google-metric-queries"></a>

 The metric query editor allows you to select metrics, group/aggregate by labels and by time, and use filters to specify which time series you want in the results. 

 To create a metric query, follow these steps: 

1.  Choose the option **Metrics** in the **Query Type** dropdown list. 

1.  Choose a project from the **Project** dropdown list. 

1.  Choose a Google Cloud Platform service from the **Service** dropdown list. 

1.  Choose a metric from the **Metric** dropdown list. 

1.  To add or remove filters or group by clauses, use the plus and minus icons in the filter and group by sections. This step is optional. 

 Google Cloud Monitoring metrics can be of different kinds (GAUGE, DELTA, CUMULATIVE) and these kinds have support for different aggregation options (reducers and aligners). The Grafana query editor shows the list of available aggregation methods for a selected metric and sets a default reducer and aligner when you select the metric. Units for the Y-axis are also automatically selected by the query editor. 

#### Filters
<a name="google-filter"></a>

 To add a filter, choose the plus icon, choose a field to filter by, and enter a filter value. For example, enter `instance_name = grafana-1`. You can remove the filter by choosing the filter name and selecting `--remove filter--`. 

##### Simple wildcard characters
<a name="google-simple-wildcards"></a>

 When the operator is set to or ,`=``!=` it is possible to add wildcard characters to the filter value field. For example, `us-*` captures all values that start with "us-", and `*central-a` captures all values that end with "central-a". `*-central-*` captures all values that have the substring of `central-`. Simple wildcard characters are less expensive than regular expressions.

##### Regular expressions
<a name="google-regular-expressions"></a>

 When the operator is set to or ,`=~``!=~` it is possible to add regular expressions to the filter value field. For example, `us-central[1-3]-[af]` matches all values that start with "us-central", followed by a number in the range of 1 to 3, a dash and then either an "a" or an "f". Leading and trailing slashes are not needed when creating regular expressions.

#### Aggregation
<a name="google-aggregation"></a>

 The aggregation field lets you combine time series based on common statistics. For more information about aggregation, refer to [aggregation options](https://cloud.google.com/monitoring/charts/metrics-selector#aggregation-options). 

 The `Aligner` field allows you to align multiple time series after the same group by time interval. For more information about aligner, refer to [alignment metric selector](https://cloud.google.com/monitoring/charts/metrics-selector#alignment). 

##### Alignment Period and grouping by time
<a name="alignment-periodgroup-by-time"></a>

 The `Alignment Period` groups a metric by time if an aggregation is chosen. The default is to use the GCP Google Cloud Monitoring default groupings (which allows you to compare graphs in Grafana with graphs in the Google Cloud Monitoring UI). The option is called `cloud monitoring auto` and the defaults are: 
+  1m for time ranges < 23 hours 
+  5m for time ranges >= 23 hours and < 6 days 
+  1h for time ranges >= 6 days 

 The other automatic option is `grafana auto`. This will automatically set the group by time depending on the time range chosen and the width of the graph panel. For more information, see [Adding an interval variable](variables-types.md#add-an-interval-variable). 

 It is also possible to choose fixed time intervals to group by, such as `1h` or `1d`. 

#### Group By
<a name="google-group-by"></a>

 Group by resource or metric labels to reduce the number of time series and to aggregate the results by a group by. For example, group by instance\_name to see an aggregated metric for a compute instance. 

##### Metadata labels
<a name="google-metadata-labels"></a>

 Resource metadata labels contain information to uniquely identify a resource in Google Cloud. Metadata labels are only returned in the time series response if they’re part of the **Group By** segment in the time series request. There’s no API for retrieving metadata labels, so it’s not possible to populate the group by dropdown list with the metadata labels that are available for the selected service and metric. However, the **Group By** field dropdown list comes with a pre-defined list of common system labels. 

 User labels cannot be pre-defined, but it’s possible to enter them manually in the **Group By** field. If a metadata label, user label, or system label is included in the **Group By** segment, you can create filters based on it and expand its value in the **Alias** field. 

#### Alias patterns
<a name="google-alias-patterns"></a>

 The Alias By field allows you to control the format of the legend keys. The default is to show the metric name and labels. This can be long and hard to read. Using the following patterns in the alias field, you can format the legend key the way you want it. 

#### Metric Type patterns
<a name="metric-type-patterns"></a>


|  Alias pattern  |  Description  |  Example result  | 
| --- | --- | --- | 
|  {{metric.type}}  |  Returns the full Metric Type.  |  compute.googleapis.com/instance/cpu/utilization  | 
|  {{metric.name}}  |  Returns the metric name part.  |  instance/cpu/utilization  | 
|  {{metric.service}}  |  Returns the service part.  |  compute  | 

#### Label patterns
<a name="google-label-patterns"></a>

 In the Group By dropdown list, you can see a list of metric and resource labels for a metric. These can be included in the legend key using alias patterns. 


|  Alias pattern format  |  Description  |  Alias pattern example  |  Example result  | 
| --- | --- | --- | --- | 
|  {{metric.label.xxx}}  |  Returns the metric label value. |  {{metric.label.instance\_name}}  |  grafana-1-prod  | 
|  {{resource.label.xxx}}  |  Returns the resource label value.  |  {{resource.label.zone}}  |  us-east1-b  | 
|  {{metadata.system\_labels.xxx}}  |  Returns the metadata system label value.  |  {{metadata.system\_labels.name}}  |  grafana  | 
|  {{metadata.user\_labels.xxx}}  |  Returns the metadata user label value.  |  {{metadata.user\_labels.tag}}  |  production  | 

 Example Alias By: `{{metric.type}} - {{metric.label.instance_name}}` 

 Example Result: `compute.googleapis.com/instance/cpu/usage_time - server1-prod` 

 It is also possible to resolve the name of the Monitored Resource Type. 


|  Alias pattern format  |  Description  |  Example result  | 
| --- | --- | --- | 
|  {{resource.type}}  |  Returns the name of the monitored resource type.  |  gce\_instance  | 

 Example Alias By: `{{resource.type}} - {{metric.type}}` 

 Example Result: `gce_instance - compute.googleapis.com/instance/cpu/usage_time` 

### SLO queries
<a name="slo-service-level-objective-queries"></a>

**Note**  
 SLO queries are available only in Grafana v7.0\+ 

The SLO query builder in the Google Cloud Monitoring data source allows you to display SLO data in time series format. To get an understanding of the basic concepts in service monitoring, refer to the Google Cloud Monitoring [official documentation](https://cloud.google.com/monitoring/service-monitoring).

#### Creating an SLO query
<a name="how-to-create-an-slo-query"></a>

 To create an SLO query, follow these steps: 

1.  Choose the option **Service Level Objectives (SLO)** in the **Query Type** dropdown list. 

1.  Choose a project from the **Project** dropdown list. 

1.  Choose an [SLO service](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services) from the **Service** dropdown list. 

1.  Choose an [SLO](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives) from the **SLO** dropdown list. 

1.  Choose a [time series selector](https://cloud.google.com/monitoring/service-monitoring/timeseries-selectors#ts-selector-list) from the **Selector** dropdown list. 

 The friendly names for the time series selectors are shown in Grafana. The following table shows the mapping from the friendly name to the system name that is used in the Service Monitoring documentation.


|  Selector dropdown list value  |  Corresponding time series selector used  | 
| --- | --- | 
|  SLI Value  |  select\_slo\_health  | 
|  SLO Compliance  |  select\_slo\_compliance  | 
|  SLO Error Budget Remaining  |  select\_slo\_budget\_fraction  | 

#### Alias patterns for SLO queries
<a name="alias-patterns-for-slo-queries"></a>

 You can use the Alias By field to control the format of the legend keys for SLO queries. 


|  Alias pattern  |  Description  |  Example result  | 
| --- | --- | --- | 
|  {{project}}  |  Returns the GCP project name.  |  myProject  | 
|  {{service}}  |  Returns the service name.  |  myService  | 
|  {{slo}}  |  Returns the SLO.  |  latency-slo  | 
|  {{selector}}  |  Returns the selector.  |  select\_slo\_health  | 

#### Alignment Period and grouping by time for SLO queries
<a name="alignment-periodgroup-by-time-for-slo-queries"></a>

 SLO queries use the same alignment period functionality as metric queries. For more information, see [Metric queries](#google-metric-queries). 

## Templating
<a name="google-templating"></a>

 Instead of hardcoding things such as server, application and sensor name in your metric queries you can use variables in their place. Variables are shown as dropdown select boxes at the top of the dashboard. You can use these dropdown boxes to change the data being displayed in your dashboard. 

 For more information about templating and template variables, see [Templates and variables](templates-and-variables.md). 

### Query variable
<a name="google-query-variable"></a>

 Variable of the type *Query* allows you to query Google Cloud Monitoring for various types of data. The Google Cloud Monitoring data source plugin provides the following `Query Types`. 


|  Name  |  Description  | 
| --- | --- | 
|  Metric Types  |  Returns a list of metric type names that are available for the specified service.  | 
|  Labels Keys  |  Returns a list of keys for metric label and resource label in the specified metric.  | 
|  Labels Values  |  Returns a list of values for the label in the specified metric.  | 
|  Resource Types  |  Returns a list of resource types for the specified metric.  | 
|  Aggregations  |  Returns a list of aggregations (cross series reducers) for the specified metric.  | 
|  Aligners  |  Returns a list of aligners (per series aligners) for the specified metric.  | 
|  Alignment periods  |  Returns a list of all alignment periods that are available in Google Cloud Monitoring query editor in Grafana.  | 
|  Selectors  |  Returns a list of selectors that can be used in SLO (Service Level Objectives) queries.  | 
|  SLO Services  |  Returns a list of Service Monitoring services that can be used in SLO queries.  | 
|  Service Level Objectives (SLO)  |  Returns a list of SLO’s for the specified SLO service.  | 

### Using variables in queries
<a name="google-using-variables-in-queries"></a>

 There are two syntaxes: 
+  `$<varname>` Example: `metric.label.$metric_label` 
+  `[[varname]]` Example: `metric.label.[[metric_label]]` 

 Why two ways? The first syntax is easier to read and write but does not allow you to use a variable in the middle of a word. When the *Multi-value* or *Include all value* options are enabled, Grafana converts the labels from plaintext to a regex compatible string, which means you have to use `=~` instead of `=`. 

## Annotations
<a name="google-annotations"></a>

 You can use annotations to overlay rich event information on top of graphs. You add annotation queries via the Dashboard menu / Annotations view. Annotation rendering is expensive so it is important to limit the number of rows returned. There is no support for showing Google Cloud Monitoring annotations and events yet but it works well with [custom metrics](https://cloud.google.com/monitoring/custom-metrics/) in Google Cloud Monitoring.

For more information about annotations, see [Annotations](dashboard-annotations.md). 

 With the query editor for annotations, you can select a metric and filters. The **Title** and **Text** fields support templating and can use data returned from the query. For example, the Title field could have the following text: 

 `{{metric.type}} has value: {{metric.value}}` 

 Example Result: `monitoring.googleapis.com/uptime_check/http_status has this value: 502` 

### Patterns for the annotation query editor
<a name="patterns-for-the-annotation-query-editor"></a>


|  Alias pattern format  |  Description  |  Alias pattern example  |  Example result  | 
| --- | --- | --- | --- | 
|  {{metric.value}}  |  Value of the metric/point.  |  {{metric.value}}  |  555  | 
|  {{metric.type}}  |  Returns the full Metric Type.  |  {{metric.type}}  |  compute.googleapis.com/instance/cpu/utilization  | 
|  {{metric.name}}  |  Returns the metric name part. |  {{metric.name}}  |  instance/cpu/utilization  | 
|  {{metric.service}}  |  Returns the service part.  |  {{metric.service}}  |  compute  | 
|  {{metric.label.xxx}}  |  Returns the metric label value.  |  {{metric.label.instance\_name}}  |  grafana-1-prod  | 
|  {{resource.label.xxx}}  |  Returns the resource label value.  |  {{resource.label.zone}}  |  us-east1-b  | 

## Deep linking from Grafana panels to the Metrics Explorer in Google Cloud Console
<a name="deep-linking-from-grafana-panels-to-the-metrics-explorer-in-google-cloud-console"></a>

**Note**  
 This feature is available only for Metric queries. 

 Choose a time series in the panel to see a context menu with a link to View in Metrics Explorer in Google Cloud Console. Choosing that link opens the Metrics Explorer in the Google Cloud Console and runs the query from the Grafana panel there. The link navigates the user first to the Google Account Chooser. After successfully selecting an account, the user is redirected to the Metrics Explorer. The provided link is valid for any account, but it only displays the query if your account has access to the GCP project specified in the query. 