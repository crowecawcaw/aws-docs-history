# Creating a Google Ads account

1. Log in to [Google Ads Developer Account](https://console.cloud.google.com "https://console.cloud.google.com")
   with your credentials, and go to \*MyProject.

![The screenshot shows the welcome screen to log in to the Google Ads Developer Account.](images/google-ads-log-in-developer-account.png) 2. Choose **New Project** and provide the information which is required for creating Google project
if you don't have any registered application in it.

![The screenshot shows the select a project page. Choose New Project in the upper right hand corner.](images/google-ads-new-project.png)

![The screenshot shows the New Project window to enter a project name and choose a location.](images/google-ads-new-project-name-location.png) 3. Choose the **Navigation Tab**, then **API and Setting**, and **Create
Client Id** and **ClientSecret** which will require further configuration for creating a
connection between AWS Glue and GoogleAds. For more information, see
[API credentials](https://console.cloud.google.com/apis/credentials "https://console.cloud.google.com/apis/credentials").

![The screenshot shows the APIs and services configuration page.](images/google-ads-apis-and-services.png) 4. Choose **CREATE CREDENTIALS** and choose **OAuth client ID**.

![The screenshot shows the APIs and services configuration page with the Create Credentials drop-down and the Oauth client ID option highlighted.](images/google-ads-create-credentials.png) 5. Select the **Application type** as **Web application**.

![The screenshot shows the Create OAuth client ID page and the Application type as Web application.](images/google-ads-oauth-client-id-application-type.png) 6. Under **Authorised redirect URIs**, add the OAuth Redirect URIs and choose **Create**.
You can add multiple redirect URIs if required.

![The screenshot shows the Create OAuth client ID page and the Authorised redirect URIs section. Here, add the URIs and choose ADD URI if needed. Once done, choose CREATE.](images/google-ads-oauth-redirect-uris.png) 7. Your **Client Id** and **Client Secret** will be generated when creating a
connection between AWS Glue and Google Ads.

![The screenshot shows the Create OAuth client ID page and the Authorised redirect URIs section. Here, add the URIs and choose ADD URI if needed. Once done, choose CREATE.](images/google-ads-oauth-client-created.png) 8. Add the scopes according to your application need based, choose **OAuth consent screen** and provide
the required information and add the scopes based on requirements.

![The screenshot shows the Update selected scopes page. Select your scopes as needed.](images/google-ads-selected-scopes.png)
