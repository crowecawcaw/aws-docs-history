# Enabling Security Lake using the console

This tutorial explains how to enable and configure Security Lake through the AWS Management Console. As part of the AWS Management Console, the Security Lake console offers a
streamlined process for getting started, and creates all necessary AWS Identity and Access Management (IAM) roles that you need to create your data lake.

## Step 1: Configure sources

Security Lake collects log and event data from a variety of sources and across your
AWS accounts and AWS Regions. Follow these instructions to identify which data you want
Security Lake to collect. You can only use these instructions to add a natively-supported
AWS service as a source. For information about adding a custom source, see [Collecting data from custom sources in Security Lake](custom-sources.md "custom-sources.md").

###### To configure log source collection

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. By using the AWS Region selector in the upper-right corner of
   the page, select a Region. You can enable Security Lake in the current
   Region and other Regions while onboarding.
3. Choose **Get started**.
4. For **Select log and event sources**, choose one of the following options
   for **Source selection**:
   1. **Ingest default AWS sources** – When
      you choose the recommended option, CloudTrail - S3 data events and AWS WAF are not included
      for ingestion by default. This is because ingesting high volume of both source types
      might significantly impact usage costs.
      To ingest these sources, first select the **Ingest specific
      AWS sources** option, and then select these sources from the
      **Log and event sources** list.
   2. **Ingest specific
      AWS sources** –
      With this option, you can select one or more log and event sources that you want to ingest.###### Note

When you enable Security Lake in an account for the first time, all the
selected log and event sources will be a part of a 15-day free trial period. For more
information about usage statistics, see
[Reviewing usage and estimated costs](reviewing-usage-costs.md "reviewing-usage-costs.md"). 5. For **Versions**, chose the version of data
source from which you want to ingest log and event sources. For more information about
versions, see [OCSF source identification](open-cybersecurity-schema-framework.md#ocsf-source-identification "open-cybersecurity-schema-framework.md#ocsf-source-identification").

###### Important

If you don't have the required role permissions to enable the new version of the AWS log
source in the specified Region, contact your Security Lake administrator.
For more information, see
[Update role permissions](internal-sources.md#update-role-permissions "internal-sources.md#update-role-permissions"). 6. For **Select Regions**, choose whether to ingest
log and event sources from all supported Regions or specific
Regions. If you choose **Specific Regions**, select
which Regions to ingest data from. 7. For **Select accounts**, perform the following steps:

    1. Choose whether Security Lake will ingest data from
     **All accounts** or **Specific
     accounts** in your organization. Security Lake will be enabled for these
     accounts with the settings you choose during this configuration.
    2. The **Automatically enable Security Lake for new organization accounts**
     checkbox is selected by default. These auto-enable settings will apply to
     AWS accounts when they join your organization. You can edit the auto-enable settings
     at any time.


    ###### Note

    The auto-enable settings will only apply to accounts when
     they join your organization, not to existing accounts. For more information,
     see [Editing new account configuration in console](multi-account-management.md#security-lake-new-account-auto-enable "multi-account-management.md#security-lake-new-account-auto-enable").

8. For **Service access**, create a new IAM role
   or use an existing IAM role that gives Security Lake permission to
   collect data from your sources and add them to your data lake. One
   role is used across all Regions in which you enable
   Security Lake.
9. Choose **Next**.

## Step 2: Define storage settings and rollup Regions (optional)

You can specify the Amazon S3 storage class in which you want Security Lake to store your data
and for how long. You can also specify a rollup Region to consolidate data from multiple
Regions. These are optional steps. For more information, see [Lifecycle management in Security Lake](lifecycle-management.md "lifecycle-management.md").

###### To configure storage and rollup settings

1. If you want to consolidate data from multiple contributing Regions
   to a rollup Region, for **Select rollup Regions**,
   choose **Add rollup Region**. Specify the rollup
   Region and the Regions that will contribute to it. You can set up
   one or more rollup Regions.
2. For **Select storage classes**, choose an Amazon S3
   storage class. The default storage class is **S3
   Standard**. Provide a retention period (in days) if you
   want the data to transition to another storage class after that
   time, and choose **Add transition**. After the retention period ends,
   the objects expire and Amazon S3 deletes them. For more
   information about Amazon S3 storage classes and retention, see [Retention management](lifecycle-management.md#retention-management "lifecycle-management.md#retention-management").
3. If you selected a rollup Region in the first step, for
   **Service access**, create a new IAM role or
   use an existing IAM role that gives Security Lake permission to
   replicate data across multiple Regions.
4. Choose **Next**.

## Step 3: Review and create data lake

Review the sources that Security Lake will collect data from, your rollup Regions, and
your retention settings. Then, create your data lake.

###### To review and create the data lake

1. While enabling Security Lake, review **Log and event sources**,
   **Regions**, **Rollup Regions**, and
   **Storage classes**.
2. Choose **Create**.

After creating your data lake, you will see the **Summary** page on
the Security Lake console. This page provides an overview of the number of **Regions**
and **Rollup Regions**, information about subscribers, and **Issues**.

The **Issues** menu shows you a summary of issues from the
last 14 days that are impacting the Security Lake service or your Amazon S3 buckets. For additional details about each issue, you can
go to the **Issues** page of the Security Lake console.

## Step 4: View and query your own data

After creating your data lake, you can use Amazon Athena or similar services to view and
query your data from AWS Lake Formation databases and tables. When you use the console, Security Lake
automatically grants database view permissions to the role that you use to enable Security Lake. At a minimum, the role must have
_Data analyst_ permissions. For more information on permission
levels, see [Lake Formation personas and IAM
permissions reference](../../../lake-formation/latest/dg/permissions-reference.md "../../../lake-formation/latest/dg/permissions-reference.md"). For instructions on granting `SELECT`
permissions, see [Granting Data
Catalog permissions using the named resource method](../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md "../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md") in the
_AWS Lake Formation Developer Guide_.

## Step 5: Create subscribers

After creating your data lake, you can add subscribers to consume your data.
Subscribers can consume data by directly accessing objects in your Amazon S3 buckets or by
querying the data lake. For more information about subscribers, see [Subscriber management in Security Lake](subscriber-management.md "subscriber-management.md").
