

# Generating the account status report for EC2 policies
<a name="orgs_manage_policies_ec2_status-report"></a>

The *account status report* allows you to review the current status of all attributes supported by EC2 policies for the accounts in scope. You can choose the accounts and organizational units (OUs) to include in the report scope, or choose an entire organization by selecting the root.

This report helps you assess readiness by providing a Region breakdown and if the current state of an attribute is *uniform across accounts* (through the `numberOfMatchedAccounts`) or *inconsistent* (through the `numberOfUnmatchedAccounts`). You can also see the *most frequent value*, which is the configuration value that is most frequently observed for the attribute.

Whether to attach an EC2 policy for enforcing a baseline configuration depends on your specific use case.

For more information and an illustrative example, see [Account status report for EC2 policies](orgs_manage_policies_ec2.md#orgs_manage_policies_ec2-account-status-report).

## Prerequisites
<a name="orgs_manage_policies_ec2_accessing-status-report-prerequisites"></a>

Before you can generate an account status report, complete the following steps:

1. The `StartDeclarativePoliciesReport` operation can only be called by the management account or delegated administrators for an organization.

1. To run reports from a delegated administrator account, the account must be registered as a delegated administrator for the EC2 service.

1. You must have an S3 bucket before you generate the report. Create a new bucket or use an existing one. The bucket must be in the same Region where you make the request. The bucket must have an appropriate bucket policy. For a sample S3 policy, see *Sample Amazon S3 policy* under [Examples ](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartDeclarativePoliciesReport.html#API_StartDeclarativePoliciesReport_Examples) in the *Amazon EC2 API Reference*. 

1. You must enable trusted access for Amazon EC2. This creates a read-only service-linked role that generates the account status report of the existing configuration for accounts across your organization.

   **Using the console**

   For the Organizations console, this step is a part of the process for enabling EC2 policies.

   **Using the AWS CLI**

   For the AWS CLI, use the [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html) operation.

   For more information about how to enable trusted access for a specific service with the AWS CLI, see [AWS services that you can use with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html).

1. Only one report per organization can be generated at a time. If you generate a report while another is in progress, the operation returns an error.

## Generating the compliance status report
<a name="orgs_manage_policies_ec2_accessing-status-report"></a>

**Minimum permissions**  
To generate a compliance status report, you need permission to run the following operations:  
`ec2:StartDeclarativePoliciesReport`
`ec2:DescribeDeclarativePoliciesReports`
`ec2:GetDeclarativePoliciesReportSummary`
`ec2:CancelDeclarativePoliciesReport`
`organizations:DescribeAccount`
`organizations:DescribeOrganization`
`organizations:DescribeOrganizationalUnit`
`organizations:ListAccounts`
`organizations:ListDelegatedAdministrators`
`organizations:ListAWSServiceAccessForOrganization`
`s3:PutObject`

**Note**  
If your Amazon S3 bucket uses SSE-KMS encryption, you must also include the `kms:GenerateDataKey` permission in the policy.

------
#### [ AWS Management Console ]

Use the following procedure to generate an account status report.

**To generate an account status report**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. On the **Policies** page, choose **EC2 policies**.

1. On the **EC2 policies** page, choose **View account status report** from the **Actions** dropdown menu.

1. On the **View account status report** page, choose **Generate status report**.

1. In the **Organizational structure** widget, specify which organizational units (OUs) you want to include in the report.

1. Choose **Submit**.

------
#### [ AWS CLI & AWS SDKs ]

**To generate an account status report**

Use the following operations to generate a compliance status report, check on its status, and view the report:
+ `ec2:start-declarative-policies-report`: Generates an account status report. The report is generated asynchronously, and can take several hours to complete. For more information, see [StartDeclarativePoliciesReport](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartDeclarativePoliciesReport.html) in the *Amazon EC2 API Reference*.
+ `ec2:describe-declarative-policies-report`: Describes the metadata of an account status report, including the state of the report. For more information, see [DescribeDeclarativePoliciesReports](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeDeclarativePoliciesReports.html) in the *Amazon EC2 API Reference*.
+ `ec2:get-declarative-policies-report-summary`: Retrieves a summary of the account status report. For more information, see [GetDeclarativePoliciesReportSummary](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetDeclarativePoliciesReportSummary.html) in the *Amazon EC2 API Reference*.
+ `ec2:cancel-declarative-policies-report`: Cancels the generation of an account status report. For more information, see [CancelDeclarativePoliciesReport](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelDeclarativePoliciesReport.html) in the *Amazon EC2 API Reference*.

Before you generate a report, grant the EC2 policies principal access to the Amazon S3 bucket where the report will be stored. To do this, attach the following policy to the bucket. Replace `amzn-s3-demo-bucket` with your actual Amazon S3 bucket name, and `identity_ARN` with the IAM identity used to call the `StartDeclarativePoliciesReport` operation.

The following JSON policy grants access to deliver the report to your bucket:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DeclarativePoliciesReportDelivery",
            "Effect": "Allow",
            "Principal": {
                "AWS": "{{identity_ARN}}"
            },
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*",
            "Condition": {
                "StringEquals": {
                    "aws:CalledViaLast": "organizations.amazonaws.com"
                }
            }
        }
    ]
}
```

------

------