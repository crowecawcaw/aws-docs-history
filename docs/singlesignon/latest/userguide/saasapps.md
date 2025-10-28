# Set up an application from the IAM Identity Center application

catalog

You can use the application catalog in the IAM Identity Center console to add many commonly
used SAML 2.0 applications that work with IAM Identity Center. Examples include Salesforce,
Box, and Microsoft 365.

Most applications provide detailed information about how to set up the trust
between IAM Identity Center and the application's service provider. This information is
available in the configuration page for the application, after you select the
application in the catalog. After you configure the application, you can assign
access to users or groups in IAM Identity Center as needed.

Use this procedure to set up a SAML 2.0 trust relationship between IAM Identity Center and
your application's service provider.

Before you begin this procedure, it is helpful to have the service provider's
metadata exchange file so that you can more efficiently set up the trust. If you
do not have this file, you can still use this procedure to configure the trust it
manually.

###### To add and configure an application from the application catalog

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Applications**.
3. Choose the **Customer managed** tab.
4. Choose **Add application**.
5. On the **Select application type** page, under
   **Setup preference**, choose **I want to
   select an application from the catalog**.
6. Under **Application catalog**, start typing the name
   of the application that you want to add in the search box.
7. Choose the name of the application from the list when it appears in
   the search results, and then choose **Next**.
8. On the **Configure application** page, the
   **Display name** and
   **Description** fields are prepopulated with
   relevant details for the application. You can edit this
   information.
9. Under **IAM Identity Center metadata**, do the following:
   1. Under **IAM Identity Center SAML metadata file**, choose
      **Download** to download the
      identity provider metadata.
   2. Under **IAM Identity Center certificate**,
      choose **Download certificate** to download the
      identity provider certificate.###### Note

You will need these files later when you set up the application
from the service provider's website. Follow the instructions from
that provider. 10. (Optional) Under **Application
properties**, you can specify the **Application start URL**, **Relay
state**, and **Session duration**. For
more information, see [Understand application properties in the IAM Identity Center
console](appproperties.md "appproperties.md"). 11. Under **Application metadata**, do one of
the following:

    1. If you have a metadata file, choose **Upload
     application SAML metadata file**. Then, select
     **Choose file** to find and
     select the metadata file.
    2. If you do not have a metadata file, choose **Manually
     type your metadata values**, and then provide the
     **Application ACS URL** and
     **Application SAML audience**
     values.

12. Choose **Submit**. You're taken to the details page
    of the application that you just added.
