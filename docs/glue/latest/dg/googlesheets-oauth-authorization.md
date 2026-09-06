

# Set up Authorization code OAuth flow for Google Sheets
<a name="googlesheets-oauth-authorization"></a>

 **Prerequisites** 
+  A Google account where you can sign in to use the Google Sheets app. In your Google account, Google Sheets contains the data that you want to transfer. 
+  A Google Cloud Platform account and a Google Cloud project. See [ Create Google Cloud Project ](https://developers.google.com/workspace/guides/create-project) for more details. 

**To set up your Google account and get OAuth 2.0 credentials:**

1.  Once the Google Cloud project is setup, enable the Google Sheets API and Google Drive APIs in the project. For the steps to enable them, see [ Enable and disable APIs ](https://support.google.com/googleapi/answer/6158841) in the API Console Help for Google Cloud Platform. 

1.  Next, configure an OAuth consent screen for external users. For more information about the OAuth consent screen, see [ Setting up your OAuth consent screen ](https://support.google.com/cloud/answer/10311615#) in the Google Cloud Platform Console Help. 

1.  In the OAuth consent screen, add the following scopes: 
   +  [ The Google Sheets API read-only scope ](https://www.googleapis.com/auth/spreadsheets.readonly) 
   +  [ The Google Drive API read-only scope ](ttps://www.googleapis.com/auth/drive.readonly) 

    For more information about these scopes, see [ OAuth 2.0 Scopes for Google APIs ](https://developers.google.com/identity/protocols/oauth2/scopes) in the Google Identity documentation. 

1.  Generate OAuth 2.0 client ID and secret. For the steps to create this client ID, see [ Setting up OAuth 2.0 ](https://support.google.com/cloud/answer/6158849?hl=en#zippy=) in the Google Cloud Platform Console Help. 

    The OAuth 2.0 client ID must have one or more authorized redirect URLs. 

    Redirect URLs have the following format: 
   + https://<aws-region>.console.aws.amazon.com/gluestudio/oauth 

1.  Note the client ID and client secret from the settings for your OAuth 2.0 client ID. 