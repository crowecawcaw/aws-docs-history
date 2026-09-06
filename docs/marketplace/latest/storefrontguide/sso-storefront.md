

# Setting up single sign-on for a storefront
<a name="sso-storefront"></a>

You can enable single sign-on (SSO) so buyers sign in to a storefront with your identity provider. AWS Marketplace Storefront supports Okta and Azure Entra ID.

**To configure storefront SSO**

1. Open the storefront, then choose the **SSO Configuration** tab.

1. Turn on **Enable SSO**.

1. For **Identity Provider**, choose Okta or Azure Entra ID.

1. Enter the **Client ID** and **Client Secret** from your identity provider application.

1. For Okta, enter the **Domain**. For Azure Entra ID, enter the **Tenant ID**.

1. Choose **Save**.

1. Choose **Test Connection** to verify the configuration.

## Related topics
<a name="sso-storefront-related"></a>
+ [Deployment](storefronts-creating-deploying.md#deployment)
+ [Setting up single sign-on for your organization](setting-up-sso.md)