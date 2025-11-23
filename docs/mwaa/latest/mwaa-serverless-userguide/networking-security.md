# Security in your VPC on Amazon MWAA Serverless

Learn about the Amazon VPC components used to secure your Amazon MWAA Serverless workflow and the configurations needed for these components.

###### Contents

- [Security overview](networking-security.md#networking-security-about "networking-security.md#networking-security-about")
- [Network access control lists (ACLs)](networking-security.md#networking-security-acl "networking-security.md#networking-security-acl")
  - [(Recommended) Example ACLs](networking-security.md#networking-security-acl-example "networking-security.md#networking-security-acl-example")

- [VPC security groups](networking-security.md#networking-security-sg "networking-security.md#networking-security-sg")
  - [(Recommended) Example all access self-referencing security group](networking-security.md#networking-security-sg-example "networking-security.md#networking-security-sg-example")
  - [(Optional) Example security group that restricts inbound access to port 443](networking-security.md#networking-security-sg-port443 "networking-security.md#networking-security-sg-port443")

- [VPC endpoint policies (private routing only)](networking-security.md#networking-security-policies "networking-security.md#networking-security-policies")
  - [(Recommended) Example VPC endpoint policy to allow all access](networking-security.md#networking-security-policies-all "networking-security.md#networking-security-policies-all")
  - [(Recommended) Example Amazon S3 gateway endpoint policy to allow bucket access](networking-security.md#networking-security-external-policies-s3 "networking-security.md#networking-security-external-policies-s3")

## Security overview

Security groups and access control lists (ACLs) provide ways to control the network traffic across the subnets and instances in your Amazon VPC using rules that you specify.

- Network traffic to and from a subnet can be controlled by ACLs. You only need one ACL, and the same ACL can be used on multiple workflows.
- Network traffic to and from an instance can be controlled by an Amazon VPC security group. You can use between one and five security groups per workflow.
- Network traffic to and from an instance can also be controlled by VPC endpoint policies. If internet access within your Amazon VPC is not allowed by your organization and you're using an Amazon VPC network with _private routing_, a VPC endpoint is required. You can optionally attach a policy to the endpoint to further restrict access to specific resources that are relevant to the service for which the endpoint was created. For example, if you have a AWS KMS VPC endpoint, you can write a policy that restricts actions to certain AWS KMS keys.

## Network access control lists (ACLs)

A [network access control list (ACL)](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") can manage (by allow or deny rules) inbound and outbound traffic at the _subnet_ level. An ACL is stateless, which means that inbound and outbound rules must be specified separately and explicitly. It is used to specify the types of network traffic that are allowed in or out from the instances in a VPC network.

Every Amazon VPC has a default ACL that allows all inbound and outbound traffic. You can edit the default ACL rules, or create a custom ACL and attach it to your subnets. A subnet can only have one ACL attached to it at any time, but one ACL can be attached to multiple subnets.

### (Recommended) Example ACLs

The following example shows the _inbound_ and _outbound_ ACL rules that can be used for an Amazon VPC with _public routing_ (Amazon VPC network has access to the internet) or _private routing_ (Amazon VPC network doees not have access to the internet).

| Rule number | Type             | Protocol | Port range | Source    | Allow or deny |
| ----------- | ---------------- | -------- | ---------- | --------- | ------------- |
| 100         | All IPv4 traffic | All      | All        | 0.0.0.0/0 | Allow         |
| \*          | All IPv4 traffic | All      | All        | 0.0.0.0/0 | Deny          |

## VPC security groups

A [VPC security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") acts as a virtual firewall that controls the network traffic at the _instance_ level. A security group is stateful, which means that when an inbound connection is permitted, it is allowed to reply. It is used to specify the types of network traffic that are allowed in from the instances in a VPC network.

Every Amazon VPC has a default security group. By default, it has no inbound rules. It has an outbound rule that allows all outbound traffic. You can edit the default security group rules, or create a custom security group and attach it to your Amazon VPC. On Amazon MWAA, you need to configure inbound and outbound rules to direct traffic on your NAT gateways.

### (Recommended) Example all access self-referencing security group

The following example shows the _inbound_ security group rules that
allows all traffic for an Amazon VPC with _public routing_ or
_private routing_. The security group in this example is a
self-referencing rule to itself.

| Type        | Protocol | Source Type | Source                                                  |
| ----------- | -------- | ----------- | ------------------------------------------------------- |
| All traffic | All      | All         | sg-0909e8e81919 / my-mwaa-serverless-vpc-security-group |

The following example shows the _outbound_ security group rules.

| Type        | Protocol | Source Type | Source    |
| ----------- | -------- | ----------- | --------- |
| All traffic | All      | All         | 0.0.0.0/0 |

test

### (Optional) Example security group that restricts inbound access to port 443

The following example shows the _inbound_ security group rules that allow all TCP traffic on port 443 for the Apache Airflow _Web server_.

| Type  | Protocol | Port range | Source type | Source                                                  |
| ----- | -------- | ---------- | ----------- | ------------------------------------------------------- |
| HTTPS | TCP      | 443        | Custom      | sg-0909e8e81919 / my-mwaa-serverless-vpc-security-group |

## VPC endpoint policies (private routing only)

A VPC endpoint (AWS PrivateLink) policy controls access to AWS services from your private subnet. A VPC endpoint policy is an IAM resource policy that you attach to your VPC gateway or interface endpoint. This section describes the permissions needed for the VPC endpoint policies for each VPC endpoint.

We recommend using a VPC interface endpoint policy for each of the VPC endpoints you created that allows full access to all AWS services, and using your execution role exclusively for AWS permissions.

### (Recommended) Example VPC endpoint policy to allow all access

The following example shows a VPC interface endpoint policy for an Amazon VPC with _private routing_.

```
{
  "Statement": [
    {
      "Action": "*",
      "Effect": "Allow",
      "Resource": "*",
      "Principal": "*"
    }
  ]
}
```

### (Recommended) Example Amazon S3 gateway endpoint policy to allow bucket access

The following example shows a VPC gateway endpoint policy that provides access to the Amazon S3 buckets required for Amazon ECR operations for an Amazon VPC with _private routing_. This is required for your Amazon ECR image to be retrieved, in addition to the bucket where your DAGs and supporting files are stored.

```
{
  "Statement": [
    {
      "Sid": "Access-to-specific-bucket-only",
      "Principal": "*",
      "Action": [
        "s3:GetObject"
      ],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::prod-`us-east-1`-starport-layer-bucket/*"]
    }
  ]
}
```
