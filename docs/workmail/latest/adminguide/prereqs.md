

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Prerequisites
<a name="prereqs"></a>

To act as an Amazon WorkMail administrator, you need an AWS account. If you haven't signed up for AWS yet, complete the following tasks to get set up.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Grant IAM users permissions for Amazon WorkMail](#iam_policies_workmail)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Grant IAM users permissions for Amazon WorkMail
<a name="iam_policies_workmail"></a>

By default, IAM users don't have permissions to manage Amazon WorkMail resources. You must attach an AWS managed policy (**AmazonWorkMailFullAccess** or **AmazonWorkMailReadOnlyAccess**) or create a customer-managed policy that explicitly grants IAM users those permissions. You then attach the policy to the IAM users or groups that require those permissions. For more information, see [Identity and access management for Amazon WorkMail](security-iam.md).