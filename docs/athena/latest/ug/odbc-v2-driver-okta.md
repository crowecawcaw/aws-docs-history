

# Okta
<a name="odbc-v2-driver-okta"></a>

Okta is a SAML-based authentication plugin that works with the Okta identity provider. For information about configuring federation for Okta and Amazon Athena, see [Configure SSO for ODBC using the Okta plugin and Okta Identity Provider](odbc-okta-plugin.md).

## Authentication Type
<a name="odbc-v2-driver-okta-authentication-type"></a>



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| AuthenticationType | Required | IAM Credentials | AuthenticationType=Okta; | 

## User ID
<a name="odbc-v2-driver-okta-user-id"></a>

Your Okta user name.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| UID | Required | none | UID=jane.doe@org.com; | 

## Password
<a name="odbc-v2-driver-okta-password"></a>

Your Okta user password.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| PWD | Required | none | PWD=oktauserpasswordexample; | 

## Preferred role
<a name="odbc-v2-driver-okta-preferred-role"></a>

The Amazon Resource Name (ARN) of the role to assume. For more information about ARN roles, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| preferred\_role | Optional | none | preferred\_role=arn:aws:IAM::123456789012:id/user1; | 

## Session duration
<a name="odbc-v2-driver-okta-session-duration"></a>

The duration, in seconds, of the role session. For more information, see [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) in the *AWS Security Token Service API Reference*.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| duration | Optional | 900 | duration=900; | 

## IdP host
<a name="odbc-v2-driver-okta-idp-host"></a>

The URL for your Okta organization. You can extract the `idp_host` parameter from the **Embed Link** URL in your Okta application. For steps, see [Retrieve ODBC configuration information from Okta](odbc-okta-plugin.md#odbc-okta-plugin-retrieve-odbc-configuration-information-from-okta). The first segment after `https://`, up to and including `okta.com` is your IdP host (for example, `http://trial-1234567.okta.com`).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| idp\_host | Required | None | idp\_host=dev-99999999.okta.com; | 

## IdP port
<a name="odbc-v2-driver-okta-idp-port"></a>

The port number to use to connect to your IdP host.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| idp\_port | Required | None | idp\_port=443; | 

## Okta app ID
<a name="odbc-v2-driver-okta-app-id"></a>

The two-part identifier for your application. You can extract the `app_id` parameter from the **Embed Link** URL in your Okta application. For steps, see [Retrieve ODBC configuration information from Okta](odbc-okta-plugin.md#odbc-okta-plugin-retrieve-odbc-configuration-information-from-okta). The application ID is the last two segments of the URL, including the forward slash in the middle. The segments are two 20-character strings with a mix of numbers and upper and lowercase letters (for example, `Abc1de2fghi3J45kL678/abc1defghij2klmNo3p4`).



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| app\_id | Required | None | app\_id=0oa25kx8ze9A3example/alnexamplea0piaWa0g7; | 

## Okta app name
<a name="odbc-v2-driver-okta-app-name"></a>

The name of the Okta application.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| app\_name | Required | None | app\_name=amazon\_aws\_redshift; | 

## Okta wait time
<a name="odbc-v2-driver-okta-wait-time"></a>

Specifies the duration in seconds to wait for the multifactor authentication (MFA) code.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| okta\_mfa\_wait\_time | Optional | 10 | okta\_mfa\_wait\_time=20; | 

## Okta MFA type
<a name="odbc-v2-driver-okta-mfa-type"></a>

The MFA factor type. Supported types are Google Authenticator, SMS (Okta), Okta Verify with Push, and Okta Verify with TOTP. Individual organization security policies determine whether or not MFA is required for user login.



| **Connection string name** | **Parameter type** | **Default value** | **Possible values** | **Connection string example** | 
| --- | --- | --- | --- | --- | 
| okta\_mfa\_type | Optional | None | googleauthenticator, smsauthentication, oktaverifywithpush, oktaverifywithtotp | okta\_mfa\_type=oktaverifywithpush; | 

## Okta phone number
<a name="odbc-v2-driver-okta-phone-number"></a>

The phone number to use with AWS SMS authentication. This parameter is required only for multifactor enrollment. If your mobile number is already enrolled, or if AWS SMS authentication is not used by the security policy, you can ignore this field.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| okta\_mfa\_phone\_number | Required for MFA enrollment, optional otherwise | None | okta\_mfa\_phone\_number=19991234567; | 

## Enable Okta file cache
<a name="odbc-v2-driver-okta-file-cache"></a>

Enables a temporary credentials cache. This connection parameter enables temporary credentials to be cached and reused between the multiple processes opened by BI applications. Use this option to avoid the Okta API throttling limit.



| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** | 
| --- | --- | --- | --- | 
| okta\_cache | Optional | 0 | okta\_cache=1; | 