# AWS Management Console for the AWS GovCloud (US) Region

The AWS Management Console is a graphical interface for accessing a wide range of AWS Cloud services and managing compute, storage, and other cloud resources. The console includes the Tag Editor tool for managing metadata that you add to your resources. You can then use those tags to create resource groups to manage your AWS resources collectively.

## How AWS Management Console differs for AWS GovCloud (US)

- You access the [AWS GovCloud (US) console](https://console.amazonaws-us-gov.com "https://console.amazonaws-us-gov.com") by using a different URL than the standard AWS Management Console.
- You can only access the AWS GovCloud (US) console by using an IAM user name and password, not with the
  GovCloud account root user email address. You cannot enable an MFA device for your AWS GovCloud (US) account root user email, but can enable for IAM users.
  For information about the AWS GovCloud (US) differences in IAM, see [AWS Identity and Access Management](https://aws.amazon.com/iam/details/mfa/ "https://aws.amazon.com/iam/details/mfa/").
- The console includes only the services that are available in AWS GovCloud (US) Regions. To see a list of the supported services,
  see [Services in the AWS GovCloud (US)](using-services.md "using-services.md").
- You are automatically signed out from the console after 4 hours.
- Due to the separate authentication stack for AWS GovCloud (US), the hardware MFA devices used with
  standard AWS Regions are not compatible with AWS GovCloud (US) accounts. AWS GovCloud (US) supports
  only MFA devices listed in the **Compatibility with
  AWS GovCloud (US)** table row on the [Multi-Factor Authentication](https://aws.amazon.com/iam/details/mfa/ "https://aws.amazon.com/iam/details/mfa/") page.
- The console does not permit navigation to any Regions other than AWS GovCloud (US) Regions.
- You can sign in to the AWS GovCloud (US) console and the standard AWS Management Console concurrently.
- You cannot automatically create a support ticket from the AWS GovCloud (US) console.
- Resource Groups, Tag Editor, and AWS Console mobile app are not available.
- On the Console Navigation the following features are not available: Personal Health Dashboard
  (PHD) alerts, Language Selector, Feedback.
- Unified Search only supports service and feature searches.
- myApplications is unavailable.
- Multi-session support is unavailable.

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Your user name is not permitted to contain export-controlled data.
- All console data fields inherit the export restrictions for the specific service that
  is being accessed. See each service for details.
