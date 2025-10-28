# Setting up your tax information

You can use the **Tax settings** page under **Preferences and Settings** in the left navigation of your AWS Billing and Cost Management console. Use this page to manage your tax registration numbers, turn on tax setting inheritance so your tax registration information is aligned across your Organizations accounts, and manage your tax exemptions. This page also shows how you can set up your Amazon S3 buckets to use your Tax Settings API.

## Updating and deleting

tax registration numbers

Use the following steps to update or delete one or more tax registration
numbers.

###### Note

If a country isn't listed in the **Tax settings** page dropdown,
AWS doesn't collect tax registration for that country at this time.

###### To update tax registration numbers

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Tax settings**.
3. Under **Tax registrations**, select the numbers to
   edit.
4. For **Manage tax registration**, choose
   **Edit**.
5. Enter your updated information and choose **Update**.

You can remove one or more tax registration numbers.

###### To delete tax registration numbers

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Tax settings**.
3. Under **Tax Registrations**, select the tax registration
   numbers to delete.
4. For **Manage tax registration**, choose **Delete
   TRN**.
5. In the **Delete tax registration** dialog box, choose
   **Delete**.

## Turning on tax setting

inheritance

You can use your tax registration information with your member accounts by turning on
your **Tax settings inheritance**. After you activate it, your tax
registration information is added to your other AWS Organizations accounts, saving you the effort
of registering redundant information. Tax invoices are processed with the consistent tax
information, and your usage from member accounts will consolidate to a single tax
invoice.

###### Notes

- Tax inheritance settings are only available to accounts after a member
  account is added.
- If you turn off tax inheritance, the member accounts revert to the
  account's original TRN setting. If there was no TRN originally set for the
  account, no TRN will be assigned.

Tax registration information includes:

- Business legal name
- Tax address
- Tax registration number
- Special exemptions

###### To turn on tax setting inheritance

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Tax settings**.
3. Under **Tax registrations**, select **Enable tax
   settings inheritance**.
4. In the dialog box, choose **Enable**.

## Managing your US tax

exemptions

If your state is eligible, you can manage your US tax exemptions on the **Tax
settings** page. The documents you upload for the exemption are reviewed by
Support within 24 hours.

###### Note

You must have IAM permissions to view the **Tax exemptions**
tab on the **Tax settings** page in the Billing and Cost Management console.

For an example IAM policy, see [Allow IAM users to view US tax
exemptions and create Support cases](billing-example-policies.md#example-awstaxexemption "billing-example-policies.md#example-awstaxexemption").

###### To upload or add your US

tax exemption

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Tax settings**.
3. Choose **Tax exemptions**.
4. Choose all of the accounts to add the tax exemption. Choose **Manage
   tax exemption** and select **Add tax
   exemption**.
   1. If you're logged in as a linked account, you can add tax exemptions to
      only the linked account.
   2. If you're logged in as a payer account, you can add tax exemptions to
      both payer and linked accounts.

5. Specify your exemption type and jurisdiction.
6. Upload certificate documents.
7. Review your information, and choose **Submit**.

Within 24 hours, Support will notify you through a support case if they need additional
information, or if any of your documents weren't valid.

Once the exemption is approved, you can view it under the **Tax
exemption** tab with an **Active** validity period.

You will be notified through a support case contact if your exemption was
rejected.

## Setting up your Amazon S3 to use your Tax Settings API

Follow this procedure so that the [Tax Settings API](../../../aws-cost-management/latest/APIReference/API_Operations_Tax_Settings.md "../../../aws-cost-management/latest/APIReference/API_Operations_Tax_Settings.md") has permission to send your tax documents to an Amazon S3 bucket. You can then download the tax document from your Amazon S3 bucket. You only need to do this procedure for the following countries that require a tax registration document:

- BD: Bangladesh
- KE: Kenya
- KR: South Korea
- ES: Spain

For all other countries, you don’t need to specify a tax registration document. If you call the Tax Settings API and provide a tax registration document in your request, the API will return a `ValidationException` error message.

The following Tax Settings API operations require access to your Amazon S3 bucket:

- `BatchPutTaxRegistration`: Requires access to read the Amazon S3 bucket
- `PutTaxRegistration`: Requires access to read the Amazon S3 bucket
- `GetTaxRegistrationDocument`: Requires access to write to the Amazon S3 bucket

### Adding resource policies to your Amazon S3 bucket

To allow the Tax Settings API to access the object in your Amazon S3 bucket, add the following resource policies in your Amazon S3 bucket.

###### Example For `BatchPutTaxRegistration` and `PutTaxRegistration`

Replace `DOC-EXAMPLE-BUCKET1` with the name of your bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow the Tax Settings API to access objects",
 "Effect": "Allow",
 "Principal": {
 "Service": "tax.amazonaws.com"
 },
 "Action": [
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:tax:us-east-1:${AccountId}:*",
 "aws:SourceAccount": "${AccountId}"
 }
 }
 }
 ]
}`

```

###### Example For `GetTaxRegistrationDocument`

Replace `amzn-s3-demo-bucket1` with the name of your
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow the Tax Settings API to access objects",
 "Effect": "Allow",
 "Principal": {
 "Service": "tax.amazonaws.com"
 },
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:tax:us-east-1:${AccountId}:*",
 "aws:SourceAccount": "${AccountId}"
 }
 }
 }
 ]
}`

```

###### Note

For the classic AWS Regions (`aws` partition), the `aws:SourceArn` will be: `arn:aws:tax:us-east-1:`{YOUR_ACCOUNT_ID}`:*`

For the China Regions (`aws-cn` partition), the `aws:SourceArn` will be: `arn:aws-cn:tax:cn-northwest-1:`{YOUR_ACCOUNT_ID}`:*`

###### To allow the Tax Settings API access to your S3 bucket

1. Go to the [Amazon S3
   console](https://s3.console.aws.amazon.com/s3/home?region=us-east-1 "https://s3.console.aws.amazon.com/s3/home?region=us-east-1") and sign in.
2. Choose **Buckets** from the left navigation, and then choose
   your bucket from the list.
3. Choose the **Permissions** tab, then, next to
   **Bucket policy**, choose **Edit**.
4. In the **Policy** section, add the policies to the bucket.
5. Choose **Save changes** to save your policy, attached to your
   bucket.

Repeat for each bucket that encrypts an S3 bucket that Tax Settings needs to access.

### AWS KMS managed key policy

If your S3 bucket is encrypted with AWS KMS managed key (SSE-KMS), add the following permission to the KMS key. This permission is required for the following API operations:

- `BatchPutTaxRegistration`
- `PutTaxRegistration`
- `GetTaxRegistrationDocument`

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-consolepolicy-3",
 "Statement": [
 {
 "Sid": "Allow the Tax Settings API to access objects",
 "Effect": "Allow",
 "Principal": {
 "Service": "tax.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn": "arn:aws:tax:us-east-1:${YOUR_ACCOUNT_ID}:*",
 "aws:SourceAccount": "${YOUR_ACCOUNT_ID}"
 }
 }
 }
 ]
}`

```

###### To give Tax Settings access to AWS KMS for SSE-KMS encrypted S3 buckets

1. Go to the [Amazon S3
   console](https://s3.console.aws.amazon.com/s3/home?region=us-east-1 "https://s3.console.aws.amazon.com/s3/home?region=us-east-1") and sign in.
2. Choose **Customer managed keys** from the left navigation, and then choose the key that is used to encrypt your bucket from the list.
3. Select **Switch to policy view**, then choose **Edit**.
4. In the **Policy** section, add the AWS KMS policy statement.
5. Choose **Save changes** to save your policy, attached to your
   key.

Repeat for each key that encrypts an S3 bucket that Tax Settings needs to access.
