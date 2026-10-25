

AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html). 

# Setting up AWS Systems Manager Incident Manager
<a name="setting-up"></a>

We recommend setting up AWS Systems Manager Incident Manager in the account that you use to manage your operations. Before you use Incident Manager for the first time, complete the following tasks:

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Required role for Incident Manager setup](#iam-prereq-service-role)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Required role for Incident Manager setup
<a name="iam-prereq-service-role"></a>

Before you begin, your account must have the IAM permission `iam:CreateServiceLinkedRole`. Incident Manager uses this permission to create the `AWSServiceRoleforIncidentManager` in your account. For more information, see [Using service-linked roles for Incident Manager](using-service-linked-roles.md). 