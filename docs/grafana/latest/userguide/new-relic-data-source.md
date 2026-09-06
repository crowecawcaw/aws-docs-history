

# Connect to a New Relic data source
<a name="new-relic-data-source"></a>

 This section covers New Relic [APM](https://newrelic.com/products/application-monitoring) and [Insights](https://newrelic.com/products/insights) for Grafana. 

**Note**  
This data source is for Grafana Enterprise only. For more information, see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md).  
Additionally, in workspaces that support version 9 or newer, this data source might require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md).

## Features
<a name="newrelic-features"></a>
+  Template variables 
  +  Metric names 
  +  Metric values 
+  Annotations 
+  Aliasing 
  +  Metric names 
  +  Metric values 
+  Ad-hoc filters 
  +  Not currently supported 
+  Alerting 

## Configuration
<a name="newrelic-configuration"></a>

 Add the data source, filling out the fields for your [admin API key](https://docs.newrelic.com/docs/apis/get-started/intro-apis/types-new-relic-api-keys#admin), [personal API key](https://docs.newrelic.com/docs/apis/get-started/intro-apis/types-new-relic-api-keys#personal-api-key) and [account ID](https://docs.newrelic.com/docs/accounts/install-new-relic/account-setup/account-id). 

## Usage
<a name="newrelic-usage"></a>

### Service types
<a name="newrelic-service-types"></a>
+  **Metrics**; for querying New Relic APM via New Relic’s [REST API](https://docs.newrelic.com/docs/apis/rest-api-v2). 
+  **Insights**; for querying New Relic Insights via [NRQL](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/nrql-resources/nrql-syntax-components-functions). 

### Aliases
<a name="newrelic-aliases"></a>

 You can combine plaintext with the following variables to produce custom output. 


|  Variable  |  Description  |  Example value  | 
| --- | --- | --- | 
|  $\_\_nr\_metric  |  Metric name  |  CPU/User time  | 
|  $\_\_nr\_metric\_value  |  Metric values  |  average\_value  | 

For example:

```
    <para>
      Server: $__nr_server Metric: $__nr_metric
    </para>
    <programlisting>
```

### Templates and variables
<a name="newrelic-templates-and-variables"></a>

1.  Create a template variable for your dashboard. For more information, see [Templates and variables](templates-and-variables.md). 

1.  Select the "Query" type. 

1.  Select the "New Relic" data source. 

1.  Formulate a query using relative [REST API](https://docs.newrelic.com/docs/apis/rest-api-v2) endpoints (excluding file extensions). 

List of available applications:

```
    <para>
      applications
    </para>
    <programlisting>
```

List of available metrics for an application:

```
    <para>
      applications/{application_id}/metrics
    </para>
    <programlisting>
```

### NRQL macros
<a name="nrql-macros"></a>

 To improve the writing experience when creating New Relic Query Language (NRQL) queries, the editor supports predefined macros: 
+  `$__timeFilter` (or `[[timeFilter]]`) will interpolate to `SINCE &lt;from&gt; UNTIL &lt;to&gt;` based on your dashboard’s time range. 

Example:

```
    <para>
      SELECT average(value) FROM $event_template_variable
      $__timeFilter TIMESERIES
    </para>
    <programlisting>
```

 For further hints on how to use macros and template variables, refer to the editor’s help section. 

### Alert events
<a name="newrelic-alert-events"></a>

 Select your New Relic data source and set additional filters. Without any filters set, all events will be returned. 

 If you want to filter events by *Entity ID*, use template variables because you will be able to select the entity name instead of ID. For example, to filter events for a particular application, create a variable `_$app_` which retrieves a list of apps and uses it as an *Entity ID* filter. 

### Deployment events
<a name="newrelic-deployment-events"></a>

 *Application ID* is a required field. 