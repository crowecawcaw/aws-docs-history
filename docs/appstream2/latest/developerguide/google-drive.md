

# Enable and Administer Google Drive for Your WorkSpaces Applications Users
<a name="google-drive"></a>

**Note**  
Amazon WorkSpaces Applications's use and transfer to any other app of information received from Google APIs will adhere to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.

Amazon WorkSpaces Applications supports the following persistent storage options for users in your organization: 
+ Google Drive for Google Workspace
+ OneDrive for Business
+ Home folders

You can enable one or more options for your organization. When you enable Google Drive for Google Workspace for an WorkSpaces Applications stack, users of the stack can link their Google Drive for Google Workspace account to WorkSpaces Applications. Then they can sign into their Google Drive for Google Workspace account and access their Google Drive folder during application streaming sessions. Any changes that they make to files or folders in Google Drive during those sessions are automatically backed up and synchronized, so that they are available to users outside of their streaming sessions. 

**Important**  
You can enable Google Drive for Google Workspace for accounts in your Google Workspace domains only, but not for personal Gmail accounts.

**Note**  
You can enable Google Drive for Windows stacks, but not for Linux stacks.  
To enable Google Drive for stacks associated with multi-session fleets, the image must use [WorkSpaces Applications Agent Release Notes](agent-software-versions.md) released on or after June 29, 2026 or your image is using [Update an Image by Using Managed WorkSpaces Applications Image Updates](keep-image-updated-managed-image-updates.md) released on or after June 29, 2026.

**Topics**
+ [Enable Google Drive for Your WorkSpaces Applications Users](enable-google-drive.md)
+ [Disable Google Drive for Your WorkSpaces Applications Users](disable-google-drive.md)