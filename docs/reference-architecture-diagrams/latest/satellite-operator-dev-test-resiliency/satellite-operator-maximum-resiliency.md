

# Satellite Operator Maximum Resiliency
<a name="satellite-operator-maximum-resiliency"></a>

Publication date: **April 25, 2023 ([Diagram history](#sat-max-history))**

With this architecture, you can achieve maximum resiliency for satellite operator workloads. The solution separates connections that terminate on separate devices in more than one location. An AWS Direct Connect Service Delivery Partner provides redundant satellite infrastructure.

## Satellite operator maximum resiliency diagram
<a name="sat-max-diagram"></a>

![Reference architecture diagram showing how to achieve maximum resiliency for satellite operators by using AWS Direct Connect with separate connections at multiple locations.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/satellite-operator-dev-test-resiliency/images/satellite-operator-dev-test-resiliency-3.png)


The following steps describe the data flow and connectivity setup for this architecture:

1. Use satellite communications from your on-premises locations to communicate back to your AWS Cloud environment. Use two customer routers and one satellite antenna in multiple locations.

1. Work with an [AWS Direct Connect Service Delivery Partner](https://aws.amazon.com/directconnect/partners/) that provides redundant satellite infrastructure.

1. The partner provides teleport connectivity with two physical connections on two different devices at multiple locations and handles necessary demodulation of your data.

1. The partner sets up two physical connections on different devices at multiple sites. Use these connections for dedicated or hosted connectivity.

1. Order dedicated connectivity or hosted connectivity from the AWS Direct Connect Service Delivery Partner.

1. (Optional) Enable MAC Security.

1. (Optional) Provision private virtual interfaces (VIFs) to access your private AWS resources through [Direct Connect Gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html).

1. (Optional) Provision transit VIFs to access your private AWS resources through Direct Connect Gateway and [AWS Transit Gateway](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway.html).

1. (Optional) Provision public VIFs to access your public AWS resources such as [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html). Connectivity can be Regional or global.

## Further reading
<a name="sat-max-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="sat-max-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](satellite-operator-dev-test.md#sat-dev-history) | Reference architecture diagram first published. | April 25, 2023 | 
| [Initial publication](satellite-operator-high-resiliency.md#sat-high-history) | Reference architecture diagram first published. | April 25, 2023 | 
| [Initial publication](#sat-max-history) | Reference architecture diagram first published. | April 25, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.