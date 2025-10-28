# Amazon Macie and

AWS Organizations

Amazon Macie is a fully managed data security and data privacy service that uses machine
learning and pattern matching to discover, monitor, and help you protect your sensitive data
in Amazon Simple Storage Service (Amazon S3). Macie automates the discovery of sensitive data, such as personally
identifiable information (PII) and intellectual property, to provide you with a better
understanding of the data that your organization stores in Amazon S3.

For more information, see [Managing Amazon Macie accounts
with AWS Organizations](../../../macie/latest/user/macie-organizations.md "../../../macie/latest/user/macie-organizations.md") in the _[Amazon Macie User Guide](../../../macie/latest/userguide.md "../../../macie/latest/userguide.md")_.

Use the following information to help you integrate
Amazon Macie with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created for your organization's delegated Macie
administrator account when you enable trusted access. This role allows
Macie to perform supported operations for the accounts in your
organization.

You can delete this role only if you disable trusted access between Macie
and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleRorAmazonMacie`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Macie grant access to the following service
principals:

- `macie.amazonaws.com`

## Enabling trusted access with

Macie

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the Amazon Macie console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the Amazon Macie console or
tools to enable integration with Organizations. This lets Amazon Macie perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by Amazon Macie. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the Amazon Macie console or tools then you
don’t need to complete these steps.

###### To enable trusted access using the Macie console

Amazon Macie requires trusted access to AWS Organizations to designate a member account to be
the Macie administrator for your organization. If you configure a delegated
administrator using the Macie management console, then Macie automatically enables
trusted access for you.

For more information, see [Integrating and configuring an organization in Amazon Macie](../../../macie/latest/user/accounts-mgmt-ao-integrate.md "../../../macie/latest/user/accounts-mgmt-ao-integrate.md") in the _Amazon Macie User Guide_.

You can enable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To enable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable Amazon Macie as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal macie.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Enabling a delegated administrator

account for Macie

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
Macie that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of Macie.

###### Minimum permissions

Only a user or role in the Organizations management account with the following
permissions can configure a member account as a delegated administrator for
Macie in the organization:

- `organizations:EnableAWSServiceAccess`
- `macie:EnableOrganizationAdminAccount`

###### To designate a member account as a delegated administrator for

Macie

Amazon Macie requires trusted access to AWS Organizations to designate a member account to be
the Macie administrator for your organization. If you configure a delegated
administrator using the Macie management console, then Macie automatically enables
trusted access for you.

For more information, see [https://docs.aws.amazon.com/macie/latest/user/macie-organizations.html#register-delegated-admin](../../../macie/latest/user/macie-organizations.md#register-delegated-admin "../../../macie/latest/user/macie-organizations.md#register-delegated-admin")
