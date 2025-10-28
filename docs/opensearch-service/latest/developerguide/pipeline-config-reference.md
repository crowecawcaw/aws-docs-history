# Supported plugins and options for

Amazon OpenSearch Ingestion pipelines

Amazon OpenSearch Ingestion supports a subset of sources, processors, and sinks within open source
[OpenSearch Data
Prepper](https://opensearch.org/docs/latest/data-prepper/ "https://opensearch.org/docs/latest/data-prepper/"). In addition, there are some constraints that OpenSearch Ingestion places on
the available options for each supported plugin. The following sections describe the plugins
and associated options that OpenSearch Ingestion supports.

###### Note

OpenSearch Ingestion doesn't support any buffer plugins because it automatically configures
a default buffer. You receive a validation error if you include a buffer in your
pipeline configuration.

###### Topics

- [Supported plugins](#ingestion-plugins "#ingestion-plugins")
- [Stateless versus stateful
  processors](#processor-stateful-stateless "#processor-stateful-stateless")
- [Configuration requirements and
  constraints](#ingestion-parameters "#ingestion-parameters")

## Supported plugins

OpenSearch Ingestion supports the following Data Prepper plugins:

**Sources**:

- [DocumentDB](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/documentdb/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/documentdb/")
- [DynamoDB](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/dynamo-db/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/dynamo-db/")

- [HTTP](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/")
- [Kafka](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/kafka/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/kafka/")
- [Kinesis](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/kinesis/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/kinesis/")
- [OpenSearch](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/opensearch/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/opensearch/")
- [OTel logs](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-logs-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-logs-source/")
- [OTel metrics](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/")
- [OTel trace](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/")
- [S3](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/")

**Processors**:

- [Add entries](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/add-entries/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/add-entries/")
- [Aggregate](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aggregate/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aggregate/")
- [Anomaly detector](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/anomaly-detector/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/anomaly-detector/")
- [AWS Lambda](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aws-lambda/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aws-lambda/")
- [Convert entry type](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/convert-entry-type/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/convert-entry-type/")
- [Copy values](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/copy-values/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/copy-values/")
- [CSV](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/csv/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/csv/")
- [Date](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/date/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/date/")
- [Delay](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/delay/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/delay/")
- [Decompress](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/decompress/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/decompress/")
- [Delete entries](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/delete-entries/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/delete-entries/")
- [Dissect](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/dissect/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/dissect/")
- [Drop events](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/drop-events/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/drop-events/")
- [Flatten](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/flatten/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/flatten/")
- [Geo IP](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/geoip/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/geoip/")
- [Grok](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/grok/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/grok/")
- [Key value](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/key-value/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/key-value/")
- [List to map](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/list-to-map/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/list-to-map/")
- [Lowercase string](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/lowercase-string/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/lowercase-string/")
- [Map to list](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/map-to-list/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/map-to-list/")
- [Mutate event](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/mutate-event/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/mutate-event/") (series of processors)
- [Mutate string](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/mutate-string/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/mutate-string/") (series of processors)
- [Obfuscate](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/obfuscate/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/obfuscate/")
- [OTel metrics](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/otel-metrics/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/otel-metrics/")
- [OTel trace group](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/otel-trace-group/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/otel-trace-group/")
- [OTel trace](https://docs.opensearch.org/latest/data-prepper/common-use-cases/trace-analytics/ "https://docs.opensearch.org/latest/data-prepper/common-use-cases/trace-analytics/")
- [Parse Ion](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/parse-ion/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/parse-ion/")
- [Parse JSON](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/parse-json/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/parse-json/")
- [Parse XML](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/parse-xml/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/parse-xml/")
- [Rename keys](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/rename-keys/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/rename-keys/")
- [Select entries](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/select-entries/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/select-entries/")
- [Service map](https://docs.opensearch.org/latest/data-prepper/common-use-cases/trace-analytics/ "https://docs.opensearch.org/latest/data-prepper/common-use-cases/trace-analytics/")
- [Split event](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/split-event/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/split-event/")
- [Split string](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/split-string/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/split-string/")
- [String converter](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/string-converter/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/string-converter/")
- [Substitute string](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/substitute-string/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/substitute-string/")
- [Trace peer forwarder](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/trace-peer-forwarder/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/trace-peer-forwarder/")
- [Translate](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/translate/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/translate/")
- [Trim string](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/trim-string/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/trim-string/")
- [Truncate](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/truncate/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/truncate/")
- [Uppercase string](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/uppercase-string/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/uppercase-string/")
- [User agent](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/user-agent/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/user-agent/")
- [Write JSON](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/write-json/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/write-json/")

**Sinks**:

- [OpenSearch](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/") (supports OpenSearch Service, OpenSearch Serverless, and Elasticsearch 6.8 or
  later)
- [S3](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/")

**Sink codecs**:

- [Avro](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/#avro-codec "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/#avro-codec")
- [NDJSON](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/#ndjson-codec "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/#ndjson-codec")
- [JSON](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/#json-codec "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/#json-codec")
- [Parquet](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/#parquet-codec "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/s3/#parquet-codec")

## Stateless versus stateful

processors

_Stateless_ processors perform operations like transformations and
filtering, while _stateful_ processors perform operations like
aggregations, which remember the result of the previous run. OpenSearch Ingestion supports
the stateful processors [Aggregate](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aggregate/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/aggregate/") and [Service-map](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/service-map/ "https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/service-map/"). All other supported processors are stateless.

For pipelines that contain only stateless processors, the maximum capacity limit is 96
Ingestion OCUs. If a pipeline contains any stateful processors, the maximum capacity
limit is 48 Ingestion OCUs. However, if a pipeline has [persistent buffering](osis-features-overview.md#persistent-buffering "osis-features-overview.md#persistent-buffering") enabled, it can have a
maximum of 384 Ingestion OCUs with only stateless processors, or 192 Ingestion OCUs if
it contains any stateful processors. For more information, see [Scaling pipelines in Amazon OpenSearch Ingestion](ingestion-scaling.md "ingestion-scaling.md").

End-to-end acknowledgment is only supported for stateless processors. For more
information, see [End-to-end acknowledgement](osis-features-overview.md#osis-features-e2e "osis-features-overview.md#osis-features-e2e").

## Configuration requirements and

constraints

Unless otherwise specified below, all options described in the Data Prepper
configuration reference for the supported plugins listed above are allowed in
OpenSearch Ingestion pipelines. The following sections explain the constraints that
OpenSearch Ingestion places on certain plugin options.

###### Note

OpenSearch Ingestion doesn't support any buffer plugins because it automatically
configures a default buffer. You receive a validation error if you include a buffer
in your pipeline configuration.

Many options are configured and managed internally by OpenSearch Ingestion, such as
`authentication` and `acm_certificate_arn`. Other options,
such as `thread_count` and `request_timeout`, have performance
impacts if changed manually. Therefore, these values are set internally to ensure
optimal performance of your pipelines.

Lastly, some options can't be passed to OpenSearch Ingestion, such as
`ism_policy_file` and `sink_template`, because they're local
files when run in open source Data Prepper. These values aren't supported.

###### Topics

- [General pipeline options](#ingestion-params-general "#ingestion-params-general")
- [Grok processor](#ingestion-params-grok "#ingestion-params-grok")
- [HTTP source](#ingestion-params-http "#ingestion-params-http")
- [OpenSearch sink](#ingestion-params-opensearch "#ingestion-params-opensearch")
- [OTel metrics source, OTel trace
  source, and OTel logs source](#ingestion-params-otel-source "#ingestion-params-otel-source")
- [OTel trace group processor](#ingestion-params-otel-trace "#ingestion-params-otel-trace")
- [OTel trace processor](#ingestion-params-otel-raw "#ingestion-params-otel-raw")
- [Service-map processor](#ingestion-params-servicemap "#ingestion-params-servicemap")
- [S3 source](#ingestion-params-s3 "#ingestion-params-s3")

### General pipeline options

The following [general pipeline options](https://docs.opensearch.org/latest/data-prepper/pipelines/pipelines/ "https://docs.opensearch.org/latest/data-prepper/pipelines/pipelines/") are set by OpenSearch Ingestion and aren't
supported in pipeline configurations:

- `workers`
- `delay`

### Grok processor

The following [Grok](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/grok/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/grok/") processor options aren't supported:

- `patterns_directories`
- `patterns_files_glob`

### HTTP source

The [HTTP](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/") source plugin has the following requirements and
constraints:

- The `path` option is _required_. The path is
  a string such as `/log/ingest`, which represents the URI path for
  log ingestion. This path defines the URI that you use to send data to the
  pipeline. For example,
  `https://log-pipeline.us-west-2.osis.amazonaws.com`/log/ingest``.
The path must start with a slash (/), and can contain the special characters
'-', '\_', '.', and '/', as well as the `${pipelineName}`
  placeholder.
- The following HTTP source options are set by OpenSearch Ingestion and aren't
  supported in pipeline configurations:
  - `port`
  - `ssl`
  - `ssl_key_file`
  - `ssl_certificate_file`
  - `aws_region`
  - `authentication`
  - `unauthenticated_health_check`
  - `use_acm_certificate_for_ssl`
  - `thread_count`
  - `request_timeout`
  - `max_connection_count`
  - `max_pending_requests`
  - `health_check_service`
  - `acm_private_key_password`
  - `acm_certificate_timeout_millis`
  - `acm_certificate_arn`

### OpenSearch sink

The [OpenSearch](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/") sink plugin has the following requirements and
limitations.

- The `aws` option is _required_, and must
  contain the following options:
  - `sts_role_arn`
  - `region`
  - `hosts`
  - `serverless` (if the sink is an OpenSearch Serverless
    collection)

- The `sts_role_arn` option must point to the same role for each
  sink within a YAML definition file.
- The `hosts` option must specify an OpenSearch Service domain endpoint or an
  OpenSearch Serverless collection endpoint. You can't specify a [custom endpoint](customendpoint.md "customendpoint.md") for a
  domain; it must be the standard endpoint.
- If the `hosts` option is a serverless collection endpoint, you
  must set the `serverless` option to `true`. In
  addition, if your YAML definition file contains the `index_type`
  option, it must be set to `management_disabled`, otherwise
  validation fails.
- The following options aren't supported:
  - `username`
  - `password`
  - `cert`
  - `proxy`
  - `dlq_file` - If you want to offload failed events to a
    dead letter queue (DLQ), you must use the `dlq` option
    and specify an S3 bucket.
  - `ism_policy_file`
  - `socket_timeout`
  - `template_file`
  - `insecure`

### OTel metrics source, OTel trace

source, and OTel logs source

The [OTel metrics](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/") source, [OTel trace](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/") source, and [OTel logs](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-logs-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-logs-source/") source plugins have the following requirements and
limitations:

- The `path` option is _required_. The path is
  a string such as `/log/ingest`, which represents the URI path for
  log ingestion. This path defines the URI that you use to send data to the
  pipeline. For example,
  `https://log-pipeline.us-west-2.osis.amazonaws.com`/log/ingest``.
The path must start with a slash (/), and can contain the special characters
'-', '\_', '.', and '/', as well as the `${pipelineName}`
  placeholder.
- The following options are set by OpenSearch Ingestion and aren't supported in
  pipeline configurations:
  - `port`
  - `ssl`
  - `sslKeyFile`
  - `sslKeyCertChainFile`
  - `authentication`
  - `unauthenticated_health_check`
  - `useAcmCertForSSL`
  - `unframed_requests`
  - `proto_reflection_service`
  - `thread_count`
  - `request_timeout`
  - `max_connection_count`
  - `acmPrivateKeyPassword`
  - `acmCertIssueTimeOutMillis`
  - `health_check_service`
  - `acmCertificateArn`
  - `awsRegion`

### OTel trace group processor

The [OTel trace group](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/otel-trace-group/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/processors/otel-trace-group/") processor has the following requirements and
limitations:

- The `aws` option is _required_, and must
  contain the following options:
  - `sts_role_arn`
  - `region`
  - `hosts`

- The `sts_role_arn` option specify the same role as the pipeline
  role that you specify in the OpenSearch sink configuration.
- The `username`, `password`, `cert`, and
  `insecure` options aren't supported.
- The `aws_sigv4` option is required and must be set to
  true.
- The `serverless` option within the OpenSearch sink plugin isn't
  supported. The Otel trace group processor doesn't currently work with OpenSearch Serverless
  collections.
- The number of `otel_trace_group` processors within the pipeline
  configuration body can't exceed 8.

### OTel trace processor

The [OTel trace](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/otel-traces/ "https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/otel-traces/") processor has the following requirements and
limitations:

- The value of the `trace_flush_interval` option can't exceed 300
  seconds.

### Service-map processor

The [Service-map](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/service-map/ "https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/processors/service-map/") processor has the following requirements and
limitations:

- The value of the `window_duration` option can't exceed 300
  seconds.

### S3 source

The [S3](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/s3/") source plugin has the following requirements and limitations:

- The `aws` option is _required_, and must
  contain `region` and `sts_role_arn` options.
- The value of the `records_to_accumulate` option can't exceed

200.

- The value of the `maximum_messages` option can't exceed

10.

- If specified, the `disable_bucket_ownership_validation` option
  must be set to false.
- If specified, the `input_serialization` option must be set to
  `parquet`.
