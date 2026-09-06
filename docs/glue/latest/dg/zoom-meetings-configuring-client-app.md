

# Configuring the Zoom Meetings client app
<a name="zoom-meetings-configuring-client-app"></a>

1. Log into the Zoom App Marketplace.

1. Choose **Develop** > **Build App**.

1. Choose **General App** for an OAuth 2.0 based app.

1. On the **Basic Info** page, add or update information about the app such as the app's name, how the app is managed, app credentials, and OAuth information.

1. In the **Select how the app is managed** section, confirm how you want your app to be managed:

   1. **Admin-managed**: Account admins add and manage the app

   1. **User-managed**: Individual users add and manage the app. The app has access to only the user's authorized data.

1. **App Credentials**: The build flow automatically generates app credentials (client ID and client secret) for your app.

1. In the OAuth Information section, set up OAuth for your app.

   1. **OAuth redirect URL** (required): Enter your redirect URL or endpoint to set up OAuth between your app and Zoom.

   1. **Use Strict Mode URL** (optional)

   1. **Subdomain check** (optional)

   1. **OAuth allow lists** (required): Add any unique URLs that Zoom should allow as valid redirects for your OAuth flows.

1. On the **Scopes** page, select the Zoom API methods your app is allowed to call. The scopes define which information and capabilities are available to your user. Select the following granular scopes:
   + user:read:list\_users:admin
   + zoom\_rooms:read:list\_rooms:admin
   + group:read:list\_members:admin
   + group:read:administrator:admin
   + group:read:list\_groups:admin
   + report:read:admin
   + role:read:list\_roles, role:read:list\_roles:admin

   Once the scopes are added choose **Continue** and the app is ready to use.

For more information about OAuth 2.0 setup see [Integrations (OAuth apps)](https://developers.zoom.us/docs/integrations/).