# Configure Amazon Managed Grafana to use Ping

Identity

Use the following steps to configure Amazon Managed Grafana to use Ping Identity as an identity
provider. These steps assume that you have already created your Amazon Managed Grafana workspace
and you have made a note of the workspace's ID, URLs, and Region.

## Step 1: Steps to complete in

Ping Identity

Complete the following steps in Ping Identity.

###### To set up Ping Identity as an identity provider for Amazon Managed Grafana

1. Sign in to the Ping Identity console as an admin.
2. Choose **Applications**.
3. Choose **Add Application**, **Search
   Application Catalog**.
4. Search for the **Amazon Managed Grafana for SAML**
   application, then choose it and choose
   **Setup**.
5. In the Ping Identity application, choose **Next** to
   get to the SAML configuration page. Then make the following SAML
   settings:
   - For **Assertion Consumer Service**, paste in
     your **Service provider reply URL** from the
     Amazon Managed Grafana workspace.
   - For **Entity ID**, paste in your
     **Service provider identifier** from the
     Amazon Managed Grafana workspace.
   - Make sure that **Sign Assertion** is selected
     and that **Encrypt Assertion** is not
     selected.

6. Choose **Continue to Next Step**.
7. In **SSO Attribute Mapping**, make sure that the
   Amazon Managed Grafana attribute is in **Application Attribute** and
   that the Ping Identity attribute is in the **Identity Bridge
   Attribute**. Then make the following settings:
   - **mail** must be **Email
     (Work)**.
   - **displayName** must be **Display
     Name**.
   - **SAML_SUBJECT** must be **Email
     (Work)**. And then for this attribute, choose
     **Advanced**, set the **Name ID
     Format to send to SP** to
     **urn:oasis:names:tc:SAML:2.0:nameid-format:transient**
     and choose **Save**.
   - Add in any other attribute that you would like to pass.
   - Add any other attributes that you would like to pass. For more
     information about the attributes that you can pass to Amazon Managed Grafana
     in the assertion mapping, see [Assertion mapping](authentication-in-AMG-SAML.md#AMG-SAML-Assertion-Mapping "authentication-in-AMG-SAML.md#AMG-SAML-Assertion-Mapping").

8. Choose **Continue to Next Step**.
9. In **Group Access**, choose which groups to assign
   this application to.
10. Choose **Continue to Next Step**.
11. Copy the **SAML Metadata URL** which starts with
    `https://admin- api.pingone.com/latest/metadata/`. You
    use this later in the configuration.
12. Choose **Finish**.

## Step 2: Steps to complete in

Amazon Managed Grafana

Complete the following steps in the Amazon Managed Grafana console.

###### To finish setting up Ping Identity as an identity provider for

Amazon Managed Grafana

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. In the navigation pane, choose the menu icon.
3. Choose **All workspaces**.
4. Choose the name of the workspace.
5. In the **Authentication** tab, choose **Setup
   SAML configuration**.
6. Under **Import the metadata**, choose
   **Upload or copy/paste** and paste the Ping URL
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
   - (Optional) If you changed the default attributes in your Ping
     Identity application, expand **Additional settings -
     optional** and then set the new attribute
     names.

   By default, the Ping Identity **displayName**
   attribute is passed to the **name** attribute
   and the Ping Identity **mail** attribute is
   passed to both the **email** and
   **login** attributes.

8. Choose **Save SAML Configuration**.
