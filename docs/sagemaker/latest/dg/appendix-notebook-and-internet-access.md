# Connect a Notebook Instance in a

VPC to External Resources

The following topic gives information on how to connect your notebook instance in a
VPC to external resources.

## Default

communication with the internet

When your notebook allows _direct internet access_, SageMaker AI
provides a network interface that allows the notebook to communicate with the
internet through a VPC managed by SageMaker AI. Traffic within your VPC's CIDR goes through
elastic network interface created in your VPC. All the other traffic goes through
the network interface created by SageMaker AI, which is essentially through the public
internet. Traffic to gateway VPC endpoints like Amazon S3 and DynamoDB goes through the
public internet, while traffic to interface VPC interface endpoints still goes
through your VPC. If you want to use gateway VPC endpoints, you might want to
disable direct internet access.

## VPC-only

communication with the internet

To disable direct internet access, you can specify a VPC for your notebook
instance. By doing so, you prevent SageMaker AI from providing internet access to your
notebook instance. As a result, the notebook instance can't train or host models
unless your VPC has an interface endpoint (AWS PrivateLink) or a NAT gateway and your
security groups allow outbound connections.

For information about creating a VPC interface endpoint to use AWS PrivateLink for
your notebook instance, see [Connect to a Notebook Instance Through a
VPC Interface Endpoint](notebook-interface-endpoint.md "notebook-interface-endpoint.md"). For information about setting up
a NAT gateway for your VPC, see [VPC with
Public and Private Subnets (NAT)](../../../vpc/latest/userguide/vpc-example-private-subnets-nat.md "../../../vpc/latest/userguide/vpc-example-private-subnets-nat.md") in the _Amazon Virtual Private
Cloud User Guide_. For information about security groups, see [Security Groups for Your VPC](../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md "../../../AmazonVPC/latest/UserGuide/VPC_SecurityGroups.md"). For more information about networking
configurations in each networking mode and configuring network on premise, see
[Understanding Amazon SageMaker notebook instance networking configurations and advanced
routing options](https://aws.amazon.com/blogs/machine-learning/understanding-amazon-sagemaker-notebook-instance-networking-configurations-and-advanced-routing-options/ "https://aws.amazon.com/blogs/machine-learning/understanding-amazon-sagemaker-notebook-instance-networking-configurations-and-advanced-routing-options/").

###### Warning

When you use a VPC for your notebook instance, you partly own the networking
configuration for the instance. As a security best practice, we recommend that
you apply least-privilege permissions to the inbound and outbound access that
you permit with your security group rules. If you apply overly permissive
inbound rule configurations, then users who have access to your VPC could access
your Jupyter Notebooks without authenticating.

## Security and Shared Notebook

Instances

A SageMaker notebook instance is designed to work best for an individual user. It is
designed to give data scientists and other users the most power for managing their
development environment.

A notebook instance user has root access for installing packages and other
pertinent software. We recommend that you exercise judgement when granting
individuals access to notebook instances that are attached to a VPC that contains
sensitive information. For example, you might grant a user access to a notebook
instance with an IAM policy by giving them the ability to create a presigned
notebook URL, as shown in the following example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sagemaker:CreatePresignedNotebookInstanceUrl",
 "Resource": "arn:aws:sagemaker:`us-east-1`:`111122223333`:notebook-instance/myNotebookInstance"
 }
 ]
}`

```
