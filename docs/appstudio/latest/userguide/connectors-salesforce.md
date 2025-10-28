# Connect to Salesforce

To connect App Studio with Salesforce to enable builders to access and use Salesforce resources in applications, you must create and configure a connected app
in Salesforce and create a Salesforce connector in App Studio.

###### To connect Salesforce with App Studio

1. In App Studio, in the navigation pane, choose **Connectors** in the **Manage** section.
   You will be taken to a page displaying a list of existing connectors with some details about each.
2. Choose **+ Create connector**.
3. Choose **Salesforce** from the list of connector types to open the connector creation page.
4. Take note of the **Redirect URL**, which you will use to configure Salesforce in the following steps.
5. The next step is to create a connected app in Salesforce.
   In another tab or window, navigate to your Salesforce instance.
6. In the Quick Find box, search `App Manager` and then select **App Manager**.
7. Choose **New Connected App**.
8. In **Connected App Name** and **API Name**, enter a name for your app. It does not have to match your App Studio app name.
9. Provide contact information as needed.
10. In the **API (Enable OAuth Settings)** section, enable **Enable OAuth Settings**.
11. In **Callback URL**, enter the **Redirect URL** you noted earlier from App Studio.
12. In **Selected OAuth Scopes**, add the necessary permissions scopes from the list. App Studio can interact with Salesforce REST APIs to
    perform CRUD operations on five objects: Accounts, Cases, Contacts, Leads, and Opportunities. It is recommended to add **Full access (full)** to
    ensure that your App Studio app has all relevant permissions or scopes.
13. Disable the **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows** option. PKCE is not supported
    by App Studio.
14. Enable **Require Secret for Web Server Flow** and **Require Secret for Refresh Token Flow** to follow the best security practices.
15. App Studio supports both of the following authentication flows:
    - **Client Credentials Flow**: Ideal for server-to-server interactions where the application
      acts on its own behalf without user interaction. For example, listing all leads information for a team of temporary employees who do not have Salesforce access.
    - **Authorization Code Flow**: Suitable for applications that act on behalf of a user, such as
      personal data access or actions. For example, listing each sales manager’s leads sourced or owned by them to perform other tasks through this app.
    - For the Client Credentials Flow:
      1. Enable **Enable Client Credentials Flow**. Review and confirm the message.
      2. Save the app.
      3. You must select an execution user, although there is no user interaction in the flow. By selecting an execution user, Salesforce returns access
         tokens on behalf of the user.
         1. In the **App Manager**, from the list of apps, choose the arrow of the App Studio app and choose **Manage**.
         2. Choose **Edit Policies**
         3. In **Client Credentials Flow**, add the appropriate user.

    - For the Authorization Code Flow, enable **Enable Authorization Code and Credentials Flow**

16. Salesforce provides a Client ID and Client Secret, which must be used to configure the connector in App Studio in the following steps.
    1. In the **App Manager**, choose the arrow of the App Studio app and choose **View**.
    2. In the **API (Enable OAuth Settings)** section, choose **Manage Consumer Details** . This may send an email
       for a verification key, which you need to enter for confirmation.
    3. Note the **Consumer Key** (Client ID) and the **Consumer Secret** (Client Secret).

17. Back in App Studio, configure and create your connector by filling out the following fields.
18. In **Name**, enter a name for your Salesforce connector.
19. In **Description**, enter a description for your Salesforce connector.
20. In **Base URL**, enter the base URL for your Salesforce instance. It should look like this:
    `https://`hostname`.salesforce.com/services/data/v60.0`, replacing `hostname` with your Salesforce instance name.
21. In **Authentication method**, ensure **OAuth 2.0** is selected.
22. In **OAuth 2.0 Flow**, select the OAuth authentication method and fill out the related fields:
    - Select **Client credentials flow** for use in applications that act on their own behalf, for system-to-system integrations.
      1. In **Client ID**, enter the **Consumer Key** obtained previously from Salesforce.
      2. In **Client secret**, enter the **Consumer Secret**, obtained previously from Salesforce.
      3. In **Access token URL**, enter the OAuth 2.0 token endpoint. It should look like this:
         `https://`hostname`/services/oauth2/token`, replacing `hostname` with your Salesforce instance name. For more information, see the [Salesforce OAuth Endpoints](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_endpoints.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_endpoints.htm&type=5") documentation.
      4. Choose **Verify connection** to test the authentication and connection.

    - Select **Authorization code flow** for use in applications that act on behalf of the user.
      1. In **Client ID**, enter the **Consumer Key** obtained previously from Salesforce.
      2. In **Client secret**, enter the **Consumer Secret**, obtained previously from Salesforce.
      3. In **Authorization URL**, enter the authorization endpoint. It should look like this:
         `https://`hostname`/services/oauth2/authorize`, replacing `hostname` with your Salesforce instance name. For more information, see the [Salesforce OAuth Endpoints](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_endpoints.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_endpoints.htm&type=5") documentation.
      4. In **Access token URL**, enter the OAuth 2.0 token endpoint. It should look like this:
         `https://`hostname`/services/oauth2/token`, replacing `hostname` with your Salesforce instance name. For more information, see the [Salesforce OAuth Endpoints](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_endpoints.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_endpoints.htm&type=5") documentation.

23. In **Operations**, select the Salesforce operations that your connector will support. The operations in this list are predefined
    and represent common tasks within Salesforce, such as creating, retrieving, updating, or deleting records from common objects.
24. Choose **Create**. The newly created connector will appear in the **Connectors** list.
