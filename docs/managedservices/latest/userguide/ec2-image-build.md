# Use AMS SSP to provision EC2 Image Builder in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access EC2 Image Builder capabilities directly in your AMS managed account. EC2 Image Builder is a fully managed AWS service that makes it easier to automate the creation, management, and deployment of customized,
secure, and up-to-date "golden" server images that are pre-installed and pre-configured with software and settings to meet specific IT standards.

You can use the AWS Management Console, AWS CLI, or APIs to create custom images in your AWS account. When you use the AWS Management Console, the Amazon EC2
Image Builder wizard guides you through steps to:

- Provide starting artifacts
- Add and remove software
- Customize settings and scripts
- Run selected tests
- Distribute images to AWS Regions
  The images you build are created in your account and can be configured for operating system patches on an
  ongoing basis.
  To learn more, see [EC2 Image Builder](https://aws.amazon.com/image-builder/ "https://aws.amazon.com/image-builder/").

## EC2 Image Builder in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to EC2 Image Builder in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
Through this RFC, the following IAM role will be provisioned in your account:
`customer_ec2_imagebuilder_role`. Once provisioned in your account, you must onboard
the role in your federation solution.

**Q: What are the restrictions for EC2 Image Builder?**

AMS does not support the use of Service Defaults for infrastructure configuration. You can create a new
infrastructure configuration or use an existing one.

AMS does not currently support the creation of container recipes.

**Q: What are the prerequisites or dependencies to enable EC2 Image Builder?**

- EC2 Image Builder service-linked role: You don't need to manually create a service-linked role. When
  you create your first Image Builder resource in the AWS Management Console, the AWS CLI, or the AWS API, Image Builder creates the
  service-linked role for you.
- Instances used to build images and run tests using Image Builder must have access to the Systems Manager service.

The SSM Agent will be installed on the
source image if it is not already present, and it will be removed before the image is created.

- AWS IAM: The IAM role that you associate with your instance profile must have
  permissions to run the build and test components included in your image. The following IAM role policies
  must be attached to the IAM role that is associated with the instance profiles:
  `EC2InstanceProfileForImageBuilder` and
  `AmazonSSMManagedInstanceCore`. The IAM role name should contain the
  `*imagebuilder*` keyword.
- If you configure logging, the instance profile specified in your infrastructure configuration
  must have `s3:PutObject` permissions for the target bucket
  (`arn:aws:s3:::`{bucket-name}`/*`). For example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`{bucket-name}`/*"
 }
 ]
}`

```

- Create an SNS topic with name 'imagebuilder' to receive any alerts and notification from EC2 Image Builder.
