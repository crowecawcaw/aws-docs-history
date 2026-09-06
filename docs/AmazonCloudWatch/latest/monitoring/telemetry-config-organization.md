

# Enable telemetry configuration for your organization
<a name="telemetry-config-organization"></a>

To turn on telemetry configuration for your organization, you must use a AWS Organization management account or a delegated administrator account. CloudWatch uses this account to discover your organization's AWS resources and configure their telemetry.

When you turn on telemetry configuration from a management account, CloudWatch automatically sets up trusted access between AWS Organizations and CloudWatch, including creating the required service-linked role. You do not need to enable trusted access manually as a separate step. CloudWatch uses your own IAM permissions to perform this setup. You must be allowed to perform `iam:CreateServiceLinkedRole` and `organizations:EnableAWSServiceAccess`. For more information about permissions, see [Prerequisites and permissions](telemetry-config-turn-on.md#telemetry-config-prerequisites).

**To turn on telemetry auditing for your organization**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Settings**.

1. Choose the **Organizations** tab.

1. On the **CloudWatch** settings page, in the **Organizational settings management** pane, choose **Turn on**. CloudWatch automatically enables trusted access and creates the **AWSServiceRoleForObservabilityAdmin** service-linked role in your organization.

   To review the role policy, choose **View permission details**.

1. After Telemetry config is turned on for the organization, a notification appears. On the notification, choose Go to Telemetry config. The Telemetry Configuration experience can be accessed in the **Ingestion** page and CloudWatch begins discovering AWS resources in the organization. As CloudWatch discovers resources, it updates information on the **Telemetry config** page.
**Note**  
The time delay before resources appear on the **Telemetry config** page depends on the number of member accounts and resources in your organization or account.

## Configuring telemetry for your organization
<a name="telemetry-config-turn-on-organization"></a>

Configure telemetry for AWS Organizations to monitor the telemetry for the AWS resources across all your member accounts. This also configures the telemetry for individual accounts. You can also configure telemetry for only your account. For more information, see [Enable telemetry configuration for your account](telemetry-config-turn-on.md#telemetry-config-turn-on-account).

You can disable trusted access across all your member accounts. For more information, see [Turning off trusted access for AWS Organizations](telemetry-config-turn-on.md#telemetry-config-turn-off-trusted-access).

**To configure telemetry auditing for your organization**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Ingestion**.

1. Choose **Data sources**, and then choose the **Enable Resources Discovery Button**. CloudWatch begins discovering AWS resources in your organization. As CloudWatch discovers resources, it updates information in the **Overview** page.
**Note**  
The delay before resources appear on the **Overview** page depends on the number of member accounts and resources in your organization.

## Enabling across Regions
<a name="telemetry-config-org-multi-region"></a>

You can extend telemetry configuration to multiple AWS Regions from a single Region for your entire organization. When you enable multi-Region support, the current Region becomes your *home Region*. Telemetry configuration is replicated to the Regions you select for all member accounts.

**To enable telemetry configuration across Regions for your organization (initial setup)**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Settings**, and then choose the **Organizations** tab.

1. In the **CloudWatch telemetry config** section on the **Global** tab, the status shows **Off**. When multi-Region is enabled, a **Target regions** selector appears inline below the status.

1. Use the **All regions** toggle to include all Regions, or use the multiselect dropdown to choose individual Regions. The current Region is always included automatically and is not shown in the selector.

1. Choose **Turn on**.

1. After telemetry configuration is turned on, a **Region status** table appears showing the per-Region evaluation status.

**To reconfigure Regions for your organization (telemetry already running)**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Settings**, and then choose the **Organizations** tab.

1. In the **CloudWatch telemetry config** section, choose **Configure regions**. The **Target regions** selector appears inline, pre-populated with the currently configured Regions.

1. Modify the Region selection as needed, and then choose **Save**.

If you select **All regions**, new Regions are automatically included when you opt in to them. The system periodically reconciles configuration across Regions to correct any drift.