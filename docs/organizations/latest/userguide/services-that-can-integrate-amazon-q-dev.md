# Amazon Q Developer and

AWS Organizations

Amazon Q Developer is a generative AI powered conversational assistant that can help you understand, build,
extend, and operate AWS applications. It is also a general purpose, machine learning-powered code generator that provides you with
code recommendations in real time. The paid subscription version of Amazon Q Developer requires Organizations integration. For more information see
[Account, IAM Identity Center, and Organizations setup](../../../amazonq/latest/qdeveloper-ug/q-admin-setup-topic-account.md#admin-setup-org "../../../amazonq/latest/qdeveloper-ug/q-admin-setup-topic-account.md#admin-setup-org") in the _Amazon Q user guide_.

Use the following information to help you integrate
Amazon Q Developer with AWS Organizations.

## Service-linked roles

The `AWSServiceRoleForAmazonQDeveloper` service-linked role allows Amazon Q Developer to perform supported operations within your organization.
Create the role using the Amazon Q Developer console, API, or CLI, as described in [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

If you are using a member account, then you can delete or modify this role only if you disable trusted access between Amazon Q Developer and Organizations, or if you remove the member account from the organization.

## Service principals used by Amazon Q Developer

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Amazon Q Developer grant access to the following service
principals:

- `q.amazonaws.com`

## Enabling trusted access with

Amazon Q Developer

Amazon Q Developer Pro uses trusted access to share the settings made in the Organizations management
account with member accounts in the same organization.

For example, the Amazon Q Developer Pro administrator, working in the Organizations management
account, may enable suggestions with code references. If trusted access is enabled, then
suggestions with code references will also be enabled for all member accounts in that
organization.

You can only enable trusted access using
Amazon Q Developer.

To enable trusted access for Amazon Q Developer, use this procedure.

1. On the Amazon Q Developer **Settings** page, under **Member account settings**, choose **Edit**.
2. In the pop-up window, select **On**.
3. Choose **Save**.

For more information, see [Enabling trusted access](../../../amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-general.md#q-admin-trusted-access "../../../amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-general.md#q-admin-trusted-access") in the _Amazon Q Developer user
guide_.

## Disabling trusted access with

Amazon Q Developer

You can only disable trusted access using the
Amazon Q Developer tools.

To disable trusted access for Amazon Q Developer, use this procedure.

1. On the Amazon Q Developer **Settings** page, under **Member account settings**, choose **Edit**.
2. In the pop-up window, select **Off**.
3. Choose **Save**.

For more information, see [Enabling trusted access](../../../amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-general.md#q-admin-trusted-access "../../../amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-general.md#q-admin-trusted-access") in the _Amazon Q Developer user
guide_.
