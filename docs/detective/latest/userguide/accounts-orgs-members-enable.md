# Enabling organization accounts as Detective member

accounts

If you do not automatically enable new organization accounts, then you can enable those
accounts manually. You must also manually enable accounts that you disassociated.

## Determining whether an account can be

enabled

You cannot enable an organization account as a member account if the organization behavior
graph already has the maximum 1,200 enabled accounts. In this case, the organization account
status remains **Not a member**. The account does not contribute data to the
behavior graph.

As soon as the member account can be enabled, Detective automatically changes the member
account status to **Enabled**. For example, the member account status changes
to **Enabled** if the administrator account removes other member
accounts to make space for an account.

Console
From the **Account management** page, you can enable organization accounts
as member accounts.

###### To enable organization accounts as member accounts

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, choose **Account management**.
3. To view the list of accounts that are not currently enabled, choose **Not
   enabled**.
4. You can either select specific organization accounts, or enable all organization
   accounts.

To enable selected organization accounts:

    1. Select each organization account that you want to enable.
    2. Choose **Enable accounts**.To enable all organization accounts, choose **Enable all organization

accounts\*\*.

Detective API/AWS CLI
You can use the Detective API or the AWS Command Line Interface to enable organization accounts as member
accounts in the organization behavior graph. To get the ARN of your behavior graph to use in the
request, use the [`ListGraphs`](../APIReference/API_ListGraphs.md "../APIReference/API_ListGraphs.md")
operation.

###### To enable organization accounts as member accounts

- **Detective API:** Use the [`CreateMembers`](../APIReference/API_CreateMembers.md "../APIReference/API_CreateMembers.md")
  operation. You must provide the graph ARN.

For each account, specify the account identifier. Organization accounts in the
organization behavior graph do not receive an invitation. You do not need to provide an email
address or other invitation information.

- **AWS CLI:** At the command line, run the [`create-members`](../../../cli/latest/reference/detective/create-members.md "../../../cli/latest/reference/detective/create-members.md") command.

```
aws detective create-members --accounts AccountId=`<AWS account ID>` --graph-arn `<behavior graph ARN>`
```

**Example**

```
aws detective create-members --accounts AccountId=444455556666 AccountId=123456789012 --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234
```
