

# AWS PrivateLink for AWS Systems Manager for SAP
<a name="privatelink"></a>

You can use AWS PrivateLink to establish a private connection between your VPC and AWS Systems Manager for SAP by creating an interface VPC endpoint. With interface endpoints, you can privately access Systems Manager for SAP APIs without needing an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

Traffic between your VPC and Systems Manager for SAP stays within the AWS network. Amazon EC2 instances in your VPC don’t require public IP addresses to use Systems Manager for SAP APIs.

## Create a VPC endpoint for Systems Manager for SAP
<a name="create-vpc-endpoint"></a>

Use the following procedure to create a VPC endpoint for AWS Systems Manager for SAP.

To create a VPC endpoint:

1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. For **Service category**, choose ** AWS services**.

1. For **Service Name**, search for and select `com.amazonaws.[region].ssm-sap`. There should only be 1 entry.

1. For **VPC**, select the VPC where you want to create the endpoint.

1. For **Subnets**, select the subnets (Availability Zones) where you want to create the endpoint network interfaces.

1. For **Security group**, select one or more security groups to associate with the endpoint network interfaces.
   + Ensure the security group allows inbound HTTPS traffic (port 443) from the resources in your VPC that need to communicate with Systems Manager for SAP.

1. (Optional) Under **Policy**, you can keep the default setting **Full access** or customize the policy to restrict access.

1. Choose **Create endpoint**.

Note - VPC endpoints for AWS Systems Manager for SAP are dual-stack by default, supporting both IPv4 and IPv6 communication.

## Creating FIPS-compliant VPC endpoints
<a name="fips-endpoints"></a>

For customers who need to meet FIPS (Federal Information Processing Standard) compliance requirements, Systems Manager for SAP offers FIPS-compliant endpoints.

To create a FIPS-capable VPC endpoint:

1. Follow steps 1-4 from the standard VPC endpoint creation process above.

1. For **Service Name**, search for and select `com.amazonaws.[region].ssm-sap-fips`.

1. Continue with the remaining standard process steps.

**Note**  
FIPS endpoints are available only in specific AWS regions. Consult the Systems Manager for SAP documentation or AWS regional services list for availability information.

## Verify the endpoint connection
<a name="verify-connection"></a>

After creating the endpoint, verify its status:

1. In the VPC console, choose **Endpoints**.

1. Look for your newly created endpoint and check that its **Status** is **Available**.

1. Note the **Endpoint ID** for reference in case you need to troubleshoot connectivity issues.

## Important Notes About Service Dependencies
<a name="service-dependencies"></a>

When using Systems Manager for SAP with VPC endpoints, be aware that you are responsible for creating VPC endpoints for other AWS services that Systems Manager for SAP depends on, such as:
+ ssm
+ ssm-messages
+ ec2-messages

For more information on how to setup these endpoints, refer to the guide at [AWS Systems Manager VPC endpoints](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html).

If these dependent service endpoints are not configured, or if your VPC doesn’t have internet access through an internet gateway or NAT gateway, operations involving these services will fail. Review your security group and network ACL configurations to ensure they allow traffic to these dependent service endpoints.

## Considerations
<a name="considerations"></a>
+ VPC endpoint policies support all Systems Manager for SAP API operations
+  AWS PrivateLink charges apply when using interface VPC endpoints. For more information, refer to Pricing in the [AWS PrivateLink guide](https://aws.amazon.com/privatelink/pricing/) 
+ For information about endpoint quotas, see [AWS PrivateLink quotas](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-endpoints) 

## Additional Resources
<a name="additional-resources"></a>
+ For more information about enabling Systems Manager for SAP service dependency on VPC endpoints, see [AWS Systems Manager VPC endpoints](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html) 
+ For more information about AWS PrivateLink and VPC endpoints, see [AWS PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) 