# Restrict access with VPC origins

You can use CloudFront to deliver content from applications that are hosted in your virtual
private cloud (VPC) private subnets. You can use Application Load Balancers (ALBs), Network Load Balancers (NLBs), and EC2
instances in private subnets as VPC origins.

Here are some reasons why you might want to use VPC origins:

- **Security** – VPC origins is designed to
  enhance the security posture of your application by placing your load balancers
  and EC2 instances in private subnets, making CloudFront the single point of entry.
  User requests go from CloudFront to the VPC origins over a private, secure connection,
  providing additional security for your applications.
- **Management** – VPC origins reduces the
  operational overhead required for secure connectivity between CloudFront and origins.
  You can move your origins to private subnets with no public access, and you
  don’t have to implement access control lists (ACLs) or other mechanisms to
  restrict access to your origins. This way, you don't have to invest in
  undifferentiated development work to secure your web applications with CloudFront.
- **Scalability and performance** – VPC origins
  helps you to secure your web applications, freeing up time to focus on growing
  your critical business applications while improving security and maintaining
  high performance and global scalability with CloudFront. VPC origins streamlines security
  management and reduces operational complexity so that you can use CloudFront as the
  single point of entry for your applications.

## Prerequisites

Before you create a VPC origin for your CloudFront distribution, you must complete the
following:

- Create a virtual private cloud (VPC) on Amazon VPC.

      + Your VPC must be in the same AWS account as your CloudFront
       distribution.
      + Your VPC must be in one of the AWS Regions that are supported
       for VPC origins. For more information, see [Supported AWS Regions for
       VPC origins](#vpc-origins-supported-regions "#vpc-origins-supported-regions").
      + Network ACLs associated with your VPC subnets apply to egress (outbound) traffic when client IP address preservation is enabled on your VPC origin. However, for traffic to be allowed to exit through your VPC origin you must configure the ACL as both an inbound and outbound rule.


      For example, to allow TCP and UDP clients using an ephemeral source port to connect to your endpoint through your VPC origin, associate the subnet of your endpoint with a Network ACL that allows outbound traffic destined to an ephemeral TCP or UDP port (port range 1024-65535, destination 0.0.0.0/0). In addition, create a matching inbound rule (port range 1024-65535, source 0.0.0.0/0).

  For information about creating a VPC, see [Create a VPC plus other VPC resources](../../../vpc/latest/userguide/create-vpc.md#create-vpc-and-other-resources "../../../vpc/latest/userguide/create-vpc.md#create-vpc-and-other-resources") in the
  _Amazon VPC User Guide_.

- Include the following in your VPC:
  - **Internet gateway** –
    You need to add an internet gateway to the VPC that has your VPC origin resources. The internet gateway is required to denote that the VPC can receive traffic from the internet. The internet gateway is not used for routing traffic to origins inside the subnet, and you don't need to update the routing policies.
  - **Private subnet with at least one available
    IPv4 address** – CloudFront routes to your subnet by
    using a service-managed elastic network interface (ENI) that CloudFront creates after
    you define your VPC origin resource with CloudFront. You must have at
    least one available IPv4 address in your private subnet so that the
    ENI creation process can succeed. The IPv4 address can be private,
    and there is no additional cost for it.

  ###### Note

  IPv6-only subnets are not supported.

- In the private subnet, launch an Application Load Balancer, a Network Load Balancer, or an EC2 instance to use
  as your origin.
  - The resource you launch must be fully deployed and in
    **Active** status before you can use it for a
    VPC origin.
  - Gateway Load Balancers, dual-stack Network Load Balancers and Network Load Balancers with TLS listeners can't be added as
    origins.
  - To be used as a VPC origin, a Network Load Balancer must have a security group
    attached to it.
  - Update your security groups for the VPC private origins to explicitly allow the CloudFront managed prefix list. For more information, see [Use the CloudFront managed prefix list](LocationsOfEdgeServers.md#managed-prefix-list "LocationsOfEdgeServers.md#managed-prefix-list").

  ###### Note

  CloudFront-VPCOrigins-Service-SG is an AWS reserved
  name for security groups that are used for VPC origins. You must
  specify a different name for your security group. For more
  information, see [Creating a security group](../../../vpc/latest/userguide/creating-security-groups.md "../../../vpc/latest/userguide/creating-security-groups.md").

      - After the VPC origin is created, the security group can be further
       restricted to allow only traffic from your VPC origins. To do this,
       update the allowed traffic source from the managed prefix list to
       the CloudFront security group.

  ###### Note

  WebSockets, gRPC traffic, origin request and origin response
  triggers with Lambda@Edge in CloudFront are not supported for VPC origins.
  For more information, see [Work with requests and
  responses](lambda-generating-http-responses.md "lambda-generating-http-responses.md") in the
  Lambda@Edge documentation.

## Create a VPC origin (new distribution)

The following procedure shows you how to create a VPC origin for your new CloudFront
distribution in the CloudFront console. Alternatively, you can use the [CreateVpcOrigin](../../../cloudfront/latest/APIReference/API_CreateVpcOrigin.md "../../../cloudfront/latest/APIReference/API_CreateVpcOrigin.md") and [CreateDistribution](../../../cloudfront/latest/APIReference/API_CreateDistribution.md "../../../cloudfront/latest/APIReference/API_CreateDistribution.md") API operations with the AWS CLI or an AWS
SDK.

###### To create a VPC origin for a new CloudFront distribution

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose **VPC origins**, **Create VPC
   origin**.
3. Fill out the required fields. For **Origin ARN**, select
   the ARN of your Application Load Balancer, Network Load Balancer, or EC2 instance. If you don’t see the ARN, you
   can copy your specific resource ARN and paste it here instead.
4. Choose **Create VPC origin**.
5. Wait for your VPC origin status to change to
   **Deployed**. This can take up to 15 minutes.
6. Choose **Distributions**, **Create
   distribution**.
7. For **Origin domain**, select your VPC origins resource from
   the dropdown list.

If your VPC origin is an EC2 instance, copy and paste the
**Private IP DNS name** of the instance into the
**Origin domain** field. 8. Finish creating your distribution. For more information, see [Create a CloudFront distribution in the console](distribution-web-creating-console.md#create-console-distribution "distribution-web-creating-console.md#create-console-distribution").

## Create a VPC origin (existing

distribution)

The following procedure shows you how to create a VPC origin for your existing
CloudFront distribution in the CloudFront console, which helps to ensure continuous availability
of your applications. Alternatively, you can use the [CreateVpcOrigin](../../../cloudfront/latest/APIReference/API_CreateVpcOrigin.md "../../../cloudfront/latest/APIReference/API_CreateVpcOrigin.md") and [UpdateDistributionWithStagingConfig](../../../cloudfront/latest/APIReference/API_UpdateDistributionWithStagingConfig.md "../../../cloudfront/latest/APIReference/API_UpdateDistributionWithStagingConfig.md") API operations with the AWS CLI or an
AWS SDK.

Optionally, you could choose to add your VPC origin to your existing distribution
without creating a staging distribution.

###### To create a VPC origin for your existing CloudFront distribution

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose **VPC origins**, **Create VPC
   origin**.
3. Fill out the required fields. For **Origin ARN**, select
   the ARN of your Application Load Balancer, Network Load Balancer, or EC2 instance. If you don’t see the ARN, you
   can copy your specific resource ARN and paste it here instead.
4. Choose **Create VPC origin**.
5. Wait for your VPC origin status to change to
   **Deployed**. This can take up to 15 minutes.
6. In the navigation pane, choose **Distributions**.
7. Choose the ID of your distribution.
8. On the **General** tab, under **Continuous
   deployment**, choose **Create staging
   distribution**. For more information, see [Use CloudFront continuous deployment to safely test CDN
   configuration changes](continuous-deployment.md "continuous-deployment.md").
9. Follow the steps in the **Create staging distribution**
   wizard to create a staging distribution. Include the following steps:
   - For **Origins**, choose **Create
     origin**.
   - For **Origin domain**, select your VPC origins
     resource from the dropdown menu.

   If your VPC origin is an EC2 instance, copy and paste the
   **Private IP DNS name** of the instance into
   the **Origin domain** field.
   - Choose **Create origin**.

10. In your staging distribution, test the VPC origin.
11. Promote the staging distribution configuration to your primary
    distribution. For more information, see [Promote a staging distribution configuration](working-with-staging-distribution-continuous-deployment-policy.md#promote-staging-distribution-configuration "working-with-staging-distribution-continuous-deployment-policy.md#promote-staging-distribution-configuration").
12. Remove public access to your VPC origin by making the subnet private.
    After you do this, the VPC origin won't be discoverable over the internet,
    but CloudFront will still have private access to it. For more information,
    see [Associate or disassociate a subnet with a route table](../../../vpc/latest/userguide/WorkWithRouteTables.md#AssociateSubnet "../../../vpc/latest/userguide/WorkWithRouteTables.md#AssociateSubnet") in the
    _Amazon VPC User Guide_.

## Update a VPC origin

The following procedure shows you how to update a VPC origin for your CloudFront
distribution in the CloudFront console. Alternatively, you can use the [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") and [UpdateVpcOrigin](../../../cloudfront/latest/APIReference/API_UpdateVpcOrigin.md "../../../cloudfront/latest/APIReference/API_UpdateVpcOrigin.md") API operations with the AWS CLI or an AWS SDK.

###### To update an existing VPC origin for your CloudFront distribution

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**.
3. Choose the ID of your distribution.
4. Choose the **Behaviors** tab.
5. Make sure that the VPC origin is not the default origin for your cache
   behavior.
6. Choose the **Origins** tab.
7. Select the VPC origin that you're going to update and choose
   **Delete**. This disassociates the VPC origin from your
   distribution. Repeat steps 2-7 to disassociate the VPC origin from any other
   distributions.
8. Choose **VPC origins**.
9. Select the VPC origin and choose **Edit**.
10. Make your updates and choose **Update VPC
    origin**.
11. Wait for your VPC origin status to change to
    **Deployed**. This can take up to 15 minutes.
12. In the navigation pane, choose **Distributions**.
13. Choose the ID of your distribution.
14. Choose the **Origins** tab.
15. Choose **Create origin**.
16. For **Origin domain**, select your VPC origins resource from
    the dropdown menu.

If your VPC origin is an EC2 instance, copy and paste the
**Private IP DNS name** of the instance into the
**Origin domain** field. 17. Choose **Create origin**. This associates the VPC origin
with your distribution again. Repeat steps 12-17 to associate the updated
VPC origin with any other distributions.

## Supported AWS Regions for

VPC origins

VPC origins are currently supported in the following commercial AWS Regions.
Availability Zone (AZ) exceptions are noted.

| Region Name               | Region                                 |
| ------------------------- | -------------------------------------- |
| US East (Ohio)            | `us-east-2`                            |
| US East (N. Virginia)     | `us-east-1 (except AZ use1-az3)`       |
| US West (N. California)   | `us-west-1 (except AZ usw1-az2)`       |
| US West (Oregon)          | `us-west-2`                            |
| Africa (Cape Town)        | `af-south-1`                           |
| Asia Pacific (Hong Kong)  | `ap-east-1`                            |
| Asia Pacific (Mumbai)     | `ap-south-1`                           |
| Asia Pacific (Hyderabad)  | `ap-south-2`                           |
| Asia Pacific (Jakarta)    | `ap-southeast-3`                       |
| Asia Pacific (Melbourne)  | `ap-southeast-4`                       |
| Asia Pacific (Osaka)      | `ap-northeast-3`                       |
| Asia Pacific (Singapore)  | `ap-southeast-1`                       |
| Asia Pacific (Sydney)     | `ap-southeast-2`                       |
| Asia Pacific (Tokyo)      | `ap-northeast-1 (except AZ apne1-az3)` |
| Asia Pacific (Seoul)      | `ap-northeast-2 (except AZ apne2-az1)` |
| Canada (Central)          | `ca-central-1 (except AZ cac1-az3)`    |
| Canada West (Calgary)     | `ca-west-1`                            |
| Europe (Frankfurt)        | `eu-central-1`                         |
| Europe (Ireland)          | `eu-west-1`                            |
| Europe (London)           | `eu-west-2`                            |
| Europe (Milan)            | `eu-south-1`                           |
| Europe (Paris)            | `eu-west-3`                            |
| Europe (Spain)            | `eu-south-2`                           |
| Europe (Stockholm)        | `eu-north-1`                           |
| Europe (Zurich)           | `eu-central-2`                         |
| Israel (Tel Aviv)         | `il-central-1`                         |
| Middle East (Bahrain)     | `me-south-1`                           |
| Middle East (UAE)         | `me-central-1`                         |
| South America (São Paulo) | `sa-east-1`                            |
