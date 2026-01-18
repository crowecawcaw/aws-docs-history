# AWS PrivateLink for AWS Systems Manager for SAP

You can use AWS PrivateLink to establish a private connection between your VPC and AWS Systems Manager for SAP by creating an interface VPC endpoint. With interface endpoints, you can privately access Systems Manager for SAP APIs without needing an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

Traffic between your VPC and Systems Manager for SAP stays within the AWS network. Amazon EC2 instances in your VPC don’t require public IP addresses to use Systems Manager for SAP APIs.

## Create a VPC endpoint for Systems Manager for SAP

Use the following procedure to create a VPC endpoint for AWS Systems Manager for SAP.

To create a VPC endpoint:

1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. For **Service category**, choose **AWS services**.
5. For **Service Name**, search for and select `com.amazonaws.[region].ssm-sap`. There should only be 1 entry.
6. For **VPC**, select the VPC where you want to create the endpoint.
7. For **Subnets**, select the subnets (Availability Zones) where you want to create the endpoint network interfaces.
8. For **Security group**, select one or more security groups to associate with the endpoint network interfaces.
   - Ensure the security group allows inbound HTTPS traffic (port 443) from the resources in your VPC that need to communicate with Systems Manager for SAP.

9. (Optional) Under **Policy**, you can keep the default setting **Full access** or customize the policy to restrict access.
10. Choose **Create endpoint**.

Note - VPC endpoints for AWS Systems Manager for SAP are dual-stack by default, supporting both IPv4 and IPv6 communication.

## Creating FIPS-compliant VPC endpoints

For customers who need to meet FIPS (Federal Information Processing Standard) compliance requirements, Systems Manager for SAP offers FIPS-compliant endpoints.

To create a FIPS-capable VPC endpoint:

1. Follow steps 1-4 from the standard VPC endpoint creation process above.
2. For **Service Name**, search for and select `com.amazonaws.[region].ssm-sap-fips`.
3. Continue with the remaining standard process steps.

###### Note

FIPS endpoints are available only in specific AWS regions. Consult the Systems Manager for SAP documentation or AWS regional services list for availability information.

## Verify the endpoint connection

After creating the endpoint, verify its status:

1. In the VPC console, choose **Endpoints**.
2. Look for your newly created endpoint and check that its **Status** is **Available**.
3. Note the **Endpoint ID** for reference in case you need to troubleshoot connectivity issues.

## Important Notes About Service Dependencies

When using Systems Manager for SAP with VPC endpoints, be aware that you are responsible for creating VPC endpoints for other AWS services that Systems Manager for SAP depends on, such as:

- ssm
- ssm-messages
- ec2-messages

For more information on how to setup these endpoints, refer to the guide at [AWS Systems Manager VPC endpoints](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md").

If these dependent service endpoints are not configured, or if your VPC doesn’t have internet access through an internet gateway or NAT gateway, operations involving these services will fail. Review your security group and network ACL configurations to ensure they allow traffic to these dependent service endpoints.

## Considerations

- VPC endpoint policies support all Systems Manager for SAP API operations
- AWS PrivateLink charges apply when using interface VPC endpoints. For more information, refer to Pricing in the [AWS PrivateLink guide](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/")
- For information about endpoint quotas, see [AWS PrivateLink quotas](../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-endpoints "../../../vpc/latest/userguide/amazon-vpc-limits.md#vpc-limits-endpoints")

## Additional Resources

- For more information about enabling Systems Manager for SAP service dependency on VPC endpoints, see [AWS Systems Manager VPC endpoints](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md")
- For more information about AWS PrivateLink and VPC endpoints, see [AWS PrivateLink Guide](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md")
