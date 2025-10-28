# Distribute License Manager entitlements

If you are a license administrator operating in the management account of your
organization with [all
features](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md") enabled, you can distribute entitlements to your organization from your
granted licenses by creating a grant. For more information about AWS Organizations, see [AWS Organizations
terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md").

You can specify the recipient of the grant as one of the following:

- An AWS account, which includes only the specified account.
- An organization root, which will include all accounts across your
  organization.
- An organizational unit (OU) (that is not nested), which includes all accounts in
  the specified OU and in nested OUs under the specified OU.

###### Note

You can create up to 2,000 grants per license.

You can use either the AWS License Manager console or the AWS CLI to distribute your
entitlements. You can specify the organization ID or the organization ARN when creating
a grant in the console, but the ARN format must be used with the AWS CLI. For example, the
ARNs will resemble the following:

**Organization ID ARN**

`arn:aws:organizations::`<account-id-of-management-account>`:organization/o-`<organization-id>``

**Organization OU ARN**

`arn:aws:organizations::`<account-id-of-management-account>`:ou/o-`<organization-id>`/ou-`<organizational-unit-id>``

Console

###### To create a grant (Console)

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Granted
   licenses**.
3. Choose a license ID to open the **License overview**
   page.
4. From the **Grants** section, choose **Create
   grant**.
5. On the **Grant details** panel, do the following:
   1. Enter a name for the grant to help you identify the purpose or
      recipient of the grant.
   2. Enter the AWS account ID, AWS Organizations OU ID or ARN, or AWS Organizations ID
      or ARN of the grant recipient.
   3. Choose **Create grant**.

6. On the **License overview** page, you'll see an entry
   for the grant in the **Grants** panel. The initial status
   of the grant is **Pending acceptance**. The status changes
   to **Active** when the recipient accepts the grant or
   **Rejected** when the recipient rejects the
   grant.

AWS CLI
You can use the AWS CLI to distribute an entitlement. You must use specify an
organization ID or OU in ARN format when using the AWS License Manager API.

###### To create and list your grants using the AWS CLI:

- [create-grant](../../../cli/latest/reference/license-manager/create-grant.md "../../../cli/latest/reference/license-manager/create-grant.md")
- [list-distributed-grants](../../../cli/latest/reference/license-manager/list-distributed-grants.md "../../../cli/latest/reference/license-manager/list-distributed-grants.md")

The grant details page displays the list of accounts that you have granted access to the
entitlement. After distributing a license to your organization, you can deactivate or
activate the licenses individually on each account.
