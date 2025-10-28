**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# View aggregated data about cluster resources with the EKS Dashboard

## What is the Amazon EKS Dashboard?

The Amazon EKS Dashboard provides consolidated visibility into your Kubernetes clusters across multiple AWS Regions and AWS Accounts. With this dashboard, you can:

- Track clusters scheduled for end-of-support auto-upgrades within the next 90 days.
- Project EKS control plane costs for clusters in extended support.
- Review clusters with insights that need attention before upgrading.
- Identify managed node groups running specific AMI versions.
- Monitor cluster support type distribution (standard compared to extended support).

The EKS dashboard integrates with EKS Cluster Insights to surface issues with your clusters, such as use of deprecated Kubernetes APIs. For more information, see [Prepare for Kubernetes version upgrades and troubleshoot misconfigurations with cluster insights](cluster-insights.md "cluster-insights.md").

###### Note

The EKS Dashboard is not real-time and updates every 12 hours. For real-time cluster monitoring, see [Monitor your cluster performance and view logs](eks-observe.md "eks-observe.md")

## How does the dashboard use AWS Organizations?

The Amazon EKS dashboard requires AWS Organizations integration for functionality. It leverages AWS Organizations to securely gather cluster information across accounts. This integration provides centralized management and governance as your AWS infrastructure scales.

If AWS Organizations isn’t enabled for your infrastructure, see the AWS
[Organizations User Guide](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") for setup instructions.

### Cross-region and cross-account access

The EKS Dashboard can see cluster resources in any account that is a member of the AWS organization. To generate a list of AWS accounts in your organization, see [Export details for all accounts in an organization](../../../organizations/latest/userguide/orgs_manage_accounts_export.md "../../../organizations/latest/userguide/orgs_manage_accounts_export.md").

The us-east-1 AWS region generates the dashboard. You must log in to this region to see the dashboard. The dashboard aggregates data across AWS regions, but this does not include `GovCloud` or China regions.

### Key terms

- **AWS Organization**: A unified management structure for multiple AWS accounts.
- **Management account**: The primary account that controls the AWS Organization.
- **Member account**: Any account within the organization except the management account.
- **Delegated administrator**: A member account granted specific cross-account administrative permissions. Within the management account, you can select one delegated administrator account per AWS Service.
- **Trusted access**: Authorization for the EKS Dashboard to access cluster information across organizational accounts.
- **Service-Linked Role (SLRs)**: A unique type of IAM role directly linked to an AWS service. The EKS Dashboard uses a SLR to read information about your accounts and organizations.
- For more information, see [Terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the AWS Organizations User Guide.

### General overview

1. Access the management account of your AWS Organization.
   - The steps to access the management account depend on how you have configured your AWS Organization. For example, you might access the management account via AWS
     [Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/") or [Okta](https://www.okta.com/partners/aws/ "https://www.okta.com/partners/aws/").

2. Enable Trusted access through the EKS Console.
3. Assign a Delegated administrator using their AWS Account ID.
4. Switch to the Delegated administrator account.
5. Access the enhanced EKS Console with organization-wide visibility.

## Enable the EKS Dashboard using the AWS console

###### Important

You must be logged in to the Management Account of your AWS Organization to enable the EKS Dashboard.

### Access EKS Dashboard settings

1. Confirm the following:
   1. You have AWS Organizations enabled and configured.
   2. You are logged into the Management account of the organization.
   3. You are viewing the AWS Management Console in the us-east-1 region.

2. Navigate to the EKS console.
3. In the left sidebar, open Dashboard Settings.

### Set up access to the Amazon EKS Dashboard

1. Find the AWS Account ID of the AWS Account you want to allow to view the EKS Dashboard.
   1. This step is optional, but suggested. If you don’t, you can only access the dashboard from the management account. As a best practice, you should limit access to the management account.

2. Click **Enable trusted access**.
   1. You can now view the dashboard from the management account.

3. Click **Register delegated administrator** and input the Account ID of the AWS Account you will use to view the dashboard.
   1. You can now view the dashboard from the delegated administrator account or the management account.

For information about permissions required to enable the dashboard, see [Minimum IAM policies required](cluster-dashboard-orgs.md#dashboard-iam-policy "cluster-dashboard-orgs.md#dashboard-iam-policy").

## View the EKS dashboard

1. Log in to the delegated administrator account (suggested) or the management account.
2. Log in to the us-east-1 region.
3. Go to the EKS service, and select Dashboard from the left sidebar.

###### Note

[Review the IAM permissions required to view the EKS dashboard.](cluster-dashboard-orgs.md#eks-dashboard-view-policy "cluster-dashboard-orgs.md#eks-dashboard-view-policy")

## Configure the dashboard

You can configure the view of the dashboard, and filter resources.

### Available resources

- **Clusters**: View aggregated information about the status and location of EKS Clusters.
  - Clusters with health issues.
  - Clusters on EKS Extended Support.
  - Breakdown of clusters by Kubernetes version.

- **Managed node groups**: Review Managed node groups and EC2 Instances.
  - Node groups by AMI type, such as Amazon Linux or Bottlerocket.
  - Node group health issues.
  - Instance type distribution.

- **Add-ons**: Learn about what Amazon EKS Add-ons you have installed, and their status.
  - Number of installations per add-on.
  - Add-ons with health issues.
  - Version distribution per add-on.

### Available views

- **Graph view**
  - A customizable widget view displaying graphs and visualizations of the selected resource.
  - Changes to the Graph view, such as removing a widget, are visible to all users of the EKS Dashboard.

- **Resource view**
  - A list view of the selected resource, supporting filters.

- **Map View**
  - View the geographic distribution of the selected resource.

### Filter the EKS dashboard

You can filter the EKS Dashboard by:

- AWS Account
- Organizational unit, defined by AWS Organizations
- AWS Region

## Disable the EKS dashboard using the AWS console

1. Confirm the following:
   1. You have AWS Organizations enabled and configured.
   2. You are logged into the Management account of the organization.
   3. You are viewing the AWS Management Console in the us-east-1 region.

2. Navigate to the EKS console.
3. In the left sidebar, open Dashboard Settings.
4. Click **Disable trusted access**.

## Troubleshoot the EKS dashboard

### Issue enabling EKS dashboard

- You must be logged in to the management account of an AWS Organization.
  - If you do not have an AWS Organization, create one. Learn how to [Create and configure an organization](../../../organizations/latest/userguide/orgs_tutorials_basic.md "../../../organizations/latest/userguide/orgs_tutorials_basic.md").
  - If your AWS account is already a member of an AWS Organization, identify the administrator of the organization.

- You must be logged in to the AWS account with sufficient IAM permissions to create and update AWS Organizations resources.

### Issue viewing the EKS dashboard

- You must be logged in to one of the following AWS accounts:
  - The management account of the AWS Organization
  - A delegated administrator account, identified in the EKS dashboard settings of the management account.

- If you’ve recently enabled the EKS Dashboard, please note that initial data population may take up to 12 hours.
- [Try re-enabling the dashboard using the CLI](cluster-dashboard-orgs.md#dashboard-enable-cli "cluster-dashboard-orgs.md#dashboard-enable-cli"), including creating the service linked role.

### Dashboard widgets move unexpectedly

- The EKS Dashboard saves the configurable widget view at the AWS Account level. If you change the widget view, other people using the same AWS account will see the changes.
