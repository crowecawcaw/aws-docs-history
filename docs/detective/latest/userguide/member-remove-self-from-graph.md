# Removing your account from a behavior

graph

After you accept an invitation, you can remove your account from a behavior graph at any
time. When you remove your account from a behavior graph, Amazon Detective stops ingesting data from
your account into the behavior graph. Existing data remains in the behavior graph.

Only invited accounts can remove their account from a behavior graph. Organization
accounts cannot remove their account from the organization behavior graph.

## Removing your account from a behavior graph

(Console)

You can use the AWS Management Console to remove your account from a behavior graph.

###### To remove your account from a behavior graph (console)

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, choose **Account management**.
3. Under **My administrator accounts**, for the behavior graph you
   want to resign from, choose **Resign**.

## Removing your account from a behavior graph (Detective

API, AWS CLI)

You can use the Detective API or the AWS Command Line Interface to remove your account from a behavior
graph.

###### To remove your account from a behavior graph (Detective API, AWS CLI)

- **Detective API:** Use the [`DisassociateMembership`](../APIReference/API_DisassociateMembership.md "../APIReference/API_DisassociateMembership.md") operation. You must specify the graph
  ARN.
- **AWS CLI:** At the command line, run the [`disassociate-membership`](../../../cli/latest/reference/detective/disassociate-membership.md "../../../cli/latest/reference/detective/disassociate-membership.md") command.

```
aws detective disassociate-membership --graph-arn `<behavior graph ARN>`
```

Example:

```
aws detective disassociate-membership --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234
```
