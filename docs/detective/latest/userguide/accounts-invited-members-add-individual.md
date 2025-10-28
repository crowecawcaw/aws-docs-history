# Inviting individual accounts to a

behavior graph

You can manually specify the member accounts to invite to contribute their data to a
behavior graph.

Console

###### To manually select the member accounts to invite using the Detective console.

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective navigation pane, choose **Account management**.
3. Choose **Actions**. Then choose **Invite
   accounts**.
4. Under **Add accounts**, choose **Add individual
   accounts**.
5. To add a member account to the invitation list, perform the following steps.
   1. Choose **Add account**.
   2. For **AWS Account ID**, enter the AWS account ID.
   3. For **Email address**, enter the root user email address for the
      account.

6. To remove an account from the list, choose **Remove** for that
   account.
7. Under **Personalize invitation email**, add customized content to
   include in the invitation email.

For example, you can use this area to provide contact information. Or use it to
remind the member account that they need to attach the required IAM policy to their
user or role before they can accept the invitation. 8. **Member account IAM policy** contains the text of the required
IAM policy for member accounts. The email invitation includes this policy text. To
copy the policy text, choose **Copy**. 9. Choose **Invite**.

Detective API/AWS CLI
You can use the Detective API or the AWS Command Line Interface to invite member accounts to contribute their
data to a behavior graph. To get the ARN of your behavior graph to use in the request, use
the [`ListGraphs`](../APIReference/API_ListGraphs.md "../APIReference/API_ListGraphs.md") operation.

###### To invite member accounts to a behavior graph (Detective API, AWS CLI)

- **Detective API:** Use the [`CreateMembers`](../APIReference/API_CreateMembers.md "../APIReference/API_CreateMembers.md") operation. You must provide the graph ARN. For
  each account, specify the account identifier and the root user email address.

To not send invitation emails to the member accounts, set
`DisableEmailNotification` to true. By default,
`DisableEmailNotification` is false .

If you do send invitation emails, you can optionally provide custom text to add to
the invitation email.

- **AWS CLI:** At the command line, run the
  `create-members` command.

```
aws detective create-members --accounts AccountId=`<AWS account ID>`,EmailAddress=`<root user email address>` --graph-arn `<behavior graph ARN>` --message "`<Custom message text>`"
```

**Example**

```
aws detective create-members --accounts AccountId=444455556666,EmailAddress=mmajor@example.com AccountId=123456789012,EmailAddress=jstiles@example.com --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234 --message "This is Paul Santos. I need to add your account to the data we use for security investigation in Amazon Detective. If you have any questions, contact me at psantos@example.com."
```

To indicate to not send invitation emails to the member accounts, include
`--disable-email-notification`.

```
aws detective create-members --accounts AccountId=`<AWS account ID>`,EmailAddress=`<root user email address>` --graph-arn `<behavior graph ARN>` --disable-email-notification
```

**Example**

```
aws detective create-members --accounts AccountId=444455556666,EmailAddress=mmajor@example.com AccountId=123456789012,EmailAddress=jstiles@example.com --graph-arn arn:aws:detective:us-east-1:111122223333:graph:123412341234 --disable-email-notification
```
