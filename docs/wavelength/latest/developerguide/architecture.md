

# Architect apps for Wavelength
<a name="architecture"></a>

Wavelength Zones are designed for the following workloads:
+ Applications that require edge resiliency across existing AWS hybrid and edge infrastructure deployments
+ Applications that need to connect to compute with low latency
+ Applications that need to run in a certain geography due to legal or regulatory requirements
+ Applications that need consistent data rates from mobile devices to compute in a Wavelength Zone

Review [Quotas and considerations for Wavelength Zones](wavelength-quotas.md), which includes information about available Wavelength Zones, service differences, and Service Quotas.

 Consider the following factors when using Wavelength Zones:
+ AWS recommends that you architect the edge applications in a hub and spoke model with the Region to provide the most scalable, resilient, and cost-effective options for components. For more information, see [Workload placement](#architecture-best-practices)
+ Services that run in Wavelength Zones have different compliance than services in an AWS Region. For more information, see [Compliance validation for AWS Wavelength](compliance-validation.md).

Most Wavelength Zones have network access that is specific to a telecommunication carrier and location. Therefore, you might need to have multiple Wavelength Zones for your latency-sensitive applications to meet your latency requirements. For more information, see [Networking considerations](wavelength-quotas.md#networking-considerations).

## Discover the closest Wavelength Zone endpoint
<a name="discover-nearest-wavelength-zone"></a>

You can use the following procedures to have client devices discover the closest Wavelength Zone endpoint, for example an Amazon EC2 instance:
+ Register the instance with a discovery service such as AWS Cloud Map. For information about how to register an instance, see [Registering Instances](https://docs.aws.amazon.com/cloud-map/latest/dg/registering-instances.html) in the *AWS Cloud Map Developer Guide*.
+ Another approach is to use multiple Wavelength Zones across your deployment and utilize adjacent Zones, powered by carrier-developed edge discovery services to route mobile traffic. For more information, see [Deploying dynamic 5G Edge Discovery architectures with AWS Wavelength](https://aws.amazon.com/blogs/industries/deploying-dynamic-5g-edge-discovery-architectures-with-aws-wavelength/).
+ Applications that run on client devices can run latency tests such as `ping` from the client to select the best endpoint that is registered in AWS Cloud Map, or can use the geolocation data from the mobile device.

## Load balancing
<a name="architecture-load-balancing"></a>

Application Load Balancer (ALB) is supported in select Wavelength Zones. Load balancers distribute your incoming traffic across multiple targets, such as Amazon EC2 instances, containers, and IP addresses, within the Wavelength Zone. Key considerations include:
+ Network Load Balancer (NLB) is not supported in Wavelength Zones. To learn more, see [Enabling load-balancing of non-HTTP(s) traffic on AWS Wavelength](https://aws.amazon.com/blogs/compute/enabling-load-balancing-of-non-https-traffic-on-aws-wavelength/).
+ Cross-Zone load balancing across multiple Wavelength Zones is not supported.

ALB is available in the following Wavelength Zones:
+ All Wavelength Zones in the `us-east-1` Region.
+ All Wavelength Zones in `us-west-2` Region.
+ All Wavelength Zones in the `ap-northeast-1` Region.
+ All Wavelength Zones in the `eu-central-1` Region.

## High availability
<a name="architecture-high-availability"></a>

Follow these strategies to deploy highly available architectures at the edge.

### Deployment
<a name="w2aac15c19b5"></a>

Consider the following:
+ **Multiple Wavelength Zones within a given VPC**: using techniques highlighted in the [Discover the closest Wavelength Zone endpoint](#discover-nearest-wavelength-zone) section, you can steer traffic to the optimal Wavelength Zone based on latency or application health.
+ **Combine Wavelength Zones with other AWS hybrid and edge locations**: you can combine AWS Local Zones subnets with AWS Wavelength Zones subnets to create highly-available deployments within a given geography. For example, you can create an Atlanta AWS Local Zone subnet (`us-east-1-atl-2a`) alongside an Atlanta Wavelength Zone subnet (`us-east-1-wl1-atl-wlz-1`) within the same VPC.

### DNS resolution
<a name="w2aac15c19b7"></a>

One way to create both physical and logical redundancy across your high-availability edge deployments is to utilize the parent Region as the failover, using simple Route 53-based failover policies to steer traffic to an available endpoint. For more information, see [Configuring DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html) in the *Amazon Route 53 Developer Guide*.

## Workload placement
<a name="architecture-best-practices"></a>

Run the following components in the Region:
+ Components that are less latency sensitive
+ Components that do not require data residency
+ Components that need to be shared across Zones
+ Components that need to persist state, such as databases

Run the application components that need low latency and higher bandwidth over mobile networks in Wavelength Zones.

For optimal throughput, AWS recommends that you use a public service endpoint when applications in the Wavelength Zone need to connect to AWS services in the parent Region.