# Automatically exporting AWS Data Exchange asset

revisions to an S3 bucket as a subscriber

When the provider publishes new revisions, you can select to automatically export new
revisions to your Amazon S3 bucket. You can export new revisions to up to five S3 buckets. New
revisions will automatically appear in the S3 buckets you have selected.

###### Topics

- [Prerequisites for S3 bucket
  policy permissions](#auto-export-rev-s3-bucket-policy-prereq "#auto-export-rev-s3-bucket-policy-prereq")
- [Automatically exporting revisions to
  an S3 bucket as a subscriber (console)](#auto-export-rev-s3-console-sub-proc "#auto-export-rev-s3-console-sub-proc")
- [Automatically exporting revisions to an S3
  bucket as a subscriber (AWS SDKs)](#auto-export-rev-s3-prog-sub "#auto-export-rev-s3-prog-sub")

###### Note

To automatically export revisions to an S3 bucket of your choice, your S3 bucket must
have a bucket policy with permissions set to allow AWS Data Exchange to export data into it. For more
information, see [Prerequisites for S3 bucket
policy permissions](#auto-export-rev-s3-bucket-policy-prereq "#auto-export-rev-s3-bucket-policy-prereq").

## Prerequisites for S3 bucket

policy permissions

Before you can automatically export revisions to an Amazon S3 bucket,
you must
disable
requester pays and your Amazon S3 bucket must have a bucket policy with
permissions set to allow AWS Data Exchange to export data into it. The following procedures provide
information about how to either edit your existing S3 bucket policy or create an S3 bucket
policy with these permissions.

If your S3 bucket is configured for SSE-KMS encryption, the user configuring the
auto-export job must have `CreateGrant` permission on the KMS key for AWS Data Exchange
to copy the objects into your S3 bucket.

###### Important

To verify that the prerequisites for S3 bucket policy permissions are met, an object
with the naming format `_ADX-TEST-ACCOUNTID#` is added to the S3 bucket
during the automatic export process.

###### Topics

- [Editing an existing S3
  bucket policy](#bucket-policy-prereq-existing-s3-bucket-policy "#bucket-policy-prereq-existing-s3-bucket-policy")
- [Creating an S3 bucket
  policy](#bucket-policy-prereq-create-s3-bucket-policy "#bucket-policy-prereq-create-s3-bucket-policy")

### Editing an existing S3

bucket policy

If your S3 bucket has a bucket policy, complete the following procedure to allow
AWS Data Exchange to export data to it.

###### To edit an existing S3 bucket policy

1. Navigate to the bucket to which you want to export revisions.
2. Select the **Permissions** tab, and choose
   **Edit** in the bucket policy section.
3. Copy the following statement and paste it at the end of the statement
   list.

```

    {
      "Effect": "Allow",
      "Principal": {
      "Service": "dataexchange.amazonaws.com"
      },
      "Action": [
        "s3:PutObject",
        "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::<BUCKET-NAME>/*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<AWS ID>"
        }
      }
    }

```

4. Replace `<BUCKET-NAME>` with the name of your S3 bucket and
   replace `<AWS ID>` with your AWS ID.
5. Choose **Save changes**.
6. If you want to add more buckets as a destination for your auto-export jobs,
   repeat the procedure, starting from Step 1.

### Creating an S3 bucket

policy

If your S3 bucket does not have a bucket policy, complete the following procedure to
create an S3 bucket policy to allow AWS Data Exchange to export data to it.

###### To create an S3 bucket policy

1. Navigate to the bucket to which you want to export revisions.
2. Select the **Permissions** tab, and choose
   **Edit** in the bucket policy section.
3. Copy the following full bucket policy and paste it into the bucket policy
   editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "dataexchange.amazonaws.com"
 },
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::<BUCKET-NAME>/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "<AWS ID>"
 }
 }
 }
 ]
}`

```

4. Replace `<BUCKET-NAME>` with the name of your S3 bucket and
   replace `<AWS ID>` with your AWS ID.
5. Choose **Save changes**.
6. If you want to add more buckets as a destination for your auto-export jobs,
   repeat the procedure, starting from Step 1.

## Automatically exporting revisions to

an S3 bucket as a subscriber (console)

###### Note

To automatically export revisions to an S3 bucket of your choice, your S3 bucket
must have a bucket policy with permissions set to allow AWS Data Exchange to export data into it.
For more information, see [Prerequisites for S3 bucket
policy permissions](#auto-export-rev-s3-bucket-policy-prereq "#auto-export-rev-s3-bucket-policy-prereq").

###### To automatically export a revision to an S3 bucket as a subscriber

(console)

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, for **My subscriptions**,
   choose **Entitled data**.
3. In **Entitled data**, choose the product that has the revision
   you want to export.
4. In **Entitled data sets**, choose the data set.
5. On the **Revisions** tab, under **Auto-export job
   destinations**, choose **Actions** and then choose
   **Add auto-export job destination**.
6. In **Add auto-export job destination**, choose either the
   **Simple** or **Advanced** destination
   option.
   1. If you choose the **Simple** option, select the Amazon S3 bucket
      folder destination from the dropdown list and the encryption options, and then
      choose **Add bucket destination**.
   2. If you choose the **Advanced** option, select the Amazon S3 bucket
      folder destination from the dropdown list, select the [Key naming pattern](revision-export-keypatterns.md "revision-export-keypatterns.md") and append it to
      the path.

7. Review the **Output**.
8. Set the **Encryption options**, review the **Amazon S3
   pricing**, and then choose **Add bucket
   destination**.

The Amazon S3 bucket destination appears on the **Revisions** tab
under **Auto-export job destinations**.

A job is started to automatically export your revision.

To verify that the prerequisites for S3 bucket policy permissions are met, an
object with the naming format `_ADX-TEST-ACCOUNTID#` is added to the S3
bucket.

After the job is finished, the **State** field in the
**Jobs** section is updated to
**Completed**.

To add another destination, choose **Actions**, and then
**Add auto-export job destination**.

To edit, select the destination you want to edit, choose
**Actions**, and then **Edit destination
configuration**.

To delete, choose **Actions**, and then choose **Remove
auto-export job destination**.

## Automatically exporting revisions to an S3

bucket as a subscriber (AWS SDKs)

###### Note

To automatically export revisions to an S3 bucket of your choice, your S3 bucket
must have a bucket policy with permissions set to allow AWS Data Exchange to export data into it.
For more information, see [Prerequisites for S3 bucket
policy permissions](#auto-export-rev-s3-bucket-policy-prereq "#auto-export-rev-s3-bucket-policy-prereq").

###### To automatically export a revision to an S3 bucket (AWS SDKs)

1. Create a `Create_Event_Action` request.
2. Include the following in the request:
   - `Action`
     - `ExportRevisionToS3`
       - `Encryption`
         - `KmsKeyArn`
         - `Type`

     - `RevisionDestination`
       - `Bucket`
       - `KeyPattern`

   - `Event`
     - `RevisionPublished`
       - `DataSetId`

   - `Tags`

3. Modify the key pattern if necessary. The Amazon S3 object key defaults to the key
   pattern `{Revision.CreatedAt}/{Asset.Name}`.

For more information about key patterns, see [Key patterns when exporting asset revisions
from AWS Data Exchange](revision-export-keypatterns.md "revision-export-keypatterns.md").

To verify that the prerequisites for S3 bucket policy permissions are met, an
object with the naming format `_ADX-TEST-ACCOUNTID#` is added to the S3
bucket.
