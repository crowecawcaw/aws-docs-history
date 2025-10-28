# Generating the account

status report for declarative policies

The _account status report_ allows you to review the current status of
all attributes supported by declarative policies for the accounts in scope. You can choose
the accounts and organizational units (OUs) to include in the report scope, or choose an
entire organization by selecting the root.

This report helps you assess readiness by providing a Region breakdown and if the current
state of an attribute is _uniform across accounts_ (through the
`numberOfMatchedAccounts`) or _inconsistent_ (through the
`numberOfUnmatchedAccounts`). You can also see the _most frequent
value_, which is the configuration value that is most frequently observed for
the attribute.

The choice to attach a declarative policy for enforcing a baseline configuration depends
on your specific use case.

For more information and an illustrative example, see [Account status
report for declarative policies](orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-account-status-report "orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-account-status-report").

## Prerequisites

Before you can generate an account status report, you must perform the following
steps

1. The `StartDeclarativePoliciesReport` API can only be called by the
   management account or delegated administrators for an organization.
2. You must have an S3 bucket before generating the report (create a new one or
   use an existing one), it must be in the same Region in which the request is
   made, and it must have an appropriate S3 bucket policy. For a sample S3 policy,
   see _Sample Amazon S3 policy_ under [Examples](../../../AWSEC2/latest/APIReference/API_StartDeclarativePoliciesReport.md#API_StartDeclarativePoliciesReport_Examples "../../../AWSEC2/latest/APIReference/API_StartDeclarativePoliciesReport.md#API_StartDeclarativePoliciesReport_Examples") in the _Amazon EC2 API Reference_
3. You must enable trusted access for the service where the declarative policy
   will enforce a baseline configuration. This creates a read-only service-linked
   role that is used to generate the account status report of what the existing
   configuration is for accounts across your organization.

**Using the console**

For the Organizations console, this step is a part of the process for enabling
declarative policies.

**Using the AWS CLI**

For the AWS CLI, use the [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md") API.

For more information on how to enable trusted access for a specific service
with the AWS CLI see, [AWS services that you can use with AWS Organizations](orgs_integrate_services_list.md "orgs_integrate_services_list.md"). 4. Only one report per organization can be generated at a time. Attempting to
generate a report while another is in progress will result in an error.

## Access the

compliance status report

###### Minimum permissions

To generate a compliance status report, you need permission to run the following
actions:

- `ec2:StartDeclarativePoliciesReport`
- `ec2:DescribeDeclarativePoliciesReports`
- `ec2:GetDeclarativePoliciesReportSummary`
- `ec2:CancelDeclarativePoliciesReport`
- `organizations:DescribeAccount`
- `organizations:DescribeOrganization`
- `organizations:DescribeOrganizationalUnit`
- `organizations:ListAccounts`
- `organizations:ListDelegatedAdministrators`
- `organizations:ListAWSServiceAccessForOrganization`
- `s3:PutObject`

###### Note

If your Amazon S3 bucket uses SSE-KMS encryption, you must also include the
`kms:GenerateDataKey` permission in the policy.

AWS Management Console
Use the following procedure to generate an account status report.

###### To generate an account status report

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **Policies** page, choose
   **Declarative policies for EC2**.
3. On the **Declarative policies for EC2** page,
   choose **View account status report** from the
   **Actions** dropdown menu.
4. On the **View account status report** page,
   choose **Generate status report**.
5. In the **Organizational structure** widget,
   specify which organizational units (OUs) you want to include in the
   report.
6. Choose **Submit**.

AWS CLI & AWS SDKs
**To generate an account status
report**

Use the following operations to generate a compliance status report, check
on its status, and view the report:

- `ec2:start-declarative-policies-report`: Generates an
  account status report. The report is generated asynchronously, and
  can take several hours to complete. For more information, see [StartDeclarativePoliciesReport](../../../AWSEC2/latest/APIReference/API_StartDeclarativePoliciesReport.md "../../../AWSEC2/latest/APIReference/API_StartDeclarativePoliciesReport.md") in the _Amazon EC2
  API Reference_.
- `ec2:describe-declarative-policies-report`: Describes
  the metadata of an account status report, including the state of the
  report. For more information, see [DescribeDeclarativePoliciesReports](../../../AWSEC2/latest/APIReference/API_DescribeDeclarativePoliciesReports.md "../../../AWSEC2/latest/APIReference/API_DescribeDeclarativePoliciesReports.md") in the
  _Amazon EC2 API Reference_.
- `ec2:get-declarative-policies-report-summary`:
  Retrieves a summary of the account status report. For more
  information, see [GetDeclarativePoliciesReportSummary](../../../AWSEC2/latest/APIReference/API_GetDeclarativePoliciesReportSummary.md "../../../AWSEC2/latest/APIReference/API_GetDeclarativePoliciesReportSummary.md") in the
  _Amazon EC2 API Reference_.
- `ec2:cancel-declarative-policies-report`: Cancels the
  generation of an account status report. For more information, see
  [CancelDeclarativePoliciesReport](../../../AWSEC2/latest/APIReference/API_CancelDeclarativePoliciesReport.md "../../../AWSEC2/latest/APIReference/API_CancelDeclarativePoliciesReport.md") in the _Amazon EC2
  API Reference_.

Before generating a report, grant the EC2 declarative policies principal
access to the Amazon S3 bucket where the report will be stored. To do this,
attach the following policy to the bucket. Replace
`amzn-s3-demo-bucket` with your actual Amazon S3 bucket name, and
`identity_ARN` with the IAM identity used to call the
`StartDeclarativePoliciesReport` API.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DeclarativePoliciesReportDelivery",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`identity_ARN`"
 },
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "organizations.amazonaws.com"
 }
 }
 }
 ]
}`

```
