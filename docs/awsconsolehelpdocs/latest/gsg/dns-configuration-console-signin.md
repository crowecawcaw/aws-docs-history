

# Configuring DNS for accessing AWS Management Console
<a name="dns-configuration-console-signin"></a>

AWS Management Console Private Access uses VPC endpoints to route browser traffic to the AWS Management Console. When you create VPC endpoints with private DNS enabled, AWS automatically resolves the AWS Management Console and AWS Sign-In domain names to the private IP addresses of your VPC endpoints. In most cases, you do not need to manually configure DNS records.

The DNS configuration depends on your network setup. The following sections describe the configuration for common scenarios.

## Single Region without internet access
<a name="dns-single-region-isolated"></a>

If you use a dedicated environment such as an Amazon EC2 instance or Amazon WorkSpaces inside a VPC without internet access, DNS resolution is handled automatically by the default VPC DNS resolver. When you create VPC endpoints for AWS Sign-In, AWS Management Console, and console static content with private DNS enabled, the VPC resolver directs traffic to the correct endpoints without additional configuration.

In this scenario, the following limitations apply:
+ The AWS Management Console relies on some dependencies that are hosted only in US East (N. Virginia). If you configure a different Region, some features such as Amazon Q Developer might not be available.
+ If you do not configure VPC endpoints for all AWS services that you use, requests to services without endpoints will fail.
+ Some service consoles make cross-Region calls. These calls will fail if you have not configured VPC peering and VPC endpoints in the target Region.

## Single Region connected to a corporate network
<a name="dns-single-region-corp"></a>

If you connect your VPC to a corporate network using Direct Connect or AWS Site-to-Site VPN, configure split-horizon DNS on your corporate DNS servers to direct AWS Management Console traffic to the VPC endpoints. Point the following domain suffixes to the corresponding VPC endpoints:
+ `.console.aws.amazon.com` – for the AWS Management Console
+ `.signin.aws.amazon.com` – for AWS Sign-In
+ `.amazonaws.com` / `.api.aws` – for AWS service APIs
+ `.console.api.aws` and `.console.awsstatic.com` – for AWS Management Console static content and internal APIs

## Multiple Regions connected to a corporate network
<a name="dns-multi-region-corp"></a>

If you use more than one Region, for example, if you use one Region for your infrastructure and need to access IAM or Route 53 in US East (N. Virginia), configure your corporate DNS to point regional prefixes to the corresponding VPC endpoints in each Region:
+ `.{{region}}.console.aws.amazon.com` – for the AWS Management Console in each Region
+ `.{{region}}.signin.aws.amazon.com` – for AWS Sign-In in each Region
+ `.{{region}}.amazonaws.com` / `.{{region}}.api.aws` – for AWS service APIs in each Region

In addition, point the following region-agnostic domains to VPC endpoints in one or two specific Regions. Any supported Region can handle these domains:
+ `.global.console.aws.amazon.com`
+ `.console.api.aws`
+ `.console.awsstatic.com`

**Note**  
Some service consoles, such as IAM, Cloudfront, and Route 53, are hosted only in US East (N. Virginia). To access these consoles, you must set up AWS Management Console Private Access in US East (N. Virginia) and use VPC peering or AWS Transit Gateway to connect it to your other Regions.

**Note**  
DynamoDB VPC endpoints require manual creation of a private hosted zone. See [AWS PrivateLink for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/privatelink-interface-endpoints.html) for instructions.