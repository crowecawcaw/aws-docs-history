# Session duration considerations for using external IdPs, the AWS CLI, and AWS SDKs

Following are considerations for configuring the session duration if you are using an external identity provider (IdP), or the AWS Command Line Interface, AWS Software Development Kits (SDKs), or other AWS development tools to access AWS services programmatically.


## External identity providers, user interactive sessions, and extended sessions for Amazon Q Developer


If you use an external identity provider (IdP) and you are configuring the session duration for user interactive sessions or extended sessions for Amazon Q Developer, keep the following considerations in mind.


###### Note

These considerations do not apply to user background sessions.


IAM Identity Center uses `SessionNotOnOrAfter` attribute from SAML assertions to help determine how long the session can be valid.



* If `SessionNotOnOrAfter` is not passed in a SAML assertion, the duration of an AWS access portal session is not impacted by the duration of your external IdP session. For example, if your IdP session duration is 24 hours and you set an 18-hour session duration in IAM Identity Center, your users must re-authenticate in the AWS access portal after 18 hours.
* If `SessionNotOnOrAfter` is passed in a SAML assertion, the session duration value is set to the shorter of the AWS access portal session duration and your SAML IdP session duration. If you set a 72-hour session duration in IAM Identity Center and your IdP has a session duration of 18 hours, your users will have access to AWS resources for the 18 hours defined in your IdP.
* If the session duration of your IdP is longer than the one set in IAM Identity Center, your users can start a new IAM Identity Center session without re-entering their credentials, based on their still-valid login session with your IdP.

## AWS CLI and SDK sessions


If you are using the AWS CLI, AWS SDKs, or other AWS development tools to access AWS services programmatically, the following prerequisites must be met to set session duration for the AWS access portal and the AWS managed applications.



* You must [configure the AWS access portal session duration](user-interactive-sessions.md "user-interactive-sessions.md") in the IAM Identity Center console.
* You must define a profile for single sign-on settings in your shared AWS config file. This profile is used to connect to the AWS access portal. We recommend that you use the SSO token provider configuration. With this configuration, your AWS SDK or tool can automatically retrieve refreshed authentication tokens. For more information, see [SSO token provider configuration](https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html#sso-token-config "https://docs.aws.amazon.com/sdkref/latest/guide/feature-sso-credentials.html#sso-token-config") in the *AWS SDK and Tools Reference Guide*.
* Users must run a version of the AWS CLI or an SDK that supports session management.

### Minimum versions of the AWS CLI that support session management


Following are the minimum versions of the AWS CLI that support session management.



* AWS CLI V2 2.9 or later
* AWS CLI V1 1.27.10 or later

###### Note

For account access use cases, if your users are running the AWS CLI, if you refresh your permission set just before the IAM Identity Center session is set to expire and the session duration is set to 20 hours while the permission set duration is set to 12 hours, the AWS CLI session runs for the maximum of 20 hours plus 12 hours for a total of 32 hours. For more information about the IAM Identity Center CLI, see [AWS CLI Command Reference.](https://docs.aws.amazon.com/cli/latest/reference/identitystore "https://docs.aws.amazon.com/cli/latest/reference/identitystore")


### Minimum versions of SDKs that support IAM Identity Center session management


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
| C++ | 1.9.372 |
| .NET | v3.7.400.0 |
