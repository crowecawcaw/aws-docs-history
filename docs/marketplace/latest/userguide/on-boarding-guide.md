# Onboarding to AWS Marketplace Commerce Analytics Service

With the AWS Marketplace Commerce Analytics Service, you can programmatically access product and customer data
through AWS Marketplace. To get started with the AWS Marketplace Commerce Analytics Service, you must configure your
AWS account and AWS services to use the AWS Marketplace Commerce Analytics Service. These sections show you how to
configure your AWS account and AWS services to use the AWS Marketplace Commerce Analytics Service.

###### To use the AWS Marketplace Commerce Analytics Service

- [Step 1: Set up your AWS account with
  permissions](#permissions-for-commerce-analytics "#permissions-for-commerce-analytics")
- [Step 2: Create a destination Amazon S3
  bucket](#create-a-destination-amazon-s3-bucket "#create-a-destination-amazon-s3-bucket")
- [Step 3: Configure an
  Amazon SNS topic for response notifications](#create-an-amazon-sns-topic-for-response-notifications "#create-an-amazon-sns-topic-for-response-notifications")
- [Step 4: Enroll in the
  Commerce Analytics Service program](#enroll-in-the-commerce-analytics-service-program "#enroll-in-the-commerce-analytics-service-program")
- [Step 5: Verify your configuration](#verify-your-configuration "#verify-your-configuration")

## Step 1: Set up your AWS account with

permissions

AWS Marketplace **strongly** recommends using AWS Identity and Access Management (IAM)
roles to sign in to the AWS Marketplace Management Portal rather than using your root account credentials. See [Policies and permissions for AWS Marketplace
sellers](detailed-management-portal-permissions.md "detailed-management-portal-permissions.md") for specific IAM permissions for
AWS Marketplace Commerce Analytics Service permissions. By creating individual users for people accessing your account,
you can give each user a unique set of security credentials. You can also grant different
permissions to each user. If necessary, you can change or revoke an user's permissions any
time.

## Step 2: Create a destination Amazon S3

bucket

The Commerce Analytics Service delivers the data you request to an Amazon S3 bucket that you specify. If you
already have an Amazon S3 bucket to use, proceed to the next step.

If you don't have an Amazon S3 bucket or you want to create an Amazon S3 bucket specifically
for this data, see [How do I Create
an Amazon S3 Bucket](../../../AmazonS3/latest/UG/CreatingaBucket.md "../../../AmazonS3/latest/UG/CreatingaBucket.md").

## Step 3: Configure an

Amazon SNS topic for response notifications

The Commerce Analytics Service delivers response notifications using Amazon SNS. The service publishes messages to
this topic to notify you when your datasets are available or if an error occurred. If you
already have an Amazon SNS topic for this purpose, proceed to the next step.

If you don't have an Amazon SNS topic configured for this service, configure one
now. For instructions, see [Create a Topic](../../../sns/latest/dg/CreateTopic.md "../../../sns/latest/dg/CreateTopic.md").

Record the topic Amazon Resource Name (ARN) for the topic you created, because the ARN is required to
call the service.

## Step 4: Enroll in the

Commerce Analytics Service program

The Commerce Analytics Service accesses the Amazon S3 bucket and Amazon SNS topic after you configure the service with
the ARN for the topic and name of the bucket.

###### To enable access

1. Log in to the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/ "https://aws.amazon.com/marketplace/management/") with the AWS account you use to manage your AWS Marketplace products.
2. Ensure you have the [necessary IAM permissions](commerce-analytics-service.md#technical-implementation-guide "commerce-analytics-service.md#technical-implementation-guide") to enroll in the AWS Marketplace
   Commerce Analytics Service.
3. Navigate to the [Commerce Analytics
   Service enrollment page](https://aws.amazon.com/marketplace/management/cas/enroll "https://aws.amazon.com/marketplace/management/cas/enroll").
4. Enter the Amazon S3 bucket name and Amazon SNS topic ARN, and choose
   **Enroll**.
5. On the permissions page, choose **Allow**.
6. On the AWS Marketplace Management Portal, record the **Role Name ARN** in the success
   message. You need the ARN to call the service.

###### Note

Onboarding to the Commerce Analytics Service creates an IAM role in your AWS account. The IAM role
allows AWS Marketplace to write to the Amazon S3 bucket and publish notifications to the Amazon SNS topic.
AWS Marketplace uses the account 452565589796 to perform these associated actions with this IAM
role.

## Step 5: Verify your configuration

The last step is to verify that your configuration works as expected.

###### To test your configuration

1. Download, install, and configure the [AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") (AWS CLI).
2. Using the AWS CLI, run this command.

```

aws marketplacecommerceanalytics generate-data-set \
--data-set-type "customer_subscriber_hourly_monthly_subscriptions" \
--data-set-publication-date "{TODAY'S-DATE}" \
--role-name-arn "{YOUR-ROLE-NAME-ARN}" \
--destination-s3-bucket-name "{amzn-s3-demo-bucket}" \
--destination-s3-prefix "TEST_PREFIX" \
--sns-topic-arn "{YOUR-SNS-TOPIC-ARN}"

```

- For `--data-set-publication-date`, replace `{TODAY'S DATE}`
  with the current date using ISO-8601 format, `YYYY-MM-DDT00:00:00Z`, where
  `YYYY` is the four-digit year, `MM` is the two-digit month, and
  `DD` is the two-digit day.
- For `--role-name-arn`, replace `{YOUR-ROLE-NAME-ARN}` with
  the ARN of the role you received from the enrollment process in
  [Step 4: Enroll in the
  Commerce Analytics Service program](#enroll-in-the-commerce-analytics-service-program "#enroll-in-the-commerce-analytics-service-program").
- For _--destination-s3-bucket-name_, replace
  _{amzn-s3-demo-bucket}_ with the name of the Amazon S3 bucket you created
  in [Step 2: Create a destination Amazon S3
  bucket](#create-a-destination-amazon-s3-bucket "#create-a-destination-amazon-s3-bucket").
- For _–sns-topic-arn_, replace _{YOUR-SNS-TOPIC-ARN}_ with the Amazon SNS topic you created in
  [Step 3: Configure an
  Amazon SNS topic for response notifications](#create-an-amazon-sns-topic-for-response-notifications "#create-an-amazon-sns-topic-for-response-notifications").

If you receive a response including the _dataSetRequestId_ response from the service, you've completed the on-boarding
process. A successful response looks like this:

```

{
   "dataSetRequestId": "646dd4ed-6806-11e5-a6d8-fd5dbcaa74ab"
}

```
