

As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

# Setting up Amazon CodeGuru Reviewer
<a name="setting-up-codeguru-reviewer"></a>

Complete the tasks in this section to set up Amazon CodeGuru Reviewer for the first time. If you already have an AWS account, know the repository that contains the source code you want reviewed, and prefer to use the defaults for IAM, skip ahead to [Getting started](getting-started-with-guru.md).

You should know the following about Amazon Web Services (AWS): 
+ When you sign up for AWS, your AWS account automatically has access to all services in AWS, including CodeGuru Reviewer. However, you are charged only for the services that you use. 
+ With CodeGuru Reviewer, you pay for the size of each of your associated repositories measured in lines of code. For more information, see [Amazon CodeGuru pricing](https://aws.amazon.com/codeguru/pricing/).
**Note**  
You can suppress recommendations from CodeGuru Reviewer, which reduces the number of lines of code analyzed and, by extension, might reduce costs. For more information, see [Suppress recommendations](recommendation-suppression.md).

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Configure IAM permissions for Amazon CodeGuru Reviewer](get-set-up-configure-iam-permissions.md)
+ [Install or upgrade and then configure the AWS CLI](get-set-up-install-cli.md)
+ [Create a repository for your source code](get-set-up-setup-repository.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).