# Creating an Amazon Quick Suite-integrated Amazon Q Business

application

With an Amazon Quick Suite-integrated Amazon Q Business application, Quick Suite users authenticate through
Amazon Quick Suite and access answers from unstructured data in Amazon Q Business. [Amazon Quick Suite](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md")
is a business intelligence service that provides insights from your structured data, such as
databases, data lakes, and data warehouses.

With Quick Suite authentication, your Amazon Quick Suite administrator uses Quick Suite as a single
point of entry to manage access to unstructured data in Amazon Q Business. You can manage users and
groups without reliance on AWS IAM Identity Center, including permissions, governance, and access
controls.

After you set up Quick Suite as your authentication, users sign in through Quick Suite with
their existing credentials. After authentication, they can use Quick Suite Q&A and Data
Stories to get answers to questions based on your unstructured enterprise data in Amazon Q Business
and your structured data analytics.

You can create an Quick Suite integrated Amazon Q Business application environment from Amazon Quick Suite or you can
create it with the Amazon Q Business [CreateApplication](../api-reference/API_CreateApplication.md "../api-reference/API_CreateApplication.md")
API operation.

###### Topics

- [Considerations](#quicksight-integrated-application-considerations "#quicksight-integrated-application-considerations")
- [Creating a Quick Suite-integrated
  application from Amazon Quick Suite](#creating-application-from-quicksight "#creating-application-from-quicksight")
- [Creating a
  Quick Suite-integrated application with Amazon Q Business API operations](#create-quicksight-integrated-application-apis "#create-quicksight-integrated-application-apis")

## Considerations

The following limitations apply to the Amazon Q application.

- Quick Suite and Amazon Q Business must exist in the same AWS account. Cross account calls
  are not supported.
- Quick Suite and Amazon Q Business accounts must exist in the same AWS Region. Cross-region
  calls are not supported. For a list of all supported Quick Suite Regions, see
  [Supported AWS Regions for Amazon Q in QuickSight](../../../quicksight/latest/user/regions-aqs.md "../../../quicksight/latest/user/regions-aqs.md"). For
  a list of all supported Amazon Q Business Regions, see [Service quotas for
  Amazon Q Business](quotas-regions.md "quotas-regions.md").

If your Quick Suite account exists in more than one region, you can connect one
Amazon Q Business application from each region to the Quick Suite account. For example,
if your Quick Suite account exists in US East (N. Virginia) and US West (Oregon),
one Amazon Q Business application located in US East (N. Virginia) and one Amazon Q Business
application located in US West (Oregon) can be connected to the Quick Suite
account.

- Quick Suite and Amazon Q Business accounts that are integrated need to use the same identity
  methods. For example, if a Quick Suite account uses IAM Identity Center for identity management,
  the Amazon Q Business account that it is integrating with must also use IAM Identity Center for
  identity management.
- Email addresses that are associated with Quick Suite users and groups are used
  to perform authorization checks in Amazon Q Business.
- To create an Amazon Q Business application with the [CreateApplication](../api-reference/API_CreateApplication.md "../api-reference/API_CreateApplication.md") API operation, the user or role must have
  permissions to create an application. For more information about setting up
  Amazon Q Business, see [Setting up for Amazon Q Business](setting-up.md "setting-up.md").

## Creating a Quick Suite-integrated

application from Amazon Quick Suite

To set up an Quick Suite-integrated Amazon Q Business application environment, Quick Suite administrators
can create a new application from the Quick Suite admin portal or connect to an existing
one. After you create an application environment, you create an index and add a data source in
Amazon Q Business.

- For information on setting up and managing a Quick Suite-integrated Amazon Q Business
  application from Quick Suite, see [Augmenting Amazon QuickSight generative BI capabilities with Amazon
  Q](../../../quicksight/latest/user/generative-bi-q-business-configure.md "../../../quicksight/latest/user/generative-bi-q-business-configure.md") in the _Amazon Quick Suite User Guide_.
- For information about adding a data source to an Amazon Q application, see [Connecting Amazon Q Business data sources](data-sources.md "data-sources.md").

## Creating a

Quick Suite-integrated application with Amazon Q Business API operations

To create an Amazon Quick Suite integrated application environment with Amazon Q Business APIs, you use the
[CreateApplication](../api-reference/API_CreateApplication.md "../api-reference/API_CreateApplication.md") API operation. For `identityType`, specify
`AWS_QUICKSIGHT_IDP`. In `QuickSightConfiguration`, specify
the `clientNamespace`. This is the Quick Suite namespace that you use as your
identity provider. For more information about Quick Suite namespaces, see [Namespace
operations](../../../quicksight/latest/developerguide/namespace-operations.md "../../../quicksight/latest/developerguide/namespace-operations.md").

The following example shows how to use the AWS Command Line Interface (AWS CLI) to create a
Quick Suite-integrated application environment.

```
aws qbusiness create-application \
--display-name `MyQBusinessApp` \
--identity-type AWS_QUICKSIGHT_IDP \
--quick-sight-configuration '{"clientNamespace": "`my-quicksight-namespace`"}'
```
