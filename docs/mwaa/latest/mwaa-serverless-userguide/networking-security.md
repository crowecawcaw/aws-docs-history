

# Security in your VPC on Amazon MWAA Serverless
<a name="networking-security"></a>

Learn about the Amazon VPC components used to secure your Amazon MWAA Serverless workflow and the configurations needed for these components.

**Contents**
+ [Security overview](#networking-security-about)
+ [Network access control lists (ACLs)](#networking-security-acl)
  + [(Recommended) Example ACLs](#networking-security-acl-example)
+ [VPC security groups](#networking-security-sg)
  + [(Recommended) Example all access self-referencing security group](#networking-security-sg-example)
  + [(Optional) Example security group that restricts inbound access to port 443](#networking-security-sg-port443)
+ [VPC endpoint policies (private routing only)](#networking-security-policies)
  + [(Recommended) Example VPC endpoint policy to allow all access](#networking-security-policies-all)
  + [(Recommended) Example Amazon S3 gateway endpoint policy to allow bucket access](#networking-security-external-policies-s3)

## Security overview
<a name="networking-security-about"></a>

Security groups and access control lists (ACLs) provide ways to control the network traffic across the subnets and instances in your Amazon VPC using rules that you specify.
+ Network traffic to and from a subnet can be controlled by ACLs. You only need one ACL, and the same ACL can be used on multiple workflows.
+ Network traffic to and from an instance can be controlled by an Amazon VPC security group. You can use between one and five security groups per workflow.
+ Network traffic to and from an instance can also be controlled by VPC endpoint policies. If internet access within your Amazon VPC is not allowed by your organization and you're using an Amazon VPC network with *private routing*, a VPC endpoint is required. You can optionally attach a policy to the endpoint to further restrict access to specific resources that are relevant to the service for which the endpoint was created. For example, if you have a AWS KMS VPC endpoint, you can write a policy that restricts actions to certain AWS KMS keys.

## Network access control lists (ACLs)
<a name="networking-security-acl"></a>

A [network access control list (ACL)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) can manage (by allow or deny rules) inbound and outbound traffic at the *subnet* level. An ACL is stateless, which means that inbound and outbound rules must be specified separately and explicitly. It is used to specify the types of network traffic that are allowed in or out from the instances in a VPC network.

Every Amazon VPC has a default ACL that allows all inbound and outbound traffic. You can edit the default ACL rules, or create a custom ACL and attach it to your subnets. A subnet can only have one ACL attached to it at any time, but one ACL can be attached to multiple subnets.

### (Recommended) Example ACLs
<a name="networking-security-acl-example"></a>

The following example shows the *inbound* and *outbound* ACL rules that can be used for an Amazon VPC with *public routing* (Amazon VPC network has access to the internet) or *private routing* (Amazon VPC network doees not have access to the internet). 


| Rule number | Type | Protocol | Port range | Source | Allow or deny | 
| --- | --- | --- | --- | --- | --- | 
| 100 | All IPv4 traffic | All | All | 0.0.0.0/0 | Allow | 
| \* | All IPv4 traffic | All | All | 0.0.0.0/0 | Deny | 

## VPC security groups
<a name="networking-security-sg"></a>

A [VPC security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) acts as a virtual firewall that controls the network traffic at the *instance* level. A security group is stateful, which means that when an inbound connection is permitted, it is allowed to reply. It is used to specify the types of network traffic that are allowed in from the instances in a VPC network.

Every Amazon VPC has a default security group. By default, it has no inbound rules. It has an outbound rule that allows all outbound traffic. You can edit the default security group rules, or create a custom security group and attach it to your Amazon VPC. On Amazon MWAA, you need to configure inbound and outbound rules to direct traffic on your NAT gateways.

### (Recommended) Example all access self-referencing security group
<a name="networking-security-sg-example"></a>

The following example shows the *inbound* security group rules that allows all traffic for an Amazon VPC with *public routing* or *private routing*. The security group in this example is a self-referencing rule to itself.


| Type | Protocol | Source Type | Source | 
| --- | --- | --- | --- | 
| All traffic | All | All | sg-0909e8e81919 / my-mwaa-serverless-vpc-security-group | 

The following example shows the *outbound* security group rules.


| Type | Protocol | Source Type | Source | 
| --- | --- | --- | --- | 
| All traffic | All | All | 0.0.0.0/0 | 

 test

### (Optional) Example security group that restricts inbound access to port 443
<a name="networking-security-sg-port443"></a>

The following example shows the *inbound* security group rules that allow all TCP traffic on port 443 for the Apache Airflow *Web server*.


| Type | Protocol | Port range | Source type | Source | 
| --- | --- | --- | --- | --- | 
| HTTPS | TCP | 443 | Custom | sg-0909e8e81919 / my-mwaa-serverless-vpc-security-group | 

## VPC endpoint policies (private routing only)
<a name="networking-security-policies"></a>

A VPC endpoint (AWS PrivateLink) policy controls access to AWS services from your private subnet. A VPC endpoint policy is an IAM resource policy that you attach to your VPC gateway or interface endpoint. This section describes the permissions needed for the VPC endpoint policies for each VPC endpoint.

We recommend using a VPC interface endpoint policy for each of the VPC endpoints you created that allows full access to all AWS services, and using your execution role exclusively for AWS permissions.

### (Recommended) Example VPC endpoint policy to allow all access
<a name="networking-security-policies-all"></a>

The following example shows a VPC interface endpoint policy for an Amazon VPC with *private routing*.

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
<a name="networking-security-external-policies-s3"></a>

The following example shows a VPC gateway endpoint policy that provides access to the Amazon S3 buckets required for Amazon ECR operations for an Amazon VPC with *private routing*. This is required for your Amazon ECR image to be retrieved, in addition to the bucket where your DAGs and supporting files are stored.

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
      "Resource": ["arn:aws:s3:::prod-{{us-east-1}}-starport-layer-bucket/*"]
    }
  ]
}
```