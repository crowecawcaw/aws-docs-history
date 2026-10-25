

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Prerequisites
<a name="prereqs"></a>

To act as an Amazon WorkMail administrator, you need an AWS account. If you haven't signed up for AWS yet, complete the following tasks to get set up.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Grant IAM users permissions for Amazon WorkMail](#iam_policies_workmail)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).

## Grant IAM users permissions for Amazon WorkMail
<a name="iam_policies_workmail"></a>

By default, IAM users don't have permissions to manage Amazon WorkMail resources. You must attach an AWS managed policy (**AmazonWorkMailFullAccess** or **AmazonWorkMailReadOnlyAccess**) or create a customer-managed policy that explicitly grants IAM users those permissions. You then attach the policy to the IAM users or groups that require those permissions. For more information, see [Identity and access management for Amazon WorkMail](security-iam.md).