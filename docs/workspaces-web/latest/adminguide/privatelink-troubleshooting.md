

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Troubleshooting
<a name="privatelink-troubleshooting"></a>

If your calls to the Amazon WorkSpaces Secure Browser APIs are hanging, there is likely a misconfiguration in your VPC Endpoint Service security group or IAM role setup. To resolve this, try the following:
+ While creating your interface VPC endpoint, it might have automatically attached to your AWS account’s default security group. Try using a different security group, and make sure the inbound and outbound permissions allow you to transfer your data appropriately.
+ Make sure you are using an IAM role that allows you to call Amazon WorkSpaces Secure Browser APIs.