# Set up the Authorization Code flow for Salesforce

Refer to Salesforce public documentation for enabling the OAuth 2.0 Authorization Code flow.

To configure the connected app:

1. Activate the **Enable OAuth Settings** checkbox.
2. In the **Callback URL** text field, enter one or more redirect URLs for AWS Glue.

Redirect URLs have the following format:

https://`region`.console.aws.amazon.com/gluestudio/oauth

In this URL, _region_ is the code for the AWS Region where you use AWS Glue to transfer data from Salesforce. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

https://us-east-1.console.aws.amazon.com/gluestudio/oauth

For the AWS Regions that AWS Glue supports, and their codes, see [AWS Glue endpoints and quotas](../../../general/latest/gr/glue.md "../../../general/latest/gr/glue.md") in the _AWS General Reference_. 3. Activate the **Require Secret for Web Server Flow** checkbox. 4. In the **Available OAuth Scopes** list, add the following scopes:

    * Manage user data via APIs (api)
    * Access custom permissions (custom\_permissions)
    * Access the identity URL service (id, profile, email, address, phone)
    * Access unique user identifiers (openid)
    * Perform requests at any time (refresh\_token, offline\_access)

5. Set the refresh token policy for the connected app to **Refresh token is valid until revoked**. Otherwise, your jobs will fail when your refresh token expires. For more information on how to check and edit the refresh token policy, see [Manage OAuth Access Policies for a Connected App](https://help.salesforce.com/articleView?id=connected_app_manage_oauth.htm "https://help.salesforce.com/articleView?id=connected_app_manage_oauth.htm") in the Salesforce documentation.
