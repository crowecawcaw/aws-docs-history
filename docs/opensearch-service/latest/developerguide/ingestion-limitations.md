# Limitations of Amazon OpenSearch Ingestion

OpenSearch Ingestion has the following limitations:

- You can only ingest data into domains running OpenSearch 1.0 or later, or
  Elasticsearch 6.8 or later. If you're using the [OTel trace](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/") source, we recommend using Elasticsearch 7.9 or later so
  that you can use the [OpenSearch Dashboards plugin](https://opensearch.org/docs/latest/observability-plugin/trace/ta-dashboards/ "https://opensearch.org/docs/latest/observability-plugin/trace/ta-dashboards/").
- If a pipeline is writing to an OpenSearch Service domain that's within a VPC, the pipeline
  must be created in the same AWS Region as the domain.
- You can only configure a single data source within a pipeline
  definition.
- You can't specify [self-managed OpenSearch clusters](https://opensearch.org/docs/latest/about/#clusters-and-nodes "https://opensearch.org/docs/latest/about/#clusters-and-nodes") as sinks.
- You can't specify a [custom
  endpoint](customendpoint.md "customendpoint.md") as a sink. You can still write to a domain that has custom
  endpoints enabled, but you must specify its standard endpoint.
- You can't specify resources within [opt-in Regions](../../../controltower/latest/userguide/opt-in-region-considerations.md "../../../controltower/latest/userguide/opt-in-region-considerations.md") as sources or sinks.
- There are some constraints on the parameters that you can include in a
  pipeline configuration. For more information, see [Configuration requirements and
  constraints](pipeline-config-reference.md#ingestion-parameters "pipeline-config-reference.md#ingestion-parameters").
