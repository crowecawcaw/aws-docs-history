# Update a report group

When you update a report group, you can specify information about whether to
export the raw test result data to files in an Amazon S3 bucket. If you choose to export
to an S3 bucket, you can specify the following for your report group:

- Whether the raw test results files are compressed in a ZIP file.
- Whether the raw test result files are encrypted. You can specify
  encryption with one of the following:

      + An AWS managed key for Amazon S3.
      + A customer managed key that you create and configure.

  For more information, see [Data encryption](security-encryption.md "security-encryption.md").

If you use the AWS CLI to update a report group, you can also update or add tags.
For more information, see [Tag a report group in AWS CodeBuild](how-to-tag-report-group.md "how-to-tag-report-group.md").

###### Note

The CodeBuild service role specified in the project is used for permissions to upload to the S3
bucket.

###### Topics

- [Update a report group
  (console)](#update-report-group-console "#update-report-group-console")
- [Update a report group (CLI)](#update-report-group-cli "#update-report-group-cli")

## Update a report group

(console)

Use the following procedure to update a report group using the AWS Management Console.

###### To update a report group

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. In the navigation pane, choose **Report groups**.
3. Choose the report group you want to update.
4. Choose **Edit**.
5. Select or clear **Backup to Amazon S3**. If you selected
   this option, specify your export settings:
   1. For **S3 bucket name**, enter the name of the
      S3 bucket.
   2. For **Path prefix**, enter the path in your
      S3 bucket where you want to upload your test results.
   3. Select **Compress test result data in a zip
      file** to compress your raw test result data files.
   4. Expand **Additional configuration** to
      display encryption options. Choose one of the following:
      - **Default AWS managed key** to use a AWS managed key for Amazon S3. For
        more information, see [Customer managed
        CMKs](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service User Guide_. This is the default
        encryption option.
      - **Choose a custom key** to use a customer managed key that you create and
        configure. For **AWS KMS encryption key**, enter the ARN of your
        encryption key. Its format is `arn:aws:kms:`<region-id>`:
`<aws-account-id>`:key/`<key-id>``. For more information, see [Creating KMS keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
        _AWS Key Management Service User Guide_.
      - **Disable artifact encryption** to disable encryption. You might choose
        this if you want to share your test results, or publish them to a static website. (A
        dynamic website can run code to decrypt test results.)

## Update a report group (CLI)

Use the following procedure to update a report group using the AWS CLI.

###### To update a report group

1. Create a file named
   `UpdateReportGroupInput.json`.
2. Copy the following into
   `UpdateReportGroupInput.json`:

```
{
    "arn": "",
    "exportConfig": {
        "exportConfigType": "S3",
        "s3Destination": {
            "bucket": "`bucket-name`",
            "path": "`path`",
            "packaging": "NONE | ZIP",
            "encryptionDisabled": "false",
            "encryptionKey": "`your-key`"
         }
     },
     "tags": [
        {
            "key": "tag-key",
            "value": "tag-value"
        }
     ]
}

```

3. Enter the ARN of your report group in the `arn` line (for
   example,
   `"arn":"arn:aws:codebuild:`region`:`123456789012`:report-group/`report-group-1`")`.
4. Update `UpdateReportGroupInput.json` with the
   updates you want to apply to your report group.
   - If you want to update your report group to export raw test
     result files to an S3 bucket, update the
     `exportConfig` section. Replace
     `bucket-name` with your S3 bucket name and
     `path` with the path in your S3 bucket that you
     want to export the files to. If you want to compress the
     exported files, for `packaging`, specify
     `ZIP`. Otherwise, specify `NONE`. Use
     `encryptionDisabled` to specify whether to
     encrypt the exported files. If you encrypt the exported files,
     enter your customer managed key.
   - If you want to update your report group so that it does not
     export raw test result files to an S3 bucket, update the
     `exportConfig` section with the following JSON:

   ```
   {
     "exportConfig": {
         "exportConfigType": "NO_EXPORT"
     }
   }
   ```

   - If you want to update the report group's tags, update the
     `tags` section. You can change, add, or remove
     tags. If you want to remove all tags, update it with the
     following JSON:

   ```
   "tags": []
   ```

5. Run the following command:

```
aws codebuild update-report-group \
--cli-input-json file://UpdateReportGroupInput.json
```
