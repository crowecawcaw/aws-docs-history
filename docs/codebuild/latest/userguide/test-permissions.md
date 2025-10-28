# Test report permissions

This topic describes important information about permissions related to test
reporting.

###### Topics

- [IAM role for test reports](#test-permissions-required "#test-permissions-required")
- [Permissions for test
  reporting operations](#test-permissions-related-to-reporting "#test-permissions-related-to-reporting")
- [Test reporting permissions
  examples](#test-permissions-examples "#test-permissions-examples")

## IAM role for test reports

To run a test report, and to update a project to include test reports, your IAM
role requires the following permissions. These permissions are included in the
predefined AWS managed policies. If you want to add test reporting to an existing
build project, you must add these permissions yourself.

- `CreateReportGroup`
- `CreateReport`
- `UpdateReport`
- `BatchPutTestCases`

To run a code coverage report, your IAM role must also include the
`BatchPutCodeCoverages` permission.

###### Note

`BatchPutTestCases`, `CreateReport`,
`UpdateReport`, and `BatchPutCodeCoverages` are not
public permissions. You cannot call a corresponding AWS CLI command or SDK method
for these permissions.

To make sure you have these permissions, you can attach the following policy to
your IAM role:

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
        "codebuild:BatchPutTestCases",
        "codebuild:BatchPutCodeCoverages"
    ]
}
```

We recommend that you restrict this policy to only those report groups you must
use. The following restricts permissions to only the report groups with the two ARNs
in the policy:

```
{
    "Effect": "Allow",
    "Resource": [
        "arn:aws:codebuild:your-region:your-aws-account-id:report-group/report-group-name-1",
        "arn:aws:codebuild:your-region:your-aws-account-id:report-group/report-group-name-2"
    ],
    "Action": [
        "codebuild:CreateReportGroup",
        "codebuild:CreateReport",
        "codebuild:UpdateReport",
        "codebuild:BatchPutTestCases",
        "codebuild:BatchPutCodeCoverages"
    ]
}
```

The following restricts permissions to only report groups created by running
builds of a project named `my-project`:

```
{
    "Effect": "Allow",
    "Resource": [
        "arn:aws:codebuild:your-region:your-aws-account-id:report-group/my-project-*"
    ],
    "Action": [
        "codebuild:CreateReportGroup",
        "codebuild:CreateReport",
        "codebuild:UpdateReport",
        "codebuild:BatchPutTestCases",
        "codebuild:BatchPutCodeCoverages"
    ]
}
```

###### Note

The CodeBuild service role specified in the project is used for permissions to upload to the S3
bucket.

## Permissions for test

reporting operations

You can specify permissions for the following test reporting CodeBuild API
operations:

- `BatchGetReportGroups`
- `BatchGetReports`
- `CreateReportGroup`
- `DeleteReportGroup`
- `DeleteReport`
- `DescribeTestCases`
- `ListReportGroups`
- `ListReports`
- `ListReportsForReportGroup`
- `UpdateReportGroup`

For more information, see [AWS CodeBuild permissions
reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

## Test reporting permissions

examples

For information about sample policies related to test reporting, see the
following:

- [Allow a
  user to change a report group](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-change-report-group "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-change-report-group")
- [Allow a
  user to create a report group](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-create-report-group "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-create-report-group")
- [Allow a user
  to delete a report](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-delete-report "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-delete-report")
- [Allow a
  user to delete a report group](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-delete-report-group "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-delete-report-group")
- [Allow a user to get information about report groups](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-get-information-about-report-group "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-get-information-about-report-group")
- [Allow
  a user to get information about reports](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-get-information-about-reports "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-get-information-about-reports")
- [Allow a user to get a list of report groups](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-get-list-of-report-groups "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-get-list-of-report-groups")
- [Allow a
  user to get a list of reports](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-get-list-of-reports "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-get-list-of-reports")
- [Allow a user to get a list of reports for a report group](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-get-list-of-reports-for-report-group "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-get-list-of-reports-for-report-group")
- [Allow a user to get a list of test cases for a report](auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-get-list-of-test-cases-for-report "auth-and-access-control-iam-identity-based-access-control.md#customer-managed-policies-example-get-list-of-test-cases-for-report")
