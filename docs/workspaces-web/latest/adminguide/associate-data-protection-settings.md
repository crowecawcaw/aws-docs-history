# Associate data protection settings in Amazon WorkSpaces Secure Browser

You can associate data protection settings in WorkSpaces Secure Browser.

###### To associate a data protection setting with an existing portal

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/ "https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/").
2. In the left hand navigation pane, choose **Web portals**.
3. Select the web portal, and choose **Edit**.
4. Under **Data protection settings**, select the setting for your
   portal.
5. Choose **Save**.
   To associate a data protection setting when creating a new portal, follow these
   steps.

###### To associate a data protection setting when creating a new portal

1. Follow the instructions in [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md "getting-started-step1.md") to create a portal,
   until you get to **data protection setting**.
2. Choose your **data protection setting** from the drop-down menu.
3. Complete the steps in [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md "getting-started-step1.md") to finish creating your
   portal.
   To create a data protection setting when creating a new portal, follow these steps.

###### To create a data protection setting when creating a new portal

1. Follow the instructions in [Creating a web portal for Amazon WorkSpaces Secure Browser](getting-started-step1.md "getting-started-step1.md") to create a portal,
   until you get to **data protection setting**.
2. Choose **data protection settings** from the drop-down menu.
3. Enter a display name (required) and description (optional) for the setting.
4. Select the default settings for inline redaction. You can set the following:
   - The level of strictness of all data types
   - The domains on which redaction should be enforced

5. Choose your base inline redaction data types from the supported types, or create a custom
   data type. You can set overrides for each data type, including the level of strictness and
   domain exceptions.
6. Add any **Tags** (optional) for reporting.
7. When you are done, choose **Save**.
8. Select the refresh button under **data protection settings**, then
   choose your data protection setting from the drop-down menu.
9. Continue to follow the create portal instructions to finish creating your portal.
