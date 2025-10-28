# Prerequisites for configuring

automated sensitive data discovery

Before you enable or configure settings for automated sensitive data discovery, complete the following tasks. This
helps ensure that you have the resources and permissions that you need.

To complete these tasks, you must be the Amazon Macie administrator for an organization or have a
standalone Macie account. If your account is part of an organization, only the Macie administrator for
your organization can enable or disable automated sensitive data discovery for accounts in the organization. In addition,
only the Macie administrator can configure automated discovery settings for the accounts.

###### Tasks

- [Step 1: Configure a
  repository for sensitive data discovery results](#discovery-asdd-account-configure-prereqs-sddr "#discovery-asdd-account-configure-prereqs-sddr")
- [Step 2: Verify your
  permissions](#discovery-asdd-account-configure-prereqs-perms "#discovery-asdd-account-configure-prereqs-perms")
- [Next steps](#discovery-asdd-account-configure-prereqs-next "#discovery-asdd-account-configure-prereqs-next")

## Step 1: Configure a repository for

sensitive data discovery results

When Amazon Macie performs automated sensitive data discovery, it creates an analysis record for each Amazon Simple Storage Service (Amazon S3)
object that it selects for analysis. These records, referred to as _sensitive data discovery results_, log details about the analysis of individual S3 objects. This
includes objects that Macie doesn't find sensitive data in, and objects that Macie can't analyze
due to errors or issues such as permissions settings. If Macie finds sensitive data in an
object, the sensitive data discovery result includes information about the sensitive data that Macie found. Sensitive
data discovery results provide you with analysis records that can be helpful for data privacy
and protection audits or investigations.

Macie stores your sensitive data discovery results for only 90 days. To access the results and enable long-term
storage and retention of them, configure Macie to store the results in an S3 bucket. The bucket
can serve as a definitive, long-term repository for all of your sensitive data discovery results. If you're the
Macie administrator for an organization, this includes sensitive data discovery results for member accounts that you enable
automated sensitive data discovery for.

To verify that you configured this repository, choose **Discovery
results** in the navigation pane on the Amazon Macie console. If you prefer to do this
programmatically, use the [GetClassificationExportConfiguration](../APIReference/classification-export-configuration.md "../APIReference/classification-export-configuration.md") operation of the Amazon Macie API. To learn more
about sensitive data discovery results and how to configure this repository, see [Storing and retaining
sensitive data discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").

If you configured the repository, Macie creates a folder named
`automated-sensitive-data-discovery` in the repository when you enable automated sensitive data discovery
for the first time. This folder stores sensitive data discovery results that Macie creates while performing automated discovery
for your account or organization.

If you use Macie in multiple AWS Regions, verify that you configured the repository for
each of those Regions.

## Step 2: Verify your

permissions

To verify your permissions, use AWS Identity and Access Management (IAM) to review the IAM policies that are
attached to your IAM identity. Then compare the information in those policies to the following
list of actions that you must be allowed to perform:

- `macie2:GetMacieSession`
- `macie2:UpdateAutomatedDiscoveryConfiguration`
- `macie2:ListClassificationScopes`
- `macie2:UpdateClassificationScope`
- `macie2:ListSensitivityInspectionTemplates`
- `macie2:UpdateSensitivityInspectionTemplate`

The first action allows you to access your Amazon Macie account. The second action allows you
to enable or disable automated sensitive data discovery for your account or organization. For an organization, it also
allows you to enable automated discovery automatically for accounts in your organization. The remaining
actions allow you to identify and change the configuration settings.

If you plan to review or change the configuration settings by using the Amazon Macie console,
you must also be allowed to perform the following actions:

- `macie2:GetAutomatedDiscoveryConfiguration`
- `macie2:GetClassificationScope`
- `macie2:GetSensitivityInspectionTemplate`

These actions allow you to retrieve your current configuration settings and the status of
automated sensitive data discovery for your account or organization. Permission to perform these actions is optional if
you plan to change the configuration settings programmatically.

If you're the Macie administrator for an organization, you must also be allowed to perform the
following actions:

- `macie2:ListAutomatedDiscoveryAccounts`
- `macie2:BatchUpdateAutomatedDiscoveryAccounts`

The first action allows you to retrieve the status of automated sensitive data discovery for individual accounts in
your organization. The second action allows you to enable or disable automated discovery for individual
accounts in your organization.

If you're not allowed to perform the requisite actions, ask your AWS administrator for
assistance.

## Next steps

After you complete the preceding tasks, you're ready to enable and configure the settings
for your account or organization:

- [Enabling automated sensitive data discovery](discovery-asdd-account-enable.md "discovery-asdd-account-enable.md")
- [Configuring settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md")
