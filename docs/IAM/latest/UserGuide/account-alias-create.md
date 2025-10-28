# Creating an account alias

To perform the following steps, you must have at least the following IAM permissions:

- `iam:ListAccountAliases`
- `iam:CreateAccountAlias`

## To create an AWS account alias

Console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose
   **Dashboard**.
3. In the **AWS Account** section, next to
   **Account Alias**, choose
   **Create**. If an alias already exists,
   then choose **Edit**.
4. In the dialog box, enter the name you want to use for your
   alias, then choose **Save changes**.

AWS CLI
Run the following command:

- `aws
iam create-account-alias`

API
To create an alias for your AWS Management Console
sign-in page URL, call the following operation:

- `CreateAccountAlias`
