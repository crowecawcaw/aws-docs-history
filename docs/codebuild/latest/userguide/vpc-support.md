

# Use AWS CodeBuild with Amazon Virtual Private Cloud
<a name="vpc-support"></a>

Typically, AWS CodeBuild cannot access resources in a VPC. To enable access, you must provide additional VPC-specific configuration information in your CodeBuild project configuration. This includes the VPC ID, the VPC subnet IDs, and the VPC security group IDs. VPC-enabled builds can then access resources inside your VPC. For more information about setting up a VPC in Amazon VPC, see the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Introduction.html).

**Topics**
+ [Use cases](#use-cases)
+ [Best practices for VPCs](#best-practices-for-vpcs)
+ [Limitations of VPCs](#vpc-limitations)
+ [Allow Amazon VPC access in your CodeBuild projects](enabling-vpc-access-in-projects.md)
+ [Troubleshoot your VPC setup](troubleshooting-vpc.md)
+ [Use VPC endpoints](use-vpc-endpoints-with-codebuild.md)
+ [Use AWS CodeBuild with a managed proxy server](run-codebuild-in-managed-proxy-server.md)
+ [Use AWS CodeBuild with a proxy server](use-proxy-server.md)
+ [CloudFormation VPC template](cloudformation-vpc-template.md)

## Use cases
<a name="use-cases"></a>

VPC connectivity from AWS CodeBuild builds makes it possible to:
+ Run integration tests from your build against data in an Amazon RDS database that's isolated on a private subnet.
+ Query data in an Amazon ElastiCache cluster directly from tests.
+ Interact with internal web services hosted on Amazon EC2, Amazon ECS, or services that use internal Elastic Load Balancing.
+ Retrieve dependencies from self-hosted, internal artifact repositories, such as PyPI for Python, Maven for Java, and npm for Node.js.
+ Access objects in an S3 bucket configured to allow access through an Amazon VPC endpoint only.
+ Query external web services that require fixed IP addresses through the Elastic IP address of the NAT gateway or NAT instance associated with your subnet.

Your builds can access any resource that's hosted in your VPC.

## Best practices for VPCs
<a name="best-practices-for-vpcs"></a>

Use this checklist when you set up a VPC to work with CodeBuild.
+ Set up your VPC with public and private subnets, and a NAT gateway. The NAT gateway must reside in a public subnet. For more information, see [VPC with public and private subnets (NAT)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html) in the *Amazon VPC User Guide*.
**Important**  
You need a NAT gateway or NAT instance to use CodeBuild with your VPC so that CodeBuild can reach public endpoints (for example, to run CLI commands when running builds). You cannot use the internet gateway instead of a NAT gateway or a NAT instance because CodeBuild does not support assigning Elastic IP addresses to the network interfaces that it creates, and auto-assigning a public IP address is not supported by Amazon EC2 for any network interfaces created outside of Amazon EC2 instance launches. 
+ Include multiple Availability Zones with your VPC.
+ Make sure that your security groups have no inbound (ingress) traffic allowed to your builds. CodeBuild does not have specific requirements for outbound traffic, but you must allow access to any Internet resources required for your build, such as GitHub or Amazon S3.

  For more information, see [Security groups rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules) in the *Amazon VPC User Guide*. 
+ Set up separate subnets for your builds.
+ When you set up your CodeBuild projects to access your VPC, choose private subnets only. 

For more information about setting up a VPC in Amazon VPC, see the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Introduction.html).

For more information about using CloudFormation to configure a VPC to use the CodeBuild VPC feature, see the [CloudFormation VPC template](cloudformation-vpc-template.md).

## Limitations of VPCs
<a name="vpc-limitations"></a>
+ VPC connectivity from CodeBuild is not supported for shared VPCs.