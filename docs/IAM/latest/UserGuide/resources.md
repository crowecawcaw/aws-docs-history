# Resources to learn more about IAM

IAM is a rich product, and you'll find many resources to help you learn more about how
IAM can help you secure your AWS account and resources.

###### Topics

- [Identities](#resources-users-and-groups "#resources-users-and-groups")
- [Credentials (passwords, access keys, and MFA
  devices)](#resources-credentials "#resources-credentials")
- [Permissions and policies](#resources-permissions-and-policies "#resources-permissions-and-policies")
- [Federation and delegation](#resources-federation-and-delegation "#resources-federation-and-delegation")
- [IAM and other AWS products](#resources-iam-and-other-services "#resources-iam-and-other-services")
- [General security practices](#resources-general-security "#resources-general-security")
- [General resources](#resources-general "#resources-general")

## Identities

Consult these resources for creating, managing, and using identities.

- [Manage identities
  in IAM Identity Center](../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md "../../../singlesignon/latest/userguide/manage-your-identity-source-sso.md") – Procedural information about creating users and group in
  IAM Identity Center.
- **[IAM Identities](id.md "id.md")** – An in-depth discussion of users, groups, and roles.

## Credentials (passwords, access keys, and MFA

devices)

Review the following guides to manage
passwords, access keys,
and MFA devices for your AWS account and for IAM users.

- **[User passwords in AWS](id_credentials_passwords.md "id_credentials_passwords.md")** –
  Describes
  options for managing passwords for IAM users in your
  account.
- **[Manage access keys for IAM users](id_credentials_access-keys.md "id_credentials_access-keys.md")** –

Describes how _access keys_ work and how you can use them to make
programmatic calls to AWS. There are other more secure alternatives to access keys that
we recommend you consider first. For more information, see [Considerations and alternatives for long-term access keys](../../../general/latest/gr/aws-sec-cred-types.md#alternatives-to-long-term-access-keys "../../../general/latest/gr/aws-sec-cred-types.md#alternatives-to-long-term-access-keys") in the
_AWS General Reference guide_.

- **[AWS Multi-factor authentication in IAM](id_credentials_mfa.md "id_credentials_mfa.md")** – Describes how to configure
  your account and IAM users to require both a password and a one-time use code that is
  generated on a device before sign-in is allowed. (This is sometimes called two-factor
  authentication.)

For general information about the types of credentials you use to access Amazon Web Services, see
**[AWS Security
Credentials](../../../general/latest/gr/aws-security-credentials.md "../../../general/latest/gr/aws-security-credentials.md")** in the _AWS General Reference guide_..

## Permissions and policies

Learn the inner workings of IAM policies and find tips on the best ways to confer
permissions:

- **[Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md")** – Introduces the policy language that is used to define
  permissions. Describes how permissions can be attached to users or groups or, for some
  AWS products, to resources themselves.
- **[IAM JSON policy element reference](reference_policies_elements.md "reference_policies_elements.md")** – Provides
  descriptions and examples of each policy language element.
- **[IAM policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md")** – Find resources
  for JSON policy validation.
- **[Example IAM identity-based policies](access_policies_examples.md "access_policies_examples.md")** – Shows examples of
  policies for common tasks in various AWS products.
- **[AWS
  Policy Generator](https://aws.amazon.com/blogs/aws/aws-policy-generator/ "https://aws.amazon.com/blogs/aws/aws-policy-generator/")** – Create custom policies by choosing
  products and actions from a list.
- **[IAM Policy
  Simulator](https://policysim.aws.amazon.com/ "https://policysim.aws.amazon.com/")** – Test whether a policy would allow or deny a
  specific request to AWS.

## Federation and delegation

You can grant access to resources in your AWS account for users who are authenticated
(signed in) elsewhere. These can be IAM users in another AWS account (known as
_delegation_), users who are authenticated with your organization's
sign-in process, or users from an Internet identity provider like Login with Amazon, Facebook,
Google, or any other OpenID Connect (OIDC) compatible identity provider. In these cases, the
users get temporary security credentials to access AWS resources.

- **[IAM tutorial: Delegate access across
  AWS accounts using IAM roles](tutorial_cross-account-with-roles.md "tutorial_cross-account-with-roles.md")** – Guides you
  through granting cross-account access to an IAM user in another AWS account.
- **[Common scenarios for temporary credentials](id_credentials_temp.md#sts-introduction "id_credentials_temp.md#sts-introduction")** – Describes ways in which users
  can be federated into AWS after being authenticated outside of AWS.

## IAM and other AWS products

Most AWS products are integrated with IAM so that you can use IAM features to help
protect access to the resources in those products. The following resources discuss IAM and
security for some of the most popular AWS products. For a complete list of products that
work with IAM, including links to more information on each, see [AWS services that work with
IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md").

### Using IAM with Amazon EC2

- [Controlling Access to Amazon EC2
  Resources](../../../AWSEC2/latest/UserGuide/UsingIAM.md "../../../AWSEC2/latest/UserGuide/UsingIAM.md") – Describes how to use IAM features to permit users to
  administer Amazon EC2 instances, volumes, and more.
- [Use instance profiles](id_roles_use_switch-role-ec2_instance-profiles.md "id_roles_use_switch-role-ec2_instance-profiles.md") – Describes how to
  use IAM roles to securely provide credentials for applications that run on Amazon EC2
  instances and that need access to other AWS products.

### Using IAM with Amazon S3

- [Managing Access Permissions to Your
  Amazon S3 Resources](../../../AmazonS3/latest/userguide/s3-access-control.md "../../../AmazonS3/latest/userguide/s3-access-control.md") – Discusses the Amazon S3 security model for buckets and
  objects, which includes IAM policies.
- [Writing IAM Policies: Grant Access to User-Specific Folders in an Amazon S3
  Bucket](https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket "https://aws.amazon.com/blogs/security/writing-iam-policies-grant-access-to-user-specific-folders-in-an-amazon-s3-bucket") – Discusses how to let users protect their own folders in Amazon S3.
  (For more posts about Amazon S3 and IAM, choose the **S3** tag below the
  title of the blog post.)

### Using IAM with Amazon RDS

- [Using AWS Identity and Access Management (IAM) to Manage
  Access to Amazon RDS Resources](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md") – Describes how to use IAM to control
  access to database instances, database snapshots, and more.
- [A
  Primer on RDS Resource-Level Permissions](https://aws.amazon.com/blogs/security/a-primer-on-rds-resource-level-permissions "https://aws.amazon.com/blogs/security/a-primer-on-rds-resource-level-permissions") – Describes how to use IAM
  to control access to specific Amazon RDS instances.

### Using IAM with Amazon DynamoDB

- [Using IAM to Control Access to
  DynamoDB Resources](../../../amazondynamodb/latest/developerguide/UsingIAMWithDDB.md "../../../amazondynamodb/latest/developerguide/UsingIAMWithDDB.md") – Describes how to use IAM to permit users to
  administer DynamoDB tables and indexes.
- The following video (8:55) explains how to provide access control for individual
  DynamoDB database items or attributes (or both).

## General security practices

Find expert tips and guidance on the best ways to secure your AWS account and
resources:

- **[Best Practices for Security, Identity,
  &, Compliance](https://aws.amazon.com/architecture/security-identity-compliance "https://aws.amazon.com/architecture/security-identity-compliance")** – Find resources for how to manage
  security across AWS accounts and products, including suggestions for security
  architecture, use of IAM, encryption and data security, and more.
- **[Identity and Access Management](../../../wellarchitected/latest/security-pillar/identity-and-access-management.md "../../../wellarchitected/latest/security-pillar/identity-and-access-management.md")** – The AWS Well-Architected
  Framework helps you understand key concepts, design principles, and architectural best
  practices for designing and running workloads in the cloud.
- **[Security best practices in IAM](best-practices.md "best-practices.md")** – Offers recommendations for ways to use IAM to help secure your
  AWS account and resources.
- **[AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md")** – Use AWS CloudTrail to track a
  history of API calls made to AWS and store that information in log files. This helps you
  determine which users and accounts accessed resources in your account, when the calls were
  made, what actions were requested, and more.

## General resources

Explore the following resources to learn more about IAM and AWS.

- **[Product Information for
  IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")** – General information about the AWS Identity and Access Management
  product.
- **[AWS re:Post for AWS Identity and Access Management](https://forums.aws.amazon.com/forum.jspa?forumID=76 "https://forums.aws.amazon.com/forum.jspa?forumID=76")** – Visit AWS re:Post to discuss
  technical questions related to IAM with the AWS community.

- [Classes & Workshops](https://aws.amazon.com/training/course-descriptions/ "https://aws.amazon.com/training/course-descriptions/")
  – Links to role-based and specialty courses, in addition to
  self-paced labs to help sharpen your AWS skills and gain practical experience.
- [AWS Developer Center](https://aws.amazon.com/developer/?ref=docs_id=res1 "https://aws.amazon.com/developer/?ref=docs_id=res1")
  – Explore tutorials, download tools, and learn about AWS developer events.
- [AWS Developer Tools](https://aws.amazon.com/developer/tools/?ref=docs_id=res1 "https://aws.amazon.com/developer/tools/?ref=docs_id=res1")
  – Links to developer tools, SDKs, IDE toolkits, and command line tools
  for developing and managing AWS applications.
- [Getting Started Resource Center](https://aws.amazon.com/getting-started/?ref=docs_id=res1 "https://aws.amazon.com/getting-started/?ref=docs_id=res1")
  – Learn how to set up your AWS account, join the AWS community, and launch your first application.
- [Hands-On Tutorials](https://aws.amazon.com/getting-started/hands-on/?ref=docs_id=res1 "https://aws.amazon.com/getting-started/hands-on/?ref=docs_id=res1")
  – Follow step-by-step tutorials to launch your first application on AWS.
- [AWS Whitepapers](https://aws.amazon.com/whitepapers/ "https://aws.amazon.com/whitepapers/")
  – Links to a comprehensive list of technical AWS whitepapers, covering
  topics such as architecture, security, and economics and authored by AWS
  Solutions Architects or other technical experts.
- [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/")
  – The hub for creating and managing your
  AWS Support cases. Also includes links to other helpful
  resources, such as forums, technical FAQs,
  service health status, and AWS Trusted Advisor.
- [Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")
  – The primary webpage for information
  about Support, a one-on-one, fast-response support
  channel to help you build and run applications in the cloud.
- [Contact Us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/")
  – A central contact point for inquiries concerning
  AWS billing, account, events, abuse, and other issues.
- [AWS Site Terms](https://aws.amazon.com/terms/ "https://aws.amazon.com/terms/")
  – Detailed information about our copyright
  and trademark; your account, license, and site access;
  and other topics.
