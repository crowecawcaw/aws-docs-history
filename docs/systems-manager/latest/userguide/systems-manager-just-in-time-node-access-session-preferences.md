AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Update just-in-time node access session preferences

With just-in-time node access, you can specify general session and logging
preferences in each AWS account and AWS Region in your organization.
Alternatively, you can use AWS CloudFormation StackSets to create a session preferences document
in multiple accounts and Regions to help you have consistent session preferences.
For information about the schema for session preferences documents, see [Session document schema](session-manager-schema.md "session-manager-schema.md").

For logging purposes, we recommend using the streaming option with Amazon CloudWatch Logs. This
feature allows you to send a continual stream of session data logs to CloudWatch Logs.
Essential details, such as the commands a user has run in a session, the ID of the
user who ran the commands, and timestamps for when the session data is streamed to
CloudWatch Logs, are included when streaming session data. When streaming session data, the
logs are JSON-formatted to help you integrate with your existing logging
solutions.

Systems Manager doesn't automatically terminate just-in-time node access sessions. As a best
practice, specify values for the _maximum session duration_ and
_idle session timeout_ settings. Using these settings helps
you to prevent a user from remaining connected to a node longer than the window of
time approved in an access request. The following procedure describes how to update
session preferences for just-in-time node access.

###### Important

You must tag the AWS KMS keys used for Session Manager encryption and RDP recording in
just-in-time node access with the tag key
`SystemsManagerJustInTimeNodeAccessManaged` and tag value
`true`.

For information about tagging KMS keys, see [Tags in AWS KMS](../../../kms/latest/developerguide/tagging-keys.md "../../../kms/latest/developerguide/tagging-keys.md") in
the _AWS Key Management Service Developer Guide_.

###### To update session preferences

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Settings** in the navigation pane.
3. Select the **Just-in-time node access** tab.
4. In the **Session preferences** section, select
   **Edit**.
5. Update your general and logging preferences as needed and select
   **Save**.
