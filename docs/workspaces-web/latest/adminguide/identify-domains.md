# Identifying domains for the single sign-on extension in Amazon WorkSpaces Secure Browser

First, determine which domains you need for your SAML IdP and websites. You
can add up to 10 domains.

You are responsible for testing and identifying the appropriate domain for the cookies to be
synchronized. Changes might be required at the IdP or website authentication level to ensure
single sign-on works as expected.

To see which domains to use with most common IdP, refer to the following table:

| IdP and domains     | IdP                 | Domain |
| ------------------- | ------------------- | ------ |
| Okta                | okta.com            |
| Entra ID            | microsoftonline.com |
| AWS Identity Center | awsapps.com         |
| One Login           | onelogin.com        |
| Duo                 | duosecurity.com     |
