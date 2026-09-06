

# Configure Amazon Managed Grafana to use Okta
<a name="AMG-SAML-providers-okta"></a>

Use the following steps to configure Amazon Managed Grafana to use Okta as an identity provider. These steps assume that you have already created your Amazon Managed Grafana workspace and you have made a note of the workspace's ID, URLs, and Region.

## Step 1: Steps to complete in Okta
<a name="AMG-SAML-providers-okta-step1"></a>

Complete the following steps in Okta.

**To set up Okta as an identity provider for Amazon Managed Grafana**

1. Sign in to the Okta console as an admin. 

1. In the left panel, choose **Applications**, **Applications**.

1. Choose **Browse App Catalog** and search for **Amazon Managed Grafana**.

1. Choose **Amazon Managed Grafana** and choose **Add**, **Done**.

1. Choose the application to start setting it up.

1. In the **Sign On** tab, choose **Edit**.

1. Under **Advanced Sign-on Settings**, enter your Amazon Managed Grafana workspace id and your Region in the **Name Space** and **Region** fields respectively. Your Amazon Managed Grafana workspace id and Region can be found in your Amazon Managed Grafana workspace url which is of the format **{{workspace-id}}.grafana-workspace.{{Region}}.amazonaws.com**.

1. Choose **Save**.

1. Under **SAML 2.0**, copy the URL for **Identity Provider metadata**. You use this later in this procedure in the Amazon Managed Grafana console.

1. In the **Assignments** tab, choose the **People** and **Groups** that you want to be able to use Amazon Managed Grafana.

## Step 2: Steps to complete in Amazon Managed Grafana
<a name="AMG-SAML-providers-okta-step2"></a>

Complete the following steps in the Amazon Managed Grafana console.

**To finish setting up Okta as an identity provider for Amazon Managed Grafana**

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/).

1. In the navigation pane, choose the menu icon.

1. Choose **All workspaces**.

1. Choose the name of the workspace.

1. In the **Authentication** tab, choose **Complete Setup**.

1. Under **Import the meta data**, choose **Upload or copy/paste** and paste the Okta URL that you copied in the previous procedure.

1. Under **Assertion mapping**, do the following:
   + Make sure that **I want to opt-out of assigning admins to my workspace** is not selected.
**Note**  
If you choose **I want to opt-out of assigning admins to my workspace**, you won't be able to use the Amazon Managed Grafana workspace console to administer the workspace, including tasks such as managing data sources, users, and dashboard permissions. You can make administrative changes to the workspace only by using Grafana APIs.
   + Set **Assertion attribute role** to the attribute name that you chose.
   + Set **Admin role values** to value corresponding to your admin users' roles.
   + (Optional) If you changed the default attributes in your Okta application, expand **Additional settings - optional** and then set the new attribute names.

     By default, the Okta **displayName** attribute is passed to the **name** attribute and the Okta **mail** attribute is passed to both the **email** and **login** attributes.

1. Choose **Save SAML Configuration**.