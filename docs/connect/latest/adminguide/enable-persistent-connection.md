

# Enable persistent connection for Connect Customer agents
<a name="enable-persistent-connection"></a>

When you select **Enable persistent connection** for an agent, the agent's softphone maintains its media connection to Connect Customer for a few minutes after login and after each call ends. This enables subsequent calls to connect faster. If the agent remains idle for an extended period of time, the softphone drops the media connection to reduce agent workstation and network resource consumption. This does not impact the agent's ability to receive calls. The media connection is re-established when the agent receives the next call.

This functionality doesn't apply to chats or tasks.

## How to configure persistent connection for an agent
<a name="howto-persistent-connection"></a>

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an Admin account, or an account with **Users and Permissions** - **Users** - **Create** or **Edit** permission in it's security profile.

1. On the left navigation menu, choose **Users**, **User management**.

1. In the list of users, select an agent, and then choose **Edit**.

1. On the **Edit users** page, under **Phone**, choose **Softphone**, and then

   a) select **Enable persistent connection** - to enable the feature

   b) deselect **Enable persistent connection** - to disable the feature

1. Choose **Save**.

## Configure Persistent Connection using Bulk upload for new users
<a name="bulk-upload-users-persistent-connection"></a>

You can't use the CSV template to edit information for existing users. If you include duplicate users with different information in the CSV template, you will receive an error.

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an Admin account, or an account with **Users and Permissions** - **Users** - **Create** permission in it's security profile.

1. On the left navigation menu, choose **Users**, **User management**.

1. Choose **Add new users**.

1. Choose **Import users using a .csv template**.

1. Download the template for a pre-formatted CSV file.

1. In the CSV file, configure the details for the new users who you want to add.

   a) To enable persistent connection - **persistent connection (yes/no)**, be sure to enter **yes**.

   b) To disable persistent connection - **persistent connection (yes/no)**, be sure to enter **no**.

1. After configuring the CSV file, in your Connect Customer instance, choose **Upload file**, and then choose the configured CSV file from its location on your computer.

1. Under **Upload file and verify**. 

1. Under **Verify user details**, verify that the information is correct for the new users, and then choose **Save**.

## FAQ
<a name="faq-persistent-connection"></a>

### When is the softphone connection created?
<a name="faq-1"></a>

The media connection for agent softphone is created upon the first incoming or outbound call for the agent.

### Does the softphone connection persist for the entire agent session?
<a name="faq-2"></a>

If the agent makes or receives another call within a few minutes of a previous call ending, the softphone connection gets re-used to reduce call setup time for the new call. This process repeats (and the session persists) for as long as the agent keeps placing or receiving calls in quick succession. However, if the agent remains idle for several minutes, then the connection is dropped. In such cases, the connection is re-created silently upon the next call.

### Can the agent opt-out of persistent connection?
<a name="faq-3"></a>

Only the contact center administrator can enable or disable this feature for agents using steps mentioned above. Agents cannot disable persistent connection.

### Are there any browser restrictions for using this feature?
<a name="faq-4"></a>

This feature is available on supported versions of [Chrome and Edge](connect-supported-browsers.md). It's not supported on Firefox.

### Can this feature be used when VDI audio optimization is enabled?
<a name="faq-5"></a>

Yes.

### Is this feature supported on custom Call Control Panels (CCPs)? Is there a change needed to the Call Control Panel (CCP) to use this feature?
<a name="faq-6"></a>

If your custom CCP uses the softphone from Connect Customer embedded iframe (that is, if `allowFramedSoftphone` is passed as true to initiate the CCP using [Connect Customer Streams JS](https://github.com/amazon-connect/amazon-connect-streams)), then you don't need to make any changes for this functionality to work. 

If your custom CCP integrates [Connect Customer RTC JS](https://github.com/aws/connect-rtc-js) in it's own frame, then you need to upgrade the same.