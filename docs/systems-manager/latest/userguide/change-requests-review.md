AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Reviewing and approving or rejecting

change requests

###### Change Manager availability change

AWS Systems Manager Change Manager will no longer be open to new customers
starting November 7, 2025. If you would like to use Change Manager, sign up prior to that
date. Existing customers can continue to use the service as normal. For more
information, see [AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

If you're specified as a reviewer for a change request in Change Manager, a tool in
AWS Systems Manager, you're notified through an Amazon Simple Notification Service (Amazon SNS) topic when a new
change request is awaiting your review.

###### Note

This functionality depends on whether an Amazon SNS was specified in the
change template for sending review notifications. For information, see
[Configuring Amazon SNS topics for Change Manager
notifications](change-manager-sns-setup.md "change-manager-sns-setup.md").

To review the change request, you can follow the link in your notification,
or sign in to the AWS Management Console directly and follow the steps in this
procedure.

###### Note

If an Amazon SNS topic is assigned for reviewers in a change template,
notifications are sent to the topic's subscribers when the change request
changes status.

For more information about approvals for change requests, see [About change request
approvals](change-requests-create.md#cm-approvals-requests "change-requests-create.md#cm-approvals-requests").

## Reviewing and approving or

rejecting change requests (console)

The following procedures describe how to use the Systems Manager console to review
and approve or reject change requests.

###### To review and approve or reject a single change request

1. Open the link in the email notification you received and sign in
   to the AWS Management Console, which directs you to the change request for your
   review.
2. In the summary page, review the proposed content of the
   change request.

To approve the change request, choose
**Approve**. In the dialog box, provide any
comments you want to add for this approval, and then choose
**Approve**. The runbook workflow represented
by this request starts to run either when scheduled, or as soon as
changes aren't blocked by any restrictions.

-or-

To reject the change request, choose **Reject**.
In the dialog box, provide any comments you want to add for this
rejection, and then choose **Reject**.

###### To review and approve or reject change requests in bulk

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Change Manager**.
3. Choose the **Approvals** tab.
4. (Optional) Review the details of requests pending your approval by
   choosing the name of each request, and then return to the
   **Approvals** tab.
5. Select the check box of each change request that you want to
   approve.

-or-

Select the check box of each change request that you want to
reject. 6. In the dialog box, provide any comments you want to add for this
approval or rejection. 7. Depending on whether you're approving or rejecting the selected
change requests, choose **Approve** or
**Reject**.

## Reviewing and

approving or rejecting a change request (command line)

The following procedure describes how to use the AWS Command Line Interface (AWS CLI) (on
Linux, macOS, or Windows Server) to review and approve or reject a
change request.

###### To review and approve or reject a change request

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Create a JSON file on your local machine that specifies the
parameters for your AWS CLI call.

```
{
  "OpsItemFilters":
  [
    {
      "Key": "OpsItemType",
      "Values": ["/aws/changerequest"],
      "Operator": "Equal"
    }
  ],
  "MaxResults": `number`
}
```

You can filter the results for a specific approver by specifying
the approver's Amazon Resource Name (ARN) in the JSON file. Here is
an example.

```
{
  "OpsItemFilters":
  [
    {
      "Key": "OpsItemType",
      "Values": ["/aws/changerequest"],
      "Operator": "Equal"
    },
    {
      "Key": "ChangeRequestByApproverArn",
      "Values": ["arn:aws:iam::`account-id`:user/`user-name`"],
      "Operator": "Equal"
    }
  ],
  "MaxResults": `number`
}
```

3. Run the following command to view the maximum number of
   change requests you specified in the JSON file.

Linux & macOS

```
aws ssm describe-ops-items \
--cli-input-json file://`filename`.json
```

Windows

```
aws ssm describe-ops-items ^
--cli-input-json file://`filename`.json
```

4. Run the following command to approve or reject a
   change request.

Linux & macOS

```
aws ssm send-automation-signal \
    --automation-execution-id `ID` \
    --signal-type `Approve_or_Reject` \
    --payload Comment="`message`"

```

Windows

```
aws ssm send-automation-signal ^
--automation-execution-id `ID` ^
    --signal-type `Approve_or_Reject` ^
    --payload Comment="`message`"

```

If an Amazon SNS topic has been specified in the change template you
chose for the request, notifications are sent when the request is
rejected or approved. If you don't receive notifications for the
request, you can return to Change Manager to check the status of your
request. For information about other options when using this
command, see [send-automation-signal](../../../cli/latest/reference/ssm/send-automation-signal.md "../../../cli/latest/reference/ssm/send-automation-signal.md") in the AWS Systems Manager
section of the _AWS CLI Command Reference_.
