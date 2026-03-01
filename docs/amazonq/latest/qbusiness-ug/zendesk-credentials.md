# Setting up Zendesk for connecting to Amazon Q Business

Before you connect Zendesk to Amazon Q Business, you need to create and
retrieve the Zendesk credentials you will use to connect Zendesk to
Amazon Q. You will also need to add any authorization permissions needed by
Zendesk to connect to Amazon Q.

The following procedure gives you an overview of how to configure Zendesk for
Amazon Q.

###### Configuring Zendesk for OAuth 2.0 authentication

1. Log in to your Zendesk account. Note the username and password you logged
   in with. You will need them later to connect to Amazon Q.
2. Copy your Zendesk URL, if you haven't already, from the Zendesk
   webpage URL. This will be the URL you will input as host URL in Amazon Q.

###### Note

You can also copy your Zendesk host URL from the top menu in the
**Admin Center**. 3. From the left navigation menu, choose the settings icon. Then, choose **Go to
Admin Center**.

![Screenshot of the Zendesk admin interface showing the profile menu where users can access the Admin Center.](images/zendesk-1.png) 4. In **Admin Center**, from the left navigation menu, under
**Apps and integrations**, choose **Zendesk
API**.

![Screenshot of the Zendesk Admin Center showing the left navigation menu with the "Zendesk API" option under "Apps and integrations" section.](images/zendesk-2.png) 5. From the **Zendesk API** menu, choose **OAuth
Clients** and then choose **Add OAuth client**.

![Screenshot of the Zendesk API menu showing the "OAuth Clients" option and the "Add OAuth client" button for creating a new OAuth client.](images/zendesk-3.png) 6. On the **OAuth Clients** page, under **Create a new OAuth
client** enter the following information:

    * **Client name** – A human-readable name for your client.
     This will be visible to users.
    * **Unique identifier** – An internal code-level identifier
     for your client. This will be the Client ID you input in Amazon Q.

Optionally, choose to fill in other information based on your use case. Then, choose
**Save**.

![Screenshot of the Zendesk "Create a new OAuth client" form where users enter client name, redirect URL, and other configuration details for the OAuth client.](images/zendesk-4.png) 7. On the **Please store the secret that will appear** dialog box that
appears, select **OK**. Then, copy the secret you see into a text editor
of your choice and save it. You won't be able to re-generate this secret so it's important
that you store it securely. You will input this as the client secret during the connection
configuration process in Amazon Q.

![Screenshot of the Zendesk client secret dialog box showing the generated secret that needs to be copied and stored securely for API authentication.](images/zendesk-5.png)

You now have the username, password, host URL, client ID, and client secret you need
to connect Zendesk to Amazon Q.
