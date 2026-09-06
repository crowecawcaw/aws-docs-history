

# Satellite Operator Development and Test Resiliency
<a name="satellite-operator-dev-test"></a>

Publication date: **April 25, 2023 ([Diagram history](#sat-dev-history))**

With this architecture, you can achieve development and test resiliency for non-critical satellite operator workloads. The solution uses separate connections that terminate on separate devices in one location through an AWS Direct Connect Service Delivery Partner.

## Development and test resiliency diagram
<a name="sat-dev-diagram"></a>

![Reference architecture diagram showing how to achieve development and test resiliency for satellite operators by using AWS Direct Connect with separate connections at a single location.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/satellite-operator-dev-test-resiliency/images/satellite-operator-dev-test-resiliency-1.png)


The following steps describe the data flow and connectivity setup for this architecture:

1. Use satellite communications from your on-premises location to communicate back to your AWS Cloud environment. Use two customer routers and one satellite antenna.

1. Work with an [AWS Direct Connect Service Delivery Partner](https://aws.amazon.com/directconnect/partners/) that provides and manages the single satellite infrastructure.

1. The partner provides teleport connectivity with one physical connection on two different devices at a single location and handles necessary demodulation of your data.

1. The partner sets up two physical connections on different devices at a single site. Use these connections for dedicated or hosted connectivity.

1. Order dedicated connectivity or hosted connectivity from the AWS Direct Connect Service Delivery Partner.

1. (Optional) Enable MAC Security.

1. (Optional) Provision private virtual interfaces (VIFs) to access your private AWS resources through [Direct Connect Gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html).

1. (Optional) Provision transit VIFs to access your private AWS resources through Direct Connect Gateway and [AWS Transit Gateway](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html).

1. (Optional) Provision public VIFs to access your public AWS resources such as [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html). Connectivity can be Regional or global.

## Further reading
<a name="sat-dev-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="sat-dev-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#sat-dev-history) | Reference architecture diagram first published. | April 25, 2023 | 
| [Initial publication](satellite-operator-high-resiliency.md#sat-high-history) | Reference architecture diagram first published. | April 25, 2023 | 
| [Initial publication](satellite-operator-maximum-resiliency.md#sat-max-history) | Reference architecture diagram first published. | April 25, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.