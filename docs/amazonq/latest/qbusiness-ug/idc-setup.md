# Configuring an IAM Identity Center instance for an Amazon Q Business application

Amazon Q Business integrates with IAM Identity Center to enable managing end user access to
your Amazon Q Business application. IAM Identity Center is the recommended method for managing
human access to AWS resources. We recommend enabling and pre-configuring an IAM Identity Center
instance before creating your Amazon Q Business application.

###### Topics

- [Prerequisites](#idc-notes-create-application "#idc-notes-create-application")
- [Understanding types of IAM Identity Center instances](#idc-instance-types "#idc-instance-types")
- [Creating a same-region integration](#same-region-idc "#same-region-idc")
- [Creating a cross-region integration](#cross-region-idc "#cross-region-idc")

## Prerequisites

Before you create an Amazon Q Business application, make sure you complete
the following prerequisites:

- [Enable an IAM Identity Center instance](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") and [connect the identity source](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md") for your Amazon Q Business
  application environment in IAM Identity Center. Amazon Q Business supports both organization and account
  level IAM Identity Center instances.

###### Note

To minimize latency, we recommend using an IAM Identity Center instance created in
the same region as your Amazon Q Business application. However,
you can also use an IAM Identity Center instance created in an AWS region not yet
supported by Amazon Q Business. For more information, see [Creating a cross-region IAM Identity Center instance](idc-setup.md "idc-setup.md").

- [Configure an IAM Identity Center instance](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") to connect to
  your Amazon Q Business application environment with users and groups added. You
  can also create and connect an IAM Identity Center instance to Amazon Q Business
  from the Amazon Q Business console. You can only add users to an IAM Identity Center
  instance created from the Amazon Q Business and not groups. To add
  groups, you need to use the IAM Identity Center console.

###### Important

If you add a user to a group in IAM Identity Center and have given that group access
to your application, it can take up to 24 hours for the change to take
effect and for the user to be able to access your Amazon Q Business application.

## Understanding types of IAM Identity Center instances

There are two types of IAM Identity Center instances: organization instances and account
instances. Amazon Q supports both organization and account level IAM Identity Center
instances.

###### Important

Amazon Q Business supports cross-region IAM Identity Center and Amazon Q Business integrations only for organization instances. Amazon Q Business doesn't
support cross-region IAM Identity Center integrations for account level instances. Same-region
Amazon Q Business and IAM Identity Center integrations are supported for both
organization and account level instances.

The following section provides a brief overview of both instance types. For
in-depth distinctions between the two and prerequisites for enabling them, see
[Manage instances](../../../singlesignon/latest/userguide/identity-center-instances.md "../../../singlesignon/latest/userguide/identity-center-instances.md") in the IAM Identity Center User Guide.

###### Topics

- [Organization instances](#idc-org-account-setup "#idc-org-account-setup")
- [Account instances](#idc-account-instance-setup "#idc-account-instance-setup")

### Organization instances

When you enable IAM Identity Center in conjunction with AWS Organizations, you're creating
an organization instance of IAM Identity Center. AWS Organizations is an account management
service that enables you to consolidate multiple AWS accounts into an
organization that you create and centrally manage. Your organization instance
must be enabled in your management account and you can centrally manage the
access of users and groups with a single organization instance. This is the
AWS recommended approach to managing workforce identities.

To learn how to create and manage IAM Identity Center organization instances, see the
following content in the IAM Identity Center User Guide:

- [Enabling an organization instance of
  IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md")
- [Prerequisites and considerations for setting up
  IAM Identity Center](../../../singlesignon/latest/userguide/get-started-prereqs-considerations.md "../../../singlesignon/latest/userguide/get-started-prereqs-considerations.md")
- [Confirm your identity sources in
  IAM Identity Center](../../../singlesignon/latest/userguide/prereq-identity-sources.md "../../../singlesignon/latest/userguide/prereq-identity-sources.md")
- [Get started with common tasks in
  IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md")

### Account instances

If you don’t have plans to adopt IAM Identity Center for your entire organization, you can
use an account instance of IAM Identity Center to manage user and group access to Amazon Q Business
application. Account instances are bound to a single AWS account and are used
only to manage user and group access for supported applications in the same
account and AWS Region. You are limited to one account instance per AWS
account. You can create an account instance from either of the following:

- A member account in AWS Organizations.
- A standalone AWS account that is not managed by AWS
  Organizations.

An account instance may fit your use case if:

- You are trying out Amazon Q Business, and you haven’t yet decided that you
  want to deploy it to your entire organization.
- You are the administrator of a single AWS account within an
  organization. Instead of waiting for the administrator of your
  organization to implement Amazon Q Business, you want to go ahead and do it
  just for the AWS account that you control.
- Your enterprise is large, and does not have a single identity
  provider, or a single identity store, containing the entire user base
  that you want to give access to Amazon Q Business.

To learn how to create and manage IAM Identity Center account instances, see the following
content in the IAM Identity Center User Guide:

- [Account instances of IAM Identity Center](../../../singlesignon/latest/userguide/account-instances-identity-center.md "../../../singlesignon/latest/userguide/account-instances-identity-center.md")
- [Enable an account instance of
  IAM Identity Center](../../../singlesignon/latest/userguide/enable-account-instance-console.md "../../../singlesignon/latest/userguide/enable-account-instance-console.md")
- [Control account instance creation with Service
  Control Policies](../../../singlesignon/latest/userguide/control-account-instance.md "../../../singlesignon/latest/userguide/control-account-instance.md")
- [Create an account instance of
  IAM Identity Center](../../../singlesignon/latest/userguide/create-account-instance.md "../../../singlesignon/latest/userguide/create-account-instance.md")
- [Get started with common tasks in
  IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md")

## Creating a same-region integration

If you don’t have an existing IAM Identity Center instance to integrate with Amazon Q Business, we recommend creating one in a [region Amazon Q Business is available
in](quotas-regions.md#regions "quotas-regions.md#regions").

You can enable and configure an IAM Identity Center instance before you start to create your
Amazon Q Business application in the IAM Identity Center console. If you pre-configure
an IAM Identity Center instance, you add users and groups in the IAM Identity Center console. Then, during the
application creation process, Amazon Q Business automatically
detects—and connects to—your already configured IAM Identity Center instance. You
add Amazon Q Business subscriptions to your IAM Identity Center users in the Amazon Q Business console.

Or, you can create an IAM Identity Center instance from within the Amazon Q Business
console during the [Amazon Q Business application creation
process](create-application.md "create-application.md"). If you choose this option, keep in mind that you can only
create and add users to your application using this method. You can add groups
you’ve already created in your IAM Identity Center instance, but can’t create them. All groups
need to be created from the IAM Identity Center console.

Amazon Q Business supports same-region IAM Identity Center and Amazon Q Business
integrations for both organization and account level instances.

## Creating a cross-region integration

Amazon Q Business, including Amazon Q Apps, can also integrate with IAM Identity Center in
any [commercial region
where IAM Identity Center is available](../../../general/latest/gr/sso.md "../../../general/latest/gr/sso.md") (excluding opt-in and special regions), even if
that region isn’t one of the [regions supported by Amazon Q Business](quotas-regions.md#regions "quotas-regions.md#regions"). You
can choose to create a cross-region integration if you already have an IAM Identity Center
instance configured in a region that Amazon Q Business isn’t currently
available in.

When you create a cross-region Amazon Q Business and IAM Identity Center-integration, you
enable Amazon Q Business to make cross-region calls in order to access and
store information from your IAM Identity Center instance, such as user and group attributes. This
functionality allows Amazon Q Business to support IAM Identity Center-enabled applications
in regions different from where your IAM Identity Center instance is ingested. When you create a
cross-region integration, your Amazon Q Business application will have access
to user and group information from an IAM Identity Center instance deployed in a different region.
In these cross-region calls, Amazon Q Business might send the following user
attributes:

- Email address
- Account in AWS Organizations
- User ID
- Group name
- Group ID

###### Important

Amazon Q Business supports cross-region IAM Identity Center and Amazon Q Business integrations only for organization level instances. Amazon Q Business
doesn't support cross-region IAM Identity Center integrations for account level instances. For
more information on IAM Identity Center instance types and their use cases, see [Understanding types of IAM Identity Center instances](setting-up.md#idc-instance-types "setting-up.md#idc-instance-types").

If you create a cross-region integration between an Amazon Q Business
application and an IAM Identity Center instance, you may experience higher latency when using
Amazon Q Business due to the increased overhead of making cross-region
calls. The increase in latency will be proportional to the distance of the Amazon Q Business region from the IAM Identity Center region you're using. We recommend
performing latency tests for your specific user case. We don't recommend using this
feature if you have more than 100 groups per user in your IAM Identity Center instance.

When you create a cross-region IAM Identity Center and Amazon Q Business integration, any
Amazon Q Business indices associated with your application are billed in
the Amazon Q Business region they're created in. User subscriptions for an
Amazon Q Business application using a cross-region IAM Identity Center integration are
billed in the region the IAM Identity Center instance is created in. For more information on
pricing, see [Amazon Q Business Pricing](https://aws.amazon.com/q/business/pricing "https://aws.amazon.com/q/business/pricing").

Once you opt-in, you will see the option to create a cross-region connection
during the [Amazon Q Business application creation
process](create-application.md "create-application.md"), as in the following image:

![An console screenshot of the cross-region IDC enabling option.](images/cross-region-idc.png)
