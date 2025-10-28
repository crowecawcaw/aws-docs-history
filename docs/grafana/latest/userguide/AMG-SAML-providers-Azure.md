# Configure Amazon Managed Grafana to use Azure

AD

Use the following steps to configure Amazon Managed Grafana to use Azure Active Directory as an
identity provider. These steps assume that you have already created your Amazon Managed Grafana
workspace and you have made a note of the workspace _ID_,
_URLs_, and _AWS Region_.

## Step 1: Steps to complete in

Azure Active Directory

Complete the following steps in Azure Active Directory.

###### To set up Azure Active Directory as an identity provider for

Amazon Managed Grafana

1. Sign in to the Azure console as an admin.
2. Choose **Azure Active Directory**.
3. Choose **Enterprise Applications**.
4. Search for **Amazon Managed Grafana SAML2.0**, and
   select it.
5. Select the application and choose **Setup**.
6. In the Azure Active Directory application configuration, choose
   **Users and groups**.
7. Assign the application to the users and groups that you want.
8. Choose **Single sign-on**.
9. Choose **Next** to get to the SAML configuration
   page.
10. Specify your SAML settings:
    - For **Identifier (Entity ID)**, paste in your
      **Service provider identifier** URL from
      the Amazon Managed Grafana workspace.
    - For **Reply URL (Assertion Consumer Service
      URL)**, paste in your **Service provider
      reply** from the Amazon Managed Grafana workspace.
    - Make sure that **Sign Assertion** is selected
      and that **Encrypt Assertion** is not
      selected.

11. In the **User Attributes & Claims** section, make
    sure that these attributes are mapped. They are case sensitive.
    - **mail** is set with
      **user.userprincipalname**.
    - **displayName** is set with
      **user.displayname**.
    - **Unique User Identifier** is set with
      **user.userprincipalname**.
    - Add any other attributes that you would to pass. For more
      information about the attributes that you can pass to Amazon Managed Grafana
      in the assertion mapping, see [Assertion mapping](authentication-in-AMG-SAML.md#AMG-SAML-Assertion-Mapping "authentication-in-AMG-SAML.md#AMG-SAML-Assertion-Mapping").

12. Copy the **SAML Metadata URL** for use in the
    Amazon Managed Grafana workspace configuration.

## Step 2: Steps to complete in

Amazon Managed Grafana

Complete the following steps in the Amazon Managed Grafana console.

###### To finish setting up Azure Active Directory as an identity provider for

Amazon Managed Grafana

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the name of the workspace.
5. In the **Authentication** tab, choose **Setup
   SAML configuration**.
6. Under **Import the metadata**, choose
   **Upload or copy/paste** and paste the Azure Active
   Directory URL that you copied from **SAML Metadata
   URL** in the previous section.
7. Under **Assertion mapping**, do the following:
   - Make sure that **I want to opt-out of assigning admins
     to my workspace** is not selected.

   ###### Note

   If you choose **I want to opt-out of assigning
   admins to my workspace**, you won't be able to
   use the Amazon Managed Grafana workspace console to administer the
   workspace, including tasks such as managing data sources,
   users, and dashboard permissions. You can make
   administrative changes to the workspace only by using
   Grafana APIs.
   - Set **Assertion attribute role** to the
     attribute name that you chose.
   - Set **Admin role values** to value
     corresponding to your admin users' roles.
   - (Optional) If you changed the default attributes in your Azure
     Active Directory application, expand **Additional
     settings - optional** and then set the new
     attribute names.

   By default, the Azure **displayName**
   attribute is passed as the **Name** attribute
   and the Ping Identity **mail** attribute is
   passed to both the **email** and
   **login** attributes.

8. Choose **Save SAML Configuration**.
