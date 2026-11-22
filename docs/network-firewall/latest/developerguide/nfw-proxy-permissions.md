

# Permissions for a NAT/Proxy firewall

For a NAT/Proxy firewall, Network Firewall makes Amazon EC2 and Route 53 requests with the credentials of the principal that calls Network Firewall. In addition to the Network Firewall actions, the principal's IAM policies, and any service control policies that apply to the account, must allow the following.


| Task | Additional permissions | 
| --- | --- | 
| Create a firewall, or add an Availability Zone | ec2:CreateNatGateway, ec2:AttachApplianceToNatGateway, ec2:DescribeSubnets, and ec2:CreateNetworkInterfacePermission | 
| Remove an Availability Zone, or delete a firewall | ec2:DetachApplianceFromNatGateway and ec2:DeleteNetworkInterfacePermission | 
| Delete a firewall and the NAT gateways that it created | ec2:DeleteNatGateway | 
| Create or delete a VPC endpoint association | route53:AssociateVPCWithHostedZone and route53:DisassociateVPCFromHostedZone | 
| Use a custom hostname and certificate | Permission for Network Firewall to use the ACM certificate, the same as for certificates in TLS inspection configurations. For information, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md). | 

For information about Network Firewall permissions, see [Identity and Access Management for AWS Network Firewall](security-iam.md).