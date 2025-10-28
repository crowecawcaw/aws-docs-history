# Enable auto-accept call for agents

When Auto-Accept Call is enabled for an available agent, the agent connects to
contacts automatically.

This functionality doesn't apply to chats, tasks, or emails.

## How long until the call is connected to the

agent?

###### Note

While the call will be connected in less than one second, there will be no
ringer, only the agent whisper.

Less than one second. When a call arrives to an available agent who has
Auto-Accept Call enabled, the Contact Control Panel (CCP) briefly shows the options
**Accept** or **Reject**. This is expected
behavior. After less than a second, the call is automatically accepted and these
options disappear.

There isn't an option for increasing
the amount of time before a call is automatically accepted.

Auto-Accept Call doesn't work for callbacks.

## Enable auto-accept call for existing

agents

You can't enable Auto-Accept Call while editing multiple existing users in your
Amazon Connect instance. You must edit existing users individually to enable it. However, you
can configure the setting for multiple new users when you bulk upload new users with
the CSV template.

1. Log in to the Amazon Connect admin website at https://`instance
name`.my.connect.aws/. Use an Admin account, or an account with
   **Users and Permissions** - **Users**

- **Create** or **Edit** permission in
  it's security profile.

2. On the left navigation menu, choose **Users**,
   **User management**.
3. In the list of users, select an agent, and then choose
   **Edit**.
4. On the **Edit users** page, under
   **Phone**, choose **Soft phone**, and
   then select the **Auto-Accept Call** check box.
5. Choose **Save**.
6. Repeat these steps for each user that you want to edit.

###### Note

**Firefox users**: If you are using the Firefox
browser and using auto-accept for calls, you must keep the CCP or Agent
Workspace browser tab in focus when you accept and connect to a voice contact.
The CCP conforms to Firefox microphone usage guidance, and only has access to
connect to the user's microphone when CCP tab is in focus.

## Bulk upload new users with

auto-accept call enabled

You can't use the CSV template to edit information for existing users. If you
include duplicate users with different information in the CSV template, you will
receive an error.

1. Log in to the Amazon Connect admin website at https://`instance
name`.my.connect.aws/. Use an Admin account, or an account with
   **Users and Permissions** - **Users**

- **Create** permission in it's security profile.

2. On the left navigation menu, choose **Users**,
   **User management**.
3. Choose **Add new users**.
4. Choose **Import users using a .csv template**.
5. Choose to download the template for a pre-formatted CSV file.
6. In the CSV file, configure the details for the new users who you want to
   add. For **soft phone auto accept (yes/no)**, be sure to
   enter **yes**.
7. After configuring the CSV file, in your Amazon Connect instance, choose
   **Upload file**, and then choose the configured CSV
   file from its location on your computer.
8. Under **Upload file and verify**.
9. Under **Verify user details**, verify that the
   information is correct for the new users, and then choose
   **Save**.

## (Optional) Verify the change

in CCP logs

To confirm that **Auto-Accept Call** is enabled for an agent,
download the CCP logs generated for that agent: in the CCP for the agent, choose
**Settings**, **Download logs**. The logs are
saved to your browser's default download directory.

In the logs, the **autoAccept** attribute is set to
**"true"** if this setting is enabled. The logs show something
like this:

```

                  "type": "agent",
                  "initial": false,
                  "softphoneMediaInfo": {
                       "callType": "audio_only",
                       "autoAccept": true

```
