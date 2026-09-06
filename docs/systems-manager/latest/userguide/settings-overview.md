

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Adjusting Systems Manager settings
<a name="settings-overview"></a>

The options on the **Settings** pages enable and configure features in the Systems Manager unified console. The options displayed depend on the account you are logged into and whether you have already set up Systems Manager. 

**Note**  
The options on the **Settings** page don't affect Systems Manager tools (formerly called capabilities).

## Account setup settings
<a name="settings-acccount-setup"></a>

If Systems Manager is enabled, the **Account setup** page shows the option to **Disable Systems Manager** if either of the following is true: your account is not a member of Organizations, or the delegated administrator has not added your Organizations account to Systems Manager. Disabling Systems Manager means Systems Manager doesn't display the unified console. All Systems Manager tools still function.

## Organizational setup settings
<a name="settings-organizational-setup"></a>

On the **Organizational setup** tab, the **Home Region** section displays the AWS Region chosen as the home Region during setup. In multi-account and multi-Region environments that use AWS Organizations, Systems Manager automatically aggregates node data from all accounts and Regions to the home Region. Aggregating data in this way lets you view node data across accounts and Regions in a single location. 

**Note**  
If you want to change the home Region, you must disable Systems Manager and enable it again. To disable Systems Manager, choose **Disable**.

The **Organizational setup** section displays the AWS organizational units and AWS Regions chosen during setup. To change which organizational units and Regions display node data in Systems Manager, choose **Edit**. For more information about setting up Systems Manager for Organizations, see [Setting up AWS Systems Manager](systems-manager-setting-up-console.md).

## Feature configurations
<a name="settings-feature-configurations"></a>

The **Feature configurations** section lets you enable and configure key Systems Manager capabilities that enhance node management across your organization. These features work together to provide automated management, compliance monitoring, and maintenance of your managed nodes.

You can configure these features during initial Systems Manager setup or modify them later through the Settings page. Each feature can be enabled or disabled independently based on your organization's requirements.

### Default Host Management Configuration
<a name="settings-default-host-management-configuration"></a>

Default Host Management Configuration (DHMC) automatically configures Amazon Elastic Compute Cloud (Amazon EC2) instances in your organization to be managed by Systems Manager. When enabled, DHMC ensures that new and existing EC2 instances have the necessary AWS Identity and Access Management (IAM) permissions and configurations to communicate with Systems Manager services.

DHMC provides the following benefits:
+ **Automatic IAM role assignment** – Ensures EC2 instances have the required IAM roles and policies to function as managed nodes.
+ **Drift remediation** – Automatically corrects configuration drift when instances lose their managed node status.
+ **Simplified onboarding** – Reduces manual configuration steps for new instances.
+ **Consistent configuration** – Maintains uniform settings across your EC2 fleet.

#### Configuring drift remediation frequency
<a name="dhmc-drift-remediation"></a>

Drift remediation automatically detects and corrects when EC2 instances lose their managed node configuration. You can configure how frequently Systems Manager checks for and remediates configuration drift.

**To configure Default Host Management Configuration**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Settings**.

1. In the **Feature configurations** section, locate **Default Host Management Configuration**.

1. To enable DHMC, turn on the toggle switch.

1. For **Drift remediation frequency**, choose how often you want Systems Manager to check for and remediate configuration drift:
   + **Daily** - Checks and remediates drift once per day
   + **Weekly** - Checks and remediates drift once per week
   + **Monthly** - Checks and remediates drift once per month

1. Choose **Save**.

**Note**  
When you enable DHMC, Systems Manager creates the necessary IAM roles and policies in your account. These roles allow EC2 instances to communicate with Systems Manager services. For more information about the IAM roles created by DHMC, see [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md).

### Inventory metadata collection
<a name="settings-inventory-metadata-collection"></a>

Inventory metadata collection automatically gathers detailed information about your managed nodes, including installed applications, network configurations, system updates, and other system metadata. This information helps you maintain compliance, perform security analysis, and understand your infrastructure composition.

Inventory collection provides the following benefits:
+ **Compliance monitoring** – Track installed software and configurations for compliance reporting.
+ **Security analysis** – Identify outdated software and potential security vulnerabilities.
+ **Asset management** – Maintain an up-to-date inventory of your infrastructure.
+ **Query capabilities** – Use collected data with Amazon Q Developer for natural language queries.

#### Types of inventory data collected
<a name="inventory-collection-types"></a>

When inventory metadata collection is enabled, Systems Manager collects the following types of information from your managed nodes:
+ **Applications** - Installed software packages and applications
+ **Network configurations** - Network interfaces, IP addresses, and network settings
+ **System updates** - Installed patches and available updates
+ **System properties** - Hardware specifications, operating system details, and system configurations
+ **Services** - Running services and their configurations

#### Configuring inventory collection frequency
<a name="configuring-inventory-collection"></a>

You can configure how frequently Systems Manager collects inventory metadata from your managed nodes. More frequent collection provides more up-to-date information but may increase AWS service usage.

**To configure inventory metadata collection**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Settings**.

1. In the **Feature configurations** section, locate **Inventory metadata collection**.

1. To enable inventory collection, turn on the toggle switch.

1. For **Collection frequency**, choose how often you want Systems Manager to collect inventory data:
   + **Daily** - Collects inventory data once per day
   + **Weekly** - Collects inventory data once per week
   + **Monthly** - Collects inventory data once per month

1. Choose **Save**.

**Important**  
Inventory collection requires managed nodes to have the necessary permissions to gather system information. Make sure your managed nodes have the appropriate IAM roles and policies. For more information about required permissions, see [AWS Systems Manager Inventory](systems-manager-inventory.md).

### SSM Agent updates
<a name="settings-ssm-agent-updates"></a>

Automatic SSM Agent updates make sure that your managed nodes are running the latest version of the SSM Agent. Keeping the agent up-to-date provides access to the latest features, security improvements, and bug fixes.

SSM Agent automatic updates provide the following benefits:
+ **Latest features** - Access to new Systems Manager capabilities and improvements
+ **Security updates** - Automatic installation of security patches and fixes
+ **Improved reliability** - Bug fixes and stability improvements
+ **Reduced maintenance** - Eliminates the need for manual agent updates

#### Configuring automatic agent updates
<a name="configuring-agent-updates"></a>

You can configure how frequently Systems Manager checks for and installs SSM Agent updates on your managed nodes. Regular updates help ensure optimal performance and security.

**To configure SSM Agent updates**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Settings**.

1. In the **Feature configurations** section, locate **SSM Agent updates**.

1. To enable automatic updates, turn on the toggle switch.

1. For **Update frequency**, choose how often you want Systems Manager to check for and install agent updates:
   + **Daily** - Checks for updates once per day
   + **Weekly** - Checks for updates once per week
   + **Monthly** - Checks for updates once per month

1. Choose **Save**.

## Diagnose and remediate settings
<a name="settings-diagnose-and-remediate"></a>

The **Diagnose and remediate** settings determine whether Systems Manager automatically scans your nodes to make sure they can communicate with Systems Manager. If enabled, the feature runs automatically according to a schedule you define. The feature identifies which nodes can't connect to Systems Manager and why. This feature also provides recommended runbooks for remediating networking issues and other problems preventing nodes from being configured as managed nodes.

### Scheduling a recurring diagnostic scan
<a name="settings-diagnose-and-remediate-schedule-diagnostic-run"></a>

Systems Manager can diagnose and help you remediate several types of deployment failures, as well as drifted configurations. Systems Manager can also identify Amazon Elastic Compute Cloud (Amazon EC2) instances in your account or organization that Systems Manager can't treat as a *managed node*. The EC2 instance diagnosis process can identify issues related to misconfigurations for a virtual private cloud (VPC), in a Domain Name Service (DNS) setting, or in an Amazon Elastic Compute Cloud (Amazon EC2) security group. 

To simply the task of identifying nodes that can't connect to Systems Manager, the **Schedule recurring diagnosis** feature lets you automate a recurring diagnostic scan. The scans help identify which nodes can't connect to Systems Manager and why. Use the following procedure to enable and configure a recurring diagnostic scan of your nodes.

**To schedule a recurring diagnostic scan**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Settings**, and then choose the **Diagnose and remediate** tab.

1. Turn on the **Schedule recurring diagnosis** option.

1. For **Scanning period**, choose how often you want the scan to run.

1. (Optional) For **Start time**, enter a time, in 24-hour format, for the diagnosis to begin. For example, for 8:15 PM, enter **20:15**.

   The time you enter is for your current local time zone.

   If you don't specify a time, the diagnostic scan runs immediately. Systems Manager also schedules the scan to run in the future at the current time. If you specify a time, Systems Manager waits to run the diagnostic scan at the specified time.

1. Choose **Save**.

1. After the scan completes, view the details by choosing **Diagnose and remediate** in the left navigation.

For more information about the **Diagnose and remediate** feature, see [Diagnosing and remediating](diagnose-and-remediate.md).

### Updating S3 bucket encryption
<a name="settings-diagnose-and-remediate-encryption"></a>

When you onboard Systems Manager, Quick Setup creates an Amazon Simple Storage Service (Amazon S3) bucket in the delegated administrator account for AWS Organizations setups. For single-account setups, the bucket is stored in the account being set up. This bucket is used to store the metadata generated during diagnostic scans. 

For more information about setting up the unified Systems Manager console, see [Setting up AWS Systems Manager](systems-manager-setting-up-console.md).

By default, your data in the bucket is encrypted using a AWS Key Management Service (AWS KMS) key that AWS owns and manages for you. 

You can choose to use a different AWS KMS key for your bucket encryption. As another alternative, you can use server-side encryption with AWS KMS keys (SSE-KMS) using a customer managed key (CMK). For information, see [Working with Amazon S3 buckets and bucket policies for Systems Manager](systems-manager-diagnosis-metadata-bucket.md).

**To use a different AWS KMS key for S3 bucket encryption**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Settings**, and then choose the **Diagnose and remediate** tab.

1. In the **Update S3 bucket encryption** area, choose **Edit**.

1. Select the **Customize encryption settings (advanced)** check box.

1. For **Choose an AWS KMS key**, choose or enter the Amazon Resource Name (ARN) of the key.
**Tip**  
To create a new key, choose **Create an AWS KMS key**.

1. Choose **Save**.