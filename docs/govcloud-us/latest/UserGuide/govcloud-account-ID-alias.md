

# Your AWS GovCloud (US) account ID and its alias
<a name="govcloud-account-ID-alias"></a>

To sign in to an AWS GovCloud (US) account as an IAM user, you must have an account alias or an account ID for the AWS GovCloud (US) account. If you are signed in to the AWS Management Console or have configured the AWS CLI or an AWS SDK with your account credentials, you can find the account alias or account ID for the AWS GovCloud (US) account. If you cannot sign in, ask your administrator for the information that you need to sign in.

**Note**  
Account aliases are not secrets, and they will appear in your public-facing sign-in page URL. Do not include any sensitive information in your account alias.

## Finding your AWS GovCloud (US) account ID
<a name="finding-govlcoud-id"></a>

You can find the account ID for your AWS GovCloud (US) account using the following methods.

**Note**  
 Support can’t help you recover this information.

### Finding your AWS GovCloud (US) account ID using the AWS Management Console for AWS GovCloud (US)
<a name="find-govcloud-id-govcloud-console"></a>

You can retrieve your AWS GovCloud (US) account ID by [Signing in to AWS GovCloud (US)](signing-into-govcloud.md). In the navigation bar, choose **Support**, and then **Support Center**. Your currently signed-in 12-digit account number (ID) appears in the **Support Center** navigation pane.

### Finding your AWS GovCloud (US) account ID using the standard AWS Management Console
<a name="find-govcloud-id-console"></a>

You can retrieve your AWS GovCloud (US) account ID by signing in to [the standard AWS Management Console as the root](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) of the [associated standard AWS account](getting-started-standard-account-linking.md). In the navigation bar, choose your account name on the top right of the window, and then choose **Account**. On the **Account Settings** page, your 12-digit AWS GovCloud (US) account ID appears under **Linked AWS GovCloud (US) account**.

### Finding your AWS GovCloud (US) account ID using the AWS CLI
<a name="find-govcloud-id-cli"></a>

With AWS GovCloud (US) account credentials use the following command to view your user ID, account ID, and your user ARN:
+  [aws sts get-caller-identity](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-create-account-status.html) 

If your AWS GovCloud (US) account was created using the [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) API, use the following command view your AWS GovCloud (US) account ID and its associated standard AWS account ID. This call must be made from the standard [AWS Organizations management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) or by a member account that is a delegated administrator for an AWS service.
+  [aws organizations list-create-account-status](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-create-account-status.html) 

### Finding your AWS GovCloud (US) account ID using the API
<a name="find-govcloud-id-api"></a>

With AWS GovCloud (US) account credentials, use the following API to view your user ID, account ID, and your user ARN:
+  [GetCallerIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetCallerIdentity.html) 

If your AWS GovCloud (US) account was created using the [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) API, use the following command view your AWS GovCloud (US) account ID and its associated standard AWS account ID. This call must be made from the standard [AWS Organizations management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) or by a member account that is a delegated administrator for an AWS service.
+  [ListCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListCreateAccountStatus.html) 

## Finding your associated standard AWS account ID
<a name="find-standard-id"></a>

**Note**  
 Support can’t help you recover this information.

### Finding your associated standard AWS account ID using the AWS Management Console for AWS GovCloud (US)
<a name="find-standard-id-govcloud-console"></a>

You can retrieve your associated standard AWS account ID by signing into your AWS GovCloud (US) account.

In the navigation bar, choose **Support**, and then **Support Center**. In the **Support Center** navigation pane, choose **Your support cases** and open the most recently created support case by choosing its **Case ID** or **Subject**. In the **Case details**, look for the email address listed in the **Opened by** field. If your account email address has not changed since opening the case, this will be your account email address. [Sign in as the root](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) of your standard AWS account using this email and follow [Finding your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html#FindingYourAWSId) in the * AWS Identity and Access Management User Guide*guide.

**Note**  
If you have never opened a support case or believe the email address has since changed, [create a support case for account and billing](https://docs.aws.amazon.com/awssupport/latest/user/case-example.html) and [resolve it](https://docs.aws.amazon.com/awssupport/latest/user/monitoring-your-case.html#resolve-a-support-case) immediately. Review the case’s **Open by** field to see the associated account email.

### Finding your associated standard AWS account ID using the AWS CLI
<a name="find-standard-id-cli"></a>

If your AWS GovCloud (US) account was created using [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) API, use the following command view your AWS GovCloud (US) account ID and its associated standard AWS account ID. This call must be made from the standard [AWS Organizations management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) or by a member account that is a delegated administrator for an AWS service.
+  [aws organizations list-create-account-status](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-create-account-status.html) 

### Finding your associated standard AWS account ID using the API
<a name="find-standard-id-api"></a>

If your AWS GovCloud (US) account was created using the [CreateGovCloudAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateGovCloudAccount.html) API, use the following command view your AWS GovCloud (US) account ID and its associated standard AWS account ID. This call must be made from the standard [AWS Organizations management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) or by a member account that is a delegated administrator for an AWS service.
+  [ListCreateAccountStatus](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListCreateAccountStatus.html) 

## About account aliases
<a name="about-account-alias"></a>

If you want the URL for your sign-in page to contain your company name (or other friendly identifier) instead of your AWS GovCloud (US) account ID, you can create an account alias. This section provides information about AWS account aliases and lists the API operations that you use to create an alias.

Your sign-in page URL has the following format, by default.

```
https://<Your_Account_ID>.signin.aws.amazon.com/console/
```

If you create an AWS account alias for your AWS GovCloud (US) ID, your sign-in page URL looks like the following example.

```
https://<Your_Account_Alias>.signin.aws.amazon.com/console/
```

The original URL containing your AWS GovCloud (US) ID remains active and can be used after you create your AWS account alias.

**Tip**  
To create a bookmark for your account sign-in page in your web browser, you should manually type the sign-in URL in the bookmark entry. Don’t use your web browser’s "bookmark this page" feature.

## Creating, deleting, and listing an AWS account alias
<a name="create-account-alias"></a>

You can use the AWS Management Console, the IAM API, or the command line interface to create or delete your AWS GovCloud (US) account alias.

**Considerations**
+ Your AWS GovCloud (US) account can have only one alias. If you create a new alias for your AWS GovCloud (US) account, the new alias overwrites the previous alias, and the URL containing the previous alias stops working.
+ The account alias must be unique across all Amazon Web Services products. It must contain only digits, lowercase letters, and hyphens. For more information on limitations on AWS account entities, see [IAM and AWS STS quotas](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html).
+ Changes to your AWS GovCloud (US) account alias or the associated standard AWS account alias will not overwrite the other alias. They can each be customized without interference of the other. See [Creating, deleting, and listing an AWS account alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html#CreateAccountAlias) in the * AWS Identity and Access Management User Guide*to learn more about customizing the associated standard AWS account alias.

### Creating, editing, and deleting aliases (console)
<a name="create-alias-console"></a>

You can create, edit, and delete an account alias from the AWS Management Console for AWS GovCloud (US).

**To create, edit, or remove an account alias (console)**

1. Sign in to the AWS Management Console for AWS GovCloud (US) and open the IAM console at https://console.amazonaws-us-gov.com/iam/.

1. In the navigation pane, choose **Dashboard**.

1. In the ** AWS account ** section, find **Account Alias**, and choose **Create**. If an alias already exists, then choose **Edit**.

1. Type the name you want to use for your alias, then choose **Save changes**.

1. To remove the alias, next to **Account Alias** choose **Delete**, and then choose **Delete**. The sign-in URL reverts to using your AWS account ID.

### Creating, deleting, and listing aliases (AWS CLI)
<a name="create-alias-cli"></a>

**Note**  
You must use AWS GovCloud (US) credentials.

To create an alias for your AWS Management Console for AWS GovCloud (US) sign-in page URL, run the following command:
+  [aws iam create-account-alias](https://docs.aws.amazon.com/cli/latest/reference/iam/create-account-alias.html) 

To delete an AWS account ID alias, run the following command:
+  [aws iam delete-account-alias](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-account-alias.html) 

To display your AWS account ID alias, run the following command:
+  [aws iam list-account-aliases](https://docs.aws.amazon.com/cli/latest/reference/iam/list-account-aliases.html) 

### Creating, deleting, and listing aliases (AWS API)
<a name="create-alias-api"></a>

**Note**  
You must use AWS GovCloud (US) credentials.

To create an alias for your AWS Management Console for AWS GovCloud (US) sign-in page URL, call the following operation:
+  [aws CreateAccountAlias](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateAccountAlias.html) 

To delete an alias for your AWS Management Console for AWS GovCloud (US) sign-in page URL, call the following operation:
+  [aws DeleteAccountAlias](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccountAlias.html) 

To display your AWS account ID alias, call the following operation:
+  [aws ListAccountAliases](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAccountAliases.html) 