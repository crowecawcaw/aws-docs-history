# Disable Multi-party approval

When you sign in to your organization's management account, you can disable Multi-party approval by navigating to the Multi-party approval console and deleting the Multi-party approval identity source.

## Delete an identity source

To delete an identity source, complete the following steps.

**Minimum permissions**

To delete an identity source, you need permission to run the following action:

- `kms:Decrypt`
- `mpa:DeleteIdentitySource`
- `sso:DeleteApplication`
- `sso:DescribeApplication`
- `sso:DescribeInstance`
- `sso:ListInstances`
- `sso:PutApplicationAccessScope`
- `sso:PutApplicationAssignmentConfiguration`
- `sso:PutApplicationAuthenticationMethod`
- `sso:PutApplicationGrant`

If you are using the AWS Management Console, you also need permission to run the following actions:

- `kms:Decrypt`
- `organizations:DescribeOrganization`
- `organizations:ListDelegatedAdministrators`
- `sso:DescribeInstance`
- `sso:GetSharedSsoConfiguration`
- `sso:ListInstances`

AWS Management Console

###### To delete an identity source

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/").
2. On the left navigation, choose **Multi-party approval**.
3. On the **Multi-party approval** console, select an identity source and choose **Delete**.
4. On the **Delete identity source** dialog box, confirm the deletion and choose **Delete identity source**.

AWS CLI & AWS SDKs

###### To delete an identity source

You can use one of the following operations:

- AWS CLI: [list-identity-sources](../../../cli/latest/reference/mpa/list-identity-sources.md "../../../cli/latest/reference/mpa/list-identity-sources.md") and [delete-identity-source](../../../cli/latest/reference/mpa/delete-identity-source.md "../../../cli/latest/reference/mpa/delete-identity-source.md")
  1.  Run the following command to return a list of Amazon Resource Names (ARNs) for your identity sources:

  ```
  `$` `C:\>` **aws mpa list-identity-sources**
  ```

  2.  Run the following command to delete an identity source:

  ```
  `$` `C:\>` **aws mpa delete-identity-source \
   --identity-source-arn arn:aws:mpa:`region`:`123456789012`:identity-sources/IamIdentityCenter**
  ```

- AWS SDKs: [ListIdentitySources](../../../organizations/latest/APIReference/API_ListIdentitySources.md "../../../organizations/latest/APIReference/API_ListIdentitySources.md") and [DeleteIdentitySource](../../../organizations/latest/APIReference/API_DeleteIdentitySource.md "../../../organizations/latest/APIReference/API_DeleteIdentitySource.md")

###### What to do next

You can re-enable Multi-party approval at any time. For more information, see [Setting up Multi-party approval](setting-up.md "setting-up.md").

## Considerations

**Identity sources cannot be deleted when there are dependent approvers**

You cannot delete a Multi-party approval identity source when the identity source is managing the user authentication for approvers who are currently in approval teams.

To delete an identity source, you must first delete all teams associated with identity source. For more information, see [Delete team](delete-team.md "delete-team.md").

**Deleted IAM Identity Center instance**

If you deleted the IAM Identity Center instance connected to your identity source, you can still delete the Multi-party approval identity source. However, if you have active approval teams when the IAM Identity Center instance is deleted, these teams become non-functional. Approvers can no longer access the Multi-party approval portal to vote on sessions. To restore functionality, create a new IAM Identity Center instance with users and connect to a new identity source before you follow the approval team recovery process.

For steps to recover approval teams that are in an error state, see [Troubleshooting](troubleshooting.md "troubleshooting.md").
