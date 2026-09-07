

# Create data protection settings in Amazon WorkSpaces Secure Browser
<a name="create-data-protection-settings"></a>

You can create data protection settings in WorkSpaces Secure Browser.

**To create data protection settings**

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/).

1. In the left-hand navigation pane, choose **Data Protection Settings**.

1. Choose **Create Data Protection Settings**.

1. Enter a display name (required) and description (optional) for the setting. 

1. Select the default settings for inline redaction. You can set the following:
   + The level of strictness of all data types
   + The domains on which redaction should be enforced

1. Choose your base inline redaction data types from the supported types, or create a custom data type. You can set overrides for each data type, including the level of strictness and domain exceptions.

1. Add any **Tags** (optional) for reporting.

1. When you are done, choose **Save**.