

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Editing a web portal in Amazon WorkSpaces Secure Browser
<a name="edit-portals"></a>

To edit a web portal, follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/).

1. Choose **WorkSpaces Secure Browser**, **Web portals**, choose your web portal, and then choose **Edit**.
**Note**  
Changes to networking settings or timeout settings immediately end any active portal sessions. Users are disconnected and must reconnect to begin a new session. Changes to **Clipboard permissions**, **File transfer permissions**, or **Print to local device** apply beginning with the first new session. Currently active sessions aren't disconnected. Users connected to active sessions aren't affected by the changes until they disconnect and connect to a new session.