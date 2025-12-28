# Tutorial: Configure plan execution report autogeneration

This tutorial guides you through configuring plan execution report autogeneration for a Region switch plan. Reports
provide comprehensive PDF documentation of plan executions for compliance purposes.

In this tutorial, you'll complete the following steps:

- Create an Amazon S3 bucket for report storage
- Enable report autogeneration on a Region switch plan
- Execute the plan and download the report

## Prerequisites

Before you begin this tutorial, verify that you have the following:

- An existing Region switch plan with configured workflows
- Permissions to create Amazon S3 buckets
- Your plan's execution IAM role configured with the required permissions. For more information,
  see [Automatic plan execution reports permissions](security_iam_region_switch_reports.md "security_iam_region_switch_reports.md").

## Step 1: Create an Amazon S3 bucket for reports

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. Provide the following details:
   - **Bucket name**: Enter a unique name, such as `my-region-switch-reports`
   - **Block Public Access settings**: Keep all public access blocked (recommended)
   - **Bucket Versioning**: Enable versioning (optional but recommended)
   - **Default encryption**: Select the encryption. If using SSM-KMS, the planExecutionRole needs kms:Encrypt
     and kms:GenerateDataKey permissions on the s3 bucket's default CMK

4. Choose **Create bucket**.
5. Note the bucket name for use in the next step.

## Step 2: Enable report autogeneration on your plan

1. Open the Region switch console at [https://console.aws.amazon.com/route53recovery/regionswitch/home](https://console.aws.amazon.com/route53recovery/regionswitch/home "https://console.aws.amazon.com/route53recovery/regionswitch/home").
2. Select the plan you want to configure reports for.
3. Choose **In the navigation bar, go to Actions and select Edit plan details**.
4. In the **Report settings** section, provide the following:
   - Select **Enable report autogeneration**
   - **Amazon S3 URI:** Select or enter the bucket S3 URI you created in Step 1
   - **Account ID that owns bucket:** Enter the bucket owner account ID

5. Choose **Save**.
6. Wait for plan evaluation to complete. If there are any configuration issues, warnings will appear on the
   plan details page.

## Step 3: Execute the plan and download the report

1. On the plan details page, choose **Execute**.
2. Complete the plan execution as normal, selecting the Region to activate and execution mode.
3. After the plan execution completes, navigate to the execution details page.
4. In the **Plan execution report** section, monitor the report generation status. Report generation typically
   completes within 30 minutes of execution completion.
5. When the report status shows **Completed**, choose **Download plan execution report** to
   download the PDF.
6. Alternatively, navigate to your Amazon S3 bucket to access the report directly. Reports are stored with the
   following naming pattern: `ExecutionReport-${planVersion.ownerAccountId}-${planName}-${execution.regionTo}-${event.executionId}-${dateStr}.pdf`

The generated report includes:

- Executive summary with service overview and report creation date
- Plan configuration details as they existed at execution time
- Detailed execution timeline with steps, affected resources, and statuses
- Plan warnings that were present when the execution started
- Amazon CloudWatch alarm states and alarm history for associated alarms
- For parent plans, configuration and execution details of child plans
- Glossary of terms and concepts

## Troubleshooting

If report generation fails, check the following:

- **Permission errors**: Verify that the execution role has the correct IAM
  permissions. For more information, see [Automatic plan execution reports permissions](security_iam_region_switch_reports.md "security_iam_region_switch_reports.md"). Check the plan evaluation warnings for specific permission issues.
- **Amazon S3 bucket access**: Ensure the Amazon S3 bucket exists and is accessible from the
  Region where the plan is configured. Verify that bucket policies don't block access from the execution role.
- **Bucket encryption**: If using customer-managed KMS keys for bucket encryption,
  ensure the execution role has permissions to use the KMS key.

For additional help, view detailed error messages on the execution details page or contact AWS Support.
