

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# User access logging in Amazon WorkSpaces Secure Browser
<a name="data-protection-logging"></a>

Administrators are able to record WorkSpaces Secure Browser session events, including start, stop, and URL visits. These logs are encrypted and securely delivered to customers through an Amazon Kinesis Data Stream. Browsing information from user access logging is not stored by AWS, or available from sessions without logging configured. URL visits in incognito mode, or deleted URLs from browser history, are not recorded in user access logging.