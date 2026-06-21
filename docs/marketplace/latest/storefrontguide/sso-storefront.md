# Setting up single sign-on for a storefront

You can enable single sign-on (SSO) so buyers sign in to a storefront with your identity
provider. AWS Marketplace Storefront supports Okta and Azure Entra ID.

###### To configure storefront SSO

1. Open the storefront, then choose the **SSO
   Configuration** tab.
2. Turn on **Enable SSO**.
3. For **Identity Provider**, choose Okta or Azure Entra
   ID.
4. Enter the **Client ID** and **Client Secret** from your identity provider application.
5. For Okta, enter the **Domain**. For Azure Entra ID,
   enter the **Tenant ID**.
6. Choose **Save**.
7. Choose **Test Connection** to verify the
   configuration.

## Related topics

- [Deployment](storefronts-creating-deploying.md#deployment "storefronts-creating-deploying.md#deployment")
- [Setting up single sign-on for your organization](setting-up-sso.md "setting-up-sso.md")
