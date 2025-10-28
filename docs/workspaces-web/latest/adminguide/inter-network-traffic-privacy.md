# Inter-network traffic privacy in Amazon WorkSpaces Secure Browser

To secure connections between WorkSpaces Secure Browser and on-premise applications, you use WorkSpaces Secure Browser to launch
browser sessions inside of your own VPC. The connection to on-premise applications is
configured in your own VPC, and is not controlled by WorkSpaces Secure Browser.

To secure connections between accounts, WorkSpaces Secure Browser uses a service-linked role to securely
connect to customer accounts and run operations on behalf of the customer. For more
information, see [Using service-linked roles for
Amazon WorkSpaces Secure Browser](using-service-linked-roles.md "using-service-linked-roles.md").
