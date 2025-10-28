# Deleting an account alias

To perform the following steps, you must have at least the following IAM permissions:

- `iam:ListAccountAliases`
- `iam:DeleteAccountAlias`

## To delete an account alias

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose
   **Dashboard**.
3. In the **AWS Account** section, next to
   **Account Alias**, choose
   **Delete**.

AWS CLI
To delete an AWS account ID
alias, run the following command:

- `aws
iam delete-account-alias`

To confirm that the account alias is
deleted, attempt to display your AWS account ID
alias, by running the following command:

- `aws
iam list-account-aliases`

API
To delete an AWS account ID
alias, call the following operation:

- `DeleteAccountAlias`

To confirm that the account alias is deleted
attempt to display your AWS account ID alias, by
calling the following operation:

- `ListAccountAliases`

###### Note

After deleting your account alias, the only sign-in URL for your account
is based off your account ID. Any attempts to connect to the alias URL will
fail and are not redirected.
