# Aggregated reports

Aggregated self-service reporting (SSR) provides you a view of existing self-service reports aggregated at the organization level, cross-account. This gives you visibility
into key operational metrics, like patch compliance, backup coverage, and incidents, across all the accounts under AMS management within your AWS Organizations.

Aggregated SSR is available across all commercial AWS Regions where AWS Managed Services is available. For a full list of available Regions, see the
[Region table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

## Enable aggregated reports

You must manage aggregated SSR from an AWS Organizations [management account](../../../organizations/latest/userguide/orgs-manage_accounts_management.md "../../../organizations/latest/userguide/orgs-manage_accounts_management.md").
The management account is the AWS account that you used to create your organization.

To enable Aggregated SSR for an AWS Organizations management account that's onboarded to AMS, access your AMS console and navigate to **Reports**. Select
**Organization Access** in the top-right-hand corner to open the
[AWS Managed Services Console: Organization View](https://console.aws.amazon.com/managedservices/organization-access "https://console.aws.amazon.com/managedservices/organization-access") pane.
From this pane, you can manage the Aggregated SSR functionality.

AWS Organizations management accounts that aren't onboarded to AMS don't have access to the AMS console. To enable Aggregated SSR for an AWS Organizations management account that is not onboarded to AMS, first authenticate to your AWS account, then navigate to the
[AWS console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and search for **Managed Services**.
This opens the AMS Marketing page. On this page, select the **Organization Access** link in the navigation bar to open the AWS Managed Services console: Organization View, where you can manage the Aggregated SSR functionality.

The first time you access the [AWS Managed Services Console: Organization View](https://console.aws.amazon.com/managedservices/organization-access "https://console.aws.amazon.com/managedservices/organization-access"), complete the following steps:

1. If you have not already set up AWS Organizations, choose **Enable AWS Organizations** from your console. For additional information on setting up AWS Organizations, see the _[AWS Organizations User Guide](../../../organizations/latest/userguide/orgs_getting-started.md "../../../organizations/latest/userguide/orgs_getting-started.md")_. You can skip this step if you already use AWS Organizations.
2. To enable the Aggregated Self-Service Reporting service. select **Enable trusted access**
   on the console.
3. (Optional) Register a Delegated Administrator to have read access for the organizational view.

## View aggregated reports as a delegated administrator

A delegated administrator is the account you choose to have read access to the aggregated reports. The delegated administrator must be an account onboarded to
AMS and be the only account that has read access to aggregated reports.

To choose a delegated administrator, enter the account ID in Step 3 on the AWS Managed Services Console: Organization View. You can have only one delegated administrator
account registered at a time. Note that the delegated administrator account must be an AMS-managed account.

To update a delegated administrator account, navigate to the [AWS Managed Services Console: Organization View](https://console.aws.amazon.com/managedservices/organization-access "https://console.aws.amazon.com/managedservices/organization-access")
and select **Remove the Delegated Administrator**. The console prompts you to insert a new account ID to register as the delegated administrator.

## Read aggregated reports

If you don't register a delegated administrator, and your AWS Organizations management account is onboarded to AMS, then the AWS Organizations management account
gets read access to the aggregated reports by default. If the AWS Organizations management account is not managed by AMS, then you must choose a delegated administrator account
to have read access to the aggregated reports.

At any time, only a single account onboarded to AMS has read access to the aggregated reports, either the AWS Organizations management account or the registered delegated administrator.
All other member accounts within your organization (and onboarded to AMS) still have access only to single-account reports for each individual account.

After you enable Aggregated SSR, navigate to your [**Reports**](https://console.aws.amazon.com/managedservices/ "https://console.aws.amazon.com/managedservices/").
All your existing self-service reports are listed in this section, and a blue tag indicates that they have been aggregated.
Note that you must access the AMS console from the account that you chose to have read access to the aggregated reports. This is either
the AWS Organizations management account or the delegated administrator account.

After you enable Aggregated SSR, aggregated reports are available from the next reporting cycle onward.

## Disable aggregated reports

To disable Aggregated SSR, open the [AWS Managed Services Console: Organization View](https://console.aws.amazon.com/managedservices/organization-access "https://console.aws.amazon.com/managedservices/organization-access").
Select **Disable trusted access**. After you disable trusted access for Aggregated SSR, your AMS self-service reports
stop being aggregated at the organization level, across accounts. Also note that deactivation takes effect from the next reporting cycle onwards.

After disabling Aggregated SSR, there is a wait before the reports in your AMS console appear as single-account reports. This delay occurs because the feature
deactivation takes effect from the next reporting cycle onwards.
