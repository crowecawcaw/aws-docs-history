

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# End a session
<a name="session-manager-working-with-sessions-end"></a>

You can end a session that you started in your account using the AWS Systems Manager console or the AWS Command Line Interface (AWS CLI). When you choose the **Terminate session** button for a session in the console or call the [TerminateSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_TerminateSession.html) API action by using the AWS CLI, Session Manager permanently ends the session and closes the data connection between the Session Manager client and SSM Agent on the managed node. You can't resume a terminated session.

If there is no user activity in an open session for 20 minutes, the idle state triggers a timeout. Session Manager doesn't call `TerminateSession`, but it does close the underlying channel. You can't resume a session closed because of idle timeout.

We recommend always explicitly terminating a session by using the `terminate-session` command, when using the AWS CLI, or the **Terminate session** button when using the console. (**Terminate session** buttons are located on both the session window and main Session Manager console page.) If you only close a browser or command window, the session remains listed as **Active** in the console for 30 days. When you don't explicitly terminate a session, or when a session times out, any processes that were running on the managed node at the time will continue to run.

**Topics**
+ [Ending a session (console)](#stop-sys-console)
+ [Ending a session (AWS CLI)](#stop-cli)

## Ending a session (console)
<a name="stop-sys-console"></a>

You can use the AWS Systems Manager console to end a session in your account.

**To end a session (console)**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Session Manager**.

1. For **Sessions**, choose the option button to the left of the session you want to end.

1. Choose **Terminate session**.

## Ending a session (AWS CLI)
<a name="stop-cli"></a>

To end a session using the AWS CLI, run the following command. Replace {{session-id}} with your own information.

```
aws ssm terminate-session \
    --session-id {{session-id}}
```

For more information about the **terminate-session** command, see [terminate-session](https://docs.aws.amazon.com/cli/latest/reference/ssm/terminate-session.html) in the AWS Systems Manager section of the AWS CLI Command Reference.