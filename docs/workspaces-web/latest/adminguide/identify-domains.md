

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Identifying domains for the single sign-on extension in Amazon WorkSpaces Secure Browser
<a name="identify-domains"></a>

First, determine which domains you need for your SAML IdP and websites. You can add up to 10 domains.

You are responsible for testing and identifying the appropriate domain for the cookies to be synchronized. Changes might be required at the IdP or website authentication level to ensure single sign-on works as expected. 

To see which domains to use with most common IdP, refer to the following table:


**IdP and domains**  

| IdP | Domain | 
| --- | --- | 
| Okta | okta.com | 
| Entra ID | microsoftonline.com | 
| AWS Identity Center | awsapps.com | 
| One Login | onelogin.com | 
| Duo | duosecurity.com | 