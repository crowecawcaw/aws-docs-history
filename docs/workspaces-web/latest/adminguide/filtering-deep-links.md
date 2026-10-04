

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Using URL filtering for deep links in Amazon WorkSpaces Secure Browser
<a name="filtering-deep-links"></a>

Any user you share this portal link with can manipulate the deep link value to visit a website, if that domain is reachable from the portal and not on the URL blocklist. To create a restrictive allowlist or blocklist to prevent users from visiting unintended domains with your portal, use URL filtering.

The allowlist and blocklist for a portal can be edited with URL filtering in your portal’s browser settings. To do this, append the URL to an allow-listed portal URL in the following format, where UUID is the portal id: https://<uuid>.workspaces-web.com/?deepLinks=https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue

For more information, see [Web content filtering in Amazon WorkSpaces Secure Browser](web-content-filtering.md) and [Allow or block access to websites](https://support.google.com/chrome/a/answer/7532419?hl=en).