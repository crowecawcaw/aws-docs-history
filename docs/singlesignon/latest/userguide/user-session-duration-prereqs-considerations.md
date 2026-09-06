

# Session duration considerations for using identity sources, the AWS CLI, and AWS SDKs
<a name="user-session-duration-prereqs-considerations"></a>

Following are considerations for configuring the session duration if you use Microsoft Active Directory (AD) or an external identity provider (IdP) as the identity source, or the AWS Command Line Interface, AWS Software Development Kits (SDKs), or other AWS development tools to access AWS services programmatically.

## Microsoft Active Directory, user interactive sessions, and extended sessions for Kiro
<a name="user-session-duration-microsoft-ad"></a>

If you use Microsoft Active Directory (AD) as the identity source and you configure the session duration for user interactive sessions or extended sessions for Kiro, keep the following considerations in mind. 

**Note**  
These considerations do not apply to user background sessions.

Whether you use AWS Managed Microsoft AD or AD Connector configured in AWS Directory Service, the maximum lifetime for user Kerberos tickets defined in Microsoft AD can affect how long user interactive sessions and extended sessions for Kiro are valid. For more information about this setting, see [Maximum lifetime for user ticket](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/maximum-lifetime-for-user-ticket) on the Microsoft website.
+ **AWS Managed Microsoft AD**: If you use AWS Managed Microsoft AD configured in AWS Directory Service, the maximum lifetime for user Kerberos tickets is fixed at 10 hours. Therefore, the user interactive session duration is set to the shorter of the IAM Identity Center setting and 10 hours. For example, if you set the user interactive session duration to 12 hours, your users must re-authenticate in the AWS access portal after 10 hours. The same 10-hour limit applies to extended sessions for Kiro.
+ **AD Connector**: If you use AD Connector configured in AWS Directory Service, the maximum lifetime for user Kerberos tickets is defined in Microsoft AD behind the AD Connector. The default value is 10 hours, and it has the same effect on user interactive sessions and extended sessions as for AWS Managed Microsoft AD. Although this limit might be configurable in Microsoft AD, we recommend that you work with your IT administrator to consider the risks, especially because this setting can affect the session duration for other Microsoft AD client applications.

## External identity providers, user interactive sessions, and extended sessions for Kiro
<a name="user-session-duration-external-idps"></a>

If you use an external identity provider (IdP) and you configure the session duration for user interactive sessions or extended sessions for Kiro, keep the following considerations in mind.

**Note**  
These considerations do not apply to user background sessions.

IAM Identity Center uses `SessionNotOnOrAfter` attribute from SAML assertions to help determine how long the session can be valid.
+ If `SessionNotOnOrAfter` is not passed in a SAML assertion, the duration of an AWS access portal (user interactive) session and an extended session is not impacted by the duration of your external IdP session. For example, if your IdP session duration is 24 hours and you set an 18-hour session duration in IAM Identity Center, your users must re-authenticate in the AWS access portal after 18 hours. Similarly, if you set a 90-day extended session for Kiro, your Kiro users need to re-authenticate after 90 days.
+ If `SessionNotOnOrAfter` is passed in a SAML assertion, the session duration value is set to the shorter of the AWS access portal (user interactive) session or extended session duration and your SAML IdP session duration. If you set a 72-hour session duration in IAM Identity Center and your IdP has a session duration of 18 hours, your users will have access to AWS resources for the 18 hours defined in your IdP. Similarly, if you set a 90-day extended session for Kiro, your Kiro users need to re-authenticate in Kiro after 18 hours.
+ If the session duration of your IdP is longer than the one set in IAM Identity Center, your users can start a new IAM Identity Center session without re-entering their credentials, based on their still-valid login session with your IdP.

## AWS CLI and SDK sessions
<a name="user-session-duration-cli-sdks"></a>

If you are using the AWS CLI, AWS SDKs, or other AWS development tools to access AWS services programmatically, the following prerequisites must be met to set session duration for the AWS access portal and the AWS managed applications.
+ You must [configure the AWS access portal session duration](user-interactive-sessions.md) in the IAM Identity Center console.
+ You must define a profile for single sign-on settings in your shared AWS config file. This profile is used to connect to the AWS access portal. We recommend that you use the SSO token provider configuration. With this configuration, your AWS SDK or tool can automatically retrieve refreshed authentication tokens. For more information, see [SSO token provider configuration](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html#sso-token-config) in the *AWS SDK and Tools Reference Guide*.
+ Users must run a version of the AWS CLI or an SDK that supports session management.

### Minimum versions of the AWS CLI that support session management
<a name="min-supported-cli-session-duration"></a>

Following are the minimum versions of the AWS CLI that support session management.
+ AWS CLI V2 2.9 or later
+ AWS CLI V1 1.27.10 or later

**Note**  
For account access use cases, if your users are running the AWS CLI, if you refresh your permission set just before the IAM Identity Center session is set to expire and the session duration is set to 20 hours while the permission set duration is set to 12 hours, the AWS CLI session runs for the maximum of 20 hours plus 12 hours for a total of 32 hours. For more information about the IAM Identity Center CLI, see [AWS CLI Command Reference.](https://docs.aws.amazon.com/cli/latest/reference/identitystore)

### Minimum versions of SDKs that support IAM Identity Center session management
<a name="min-supported-sdks-session-duration"></a>

Following are the minimum versions of the SDKs that support IAM Identity Center session management.



| SDK | Minimum version | 
| --- | --- | 
| Python | 1.26.10 | 
| PHP | 3.245.0 | 
| Ruby | aws-sdk-core 3.167.0 | 
| Java V2 | AWS SDK for Java v2 (2.18.13) | 
| Go V2 | Whole SDK: release-2022-11-11 and specific Go modules: credentials/v1.13.0, config/v1.18.0 | 
| JS V2 | 2.1253.0 | 
| JS V3 | v3.210.0 | 
| C\+\+ | 1.9.372 | 
| .NET | v3.7.400.0 | 