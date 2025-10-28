# Connect to an Amazon OpenSearch Service data

source

###### Note

In workspaces that support version 9 or newer, this data source might require
you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

With Amazon Managed Grafana, you can add Amazon OpenSearch Service as a data source by using the AWS data
source configuration option in the Grafana workspace console. This data source
supports OpenSearch Service domains, which run OpenSearch clusters as well as legacy
Elasticsearch clusters.

The AWS data source configuration option simplifies adding OpenSearch Service as a data
source by discovering your existing OpenSearch Service accounts, and manages the configuration of
the authentication credentials that are required to access OpenSearch. You can use
this method to set up authentication and add OpenSearch Service as a data source, or you can
manually set up the data source and the necessary authentication credentials using
the same method that you would on a self-managed Grafana server.

The OpenSearch Service data source supports piped processing language (PPL). For more
information about PPL, see [Querying
Amazon OpenSearch Service data using Piped Processing Language](../../../opensearch-service/latest/developerguide/ppl-support.md "../../../opensearch-service/latest/developerguide/ppl-support.md").

You can use the OpenSearch Service data source to perform many types of simple or complex
OpenSearch queries in order to visualize logs or metrics stored in OpenSearch.
You can also annotate your graphs with log events stored in OpenSearch.

###### Topics

- [Use AWS data source configuration to
  add OpenSearch Service as a data source](ES-adding-AWS-config.md "ES-adding-AWS-config.md")
- [Manually add Amazon OpenSearch Service as a data
  source](ES-adding-the-data-source.md "ES-adding-the-data-source.md")
- [OpenSearch Service settings](#ES-settings "#ES-settings")
- [Using the Amazon OpenSearch Service data source](ES-use-datasource.md "ES-use-datasource.md")
- [Amazon OpenSearch Service Serverless](datasources-opensearch-serverless.md "datasources-opensearch-serverless.md")
- [Traces support](datasources-opensearch-traces.md "datasources-opensearch-traces.md")

## OpenSearch Service settings

| Name       | Description                                                                                                                                   |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Name`     | The data source name. This is how you see the data source in panels and queries.                                                              |
| `Default`  | Default data source means that it will be pre-selected for new panels.                                                                        |
| `Url`      | The endpoint of your OpenSearch Service domain. The endpoint takes the following format: https://search-my-domain.us-east-1.es.amazonaws.com. |
| `Access`   | Server (default) = URL must be accessible from the Grafana backend/server. Browser = URL must be accessible from the browser.                 | Access mode controls how requests to the data source will be handled. Server should be the preferred way if nothing else is stated. ### Server access mode (default) All requests are made from the browser to Grafana backend or server, which forwards the requests to the data source, circumventing possible Cross-Origin Resource Sharing (CORS) requirements. If you select this access mode, the URL must be accessible from the Grafana backend or server. ### Browser (direct) access Amazon Managed Grafana does not support browser direct access. ### Index settings Here you can specify a default for the `time field` and specify the name of your OpenSearch index. You can use a time pattern for the index name or a wildcard character. ### OpenSearch/Elasticsearch version Specify your OpenSearch or legacy Elasticsearch version in the version dropdown menu. The version is important because there are differences in how queries are composed for each version. Currently, Grafana supports OpenSearch 1.0.x. Supported versions of Elasticsearch are `2.0+`, `5.0+`, `5.6+`, `6.0+`, and `7.0+`. The value `5.6+` means version 5.6 or higher, but lower than 6.0. The value `6.0+` means version 6.0 or higher, but lower than 7.0. Finally, `7.0+` means version 7.0 or higher, but lower than 8.0. ### Min time interval A lower limit for the auto group by time interval. Recommended to be set to write frequency; for example, `1m` if your data is written every minute. This option can also be overridden/configured in a dashboard panel under data source options. This value **must** be formatted as a number followed by a valid time identifier; for example, `1m` (1 minute) or `30s` (30 seconds). The following time identifiers are supported. |
| Identifier | Description                                                                                                                                   |
| ---        | ---                                                                                                                                           |
| `y`        | Year                                                                                                                                          |
| `M`        | Month                                                                                                                                         |
| `w`        | Week                                                                                                                                          |
| `d`        | Day                                                                                                                                           |
| `h`        | Hour                                                                                                                                          |
| `m`        | Minute                                                                                                                                        |
| `s`        | Second                                                                                                                                        |
| `ms`       | Millisecond                                                                                                                                   | ### Logs Two parameters, `Message field name` and `Level field name`, can optionally be configured from the data source settings page that determine which fields will be used for log messages and log levels when visualizing logs in [Explore](explore.md "explore.md"). For example, if you use a default setup of Filebeat for shipping logs to OpenSearch Service, the following configuration should work. <br>• **Message field name:** message <br>• **Level field name:** fields.level ### Data links Data links create a link from a specified field that can be accessed in logs view in Explore. Each data link configuration consists of the following: <br>• **Field** – Name of the field used by the data link. <br>• **URL/query** – If the link is external, then enter the full link URL. If the link is internal link, then this input serves as query for the target data source. In both cases, you can interpolate the value from the field with `${__value.raw }` macro. <br>• **Internal link** – Select this if the link is internal or external. If the link is internal, a data source selector allows you to select the target data source. Only tracing data sources are supported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
