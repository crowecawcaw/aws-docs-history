

# Step 1: Set up an AWS account and create a User
<a name="setting-up"></a>

Before you use Amazon Rekognition for the first time, you must complete the following tasks:

1. Sign up for an AWS account.

1. Create a User.

This section of the developer guide explains why and how you'll create an AWS account and user.

**Topics**
+ [Create an AWS Account and User](#setting-up-iam)

## Create an AWS Account and User
<a name="setting-up-iam"></a>

**AWS Accounts**

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed up for all services in AWS, including Amazon Rekognition. You're charged only for the services that you use.

With Amazon Rekognition, you pay only for the resources that you use. 

If you're a new AWS customer, you can get started with Amazon Rekognition for free. For more information, see [AWS Free Usage Tier](https://aws.amazon.com/free/).

Refer to the upcoming [Sign up for an AWS account](#sign-up-for-aws) section for account creation instructions.

If you already have an AWS account, skip account setup and create an administrative user.

**Users**

Services in AWS, such as Amazon Rekognition, require that you provide credentials when you access them. This is so that the service can determine whether you have permissions to access the resources owned by that service. 

You can create access keys for your AWS account to access the AWS CLI or APIs while using the console requires your password. However, we don't recommend that you access AWS by using the credentials for your AWS account root user. Instead, we recommend that you use AWS Identity and Access Management (IAM) to create an administrative user.

You can then access AWS by using a special URL and that administrative user's credentials.

If you signed up for AWS, but you haven't yet created a user for yourself, you can create one by using the IAM console. Refer to the upcoming  section for instructions about how to create an administrative user.



### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.