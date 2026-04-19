# What is AWS Interconnect?

## What is AWS Interconnect?

AWS Interconnect is a family of managed private connectivity services that enables you to create high-speed connections from your locations to AWS and between cloud environments.

With AWS Interconnect, you no longer need to configure physical or virtual routers, order cross-connects, or manage BGP peering. Through a simplified process you select your AWS region, your required network capacity, and your preferred provider.

AWS and the provider will quickly provision and configure your requested capacity on redundant network devices. They present it to you as a single object called an _interconnect_.

AWS Interconnect includes two offerings:

- Interconnect – multicloud: Connect your AWS VPCs directly to VPCs in other public clouds.
- Interconnect – last mile: Connect your branch offices, data centers, and remote locations to AWS through qualified delivery partners' existing last-mile networks.

## Advantages of AWS Interconnect

### Simplified Network Architecture

With AWS Interconnect, your traffic is transported on the AWS global backbone until it is handed off to the provider directly. This eliminates the need for complex on-premises routing or intermediate network hops.

### Fast Provisioning and Scaling

New Interconnects are typically provisioned and configured within minutes. Once live, you can increase or decrease bandwidth directly through the AWS Console without reprovisioning connections or engaging support. This elastic model lets you scale up for peak workloads and scale back down to control costs.

### Fully managed service

AWS and your provider manage all aspects of the physical network infrastructure and configuration. This includes provisioning network devices, configuring VLANs and BGP sessions, and handling ongoing maintenance. You focus on your applications while AWS handles the underlying connectivity infrastructure.

### Built-in maximum resiliency

Every Interconnect is provisioned across redundant network devices spanning at least two physically distinct facilities with independent power and networking. This architecture eliminates single points of failure at the device, cross-connect, and facility level. Multicloud and last mile connections use a four-connection model with Equal-Cost Multi-Path (ECMP) load balancing, ensuring at least one link remains operational during planned maintenance.

## Region Availability

### AWS Interconnect – last mile

AWS Interconnect – last mile initially launches with Lumen in us-east-1 (N. Virginia). You can create a last mile connection from the NJ sites in us-east-1 to any AWS region globally, and connect from anywhere in the continental United States via the Lumen connectivity fabric. Additional partners and regions will be added over time.

### AWS Interconnect – Multicloud

Interconnect - multicloud is supported in the following AWS and Google Cloud Regions:

- AWS US East (N. Virginia) us-east-1 – Google Cloud N. Virginia (us-east4)
- AWS US West (N. California) us-west-1 – Google Cloud Los Angeles (us-west2)
- AWS US West (Oregon) us-west-2 – Google Cloud Oregon (us-west1)
- AWS Europe (London) eu-west-2 – Google Cloud London (europe-west2)
- AWS Europe (Frankfurt) eu-central-1 – Google Cloud Frankfurt (europe-west3)

## How AWS Interconnect works

AWS Interconnect is designed to connect your private networks in AWS with your private networks in remote locations or other cloud environments. You don’t need to think about physical networking devices or configure routing protocols. The service is also designed to provision capacity quickly. It follows our standards for security and maximum network resiliency.

To achieve these design goals, AWS and its partners have pre-provisioned capacity in each of the supported regions and locations. This capacity spans multiple network devices distributed across at least two physical buildings. These buildings have independent power and networking.

All connections between the AWS network devices and the adjacent partner devices are encrypted by default. The encryption uses industry standard IEEE 802.1AE MAC Security (MACsec). The devices are configured to transmit customer traffic only if the encryption session is active.

## AWS Interconnect concepts

### Interconnect

The managed connectivity object provisioned between AWS and a provider (cloud service provider or last-mile provider). Each Interconnect is presented as a single logical object in your AWS account, abstracting the underlying redundant infrastructure.

### Attach point

A logical identifier that anchors the Interconnect on each side of the connection. On AWS, the attach point is always the Direct Connect Gateway. On the remote side, the attach point varies by offering: a CSP router (Multicloud) or a partner-side network identifier (last mile).

### Direct Connect Gateway

A logical, highly-available, globally distributed object that serves as the attach point for Region or Local Zone-based AWS networking services such as Virtual Private Gateways, Transit Gateways, and Cloud WAN, as well as AWS Interconnect.

### Activation Key

A token generated during the connection creation process. It is shared between parties (AWS and provider) to authorize and complete the provisioning of a new Interconnect, ensuring that both sides validate the request before resources are committed.

### Create/Accept flows

The process to create a new Interconnect has two main actions: one party initiates a Create action, generating an Activation Key. The other party uses that key to perform the Accept action, triggering automated provisioning on both sides.

### Built-in resiliency and security

AWS Interconnect uses redundant infrastructure to provide maximum network resiliency. The service automatically provisions multiple logical connections spanning multiple network devices across two or more physical facilities. All physical connections between AWS routers and partner devices are secured using MACsec encryption. The customer sees only a single abstracted Interconnect object in their console, while the underlying infrastructure ensures business continuity during device or facility failures.

The following diagram shows the high-level physical infrastructure used to provide AWS Interconnect. The customer Interconnect is represented by the grey dotted line attachment. This attachment is created directly between the attach points on both sides. The customer sees only the abstracted object in their console. In this example, the customer is using a Transit Gateway attached to a Direct Connect gateway. This gateway is used as the attach point on the AWS side.

At the infrastructure level, AWS and the provider have provisioned multiple logical connections. These connections span multiple network devices across two physical facilities. All the physical connections between the AWS routers and the provider routers in each facility are secured using MACsec.

![Interconnect architecture diagram](images/interconnect-diagram.png)

### Interconnect Creation Process at High-Level

In the following example diagram, a customer begins the process by creating a new Interconnect using the AWS Console (1). AWS receives the request. AWS provides the customer with the new Interconnect activation key. AWS submits the request to the provider (2).

The provider receives the request and waits for confirmation from the customer. The customer then uses the activation key to approve the request (3).

AWS and the provider then begin the provisioning process. No further customer interaction is needed (4). The process is completed with the successful creation of the new Interconnect. The Interconnect attaches to the Direct Connect gateway on the AWS side and to the provider’s attach point on the remote side.

![Interconnect creation process diagram](images/interconnect-diagram-process.png)

## Supported configurations with AWS networking services

AWS Interconnect can connect to your VPCs through supported AWS networking services: Virtual private gateways, Transit Gateways, and Cloud WAN.

### Virtual Private Gateways and Transit Gateways

Virtual gateways or Transit Gateways in a specific AWS Region, through a Direct Connect gateway, can only reach an Interconnect that provides connectivity to the paired Google Cloud Region.
This Interconnect is considered "local" to that AWS Region. For example, a Transit Gateway in the AWS Region N. Virginia (us-east-1) can only reach an Interconnect that connects to the Google Cloud N. Virginia (us-east4) Region.

### Cloud WAN

When using Cloud WAN you define the AWS Regions where your global network will have a Core Network Edge (CNE). Using the native Direct Connect attachment, any Cloud WAN CNE can reach any
Interconnect globally that is attached to the same Direct Connect gateway.

## Network health monitoring

All Interconnects include a single CloudWatch Network Synthetic Monitor at no extra cost. You can use this active synthetic probe to produce round trip latency and packet loss metrics.
You can configure CloudWatch alarms on your set thresholds. Refer to the CloudWatch Network Synthetic Monitor user guide for configuration. Note that the Network Health Indicator feature
is not yet supported with Interconnects. Latency and packet loss metrics are fully supported.

## Bandwidth utilization monitoring

Your Interconnects provide a percentage utilization metric on CloudWatch. This metric displays the percentage of the capacity of your Interconnect that your traffic is utilizing. This metric is
designed to help you understand your usage patterns and increase or decrease your provisioned bandwidth as needed.

You can set up CloudWatch alarms on your desired thresholds to help you prevent potential congestion events due to an application consuming all of your provisioned network capacity on an Interconnect.
