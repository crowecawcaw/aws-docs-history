

# Creating an account alias
<a name="account-alias-create"></a>

To perform the following steps, you must have at least the following IAM permissions:
+ `iam:ListAccountAliases`
+ `iam:CreateAccountAlias`

## To create an AWS account alias
<a name="console-account-alias-section-1"></a>

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Dashboard**.

1. In the **AWS Account** section, next to **Account Alias**, choose **Create**. If an alias already exists, then choose **Edit**.

1. In the dialog box, enter the name you want to use for your alias, then choose **Save changes**.

------
#### [ AWS CLI ]

Run the following command:
+ `[aws iam create-account-alias](https://docs.aws.amazon.com/cli/latest/reference/iam/create-account-alias.html)`

------
#### [ API ]

To create an alias for your AWS Management Console sign-in page URL, call the following operation:
+ `[CreateAccountAlias](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccountAlias.html)` 

------