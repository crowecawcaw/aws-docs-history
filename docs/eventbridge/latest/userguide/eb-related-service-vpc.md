# Using Amazon EventBridge with Interface VPC endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and EventBridge. Your resources on your VPC can use this connection to communicate with EventBridge.

With a VPC, you have control over your network settings, such as the IP address range,
subnets, route tables, and network gateways. To connect your VPC to EventBridge, you define an
_interface VPC endpoint_ for EventBridge. The endpoint provides reliable, scalable
connectivity to EventBridge without requiring an internet gateway, network address translation (NAT)
instance, or VPN connection. For more information, see [What is
Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the _Amazon VPC User Guide_.

Interface VPC endpoints are powered by AWS PrivateLink, which enables private
communication between AWS services using an elastic network interface with private IP
addresses. For more information, see [AWS PrivateLink and VPC
endpoints](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md").

![Private interface endpoints providing connections between VPCs and EventBridge event buses, pipes, and schemas.](images/interface-vpc_eventbridge_conceptual.svg)
When you use a private interface VPC endpoint, custom [events](eb-events.md "eb-events.md") your VPC sends to EventBridge use that endpoint. EventBridge then sends those events to other
AWS services based on the [rules](eb-rules.md "eb-rules.md") and [targets](eb-targets.md "eb-targets.md") that you've configured. Once events are sent to another service you can
receive them through either the public endpoint or a VPC endpoint for that service. For example,
if you create a rule to send events to an Amazon SQS queue, you can configure an interface VPC
endpoint for Amazon SQS to receive messages from that queue in your VPC without using the public
endpoint.

## Creating a VPC endpoint for EventBridge

To use EventBridge with your VPC, create an interface VPC endpoint for EventBridge and choose
the appropriate EventBridge service name. For more information, see [Creating an Interface
Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint.html") in the _Amazon VPC User Guide_.

- **Event buses**

Service name: **com.amazonaws.`region`.events**

Event bus FIPS endpoints also support VPC endpoints. For a complete list of FIPS endpoints, see
[EventBridge endpoints and quotas](../../../general/latest/gr/ev.md "../../../general/latest/gr/ev.md") in the _AWS General Reference._.

Service name: **com.amazonaws.`region`.events-fips**

- **Pipes**

Service name: **com.amazonaws.`region`.pipes**

EventBridge Pipes supports endpoints for all [pipe API operations](../pipes-reference/Welcome.md "../pipes-reference/Welcome.md").

Pipes FIPS endpoints also support VPC endpoints. For a complete list of FIPS endpoints, see
[EventBridge Pipes endpoints and quotas](../../../general/latest/gr/ev_pipes.md "../../../general/latest/gr/ev_pipes.md") in the _AWS General Reference._.

Service name: **com.amazonaws.`region`.pipes-fips**

You can also use a VPC endpoint to fulfill networking requirements for Pipes Apache Kafka and Amazon MQ sources.

Service name: **com.amazonaws.`region`.pipes-data**

For more information, refer to the following:

    + [Apache Kafka network configuration](eb-pipes-kafka.md#pipes-kafka-vpc-config "eb-pipes-kafka.md#pipes-kafka-vpc-config")
    + [Amazon MSK network configuration](eb-pipes-msk.md#pipes-msk-vpc-config "eb-pipes-msk.md#pipes-msk-vpc-config")
    + [Amazon MQ network configuration](eb-pipes-mq.md#pipes-mq-vpc-config "eb-pipes-mq.md#pipes-mq-vpc-config")

###### Note

VPC endpoints to **pipes-data** do not support VPC Endpoint resource policies.

VPC endpoints to **pipes** and **pipes-fips** do support VPC Endpoint resource policies that allow you to:

    + Deny access to specific Pipe APIs.
    + Limit access on some APIs to specific Pipes by ARN using the IAM **Resource** condition key.

- **Schemas**

Service name: **com.amazonaws.`region`.schema**

EventBridge supports endpoints for all [schema API
operations](../schema-reference/what-is-eventbridge-schemas.md "../schema-reference/what-is-eventbridge-schemas.md").
