# Determine your user type

How you sign in depends on what type of AWS user you are. You can manage an
AWS account as a root user, an IAM user, a user in IAM Identity Center, or a federated identity. You can
use an AWS Builder ID profile to access certain AWS services and tools. The different user types
are listed below.

###### Topics

- [Root user](#account-root-user-type "#account-root-user-type")
- [IAM user](#iam-user-type "#iam-user-type")
- [IAM Identity Center user](#sso-user-type "#sso-user-type")
- [Federated identity](#federated-identity-type "#federated-identity-type")
- [AWS Builder ID user](#builder-id-type "#builder-id-type")

## Root user

Also referred to as the account owner or account root user. As the root user, you have
complete access to all AWS services and resources in your AWS account. When you first
create an AWS account, you begin with a single sign-in identity that has complete access
to all AWS services and resources in the account. This identity is the AWS account
root user. You can sign in as the root user using the email address and password that you used to
create the account. Root users sign in with the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"). For step by step instructions on
how to sign in, see [Sign in to the AWS Management Console as the
root user](introduction-to-root-user-sign-in-tutorial.md "introduction-to-root-user-sign-in-tutorial.md").

###### Important

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

For more information about IAM identities including the root user, see [IAM Identities (users, user
groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md").

## IAM user

An IAM user is an entity you create in AWS. This user is an identity within your
AWS account that's granted specific custom permissions. Your IAM user credentials
consist of a name and password used to sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"). For step by step instructions on
how to sign in, see [Sign in to the AWS Management Console as an
IAM user](introduction-to-iam-user-sign-in-tutorial.md "introduction-to-iam-user-sign-in-tutorial.md").

For more information about IAM identities including the IAM user, see [IAM Identities (users, user
groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md").

## IAM Identity Center user

An IAM Identity Center user is a member of AWS Organizations and can be granted access to multiple
AWS accounts and applications through your AWS access portal. If their company has integrated
Active Directory or another identity provider with IAM Identity Center, users in IAM Identity Center can use their
corporate credentials to sign-in. IAM Identity Center can also be an identity provider where an
administrator can create users. Regardless of the identity provider, users in IAM Identity Center sign in
using your AWS access portal, which is a specific sign-in URL for their organization.
IAM Identity Center users **can't** sign in through the
AWS Management Console URL.

Human users in IAM Identity Center can get your AWS access portal URL from either:

- A message from their administrator or help desk employee
- An email from AWS with an invitation to join IAM Identity Center

###### Tip

All emails sent by the IAM Identity Center service originate from either the address
**no-reply@signin.aws** or
**no-reply@login.awsapps.com**. We recommend that you configure your
email system so that it accepts emails from these sender email addresses and doesn't
handle them as junk or spam.

For step by step instructions on how to sign in, see [Sign in to your AWS access portal](iam-id-center-sign-in-tutorial.md "iam-id-center-sign-in-tutorial.md").

###### Note

We recommend you bookmark your organization's specific sign-in URL for your
AWS access portal so that you can access it later.

For more information about IAM Identity Center, see [What is IAM Identity
Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md")

## Federated identity

A federated identity is a user who can sign in using a well-known external identity
provider (IdP), such as Login with Amazon, Facebook, Google, or any other [OpenID Connect (OIDC)](https://openid.net/connect/ "https://openid.net/connect/")-compatible IdP. With web
identity federation, you can receive an authentication token, and then exchange that token
for temporary security credentials in AWS that map to an IAM role with permissions to
use the resources in your AWS account. You don't sign in with the AWS Management Console or
AWS access portal. Instead, the external identity in use determines how you sign in.

For more information, see [Sign in as a federated identity](federated-identity-overview.md "federated-identity-overview.md").

## AWS Builder ID user

As an AWS Builder ID user, you specifically sign in to the AWS service or tool that you
want to access. An AWS Builder ID user complements any AWS account you already have or want to
create. An AWS Builder ID represents you as a person, and you can use it to access AWS services
and tools without an AWS account. You also have a profile where you can see and update
your information. For more information, see [Sign in with AWS Builder ID](sign-in-builder-id.md "sign-in-builder-id.md").

AWS Builder ID is separate from your AWS Skill Builder subscription, an online learning
center where you can learn from AWS experts and build cloud skills online. For
more information about AWS Skill Builder, see
[AWS Skill Builder](https://skillbuilder.aws/ "https://skillbuilder.aws/").
