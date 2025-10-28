# Configure Amazon EC2 instance types for use with Amazon EMR

EC2 instances come in different configurations known as _instance
types_. Instance types have different CPU, input/output, and storage
capacities. In addition to the instance type, you can choose different purchasing
options for Amazon EC2 instances. You can specify different instance types and purchasing
options within uniform instance groups or instance fleets. For more information, see
[Create an Amazon EMR cluster with instance
fleets or uniform instance groups](emr-instance-group-configuration.md "emr-instance-group-configuration.md"). For guidance about choosing
instance types and purchasing options for your application, see [Configuring Amazon EMR cluster instance types and best practices for Spot instances](emr-plan-instances-guidelines.md "emr-plan-instances-guidelines.md").

###### Important

When you choose an instance type using the AWS Management Console, the number of **vCPU** shown for each **Instance type** is the number of YARN vcores for that instance type, not the number of EC2 vCPUs for that instance type. For more information on the number of vCPUs for each instance type, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/").

###### Topics

- [Supported instance types with Amazon EMR](emr-supported-instance-types.md "emr-supported-instance-types.md")
- [Configure networking in a VPC for Amazon EMR](emr-plan-vpc-subnet.md "emr-plan-vpc-subnet.md")
- [Create an Amazon EMR cluster with instance
  fleets or uniform instance groups](emr-instance-group-configuration.md "emr-instance-group-configuration.md")
