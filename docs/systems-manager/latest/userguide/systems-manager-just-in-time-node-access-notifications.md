AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Configure

notifications for just-in-time access requests

You can configure Systems Manager to send notifications when a user creates a just-in-time
node access request to the email addresses, or chat client, for approvers and the
requester. The notification contains the reason for the access request provided by
the requester, the AWS account, AWS Region, status of the request, and ID of the
target node. Currently, Systems Manager supports Slack and Microsoft Teams clients through
integration with Amazon Q Developer in chat applications. When using notifications through chat clients, access
request approvers can interact directly with access requests. This eliminates the
need to log in to the console to take action on access requests.

###### Before you begin

Before you configure a chat client for just-in-time node access notifications,
note the following requirement:

- If you're using IAM roles to manage user identities in your account, you
  must manually associate the email addresses of the approvers or requesters
  you want to send notifications to with the associated role. Otherwise the
  intended recipients can't be notified by email.
  The following procedures describe how to configure notifications for just-in-time
  node access requests.

###### To configure a chat client for just-in-time node access notifications

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Settings** in the navigation pane.
3. Select the **Just-in-time node access** tab.
4. In the **Chat** section, select **Configure new
   client**.
5. In the **Select client type** dropdown, choose the type
   of chat client you want to configure and select
   **Next**.
6. You're prompted to allow Amazon Q Developer in chat applications to access your chat client. Select
   **Allow**.
7. In the **Configure channel** section, enter the
   information for your chat client channel and select the types of
   notifications you want to receive.
8. If you're configuring Slack notifications, invite "@Amazon Q" to every
   Slack channel that notifications are being configured in.
9. Select **Configure channel**.

###### Note

To allow approving/rejecting access requests directly from a Slack channel,
make sure the IAM role that is configured with the Slack channel has
`ssm:SendAutomationSignal` permissions and has a trust policy
that includes chatbot:

```
{
            "Effect": "Allow",
            "Principal": {
                "Service": "chatbot.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
}
```

###### To configure email notifications for just-in-time node access

notifications

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Settings** in the navigation pane.
3. Select the **Just-in-time node access** tab.
4. In the **Email** section, select
   **Edit**.
5. Select **Add emails**, choose the **IAM
   role** you want to manually associate email addresses
   with.
6. Enter an email address in the **Email address** field.
   Whenever an access request is created that requires approval from the IAM
   role you specified, the email addresses you associate with the role are
   notified.
7. Select **Add email address**.
