AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Specify an idle session timeout

value

Session Manager, a tool in AWS Systems Manager, allows you to specify the amount of time to
allow a user to be inactive before the system ends a session. By default,
sessions time out after 20 minutes of inactivity. You can modify this setting to
specify that a session times out between 1 and 60 minutes of inactivity. Some
professional computing security agencies recommend setting idle session timeouts
to a maximum of 15 minutes.

###### To allow idle session timeout (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Session Manager**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. Specify the amount of time to allow a user to be inactive before a
   session ends in the **minutes** field under
   **Idle session timeout**.
5. Choose **Save**.
