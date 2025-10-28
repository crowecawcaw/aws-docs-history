# Setting up Salesforce Online for connecting to

Amazon Q Business

Before you connect Salesforce Online to Amazon Q Business, you need to create and
retrieve the Salesforce Online credentials you will use to connect Salesforce Online to
Amazon Q. You will also need to add any authorization permissions needed by
Salesforce Online to connect to Amazon Q.

The following procedure gives you an overview of how to configure Salesforce Online for
Amazon Q.

###### Configuring Salesforce Online for Amazon Q

1. Create a Salesforce Online instance at [https://developer.salesforce.com/signup](https://developer.salesforce.com/signup "https://developer.salesforce.com/signup"). Note the username and password you
   logged in with. Also note the Salesforce Online URL that's sent to your email on
   successful instance setup.

You will need these pieces of information later to connect to Amazon Q. 2. Log in to your Salesforce Online Developer Edition account at [https://login.salesforce.com](https://login.salesforce.com "https://login.salesforce.com") or
Salesforce Online Sandbox Edition account at [https://test.salesforce.com](https://test.salesforce.com "https://test.salesforce.com"). 3. From the Salesforce Online profile menu, copy your Salesforce Online URL, if you
haven't already. This will be the URL you will input as host URL in Amazon Q.

![Screenshot showing the Salesforce login page where users enter their credentials to access their Salesforce instance.](images/salesforce-1.png) 4. Then, from the Salesforce Online profile menu, select the **Setup**
icon and then select **Setup**.

![Screenshot of the Salesforce profile menu showing the Setup icon and Setup option that users need to select to access the setup page.](images/salesforce-3.png) 5. From the left navigation menu, on the **Setup** home page, go to
**Platform tools**, select **Apps**, and then, select
**App manager**.

Then, from the **Lightning Experience App Manager** page, select
**New Connected App**.

![Screenshot of the Salesforce Lightning Experience App Manager page showing the "New Connected App" button that users need to click to create a new connected app.](images/salesforce-2.png) 6. On the **New Connected App** page, do the following:

    * In **Basic information**, enter the following required
     information:




    	+ **Connect App Name** – A name for your connected
    	 app.
    	+ **API Name** – A name for your API.
    	+ **Contact Email** – Your contact email.

    ![Screenshot of the Salesforce "New Connected App" page showing the Basic Information section where users enter the app name, API name, and contact email.](images/salesforce-4.png)

    Enter other values as per your use case.
    * In **API (Enable OAuth Settings)**, select the checkbox to
     enable. Then, enter the following information:




    	+ **Callback URL** – Enter the following callback URL,
    	 depending on your Salesforce Online account type:




    		- Developer Edition –
    		 `https://login.salesforce.com/services/oauth2/token`
    		- Sandbox Edition –
    		 `https://test.salesforce.com/services/oauth2/token`
    	Also, copy and save this URL in a text editor of your choice. You will enter
    	 this callback URL in Amazon Q later as **Authentication
    	 URL**.
    	+ **Select OAuth Scopes** – Select **Full access
    	 (full)** as your OAuth Scope.
    	+ **Introspect All Tokens** – Select this option to
    	 generate access tokens in a future step. You need this access token to connect to
    	 Amazon Q. You enter this as the **Security token**
    	 in the Amazon Q console.
    Select other options as per your use case.


    * Select **Save**.

7. From the **Manage Connected Apps** page that opens, choose
   **Manage Consumer Details**. You will be redirected to a
   **Connected App Name** summary page.

![Screenshot of the Salesforce confirmation message indicating that the connected app has been created successfully and will be available after a short delay.](images/salesforce-6.png) 8. On the **Connected App Name** page, do the following:

    * From **Consumer Details**, copy and save the following in a text
     editor of your choice:




    	+ **Consumer Key** – You will need this to connect
    	 Salesforce Online to Amazon Q.
    	+ **Consumer Secret** – You will need this to connect
    	 Salesforce Online to Amazon Q.
    	+ Select **Apply**.



    	![Screenshot of the Salesforce Connected App details page showing the Consumer Details section with the Consumer Key (client ID) and Consumer Secret that need to be copied for API authentication.](images/salesforce-7.png)

9. Next, you will generate a security token. Navigate back to your Salesforce Online
   account home page. From the Salesforce Online profile menu, select
   **Settings**.

![Screenshot of the Salesforce user menu showing the "Settings" option that users need to select to access personal settings for generating a security token.](images/salesforce-8.png) 10. Then, from the left navigation menu, select **My Personal
Information**. Then, select **Reset My Security Token**. Your
security token will be sent to the email address connect to your Salesforce Online
instance. You need this security token to connect Salesforce Online to Amazon Q.

![Screenshot of the Salesforce personal settings page showing the "My Personal Information" menu with the "Reset My Security Token" option highlighted for generating a new security token.](images/salesforce-9.png) 11. Then, you activate OAuth Username-Password Flow for the Salesforce Online Connected
App you've created. From the left navigation menu, from **Settings**,
select **Identity** and then select **OAuth and OpenID Connect
Settings**. 12. On the **OAuth and OpenID Connect Settings**, in **OAuth and
OpenID Connect Flows**, make sure that both **Allow OAuth
Username-Password Flows** and **Allow OAuth User-Agent Flows**
are activated.

![Screenshot of the Salesforce OAuth and OpenID Connect Settings page showing the OAuth settings configuration options for enabling the Username-Password flow for the connected app.](images/salesforce-11.png)

You now have the Salesforce Online host URL, username, password, security token,
client ID, client secret, and authentication URL you need to connect Salesforce Online to
Amazon Q.
