AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Exporting OpsData from Systems Manager

Explorer

You can export 5,000 OpsData items as a comma separated value (.csv) file to an
Amazon Simple Storage Service (Amazon S3) bucket from AWS Systems Manager Explorer. Explorer uses the [AWS-ExportOpsDataToS3](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-exportopsdatatos3.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-exportopsdatatos3.md") automation runbook to export
OpsData. When you export OpsData, the system displays the automation runbook page where
you can specify details, such as assumeRole, Amazon S3 bucket name, SNS topic ARN, and fields
to be exported.

###### To export OpsData:

- [Step 1: Specifying an SNS topic](#Explorer-specify-SNS-topic "#Explorer-specify-SNS-topic")
- [Step 2: (Optional) Configuring data
  export](#Explorer-configure-data-export "#Explorer-configure-data-export")
- [Step 3: Exporting OpsData](#Explorer-export-OpsData "#Explorer-export-OpsData")

## Step 1: Specifying an SNS topic

When you configure data export, you must specify an Amazon Simple Notification Service (Amazon SNS) topic that
exists in the same AWS Region where you want to export the data. Systems Manager sends a
notification to the Amazon SNS topic when an export is complete. For information about
creating an Amazon SNS topic, see [Creating an Amazon SNS topic](../../../sns/latest/dg/sns-tutorial-create-topic.md "../../../sns/latest/dg/sns-tutorial-create-topic.md").

## Step 2: (Optional) Configuring data

export

You can configure data export settings from the **Settings** or
**Export Ops Data to S3 Bucket** page.

###### To configure data export from Explorer

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Explorer**.
3. Choose **Settings**.
4. In the **Configure data export** section, choose
   **Edit**.
5. To upload the data export file to an existing Amazon S3 bucket, choose
   **Select an existing S3 bucket** and choose the bucket
   from the list.

To upload the data export file to a new Amazon S3 bucket, choose
**Create a new S3 bucket** and enter the name that you
want to use for the new bucket.

###### Note

You can only edit the Amazon S3 bucket name and Amazon SNS topic ARN from the
page where you configured those settings for the first time in Explorer.
If you set up the Amazon S3 bucket and the Amazon SNS topic ARN from the
**Settings** page, then you can only modify those
settings from the **Settings** page. 6. For **Select an Amazon SNS topic ARN**, choose the topic
that you want to notify when the export is complete. 7. Choose **Create**.

## Step 3: Exporting OpsData

When you export Explorer data, Systems Manager creates an AWS Identity and Access Management (IAM) role named
`AmazonSSMExplorerExportRole`. This role uses the following IAM
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OpsSummaryExportAutomationServiceRoleStatement1",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Sid": "OpsSummaryExportAutomationServiceRoleStatement2",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketAcl",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`"
 ]
 },
 {
 "Sid": "OpsSummaryExportAutomationServiceRoleStatement3",
 "Effect": "Allow",
 "Action": [
 "sns:Publish"
 ],
 "Resource": [
 "arn:aws:sns:`us-east-1`:`111122223333`:`SNSTopicName`"
 ]
 },
 {
 "Sid": "OpsSummaryExportAutomationServiceRoleStatement4",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:`MyLogGroup`"
 ]
 },
 {
 "Sid": "OpsSummaryExportAutomationServiceRoleStatement5",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:PutLogEvents",
 "logs:CreateLogStream"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "OpsSummaryExportAutomationServiceRoleStatement6",
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsSummary"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
 }`

```

The role includes the following trust entity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OpsSummaryExportAutomationServiceRoleTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "ssm.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
 }`

```

###### To export OpsData from Explorer

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Explorer**.
3. Choose a data link in an Explorer widget. For example, choose
   **Unresolved** or **Open issues** in the
   **OpsItems by status** widget. Or choose the
   **Critical** or **High** data link in the
   **OpsItem by severity** widget. Explorer opens the
   **OpsData** page for the selected data set.
4. Choose **Export Table**.

###### Note

When you export OpsData for the first time, the system creates an assume
role for the export. You can't modify the default assume role. 5. For **S3 Bucket Name**, choose an existing bucket. You can
choose **Create** to create an Amazon S3 bucket if needed.

If you can't change the S3 bucket name, it means that you configured the
bucket name from the **Settings** page. You can
only change the bucket name from the **Settings** page.

###### Note

You can only edit the Amazon S3 bucket name and Amazon SNS topic ARN from the page
where you configured those settings for the first time in Explorer. 6. For **SNS Topic Arn**, choose an existing Amazon SNS topic ARN to
notify when the download completes.

If you can't change the Amazon SNS topic ARN, it means that you configured the
Amazon SNS topic ARN from the **Settings** page. You can
only change the topic ARN from the **Settings**
page. 7. (Optional) For **SNS Success Message**, specify a success
message that you want to display when the export is successfully
completed. 8. Choose **Submit**. The system navigates to the previous page
and displays the message **Click to view status of export process. View
details**.

You can choose **View details** to view the status of the
runbook and progress in Systems Manager Automation.
You can now export OpsData from Explorer to the specified Amazon S3 bucket.

If you can't export data by using this procedure, verify that your user, group, or
role includes the `iam:CreatePolicyVersion` and
`iam:DeletePolicyVersion` actions. For information about adding these
actions to your user, group, or role, see [Editing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md")
in the _IAM User Guide_.
