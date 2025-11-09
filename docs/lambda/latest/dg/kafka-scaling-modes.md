# Apache Kafka event poller scaling modes in Lambda

You can choose between two modes of event poller scaling for Amazon MSK and self-managed Apache Kafka event source mappings:

- [On-demand mode (default)](#kafka-default-mode "#kafka-default-mode")
- [Provisioned mode](#kafka-provisioned-mode "#kafka-provisioned-mode")

## On-demand mode (default)

When you initially create the Kafka event source, Lambda allocates a default number of event pollers
to process all partitions in the Kafka topic. Lambda automatically scales up or down the number of
[event pollers](invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode "invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode") based on message
load.

In one-minute intervals, Lambda evaluates the offset lag
of all the partitions in the topic. If the offset lag is too high, the partition is receiving messages
faster than Lambda can process them. If necessary, Lambda adds or removes event pollers from the topic.
This autoscaling process of adding or removing event pollers occurs within three minutes of evaluation.

If your target Lambda function is throttled, Lambda reduces the number of event pollers. This action
reduces the workload on the function by reducing the number of messages that event pollers can
retrieve and send to the function.

## Provisioned mode

For workloads where you need to fine-tune the throughput of your event source mapping, you can use
provisioned mode. In provisioned mode, you define minimum and maximum limits for the amount of
provisioned event pollers. These provisioned event pollers are dedicated to your event source mapping,
and can handle unexpected message spikes through responsive autoscaling. We recommend that you use
provisioned mode for Kafka workloads that have strict performance requirements.

In Lambda, an event poller is a compute unit capable of handling up to 5 MBps of throughput.
For reference, suppose your event source produces an average payload of 1MB, and the average function duration is 1 sec.
If the payload doesn’t undergo any transformation (such as filtering), a single poller can support 5 MBps throughput,
and 5 concurrent Lambda invocations. Using provisioned mode incurs additional costs. For pricing estimates,
see [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/").

###### Note

When using provisioned mode, you don't need to create AWS PrivateLink VPC endpoints or grant the associated permissions as part of your network configuration.

In provisioned mode, the range of accepted values for the minimum number of event pollers
(`MinimumPollers`) is between 1 and 200, inclusive. The range of
accepted values for the maximum number of event pollers (`MaximumPollers`)
is between 1 and 2,000, inclusive. `MaximumPollers` must be greater than
or equal to `MinimumPollers`. In addition, to maintain ordered
processing within partitions, Lambda caps the `MaximumPollers` to the
number of partitions in the topic.

For more details about choosing appropriate values for minimum and maximum event pollers,
see [Best practices](#kafka-provisioned-mode-bp "#kafka-provisioned-mode-bp").

You can configure provisioned mode for your Kafka event source mapping using the console
or the Lambda API.

###### To configure provisioned mode for an existing event source mapping (console)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the function with the event source mapping you want to configure
   provisioned mode for.
3. Choose **Configuration**, then choose **Triggers**.
4. Choose the event source mapping that you want to configure provisioned mode for,
   then choose **Edit**.
5. Under **Provisioned mode**, select **Configure**.
   - For **Minimum event pollers**, enter a value between 1 and 200.
     If you don't specify a value, Lambda chooses a default value of 1.
   - For **Maximum event pollers**, enter a value between 1 and 2,000.
     This value must be greater than or equal to your value for **Minimum event
     pollers**. If you don't specify a value, Lambda chooses a default value of 200.

6. Choose **Save**.

You can configure provisioned mode programmatically using the [ProvisionedPollerConfig](../api/API_ProvisionedPollerConfig.md "../api/API_ProvisionedPollerConfig.md") object
in your [EventSourceMappingConfiguration](../api/API_EventSourceMappingConfiguration.md "../api/API_EventSourceMappingConfiguration.md"). For example, the following [UpdateEventSourceMapping](../api/API_UpdateEventSourceMapping.md "../api/API_UpdateEventSourceMapping.md") CLI
command configures a `MinimumPollers` value of 5, and a
`MaximumPollers` value of 100.

```
aws lambda update-event-source-mapping \
    --uuid a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --provisioned-poller-config '{"MinimumPollers": 5, "MaximumPollers": 100}'

```

After configuring provisioned mode, you can observe the usage of event pollers for your workload by monitoring
the `ProvisionedPollers` metric. For more information, see [Event source mapping metrics](monitoring-metrics-types.md#event-source-mapping-metrics "monitoring-metrics-types.md#event-source-mapping-metrics").

To disable provisioned mode and return to default (on-demand) mode,
you can use the following [UpdateEventSourceMapping](../api/API_UpdateEventSourceMapping.md "../api/API_UpdateEventSourceMapping.md") CLI
command:

```
aws lambda update-event-source-mapping \
    --uuid a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --provisioned-poller-config '{}'

```

## Best practices and considerations when using provisioned mode

The optimal configuration of minimum and maximum event pollers for your event source mapping
depends on your application's performance requirements. We recommend that you start with the
default minimum event pollers to baseline the performance profile. Adjust your configuration
based on observed message processing patterns and your desired performance profile.

For workloads with spiky traffic and strict performance needs, increase the minimum event
pollers to handle sudden surges in messages. To determine the minimum event pollers required,
consider your workload's messages per second and average payload size, and use the throughput
capacity of a single event poller (up to 5 MBps) as a reference.

To maintain ordered processing within a partition, Lambda limits the maximum event pollers
to the number of partitions in the topic. Additionally, the maximum event pollers your event
source mapping can scale to depends on the function's concurrency settings.

When activating provisioned mode, update your network settings to remove AWS PrivateLink VPC
endpoints and associated permissions.
