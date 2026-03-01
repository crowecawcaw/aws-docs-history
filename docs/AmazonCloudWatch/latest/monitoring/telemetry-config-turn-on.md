# Turning on telemetry auditing and configuration

Use the CloudWatch console to audit and configure telemetry for your AWS account or
organization. For an organization, as a AWS organization management account or a CloudWatch delegated
administrator account, CloudWatch discovers AWS resources and provides visibility into the telemetry
configurations across all the member accounts in the organization.

Telemetry config remains active until you turn it off. For more information, see [Turning off CloudWatch telemetry configuration](telemetry-config-turn-off.md "telemetry-config-turn-off.md").

###### Topics

- [Configuring Telemetry Auditing Feature for your organization](#telemetry-config-organization "#telemetry-config-organization")
- [Configuring Telemetry Auditing Feature for your account](#telemetry-config-turn-on-account "#telemetry-config-turn-on-account")
- [Deregistering a delegated administrator account](#telemetry-config-deregister-administrator "#telemetry-config-deregister-administrator")
- [Turning off trusted access for AWS Organizations](#telemetry-config-turn-off-trusted-access "#telemetry-config-turn-off-trusted-access")

## Configuring Telemetry Auditing Feature for your organization

To turn on telemetry auditing and configuration experience for your organization, you must
use a AWS Organization management account or a delegated administrator account. CloudWatch uses this
account to discover your organization's AWS resources and configure their telemetry.

Before you can configure telemetry for your organization, you need to enable trusted access
between AWS Organizations and CloudWatch. When you enable trusted access, CloudWatch creates a service-linked role
named **AWSServiceRoleForObservabilityAdmin** to support resource and telemetry
configuration discovery for the organization. The role is created in all member accounts of the
organization. For more information about the service-linked role, see [Service-linked role permissions for CloudWatch telemetry config](using-service-linked-roles.md#service-linked-role-telemetry-config "using-service-linked-roles.md#service-linked-role-telemetry-config"). For more information about AWS Organizations,
see [Amazon CloudWatch and
AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

###### To turn on telemetry auditing for your organization

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pain, choose **Settings**.
3. Choose the **Organizations** tab.
4. On the **CloudWatch** settings page, in the **Organizational settings
   management** pane, choose **Enable trusted access**. The
   **Enable trusted access** page appears.

To review the role policy, choose **View permission details** and the
role policy appears in a window. Confirm that you want to provide these permissions to the
management account by choosing **Enable trusted access**. 5. Under **Manage Settings**, in the **Organizations tab**
in the **CloudWatch Telemetry Config** block choose **Turn on**. 6. After Telemetry config is turned on for the organization, a notification appears. On the
notification, choose Go to Telemetry config. The Telemetry Configuration experience can be
accessed in the **Ingestion** page and CloudWatch begins discovering AWS
resources in the organization. As CloudWatch discovers resources, it updates information on the
**Telemetry config** page.

###### Note

The time delay before resources appear on the **Telemetry config** page
depends on the number of member accounts and resources in your organization or
account.

### Registering a delegated administrator account for your organization

A delegated administrator account is a member account that shares administrator access for
service-managed permissions. The account that you register as a delegated administrator must be
in your organization. A delegated administrator account for your organization can be used
outside of CloudWatch, so make sure that you understand this account type before you follow this
procedure. For more information, see [Amazon CloudWatch and
AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

To remove or change the delegated administrator account, deregister the account first. For
more information, see [Deregistering a delegated administrator account](#telemetry-config-deregister-administrator "#telemetry-config-deregister-administrator").

###### To register a delegated administrator account

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Organization** tab.
4. In the **Organizational settings management** pane, choose
   **Register delegated administrator**.
5. In the **Register delegated administrator** dialog, for
   **Delegated administrator account ID**, enter the 12-digit account ID for
   an organization member account.
6. Choose **Register delegated administrator**. At the top of the
   **CloudWatch settings** page, a message appears indicating the account was
   registered successfully. To see information about the delegated administrator account, select
   the number below **Delegated administrators**.

### Configuring Telemetry Auditing Feature for your organization

Configure telemetry for AWS Organizations to monitor the telemetry for the AWS resources across
all your member accounts. This also configures the telemetry for individual accounts. You can
also configure telemetry for only your account. For more information, see [Configuring Telemetry Auditing Feature for your account](#telemetry-config-turn-on-account "#telemetry-config-turn-on-account").

You can disable trusted access across all your member accounts. For more information, see
[Turning off trusted access for AWS Organizations](#telemetry-config-turn-off-trusted-access "#telemetry-config-turn-off-trusted-access").

###### To configure telemetry auditing for your organization

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Ingestion**.
3. Choose **Data Sources Tab**, and then choose the
   **Enable Resources Discovery Button**. CloudWatch begins discovering AWS
   resources in your organization. As CloudWatch discovers resources, it updates information in the
   **Overview** page.

###### Note

The delay before resources appear on the **Overview** page depends on
the number of member accounts and resources in your organization.

## Configuring Telemetry Auditing Feature for your account

Configure telemetry for your AWS account to monitor telemetry for the AWS resources in
that account. If you have an organization in AWS Organizations, configure telemetry for your organization
instead. For more information, see [Configuring Telemetry Auditing Feature for your organization](#telemetry-config-turn-on-organization "#telemetry-config-turn-on-organization").

###### To configure telemetry for your AWS account

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. Choose the **Data Source** tab, and then select **Enable
   Resource Discovery**. CloudWatch begins discovering AWS resources in your account. As
   CloudWatch discovers resources, it updates information on the **Overview**
   page.

###### Note

The delay before resources appear on the **Overview** page depends on
the number of resources in your account.

## Deregistering a delegated administrator account

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

To register an account as a delegated administrator, see [Registering a delegated administrator account for your organization](#telemetry-config-register-administrator "#telemetry-config-register-administrator").

## Turning off trusted access for AWS Organizations

Trusted access extends the functionality of the management account in AWS Organizations to other
AWS services. When you turn off trusted access, trusted access between your organization and
all AWS services—not just CloudWatch—will stop.

If you no longer want trusted access turned on for your organization, you can turn it off.
For more information, see [Amazon CloudWatch and
AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

###### Note

Before turning off trusted access for an organization, deregister the delegated
administrator account. For more information, see [Deregistering a delegated administrator account](#telemetry-config-deregister-administrator "#telemetry-config-deregister-administrator").

###### To turn off trusted access for AWS Organizations

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Organization** tab.
4. In the **Organizational Management Settings** section, select
   **Turn off**.
