# What is AWS Outposts?

AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and
tools to customer premises. By providing local access to AWS managed infrastructure, AWS Outposts
enables customers to build and run applications on premises using the same programming
interfaces as in [AWS
Regions](../../../global-infrastructure/latest/regions/aws-regions-availability-zones.md "../../../global-infrastructure/latest/regions/aws-regions-availability-zones.md"), while using local compute and storage resources for lower latency and local
data processing needs.

An Outpost is a pool of AWS compute and storage capacity deployed at a
customer site. AWS operates, monitors, and manages this capacity as part of an AWS Region.
You can create subnets on your Outpost and specify them when you create AWS resources such as
EC2 instances, EBS volumes, ECS clusters, and RDS instances. Instances in Outpost subnets
communicate with other instances in the AWS Region using private IP addresses, all within the
same VPC.

###### Note

You can't connect an Outpost to another Outpost or Local Zone that is within the same
VPC.

For more information, see the [AWS Outposts product
page](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

## Key concepts

These are the key concepts for AWS Outposts.

- Outpost site – The customer-managed physical
  buildings where AWS will install your Outpost. A site must meet the facility,
  networking, and power requirements for your Outpost.
- Outpost capacity – Compute and storage resources
  available on the Outpost. You can view and manage the capacity for your Outpost from the
  AWS Outposts console. AWS Outposts supports self-service capacity management that you can define at
  the Outposts level to reconfigure all of the assets in an Outposts or specifically for
  each individual asset. An Outpost asset can be a single server within an Outposts rack or
  an Outposts server.
- Outpost equipment – Physical hardware that
  provides access to the AWS Outposts service. The hardware includes racks, servers, switches,
  and cabling owned and managed by AWS.
- Outposts racks – An Outpost form factor that is an
  industry-standard 42U rack. Outposts racks include rack-mountable servers, switches, a network
  patch panel, a power shelf and blank panels.
- Outposts ACE racks – The Aggregation, Core, Edge
  (ACE) rack acts as a network aggregation point for multi-rack Outpost deployments. The ACE
  rack reduces the number of physical networking port and logical interface requirements by
  providing connectivity between multiple Outpost compute racks in your logical Outposts and
  your on-premise network.

You must install an ACE rack if you have four or more compute racks. If you have less
than four compute racks but plan to expand to four or more racks in the future, we
recommend that you install an ACE rack at the earliest.

For additional information on ACE racks, see [Scaling AWS Outposts rack
deployments with ACE racks](https://aws.amazon.com/blogs/compute/scaling-aws-outposts-rack-deployments-with-ace-racks/ "https://aws.amazon.com/blogs/compute/scaling-aws-outposts-rack-deployments-with-ace-racks/").

- Outposts servers – An Outpost form factor that is an
  industry-standard 1U or 2U server, which can be installed in a standard EIA-310D 19
  compliant 4 post rack. Outposts servers provide local compute and networking services to sites
  that have limited space or smaller capacity requirements.
- Outpost owner – The account owner for the
  account that places the AWS Outposts order. After AWS engages with the customer, the owner may
  include additional points of contact. AWS will communicate with the contacts to clarify
  orders, installation appointments, and hardware maintenance and replacement. Contact
  [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") if the contact information changes.
- Service link – Network route that enables
  communication between your Outpost and its associated AWS Region. Each Outpost is an
  extension of an Availability Zone and its associated Region.
- Local gateway (LGW) – A logical interconnect
  virtual router that enables communication between an Outposts rack and your on-premises network.
- Local network interface – A network interface
  that enables communication from an Outposts server and your on-premises network.

## AWS resources on Outposts

You can create the following resources on your Outpost to support low-latency workloads
that must run in close proximity to on-premises data and applications:

| Compute                                                                                                                                                                                                   | Resource type | Racks | Servers |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ------- |
| [Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#outposts-instances "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#outposts-instances") | Yes           | Yes   |
| [Amazon ECS<br>clusters](../../../AmazonECS/latest/developerguide/using-outposts.md "../../../AmazonECS/latest/developerguide/using-outposts.md")                                                         | Yes           | Yes   |
| [Amazon EKS<br>nodes](../../../eks/latest/userguide/eks-outposts.md "../../../eks/latest/userguide/eks-outposts.md")                                                                                      | Yes           | No    |

| Database and analytics                                                                                                                                                                        | Resource type | Racks | Servers |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ------- |
| [Amazon ElastiCache<br>nodes](../../../AmazonElastiCache/latest/dg/ElastiCache-Outposts.md "../../../AmazonElastiCache/latest/dg/ElastiCache-Outposts.md") (Redis cluster, Memcached cluster) | Yes           | No    |
| [Amazon EMR<br>clusters](../../../emr/latest/ManagementGuide/emr-plan-outposts.md "../../../emr/latest/ManagementGuide/emr-plan-outposts.md")                                                 | Yes           | No    |
| [Amazon RDS DB<br>instances](../../../AmazonRDS/latest/UserGuide/rds-on-outposts.md "../../../AmazonRDS/latest/UserGuide/rds-on-outposts.md")                                                 | Yes           | No    |

| Networking                                                                                                                                                                                                                                | Resource type | Racks | Servers |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----- | ------- |
| [App Mesh Envoy<br>proxy](../../../app-mesh/latest/userguide/app-mesh-on-outposts.md "../../../app-mesh/latest/userguide/app-mesh-on-outposts.md")                                                                                        | Yes           | Yes   |
| [Application Load Balancers](../../../elasticloadbalancing/latest/application/application-load-balancers.md#subnets-load-balancer "../../../elasticloadbalancing/latest/application/application-load-balancers.md#subnets-load-balancer") | Yes           | No    |
| [Amazon VPC subnets](../../../vpc/latest/userguide/Extend_VPCs.md#outposts "../../../vpc/latest/userguide/Extend_VPCs.md#outposts")                                                                                                       | Yes           | Yes   |
| [Amazon Route 53](../../../Route53/latest/DeveloperGuide/outpost-resolver.md "../../../Route53/latest/DeveloperGuide/outpost-resolver.md")                                                                                                | Yes           | No    |

| Storage                                                                                                                                                                                                | Resource type | Racks | Servers |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----- | ------- |
| [Amazon EBS<br>volumes](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#outposts-volumes "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#outposts-volumes") | Yes           | No    |
| [Amazon S3 buckets](../../../AmazonS3/latest/s3-outposts/S3onOutposts.md "../../../AmazonS3/latest/s3-outposts/S3onOutposts.md")                                                                       | Yes           | No    |

| Other AWS services | Service | Racks | Servers |
| ------------------ | ------- | ----- | ------- |
| AWS IoT Greengrass | Yes     | Yes   |

## Supported AWS services by AWS Region

AWS Outposts supports AWS services based on the AWS Region in which your Outpost operates. To
determine the supported services, view your Region in the respective geographic area:

###### Areas

- [North America](#service-north-america "#service-north-america")
- [Africa](#service-africa "#service-africa")
- [Asia Pacific](#service-asia-pacific "#service-asia-pacific")
- [Europe](#service-europe "#service-europe")
- [Middle East](#service-middle-east "#service-middle-east")
- [South America](#service-south-america "#service-south-america")

### North America

The following table indicates AWS Outposts support for AWS services in North America Regions.

| AWS Region              | Amazon EC2 | Amazon EBS | Amazon EBS Snapshots | Amazon S3 | Amazon RDS SQL, MySQL and PostgreSQL | Amazon ECS | Amazon EKS | Amazon EKS-LC | Amazon EMR | Amazon ElastiCache | CloudEndure Migrations | Elastic Disaster Recovery | Application Load Balancer | Direct Connect | Amazon VPC | Local Gateway |
| ----------------------- | ---------- | ---------- | -------------------- | --------- | ------------------------------------ | ---------- | ---------- | ------------- | ---------- | ------------------ | ---------------------- | ------------------------- | ------------------------- | -------------- | ---------- | ------------- |
| US East (N. Virginia)   | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| US East (Ohio)          | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| US West (N. California) | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| US West (Oregon)        | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Canada (Central)        | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |

### Africa

The following table indicates AWS Outposts support for AWS services in Africa Regions.

| AWS Region         | Amazon EC2 | Amazon EBS | Amazon EBS Snapshots | Amazon S3 | Amazon RDS SQL, MySQL and PostgreSQL | Amazon ECS | Amazon EKS | Amazon EKS-LC | Amazon EMR | Amazon ElastiCache | CloudEndure Migrations | Elastic Disaster Recovery | Application Load Balancer | Direct Connect | Amazon VPC | Local Gateway |
| ------------------ | ---------- | ---------- | -------------------- | --------- | ------------------------------------ | ---------- | ---------- | ------------- | ---------- | ------------------ | ---------------------- | ------------------------- | ------------------------- | -------------- | ---------- | ------------- |
| Africa (Cape Town) | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | No            | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |

### Asia Pacific

The following table indicates AWS Outposts support for AWS services in Asia Pacific Regions.

| AWS Region               | Amazon EC2 | Amazon EBS | Amazon EBS Snapshots | Amazon S3 | Amazon RDS SQL, MySQL and PostgreSQL | Amazon ECS | Amazon EKS | Amazon EKS-LC | Amazon EMR | Amazon ElastiCache | CloudEndure Migrations | Elastic Disaster Recovery | Application Load Balancer | Direct Connect | Amazon VPC | Local Gateway |
| ------------------------ | ---------- | ---------- | -------------------- | --------- | ------------------------------------ | ---------- | ---------- | ------------- | ---------- | ------------------ | ---------------------- | ------------------------- | ------------------------- | -------------- | ---------- | ------------- |
| Asia Pacific (Jakarta)   | Yes        | Yes        | Yes                  | Yes       | No                                   | Yes        | Yes        | No            | Yes        | Yes                | No                     | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Asia Pacific (Mumbai)    | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | No            | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Asia Pacific (Osaka)     | Yes        | Yes        | Yes                  | Yes       | No                                   | Yes        | Yes        | No            | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Asia Pacific (Seoul)     | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Asia Pacific (Singapore) | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Asia Pacific (Sydney)    | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Asia Pacific (Tokyo)     | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |

### Europe

The following table indicates AWS Outposts support for AWS services in Europe Regions.

| AWS Region         | Amazon EC2 | Amazon EBS | Amazon EBS Snapshots | Amazon S3 | Amazon RDS SQL, MySQL and PostgreSQL | Amazon ECS | Amazon EKS | Amazon EKS-LC | Amazon EMR | Amazon ElastiCache | CloudEndure Migrations | Elastic Disaster Recovery | Application Load Balancer | Direct Connect | Amazon VPC | Local Gateway |
| ------------------ | ---------- | ---------- | -------------------- | --------- | ------------------------------------ | ---------- | ---------- | ------------- | ---------- | ------------------ | ---------------------- | ------------------------- | ------------------------- | -------------- | ---------- | ------------- |
| Europe (Frankfurt) | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Europe (Ireland)   | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | No            | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Europe (London)    | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Europe (Milan)     | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | No            | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Europe (Paris)     | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | No            | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Europe (Stockholm) | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | No            | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |

### Middle East

The following table indicates AWS Outposts support for AWS services in Middle East Regions.

| AWS Region            | Amazon EC2 | Amazon EBS | Amazon EBS Snapshots | Amazon S3 | Amazon RDS SQL, MySQL and PostgreSQL | Amazon ECS | Amazon EKS | Amazon EKS-LC | Amazon EMR | Amazon ElastiCache | CloudEndure Migrations | Elastic Disaster Recovery | Application Load Balancer | Direct Connect | Amazon VPC | Local Gateway |
| --------------------- | ---------- | ---------- | -------------------- | --------- | ------------------------------------ | ---------- | ---------- | ------------- | ---------- | ------------------ | ---------------------- | ------------------------- | ------------------------- | -------------- | ---------- | ------------- |
| Israel (Tel Aviv)     | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | No            | Yes        | Yes                | No                     | Yes                       | No                        | Yes            | Yes        | Yes           |
| Middle East (Bahrain) | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |
| Middle East (UAE)     | Yes        | Yes        | No                   | No        | No                                   | Yes        | Yes        | No            | Yes        | Yes                | No                     | Yes                       | No                        | Yes            | Yes        | Yes           |

### South America

The following table indicates AWS Outposts support for AWS services in South America Regions.

| AWS Region                | Amazon EC2 | Amazon EBS | Amazon EBS Snapshots | Amazon S3 | Amazon RDS SQL, MySQL and PostgreSQL | Amazon ECS | Amazon EKS | Amazon EKS-LC | Amazon EMR | Amazon ElastiCache | CloudEndure Migrations | Elastic Disaster Recovery | Application Load Balancer | Direct Connect | Amazon VPC | Local Gateway |
| ------------------------- | ---------- | ---------- | -------------------- | --------- | ------------------------------------ | ---------- | ---------- | ------------- | ---------- | ------------------ | ---------------------- | ------------------------- | ------------------------- | -------------- | ---------- | ------------- |
| South America (São Paulo) | Yes        | Yes        | Yes                  | Yes       | Yes                                  | Yes        | Yes        | Yes           | Yes        | Yes                | Yes                    | Yes                       | Yes                       | Yes            | Yes        | Yes           |

## Amazon RDS on AWS Outposts supported Regions

Amazon RDS on AWS Outposts is available in the following AWS Regions:

- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Tokyo)
- Asia Pacific (Seoul)
- Asia Pacific (Osaka)
- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Canada (Central)
- China (Beijing)
- China (Ningxia)
- Europe (Frankfurt)
- Europe (Stockholm)
- Europe (Milan)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Israel (Tel Aviv)
- Middle East (UAE)
- Middle East (Bahrain)
- South America (São Paulo)
- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)

## Pricing

Pricing is based on your order details. When you place an order, you can choose from a
variety of Outpost configurations, each providing a combination of Amazon EC2 instance types and
storage options. You also choose a contract term and a payment option. Pricing includes the
following:

- **Outposts racks** - Delivery, installation, infrastructure
  service maintenance, software patches and upgrades, and rack removal.
- **Outposts servers** - Delivery, infrastructure service
  maintenance, and software patches and upgrades. You are responsible for the installation
  and packing the server for return.

You are billed for shared resources and any data transfer from the AWS Region to the
Outpost. You are also billed for data transfers that AWS performs to maintain availability
and security.

For pricing based on location, configuration, and payment option, see:

- [Outposts racks pricing](https://aws.amazon.com/outposts/rack/pricing/ "https://aws.amazon.com/outposts/rack/pricing/")
- [Outposts servers
  pricing](https://aws.amazon.com/outposts/servers/pricing/ "https://aws.amazon.com/outposts/servers/pricing/")
