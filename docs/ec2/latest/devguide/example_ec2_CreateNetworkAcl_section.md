# Use `CreateNetworkAcl` with a CLI

The following code examples show how to use `CreateNetworkAcl`.

CLI

**AWS CLI**

**To create a network ACL**

This example creates a network ACL for the specified VPC.

Command:

```
`aws ec2 create-network-acl --vpc-id `vpc-a01106c2``

```

Output:

```
{
    "NetworkAcl": {
        "Associations": [],
        "NetworkAclId": "acl-5fb85d36",
        "VpcId": "vpc-a01106c2",
        "Tags": [],
        "Entries": [
            {
                "CidrBlock": "0.0.0.0/0",
                "RuleNumber": 32767,
                "Protocol": "-1",
                "Egress": true,
                "RuleAction": "deny"
            },
            {
                "CidrBlock": "0.0.0.0/0",
                "RuleNumber": 32767,
                "Protocol": "-1",
                "Egress": false,
                "RuleAction": "deny"
            }
        ],
        "IsDefault": false
    }
}
```

- For API details, see
  [CreateNetworkAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a network ACL for the specified VPC.**

```
New-EC2NetworkAcl -VpcId vpc-12345678

```

**Output:**

```
Associations : {}
Entries      : {Amazon.EC2.Model.NetworkAclEntry, Amazon.EC2.Model.NetworkAclEntry}
IsDefault    : False
NetworkAclId : acl-12345678
Tags         : {}
VpcId        : vpc-12345678
```

- For API details, see
  [CreateNetworkAcl](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a network ACL for the specified VPC.**

```
New-EC2NetworkAcl -VpcId vpc-12345678

```

**Output:**

```
Associations : {}
Entries      : {Amazon.EC2.Model.NetworkAclEntry, Amazon.EC2.Model.NetworkAclEntry}
IsDefault    : False
NetworkAclId : acl-12345678
Tags         : {}
VpcId        : vpc-12345678
```

- For API details, see
  [CreateNetworkAcl](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
