

# Associate data protection settings in Amazon WorkSpaces Secure Browser
<a name="associate-data-protection-settings"></a>

You can associate data protection settings in WorkSpaces Secure Browser.

**To associate a data protection setting with an existing portal**

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/).

1. In the left hand navigation pane, choose **Web portals**.

1. Select the web portal, and choose **Edit**.

1. Under **Data protection settings**, select the setting for your portal.

1. Choose **Save**.

To associate a data protection setting when creating a new portal, follow these steps.

**To associate a data protection setting when creating a new portal**

1. Follow the instructions in [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md) to create a portal, until you get to **data protection setting**.

1. Choose your **data protection setting** from the drop-down menu.

1. Complete the steps in [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md) to finish creating your portal.

To create a data protection setting when creating a new portal, follow these steps.

**To create a data protection setting when creating a new portal**

1. Follow the instructions in [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md) to create a portal, until you get to **data protection setting**.

1. Choose **data protection settings** from the drop-down menu.

1. Enter a display name (required) and description (optional) for the setting. 

1. Select the default settings for inline redaction. You can set the following:
   + The level of strictness of all data types
   + The domains on which redaction should be enforced

1. Choose your base inline redaction data types from the supported types, or create a custom data type. You can set overrides for each data type, including the level of strictness and domain exceptions.

1. Add any **Tags** (optional) for reporting.

1. When you are done, choose **Save**.

1. Select the refresh button under **data protection settings**, then choose your data protection setting from the drop-down menu.

1. Continue to follow the create portal instructions to finish creating your portal.