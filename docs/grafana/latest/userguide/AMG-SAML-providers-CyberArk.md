# Configure Amazon Managed Grafana to use

CyberArk

Use the following steps to configure Amazon Managed Grafana to use CyberArk as an identity
provider. These steps assume that you have already created your Amazon Managed Grafana workspace
and you have made a note of the workspace's ID, URLs, and Region.

## Step 1: Steps to complete in

CyberArk

Complete the following steps in CyberArk.

###### To set up CyberArk as an identity provider for Amazon Managed Grafana

1. Sign in to the CyberArk Identity Admin Portal.
2. Choose **Apps**, **Web
   Apps**.
3. Choose **Add Web App**.
4. Search for **Amazon Managed Grafana for SAML2.0**,
   and choose **Add**.
5. In the CyberArk application configuration, go to the
   **Trust** section.
6. Under **Identity Provider Configuration**, choose
   **Metadata**.
7. Choose **Copy URL** and save the URL to use later in
   these steps.
8. Under **Service Provider Configuration**, choose
   **Manual Configuration**.
9. Specify your SAML settings:
   - For **SP Entity ID**, paste in your
     **Service provider identifier** URL from
     the Amazon Managed Grafana workspace.
   - For **Assertion Consumer Service (ACS) URL**,
     paste in your **Service provider reply** from
     the Amazon Managed Grafana workspace.
   - Set **Sign Response Assertion** to
     **Assertion**.
   - Make sure that **NameID Format** is
     **emailAddress**.

10. Choose **Save**.
11. In the **SAML Response** section, make sure that the
    Amazon Managed Grafana attribute is in **Application Name** and that
    the CyberArk attribute is in **Attribute Value**. Then
    make sure that the following attributes are mapped. They are case
    sensitive.
    - **displayName** is set with
      **LoginUser.DisplayName**.
    - **mail** is set with
      **LoginUser.Email**.
    - Add any other attributes that you would to pass. For more
      information about the attributes that you can pass to Amazon Managed Grafana
      in the assertion mapping, see [Assertion mapping](authentication-in-AMG-SAML.md#AMG-SAML-Assertion-Mapping "authentication-in-AMG-SAML.md#AMG-SAML-Assertion-Mapping").

12. Choose **Save**.
13. In the **Permissions** section, choose which users
    and groups to assign this application to, and then choose
    **Save**.

## Step 2: Steps to complete in

Amazon Managed Grafana

Complete the following steps in the Amazon Managed Grafana console.

###### To finishg setting up CyberArk as an identity provider for

Amazon Managed Grafana

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the name of the workspace.
5. In the **Authentication** tab, choose **Setup
   SAML configuration**.
6. Under **Import the metadata**, choose
   **Upload or copy/paste** and paste the CyberArk URL
   that you copied in the previous procedure.
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
   - (Optional) If you changed the default attributes in your
     CyberArk application, expand **Additional settings -
     optional** and then set the new attribute
     names.

   By default, the CyberA **displayName**
   attribute is passed to the **name** attribute
   and the CyberArk **mail** attribute is passed
   to both the **email** and
   **login** attributes.

8. Choose **Save SAML Configuration**.
