# Testing your web portal in Amazon WorkSpaces Secure Browser

After you create a web portal, you can sign into the WorkSpaces Secure Browser endpoint to browse your connected
websites as an end user would.

If you already completed these steps in [Configuring your identity provider for Amazon WorkSpaces Secure Browser](identity-settings.md "identity-settings.md"), you can skip
this section and go to [Distributing your web portal in Amazon WorkSpaces Secure Browser](getting-started-step3.md "getting-started-step3.md").

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/ "https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/").
2. Choose **WorkSpaces Secure Browser**, **Web portals**, choose your web
   portal, and then choose **View details**
3. Under **Web portal endpoint**, go to the specified URL for your portal.
   The web portal endpoint is the access point your users will launch your web portal from after
   signing in with the identity provider configured for the portal. It's publicly available on the
   internet and can be embedded into your network.
4. On the WorkSpaces Secure Browser sign-in page, choose **Sign in**, **SAML**,
   and enter your SAML credentials.
5. When you see the **Your session is being prepared** page, your WorkSpaces Secure Browser
   session is launching. Do not close or exit this page.
6. The web browser launches, displaying your startup URL and any other additional behavior
   configured through your browser policy settings.
7. You can now browse to connected websites by choosing links or enter URLs into the address
   bar.
