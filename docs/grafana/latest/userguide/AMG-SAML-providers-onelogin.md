

# Configure Amazon Managed Grafana to use OneLogin
<a name="AMG-SAML-providers-onelogin"></a>

Use the following steps to configure Amazon Managed Grafana to use OneLogin as an identity provider. These steps assume that you have already created your Amazon Managed Grafana workspace and you have made a note of the workspace's ID, URLs, and Region.

## Step 1: Steps to complete in OneLogin
<a name="AMG-SAML-providers-onelogin-step1"></a>

Complete the following steps in OneLogin.

**To set up OneLogin as an identity provider for Amazon Managed Grafana**

1. Sign in to the OneLogin portal as an administrator. 

1. Choose **Applications**, **Applications**, **Add app**.

1. Search for **Amazon Managed Service for Grafana**.

1. Assign a **Display name** of your choice and choose **Save**.

1. Navigate to **Configuration** and enter the Amazon Managed Grafana workspace ID in **Namespace**, and enter the Region of your Amazon Managed Grafana workspace.

1. In the **Configuration** tab, enter your Amazon Managed Grafana workspace URL.

1. You can leave the **adminRole** parameter as the default **No Default** and populate it using the **Rules** tab, if an admin requires a corresponding value in Amazon Managed Grafana. In this example, the **Assertion attribute role** would be set to **adminRole** in Amazon Managed Grafana, with a value of true. You can point this value to any attribute in your tenant. Click the **\+** to add and configure parameters to meet your organization's requirements.

1. Choose the **Rules** tab, choose **Add Rule**, and give your Rule a name. In the **Conditions** field (the if statement), we add **Email contains [email address]**. In the **Actions** field (the then statement), we select **Set AdminRole in Amazon Managed Service** and we select **Macro** in the **Set adminRole** to dropdown, with a value of **true**. Your organization can choose different rules to resolve different use cases.

1. Choose **Save**. Go to **More Actions** and choose **Reapply entitlement mappings**. You must reappy mappings any time that you create or update rules.

1. Make a note of the **Issuer URL**, which you use later in the configuration in the Amazon Managed Grafana console. Then choose **Save**.

1. Choose the **Access** tab to assign the OneLogin roles that are to access Amazon Managed Grafana and select an app security policy. 

## Step 2: Steps to complete in Amazon Managed Grafana
<a name="AMG-SAML-providers-onelogin-step2"></a>

Complete the following steps in the Amazon Managed Grafana console.

**To finish setting up OneLogin as an identity provider for Amazon Managed Grafana**

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/).

1. In the navigation pane, choose the menu icon.

1. Choose **All workspaces**.

1. Choose the name of the workspace.

1. In the **Authentication** tab, choose **Setup SAML configuration**.

1. Under **Import the metadata**, choose **Upload or copy/paste** and paste the OneLogin Issuer URL that you copied from the OneLogin console in the previous procedure.

1. Under **Assertion mapping**, do the following:
   + Make sure that **I want to opt-out of assigning admins to my workspace** is not selected.
**Note**  
If you choose **I want to opt-out of assigning admins to my workspace**, you won't be able to use the Amazon Managed Grafana workspace console to administer the workspace, including tasks such as managing data sources, users, and dashboard permissions. You can make administrative changes to the workspace only by using Grafana APIs.
   + Set **Assertion attribute role** to the attribute name that you chose. The default value for OneLogin is **adminRole**.
   + Set **Admin role values** to value corresponding to your admin users' roles.
   + (Optional) If you changed the default attributes in your OneLogin application, expand **Additional settings - optional** and then set the new attribute names.

     By default, the OneLogin **displayName** attribute is passed to the **name** attribute and the OneLogin **mail** attribute is passed to both the **email** and **login** attributes.

1. Choose **Save SAML Configuration**.