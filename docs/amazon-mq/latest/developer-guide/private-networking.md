# Private networking for Amazon MQ for RabbitMQ

Private networking enables Amazon MQ for RabbitMQ brokers to connect to
private resources in your VPC. These resources can include private identity providers (LDAP
or OAuth2), other Amazon MQ for RabbitMQ brokers, or self-hosted RabbitMQ brokers. You can
connect to your resources privately without going over the public internet.

###### Availability

- Private networking is available only for Amazon MQ for RabbitMQ brokers. ActiveMQ brokers
  are not supported.
- Private networking is not available in the AWS GovCloud (US) Regions.
- Private networking is available only in AWS Regions where Amazon VPC Lattice
  is available. For more information about the Regions where VPC Lattice is available,
  see [Amazon
  VPC Lattice endpoints and quotas](../../../general/latest/gr/vpc-lattice-service.md "../../../general/latest/gr/vpc-lattice-service.md") in the _AWS General
  Reference_.

###### Topics

- [How private networking works](#private-networking-how-it-works "#private-networking-how-it-works")
- [Prerequisites](#private-networking-prerequisites "#private-networking-prerequisites")
- [Setting up private networking](#private-networking-setup "#private-networking-setup")
- [Use cases](#private-networking-use-cases "#private-networking-use-cases")
- [Modifying shared resources](#private-networking-modifying "#private-networking-modifying")
- [Quotas](#private-networking-quotas "#private-networking-quotas")
- [Resource states](#private-networking-resource-states "#private-networking-resource-states")
- [Troubleshooting](#private-networking-troubleshooting "#private-networking-troubleshooting")

## How private networking works

Private networking uses Amazon VPC Lattice, AWS Resource Access Manager (AWS RAM), and AWS PrivateLink to
connect your broker to a private destination in your VPC.

The setup involves the following components:

1. A **VPC Lattice resource gateway** in your VPC acts as the
   entry point for traffic from the broker to your private resources.
2. One or more **VPC Lattice resource configurations** define
   the private destinations (IP address or DNS name) reachable through the resource
   gateway.
3. An **AWS RAM resource share** packages the resource
   configurations and is associated with the broker through the
   `UpdateBroker` API operation.
4. During a broker reboot, Amazon MQ creates resource VPC endpoints in the broker's
   VPC. These endpoints establish the network path through your resource gateway to the
   configured destinations.

## Prerequisites

Before you set up private networking, ensure the following:

- You have an Amazon MQ for RabbitMQ broker in a `RUNNING` state.
- You have a VPC with at least one subnet. This VPC hosts the resource gateway
  and does not need to be the same VPC as the broker. For high availability, use
  subnets in multiple Availability Zones.
- The VPC Lattice resource gateway must share at least one Availability Zone with
  the broker. This is a concern only for single-instance brokers. Cluster
  brokers use every available Availability Zone.

###### Note

The broker does not need to be private. A publicly accessible broker can also use private networking.

## Setting up private networking

Follow these steps to set up private networking for your Amazon MQ for RabbitMQ
broker.

### Step 1: Create a VPC Lattice resource gateway

Create a VPC Lattice resource gateway in a VPC that can reach your private
resources. The resource gateway acts as a transparent proxy. It routes traffic from the
broker to the configured destinations.

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/home#ResourceGateways: "https://console.aws.amazon.com/vpc/home#ResourceGateways:").
2. In the navigation pane, under **VPC
   Lattice**, choose **Resource
   gateways**.
3. Choose **Create resource gateway**.
4. Configure the resource gateway with a VPC, subnets, and security group.
   Ensure at least one subnet is in an Availability Zone shared with your
   broker.

For more information, see [Resource gateways](../../../vpc-lattice/latest/ug/resource-gateways.md "../../../vpc-lattice/latest/ug/resource-gateways.md") in the _Amazon VPC Lattice User
Guide_.

### Step 2: Create VPC Lattice resource configurations

Create one or more resource configurations that define the private destinations
your broker needs to reach. Each resource configuration specifies an IP address or
DNS name that is resolvable from within the VPC where you set up the resource
gateway.

You can optionally add a custom domain name to a resource configuration. Only
verified domain names are usable for DNS resolution from the broker. If your resource
configuration does not have a usable domain name, Amazon MQ provides a DNS name through
the `DescribeSharedResources` API operation. You can use this DNS name in your broker
configuration.

For more information, see [Resource configurations](../../../vpc-lattice/latest/ug/resource-configurations.md "../../../vpc-lattice/latest/ug/resource-configurations.md") in the _Amazon VPC Lattice User
Guide_.

### Step 3: Create an AWS RAM resource share

Create an AWS RAM resource share and add your VPC Lattice resource configurations to
it. The resource share is what you associate with your Amazon MQ broker.

###### Important

The resource share must allow external principals. Resource shares
restricted to your organization (`allowExternalPrincipals=false`)
cannot be used with Amazon MQ.

For more information, see [Creating a resource share](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS Resource Access Manager User
Guide_.

### Step 4: Associate the resource share with your broker

Use the `UpdateBroker` API operation to associate the AWS RAM resource share
with your broker. You can associate multiple resource shares by providing a list of
resource share ARNs.

###### Example Associate a resource share using the AWS CLI

```
aws mq update-broker \
    --broker-id `b-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
    --resource-share-arns `arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`
```

Replace the placeholders with your own values:

- `--broker-id` – The unique ID of your broker
  (the `b-a1b2c3d4-...` value).
- `--resource-share-arns` – The Amazon Resource Name (ARN)
  of your AWS RAM resource share
  (the `arn:aws:ram:...` value).

For more information, see
[UpdateBroker](../api-reference/brokers-broker-id.md "../api-reference/brokers-broker-id.md")
in the _Amazon MQ REST API Reference_.

To associate multiple resource shares, separate the ARNs with spaces:

```
aws mq update-broker \
    --broker-id `b-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` \
    --resource-share-arns `arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222` `arn:aws:ram:us-east-1:123456789012:resource-share/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`
```

###### Note

If you call `UpdateBroker` multiple times before rebooting, only
the last call takes effect. The `resourceShareArns` parameter is a
full replacement (put), not an additive operation. You must provide the complete
list of resource share ARNs that you want associated with the broker each time
you call `UpdateBroker`.

###### Note

Changes to resource share associations require a broker reboot to take effect.
Calling `UpdateBroker` associates the resource share with the
broker but does not establish the network path immediately.

### Step 5: Reboot the broker

Reboot the broker to apply the pending resource share changes. During the reboot,
Amazon MQ creates resource VPC endpoints in the broker's VPC. It then establishes the network
path to your private resources.

###### Example Reboot the broker using the AWS CLI

```
aws mq reboot-broker --broker-id `b-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

Rebooting causes downtime for single-instance brokers and brief unavailability
(failover) for cluster brokers. Wait for the broker to return to the
`RUNNING` state before proceeding. This typically takes 10 to 20
minutes.

For more information, see
[RebootBroker](../api-reference/brokers-broker-id-reboot.md "../api-reference/brokers-broker-id-reboot.md")
in the _Amazon MQ REST API Reference_.

### Step 6: Verify the setup

Use the `DescribeSharedResources` API operation to verify that your
resources are available. You can also use it to retrieve the DNS names for use in your broker
configuration.

###### Example Verify shared resources using the AWS CLI

```
aws mq describe-shared-resources --broker-id `b-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
```

When the setup is complete, resource shares appear in `AVAILABLE` state.
Each resource configuration shows its associated DNS name.

For more information, see

[DescribeSharedResources](../api-reference/brokers-broker-id-shared-resources.md "../api-reference/brokers-broker-id-shared-resources.md")
in the _Amazon MQ REST API Reference_.

## Use cases

The following sections describe common use cases for private networking.

### Connecting to a private identity provider

You can use private networking to connect your broker to a private LDAP or OAuth2
identity provider without exposing it to the public internet. After setting up
private networking, use the DNS name from the
`DescribeSharedResources` API response in your broker's
authentication configuration.

For more information about configuring authentication, see [LDAP authentication and authorization for Amazon MQ for RabbitMQ](ldap-for-amq-for-rabbitmq.md "ldap-for-amq-for-rabbitmq.md") and [OAuth 2.0 authentication and authorization for Amazon MQ for RabbitMQ](oauth-for-amq-for-rabbitmq.md "oauth-for-amq-for-rabbitmq.md").

### Connecting to another Amazon MQ for RabbitMQ broker

You can use private networking to connect your broker to another Amazon MQ for RabbitMQ
broker using Shovel or Federation plugins. This enables private
broker-to-broker communication without exposing either broker to the public
internet.

When creating the resource configuration for another Amazon MQ broker, provide the
broker endpoint (for example, `b-xxxx.mq.us-east-1.on.aws`) as the
custom domain name. This ensures TLS certificate validation succeeds.
RabbitMQ 4 and later enforces this validation by default for Shovel and Federation
connections. For more information, see [AMQP client SSL configuration](rabbitmq-amqp-client-ssl-configuration.md "rabbitmq-amqp-client-ssl-configuration.md").

Use the DNS name from the `DescribeSharedResources` API response as the
destination in your Shovel or Federation configuration.

###### Note

For RabbitMQ versions earlier than 4, TLS certificate peer verification is
not enforced by default for Shovel and Federation. You can either specify the
broker endpoint as a custom domain name or turn off peer verification through
configuration. For more information, see [AMQP client SSL configuration](rabbitmq-amqp-client-ssl-configuration.md "rabbitmq-amqp-client-ssl-configuration.md").

### Connecting to a self-hosted RabbitMQ broker

You can use private networking to connect your Amazon MQ broker to a self-hosted
RabbitMQ broker in your VPC using Shovel or Federation plugins. Create a resource
configuration pointing to the IP address or DNS name of your self-hosted broker.
Use the DNS name from the `DescribeSharedResources` API response in your
Shovel or Federation configuration.

RabbitMQ 4 and later enforces TLS certificate peer verification by default.
You must either use a verified domain name or turn off peer verification through
configuration. For more information, see [AMQP client SSL configuration](rabbitmq-amqp-client-ssl-configuration.md "rabbitmq-amqp-client-ssl-configuration.md").

## Modifying shared resources

You can modify the resource shares associated with your broker at any time. Call
the `UpdateBroker` API operation with an updated list of resource share ARNs.
Changes take effect after the next broker reboot.

To disassociate all resource shares from a broker, call `UpdateBroker` with
an empty list of resource share ARNs, then reboot the broker.

###### Important

You can modify AWS RAM resource shares at any time. You can add or remove VPC
Lattice resource configurations from a resource share. Amazon MQ does not detect these
changes until you call `UpdateBroker` and reboot the broker. However,
removing a resource configuration that was previously applied to the broker
immediately revokes the broker's access to that resource. This revocation does not
require calling `UpdateBroker` or rebooting, but the resource status
in `DescribeSharedResources` will not update until you call
`UpdateBroker` and reboot.

## Quotas

The following quotas apply to private networking:

| Resource                                       | Default limit | Description                                                                                                                                            |
| ---------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AWS RAM resource shares per broker             | 10            | Exceeding this limit causes the `UpdateBroker` API call to<br>fail.                                                                                    |
| VPC Lattice resource configurations per broker | 100           | The total across all associated resource shares. Excess resource<br>configurations are marked as `ERROR` in the<br>`DescribeSharedResources` response. |

## Resource states

Use the `DescribeSharedResources` API operation to check the state of your
shared resources. The following table describes the possible states:

| State                  | Description                                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SETUP_IN_PROGRESS`    | The resource is being configured. This state appears after calling<br>`UpdateBroker` and persists until the broker reboot<br>completes.                                       |
| `AVAILABLE`            | The resource is active and the broker can reach the configured<br>destination.                                                                                                |
| `DELETION_IN_PROGRESS` | The resource is being removed from the broker.                                                                                                                                |
| `PENDING_CREATE`       | The resource is queued for VPC endpoint creation. This state is<br>brief and appears during the broker reboot workflow.                                                       |
| `PENDING_DELETE`       | The resource is queued for VPC endpoint deletion. This state is<br>brief and appears during the broker reboot workflow.                                                       |
| `ERROR`                | The resource failed to be configured. Call<br>`DescribeSharedResources` for error details. Calling<br>`UpdateBroker` again moves the resource back to<br>`SETUP_IN_PROGRESS`. |

## Troubleshooting

Resource configuration is in ERROR state after reboot

Check the error details using the `DescribeSharedResources` API
operation. Common causes include:

- The VPC Lattice resource gateway does not share an Availability
  Zone with the broker.
- The total number of resource configurations across all resource
  shares exceeds the quota.

After resolving the issue, call `UpdateBroker` again (even with
the same resource share ARNs) to move the resource back to
`SETUP_IN_PROGRESS`, then reboot the broker.

UpdateBroker fails with a validation error

Ensure the following:

- The resource share ARN is valid and owned by your account.
- The resource share is in the same Region as the broker.
- The resource share allows external principals.
- You have not exceeded the resource share quota per broker.

Broker cannot reach the private resource after reboot

Verify the following:

- The resource state is `AVAILABLE` in the
  `DescribeSharedResources` response.
- The security group on the resource gateway allows outbound traffic
  to the destination on the required ports.
- The destination IP or DNS name in the resource configuration is
  reachable from the VPC where the resource gateway is
  deployed.
- You are using the correct DNS name from the
  `DescribeSharedResources` response in your broker
  configuration.
