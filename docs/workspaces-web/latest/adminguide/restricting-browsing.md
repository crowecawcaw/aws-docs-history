

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Restricting browsing to specific URLs
<a name="restricting-browsing"></a>

You can implement a "default deny" policy where only explicitly approved websites and URLs are accessible. It's ideal for high-security environments where internet access must be tightly controlled and every permitted site has been vetted for business necessity and security compliance.

In the AWS console, under URL filtering:
+ Navigate to Block list and select the toggle **Block all URLs**
+ Under Allow list, click **Add URL** to add a URL that will be allow listed for your end user. Add one entry per URL.
+ Click **Save**