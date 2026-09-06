

# Deploy Environments with CloudFormation
<a name="cloudformation"></a>

CloudFormation enables you to create and provision AWS infrastructure deployments predictably and repeatedly. It helps you leverage AWS products to build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure. CloudFormation enables you to use a template file to create and delete a collection of resources together as a single unit (a stack). For more information, see *[AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/)*.

AWS Control Tower uses CloudFormation StackSets to deploy and manage baseline resources, such as IAM roles and AWS Config recorders, in your accounts. For more information about how CloudFormation and AWS Control Tower work together, see [Create AWS Control Tower resources with AWS CloudFormation](creating-resources-with-cloudformation.md).