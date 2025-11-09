AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# End a session

You can end a session that you started in your account using the AWS Systems Manager console
or the AWS Command Line Interface (AWS CLI). When you choose the **Terminate** button
for a session in the console or call the [TerminateSession](../APIReference/API_TerminateSession.md "../APIReference/API_TerminateSession.md") API action by using the AWS CLI, Session Manager permanently
ends the session and closes the data connection between the Session Manager client and
SSM Agent on the managed node. You can't resume a terminated session.

If there is no user activity in an open session for 20 minutes, the idle state
triggers a timeout. Session Manager doesn't call `TerminateSession`, but it does
close the underlying channel. You can't resume a session closed because of idle
timeout.

We recommend always explicitly terminating a session by using the
`terminate-session` command, when using the AWS CLI, or the
**Terminate** button when using the console.
(**Terminate** buttons are located on both the session window
and main Session Manager console page.) If you only close a browser or command window, the
session remains listed as **Active** in the console for 30 days.
When you don't explicitly terminate a session, or when a session times out, any
processes that were running on the managed node at the time will continue to
run.

###### Topics

- [Ending a session (console)](#stop-sys-console "#stop-sys-console")
- [Ending a session (AWS CLI)](#stop-cli "#stop-cli")

## Ending a session (console)

You can use the AWS Systems Manager console to end a session in your account.

###### To end a session (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Session Manager**.
3. For **Sessions**, choose the option button to the
   left of the session you want to end.
4. Choose **Terminate**.

## Ending a session (AWS CLI)

To end a session using the AWS CLI, run the following command. Replace
`session-id` with your own information.

```
aws ssm terminate-session \
    --session-id `session-id`
```

For more information about the **terminate-session** command,
see [terminate-session](../../../cli/latest/reference/ssm/terminate-session.md "../../../cli/latest/reference/ssm/terminate-session.md") in the AWS Systems Manager section of the AWS CLI Command Reference.
