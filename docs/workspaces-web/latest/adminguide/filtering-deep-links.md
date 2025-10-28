# Using URL filtering for deep links in Amazon WorkSpaces Secure Browser

Any user you share this portal link with can manipulate the deep link value to visit a
website, if that domain is reachable from the portal and not on the URL blocklist. To create a
restrictive allowlist or blocklist to prevent users from visiting unintended domains with your
portal, use URL filtering.

The allowlist and blocklist for a portal can be edited with URL filtering in your portal’s
browser settings. To do this, append the URL to an allow-listed portal URL in the following
format, where UUID is the portal id:
https://<uuid>.workspaces-web.com/?deepLinks=https%3A%2F%2Fwww.example.com%2F%3Fquery%3Dtrue

For more information, see [Setting up URL filtering in Amazon WorkSpaces Secure Browser](url-filtering.md "url-filtering.md") and [Allow or block access to
websites](https://support.google.com/chrome/a/answer/7532419?hl=en "https://support.google.com/chrome/a/answer/7532419?hl=en").
