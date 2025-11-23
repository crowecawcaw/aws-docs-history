# Create an AWS Glue Crawler

AWS Glue is a fully managed extract, transform, and load (ETL) service that lets you
create a database from your Amazon S3 data and query that database by using Athena. This
database is also referred to as an AWS Glue Data Catalog. An AWS Glue crawler can
automatically detect the schema of your Amazon S3 data and create the corresponding
database and tables. WorkSpaces Applications provides an CloudFormation template that you can use to create
the necessary AWS Glue resources.

###### Important

Completing the steps in the following procedure creates an AWS Glue crawler. However, these steps don’t start the
crawler. To start the crawler, you must perform the steps in the next
procedure. For more information about AWS Glue crawlers, see [Defining Crawlers](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md").

###### To create an AWS Glue crawler

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home "https://console.aws.amazon.com/appstream2/home").
2. Choose the AWS Region for which you have subscribed to usage reports.
3. In the navigation pane, choose **Usage Reports**, and verify that usage reports logging is enabled.
4. On the **Report Details** tab, in the paragraph next to
   **Analytics**, choose the **CloudFormation
   template** link.

Choosing the link opens the CloudFormation console, where you can review the parameters
of the CloudFormation stack specified by the template before you run it. The
template, when run, creates an AWS Glue crawler and several sample Athena queries. 5. On the **Specify Details** page, next to
**ScheduleExpression**, either keep the default value or specify a different cron expression value for the frequency that you
want to run the crawler. Do not change any other default value. When you're
done, choose **Next**.

By default, the
crawler is scheduled to run on a daily basis, but you can configure the crawler to run
weekly, monthly, or on another frequency. For information about cron syntax, see [Cron
Expressions](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions"). 6. On the **Options** page, keep the default values, and choose **Next**. 7. On the **Review** page, select the check box next to "I acknowledge that CloudFormation might create IAM resources with custom names," and then choose **Create**.

You must have sufficient AWS Glue and AWS Identity and Access Management (IAM) permissions to create and
run the CloudFormation stack. If you don't have the required permissions, ask your
Amazon Web Services account administrator either to perform these steps in your account or
to grant you the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "athena:CreateNamedQuery",
 "athena:BatchGetNamedQuery",
 "athena:GetNamedQuery",
 "athena:StartQueryExecution",
 "athena:GetQueryResults",
 "athena:GetQueryExecution",
 "athena:ListNamedQueries",
 "cloudformation:DescribeStacks",
 "cloudformation:GetStackPolicy",
 "cloudformation:DescribeStackEvents",
 "cloudformation:CreateStack",
 "cloudformation:GetTemplate",
 "cloudformation:ListChangeSets",
 "cloudformation:ListStackResources",
 "iam:GetRole",
 "iam:CreateRole",
 "iam:GetRolePolicy",
 "s3:GetBucketLocation",
 "s3:ListBucketMultipartUploads",
 "s3:ListBucket",
 "s3:ListMultipartUploadParts",
 "s3:PutObject",
 "s3:GetObject",
 "s3:AbortMultipartUpload"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AppStreamUsageReports-AppStreamUsageReportGlueRole*",
 "arn:aws:cloudformation:*:*:stack/AppStreamUsageReports/*",
 "arn:aws:athena:*:*:workgroup/primary",
 "arn:aws:s3:::aws-athena-query-results-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:PutRolePolicy",
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::appstream-logs-*",
 "arn:aws:iam::*:role/AppStreamUsageReports-AppStreamUsageReportGlueRole*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/AppStreamUsageReports-AppStreamUsageReportGlueRole*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "glue.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:GetTemplateSummary",
 "glue:GetResourcePolicy",
 "glue:GetCrawlers",
 "glue:BatchGetCrawlers",
 "glue:GetClassifiers",
 "glue:CreateClassifier",
 "glue:ListCrawlers",
 "glue:GetTags",
 "glue:GetCrawlerMetrics",
 "glue:GetClassifier",
 "tag:GetResources"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "athena:RunQuery",
 "Resource": "arn:aws:athena:*:*:workgroup/primary"
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetTables",
 "glue:GetPartitions",
 "glue:GetTable"
 ],
 "Resource": [
 "arn:aws:glue:*:*:table/appstream-usage/*",
 "arn:aws:glue:*:*:database/appstream-usage",
 "arn:aws:glue:*:*:catalog"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabase",
 "glue:CreateDatabase",
 "glue:GetDatabases"
 ],
 "Resource": [
 "arn:aws:glue:*:*:database/appstream-usage",
 "arn:aws:glue:*:*:catalog"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetCrawler",
 "glue:StartCrawler",
 "glue:CreateCrawler"
 ],
 "Resource": "arn:aws:glue:*:*:crawler/appstream-usage*"
 },
 {
 "Effect": "Allow",
 "Action": "glue:GetCatalogImportStatus",
 "Resource": "arn:aws:glue:*:*:catalog"
 }
 ]
}`

```
