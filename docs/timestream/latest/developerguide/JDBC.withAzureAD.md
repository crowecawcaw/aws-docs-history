For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Setting up Azure AD

1. Sign in to Azure Portal
2. Choose **Azure Active Directory** in the list of Azure
   services. This will redirect to the Default Directory page.
3. Choose **Enterprise Applications** under the
   **Manage** section on the sidebar
4. Choose **+ New application**.
5. Find and select **Amazon Web Services**.
6. Choose **Single Sign-On** under the
   **Manage** section in the sidebar
7. Choose **SAML** as the single sign-on method
8. In the Basic SAML Configuration section, enter the following URL for both
   the Identifier and the Reply URL:

```
https://signin.aws.amazon.com/saml
```

9. Choose **Save**
10. Download the Federation Metadata XML in the SAML Signing Certificate
    section. This will be used when creating the IAM Identity Provider
    later
11. Return to the Default Directory page and choose **App
    registrations** under **Manage**.
12. Choose **Timestream for LiveAnalytics** from the **All
    Applications** section. The page will be redirected to the
    application's Overview page

###### Note

Note the Application (client) ID and the Directory (tenant) ID. These
values are required for when creating a connection. 13. Choose **Certificates and Secrets** 14. Under **Client secrets**, create a new client secret with
**+ New client secret**.

###### Note

Note the generated client secret, as this is required when creating a
connection to Timestream for LiveAnalytics. 15. On the sidebar under **Manage**, select **API
permissions** 16. In the **Configured permissions**, use **Add a
permission** to grant Azure AD permission to sign in to
Timestream for LiveAnalytics. Choose **Microsoft Graph** on the Request API
permissions page. 17. Choose **Delegated permissions** and select the
**User.Read** permission 18. Choose **Add permissions** 19. Choose **Grant admin consent for Default
Directory**
