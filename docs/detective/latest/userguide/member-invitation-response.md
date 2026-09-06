

# Responding to a behavior graph invitation
<a name="member-invitation-response"></a>

After you accept an invitation, Detective checks the number of member accounts. The maximum number of member accounts for a behavior graph is 1,200. If your behavior graph already contains 1,200 member accounts, then new accounts cannot be enabled.

After you accept the invitation, Detective is enabled in your account. Detective checks whether your data volume is within the Detective quota. The volume of data flowing into a behavior graph must be less than the maximum allowed by Detective. If the current volume ingested is above the limit of 10 TB per day, you cannot add more accounts and Detective will disable further ingestion of data. The Detective console displays a notification to indicate that data volume is too large and the status remains **Not enabled**.

If you decline the invitation, then it is removed from your list of invitations, and Detective does not use your account data in the behavior graph.

## Responding to a behavior graph invitation (console)
<a name="member-invitation-response-console"></a>

You can use the AWS Management Console to respond to the email invitation, which includes a link to the Detective console. You can only respond to an invitation that has a status of **Invited**.

**To respond to a behavior graph invitation (console)**

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/).

1. In the Detective navigation pane, choose **Account management**.

1. Under **My administrator accounts**, to accept the invitation and begin contributing data to the behavior graph, choose **Accept invitation**.

   To decline the invitation and remove it from the list, choose **Decline**.

## Responding to a behavior graph invitation (Detective API, AWS CLI)
<a name="member-invitation-response-api"></a>

You can respond to behavior graph invitations from the Detective API or the AWS Command Line Interface.

**To accept a behavior graph invitation (Detective API, AWS CLI)**
+ **Detective API:** Use the [`AcceptInvitation`](https://docs.aws.amazon.com/detective/latest/APIReference/API_AcceptInvitation.html) operation. You must specify the graph ARN.
+ **AWS CLI:** At the command line, run the [`accept-invitation`](https://docs.aws.amazon.com/cli/latest/reference/detective/accept-invitation.html) command.

  ```
  aws detective accept-invitation --graph-arn {{<behavior graph ARN>}}
  ```

  Example:

  ```
  aws detective accept-invitation --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234
  ```

**To decline a behavior graph invitation (Detective API, AWS CLI)**
+ **Detective API:** Use the [`RejectInvitation`](https://docs.aws.amazon.com/detective/latest/APIReference/API_RejectInvitation.html) operation. You must specify the graph ARN.
+ **AWS CLI:** At the command line, run the [`reject-invitation`](https://docs.aws.amazon.com/cli/latest/reference/detective/reject-invitation.html) command.

  ```
  aws detective reject-invitation --graph-arn {{<behavior graph ARN>}}
  ```

  Example:

  ```
  aws detective reject-invitation --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234
  ```