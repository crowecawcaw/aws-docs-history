

# Deploying E2E 5G Network with AWS
<a name="deploying-e2e-5g-network"></a>

Publication date: **December 28, 2020 ([Diagram history](#e2e5g-history))**

With this architecture, you can deploy an end-to-end (E2E) 5G network by using AWS services. The solution covers Radio Access Network (RAN), Multi-Access Edge Computing (MEC), 5G Core, and data network components across [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/), [AWS Wavelength](https://docs.aws.amazon.com/wavelength/latest/developerguide/), and AWS Regions.

## Deploying E2E 5G network diagram
<a name="e2e5g-diagram"></a>

![Reference architecture diagram showing how to deploy an E2E 5G network by using AWS Outposts, AWS Wavelength, Amazon EKS, Amazon ECS, and AWS Direct Connect.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/deploying-e2e-5g-network/images/deploying-e2e-5g-network.png)


The following steps describe the network components and connectivity for this architecture:

1. Use [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/snowcone-guide/) (up to 100 Mbps) or AWS Snowball Edge (up to 10 Gbps) for Open RAN Distributed Unit (DU) and Centralized Unit (CU) deployments based on throughput requirements.

1. Build MEC capabilities by using AWS Outposts with services such as [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/), [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/), and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Deploy the 5G Core User Plane Function (UPF) on AWS Outposts on-premises for high throughput.

1. Use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) to connect on-premises 5G Core components to an AWS Region for control and management.

1. Implement the 5G Core UPF as microservices on Amazon EKS. Take advantage of Single-Root Input/Output Virtualization (SR-IOV), Data Plane Development Kit (DPDK), and dual-homing capabilities.

1. Run the control plane on the AWS Region on the same Amazon VPC as on-premises. Implement control plane functions on Amazon ECS or Amazon EKS.

1. Expand UPF instances to AWS Regions through Network Load Balancer if needed by using Amazon VPC expansion to on-premises.

1. Interconnect other VPCs through [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/) to host management and orchestration services.

1. Use AWS Wavelength to give the developer community access to the communication service provider (CSP) environment. Provide low-latency applications to subscribers.

## Further reading
<a name="e2e5g-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="e2e5g-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#e2e5g-history) | Reference architecture diagram first published. | December 28, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.