**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Access Amazon EKS using AWS PrivateLink

You can use AWS PrivateLink to create a private connection between your VPC and Amazon Elastic Kubernetes Service. You can access Amazon EKS as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don’t need public IP addresses to access Amazon EKS.

You establish this private connection by creating an interface endpoint powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for Amazon EKS.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Before you begin

Before you start, make sure you have performed the following tasks:

- Review [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_

## Considerations

- **Support and Limitations**: Amazon EKS interface endpoints enable secure access to all Amazon EKS API actions from your VPC but come with specific limitations: they do not support access to Kubernetes APIs, as these have a separate private endpoint, you cannot configure Amazon EKS to be accessible only through the interface endpoint.
- **Pricing**: Using interface endpoints for Amazon EKS incurs standard AWS PrivateLink charges: hourly charges for each endpoint provisioned in each Availability Zone, data processing charges for traffic through the endpoint. To learn more, see [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/").
- **Security and Access Control**: We recommend enhancing security and controlling access with these additional configurations—use VPC endpoint policies to control access to Amazon EKS through the interface endpoint, associate security groups with endpoint network interfaces to manage traffic, use VPC flow logs to capture and monitor IP traffic to and from the interface endpoints, with logs publishable to Amazon CloudWatch or Amazon S3. To learn more, see [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") and [Logging IP traffic using VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md").
- **Connectivity Options**: Interface endpoints offer flexible connectivity options using **on-premises access** (connect your on-premises data center to a VPC with the interface endpoint using AWS Direct Connect or AWS Site-to-Site VPN) or via **inter-VPC connectivity** (use AWS Transit Gateway or VPC peering to connect other VPCs to the VPC with the interface endpoint, keeping traffic within the AWS network).
- **IP Version Support**: Endpoints created before August 2024 support only IPv4 using eks.region.amazonaws.com. New endpoints created after August 2024 support dual-stack IPv4 and IPv6 (e.g., eks.region.amazonaws.com, eks.region.api.aws).
- **Regional Availability**: AWS PrivateLink for the EKS API is not available in Asia Pacific (Malaysia) (ap-southeast-5), Asia Pacific (Thailand) (ap-southeast-7), Mexico (Central) (mx-central-1), and Asia Pacific (Taipei) (ap-east-2) regions. AWS PrivateLink support for eks-auth (EKS Pod Identity) is available in the Asia Pacific (Malaysia) (ap-southeast-5) region.

## Create an interface endpoint for Amazon EKS

You can create an interface endpoint for Amazon EKS using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for Amazon EKS using the following service names:

### EKS API

- com.amazonaws.region-code.eks
- com.amazonaws.region-code.eks-fips (for FIPS-compliant endpoints)

### EKS Auth API (EKS Pod Identity)

- com.amazonaws.region-code.eks-auth

## Private DNS feature for Amazon EKS interface endpoints

The private DNS feature, enabled by default for interface endpoints of Amazon EKS and other AWS services, facilitates secure and private API requests using default Regional DNS names. This feature ensures that API calls are routed through the interface endpoint over the private AWS network, enhancing security and performance.

The private DNS feature activates automatically when you create an interface endpoint for Amazon EKS or other AWS services. To enable, you need to configure your VPC correctly by setting specific attributes:

- **enableDnsHostnames**: Allows instances within the VPC to have DNS hostnames.
- **enableDnsSupport**: Enables DNS resolution throughout the VPC.

For step-by-step instructions to check or modify these settings, see [View and update DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating").

### DNS names and IP address types

With the private DNS feature enabled, you can use specific DNS names to connect to Amazon EKS, and these options evolve over time:

- **eks.region.amazonaws.com**: The traditional DNS name, resolving only to IPv4 addresses before August 2024. For existing endpoints updated to dual-stack, this name resolves to both IPv4 and IPv6 addresses.
- **eks.region.api.aws**: Available for new endpoints created after August 2024, this dual-stack DNS name resolves to both IPv4 and IPv6 addresses.

After August 2024, new interface endpoints come with two DNS names, and you can opt for the dual-stack IP address type. For existing endpoints, updating to dual-stack modifies **eks.region.amazonaws.com** to support both IPv4 and IPv6.

### Using the Private DNS feature

Once configured, the private DNS feature can be integrated into your workflows, offering the following capabilities:

- **API Requests**: Use the default Regional DNS names, either `eks.region.amazonaws.com` or `eks.region.api.aws`, based on your endpoint’s setup to make API requests to Amazon EKS.
- **Application Compatibility**: Your existing applications that call EKS APIs require no changes to leverage this feature.
- **AWS CLI with Dual-Stack**: To use the dual-stack endpoints with the AWS CLI, see the [Dual-stack and FIPS endpoints](../../../sdkref/latest/guide/feature-endpoints.md "../../../sdkref/latest/guide/feature-endpoints.md") configuration in the _AWS SDKs and Tools Reference Guide_.
- **Automatic Routing**: Any call to the Amazon EKS default service endpoint is automatically directed through the interface endpoint, ensuring private and secure connectivity.
