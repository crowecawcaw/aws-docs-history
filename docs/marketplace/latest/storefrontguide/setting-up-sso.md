# Setting up single sign-on for your organization

Single sign-on (SSO) lets your organization members sign in to AWS Marketplace
Storefront with your identity provider. AWS Marketplace Storefront supports Okta and
Azure Entra ID. Only organization Owners can configure SSO.

###### To configure organization SSO

1. Choose your profile avatar in the top-right corner, choose **Organization Settings**, then choose the **SSO Configuration** tab.
2. Turn on **Enable SSO**.
3. For **Identity Provider**, choose Okta or Azure
   Entra ID.
4. Enter the **Client ID** and **Client Secret** from your identity provider application.
5. For Okta, enter the **Domain** (for example,
   yourcompany.okta.com). For Azure Entra ID, enter the **Tenant
   ID**.
6. Choose **Save**.
7. Choose **Test Connection** to verify the
   configuration. The page shows the date of the last connection check.

## Related topics

- [Managing team members](organizations-storefront.md#managing-team-members "organizations-storefront.md#managing-team-members")
- [Security settings](organizations-storefront.md#security-settings "organizations-storefront.md#security-settings")
