# AWS Builder ID and other AWS credentials

Your AWS Builder ID is separate from any AWS account or sign in credential. You can use the
same email for your AWS Builder ID and for the root user email of an AWS account.

An AWS Builder ID:

- Allows you to access tools and services that use AWS Builder ID.
- Doesn't impact existing security controls, such as policies and configurations that you've
  specified on your AWS accounts or applications.
- Doesn't replace any existing root, IAM Identity Center, or IAM users, credentials, or accounts.
- Can't obtain AWS IAM credentials to access the AWS Management Console, AWS CLI, AWS SDKs, or AWS
  Toolkit.
  An AWS account is a resource container with contact and payment information. It
  establishes a security boundary in which to operate billed and metered AWS services, like S3,
  EC2, or Lambda. Account owners can sign in to an AWS account in the AWS Management Console. For more
  information see [Signing in to
  the AWS Management Console](console-sign-in-tutorials.md "console-sign-in-tutorials.md").

## How AWS Builder ID relates to your existing IAM Identity Center identity

As the individual who owns the identity you manage the AWS Builder ID. It's not connected to any
other identity you may have for another organization, such as school or work. You might use a
workforce identity in IAM Identity Center to represent your work-self and an AWS Builder ID to represent your
private-self. These identities operate independently.

Users in AWS IAM Identity Center (successor to AWS Single Sign-On) are managed by a corporate IT or cloud administrator, or by the
administrator of the organization’s identity provider, such as Okta, Ping, or Azure. Users in
IAM Identity Center can access resources across multiple accounts in AWS Organizations.

## Multiple AWS Builder ID profiles

You can create more than one AWS Builder ID as long as each ID uses a unique email address.
However, using more than one AWS Builder ID can make it difficult to recall which AWS Builder ID you used
for which purpose. When possible, we recommend using a single AWS Builder ID for all your activities
in AWS tools and services.

## Using our new AWS experience and AWS Builder ID

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

If you use your AWS Builder ID to sign into AWS using our new AWS experience and access
projects and AWS Settings, your AWS Builder ID is your sign in credential. In this case,
your AWS Builder ID does the following:

- Allows you to access all AWS tools and services that support our new AWS experience
- Replaces your root, IAM Identity Center, or IAM users as the credential to access
  your AWS resources.
- Can be used to obtain AWS IAM credentials to access the AWS Management Console,
  AWS CLI, AWS SDKs, or AWS Toolkit.

Your AWS Builder ID will be the resource container with contact and payment information for
all your projects. You can use your AWS Builder ID to sign into the AWS Management Console.
