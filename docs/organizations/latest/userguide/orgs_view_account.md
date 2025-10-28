# View details of an account in AWS Organizations

When you sign in to the organization's management account in the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"), you
can view details about your member accounts.

###### Minimum permissions

To view the details of an AWS account, you must have the following
permissions:

- `organizations:DescribeAccount`
- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:ListAccounts` – required only when using the Organizations console

AWS Management Console

###### To view details of an AWS account

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Navigate to the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page and choose the name of the name
   of the account (not the radio button) that you want to examine. If
   the account that you want is a child of an OU, you might have to
   choose the triangle icon
   ![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
   next to an OU to expand it and see its children.
   Repeat until you find the account.

The **Account details** box shows the information
about the account.

AWS CLI & AWS SDKs

###### To view details of an AWS account

You can use the following commands to view details of an
account:

- AWS CLI:

      + [list-accounts](../../../cli/latest/reference/organizations/list-accounts.md "../../../cli/latest/reference/organizations/list-accounts.md") – lists
       the details of *all*
       accounts in the organization
      + [describe-account](../../../cli/latest/reference/organizations/describe-account.md "../../../cli/latest/reference/organizations/describe-account.md") –
       lists the details of only the specified account

  Both commands return the same details for each account included in
  the response.

The following example shows how to retrieve the details about a
specified account.

```
`$` **aws organizations describe-account --account-id 123456789012**`{
 "Account": {
 "Id": "123456789012",
 "Arn": "arn:aws:organizations::123456789012:account/o-aa111bb222/123456789012",
 "Email": "admin@example.com",
 "Name": "Example.com Organization's Management Account",
 "Status": "ACTIVE",
 "JoinedMethod": "INVITED",
 "JoinedTimestamp": "2020-11-20T09:04:20.346000-08:00"
 }
}`
```

- AWS SDKs:
  - [ListAccounts](../APIReference/API_ListAccounts.md "../APIReference/API_ListAccounts.md")
  - [DescribeAccount](../APIReference/PI_DescribeAccount.md "../APIReference/PI_DescribeAccount.md")
