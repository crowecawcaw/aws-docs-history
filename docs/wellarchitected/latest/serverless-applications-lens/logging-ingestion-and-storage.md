# Logging ingestion and storage

AWS Lambda uses CloudWatch Logs to store the output of the executions to identify and troubleshoot
problems on executions as well as monitoring the serverless application. These will impact
the cost in the CloudWatch Logs service in two dimensions: ingestion and storage.

Set appropriate logging levels and remove unnecessary logging information to optimize
log ingestion. Use environment variables to control the application logging level and sample
logging in DEBUG mode to ensure you have additional insight when necessary.

Set log retention periods for new and existing CloudWatch Logs groups. For log archival, export
and set cost-effective storage classes that best suit your needs.

If you are using CloudWatch to record metrics in your Lambda Environment consider using the
CloudWatch Embedded Metric Format (EMF) instead of using the CloudWatch PutMetricData API.

EMF enables you to ingest complex high-cardinality application data in the form of logs
and easily generate actionable metrics from them. The embedded metric format is a JSON
specification used to instruct CloudWatch Logs to automatically extract metric values embedded in
structured log events.

In such high-cardinality environments you might observe cost savings by having your
Lambda functions leverage the CloudWatch Embedded Metric Format since with EMF you do not pay the
per request charge of the CloudWatch PutMetricData API. With EMF you are only charged for Data
Ingestion per GB, Data Archival per GB and per Custom Metric.

The metrics created with EMF are created asynchronously by the CloudWatch service. This means
that by using EMF when processing logs might also reduce the execution duration of your
Lambda functions compared to using the PutMetricData API which is a synchronous call.

If you need to have a precise timestamp for each individual metric or you have
dimensions with the same key but different values, at the time of writing you will need to
log separate EMF blobs. This means increased data ingestion and storage per GB CloudWatch cost.

In those cases we recommend to evaluate if the increased log ingestion and storage cost
of EMF will be more expensive versus the benefit of not paying for the per request charge of
the CloudWatch PutMetricData API. Moreover if you need high resolution metrics CloudWatch PutMetricData
API might be a better fit versus EMF.
