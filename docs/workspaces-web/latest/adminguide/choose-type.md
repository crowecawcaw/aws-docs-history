

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Choosing the identity provider type for Amazon WorkSpaces Secure Browser
<a name="choose-type"></a>

WorkSpaces Secure Browser offers two authentication types: **Standard** and **AWS IAM Identity Center**. You choose the authentication type to use with your portal on the **Configure identity provider page**. 
+ For **Standard** (default option), federate your 3rd party SAML 2.0 identity provider (such as Okta or Ping) directly with your portal. For more information, see [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md). The standard type supports both SP-initiated and IdP-initiated authentication flows.
+ For **IAM Identity Center** (advanced option), federate the IAM Identity Center with your portal. To use this authentication type, your IAM Identity Center and WorkSpaces Secure Browser portal must both reside in the same AWS Region. For more information, see [Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser](configure-iam.md).

**Topics**
+ [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md)
+ [Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser](configure-iam.md)