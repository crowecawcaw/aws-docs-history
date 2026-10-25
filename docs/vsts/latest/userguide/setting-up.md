

# Setting up the AWS Toolkit for Azure DevOps
<a name="setting-up"></a>

To use the AWS Toolkit for Azure DevOps to access AWS, you need an AWS account and AWS credentials. When build agents run the tasks contained in the tools, the tasks must be configured with, or have access to, those AWS credentials to enable them to call AWS service APIs. To increase the security of your AWS account, we recommend that you do not use your root account credentials. You should create an *IAM user* to provide access credentials to the tasks running in the build agent processes.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).