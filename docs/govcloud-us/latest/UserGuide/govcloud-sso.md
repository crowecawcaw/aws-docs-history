# AWS IAM Identity Center in AWS GovCloud (US)

IAM Identity Center is the AWS solution for connecting your workforce users to all of their AWS managed applications and AWS accounts. Users who have access to one or more AWS accounts can sign in to the AWS access portal and access AWS services by using the AWS Management Console or retrieve temporary credentials to access AWS services programmatically. You can connect your existing identity provider or create and manage your users directly in IAM Identity Center. For existing identity providers, automatic provisioning (synchronization) of user and group information from your identity provider into IAM Identity Center is supported.

## How IAM Identity Center differs for AWS GovCloud (US)

The following list details the differences for using this service in the AWS GovCloud (US) Regions compared to other AWS Regions:

- IAM Identity Center integrates with AWS Organizations to manage access across your AWS accounts, and therefore, IAM Identity Center is subject to any [AWS Organizations GovCloud differences](govcloud-organizations.md "govcloud-organizations.md").
- To access the IAM Identity Center administrative console, the Software Development Kit (SDK), or the AWS Command Line Interface (CLI) use the Federal Information Processing Standards (FIPS) endpoints. For a list of all GovCloud AWS FIPS endpoints, see _AWS GovCloud (US)_ in [FIPS Endpoints by Service](https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service").
- The AWS access portal URL has an AWS GovCloud (US) URL pattern of `https://start.us-gov-home.awsapps.com/directory/IdentityStoreId` or `https://start.us-gov-home.awsapps.com/directory/CustomAlias`

You can find this URL on the **Settings** page in the IAM Identity Center console.

- The Amazon Resource Number (ARN) for your IAM Identity Center instance has an AWS GovCloud (US) pattern of `arn:aws-us-gov:sso:::instance/<SSOInstanceId>`

You can find this ARN on the **Settings** page in the IAM Identity Center console.

- The ARNs for IAM Identity Center permission sets has an AWS GovCloud (US) pattern of `arn:aws-us-gov:sso:::permissionSet/<SSOInstanceID>/<PermissionSetID>`

You can find these ARNs on the **Permission sets** tab under the **AWS accounts** page in the IAM Identity Center console.

- The email address `no-reply@us-gov-home.awsapps.com` is used for sending email-verification, password reset, and user invitation emails to GovCloud.

The email address `no-reply@<identitystore_id>.us-gov-home.awsapps.com` is used for sending forgotten password emails.

- Multi-Region support is presently not available.
- If you filter access to specific AWS domains by using a web content filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG), you must add the following domains to your web-content filtering solution allowlists. Doing so enables you to access your AWS access portal.
  - `start.us-gov-home.awsapps.com`
  - `start.[Region].us-gov-home.awsapps.com`
  - `[IAM-Identity-Center-instance-id].[Region].portal.amazonaws.com`
  - `oidc.[Region].amazonaws.com`
  - `*.sso.amazonaws.com`
  - `*.sso.[Region].amazonaws.com`
  - `*.sso-portal.[Region].amazonaws.com`
  - `aws-access-portal-website-prod-pdt-assets.s3.us-gov-west-1.amazonaws.com`
  - `aws-access-portal-website-prod-osu-assets.s3.us-gov-east-1.amazonaws.com`
  - `s3.us-gov-west-1.amazonaws.com/awsconsole-peregrine-portal-prod-pdt-assets`
  - `s3.us-gov-east-1.amazonaws.com/awsconsole-peregrine-portal-prod-osu-assets`
  - `[Region].signin-fips.amazonaws-us-gov.com`
  - `*.cloudfront.net`
  - `opfcaptcha-prod.s3.amazonaws.com`

- If you change an AWS account name or email address, and you want your AWS access portal to show the new value, you’ll need to create a case with Support. In the support case, specify the account ID and the AWS Region of your IAM Identity Center instance. Also include a list of account IDs that require a refresh in your AWS access portal.
- The user background sessions feature appears in the console for AWS GovCloud (US), but this feature cannot be used because user background sessions are only supported for Amazon SageMaker Studio. Although Amazon SageMaker AI is supported in AWS GovCloud (US), Amazon SageMaker Studio, which is its latest web experience for running machine learning (ML) workflows, is not supported in AWS GovCloud (US).

## Documentation for AWS IAM Identity Center

[AWS IAM Identity Center documentation](../../../singlesignon.md "../../../singlesignon.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Your IAM Identity Center Identity Store ID may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
