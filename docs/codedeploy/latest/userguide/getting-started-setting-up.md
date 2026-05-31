# Step 1: Setting up

Before you use AWS CodeDeploy for the first time, you must complete setup steps. The steps
involve creating an AWS account (if you don't already have one), and an administrative user.

In this guide, the administrative user is called the **CodeDeploy
administrative user**.

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

###### Important

We strongly recommend you configure the CodeDeploy adminstrative user as a workforce
identity (a user managed in IAM Identity Center) with the AWS CLI. Many of the procedures in this guide
assume you're using the AWS CLI to perform configurations.

###### Important

If you configure the AWS CLI, you may be prompted to specify an AWS Region. Choose one
of the supported Regions listed in [Region and endpoints](../../../general/latest/gr/rande.md#codedeploy_region "../../../general/latest/gr/rande.md#codedeploy_region") in the _AWS General Reference_.
