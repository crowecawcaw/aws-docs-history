# Setting up Athena using AWS CloudFormation templates

###### Important

AWS CloudFormation doesn't support cross-Region resources. If you plan to use an AWS CloudFormation template, you
must create all resources in the same AWS Region. The Region must support the following
services:

- AWS Lambda
- Amazon Simple Storage Service (Amazon S3)
- AWS Glue
- Amazon Athena
  To streamline and automate integration of your Cost and Usage Reports with Athena, AWS provides an
  AWS CloudFormation template with several key resources along with the reports that you set up for Athena
  integration. The AWS CloudFormation template includes an AWS Glue crawler, an AWS Glue database, and an
  AWS Lambda event.

The Athena integration setup process using AWS CloudFormation removes any Amazon S3 events that your bucket might already have. This can negatively affect any existing event-based processes that you have for an existing AWS CUR report. We strongly recommend that you create both a new Amazon S3 bucket and a new AWS CUR report to use
with Athena.

Before you can use a CloudFormation template to automate Athena integration, make sure that you
do the following:

- Create a new Amazon S3 bucket for your reports. For more information, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.
- [Create a new report](cur-create.md "cur-create.md") to use with Athena. During the
  setup process, for **Report data integration**, choose
  **Athena**.
- Wait for the first report to be delivered to your Amazon S3 bucket. It can take up to 24
  hours for AWS to deliver your first report.

###### To use the Athena AWS CloudFormation template

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. From the list of buckets, choose the bucket where you chose to receive your AWS CUR
   report.
3. Choose your report path prefix (`your-report-path-prefix/`).
   Then, choose your report name (`your-report-name/`).
4. Choose the `.yml` template file.
5. Choose **Object actions**, and then choose **Download
   as**.
6. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
7. If you have never used AWS CloudFormation before, choose **Create New Stack**.
   Otherwise, choose **Create Stack**.
8. Under **Prepare template**, choose **Template is
   ready**.
9. Under **Template source**, choose **Upload a template
   file**.
10. Choose **Choose file**.
11. Choose the downloaded `.yml` template, and then choose
    **Open**.
12. Choose **Next**.
13. For **Stack name**, enter a name for your template and choose
    **Next**.
14. Choose **Next**.
15. At the bottom of the page, select **I acknowledge that AWS CloudFormation might create
    IAM resources.**

This template creates the following resources:

    * Three IAM roles
    * An AWS Glue database
    * An AWS Glue crawler
    * Two Lambda functions
    * An Amazon S3 notification

16. Choose **Create stack**.

###### To update the existing Athena AWS CloudFormation template

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. From the list of buckets, choose the bucket where you chose to receive your AWS CUR
   report.
3. Choose your report path prefix (`your-report-path-prefix/`).
   Then, choose your report name (`your-report-name/`).
4. Choose the `.yml` template file.
5. Choose **Object actions**, and then choose **Download
   as**.
6. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
7. Select the stack that was previously created, and then choose
   **Update**.
8. Under **Prepare template**, choose **Replace current
   template**.
9. Under **Template source**, choose **Upload a template
   file**.
10. Choose **Choose file**.
11. Choose the downloaded `.yml` template, and then choose
    **Open**.
12. Choose **Next**.
13. On the **Specify stack details** page, modify any details, and then
    choose **Next**.
14. Choose **Next**.
15. At the bottom of the page, select **I acknowledge that AWS CloudFormation might create
    IAM resources.**
16. Choose **Update stack**.
