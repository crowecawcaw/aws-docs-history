# Making applications Regional-fault tolerant with global endpoints in EventBridge

You can improve your application's availability with Amazon EventBridge global endpoints. Global
endpoints help make your application regional-fault tolerant at no additional cost. To start,
you assign an Amazon Route 53 health check to the endpoint. When failover is initiated, the health
check reports an “unhealthy” state. Within minutes of failover initiation, all custom [events](eb-events.md "eb-events.md") are routed to an [event
bus](eb-event-bus.md "eb-event-bus.md") in the secondary Region and are processed by that event bus. Once the health check
reports a “healthy” state, events are processed by the event bus in the primary Region.

When you use global endpoints, you can enable [event
replication](#eb-ge-event-replication "#eb-ge-event-replication"). Event replication sends all custom events to the event buses in the
primary and secondary Regions using managed rules.

###### Note

If you're using custom buses, you'll need a custom bus in each Region with the same name
and in the same account for failover to work properly.

## Recovery Time & Recovery Point Objectives

The Recovery Time Objective (RTO) is the time that it takes for the secondary Region to
start receiving events after a failure. For RTO, the time includes time period for triggering
CloudWatch alarms and updating statuses for Route 53 health checks. The Recovery Point Objective (RPO)
is the measure of the data that will be left unprocessed during a failure. For RPO, the time
includes events that are not replicated to the secondary Region and are stuck in the primary
Region until the service or Region recovers. With global endpoints, if you follow our
prescriptive guidance for alarm configuration, you can expect the RTO and RPO to be 360
seconds with a maximum of 420 seconds.

## Event replication

Events are processed in the secondary Region asynchronously. This means that events are
not guaranteed to be processed at the same time in both Regions. When failover is
triggered, the events are processed by the secondary Region and will be processed by the
primary Region when it’s available. Enabling event replication will increase your monthly
costs. For more information, see [Amazon EventBridge
pricing](https://aws.amazon.com/eventbridge/pricing "https://aws.amazon.com/eventbridge/pricing")

We recommend enabling event replication when setting up global endpoints for the following
reasons:

- Event replication helps you verify that your global endpoints are configured correctly. This
  helps to ensure that you’ll be covered in the event of failover.
- Event replication is required to automatically recover from a failover event. If you don’t have event replication enabled, you’ll have to manually
  reset the Route 53 health check to “healthy” before events will go back to the primary Region.

### Replicated event payload

The following is an example of a replicated event payload:

###### Note

For `region`, the Region that the event was replicated from is listed.

```
{
    "version": "0",
    "id": "a908baa3-65e5-ab77-367e-527c0e71bbc2",
    "detail-type": "Test",
    "source": "test.service.com",
    "account": "0123456789",
    "time": "1900-01-01T00:00:00Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:events:us-east-1:0123456789:endpoint/MyEndpoint"
    ],
    "detail": {
        "a": "b"
    }
}
```

## Working with global endpoints by using an AWS SDK

###### Note

Support for C++ is coming soon.

When using an AWS SDK to work with global endpoints, keep the following in mind:

- You'll need to have the AWS Common Runtime (CRT) library installed for your specific SDK. If you don't have the CRT installed,
  you'll get an exception message indicating what needs to be installed. For more information, see the following:
  - [AWS
    Common Runtime (CRT) libraries](../../../sdkref/latest/guide/common-runtime.md "../../../sdkref/latest/guide/common-runtime.md")
  - [awslabs/aws-crt-java](https://github.com/awslabs/aws-crt-java "https://github.com/awslabs/aws-crt-java")
  - [awslabs/aws-crt-nodejs](https://github.com/awslabs/aws-crt-nodejs "https://github.com/awslabs/aws-crt-nodejs")
  - [awslabs/aws-crt-python](https://github.com/awslabs/aws-crt-python "https://github.com/awslabs/aws-crt-python")

- Once you have created a global endpoint, you'll need to add the
  `endpointId` and `EventBusName` to any `PutEvents` calls that you use.
- Global endpoints support Signature Version 4A. This version of SigV4 allows requests
  to be signed for multiple AWS Regions. This is useful in API operations that might
  result in data access from one of several Regions. When using the AWS SDK, you supply
  your credentials and the requests to global endpoints will use Signature Version 4A
  without additional configuration. For more information about SigV4A, see [Signing
  AWS API requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md") in the _AWS General Reference_.

If you request temporary credentials from the global AWS STS endpoint (sts.amazonaws.com), AWS STS vends credentials which, by default, do not support SigV4A. See
[Managing AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md") in the
_AWS Identity and Access Management User Guide_ for further information.

## Available Regions

The following Regions support global endpoints:

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Milan)
- Europe (Paris)
- Europe (Stockholm)
- Asia Pacific (Mumbai)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- South America (São Paulo)
