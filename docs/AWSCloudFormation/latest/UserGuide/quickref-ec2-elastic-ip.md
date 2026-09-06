

# Allocate and associate Elastic IP addresses with CloudFormation
<a name="quickref-ec2-elastic-ip"></a>

The following template snippets are examples related to Elastic IP addresses (EIPs) in Amazon EC2. These examples cover allocation, association, and management of EIPs for your instances.

**Topics**
+ [Allocate an Elastic IP address and associate it with an Amazon EC2 instance](#scenario-ec2-eip)
+ [Associate an Elastic IP address to an Amazon EC2 instance by specifying the IP address](#scenario-ec2-eip-association)
+ [Associate an Elastic IP address to an Amazon EC2 instance by specifying the allocation ID of the IP address](#scenario-ec2-eip-association-vpc)

## Allocate an Elastic IP address and associate it with an Amazon EC2 instance
<a name="scenario-ec2-eip"></a>

The following snippet allocates an Amazon EC2 Elastic IP (EIP) address and associates it with an Amazon EC2 instance using an [AWS::EC2::EIP ](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eip.html) resource. You can allocate an EIP address from an address pool owned by AWS or from an address pool created from a public IPv4 address range you bring to AWS for use with your AWS resources using [bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html). In this example, the EIP is allocated from an address pool owned by AWS.

For more information about Elastic IP addresses, see [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide*.

### JSON
<a name="quickref-ec2-example-3.json"></a>

```
1. "ElasticIP": {
2.     "Type": "AWS::EC2::EIP",
3.     "Properties": {
4.         "InstanceId": {
5.             "Ref": "Ec2Instance"
6.         }
7.     }
8. }
```

### YAML
<a name="quickref-ec2-example-3.yaml"></a>

```
1. ElasticIP:
2.   Type: AWS::EC2::EIP
3.   Properties:
4.     InstanceId: !Ref EC2Instance
```

## Associate an Elastic IP address to an Amazon EC2 instance by specifying the IP address
<a name="scenario-ec2-eip-association"></a>

The following snippet associates an existing Amazon EC2 Elastic IP address to an EC2 instance using an [AWS::EC2::EIPAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eipassociation.html) resource. You must first allocate an Elastic IP address for use in your account. An Elastic IP address can be associated with a single instance.

### JSON
<a name="quickref-ec2-example-4.json"></a>

```
1. "IPAssoc": {
2.   "Type": "AWS::EC2::EIPAssociation",
3.   "Properties": {
4.     "InstanceId": {
5.       "Ref": "Ec2Instance"
6.     },
7.     "EIP": "{{192.0.2.0}}"
8.   }
9. }
```

### YAML
<a name="quickref-ec2-example-4.yaml"></a>

```
1. IPAssoc:
2.   Type: AWS::EC2::EIPAssociation
3.   Properties:
4.     InstanceId: !Ref EC2Instance
5.     EIP: {{192.0.2.0}}
```

## Associate an Elastic IP address to an Amazon EC2 instance by specifying the allocation ID of the IP address
<a name="scenario-ec2-eip-association-vpc"></a>

The following snippet associates an existing Elastic IP address to an Amazon EC2 instance by specifying the allocation ID using an [AWS::EC2::EIPAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eipassociation.html) resource. An allocation ID is assigned to an Elastic IP address upon Elastic IP address allocation. 

### JSON
<a name="quickref-ec2-example-5.json"></a>

```
1. "IPAssoc": {
2.     "Type": "AWS::EC2::EIPAssociation",
3.     "Properties": {
4.         "InstanceId": {
5.             "Ref": "Ec2Instance"
6.         },
7.         "AllocationId": "eipalloc-{{1234567890abcdef0}}"
8.     }
9. }
```

### YAML
<a name="quickref-ec2-example-5.yaml"></a>

```
1. IPAssoc:
2.   Type: AWS::EC2::EIPAssociation
3.   Properties:
4.     InstanceId: !Ref EC2Instance
5.     AllocationId: eipalloc-{{1234567890abcdef0}}
```