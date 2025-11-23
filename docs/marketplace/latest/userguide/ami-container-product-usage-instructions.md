# Creating AMI and container product usage

instructions for AWS Marketplace

As an AWS Marketplace seller, you deliver your products to buyers in different ways. When delivering with Amazon Machine Images (AMIs) and container images, you are responsible for writing usage instructions for them. The following sections provide you with requirements and recommendations about writing usage instructions for these product types.

For more information, see [AMI-based products in AWS Marketplace](ami-products.md "ami-products.md").

###### Topics

- [Requirements](#ami-write-usage-instructions "#ami-write-usage-instructions")
- [Writing release notes](#writing-the-release-notes "#writing-the-release-notes")
- [Writing usage instructions](#writing-the-usage-instructions "#writing-the-usage-instructions")
- [Writing upgrade instructions](#writing-upgrade-instructions "#writing-upgrade-instructions")
- [Writing CloudFormation delivery instructions](#ami-cloudformation-delivery "#ami-cloudformation-delivery")

## Requirements

When creating usage instructions for your product, you must include the following
information:

- Location of all sensitive information saved by customers.
- Explain all data encryption configuration. Provide detailed instructions on how the user
  interacts with your application to decrypt necessary data if your application makes use of any
  encryption techniques.
- If your product includes cryptographic material, you must include rotation requirements in the usage instruction. Refer to [AMI-based product requirements for AWS Marketplace](product-and-ami-policies.md "product-and-ami-policies.md") for basic requirements for listings
  that use credentials and cryptographic keys.
- If any of the data stores in your product are proprietary, provide step-by-step
  instructions for configuration, backup, and recovery.
- Step-by-step instructions for how to assess and monitor the health and proper function of
  the application. For example:
  - Navigate to your [Amazon EC2 console](https://us-east-1.signin.aws.amazon.com/oauth?response_type=code&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fec2&redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fec2%2Fv2%2Fhome%3Fregion%3Dus-east-1%26state%3DhashArgs%2523Home%253A%26isauthcode%3Dtrue&forceMobileLayout=0&forceMobileApp=0&code_challenge=aRqwDZ0gdWGXfWQgSpY_ge8vSRw2poGnBZ_8qsU5fiA&code_challenge_method=SHA-256 "https://us-east-1.signin.aws.amazon.com/oauth?response_type=code&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Fec2&redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Fec2%2Fv2%2Fhome%3Fregion%3Dus-east-1%26state%3DhashArgs%2523Home%253A%26isauthcode%3Dtrue&forceMobileLayout=0&forceMobileApp=0&code_challenge=aRqwDZ0gdWGXfWQgSpY_ge8vSRw2poGnBZ_8qsU5fiA&code_challenge_method=SHA-256") and verify that you're in the correct region.
  - Choose **Instance** and select your launched instance.
  - Select the server to display your metadata page and choose the **Status
    checks** tab at the bottom of the page to review if your status checks passed or
    failed.

- Prescriptive guidance on managing AWS service quotas. For more information see the
  [AWS General
  Reference Guide](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").
- A pricing breakdown including the cost of running AWS resources added above the standard
  quota. This can be included in your product usage instructions or linked to [documentation](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") containing detailed information about managing and requesting increased
  service quotas.

## Writing release notes

Each time you update a product, you must provide a description of the changes in the
release notes. The release notes should contain specific information to help the user decide
whether to install the update. Use clear labels for the update, such as "Critical" for a
security update or "Important" or "Optional" for other types of updates.

## Writing usage instructions

Provide usage instructions that help ensure that the buyer can successfully configure and
run the software. The usage instructions you provide are shown during the configuration
process.

To write effective usage instructions, follow these guidelines:

- Assume the user is interested but uninformed.
- Provide the user with all the information needed to launch and use your product, including any configuration settings and
  special steps.

Example usage instructions:

1. Launch the product using 1-Click.
2. Use a web browser to access the application at
   `https://<EC2_Instance_Public_DNS>/index.html`.
3. Sign in using the following credentials:
   - User name: `user`
   - Password: the instance ID (`instance_id`)

## Writing upgrade instructions

Provide details on how buyer can upgrade from an earlier version of the product. Include
information on how to preserve data and settings when creating another instance. If there is no
upgrade path, edit this field to specifically mention that.

Example upgrade instructions:

1. Do \*\*\*\*, and then \*\*\*\*.
2. Check that all plugins used by your project are compatible with version \*.\*, by doing
   \*\*\*. If they aren't compatible, do \*\*\*.
3. Make a backup of your data, by doing \*\*\*.

## Writing CloudFormation delivery instructions

When using CloudFormation delivery, you must also include the following:

- A purpose for each AWS Identity and Access Management (IAM) role and IAM policy created by the CloudFormation
  template
- A purpose and location of each key created by the CloudFormation template
- Network configuration details in deployments involving more than a single element
- A detailed guide on how your applications are launched and how they're configured to
  communicate if the deployment includes multiple AWS resources
- A pricing breakdown that includes the cost of running AWS resources added above the
  standard limits. Provide prescriptive guidance on managing AWS service limits.
- All data encryption configuration. For example: Amazon S3 server-side encryption, Amazon Elastic Block Store
  (Amazon EBS) encryption, Linux Unified Key Setup (LUKS), etc.)
