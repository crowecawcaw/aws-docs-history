# Tracing AWS SDK calls with the

X-Ray SDK for Python

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

When your application makes calls to AWS services to store data, write to a queue, or send
notifications, the X-Ray SDK for Python tracks the calls downstream in [subsegments](xray-sdk-python-subsegments.md "xray-sdk-python-subsegments.md"). Traced AWS services and resources
that you access within those services (for example, an Amazon S3 bucket or Amazon SQS queue), appear as
downstream nodes on the trace map in the X-Ray console.

The X-Ray SDK for Python automatically instruments all AWS SDK clients when you [patch the botocore library](xray-sdk-python-patching.md "xray-sdk-python-patching.md"). You cannot
instrument individual clients.

For all services, you can see the name of the API
called in the X-Ray console. For a subset of services, the X-Ray SDK adds information to the segment
to provide more granularity in the service map.

For example, when you make a call with an instrumented
DynamoDB client, the SDK adds the table name to the segment for calls that target a table. In the
console, each table appears as a separate node in the service map, with a generic DynamoDB node
for calls that don't target a table.

###### Example Subsegment for a call to DynamoDB to save an item

```
{
  "id": "24756640c0d0978a",
  "start_time": 1.480305974194E9,
  "end_time": 1.4803059742E9,
  "name": "DynamoDB",
  "namespace": "aws",
  "http": {
    "response": {
      "content_length": 60,
      "status": 200
    }
  },
  "aws": {
    "table_name": "scorekeep-user",
    "operation": "UpdateItem",
    "request_id": "UBQNSO5AEM8T4FDA4RQDEB94OVTDRVV4K4HIRGVJF66Q9ASUAAJG",
  }
}
```

When you access named resources,
calls to the following services create additional nodes in the service map.
Calls that don't target specific resources create a generic node for the service.

- **Amazon DynamoDB** – Table name
- **Amazon Simple Storage Service** – Bucket and key name
- **Amazon Simple Queue Service** – Queue name
