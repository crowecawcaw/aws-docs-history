

# Amazon Q Developer and AWS Organizations
<a name="services-that-can-integrate-amazon-q-dev"></a>

 Amazon Q Developer is a generative AI powered conversational assistant that can help you understand, build, extend, and operate AWS applications. It is also a general purpose, machine learning-powered code generator that provides you with code recommendations in real time. The paid subscription version of Amazon Q Developer requires Organizations integration. For more information see [ Account, IAM Identity Center, and Organizations setup ](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-topic-account.html#admin-setup-org) in the *Amazon Q user guide*. 

Use the following information to help you integrate Amazon Q Developer with AWS Organizations.



## Service-linked roles
<a name="integrate-enable-slr-amazon-q-dev"></a>

The `AWSServiceRoleForAmazonQDeveloper` service-linked role allows Amazon Q Developer to perform supported operations within your organization. Create the role using the Amazon Q Developer console, API, or CLI, as described in [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/). 

If you are using a member account, then you can delete or modify this role only if you disable trusted access between Amazon Q Developer and Organizations, or if you remove the member account from the organization. 

## Service principals used by Amazon Q Developer
<a name="integrate-enable-svcprin-amazon-q-dev"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by Amazon Q Developer grant access to the following service principals:
+ `q.amazonaws.com`

## Enabling trusted access with Amazon Q Developer
<a name="integrate-enable-ta-amazon-q-dev"></a>

 Amazon Q Developer Pro uses trusted access to share the settings made in the Organizations management account with member accounts in the same organization. 

For example, the Amazon Q Developer Pro administrator, working in the Organizations management account, may enable suggestions with code references. If trusted access is enabled, then suggestions with code references will also be enabled for all member accounts in that organization. 

You can only enable trusted access using Amazon Q Developer.

To enable trusted access for Amazon Q Developer, use this procedure.

1. On the Amazon Q Developer **Settings** page, under **Member account settings**, choose **Edit**.

1. In the pop-up window, select **On**.

1. Choose **Save**.

For more information, see [ Enabling trusted access](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-general.html#q-admin-trusted-access) in the *Amazon Q Developer user guide*. 

## Disabling trusted access with Amazon Q Developer
<a name="integrate-disable-ta-amazon-q-dev"></a>

You can only disable trusted access using the Amazon Q Developer tools.

To disable trusted access for Amazon Q Developer, use this procedure.

1. On the Amazon Q Developer **Settings** page, under **Member account settings**, choose **Edit**.

1. In the pop-up window, select **Off**.

1. Choose **Save**.

For more information, see [ Enabling trusted access](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-general.html#q-admin-trusted-access) in the *Amazon Q Developer user guide*. 