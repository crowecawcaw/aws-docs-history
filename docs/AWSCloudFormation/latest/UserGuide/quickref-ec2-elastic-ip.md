# Allocate and associate Elastic IP addresses

with CloudFormation

The following template snippets are examples related to Elastic IP addresses (EIPs) in
Amazon EC2. These examples cover allocation, association, and management of EIPs for your
instances.

###### Example snippets

- [Allocate an Elastic IP address and associate it
  with an Amazon EC2 instance](#scenario-ec2-eip "#scenario-ec2-eip")
- [Associate an Elastic IP address to an
  Amazon EC2 instance by specifying the IP address](#scenario-ec2-eip-association "#scenario-ec2-eip-association")
- [Associate an Elastic IP address
  to an Amazon EC2 instance by specifying the allocation ID of the IP address](#scenario-ec2-eip-association-vpc "#scenario-ec2-eip-association-vpc")

## Allocate an Elastic IP address and associate it

with an Amazon EC2 instance

The following snippet allocates an Amazon EC2 Elastic IP (EIP) address and associates
it with an Amazon EC2 instance using an [AWS::EC2::EIP](../TemplateReference/aws-resource-ec2-eip.md "../TemplateReference/aws-resource-ec2-eip.md") resource. You
can allocate an EIP address from an address pool owned by AWS or from an address
pool created from a public IPv4 address range you bring to AWS for use with your
AWS resources using [bring your own IP addresses
(BYOIP)](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md"). In this example, the EIP is allocated from an address pool
owned by AWS.

For more information about Elastic IP addresses, see [Elastic IP
address](../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md "../../../AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.md") in the _Amazon EC2 User Guide_.

### JSON

```
"ElasticIP": {
    "Type": "AWS::EC2::EIP",
    "Properties": {
        "InstanceId": {
            "Ref": "Ec2Instance"
        }
    }
}
```

### YAML

```
ElasticIP:
  Type: AWS::EC2::EIP
  Properties:
    InstanceId: !Ref EC2Instance
```

## Associate an Elastic IP address to an

Amazon EC2 instance by specifying the IP address

The following snippet associates an existing Amazon EC2 Elastic IP address to an EC2
instance using an [AWS::EC2::EIPAssociation](../TemplateReference/aws-resource-ec2-eipassociation.md "../TemplateReference/aws-resource-ec2-eipassociation.md") resource. You must first allocate an Elastic
IP address for use in your account. An Elastic IP address can be associated with a
single instance.

### JSON

```
"IPAssoc": {
  "Type": "AWS::EC2::EIPAssociation",
  "Properties": {
    "InstanceId": {
      "Ref": "Ec2Instance"
    },
    "EIP": "`192.0.2.0`"
  }
}
```

### YAML

```
IPAssoc:
  Type: AWS::EC2::EIPAssociation
  Properties:
    InstanceId: !Ref EC2Instance
    EIP: `192.0.2.0`
```

## Associate an Elastic IP address

to an Amazon EC2 instance by specifying the allocation ID of the IP address

The following snippet associates an existing Elastic IP address to an Amazon EC2
instance by specifying the allocation ID using an [AWS::EC2::EIPAssociation](../TemplateReference/aws-resource-ec2-eipassociation.md "../TemplateReference/aws-resource-ec2-eipassociation.md") resource. An allocation ID is assigned to an
Elastic IP address upon Elastic IP address allocation.

### JSON

```
"IPAssoc": {
    "Type": "AWS::EC2::EIPAssociation",
    "Properties": {
        "InstanceId": {
            "Ref": "Ec2Instance"
        },
        "AllocationId": "eipalloc-`1234567890abcdef0`"
    }
}
```

### YAML

```
IPAssoc:
  Type: AWS::EC2::EIPAssociation
  Properties:
    InstanceId: !Ref EC2Instance
    AllocationId: eipalloc-`1234567890abcdef0`
```
