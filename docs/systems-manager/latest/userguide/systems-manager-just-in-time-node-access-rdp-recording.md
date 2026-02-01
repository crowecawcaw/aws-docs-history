• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Recording

RDP connections

Just-in-time node access includes the ability to record RDP connections made to
your Windows Server nodes. Recording RDP connections require an S3 bucket and an AWS Key Management Service
(AWS KMS) customer managed key. The AWS KMS key is used to temporarily encrypt the recording
data while it's generated and stored on Systems Manager resources. The customer managed key must be a
symmetric key with a key usage of encrypt and decrypt. You can either use a
multi-Region key for your organization, or you must create a customer managed key in each
Region where you've enabled just-in-time node access.

If you have enabled KMS encryption on the S3 bucket where you store recordings,
you must provide access to the customer managed key used for bucket encryption to the
`ssm-guiconnect` service principal. This customer managed key can be a
different one than you specify in the recording settings, which must include for
which the `kms:CreateGrant` permission is required for establishing
connections.

## Configuring S3 bucket

encryption for RDP recordings

Your connection recordings are stored in the S3 bucket that you specify when
you enable RDP recording.

If you use a KMS key as the default encryption mechanism for the S3 bucket
(SSE-KMS), you must allow the `ssm-guiconnect` service principal
access to `kms:GenerateDataKey` action on the key. We recommend using
a customer managed key when using SSE-KMS encryption with S3 bucket. This is because you
can update the associated key policy for a customer managed key. You can't update the key
policies for AWS managed keys.

###### Important

You must tag the AWS KMS keys used for Session Manager encryption and RDP recording
in just-in-time node access with the tag key
`SystemsManagerJustInTimeNodeAccessManaged` and tag value
`true`.

For information about tagging KMS keys, see [Tags in AWS KMS](../../../kms/latest/developerguide/tagging-keys.md "../../../kms/latest/developerguide/tagging-keys.md")
in the _AWS Key Management Service Developer Guide_.

Use the following customer managed key policy to allow the `ssm-guiconnect`
service access to the KMS key for S3 storage. For information about updating a
customer managed key, see [Change a key
policy](../../../kms/latest/developerguide/key-policy-modifying.md "../../../kms/latest/developerguide/key-policy-modifying.md") in the _AWS Key Management Service Developer Guide_.

Replace each `example resource placeholder` with your
own information:

- `account-id` represents the ID of the
  AWS account that initiates the connection.
- `region` represents the AWS Region where
  the S3 bucket is located . (You can use `*` if the bucket
  will receive recordings from multiple Regions. Example:
  `s3.*.amazonaws.com`.)

###### Note

You can use `aws:SourceOrgID` in the policy instead of
`aws:SourceAccount` if the account belongs to an organization
in AWS Organizations.

```
{
    "Sid": "Allow the GUI Connect service principal to access S3",
    "Effect": "Allow",
    "Principal": {
        "Service": "ssm-guiconnect.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey*"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "`account-id`"
        },
        "StringLike": {
            "kms:ViaService": "s3.`region`.amazonaws.com"
        }
    }
}
```

## Configuring IAM

permissions for recording RDP connections

In addition to the required IAM permissions for just-in-time node access,
the user or role you use must be allowed the following permissions based on the
task you need to perform.

###### Permissions for configuring connection recording

To configure RDP connection recording, the following permissions are
required:

- `ssm-guiconnect:UpdateConnectionRecordingPreferences`
- `ssm-guiconnect:GetConnectionRecordingPreferences`
- `ssm-guiconnect:DeleteConnectionRecordingPreferences`
- `kms:CreateGrant`

###### Permissions for initiating connections

To make RDP connections with just-in-time node access, the following
permissions are required:

- `ssm-guiconnect:CancelConnection`
- `ssm-guiconnect:GetConnection`
- `ssm-guiconnect:StartConnection`
- `kms:CreateGrant`

###### Before you begin

To store your connection recordings, you must first create an S3 bucket and
add the following bucket policy. Replace each `example resource
 placeholder` with your own information.

(For information about adding a bucket policy, see [Adding a bucket policy by
using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the
_Amazon Simple Storage Service User Guide_.)

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ConnectionRecording",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "ssm-guiconnect.amazonaws.com"
 ]
 },
 "Action": "s3:PutObject",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition":{
 "StringEquals":{
 "aws:SourceAccount":"`111122223333`"
 }
 }
 }
 ]
}`

```

## Enabling and configuring RDP

connection recording

The following procedure describes how to enable and configure RDP connection
recording.

###### To enable and configure RDP connection recording

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Settings** in the navigation pane.
3. Select the **Just-in-time node access** tab.
4. In the **RDP recording** section, select
   **Enable RDP recording**.
5. Choose the S3 bucket you want to upload session recordings to.
6. Choose the customer managed key you want to use to temporarily encrypt the
   recording data while it's generated and stored on Systems Manager resources. (This
   can be a different customer managed key than you use to encrypt the
   bucket.)
7. Select **Save**.

## RDP connection recording status

values

Valid status values for RPD connection recordings include the
following:

- `Recording` - The connection is in the process of being
  recorded
- `Processing` - The video is being processed after the
  connection is terminated.
- `Finished` - Successful terminal state:The connection
  recording video processed successfully and uploaded to the specified
  bucket.
- `Failed` - Failed terminal state. The connection wasn't
  recorded successfully.
- `ProcessingError` - One or more intermediate
  failures/errors occurred during video processing. Potential causes
  include service dependency failures or missing permissions due to a
  misconfiguration on the S3 bucket specified for storing recordings. The
  service continues to attempt processing when the recording is in this
  state.

###### Note

`ProcessingError` can be the result of the
`ssm-guiconnect` service principal not having permission to
upload objects to the S3 bucket after the connection has been established.
Another potential cause is missing KMS permissions on the KMS key used for
S3 bucket encryption.
