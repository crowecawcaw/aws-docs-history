# Setting up telemetry configuration

Use the CloudWatch console to set up telemetry configuration for your AWS account or
organization. For an organization, as a management account or a CloudWatch delegated administrator
account, CloudWatch discovers AWS resources and provides visibility into the telemetry
configurations across all the member accounts in the organization.

Telemetry config remains active until you turn it off. For more information, see [Disabling telemetry configuration](telemetry-config-turn-off.md "telemetry-config-turn-off.md").

###### Topics

- [Prerequisites and permissions](#telemetry-config-prerequisites "#telemetry-config-prerequisites")
- [Enable telemetry configuration for your account](#telemetry-config-turn-on-account "#telemetry-config-turn-on-account")
- [Enable telemetry configuration for your organization](telemetry-config-organization.md "telemetry-config-organization.md")
- [Registering a delegated administrator account for your organization](#telemetry-config-register-administrator "#telemetry-config-register-administrator")

## Prerequisites and permissions

Telemetry configuration for your organization requires trusted access between AWS Organizations
and CloudWatch. When trusted access is enabled, CloudWatch creates a service-linked role named
**AWSServiceRoleForObservabilityAdmin** to support resource and telemetry
configuration discovery for the organization.

When you turn on telemetry configuration for your organization from a management
account, CloudWatch automatically enables trusted access and creates the service-linked role.
You do not need to set up trusted access manually before starting telemetry evaluation.

###### Important

CloudWatch uses your IAM permissions to perform this setup. It does not use CloudWatch service
permissions. In addition to the telemetry configuration permissions, you must be allowed
to perform the following actions:

- `iam:CreateServiceLinkedRole`—to create the
  **AWSServiceRoleForObservabilityAdmin** and
  **AWSServiceRoleForObservabilityAdmin\_TelemetryEnablement**
  service-linked roles.
- `organizations:EnableAWSServiceAccess`—to enable trusted access
  between AWS Organizations and CloudWatch.
  If you are not allowed to perform these actions, turning on telemetry configuration
  fails with an `AccessDeniedException`. CloudWatch does not enable trusted
  access.

The following example JSON policy grants the additional permissions required to turn on
telemetry configuration for an organization:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCreateObservabilityAdminServiceLinkedRoles",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": [
                "arn:aws:iam::*:role/aws-service-role/observabilityadmin.amazonaws.com/AWSServiceRoleForObservabilityAdmin",
                "arn:aws:iam::*:role/aws-service-role/telemetry-enablement.observabilityadmin.amazonaws.com/AWSServiceRoleForObservabilityAdmin_TelemetryEnablement"
            ],
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": [
                        "observabilityadmin.amazonaws.com",
                        "telemetry-enablement.observabilityadmin.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "AllowEnableTrustedAccessForObservabilityAdmin",
            "Effect": "Allow",
            "Action": "organizations:EnableAWSServiceAccess",
            "Resource": "*"
        }
    ]
}
```

###### Note

If you use a delegated administrator account to turn on telemetry configuration,
the service-linked role is automatically created in all member accounts but is
_not_ automatically created in the management account. In this case,
you must manually create the
**AWSServiceRoleForObservabilityAdmin** service-linked role in the
management account.

For more information about the service-linked role, see [Service-linked role permissions for CloudWatch telemetry config](using-service-linked-roles.md#service-linked-role-telemetry-config "using-service-linked-roles.md#service-linked-role-telemetry-config"). For more information about
AWS Organizations, see [Amazon CloudWatch
and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

## Enable telemetry configuration for your account

Configure telemetry for your AWS account to monitor telemetry for the AWS resources
in that account. If you have an organization in AWS Organizations, configure telemetry for your
organization instead. For more information, see [Configuring telemetry for your organization](telemetry-config-organization.md#telemetry-config-turn-on-organization "telemetry-config-organization.md#telemetry-config-turn-on-organization").

###### To configure telemetry for your AWS account

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Ingestion**.
3. Choose the **Data Source** tab, and then select **Enable
   Resource Discovery**. CloudWatch begins discovering AWS resources in your account.
   As CloudWatch discovers resources, it updates information on the **Overview**
   page.

###### Note

The delay before resources appear on the **Overview** page depends
on the number of resources in your account.

### Enabling across Regions

You can extend telemetry configuration to multiple AWS Regions from a single Region.
When you enable multi-Region support, the current Region becomes your
_home Region_. Telemetry configuration is replicated to the Regions you
select.

###### To enable telemetry configuration across Regions for your account (initial setup)

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**, and then choose
   the **Account** tab.
3. In the **CloudWatch telemetry config** section on the
   **Global** tab, the status shows **Off**.
   When multi-Region is enabled, a **Target regions** selector
   appears inline below the status.
4. Use the **All regions** toggle to include all Regions, or use
   the multiselect dropdown to choose individual Regions. The current Region is always
   included automatically and is not shown in the selector.
5. Choose **Turn on**.
6. After telemetry configuration is turned on, a **Region status**
   table appears showing the per-Region evaluation status.

###### To reconfigure Regions (telemetry already running)

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**, and then choose
   the **Account** tab.
3. In the **CloudWatch telemetry config** section, choose
   **Configure regions**. The **Target regions**
   selector appears inline, pre-populated with the currently configured Regions.
4. Modify the Region selection as needed, and then choose
   **Save**.

If you select **All regions**, new Regions are automatically included
when you opt in to them. The system periodically reconciles configuration across Regions to
correct any drift.

## Registering a delegated administrator account for your organization

A delegated administrator account is a member account that shares administrator access
for service-managed permissions. The account that you register as a delegated administrator
must be in your organization. A delegated administrator account for your organization can be
used outside of CloudWatch, so make sure that you understand this account type before you follow
this procedure. For more information, see [Amazon CloudWatch
and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

To remove or change the delegated administrator account, deregister the account first.
For more information, see [Deregistering a delegated administrator account](#telemetry-config-deregister-administrator "#telemetry-config-deregister-administrator").

###### To register a delegated administrator account

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Organization** tab.
4. In the **Organizational settings management** pane, choose
   **Register delegated administrator**.
5. In the **Register delegated administrator** dialog, for
   **Delegated administrator account ID**, enter the 12-digit account ID
   for an organization member account.
6. Choose **Register delegated administrator**. At the top of the
   **CloudWatch settings** page, a message appears indicating the account was
   registered successfully. To see information about the delegated administrator account,
   select the number below **Delegated administrators**.

### Deregistering a delegated administrator account

Deregister the delegated administrator account before turning off trusted access for
AWS Organizations. You can also deregister a delegated administrator account if it no longer has
access to the appropriate AWS resources for telemetry configuration or to choose a
different member account to be the delegated administrator. This account will not be able
to perform account management tasks for AWS Organizations. For more information, see [Amazon CloudWatch
and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

###### To deregister the delegated administrator account

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. On the **Organization** tab, choose
   **Deregister**.
4. On the **Deregister delegated administrator** page, choose
   **Deregister**.

To register an account as a delegated administrator, see [Registering a delegated administrator account for your organization](#telemetry-config-register-administrator "#telemetry-config-register-administrator").

### Turning off trusted access for AWS Organizations

Trusted access extends the functionality of the management account in AWS Organizations to
other AWS services. When you turn off trusted access, trusted access between your
organization and all AWS services—not just CloudWatch—will stop.

If you no longer want trusted access turned on for your organization, you can turn it
off. For more information, see [Amazon CloudWatch
and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md "../../../organizations/latest/userguide/services-that-can-integrate-cloudwatch.md") in the AWS Organizations User Guide.

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
