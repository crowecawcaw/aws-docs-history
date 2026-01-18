# AWS Directory Service in AWS GovCloud (US)

AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, enables your directory-aware workloads and AWS resources to use managed Active Directory in the AWS Cloud. AWS Managed Microsoft AD is built on actual Microsoft Active Directory and does not require you to synchronize or replicate data from your existing Active Directory to the cloud. You can use standard Active Directory administration tools and take advantage of built-in Active Directory features, such as Group Policy and single sign-on (SSO). With AWS Managed Microsoft AD, you can easily join Amazon EC2 and Amazon RDS for SQL Server instances to your domain, and use AWS Enterprise IT applications such as Amazon WorkSpaces with Active Directory users and groups.

## How AWS Directory Service differs for AWS GovCloud (US)

The following list details the differences for using this service in AWS GovCloud (US) Regions compared to other AWS Regions:

- Only AWS Managed Microsoft AD and AD Connector directory types are supported by AWS Directory Service.
- The following directory types are not supported:
  - Simple AD
  - Amazon Cloud Directory

- The following AWS apps and services are not currently supported by AWS Directory Service:
  - Amazon WorkDocs
  - Amazon WorkMail
  - Amazon Chime
  - AWS Management Console
  - Amazon Connect only in available in AWS GovCloud (US-West).
  - AWS IAM Identity Center

- The following AWS Managed Microsoft AD features are not currently supported in AWS GovCloud (US):
  - Directory sharing with other AWS accounts
  - AWS Managed Microsoft AD (Hybrid Edition)

- Only signature version 4 signing is supported.
- You can use the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") to interact with AWS Directory Service and other AWS services through the command line. For more information, see [AWS CLI](../../../cli/index.md "../../../cli/index.md") documentation.

###### Note

If you are using the Amazon Linux AMI, the AWS CLI is already installed and configured.

- To connect to AWS Directory Service by using the command line or APIs, use the following [endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md"):
  - https://ds-fips.us-gov-west-1.amazonaws.com
  - https://ds.us-gov-west-1.amazonaws.com
  - https://ds-fips.us-gov-east-1.amazonaws.com
  - https://ds.us-gov-east-1.amazonaws.com

- Automatic DNS forwarding is not enabled by default and must be configured.
- The Directory Service Data API is not available.

## Documentation for AWS Directory Service

[AWS Directory Service documentation](../../../directory-service/index.md "../../../directory-service/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS Directory Service metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your AWS Directory Service directory except passwords.

Do not enter export-controlled data in the following console fields:

    + Directory aliases
    + Directory description
    + Directory DNS name
    + Netbios name
    + Manual snapshot name
    + Resource tags
    + Description of schema extensions
