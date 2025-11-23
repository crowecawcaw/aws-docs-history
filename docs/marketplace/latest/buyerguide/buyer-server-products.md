# AMI-based products in AWS Marketplace

###### Warning

On December 31, 2025, AWS Marketplace will stop supporting the ability to copy AMIs and CloudFormation templates to Service Catalog. You can continue to deploy AMIs and CloudFormation templates through the AWS Marketplace website or Amazon EC2 console.

An Amazon Machine Image (AMI) is an image of a server, including an operating system and
often additional software, which runs on AWS.

The software listed in AWS Marketplace is only available to run on Amazon Elastic Compute Cloud (Amazon EC2). It's not
available for download.

On AWS Marketplace, you can search for AMIs (with search suggestions), view product reviews submitted
by other customers, subscribe and launch AMIs, and manage your subscriptions. All AWS Marketplace products
have been verified for quality and pre-configured for 1-Click launch capability on Amazon Web Services
(AWS) infrastructure.

Both AMI and software as a service (SaaS) product listings are from trusted sellers. AMI
products run within a customer's AWS account. You retain more control over software
configuration and over the servers that run the software, but you also have additional
responsibilities regarding server configuration and maintenance.

The AWS Marketplace catalog contains a curated selection of open source and commercial software from
well-known sellers. Many products on AWS Marketplace can be purchased by the hour.

The AMI catalog is a community resource where people and development teams can list and
exchange software or projects under development, without having to go through extensive vetting.
Listings in the community AMI catalog may or may not be from well-known sellers and generally
have not undergone additional investigations.

An AWS Marketplace product contains one AMI for each AWS Region in which the product is available.
These AMIs are identical except for their location. Additionally, when sellers update their
product with the latest patches and updates, they may add another set of AMIs to the product.

Some AWS Marketplace products may launch multiple instances of an AMI because they're deployed as a
cluster using AWS CloudFormation templates. This cluster of instances, along with additional AWS
infrastructure services configured by the CloudFormation template, act as a single product
deployment.

## AWS CloudFormation template

AWS CloudFormation is a service that helps you model and set up your AWS resources so that you
can spend less time managing those resources and more time focusing on your applications that
run in AWS. A CloudFormation template describes the various AWS resources that you want, such
as Amazon Elastic Compute Cloud (Amazon EC2) instances or Amazon Relational Database Service (Amazon RDS) database instances. CloudFormation takes care
of provisioning and configuring those resources for you. For more information, see [Getting started with CloudFormation](../../../AWSCloudFormation/latest/UserGuide/GettingStarted.md "../../../AWSCloudFormation/latest/UserGuide/GettingStarted.md").

### Using AWS CloudFormation templates

Software sellers may offer CloudFormation templates to define a preferred deployment
topology consisting of multiple AMI instances and other AWS resources. If a CloudFormation
template is available for a product, it will be listed as a deployment option on the product
listing page.

You can use an AMI to deploy a single Amazon EC2 instance. You can use a CloudFormation template
to deploy multiple instances of an AMI that act as a cluster—along with AWS resources such
as Amazon RDS, Amazon Simple Storage Service service—as a single solution.

### Metering-enabled AMI products

Some products listed on AWS Marketplace are billed on usage measured by the software application.
Examples of metered usage dimensions include Data usage, Host/Agent usage, or Bandwidth usage.
These products require extra configuration to function correctly. An IAMrole with the
permission to meter usage must be associated with your AWS Marketplace Amazon Elastic Compute Cloud (Amazon EC2) instance at the
time of launch. For more information about IAMroles for Amazon EC2, see [IAM
Roles for Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md").

### AMI product version policies

AWS Marketplace automates the version management experience for AWS customers and sellers using
S-AMI, AMI with CloudFormation template, and container products. With automated version
archival, any product version that has been restricted by a seller for longer than two years
is automatically archived. Archived versions are no longer available to launch from AWS Marketplace
for new customers, however existing users can continue to use the archived version through
launch templates and Amazon EC2 Auto Scaling groups by specifying the AMI ID. Any archived version that has
not been used to launch a new instances in the past 13 months is deleted. Once an archived
version is deleted, it is no longer available to launch for new or existing users.
