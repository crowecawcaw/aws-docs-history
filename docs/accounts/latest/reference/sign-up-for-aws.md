# Compare sign-up options

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

When you sign up for AWS, you unlock the world's most comprehensive and broadly adopted
cloud. We offer the greatest choice of innovative cloud and AI capabilities and expertise, on
the most extensive global infrastructure, with industry-leading security, reliability, and
performance.

There are two ways to sign up for AWS. If you want complete control over account
configuration and where your content is stored, or if you have regulated workloads such as
HIPAA, FedRAMP, use [Sign up for AWS (advanced)](getting-started.md "getting-started.md"). If you are
a new user and want to use a login you already own to sign in to AWS and create an AWS
environment with preconfigured defaults in select [AWS Regions](project-regions.md "project-regions.md"), use [Sign up for AWS (new)](sign-in-new.md "sign-in-new.md").

## Considerations for choosing how to sign up for AWS

Consider the following before choosing your sign-up method. You can activate all AWS
features for your account if necessary.

- If you have specific product requirements such as regulated workloads that include
  HIPAA or FedRAMP, do not use our new AWS experience.
- Your content will be stored in a designated Region which is selected based on
  your contact information.
- The new AWS experience makes it easier for you to start building without
  creating AWS permissions. If you need fine-grained control over your users or
  role-based permissions, do not use Sign up for AWS (new).
- If you need account-specific payment configurations set up by AWS, also known as net terms billing, do not use Sign up for AWS (new).
- If you need access to the full set of AWS services, do not use Sign up for AWS (new). For more information, see
  [Supported AWS services for Sign up for AWS (new)](supported-services-sign-up-new.md "supported-services-sign-up-new.md").

## Compare features for sign-up options

The following table compares AWS wide requirements that are either supported for Sign up for AWS (new) or Sign up for AWS (advanced). If a feature is not listed in this table
or described in [Compare access management](#compare-access-management "#compare-access-management"), it is available. You can activate advanced features for your account if you need any of the unsupported features. For more information, see [Activate advanced AWS features](activate-advanced-features.md "activate-advanced-features.md").

| Feature                                                                                                                                                                                                   | Sign up for AWS (new)                                                                                                                        | Sign up for AWS (advanced)                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Join AWS Partner Network                                                                                                                                                                                  | No                                                                                                                                           | Yes                                                                                                |
| Create a Professional Services contract                                                                                                                                                                   | No                                                                                                                                           | Yes                                                                                                |
| Enroll in an Enterprise Agreement with AWS                                                                                                                                                                | No                                                                                                                                           | Yes                                                                                                |
| Purchase an AWS Skill Builder Team subscription                                                                                                                                                           | No                                                                                                                                           | Yes                                                                                                |
| Work with an AWS Training Partner                                                                                                                                                                         | No                                                                                                                                           | Yes                                                                                                |
| Earn extra credits from AWS Activate                                                                                                                                                                      | No                                                                                                                                           | Yes                                                                                                |
| Use AWS Marketplace                                                                                                                                                                                       | No                                                                                                                                           | Yes                                                                                                |
| Designate your AWS account as HIPAA or SEC compliant                                                                                                                                                      | No                                                                                                                                           | Yes                                                                                                |
| Select a specific AWS Region to create your Regional resources                                                                                                                                            | No. For more information, see [AWS Regions for your projects](project-regions.md "project-regions.md").                                      | Yes                                                                                                |
| Access an opt-in Region                                                                                                                                                                                   | No                                                                                                                                           | Yes                                                                                                |
| [IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md")                                                                | No                                                                                                                                           | Yes                                                                                                |
| Sign-in access policies                                                                                                                                                                                   | No                                                                                                                                           | Yes                                                                                                |
| Create spend limits for your accounts                                                                                                                                                                     | Yes                                                                                                                                          | No                                                                                                 |
| Savings plans                                                                                                                                                                                             | No                                                                                                                                           | Yes                                                                                                |
| Automatic opt-in to [Cost<br>Optimization Hub](../../../cost-management/latest/userguide/cost-optimization-hub.md "../../../cost-management/latest/userguide/cost-optimization-hub.md") for the Paid Plan | [Yes](../../../cost-management/latest/userguide/bcm-lite-coh-savings.md "../../../cost-management/latest/userguide/bcm-lite-coh-savings.md") | No                                                                                                 |
| Automatic opt-in to [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")                                      | Yes                                                                                                                                          | No                                                                                                 |
| Automatic opt-in to [IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md")                                                          | Yes                                                                                                                                          | No                                                                                                 |
| Automatically opt in to [IAM role manager](../../../IAM/latest/UserGuide/id_roles_create_role-manager.md "../../../IAM/latest/UserGuide/id_roles_create_role-manager.md")                                 | Yes                                                                                                                                          | No                                                                                                 |
| Console account colors                                                                                                                                                                                    | No                                                                                                                                           | Yes                                                                                                |
| Disable multi-session console support                                                                                                                                                                     | No                                                                                                                                           | Yes. If you sign in again using a Builder ID, multi-session support will be enabled automatically. |

## Compare access management

When you use our new AWS experience, AWS creates preconfigured defaults to help you
get started building. Your AWS resources are organized in projects. A project contains an
AWS account and settings for sharing with other collaborators. If you use the paid plan,
your project can also have a set monthly pre-tax cost, called a spend limit. All of the
projects you own make up your organization, which you control through your management account
in AWS Settings. This organization is the same as an AWS Organization; however, AWS
manages aspects of this organization on your behalf.

AWS manages the following elements of your AWS Organization:

- **Organization management policies.** When you use our new AWS experience, AWS manages the organization management policies including the
  resource control policies (RCPs) and the service control policies (SCPs). If you want to
  create your own, use Sign up for AWS (advanced).
- **Human access roles.** A human access role is any role
  that allows a human to have specific permissions. For example, a human access role could
  let the user tester have read only access to Amazon Bedrock. While you can create IAM
  roles and IAM users, we recommend only using them when necessary. AWS manages all
  human access to your project. You can add and remove team members to your project. When
  you add a team member, they have access to all the resources in your project. For more
  information, see [Invite team members to collaborate in AWS Settings](invite-team-members.md "invite-team-members.md").

Every project has a managed security implementation that makes it easy to build with
confidence. By default, any application or code in your project has access to all AWS
resources in that same project. You do not need to perform additional access
configuration.

AWS resources in different projects cannot access each other, unless you turn on
cross-project access for certain resources. For instance, you can create a Lambda function
in one project and then invoke it using an API in a different project. This is described as a
cross-account integration. For more information, see [Cross-account
Lambda integrations](../../../apigateway/latest/developerguide/apigateway-cross-account-lambda-integrations.md "../../../apigateway/latest/developerguide/apigateway-cross-account-lambda-integrations.md"). As long as both projects are owned by the same management
account, this is supported.

By default, your project does not provide external access to any resources. You must
configure AWS resources to allow for public access. You can do the following:

- Create a public S3 bucket to host a simple static website or files. For more
  information, see [Getting
  started with Amazon S3](../../../AmazonS3/latest/userguide/GetStartedWithS3.md "../../../AmazonS3/latest/userguide/GetStartedWithS3.md").
- Create an API Gateway API to act as the front door of your application. For more
  information, see [Build
  an HTTP API](../../../apigateway/latest/developerguide/http-api-dynamo-db.md "../../../apigateway/latest/developerguide/http-api-dynamo-db.md").
- Create an EC2 instance with a public IP address to allow for communication between
  your instances and the Internet. For more information, see [Launch
  your first EC2 instance](../../../AWSEC2/latest/UserGuide/tutorial-launch-my-first-ec2-instance.md "../../../AWSEC2/latest/UserGuide/tutorial-launch-my-first-ec2-instance.md").
- Create a CloudFront distribution to deliver your static and dynamic web content,
  such as .html, .css, .js, and image files, to your users. For more information, see
  [Getting
  started with CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.md "../../../AmazonCloudFront/latest/DeveloperGuide/GettingStarted.SimpleDistribution.md").
- Create a Lambda function URL to provide a simple, direct publicly accessible HTTP
  endpoint for a Lambda function. Make sure your Lambda function has the correct
  permissions. For more information, see [Creating
  a function URL](../../../lambda/latest/dg/urls-configuration.md "../../../lambda/latest/dg/urls-configuration.md") and [Security and auth model for Lambda function URLs](../../../lambda/latest/dg/urls-auth.md "../../../lambda/latest/dg/urls-auth.md").
- Use a combination of these or other AWS mechanisms.

In addition, when you activate advanced features, you have access to even more mechanisms
to provide external access to your resources.

## Manage your AWS accounts

You manage your AWS accounts based on the type of AWS you're using. The following
table shows where to find the documentation for each management task.

| Task                                   | [Sign up for AWS (new)](sign-in-new.md "sign-in-new.md")                                                                        | [Sign up for AWS (advanced)](getting-started.md "getting-started.md")                                                                                                                   |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sign up                                | [Sign up for AWS (new)](sign-in-new.md "sign-in-new.md")                                                                        | [Sign up for AWS (advanced)](getting-started.md "getting-started.md")                                                                                                                   |
| Create an account                      | [Create a project in AWS Settings](create-project.md "create-project.md")                                                       | [Sign up for AWS (advanced)](getting-started.md "getting-started.md")                                                                                                                   |
| Close an account                       | [Close a project in AWS Settings](close-project.md "close-project.md")                                                          | [Close an AWS account](manage-acct-closing.md "manage-acct-closing.md")                                                                                                                 |
| Update your password                   | [Update your password in AWS Settings](update-password.md "update-password.md")                                                 | [Update root user password](manage-acct-update-root-user-password.md "manage-acct-update-root-user-password.md")                                                                        |
| Register MFA devices                   | [Manage multi-factor authentication (MFA) in AWS Settings](register-mfa-devices.md "register-mfa-devices.md")                   | [Step 3: (Recommended) Set up the AWS MCP Server](getting-started.md#getting-started-step3 "getting-started.md#getting-started-step3")                                                  |
| Change your email                      | [Change your email address in AWS Settings](change-email.md "change-email.md")                                                  | [Update the root user email address](manage-acct-update-root-user-email.md "manage-acct-update-root-user-email.md")                                                                     |
| Change your name                       | [Manage your name or nickname in AWS Settings](change-name.md "change-name.md")                                                 | [Update your AWS account name](manage-acct-update-acct-name.md "manage-acct-update-acct-name.md")                                                                                       |
| Update contact information             | [Edit your contact information in AWS Settings](edit-contact-info.md "edit-contact-info.md")                                    | [Update the primary contact for your AWS account](manage-acct-update-contact-primary.md "manage-acct-update-contact-primary.md")                                                        |
| Update alternate contacts              | Not applicable                                                                                                                  | [Update the alternate contacts for your AWS account](manage-acct-update-contact-alternate.md "manage-acct-update-contact-alternate.md")                                                 |
| Manage billing                         | [Manage your payment method in AWS Settings](manage-payment-method.md "manage-payment-method.md")                               | [Update billing for your AWS account](manage-acct-billing.md "manage-acct-billing.md")                                                                                                  |
| Manage tax information                 | [Manage tax registration in AWS Settings](manage-tax-registration.md "manage-tax-registration.md")                              | [Manage your payments](../../../awsaccountbilling/latest/aboutv2/manage-account-payment.md "../../../awsaccountbilling/latest/aboutv2/manage-account-payment.md")                       |
| Enable or disable AWS Regions          | Not applicable. You cannot modify your AWS Region.                                                                              | [Enable or disable AWS Regions in your account](manage-acct-regions.md "manage-acct-regions.md")                                                                                        |
| View account identifiers               | Not applicable                                                                                                                  | [View AWS account identifiers](manage-acct-identifiers.md "manage-acct-identifiers.md")                                                                                                 |
| Create an account alias                | Not applicable                                                                                                                  | [Create an AWS account alias](manage-acct-alias.md "manage-acct-alias.md")                                                                                                              |
| Upgrade your account                   | [Upgrade your account in AWS Settings](upgrade-account.md "upgrade-account.md")                                                 | [Free Tier plans](../../../awsaccountbilling/latest/aboutv2/free-tier-plans.md "../../../awsaccountbilling/latest/aboutv2/free-tier-plans.md")                                          |
| Create a spend limit                   | [Create a spend limit in AWS Settings](create-spend-limit.md "create-spend-limit.md")                                           | Not applicable                                                                                                                                                                          |
| Update a spend limit                   | [Update a spend limit in AWS Settings](update-spend-limit.md "update-spend-limit.md")                                           | Not applicable                                                                                                                                                                          |
| Remove a spend limit                   | [Remove a spend limit in AWS Settings](remove-spend-limit.md "remove-spend-limit.md")                                           | Not applicable                                                                                                                                                                          |
| Invite team members                    | [Invite team members to collaborate in AWS Settings](invite-team-members.md "invite-team-members.md")                           | [IAM Identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md")                                                                                             |
| Switch between projects                | [Switch between projects](switch-projects.md "switch-projects.md")                                                              | [Multi-session support](../../../awsconsolehelpdocs/latest/gsg/multisession.md "../../../awsconsolehelpdocs/latest/gsg/multisession.md")                                                |
| Connect an AI coding tool              | [Connect an AI coding tool](connect-ai-coding-tool.md "connect-ai-coding-tool.md")                                              | Not applicable                                                                                                                                                                          |
| Delete all sessions                    | [Delete all sessions in AWS Settings](delete-all-sessions.md "delete-all-sessions.md")                                          | Not applicable                                                                                                                                                                          |
| Opt out of AI data use                 | [Opt out of use of your content for service improvement in AWS Settings](opt-out-ai-data-use.md "opt-out-ai-data-use.md")       | [AI services opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") |
| Request your data                      | [Request your AWS Builder ID data](request-your-builder-id-data.md "request-your-builder-id-data.md")                           | [Request your data](https://pages.awscloud.com/DSAR_RTF.html "https://pages.awscloud.com/DSAR_RTF.html")                                                                                |
| Delete your AWS profile                | [Close your account in AWS Settings](close-account-new-experience.md "close-account-new-experience.md")                         | [Close an AWS account](manage-acct-closing.md "manage-acct-closing.md")                                                                                                                 |
| Manage accounts in India               | [Manage accounts in India in AWS Settings](manage-accounts-india-in-aws-settings.md "manage-accounts-india-in-aws-settings.md") | [Manage accounts in India](managing-accounts-india.md "managing-accounts-india.md")                                                                                                     |
| Create an administrator user           | Not applicable                                                                                                                  | [Sign up for AWS (advanced)](getting-started.md "getting-started.md")                                                                                                                   |
| Plan your account governance structure | Not applicable                                                                                                                  | [Plan your AWS account governance structure](plan-acct-structure.md "plan-acct-structure.md")                                                                                           |
