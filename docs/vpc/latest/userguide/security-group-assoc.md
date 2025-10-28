# Associate security groups with multiple VPCs

If you have workloads running in multiple VPCs that share network security requirements, you
can use the Security Group VPC Associations feature to associate a security group with
multiple VPCs in the same Region. This enables you to manage and maintain security
groups in one place for multiple VPCs in your account.

![A diagram of security group associated with two VPCs.](images/sec-group-vpc-assoc.png)
The diagram above shows AWS account A with two VPCs in it. Each of the VPCs has workloads
running in a private subnet. In this case, workloads in VPC A and B subnets share the
same network traffic requirements, so Account A can use the Security Group VPC
associations feature to associate the security group in VPC A with VPC B. Any updates
made to the associated security group are automatically applied to the traffic to
workloads in the VPC B subnet.

###### Requirements of the Security Group VPC Associations feature

- You must own the VPC or have one of the VPC subnets shared with
  you to associate a security group with the VPC.
- The VPC and security group must be in the same AWS Region.
- You cannot associate a default security group with another VPC or associate a
  security group with a default VPC.
- Both the security group owner and the VPC owner can view the security group VPC
  associations.
  **Services that support this feature**

- Amazon API Gateway (REST APIs only)
- AWS Auto Scaling
- AWS CloudFormation
- Amazon EC2
- Amazon EFS
- Amazon EKS
- Amazon FSx
- AWS PrivateLink
- Amazon Route 53
- Elastic Load Balancing
  - Application Load Balancer
  - Network Load Balancer

## Associate a security group with another VPC

This section explains how to use the AWS Management Console and the AWS CLI to associate a security group with VPCs.

AWS Management Console

###### To associate a security group with another VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the left navigation pane, choose **Security groups**.
3. Choose a security group to view the details.
4. Choose the **VPC associations** tab.
5. Choose **Associate VPC**.
6. Under **VPC ID**, choose a VPC to associate with the security group.
7. Choose **Associate VPC**.

Command line

###### To associate a security group with another VPC

1. Create a VPC association with [associate-security-group-vpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-security-group-vpc.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-security-group-vpc.html").
2. Check the status of a VPC association with [describe-security-group-vpc-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-group-vpc-associations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-group-vpc-associations.html") and wait for the status to be `associated`.

The VPC is now associated with the security group.

Once you’ve associated the VPC with the security group, you can, for example, [launch an instance
into the VPC and choose this new security group](../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md "../../../AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.md") or [reference this security group in an
existing security group rule](security-group-rules.md#security-group-referencing "security-group-rules.md#security-group-referencing").

## Disassociate a security group from another VPC

This section explains how to use the AWS Management Console and the AWS CLI to disassociate a security group from VPCs. You may want to do this if your goal is to delete the security group. Security groups cannot be deleted if they are associated. You can only diassociate a security group if there are no network interfaces in the associated VPC using that security group.

AWS Management Console

###### To disassociate a security group from a VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the left navigation pane, choose **Security groups**.
3. Choose a security group to view the details.
4. Choose the **VPC associations** tab.
5. Choose **Disassociate VPC**.
6. Under **VPC ID**, choose a VPC to disassociate from the security group.
7. Choose **Disassociate VPC**.
8. View the **Status** of the disassociation in the VPC associations tab and wait for the status to be `disassociated`.

Command line

###### To disassociate a security group from a VPC

1. Disassociate a VPC association with [disassociate-security-group-vpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-security-group-vpc.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-security-group-vpc.html").
2. Check the status of a VPC disassociation with [describe-security-group-vpc-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-group-vpc-associations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-group-vpc-associations.html") and wait for the status to be `disassociated`.

The VPC is now disassociated with the security group.
