# Exporting generated GuardDuty findings to Amazon S3

buckets

GuardDuty retains the generated findings for a period of 90 days. GuardDuty exports the active
findings to Amazon EventBridge (EventBridge). You can optionally export the generated findings to an Amazon Simple Storage Service
(Amazon S3) bucket. This will help you to track the historical data of potentially suspicious
activities in your account and evaluate whether the recommended remediation steps were
successful.

Any new active findings that GuardDuty generates are automatically exported within about 5
minutes after the finding is generated. You can set the frequency for how often updates to
the active findings are exported to EventBridge. The frequency that you select applies to the
exporting of new occurrences of existing findings to EventBridge, your S3 bucket (when configured),
and Detective (when integrated). For information about how GuardDuty aggregates multiple occurrences
of existing findings, see [GuardDuty finding aggregation](finding-aggregation.md "finding-aggregation.md").

When you configure settings to export findings to an Amazon S3 bucket, GuardDuty uses AWS Key Management Service
(AWS KMS) to encrypt the findings data in your S3 bucket. This requires you to add permissions
to your S3 bucket and the AWS KMS key so that GuardDuty can use them to export findings in your
account.

###### Contents

- [Considerations](#guardduty-export-findings-considerations "#guardduty-export-findings-considerations")
- [Step 1 – Permissions
  required to export findings](#guardduty_exportfindings-permissions "#guardduty_exportfindings-permissions")
- [Step 2 – Attaching
  policy to your KMS key](#guardduty-exporting-findings-kms-policy "#guardduty-exporting-findings-kms-policy")
- [Step 3 – Attaching policy
  to Amazon S3 bucket](#guardduty_exportfindings-s3-policies "#guardduty_exportfindings-s3-policies")
- [Step 4 - Exporting findings to an
  S3 bucket (Console)](#guardduty_exportfindings-new-bucket "#guardduty_exportfindings-new-bucket")
- [Step 5 – Setting frequency
  to export updated active findings](#guardduty_exportfindings-frequency "#guardduty_exportfindings-frequency")

## Considerations

Before proceeding with the prerequisites and steps to export findings, consider the
following key concepts:

- **Export settings are regional** – You
  need to configure export options in each Region where you use GuardDuty.
- **Exporting findings to Amazon S3 buckets in different
  AWS Regions (cross-Region)** – GuardDuty supports the
  following export settings:
  - Your Amazon S3 bucket or object, and AWS KMS key must belong to the same
    AWS Region.
  - For the findings generated in a commercial Region, you can choose to
    export these findings to an S3 bucket in any commercial Region. However,
    you can't export these findings to an S3 bucket in an opt-in
    Region.
  - For the findings generated in an opt-in Region, you can choose to
    export these findings to the same opt-in Region where they're generated
    or any commercial Region. However, you can't export findings from one
    opt-in Region to another opt-in Region.

- **Permissions to export findings** – To
  configure settings for exporting active findings, your S3 bucket must have
  permissions that allows GuardDuty to upload objects. You must also have an AWS KMS key
  that GuardDuty can use to encrypt findings.
- **Archived findings are not exported** –
  The default behavior is that the archived findings, including new instances of
  suppressed findings, are not exported.

When a GuardDuty finding gets generated as _Archived_, you will
need to _Unarchive_ it. This changes the **Filter
finding status** to **Active**. GuardDuty exports the
updates to the existing unarchived findings based on how you configure [Step 5 –
Frequency for exporting findings](#guardduty_exportfindings-frequency "#guardduty_exportfindings-frequency").

- **GuardDuty administrator account can export findings generated in
  associated member accounts** – When you configure export
  findings in an administrator account, all the findings from the associated member accounts
  that are generated in the same Region are also exported to the same location
  that you configured for the administrator account. For more information, see [Understanding the relationship
  between GuardDuty administrator account and member accounts](administrator_member_relationships.md "administrator_member_relationships.md").

## Step 1 – Permissions

required to export findings

When you configure settings for exporting findings, you select an Amazon S3 bucket where
you can store the findings and an AWS KMS key to use for data encryption. In addition to
permissions for GuardDuty actions, you must also have permissions to the following actions
to successfully configure settings to export findings:

- `s3:GetBucketLocation`
- `s3:PutObject`

If you need to export the findings to a specific prefix in your Amazon S3 bucket, you must also
add the following permissions to the IAM role:

- `s3:GetObject`
- `s3:ListBucket`

## Step 2 – Attaching

policy to your KMS key

GuardDuty encrypts the findings data in your bucket by using AWS Key Management Service. To successfully
configure the settings, you must first give GuardDuty permission to use a KMS key. You can
grant the permissions by [attaching
the policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") to your KMS key.

When you use a KMS key from another account, you need to apply the key policy by
logging in to the AWS account that owns the key. When you configure the settings to
export findings, you'll also need the key ARN from the account that owns the
key.

###### To modify the KMS key policy for GuardDuty to encrypt your exported

findings

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. Select an existing KMS key or perform the steps to [Create a new key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
   _AWS Key Management Service Developer Guide_, that you will use to encrypt the
   exported findings.

###### Note

The AWS Region of your KMS key and the Amazon S3 bucket must be the same.

You can use the same S3 bucket and KMS key pair to export the findings from
any applicable Region. For more information, see [Considerations](#guardduty-export-findings-considerations "#guardduty-export-findings-considerations") for exporting
findings across Regions. 4. In the **Key policy** section, choose
**Edit**.

If **Switch to policy view** is displayed, choose it to
display the **Key policy**, and then choose
**Edit**. 5. Copy the following policy block to your KMS key policy, to grant GuardDuty
permission to use your key.

```
{
    "Sid": "AllowGuardDutyKey",
    "Effect": "Allow",
    "Principal": {
        "Service": "guardduty.amazonaws.com"
    },
    "Action": "kms:GenerateDataKey",
    "Resource": "`KMS key ARN`",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "`123456789012`",
            "aws:SourceArn": "arn:aws:guardduty:`Region2`:`123456789012`:detector/`SourceDetectorID`"
        }
    }
}
```

6. Edit the policy by replacing the following values that are formatted in
   _`red`_ in the policy
   example:
   1. Replace `KMS key ARN` with the Amazon
      Resource Name (ARN) of the KMS key. To locate the key ARN, see [Finding the key ID and
      ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the _AWS Key Management Service Developer Guide_.
   2. Replace `123456789012` with the
      AWS account ID that owns the GuardDuty account exporting the
      findings.
   3. Replace `Region2` with the AWS Region where
      the GuardDuty findings are generated.
   4. Replace `SourceDetectorID` with the
      `detectorID` of the GuardDuty account in the specific Region
      where the findings generated.

   To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

###### Note

If you're using GuardDuty in an opt-in Region, replace the value for
the "Service" with the Regional endpoint for that Region. For example, if
you're using GuardDuty in the Middle East (Bahrain) (me-south-1) Region, replace
`"Service": "guardduty.amazonaws.com"` with `"Service":
 "guardduty.me-south-1.amazonaws.com"`. For information about
endpoints for each opt-in Region, see [GuardDuty endpoints and quotas](../../../general/latest/gr/guardduty.md "../../../general/latest/gr/guardduty.md"). 7. If you added the policy statement before the final statement, add a comma
before adding this statement. Make sure that the JSON syntax of your KMS key
policy is valid.

Choose **Save**. 8. (Optional) copy the key ARN to a notepad for use in the later steps.

## Step 3 – Attaching policy

to Amazon S3 bucket

Add permissions to the Amazon S3 bucket to which you will export findings so that GuardDuty can
upload objects to this S3 bucket. Independent of using an Amazon S3 bucket that belongs to
either your account or in a different AWS account, you must add these
permissions.

If at any point in time, you decide to export findings to a different S3 bucket, then
to continue exporting findings, you must add permissions to that S3 bucket and configure
the export findings settings again.

If you do not already have an Amazon S3 bucket where you want to export these findings, see
[Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_.

### To attach permissions to your S3 bucket

policy

1. Perform the steps under [To create or edit
   a bucket policy](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon S3 User Guide_, until
   the **Edit bucket policy** page appears.
2. The **example policy** shows how grant GuardDuty
   permission to export findings to your Amazon S3 bucket. If you change the path
   after you configure export findings, then you must modify the policy to
   grant permission to the new location.

Copy the following **example policy** and
paste it into the **Bucket policy editor**.

If you added the policy statement before the final statement, add a comma
before adding this statement. Make sure that the JSON syntax of your
KMS key policy is valid.

**S3 bucket example policy**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow GetBucketLocation",
 "Effect": "Allow",
 "Principal": {
 "Service": "guardduty.amazonaws.com"
 },
 "Action": "s3:GetBucketLocation",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`",
 "aws:SourceArn": "arn:aws:guardduty:`us-east-2`:`123456789012`:detector/`SourceDetectorID`"

 }
 }
 },
 {
 "Sid": "Allow PutObject",
 "Effect": "Allow",
 "Principal": {
 "Service": "guardduty.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`[optional prefix]/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`",
 "aws:SourceArn": "arn:aws:guardduty:`us-east-2`:`123456789012`:detector/`SourceDetectorID`"

 }
 }
 },
 {
 "Sid": "Deny unencrypted object uploads",
 "Effect": "Deny",
 "Principal": {
 "Service": "guardduty.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`[optional prefix]/*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption": "aws:kms"
 }
 }
 },
 {
 "Sid": "Deny incorrect encryption header",
 "Effect": "Deny",
 "Principal": {
 "Service": "guardduty.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`[optional prefix]/*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-server-side-encryption-aws-kms-key-id": "arn:aws:kms:`us-east-2`:`111122223333`:key/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`"
 }
 }
 },
 {
 "Sid": "Deny non-HTTPS access",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`[optional prefix]/*",
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 }
 ]
}`

```

3. Edit the policy by replacing the following values that are formatted in
   _`red`_ in the policy
   example:
   1. Replace `Amazon S3 bucket ARN` with the Amazon
      Resource Name (ARN) of the Amazon S3 bucket. You can find the
      **Bucket ARN** on the **Edit bucket
      policy** page in the [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/") console.
   2. Replace `123456789012` with the
      AWS account ID that owns the GuardDuty account exporting the
      findings.
   3. Replace `us-east-2` with the AWS Region
      where the GuardDuty findings are generated.
   4. Replace `SourceDetectorID` with the
      `detectorID` of the GuardDuty account in the specific
      Region where the findings generated.

   To find the `detectorId` for your account and current Region, see the
   **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
   or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API. 5. Replace `[optional prefix]` part of the
   `S3 bucket ARN/[optional prefix]`
   placeholder value with an optional folder location to which you want
   to export the findings. For more information about the use of
   prefixes, see [Organizing
   objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the
   _Amazon S3 User Guide_.

   When you provide an optional folder location that doesn't exist
   already, GuardDuty will create that location only if the account
   associated with the S3 bucket is the same as the account exporting
   the findings. When you export findings to an S3 bucket that belongs
   to another account, the folder location must exist already. 6. Replace `KMS key ARN` with the Amazon
   Resource Name (ARN) of the KMS key associated with the encryption
   of the findings exported to the S3 bucket. To locate the key ARN,
   see [Finding the key
   ID and ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the
   _AWS Key Management Service Developer Guide_.

###### Note

If you're using GuardDuty in an opt-in Region, replace the value for
the "Service" with the Regional endpoint for that Region. For example, if
you're using GuardDuty in the Middle East (Bahrain) (me-south-1) Region, replace
`"Service": "guardduty.amazonaws.com"` with `"Service":
 "guardduty.me-south-1.amazonaws.com"`. For information about
endpoints for each opt-in Region, see [GuardDuty endpoints and quotas](../../../general/latest/gr/guardduty.md "../../../general/latest/gr/guardduty.md"). 4. Choose **Save**.

## Step 4 - Exporting findings to an

S3 bucket (Console)

GuardDuty permits you to export findings to an existing bucket in another
AWS account.

When creating a new S3 bucket or choosing an existing bucket in your account, you can
add an optional prefix. When configuring export findings, GuardDuty creates a new folder in
the S3 bucket for your findings. The prefix will be appended to the default folder
structure that GuardDuty created. For example, the format of the optional prefix
`/AWSLogs/`123456789012`/GuardDuty/`Region``.

The entire path of the S3 object will be
``amzn-s3-demo-bucket`/`prefix-name`/UUID`.jsonl.gz``.
The `UUID` is randomly generated and doesn't represent the detector ID
or the finding ID.

###### Important

The KMS key and S3 bucket must be in the same Region.

Before completing these steps, make sure you have attached the respective policies to
your KMS key and existing S3 bucket.

###### To configure export findings

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Settings**.
3. On the **Settings** page, under **Findings export
   options**, for **S3 bucket**, choose
   **Configure now** (or **Edit**, as
   needed).
4. For **S3 bucket ARN**, enter the `**bucket
ARN**`. To find the bucket ARN, see [Viewing the
   properties for an S3 bucket](../../../AmazonS3/latest/userguide/view-bucket-properties.md "../../../AmazonS3/latest/userguide/view-bucket-properties.md") in the
   _Amazon S3 User Guide_.
5. For **KMS key ARN**, enter the **`key
ARN`**. To locate the key ARN, see [Finding the key ID and ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md")
   in the _AWS Key Management Service Developer Guide_.
6. ###### Attach policies
   - Perform the steps to attach the S3 bucket policy. For more
     information, see [Step 3 – Attaching policy
     to Amazon S3 bucket](#guardduty_exportfindings-s3-policies "#guardduty_exportfindings-s3-policies").

   - Perform the steps to attach the KMS key policy. For more
     information, see [Step 2 – Attaching
     policy to your KMS key](#guardduty-exporting-findings-kms-policy "#guardduty-exporting-findings-kms-policy").

7. Choose **Save**.

## Step 5 – Setting frequency

to export updated active findings

Configure the frequency for exporting updated active findings as appropriate for your
environment. By default, updated findings are exported every 6 hours. This means that
any findings that are updated after the most recent export are included in the next
export. If updated findings are exported every 6 hours and the export occurs at 12:00,
any finding that you update after 12:00 is exported at 18:00.

###### To set the frequency

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. Choose **Settings**.
3. In the **Findings export options** section, choose
   **Frequency for updated findings**. This sets the frequency
   for exporting updated Active findings to both EventBridge and Amazon S3. You can choose from
   the following:
   - **Update EventBridge and S3 every 15 minutes**
   - **Update EventBridge and S3 every 1 hour**
   - **Update EventBridge and S3 every 6 hours (default)**

4. Choose **Save changes**.
