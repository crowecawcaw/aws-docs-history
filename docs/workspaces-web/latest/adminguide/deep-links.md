

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Deep links in Amazon WorkSpaces Secure Browser
<a name="deep-links"></a>

When a user signs into WorkSpaces Secure Browser, they start the session on a home page set by the administrator. You can also allow portals to receive deep links that connect users to a specific website during a session. When a deep link is selected, the portal displays the URL specified in the deep link. The link is displayed alongside the home page(s) configured for session start, or by itself if a session is already in progress. This feature allows administrators to create more dynamic user experiences with WorkSpaces Secure Browser.

Deep links open pages in a WorkSpaces Secure Browser session. If a session is already running, it will open the deep link in a new tab. If a session is not already running, it will open the deep link URL in a new tab, and the portal default home page in a separate tab. If a deep link contains more than one URL, it will display the deep link URL listed first in focus, with each subsequent URL (including the default home page) opened in separate tabs.

**Topics**
+ [Setting up deep links in Amazon WorkSpaces Secure Browser](add-deep-links.md)
+ [Using URL filtering for deep links in Amazon WorkSpaces Secure Browser](filtering-deep-links.md)