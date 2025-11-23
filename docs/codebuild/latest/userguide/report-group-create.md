# Create a report group

You can use the CodeBuild console, the AWS CLI, or a buildspec file to create a report
group. Your IAM role must have the permissions required to create a report group.
For more information, see [Test report permissions](test-permissions.md "test-permissions.md").

###### Topics

- [Create a report group
  (buildspec)](#test-report-group-create-buildspec "#test-report-group-create-buildspec")
- [Create a report group
  (console)](#test-report-group-create-console "#test-report-group-create-console")
- [Create a report group
  (CLI)](#test-report-group-create-cli "#test-report-group-create-cli")
- [Create a report group
  (CloudFormation)](#test-report-group-create-cfn "#test-report-group-create-cfn")

## Create a report group

(buildspec)

A report group created using the buildspec does not export raw test result
files. You can view your report group and specify export settings. For more
information, see [Update a report group](report-group-export-settings.md "report-group-export-settings.md").

###### To create a report group using a buildspec file

1. Choose a report group name that is not associated with a report group
   in your AWS account.
2. Configure the `reports` section of the buildspec file with
   this name. In this example, the report group name is
   `new-report-group` and the use test cases are created
   with the JUnit framework:

```
reports:
 new-report-group: #surefire junit reports
   files:
     - '**/*'
   base-directory: 'surefire/target/surefire-reports'
```

The report group name can also be specified by using environment
variables in the buildspec:

```
version: 0.2
env:
  variables:
    REPORT_GROUP_NAME: "new-report-group"
phases:
  build:
    commands:
      - ...
...
reports:
 $REPORT_GROUP_NAME:
   files:
     - '**/*'
   base-directory: 'surefire/target/surefire-reports'
```

For more information, see [Specify test files](report-group-test-cases.md "report-group-test-cases.md") and [Reports syntax in the buildspec file](build-spec-ref.md#reports-buildspec-file "build-spec-ref.md#reports-buildspec-file"). 3. In the `commands` section, specify the command to run your
tests. For more information, see [Specify test commands](report-group-test-case-commands.md "report-group-test-case-commands.md") . 4. Run the build. When the build is complete, a new report group is
created with a name that uses the format
`project-name-report-group-name`. For more
information, see [Report group naming](test-report-group-naming.md "test-report-group-naming.md").

## Create a report group

(console)

Use the following procedure to create a report group using the AWS Management Console.

###### To create a report group

1.  Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2.  In the navigation pane, choose **Report groups**.
3.  Choose **Create report group**.
4.  For **Report group name**, enter a name for your
    report group.
5.  (Optional) For **Tags**, enter the name and value of any tags that
    you want supporting AWS services to use. Use **Add row** to add a
    tag. You can add up to 50 tags.
6.  If you want to upload the raw data of your test report results to an Amazon S3 bucket:
    1.  Select **Export to Amazon S3**.
    2.  For **S3 bucket name**, enter the name of the
        S3 bucket.
    3.  (Optional) For **S3 bucket owner**, enter the AWS
        account identifier of the account that owns the S3 bucket. This allows
        report data to be exported to an Amazon S3 bucket that is owned by an account
        other than the account running the build.
    4.  For **Path prefix**, enter the path in your
        S3 bucket where you want to upload your test results.
    5.  Select **Compress test result data in a zip file** to
        compress your raw test result data files.
    6.  Expand **Additional configuration** to display encryption
        options. Choose one of the following:

            * **Default AWS managed key** to use a AWS managed key for Amazon S3. For
             more information, see [Customer managed
             CMKs](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the *AWS Key Management Service User Guide*. This is the default
             encryption option.
            * **Choose a custom key** to use a customer managed key that you create and
             configure. For **AWS KMS encryption key**, enter the ARN of your
             encryption key. Its format is `arn:aws:kms:`<region-id>`:
             `<aws-account-id>`:key/`<key-id>``. For more information, see [Creating KMS keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
             *AWS Key Management Service User Guide*.
            * **Disable artifact encryption** to disable encryption. You might choose
             this if you want to share your test results, or publish them to a static website. (A
             dynamic website can run code to decrypt test results.)

        For more information about encryption of data at rest, see [Data encryption](security-encryption.md "security-encryption.md").###### Note

The CodeBuild service role specified in the project is used for permissions to upload to the S3
bucket. 7. Choose **Create report group**.

## Create a report group

(CLI)

Use the following procedure to create a report group using the AWS CLI.

###### To create a report group

1.  Create a file named
    `CreateReportGroup.json`.
2.  Depending on your requirements, copy one of the following JSON code snippets into
    `CreateReportGroup.json`:
    - Use the following JSON to specify that your test report group
      exports raw test result files to an Amazon S3 bucket.

    ```
    {
      "name": "`<report-name>`",
      "type": "TEST",
      "exportConfig": {
        "exportConfigType": "S3",
        "s3Destination": {
          "bucket": "`<bucket-name>`",
          "bucketOwner": "`<bucket-owner>`",
          "path": "`<path>`",
          "packaging": "NONE | ZIP",
          "encryptionDisabled": "false",
          "encryptionKey": "`<your-key>`"
        },
        "tags": [
          {
            "key": "tag-key",
            "value": "tag-value"
          }
        ]
      }
    }

    ```

        + Replace `<bucket-name>` with your Amazon S3
         bucket name and `<path>` with the path
         in your bucket to where you want to export the files.
        + If you want to compress the exported files, for
         `packaging`, specify `ZIP`. Otherwise,
         specify `NONE`.
        + `bucketOwner` is optional and is only required if the
         Amazon S3 bucket is owned by an account other than the account running
         the build.
        + Use `encryptionDisabled` to specify whether to encrypt
         the exported files. If you encrypt the exported files, enter your
         customer managed key. For more information, see [Update a report group](report-group-export-settings.md "report-group-export-settings.md").

    - Use the following JSON to specify that your test report does
      not export raw test files:

    ```
    {
      "name": "`<report-name>`",
      "type": "TEST",
      "exportConfig": {
        "exportConfigType": "NO_EXPORT"
      }
    }

    ```

###### Note

The CodeBuild service role specified in the project is used for permissions to upload to the S3
bucket. 3. Run the following command:

```
aws codebuild create-report-group --cli-input-json file://CreateReportGroupInput.json
```

## Create a report group

(CloudFormation)

Use the following instructions to create a report group using the CloudFormation
template

**To create a report group using the CloudFormation
template**

You can use an CloudFormation template file to create and provision a report group.
For more information, see [CloudFormation User
Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").

The following CloudFormation YAML template creates a report group that does not export
raw test result files.

```
Resources:
  CodeBuildReportGroup:
    Type: AWS::CodeBuild::ReportGroup
    Properties:
      Name: `my-report-group-name`
      Type: TEST
      ExportConfig:
        ExportConfigType: NO_EXPORT

```

The following CloudFormation YAML template creates a report group that exports raw
test result files to an Amazon S3 bucket.

```
Resources:
  CodeBuildReportGroup:
    Type: AWS::CodeBuild::ReportGroup
    Properties:
      Name: `my-report-group-name`
      Type: TEST
      ExportConfig:
        ExportConfigType: S3
        S3Destination:
          Bucket: `amzn-s3-demo-bucket`
          Path: `path-to-folder-for-exported-files`
          Packaging: ZIP
          EncryptionKey: `my-KMS-encryption-key`
          EncryptionDisabled: false

```

###### Note

The CodeBuild service role specified in the project is used for permissions to upload to the S3
bucket.
