# Disassociating Security Hub CSPM member accounts from your

organization

To stop receiving and viewing findings from an AWS Security Hub CSPM member account, you can
disassociate the member account from your organization.

###### Note

If you use [central
configuration](central-configuration-intro.md "central-configuration-intro.md"), disassociation works differently. You can create a configuration policy that disables Security Hub CSPM in one or more centrally managed member accounts.
After that, these accounts are still part of the organization, but won't generate Security Hub CSPM findings. If you use central configuration but
also have manually-invited member accounts, you can disassociate one or more manually-invited accounts.

Member accounts that are managed using AWS Organizations can't disassociate their accounts from the administrator account. Only the
administrator account can disassociate a member account.

Disassociating a member account does not close the account. Instead, it removes the member account from the organization.
The disassociated member account becomes a standalone AWS account that is no longer managed by the Security Hub CSPM integration with AWS Organizations.

Choose your preferred method, and follow the steps to disassociate a member account from the organization.

Security Hub CSPM console

###### To disassociate a member account from the organization

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated administrator account. 2. In the navigation pane, under **Settings**, choose **Configuration**. 3. In the **Accounts** section, select the accounts that you want to
disassociate. If you use central configuration, you can select a manually-invited account to disassociate from the `Invitation accounts`
tab. This tab is visible only if you use central configuration. 4. Choose **Actions**, and then choose
**Disassociate account**.

Security Hub CSPM API
**To disassociate a member account from the organization**

Invoke the [`DisassociateMembers`](../../1.0/APIReference/API_DisassociateMembers.md "../../1.0/APIReference/API_DisassociateMembers.md") API from the delegated administrator account. You must
provide the AWS account IDs for the member accounts to disassociate. To
view a list of member accounts, invoke the [`ListMembers`](../../1.0/APIReference/API_ListMembers.md "../../1.0/APIReference/API_ListMembers.md") API.

AWS CLI
**To disassociate a member account from the organization**

Run the [>`disassociate-members`](../../../cli/latest/reference/securityhub/disassociate-members.md "../../../cli/latest/reference/securityhub/disassociate-members.md") command from the delegated administrator account. You must
provide the AWS account IDs for the member accounts to disassociate. To
view a list of member accounts, run the [>`list-members`](../../../cli/latest/reference/securityhub/list-members.md "../../../cli/latest/reference/securityhub/list-members.md") command.

```
aws securityhub disassociate-members --account-ids "`<accountIds>`"
```

**Example**

```
aws securityhub disassociate-members --account-ids "123456789111" "123456789222"
```

You can also use the AWS Organizations console, AWS CLI, or AWS SDKs to disassociate a member account from your organization. For more information, see
[Removing a member account from your organization](../../../organizations/latest/userguide/orgs_manage_accounts_remove.md "../../../organizations/latest/userguide/orgs_manage_accounts_remove.md") in the _AWS Organizations User Guide_.
