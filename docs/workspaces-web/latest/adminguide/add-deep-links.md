

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Setting up deep links in Amazon WorkSpaces Secure Browser
<a name="add-deep-links"></a>

To allow permission for deep links, choose **Allowed** when creating user settings. The site you want to deep link to must be URL-encoded. For example, to link a user to “https://www.example.com/?query=true”, update the link to https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue.

A deeplink can contain up to 10 URLs, delineated by comma. For example:

https://<uuid>.workspaces-web.com/?deepLinks=https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue,https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue2,https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue3,https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue4.

For more information about allowing deep links, see [Configuring user settings for Amazon WorkSpaces Secure Browser](user-settings.md).