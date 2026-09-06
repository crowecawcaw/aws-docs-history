

# Migration to AWS FOCUS 1.2
<a name="migration-to-focus-1-2"></a>

## Migration Overview
<a name="migration-overview"></a>

 [FOCUS 1.2](https://focus.finops.org/) introduces additional columns and improvements to the FinOps Cost and Usage Specification. If you already have [AWS Data Exports](data-exports.md) FOCUS 1.0 enabled with the Cloud Intelligence Dashboards CloudFormation stack `CID-DataExports`, you can migrate to FOCUS 1.2 by following the steps below.

**Note**  
AWS Data Exports CloudFormation does not support in-place updates of the FOCUS table version. The migration requires temporarily disabling the FOCUS 1.0 export before enabling FOCUS 1.2.

## Prerequisites
<a name="prerequisites"></a>
+ Existing FOCUS 1.0 Data Export deployed via [AWS Data Exports](data-exports.md) CloudFormation stacks
+ Access to both the Management (Payer) Account and the Data Collection (Destination) Account

## Migration Steps
<a name="migration-steps"></a>

AWS Data Exports does not support in-place table version updates within an existing report. To migrate to FOCUS 1.2, you must first delete the existing FOCUS 1.0 report and then create a new FOCUS 1.2 report using the latest version of the CloudFormation template. The steps below walk you through this process.

### Step 1: Disable FOCUS 1.0 Export
<a name="step-1-disable-focus-1-0-export"></a>

1. Log in to your **Management (Payer)** Account.

1. Open the [CloudFormation Console](https://console.aws.amazon.com/cloudformation/home) and locate the **CID-DataExports-Source** stack.

1. Select **Update stack** → **Make a direct update** → **Use existing template** and change the **FOCUS** parameter to **No**.

1. Complete the stack update. This will temporarily delete the FOCUS 1.0 Data Export.

#### Click to see the example
<a name="focus-migration-step1-screenshot"></a>

![Disable FOCUS 1.0 Export](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/focus-migration-disable-1-0.png)


### Step 2: Enable FOCUS 1.2 Export in Source Account
<a name="step-2-enable-focus-1-2-export-in-source-account"></a>

1. Download the latest CloudFormation template from `https://aws-managed-cost-intelligence-dashboards.s3.amazonaws.com/cfn/data-exports-aggregation.yaml`.

1. In the **Management (Payer)** Account, open the **CID-DataExports-Source** stack again.

1. Select **Update stack** → **Make a direct update** → **Replace existing template** and choose **Upload a template file**, then upload the template you downloaded.

1. Set the **FOCUS** parameter to **Yes** to enable the FOCUS 1.2 version of the report.

1. Complete the stack update.

#### Click to see the example
<a name="focus-migration-step2-screenshot"></a>

![Enable FOCUS 1.2 in Source Account](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/focus-migration-enable-1-2-source.png)


### Step 3: Update Destination Account Stack
<a name="step-3-update-destination-account-stack"></a>

1. Log in to your **Data Collection (Destination)** Account.

1. Open the [CloudFormation Console](https://console.aws.amazon.com/cloudformation/home) and locate the **CID-DataExports-Destination** stack.

1. Select **Update stack** → **Make a direct update** → **Replace existing template** and choose **Upload a template file**, then upload the same template downloaded in Step 2.

1. Make sure the **FOCUS** parameter is set to **Yes**.

1. Complete the stack update.

#### Click to see the example
<a name="focus-migration-step3-screenshot"></a>

![Update Destination Account Stack](http://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/focus-migration-enable-1-2-source.png)


### Step 4: Update FOCUS Dashboard and Views
<a name="step-4-update-focus-dashboard-and-views"></a>

To bring in the new FOCUS 1.2 columns and update the FOCUS Dashboard to version 1.2.0:

1. Log in to your **Data Collection (Destination)** Account.

1. Open up a command-line interface with permissions to run API requests in your AWS account. We recommend using [CloudShell](https://console.aws.amazon.com/cloudshell).

1. Install or upgrade the CID CLI tool:

   ```
   pip3 install --upgrade cid-cmd
   ```

1. Run the following command to update the dashboard and all dependent views:

   ```
   cid-cmd update --recursive --force --dashboard-id focus-dashboard
   ```

1. If you have integrations with other cloud providers installed, select the respective Athena tables with FOCUS data from those providers along with the AWS FOCUS table when prompted. `cid-cmd` will automatically discover available columns in each table and generate the `focus_consolidation_view`.

## Next Steps
<a name="next-steps"></a>

After migrating to FOCUS 1.2, new FOCUS data will be delivered to the same S3 path where your FOCUS 1.0 data was stored. While the schemas are compatible, we recommend requesting a backfill to get historical AWS FOCUS data in version 1.2.

### Backfill Historical Data
<a name="backfill-historical-data"></a>

You can [create a Support Case](https://support.console.aws.amazon.com/support/home#/case/create) requesting a [backfill](https://docs.aws.amazon.com/cur/latest/userguide/troubleshooting.html#backfill-data) of your FOCUS report with up to 14 months of historical data. The case must be created from each of your Source Accounts (typically Management/Payer Accounts).

Support ticket example:

```
Service: Billing
Category: Other Billing Questions
Subject: Backfill Data

Hello Dear Billing Team,
Please can you backfill the data in DataExport named `cid-focus` for last 12 months.
Thanks in advance,
```

You can also use the following command in CloudShell to create this case via command line:

```
aws support create-case \
    --subject "Backfill Data" \
    --service-code "billing" \
    --severity-code "normal" \
    --category-code "other-billing-questions" \
    --communication-body "
        Hello Dear Billing Team,
        Please can you backfill the data in DataExport named 'cid-focus' for last 12 months.
        Thanks in advance"
```

Make sure you create the case from your Source Accounts (typically Management/Payer Accounts).

### Verify Dashboard Status
<a name="verify-dashboard-status"></a>

Run the following command to check dataset status in Amazon Quick Sight:

```
cid-cmd status --dashboard-id focus-dashboard
```

## Feedback
<a name="feedback"></a>

Please [contact the team](feedback-support.md) if you encounter any issues.