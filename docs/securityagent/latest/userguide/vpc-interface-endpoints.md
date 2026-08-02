# AWS Security Agent and interface VPC endpoints (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and AWS Security Agent. You can access Security Agent as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don’t need public IP addresses to access Security Agent.

You establish this private connection by creating an _interface endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for Security Agent.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for Security Agent

Before you set up an interface endpoint for Security Agent, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

Security Agent supports making calls to all of its API actions from your VPC, including operations for managing Agent Spaces, penetration tests, and security findings.

You can select IPv4, IPv6, or dualstack when creating an endpoint.

VPC endpoint policies are supported for Security Agent. By default, full access to Security Agent is allowed through the interface endpoint. You can control access by attaching an endpoint policy to the interface endpoint or by associating a security group with the endpoint network interfaces.

All API calls to Security Agent are encrypted using TLS 1.2 or higher, including calls made through VPC endpoints. For more information about data protection, see [Data protection in AWS Security Agent](data-protection.md "data-protection.md"). Security Agent API calls are logged in AWS CloudTrail. For more information, see [Example: AWS Security Agent log file entries](understanding-cloudtrail-entries.md "understanding-cloudtrail-entries.md").

## Create an interface endpoint for Security Agent

You can create an interface endpoint for Security Agent using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for Security Agent using the following service name:

```
com.amazonaws.<region>.securityagent
```

To create the interface endpoint using the AWS CLI, run the following command. Replace the Region, VPC ID, subnet IDs, and security group ID with your own values.

```
aws ec2 create-vpc-endpoint \
    --vpc-id vpc-1a2b3c4d \
    --vpc-endpoint-type Interface \
    --service-name com.amazonaws.<region>.securityagent \
    --subnet-ids subnet-1a2b3c4d subnet-5e6f7a8b \
    --security-group-ids sg-1a2b3c4d \
    --private-dns-enabled
```

###### Important

Private DNS must be enabled for the interface endpoint. Security Agent requires you to use the default Regional DNS name (for example, `securityagent.us-east-1.api.aws`) to make API requests through the endpoint. Calling the endpoint-specific VPCE URL directly is not supported.

To use private DNS, you must set both the `enableDnsSupport` and `enableDnsHostnames` attributes to `true` for your VPC. For more information, see [DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support") in the _Amazon VPC User Guide_.

## Configure security groups for the interface endpoint

When you create an interface endpoint, you can associate security groups with the endpoint network interfaces to control traffic to Security Agent. Create a security group that allows inbound HTTPS traffic (port 443) from the resources in your VPC that need to communicate with Security Agent.

The security group should include the following inbound rule:

- Type: HTTPS
- Protocol: TCP
- Port range: 443
- Source: Your VPC CIDR block (for example, `10.0.0.0/16`) or the security group IDs of the resources that need access to Security Agent

For more information, see [Security groups](../../../vpc/latest/privatelink/interface-endpoints.md#vpc-endpoints-security "../../../vpc/latest/privatelink/interface-endpoints.md#vpc-endpoints-security") in the _AWS PrivateLink Guide_.

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint. The default endpoint policy allows full access to Security Agent through the interface endpoint. To control the access allowed to Security Agent from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.

**Example: VPC endpoint policy for AWS Security Agent actions**

The following is an example of an endpoint policy for AWS Security Agent. When attached to an endpoint, this policy grants access to the listed AWS Security Agent actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": "*",
         "Action": [
            "securityagent:CreatePentest",
            "securityagent:ListPentests",
            "securityagent:BatchGetPentests",
            "securityagent:StartPentestExecution",
            "securityagent:StopPentestExecution",
            "securityagent:ListFindings",
            "securityagent:BatchGetFindings"
         ],
         "Resource": "*"
      }
   ]
}
```

**Example: VPC endpoint policy that denies all access from a specified AWS account**

The following VPC endpoint policy denies AWS account `123456789012` all access to resources using the endpoint. The policy allows all actions from other accounts.

```
{
   "Statement": [
      {
         "Effect": "Allow",
         "Principal": "*",
         "Action": "securityagent:*",
         "Resource": "*"
      },
      {
         "Effect": "Deny",
         "Principal": {
            "AWS": "123456789012"
         },
         "Action": "securityagent:*",
         "Resource": "*"
      }
   ]
}
```

## Troubleshooting

**Connection times out when calling Security Agent API**

- Verify that the VPC endpoint status is `available`:

```
aws ec2 describe-vpc-endpoints --vpc-endpoint-ids vpce-1a2b3c4d \
    --query "VpcEndpoints[].State"
```

- Confirm that the security group associated with the endpoint allows inbound TCP traffic on port 443 from your VPC CIDR or source security group.
- Check that your VPC route tables do not route Security Agent traffic to an internet gateway or NAT gateway instead of the endpoint.

**DNS resolution fails for `securityagent.<region>.api.aws`**

- Verify that private DNS is enabled on the endpoint:

```
aws ec2 describe-vpc-endpoints --vpc-endpoint-ids vpce-1a2b3c4d \
    --query "VpcEndpoints[].PrivateDnsEnabled"
```

- Confirm that both `enableDnsSupport` and `enableDnsHostnames` are set to `true` on your VPC:

```
aws ec2 describe-vpc-attribute --vpc-id vpc-1a2b3c4d --attribute enableDnsSupport
aws ec2 describe-vpc-attribute --vpc-id vpc-1a2b3c4d --attribute enableDnsHostnames
```

**`Access denied` errors when calling Security Agent APIs**

- Check the VPC endpoint policy to ensure it allows the actions you are trying to perform.
- Verify that your IAM identity policy grants the required `securityagent:` permissions.
- If using a custom endpoint policy, confirm that both the endpoint policy and the IAM policy allow the request.
