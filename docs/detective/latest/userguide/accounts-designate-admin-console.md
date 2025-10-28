# Designating a Detective administrator

The organization management account can use the Detective console to designate the Detective
administrator account.

You do not need to enable Detective in order to manage the Detective administrator account. You can
manage the Detective administrator account from the **Enable Detective** page.

Enable Detective page (Console)
To designate a Detective administrator from the **Enable Detective** page, follow these steps.

1. Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. Choose **Get started**.
3. In the **Required permissions for administrator accounts** panel, grant
   necessary the permissions to the account you choose so that they can operate as a Detective
   administrator with full access to all actions in Detective. To operate as an administrator, We
   recommend attaching the `AmazonDetectiveFullAccess` policy to the principal.
4. Choose **Attach policy from IAM** to view the recommended policy directly
   in the IAM console.
5. Depending on whether you have permissions in the IAM console, proceed as follows:
   - If you have permissions to operate in the IAM console, attach the recommended policy
     to the principal you use for Detective.
   - If you don't have permissions to operate in the IAM console, copy the Amazon Resource
     Name (ARN) of the policy and provide it to your IAM administrator. They can then attach the
     policy on your behalf.

6. Under **Delegated administrator**, choose the Detective administrator
   account.

The available options depend on whether you have a delegated administrator account for
Detective in Organizations.

    * If you do not have a delegated administrator account for Detective in Organizations, then enter the
     account identifier of the account to designate it as the Detective administrator account.


    You might have an existing administrator account and behavior graph from the manual
     invitation process. If so, we recommend that you designate that account as the Detective
     administrator account.


    If you have a delegated administrator account in Organizations for Amazon GuardDuty, AWS Security Hub, or
     Amazon Macie, then Detective prompts you to select one of those accounts. You can also enter a
     different account.
    * If you do have a delegated administrator account for Detective in Organizations, then you are
     prompted to choose either that account or your account. We recommend that you choose the
     delegated administrator account in all Regions.

7. Choose **Delegate**.

If you have Detective enabled, or are a member account in an existing behavior graph, then you
can designate the Detective administrator account from the **General** page.

General page (Console)To designate a Detective administrator from the **General** page, follow these steps.

1.  Open the Amazon Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2.  In the Detective navigation pane, under **Settings**, choose
    **General**.
3.  In the **Managed policies** panel, you can learn more about all the
    managed policies Detective supports. You can grant necessary permissions to an account depending on
    the actions you want users to perform in Detective. To operate as an administrator, We recommend
    attaching the `AmazonDetectiveFullAccess` policy to the principal.
4.  Depending on whether you have permissions in the IAM console, proceed as follows:

        * If you have permissions to operate in the IAM console, attach the recommended policy
         to the principal you use for Detective.
        * If you don't have permissions to operate in the IAM console, copy the Amazon Resource
         Name (ARN) of the policy and provide it to your IAM administrator. They can then attach the
         policy on your behalf.

    The available options depend on whether you have a delegated administrator account for
    Detective in Organizations.

        * If you do not have a delegated administrator account for Detective in Organizations, then enter the
         account identifier of the account to designate it as the Detective administrator account.


        You might have an existing administrator account and behavior graph from the manual
         invitation process. If so, then we recommend that you designate that account as the Detective
         administrator account.


        If you have a delegated administrator account in Organizations for Amazon GuardDuty, AWS Security Hub, or
         Amazon Macie, then Detective prompts you to select one of those accounts. You can also enter a
         different account.
        * If you do have a delegated administrator account for Detective in Organizations, then you are
         prompted to choose either that account or your account. We recommend that you choose the
         delegated administrator account in all Regions.

5.  Choose **Delegate**.

Detective API, AWS CLITo designate the Detective administrator account, you can use an API call or the AWS Command Line Interface. You
must use the organization management account credentials.

If you already have a delegated administrator account for Detective in organizations, then you
must choose either that account or your account we recommend that you choose the delegated
administrator account.

###### To designate the Detective administrator account (Detective API, AWS CLI)

- **Detective API:** Use the [`EnableOrganizationAdminAccount`](../APIReference/API_EnableOrganizationAdminAccount.md "../APIReference/API_EnableOrganizationAdminAccount.md") operation. You must provide the AWS
  account identifier of the Detective administrator account. To obtain the account identifier, use
  the [`ListOrganizationAdminAccounts`](../APIReference/API_ListOrganizationAdminAccounts.md "../APIReference/API_ListOrganizationAdminAccounts.md") operation.
- **AWS CLI:** At the command line, run the [`enable-organization-admin-account`](../../../cli/latest/reference/detective/enable-organization-admin-account.md "../../../cli/latest/reference/detective/enable-organization-admin-account.md") command.

```
aws detective enable-organization-admin-account --account-id `<admin account ID>`
```

**Example**

```
aws detective enable-organization-admin-account --account-id 777788889999
```
