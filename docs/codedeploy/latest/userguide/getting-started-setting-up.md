

# Step 1: Setting up
<a name="getting-started-setting-up"></a>

Before you use AWS CodeDeploy for the first time, you must complete setup steps. The steps involve creating an AWS account (if you don't already have one), and an administrative user.

In this guide, the administrative user is called the **CodeDeploy administrative user**.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

**Important**  
We strongly recommend you configure the CodeDeploy adminstrative user as a workforce identity (a user managed in IAM Identity Center) with the AWS CLI. Many of the procedures in this guide assume you're using the AWS CLI to perform configurations.

**Important**  
If you configure the AWS CLI, you may be prompted to specify an AWS Region. Choose one of the supported Regions listed in [Region and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#codedeploy_region) in the *AWS General Reference*.