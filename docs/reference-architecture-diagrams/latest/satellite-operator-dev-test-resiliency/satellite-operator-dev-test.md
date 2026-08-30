# Satellite Operator Development and Test Resiliency

Publication date: **April 25, 2023 ([Diagram history](#sat-dev-history "#sat-dev-history"))**

With this architecture, you can achieve development and test resiliency for non-critical
satellite operator workloads. The solution uses separate connections that terminate on separate
devices in one location through an AWS Direct Connect Service Delivery Partner.

## Development and test resiliency diagram

![Reference architecture diagram showing how to achieve development and test resiliency for satellite operators by using AWS Direct Connect with separate connections at a single location.](images/satellite-operator-dev-test-resiliency-1.png)

The following steps describe the data flow and connectivity setup for this architecture:

1. Use satellite communications from your on-premises location to communicate back to
   your AWS Cloud environment. Use two customer routers and one satellite antenna.
2. Work with an [AWS Direct
   Connect Service Delivery Partner](https://aws.amazon.com/directconnect/partners/ "https://aws.amazon.com/directconnect/partners/") that provides and manages the single satellite
   infrastructure.
3. The partner provides teleport connectivity with one physical connection on two
   different devices at a single location and handles necessary demodulation of your
   data.
4. The partner sets up two physical connections on different devices at a single site.
   Use these connections for dedicated or hosted connectivity.
5. Order dedicated connectivity or hosted connectivity from the AWS Direct Connect
   Service Delivery Partner.
6. (Optional) Enable MAC Security.
7. (Optional) Provision private virtual interfaces (VIFs) to access your private AWS
   resources through [Direct Connect
   Gateway](../../../directconnect/latest/UserGuide/direct-connect-gateways-intro.md "../../../directconnect/latest/UserGuide/direct-connect-gateways-intro.md").
8. (Optional) Provision transit VIFs to access your private AWS resources through
   Direct Connect Gateway and [AWS
   Transit Gateway](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.md").
9. (Optional) Provision public VIFs to access your public AWS resources such as
   [Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")
   and [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md"). Connectivity can
   be Regional or global.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS
  Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change                                                                                                                                     | Description                                     | Date           |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | -------------- |
| Initial publication                                                                                                                        | Reference architecture diagram first published. | April 25, 2023 |
| [Initial publication](satellite-operator-high-resiliency.md#sat-high-history "satellite-operator-high-resiliency.md#sat-high-history")     | Reference architecture diagram first published. | April 25, 2023 |
| [Initial publication](satellite-operator-maximum-resiliency.md#sat-max-history "satellite-operator-maximum-resiliency.md#sat-max-history") | Reference architecture diagram first published. | April 25, 2023 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are
using.
