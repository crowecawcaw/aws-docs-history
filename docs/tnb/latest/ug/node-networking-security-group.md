

# AWS.Networking.SecurityGroup
<a name="node-networking-security-group"></a>

AWS TNB supports security groups to automate the provisioning of [Amazon EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html) which you can attach to Amazon EKS Kubernetes cluster node groups.

## Syntax
<a name="node-networking-security-group-syntax"></a>

```
tosca.nodes.AWS.Networking.SecurityGroup
  properties:
    description: String
    name: String
    tags: List
  requirements:
    vpc: String
```

## Properties
<a name="node-networking-security-group-properties"></a>

 `description`    
The description of the security group. You can use up to 255 characters to describe the group. You can include only letters (A-Z and a-z), numbers (0-9), spaces, and the following special characters: .\_-:/()\#,@[]\+=&;{}\!$\*  
Required: Yes  
Type: String

 `name`    
A name for the security group. You can use up to 255 characters for the name. You can include only letters (A-Z and a-z), numbers (0-9), spaces, and the following special characters: .\_-:/()\#,@[]\+=&;{}\!$\*  
Required: Yes  
Type: String

 `tags`    
The tags that you can attach to the security group resource.  
Required: No  
Type: List

## Requirements
<a name="node-networking-security-group-requirements"></a>

 `vpc`    
An [AWS.Networking.VPC](node-vpc.md) node.  
Required: Yes  
Type: String

## Example
<a name="node-networking-security-group-example"></a>

```
SampleSecurityGroup001:
  type: tosca.nodes.AWS.Networking.SecurityGroup
  properties:
        description: {{"Sample Security Group for Testing"}}
        name: {{"SampleSecurityGroup"}}
        tags:
          - {{"Name=SecurityGroup"}}
          - {{"Environment=Testing"}}
      requirements:
        vpc: {{SampleVPC}}
```