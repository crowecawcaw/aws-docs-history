

# Creating an Adobe Analytics account
<a name="adobeanalytics-create-account"></a>

1. Register for the exchange partner program, by accessing [Adobe Partner program](https://partners.adobe.com/exchangeprogram/creativecloud.html). 

1. Choose **Join Exchange Program**. 

1. Register or create an account using your corporate email address. 

1. From the suggestion box, select the appropriate company that has an Adobe Analytics product subscription. 

1. Ensure that the account gets registered with a valid organization (from the list available) that has an active Adobe Analytics subscription. 

1. After the company administration's approval, activate your account by clicking on the link in the approval email. 

**Verifying if the account that you created has access to Adobe Analytics service**

1. Log in to [Adobe Admin Console](https://adminconsole.adobe.com/).

1. Check the organization name at the top-right corner of the page to ensure that you have logged in to the correct company.

1. Select **Products** and verify if Adobe Analytics is available.
**Note**  
If no organization is available, or Adobe Analytics product is greyed out or is unavailable, it is likely that your account is not associated with an organization and/or has no active Adobe Analytics subscription. Contact your system admin to request access for this service for your account.

**Creating a project and `OAuth2.0` credentials**

1. Log in to Adobe Analytics account where you want the [ OAuth 2.0 app](https://developer.adobe.com/developer-console/docs/guides/services/services-add-api-oauth/) to be created.

1. Select **Project** and then **Create a new project**. 

1. To add a project, select **Add to project**, and then select **API**.

1. Select **Adobe Analytics API**.

1. Select **OAUTH** as user authentication.

1. Select **Web** as `OAUTH` and provide the redirect URI. 

   For redirect URI and its pattern, see the following:
   + `OAuth 2.0` default redirect URI – A default redirect URI is the URL of the page that Adobe will access during the authentication process. For example, `https://ap-southeast-2.console.aws.amazon.com/appflow/oauth` 
   + OAuth 2.0 Redirect URI pattern – A Redirect URI pattern is a URI path (or comma-separated list of paths) to which Adobe can redirect (if requested) when the login flow is complete. For example, `https://ap-southeast-2\\.console\\.aws\\.amazon\\.com`

1. Add the following scopes: 
   + `openid`
   + `read_organizations`
   + `additional_info.projectedProductContext`
   + `additional_info.job_function`

1. Choose **Save credential**.

1. After the app is created, copy the `Client ID` and `Client Secret` values to a text file.