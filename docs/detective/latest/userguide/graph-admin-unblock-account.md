# Enabling a member account that is Not

enabled

After a member account accepts an invitation, Amazon Detective checks the number of member
accounts. The maximum number of member accounts for a behavior graph is 1,200. If your
behavior graph already contains 1,200 member accounts, then new accounts cannot be enabled. If
Detective cannot enable the member account, then it sets the member account status to **Not enabled**.

Member accounts that are **Not enabled** do not contribute
data to the behavior graph.

Detective automatically enables accounts as the behavior graph can accommodate them.

You can also try to enable member accounts manually that are **Not
enabled** member accounts. For example, you might remove existing member accounts
to reduce the data volume. Instead of waiting for the automatic process to enable accounts,
you can try to enable **Not enabled** member accounts.

Console
The member account list includes an option to enable selected member accounts that are
**Not enabled.**

###### To enable a member account that is Not enabled

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, choose **Account management**.
3. Under **My member accounts**, select the check box for each member
   account to enable.

You can only enable member accounts that have a status of **Not
enabled**. 4. Choose **Enable accounts**.

Detective determines whether the member account can be enabled. If the member account can be
enabled, the status changes to **Enabled**.

Detective API/CLI
You can use an API call or the AWS Command Line Interface to enable a single member account that is
**Not enabled**. To get the ARN of your behavior graph to use
in the request, use the [`ListGraphs`](../APIReference/API_ListGraphs.md "../APIReference/API_ListGraphs.md")
operation.

###### To enable a member account that is Not enabled

- **Detective API:** Use the [`StartMonitoringMember`](../APIReference/API_StartMonitoringMember.md "../APIReference/API_StartMonitoringMember.md") API operation. You must provide the
  behavior graph ARN. To identify the member account, use the AWS account
  identifier.
- **AWS CLI:** Run the [`start-monitoring-member`](../../../cli/latest/reference/detective/start-monitoring-member.md "../../../cli/latest/reference/detective/start-monitoring-member.md") command.

```
start-monitoring-member --graph-arn `<behavior graph ARN>` --account-id `<AWS account ID>`
```

For example:

```
start-monitoring-member --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234 --account-id 444455556666
```
