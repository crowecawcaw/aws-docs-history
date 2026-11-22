

# Create Networking Flexible Cost Allocation resources with AWS CloudFormation

Networking Flexible Cost Allocation (FCA) is integrated with AWS CloudFormation (CloudFormation), a service that helps you model and set up your AWS resources so that you can spend less time creating and managing your resources and infrastructure. You create a template that describes the FCA policies and associations that you want, and CloudFormation provisions and configures those resources for you.

## FCA and CloudFormation templates
<a name="networking-flex-cost-allocation-cfn-templates"></a>

FCA provides the following CloudFormation resource types:
+ `AWS::EC2::FcaPolicy` – Creates a Networking Flexible Cost Allocation policy.
+ `AWS::EC2::FcaPolicyAssociation` – Associates a policy with a resource, or with an account, VPC, or subnet scope.

For the properties, return values, and syntax of each resource type, see [Amazon EC2 resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_EC2.html) in the *AWS CloudFormation User Guide*.

To create an association, the IAM principal that deploys the stack also needs permission to describe the associated resource, for example `ec2:DescribeNatGateways` for a NAT gateway.

For complete examples that create policies with CloudFormation alongside the console and the AWS CLI, see the following use-case topics:
+ [Allocate EC2 instance data transfer](networking-flex-cost-allocation-ec2.md)
+ [Allocate NAT gateway costs](networking-flex-cost-allocation-natgw.md)
+ [Allocate VPC peering data transfer](networking-flex-cost-allocation-pcx.md)

## Learn more about CloudFormation
<a name="networking-flex-cost-allocation-cfn-learn-more"></a>

To learn more about CloudFormation, see the following resources:
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [AWS CloudFormation command line interface User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)