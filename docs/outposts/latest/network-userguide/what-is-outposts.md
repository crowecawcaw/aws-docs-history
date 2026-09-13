

# What is AWS Outposts?
<a name="what-is-outposts"></a>

**Important**  
AWS has discontinued sales for both 1U Outposts server and the 2U Outposts server. We are focused on making Outposts rack capabilities available in smaller power envelopes and compute footprints, including new form factors designed for space-constrained environments. As part of that focus, we are no longer accepting new customers for the original Outposts server offering and are supporting impacted customers to migrate to Outposts racks.

AWS Outposts is a family of fully managed solutions delivering AWS infrastructure, AWS services, APIs, and tools to customer premises. Outposts is available in a variety of form factors, from 1U and 2U Outposts servers to 42U Outposts racks. With Outposts, you can run the supported AWS services locally and connect to a broad range of services available in the [AWS Region](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html). AWS Outposts supports workloads that require low latency, local data processing, data residency, and migration with local network and system interdependencies.

Second-generation Outposts racks are configured for faster processing, higher memory capacity, and increased network bandwidth than first-generation AWS Outposts racks. Second-generation Outposts racks are available in two configurations:
+ **Single-rack Outposts** – Combines AWS managed compute, storage, and networking in a single 42U rack. It is purpose-built for locations with limited rack space or power. We deliver it as a self-contained rack that does not require a separate network rack. A single-rack configuration cannot be expanded by adding more racks (no scale-out). You can add capacity within the rack (scale-up).
+ **Multi-rack Outposts** – You start with a single compute rack paired with a network rack, and then add compute racks according to business needs.

## Amazon EC2 instances supported
<a name="instances"></a>

Second-generation Outposts racks currently support the following Amazon EC2 instances for a broad range of on-premises workloads:
+ General purpose [**M7i**](https://aws.amazon.com/ec2/instance-types/m7i/),[**M8i**](https://aws.amazon.com/ec2/instance-types/m8i/)
+ Compute optimized [**C7i**](https://aws.amazon.com/ec2/instance-types/c7i/),[**C8i**](https://aws.amazon.com/ec2/instance-types/c8i/)
+ Memory optimized [**R7i**](https://aws.amazon.com/ec2/instance-types/r7i/),[**R8i**](https://aws.amazon.com/ec2/instance-types/r8i/)
+ Accelerated networking (bare metal) – **bmn-sf2e** (ultra-low latency), **bmn-cx2** and **bmn-cx3a** (high throughput and low latency)

The bmn-sf2e, bmn-cx2, and bmn-cx3a instances are specialized, bare-metal instances built for latency-sensitive, compute-intensive, and throughput-intensive mission-critical workloads on-premises.

## AWS Outposts racks generations
<a name="compare-racks"></a>

The following table lists the differences between the first-generation and second-generation Outposts racks.


|  | First-generation Outposts racks | Second-generation Outposts racks (multi-rack configuration) | Second-generation Outposts racks (single-rack configuration) | 
| --- | --- | --- | --- | 
| **Compute** | M5, C5, R5, G4dn | M7i, M8i, C7i, C8i, R7i, R8i, bmn-sf2e, bmn-cx2, bmn-cx3a | M7i, M8i, C7i, C8i, R7i, R8i, bmn-sf2e, bmn-cx2, bmn-cx3a | 
| **Networking** | +  Coupled scaling of compute and networking <br />+  User-managed scaling and resiliency setup   | +  Dedicated network rack; four networking devices and four network links   | +  Integrated networking; two Outpost network devices, each connected to both of your upstream devices (four uplink link aggregation groups (LAGs) total) <br />+  No separate aggregation layer   | 
| **Locally supported services** | Amazon EC2, Amazon EBS, Amazon S3, Amazon EBS snapshots, Amazon EKS, Amazon ECS, Route 53 Resolver, Amazon RDS, Amazon EMR, AWS IoT Greengrass, Application Load Balancers, Amazon ElastiCache, Elastic Disaster Recovery | Amazon EC2, Amazon EBS, Amazon S3, Amazon EKS, Amazon ECS, Amazon RDS, AWS IoT Greengrass, Application Load Balancers | Amazon EC2, Amazon EBS, Amazon EKS, Amazon ECS, Amazon RDS, AWS IoT Greengrass, Application Load Balancers<br />Amazon S3 is not available on the single-rack configuration. | 
| **Power** | Supported power configurations: 5 kVA, 10 kVA, or 15 kVA | Supported power configurations: 10 kVA, 15 kVA, 30 kVA | Supported power configurations: 10 kVA, 15 kVA, 30 kVA | 
| **Minimum footprint** | One compute rack | Two racks: one compute and one network | One 42U rack (compute, storage, and networking integrated) | 
| **Scalability** | Add compute racks as needed | Add compute racks as needed, connected to one network rack | Single rack only; cannot add racks (no scale-out). Add capacity within the rack (scale-up). | 

## Key concepts
<a name="concepts"></a>

These are the key concepts:
+ **Outpost site** – The customer-managed physical buildings where AWS will install your Outpost. A site must meet the facility, networking, and power requirements for your Outpost.
+ **Outpost capacity** – Compute and storage resources available on the Outpost. You can view and manage the capacity for your Outpost from the AWS Outposts console.
+ **Outpost equipment** – Physical hardware that provides access to the AWS Outposts service. The hardware includes racks, servers, switches, and cabling owned and managed by AWS.
+ **Outposts racks** – An Outpost form factor that is an industry-standard 42U rack. Outposts racks include rack-mountable servers, switches, a network patch panel, a power shelf and blank panels. The single-rack configuration bundles networking, compute, and storage in one 42U rack.
+ **Network racks** – Designed for networking, a network rack has a traffic aggregation layer for all connected compute and storage racks allowing you to decouple compute scaling from networking. This enables cost-efficient scaling of your on-premises workloads based on specific workload needs. The network rack also comes with built-in resiliency to handle network device failures, making it easier for you to architect for high availability of your Outposts network. In addition, you can define the local gateway (LGW) network configurations, including IP addresses, Virtual LAN (VLAN) and Border Gateway Protocol (BGP) settings, through the API and console. Only the multi-rack configuration uses a separate network rack. The single-rack configuration integrates networking into the rack and does not use a separate network rack.
+ **Outposts servers** – An Outpost form factor that is an industry-standard 1U or 2U server, which can be installed in a standard EIA-310D 19 compliant 4 post rack. Outposts servers provide local compute and networking services to sites that have limited space or smaller capacity requirements.
+ **Single-rack Outposts** – A second-generation Outposts configuration that combines AWS managed compute, storage, and networking in a single 42U rack for space- and power-constrained sites. You cannot expand it by adding racks.
+ **Outpost owner** – The account owner for the account that places the AWS Outposts order. After AWS engages with the customer, the owner may include additional points of contact. AWS will communicate with the contacts to clarify orders, installation appointments, and hardware maintenance and replacement. Contact [AWS Support Center](https://console.aws.amazon.com/support/home#/) if the contact information changes. 
+ **Service link** – Network route that enables communication between your Outpost and its associated AWS Region. Each Outpost is an extension of an Availability Zone and its associated Region.
+ **Local gateway (LGW)** – A logical interconnect virtual router that enables communication between an Outposts rack and your on-premises network. 

## Supported AWS services by AWS Region
<a name="second-gen-rack-service-available"></a>

AWS Outposts supports AWS services based on the AWS Region in which your Outpost operates. To determine the supported services, view your Region in the respective geographic area:

**Topics**
+ [North America](#service-north-america)
+ [Asia Pacific](#service-asia-pacific)
+ [Europe](#service-europe)

### North America
<a name="service-north-america"></a>

The following table indicates AWS Outposts support for AWS services in North America Regions.


| AWS Region | Application Load Balancer | Amazon EBS | Amazon EC2 | Amazon ECS | Amazon EKS | Amazon EMR | AWS IoT Greengrass | Amazon RDS SQL, MySQL, PostgreSQL, and Oracle | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| US East (N. Virginia) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| US East (Ohio) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| US West (N. California) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| US West (Oregon) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 
| Canada (Central) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 

### Asia Pacific
<a name="service-asia-pacific"></a>

The following table indicates AWS Outposts support for AWS services in Asia Pacific Regions.


| AWS Region | Application Load Balancer | Amazon EBS | Amazon EC2 | Amazon ECS | Amazon EKS | Amazon EMR | AWS IoT Greengrass | Amazon RDS SQL, MySQL, PostgreSQL, and Oracle | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Asia Pacific (Singapore) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 

### Europe
<a name="service-europe"></a>

The following table indicates AWS Outposts support for AWS services in Europe Regions.


| AWS Region | Application Load Balancer | Amazon EBS | Amazon EC2 | Amazon ECS | Amazon EKS | Amazon EMR | AWS IoT Greengrass | Amazon RDS SQL, MySQL, PostgreSQL, and Oracle | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Europe (London) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | 

## Pricing
<a name="pricing"></a>

Pricing is based on your order details. When you place an order, you can choose from a variety of Outpost configurations, each providing a combination of Amazon EC2 instance types and storage options. You also choose a contract term and a payment option. Pricing includes delivery, installation, infrastructure service maintenance, software patches and upgrades, and rack removal. The single-rack configuration uses the same instance-based pricing model as other Outposts rack configurations.

For pricing based on location, configuration, and payment option, see: [Outposts racks pricing](https://aws.amazon.com/outposts/rack/pricing/)

You are billed for shared resources and any data transfer from the AWS Region to the Outpost. You are also billed for data transfers that AWS performs to maintain availability and security.