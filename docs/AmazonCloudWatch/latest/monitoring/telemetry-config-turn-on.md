# Turning on telemetry auditing

Use the CloudWatch console to configure telemetry for your AWS account or organization. For an
organization, CloudWatch uses a management account or a delegated administrator account to discover
AWS resources and configure telemetry for all of the member accounts in the
organization.

Telemetry config remains active until you turn it off. For more information, see [Turning off CloudWatch telemetry configuration](telemetry-config-turn-off.md "telemetry-config-turn-off.md").

###### Topics

- [Create a telemetry configuration](#configure-telemetry-collection "#configure-telemetry-collection")
- [Configuring telemetry for your
  organization](#telemetry-config-organization "#telemetry-config-organization")
- [Configuring telemetry for your
  account](#telemetry-config-turn-on-account "#telemetry-config-turn-on-account")
- [Enable telemetry for resources](#enable-telemetry-for-resources "#enable-telemetry-for-resources")
- [Deregistering a delegated
  administrator account](#telemetry-config-deregister-administrator "#telemetry-config-deregister-administrator")
- [Turning off trusted access for
  AWS Organizations](#telemetry-config-turn-off-trusted-access "#telemetry-config-turn-off-trusted-access")

## Create a telemetry configuration

Configure telemetry collection to monitor your AWS resources.

### Prerequisites

- You have permissions to configure CloudWatch telemetry
- You've identified the AWS resources you want to monitor

###### To create a telemetry configuration

1. Open the AWS Management Console.
2. In the navigation pane, choose **CloudWatch**, then choose **Telemetry
   Config**.
3. Choose **Configure telemetry**.
4. On the **Specify scope** page:
   1. Choose the scope for your configuration (account or organization).
   2. (Optional) Add tags to your configuration.

5. Choose **Next**.
6. On the **Specify telemetry destination** page:
   1. Choose a destination for your telemetry data (for example, CloudWatch Logs).
   2. Enter a prefix for your log group names.
   3. (Optional) Configure additional settings:
      - Enable evaluation metrics
      - Set sample percentage

   4. Choose data identifiers to mask sensitive information.

7. Choose **Next**.
8. Review your configuration settings.
9. Choose **Create telemetry configuration**.

After you complete these steps, CloudWatch begins collecting telemetry based on your
configuration.

## Configuring telemetry for your

organization

To configure telemetry for your organization, you must use a management account or a
delegated administrator account. CloudWatch uses this account to discover your organization's AWS
resources and configure their telemetry.

Before you can configure telemetry for your organization, you need to enable trusted access
between AWS Organizations and CloudWatch. When you enable trusted access, CloudWatch creates a service-linked role
named **AWSServiceRoleForObservabilityAdmin** to support resource and telemetry
configuration discovery for the organization. The role is created in all member accounts of the
organization. For more information about the service-linked role, see [Service-linked role
permissions for CloudWatch telemetry config](using-service-linked-roles.md#service-linked-role-telemetry-config "using-service-linked-roles.md#service-linked-role-telemetry-config"). For more information about AWS Organizations,
see [Amazon CloudWatch and
AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

To use a management account with Telemetry config, log in with the account, enable trusted
access, and then configure telemetry. For more information, see [Configuring telemetry for your
organization](#telemetry-config-turn-on-organization "#telemetry-config-turn-on-organization").

###### To configure telemetry for your organization

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pain, choose **Settings**.
3. Choose the **Organizations** tab.
4. On the **CloudWatch** settings page, in the **Organizational settings
   management** pane, choose **Enable trusted access**. The **Enable trusted
   access** page appears.

To review the role policy, choose **View permission details** and the
role policy appears in a window. Confirm that you want to provide these permissions to the management account by choosing **Enable trusted access**. 5. Under **Manage Settings**, in the **CloudWatch Telemetry
config** pane choose **Turn on**. 6. After Telemtry config is turned on for the organization a notification appears. On the notification, choose Go to Telemetry config. The
The **Telemetry config** page appears and CloudWatch begins discovering
AWS resources in the organization. As CloudWatch discovers resources, it updates information on
the **Telemetry config** page.

###### Note

The time delay before resources appear on the **Telemetry config** page depends
on the number of member accounts and resources in your organization or account.

### Registering a delegated administrator

account for your organization

A delegated administrator account is a member account that shares administrator access for
service-managed permissions. The account that you register as a delegated administrator must be
in your organization. A delegated administrator account for your organization can be used
outside of CloudWatch, so make sure that you understand this account type before you follow this
procedure. For more information, see [Amazon CloudWatch and
AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

To remove or change the delegated administrator account, deregister the account first. For
more information, see [Deregistering a delegated
administrator account](#telemetry-config-deregister-administrator "#telemetry-config-deregister-administrator").

###### To register a delegated administrator account

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Organization** tab.
4. In the **Organizational settings management** pane, choose **Register delegated administrator**.
5. In the **Register delegated administrator** dialog, for
   **Delegated administrator account ID**, enter the 12-digit account ID for
   an organization member account.
6. Choose **Register delegated administrator**. At the top of the **CloudWatch seettings** page, a
   message appears indicating the account was registered successfully. To see information about the
   delegated administrator account, select the number below **Delegated
   administrators**.

### Configuring telemetry for your

organization

Configure telemetry for AWS Organizations to monitor the telemetry for the AWS resources across
all your member accounts. This also configures the telemetry for individual accounts. You can
also configure telemetry for only your account. For more information, see [Configuring telemetry for your
account](#telemetry-config-turn-on-account "#telemetry-config-turn-on-account").

You can disable trusted access across all your member accounts. For more information, see
[Turning off trusted access for
AWS Organizations](#telemetry-config-turn-off-trusted-access "#telemetry-config-turn-off-trusted-access").

###### To configure telemetry for your organization

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. Choose **Configure**, and then choose the
   **Organization** tab. The telemetry conﬁg **Overview**
   page appears and CloudWatch begins discovering AWS resources in your organization. As CloudWatch
   discovers resources, it updates information in the **Overview** page.

###### Note

The delay before resources appear on the **Overview** page depends on
the number of member accounts and resources in your organization.

## Configuring telemetry for your

account

Configure telemetry for your AWS account to monitor telemetry for the AWS resources in
that account. If you have an organization in AWS Organizations, configure telemetry for your organization
instead. For more information, see [Configuring telemetry for your
organization](#telemetry-config-turn-on-organization "#telemetry-config-turn-on-organization").

###### To configure telemetry for your AWS account

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. Choose **Configure**, then **This account**, if you are
   using a management account or a delegated administrator account. The telemetry configuration
   **Overview** page appears and CloudWatch begins discovering AWS resources in
   your account. As CloudWatch discovers resources, it updates information on the
   **Overview** page.

###### Note

The delay before resources appear on the **Overview** page depends on
the number of resources in your account.

## Enable telemetry for resources

After configuring telemetry for your account or organization, you can enable telemetry
collection for specific AWS resources.

### Prerequisites

- You have completed the initial telemetry configuration
- You have identified the specific resources you want to monitor

###### To enable telemetry for resources

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. Choose **Enable telemetry**.
4. On the **Select resources** page:
   1. Choose the resource types you want to monitor (for example, Amazon EC2, Lambda,
      Amazon VPC).
   2. (Optional) Use filters to narrow down the resources displayed.

5. Choose **Next**.
6. On the **Configure data events** page:
   1. For each resource type, select the data events you want to collect.
   2. (Optional) Review existing trails to avoid duplicate logging.

7. Choose **Next**.
8. On the **Set sampling rates** page:
   1. Use the slider or enter a percentage to set the sampling rate.
   2. (Optional) Adjust rates for individual resource types if needed.

9. Review your settings.
10. Choose **Enable telemetry**.

After completing these steps, CloudWatch begins collecting telemetry for the selected
resources.

## Deregistering a delegated

administrator account

Deregister the delegated administrator account before turning off trusted access for
AWS Organizations. You can also deregister a delegated administrator account if it no longer has access
to the appropriate AWS resources for telemetry configuration or to choose a different member
account to be the delegated administrator. This account will not be able to perform account
management tasks for AWS Organizations. For more information, see [Amazon CloudWatch and
AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

###### To deregister the delegated administrator account

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. On the **Organization** tab, choose
   **Deregister**.
4. On the **Deregister delegated administrator** page, choose
   **Deregister**.

To register an account as a delegated administrator, see [Registering a delegated administrator
account for your organization](#telemetry-config-register-administrator "#telemetry-config-register-administrator").

## Turning off trusted access for

AWS Organizations

Trusted access extends the functionality of the management account in AWS Organizations to other
AWS services. When you turn off trusted access, trusted access between your organization and
all AWS services—not just CloudWatch—will stop.

If you no longer want trusted access turned on for your organization, you can turn it off.
For more information, see [Amazon CloudWatch and
AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

###### Note

Before turning off trusted access for an organization, deregister the delegated
administrator account. For more information, see [Deregistering a delegated
administrator account](#telemetry-config-deregister-administrator "#telemetry-config-deregister-administrator").

###### To turn off trusted access for AWS Organizations

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Organization** tab.
4. In the **Organizational Management Settings** section, select
   **Turn off**.
