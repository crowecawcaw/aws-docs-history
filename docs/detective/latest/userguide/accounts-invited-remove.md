# Removing member accounts from a behavior

graph

The administrator account can remove invited member accounts from a behavior graph at any
time.

Detective automatically removes member accounts that are terminated in AWS, except in the
AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions.

When an invited member account is removed from a behavior graph, the following
occurs.

- The member account is removed from **My member accounts**.
- Amazon Detective stops ingesting data from the removed account.
  Detective does not remove any existing data from the behavior graph, which aggregates data
  across member accounts.

Console
You can use the AWS Management Console to remove invited member accounts from your behavior
graph.

###### To remove member accounts (console)

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, choose **Account
   management**.
3. In the account list, select the check box for each member account to remove.

You cannot remove your own account from the list. 4. Choose **Actions**. Then choose **Disable accounts**.

Detective API/CLI
You can use the Detective API or the AWS Command Line Interface to remove invited member accounts from your
behavior graph. To get the ARN of your behavior graph to use in the request, use the [`ListGraphs`](../APIReference/API_ListGraphs.md "../APIReference/API_ListGraphs.md") operation.

###### To remove invited member accounts from your behavior graph (Detective API, AWS CLI)

- **Detective API:** Use the [`DeleteMembers`](../APIReference/API_DeleteMembers.md "../APIReference/API_DeleteMembers.md") operation. Specify the graph ARN and the list of
  account identifiers for the member accounts to remove.
- **AWS CLI:** At the command line, run the [`delete-members`](../../../cli/latest/reference/detective/delete-members.md "../../../cli/latest/reference/detective/delete-members.md") command.

```
aws detective delete-members --account-ids `<account ID list>` --graph-arn `<behavior graph ARN>`
```

Example:

```
aws detective delete-members --account-ids 444455556666 123456789012 --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234
```

Python script
Detective provides an open-source script in GitHub. You can use this script to remove a
specified list of member accounts from an administrator account's behavior graphs across a
specified list of Regions.

For information on how to configure and use the GitHub scripts, see [Using Detective Python scripts to manage accounts](detective-github-scripts.md "detective-github-scripts.md").
