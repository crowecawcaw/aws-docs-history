# 'Test report using the AWS CLI' sample

Tests that you specify in your buildspec file are run during your build. This sample
shows you how to use the AWS CLI to incorporate tests into builds in CodeBuild. You can use JUnit
to create unit tests, or you can use another tool to create configuration tests. You can
then evaluate the test results to fix issues or optimize your application.

You can use the CodeBuild API or the AWS CodeBuild console to access the test results. This sample
shows you how to configure your report so its test results are exported to an S3 bucket.

###### Topics

- [Run the test report sample](#sample-test-report-cli-run "#sample-test-report-cli-run")

## Run the test report sample

Use the following steps to run the trest report sample.

###### Topics

- [Prerequisites](#sample-test-report-cli-prerequisites "#sample-test-report-cli-prerequisites")
- [Step 1: Create a report
  group](#sample-test-report-cli-create-report "#sample-test-report-cli-create-report")
- [Step 2:
  Configure a project with a report group](#sample-test-report-cli-create-project-with-report "#sample-test-report-cli-create-project-with-report")
- [Step 3: Run and
  view results of a report](#sample-test-report-cli-run-and-view-report-results "#sample-test-report-cli-run-and-view-report-results")

### Prerequisites

- Create your test cases. This sample is written with the assumption that
  you have test cases to include in your sample test report. You specify the
  location of your test files in the buildspec file.

The following test report file formats are supported:

    + Cucumber JSON (.json)
    + JUnit XML (.xml)
    + NUnit XML (.xml)
    + NUnit3 XML (.xml)
    + TestNG XML (.xml)
    + Visual Studio TRX (.trx)
    + Visual Studio TRX XML (.xml)

Create your test cases with any test framework that can create report
files in one of these formats (for example, Surefire JUnit plugin, TestNG,
or Cucumber).

- Create an S3 bucket and make a note of its name. For more information, see
  [How do I create an
  S3 bucket?](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md") in the _Amazon S3 User Guide_.
- Create an IAM role and make a note of its ARN. You need the ARN when you
  create your build project.
- If your role does not have the following permissions, add them.

```
{
    "Effect": "Allow",
    "Resource": [
        "*"
    ],
    "Action": [
        "codebuild:CreateReportGroup",
        "codebuild:CreateReport",
        "codebuild:UpdateReport",
        "codebuild:BatchPutTestCases"
    ]
}
```

For more information, see [Permissions for test
reporting operations](test-permissions.md#test-permissions-related-to-reporting "test-permissions.md#test-permissions-related-to-reporting").

### Step 1: Create a report

group

1. Create a file named `CreateReportGroupInput.json`.
2. Create a folder in your S3 bucket where your test results are exported.
3. Copy the following into `CreateReportGroupInput.json`.
   For `<bucket-name>`, use the name
   of the S3 bucket. For
   `<path-to-folder>`, enter the
   path to the folder in your S3 bucket.

```
{
  "name": "`<report-name>`",
  "type": "TEST",
  "exportConfig": {
    "exportConfigType": "S3",
    "s3Destination": {
      "bucket": "`<bucket-name>`",
      "path": "`<path-to-folder>`",
      "packaging": "NONE"
    }
  }
}
```

4. Run the following command in the directory that contains
   `CreateReportGroupInput.json`.

```
aws codebuild create-report-group --cli-input-json file://CreateReportGroupInput.json
```

The output looks like the following. Make a note of the ARN for the
`reportGroup`. You use it when you create a project that uses
this report group.

```
{
  "reportGroup": {
    "arn": "arn:aws:codebuild:us-west-2:123456789012:report-group/`<report-name>`",
    "name": "`<report-name>`",
    "type": "TEST",
    "exportConfig": {
      "exportConfigType": "S3",
      "s3Destination": {
        "bucket": "`<s3-bucket-name>`",
        "path": "`<folder-path>`",
        "packaging": "NONE",
        "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3"
      }
    },
    "created": 1570837165.885,
    "lastModified": 1570837165.885
  }
}
```

### Step 2:

Configure a project with a report group

To run a report, you first create a CodeBuild build project that is configured with
your report group. Test cases specified for your report group are run when you run a
build.

1. Create a buildspec file named `buildspec.yml`.
2. Use the following YAML as a template for your
   `buildspec.yml` file. Be sure to include the commands
   that run your tests. In the `reports` section, specify the files
   that contain the results of your test cases. These files store the test
   results you can access with CodeBuild. They expire 30 days after they are
   created. These files are different from the raw test case result files you
   export to an S3 bucket.

```
version: 0.2
    phases:
    install:
        runtime-versions:
            java: openjdk8
    build:
      commands:
        - echo Running tests
        - `<enter commands to run your tests>`

    reports:
      `<report-name-or-arn>`: #test file information
      files:
        - '`<test-result-files>`'
      base-directory: '`<optional-base-directory>`'
      discard-paths: false #do not remove file paths from test result files
```

###### Note

Instead of the ARN of an existing report group, you can also specify a
name for a report group that has not been created. If you specify a name
instead of an ARN, CodeBuild creates a report group when it runs a build.
Its name contains your project name and the name you specify in the
buildspec file, in this format:
`project-name-report-group-name`. For more
information, see [Create test reports](report-create.md "report-create.md") and [Report group naming](test-report-group-naming.md "test-report-group-naming.md"). 3. Create a file named `project.json`. This file contains
input for the **create-project** command. 4. Copy the following JSON into `project.json`. For
`source`, enter the type and location of the repository that
contains your source files. For `serviceRole`, specify the ARN of
the role you are using.

```
{
  "name": "test-report-project",
  "description": "sample-test-report-project",
  "source": {
    "type": "CODECOMMIT|CODEPIPELINE|GITHUB|S3|BITBUCKET|GITHUB_ENTERPRISE|NO_SOURCE",
    "location": "`<your-source-url>`"
  },
  "artifacts": {
    "type": "NO_ARTIFACTS"
  },
  "cache": {
    "type": "NO_CACHE"
  },
  "environment": {
    "type": "LINUX_CONTAINER",
    "image": "aws/codebuild/standard:5.0",
    "computeType": "small"
  },
  "serviceRole": "arn:aws:iam::`<your-aws-account-id>`:role/service-role/`<your-role-name>`"
}
```

5. Run the following command in the directory that contains
   `project.json`. This creates a project named
   `test-project`.

```
aws codebuild create-project --cli-input-json file://project.json
```

### Step 3: Run and

view results of a report

In this section, you run a build of the project you created earlier. During the
build process, CodeBuild creates a report with the results of the test cases. The report
is contained in the report group you specified.

1. To start a build, run the following command.
   `test-report-project` is the name of the build project
   created above. Make a note of the build ID that appears in the output.

```
aws codebuild start-build --project-name test-report-project
```

2. Run the following command to get information about your build, including
   the ARN of your report. For
   `<build-id>`, specify your
   build ID. Make a note of the report ARN in the `reportArns`
   property of the output.

```
aws codebuild batch-get-builds --ids `<build-id>`
```

3. Run the following command to get details about your report. For
   `<report-arn>`, specify
   your report ARN.

```
aws codebuild batch-get-reports --report-arns `<report-arn>`
```

The output looks like the following. This sample output shows how many of
the tests were successful, failed, skipped, resulted in an error, or return
an unknown status.

```
{
  "reports": [
    {
      "status": "FAILED",
      "reportGroupArn": "`<report-group-arn>`",
      "name": "`<report-group-name>`",
      "created": 1573324770.154,
      "exportConfig": {
        "exportConfigType": "S3",
        "s3Destination": {
          "bucket": "<amzn-s3-demo-bucket>",
          "path": "<path-to-your-report-results>",
          "packaging": "NONE",
          "encryptionKey": "<encryption-key>"
        }
      },
      "expired": 1575916770.0,
      "truncated": false,
      "executionId": "arn:aws:codebuild:us-west-2:123456789012:build/`<name-of-build-project>`:2c254862-ddf6-4831-a53f-6839a73829c1",
      "type": "TEST",
      "arn": "`<report-arn>`",
      "testSummary": {
        "durationInNanoSeconds": 6657770,
        "total": 11,
        "statusCounts": {
          "FAILED": 3,
          "SKIPPED": 7,
          "ERROR": 0,
          "SUCCEEDED": 1,
          "UNKNOWN": 0
        }
      }
    }
  ],
  "reportsNotFound": []
}
```

4. Run the following command to list information about test cases for your
   report. For `<report-arn>`, specify
   the ARN of your report. For the optional `--filter` parameter,
   you can specify one status result (`SUCCEEDED`,
   `FAILED`, `SKIPPED`, `ERROR`, or
   `UNKNOWN`).

```
aws codebuild describe-test-cases \
    --report-arn `<report-arn>` \
    --filter status=SUCCEEDED|FAILED|SKIPPED|ERROR|UNKNOWN
```

The output looks like the following.

```
{
  "testCases": [
    {
      "status": "FAILED",
      "name": "Test case 1",
      "expired": 1575916770.0,
      "reportArn": "`<report-arn>`",
      "prefix": "Cucumber tests for agent",
      "message": "A test message",
      "durationInNanoSeconds": 1540540,
      "testRawDataPath": "`<path-to-output-report-files>`"
    },
    {
      "status": "SUCCEEDED",
      "name": "Test case 2",
      "expired": 1575916770.0,
      "reportArn": "`<report-arn>`",
      "prefix": "Cucumber tests for agent",
      "message": "A test message",
      "durationInNanoSeconds": 1540540,
      "testRawDataPath": "`<path-to-output-report-files>`"
    }
  ]
}
```
