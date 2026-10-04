

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Inter-network traffic privacy in Amazon WorkSpaces Secure Browser
<a name="inter-network-traffic-privacy"></a>

To secure connections between WorkSpaces Secure Browser and on-premise applications, you use WorkSpaces Secure Browser to launch browser sessions inside of your own VPC. The connection to on-premise applications is configured in your own VPC, and is not controlled by WorkSpaces Secure Browser.

To secure connections between accounts, WorkSpaces Secure Browser uses a service-linked role to securely connect to customer accounts and run operations on behalf of the customer. For more information, see [Using service-linked roles for Amazon WorkSpaces Secure Browser](using-service-linked-roles.md).