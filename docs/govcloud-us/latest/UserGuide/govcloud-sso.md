

# AWS IAM Identity Center in AWS GovCloud (US)
<a name="govcloud-sso"></a>

 IAM Identity Center is the AWS solution for connecting your workforce users to all of their AWS managed applications and AWS accounts. Users who have access to one or more AWS accounts can sign in to the AWS access portal and access AWS services by using the AWS Management Console or retrieve temporary credentials to access AWS services programmatically. You can connect your existing identity provider or create and manage your users directly in IAM Identity Center. For existing identity providers, automatic provisioning (synchronization) of user and group information from your identity provider into IAM Identity Center is supported.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How IAM Identity Center differs
<a name="govcloud-diffs-20"></a>

The following differences apply to IAM Identity Center:
+  IAM Identity Center integrates with AWS Organizations to manage access across your AWS accounts, and therefore, IAM Identity Center is subject to any [AWS Organizations GovCloud differences](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-organizations.html).
+  IAM Identity Center supports dual-stack endpoints in AWS GovCloud (US) Regions. You can use either IPv4, IPv6, or dual-stack to access IAM Identity Center services and the AWS access portal.
+ To access the IAM Identity Center administrative console, the Software Development Kit (SDK), or the AWS Command Line Interface (CLI) use the Federal Information Processing Standards (FIPS) endpoints. For a list of all GovCloud AWS FIPS endpoints, see * AWS GovCloud (US) * in [FIPS Endpoints by Service](https://aws.amazon.com/compliance/fips/#FIPS_Endpoints_by_Service).
+ The AWS access portal URL has an AWS GovCloud (US) URL pattern of `https://start.us-gov-home.awsapps.com/directory/IdentityStoreId` or `https://start.us-gov-home.awsapps.com/directory/CustomAlias` 

  You can find this URL on the **Settings** page in the IAM Identity Center console.
+ The new AWS access portal URL format for AWS GovCloud (US) follows the pattern `https://{idcInstanceId}.portal.{region}.app.aws`, similar to the commercial region format.

  This new URL format provides a consistent experience across all AWS regions.
+ The Amazon Resource Number (ARN) for your IAM Identity Center instance has an AWS GovCloud (US) pattern of `arn:aws-us-gov:sso:::instance/<SSOInstanceId>` 

  You can find this ARN on the **Settings** page in the IAM Identity Center console.
+ The ARNs for IAM Identity Center permission sets has an AWS GovCloud (US) pattern of `arn:aws-us-gov:sso:::permissionSet/<SSOInstanceID>/<PermissionSetID>` 

  You can find these ARNs on the **Permission sets** tab under the ** AWS accounts ** page in the IAM Identity Center console.
+ The email address `no-reply@us-gov-home.awsapps.com` is used for sending email-verification, password reset, and user invitation emails to GovCloud.

  The email address `no-reply@<identitystore_id>.us-gov-home.awsapps.com` is used for sending forgotten password emails.
+ Multi-Region support is presently not available.
+ If you filter access to specific AWS domains by using a web content filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG), you must add the following domains to your web-content filtering solution allowlists. Doing so enables you to access your AWS access portal.
  +  `start.us-gov-home.awsapps.com` 
  +  `start.[Region].us-gov-home.awsapps.com` 
  +  `[IAM-Identity-Center-instance-id].[Region].portal.amazonaws.com` 
  +  `oidc.[Region].amazonaws.com` 
  +  `*.sso.amazonaws.com` 
  +  `*.sso.[Region].amazonaws.com` 
  +  `*.sso-portal.[Region].amazonaws.com` 
  +  `aws-access-portal-website-prod-pdt-assets.s3.us-gov-west-1.amazonaws.com` 
  +  `aws-access-portal-website-prod-osu-assets.s3.us-gov-east-1.amazonaws.com` 
  +  `s3.us-gov-west-1.amazonaws.com/awsconsole-peregrine-portal-prod-pdt-assets` 
  +  `s3.us-gov-east-1.amazonaws.com/awsconsole-peregrine-portal-prod-osu-assets` 
  +  `[Region].signin-fips.amazonaws-us-gov.com` 
  +  `*.cloudfront.net` 
  +  `opfcaptcha-prod.s3.amazonaws.com` 
+ For dual-stack (IPv4 and IPv6) endpoint access, you must also add the following domains to your web-content filtering solution allowlists:
  +  `[idcInstanceId].portal.[Region].app.aws` 
  +  `portal.sso.[Region].api.aws` 
  +  `oidc.[Region].api.aws` 
  +  `oidc-fips.[Region].api.aws` 
  +  `sso.[Region].api.aws` 
  +  `scim.[Region].api.aws` 
  +  `identitystore.[Region].api.aws` 
  +  `identity-sync.[Region].api.aws` 
  +  `dual-stack.auth-control.[Region].prod.apps-auth.aws.a2z.com` 
  +  `pvs-controlplane.[Region].api.aws` 
  +  `[Region].sso.signin.amazonaws-us-gov.com` 
  +  `[Region].sso.signin-fips.amazonaws-us-gov.com` 
  +  `cdn.us-east-1.threat-mitigation.aws.amazon.com` 
  +  `us-east-1.threat-mitigation.aws.amazon.com` 
  +  `amcs-captcha-prod-us-east-1.s3.dualstack.us-east-1.amazonaws.com` 
+ If you change an AWS account name or email address, and you want your AWS access portal to show the new value, you’ll need to create a case with Support. In the support case, specify the account ID and the AWS Region of your IAM Identity Center instance. Also include a list of account IDs that require a refresh in your AWS access portal.
+ The user background sessions feature appears in the console for AWS GovCloud (US), but this feature cannot be used because user background sessions are only supported for Amazon SageMaker Studio. Although Amazon SageMaker AI is supported in AWS GovCloud (US), Amazon SageMaker Studio, which is its latest web experience for running machine learning (ML) workflows, is not available.

## Documentation
<a name="govcloud-docs-58"></a>
+  [AWS IAM Identity Center documentation](https://docs.aws.amazon.com/singlesignon/) 

## Export-controlled content
<a name="govcloud-itar-content-98"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Your IAM Identity Center Identity Store ID may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.