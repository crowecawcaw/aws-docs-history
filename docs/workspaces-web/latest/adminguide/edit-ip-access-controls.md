

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Editing an IP access control group in Amazon WorkSpaces Secure Browser
<a name="edit-ip-access-controls"></a>

You can delete a rule from an IP access setting at any time. If you remove a rule that was used to allow a connection to a web portal, any users with a current session will be disconnected from the web portal.

To edit an IP access control group, follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/).

1. In the navigation pane, choose **IP access controls**.

1. Select the group and choose **Edit**.

1. Edit the existing rules **Source** and **Description** (optional), or add additional rules.

1. Under **Tags**, choose whether to tag a key value pair for each IP access control group.

1. When you are done adding rules and tags, choose **Save**.

1. If you updated an existing IP access setting, wait up to 15 minutes for the new or edited rule to take effect.