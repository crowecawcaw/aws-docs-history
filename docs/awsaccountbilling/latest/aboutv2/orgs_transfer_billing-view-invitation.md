# Viewing invitations

When you sign in to your organization's management account, you can view recent invitations you have sent or received.

## Status

The following are the statuses for invitations:

- **Awaiting response** (`REQUESTED`): Invitation awaiting a response from the recipient.
- **Invitation declined** (`DECLINED`): Invitation declined by the recipient.
- **Invitation canceled** (`CANCELED`): Invitation canceled by the sender.
- **Invitation expired** (`EXPIRED`): Invitation has expired.

![](images/transfer-billing-invitation-statuses.png)

_Figure 1: Invitation statues as displayed in the AWS Billing and Cost Management console._

## View an invitation

###### Terms and concepts

The following are terms and concepts used in the AWS Billing and Cost Management console:

- **Inbound billing**: Billing transfers that allow you to manage and pay for another organization’s consolidated bill.
- **Outbound billing**: Billing transfers that allow an account outside your organization to manage and pay your consolidated bill.

###### Minimum permissions

To view an invitation, you must have the following permissions

- `organizations:ListHandshakesForOrganization`
- `organizations:ListHandshakesForAccount`
- `organizations:DescribeHandshake`

To view an invitation, complete the following steps.

###### To view an invitation

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the left navigation in **Preferences and Settings**, choose **Billing transfers**.
3. ###### For inbound billings:
   1. On the **Billing transfers** page, select the **Inbound billing** tab.
   2. On the **Inbound billing** tab, select the invitation you want to view details for.
   3. Choose the **Actions** dropdown menu, and then chose **View details**.

4. ###### For outbound billings:
   1. On the **Billing transfers** page, select the **Outbound billing** tab.
   2. On the **Outbound billing** tab, you can view details for the invitation.

###### Invitations are deleted after 30 days

You can view invitations for 30 days before they are deleted. If you accept an invitation, details for that transfer are not deleted.

###### To view an invitation

You can use one of the following operations:

- AWS CLI: [list-handshakes-for-organization](../../../cli/latest/reference/organizations/list-handshakes-for-organization.md "../../../cli/latest/reference/organizations/list-handshakes-for-organization.md"), [list-handshakes-for-account](../../../cli/latest/reference/organizations/list-handshakes-for-account.md "../../../cli/latest/reference/organizations/list-handshakes-for-account.md"), and [describe-handshake](../../../cli/latest/reference/organizations/describe-handshake.md "../../../cli/latest/reference/organizations/describe-handshake.md")
  1.  **For invitations you have sent:**

  Run the following command find the [handshake](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#invitations-handshakes "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#invitations-handshakes") ID.

  ```
  `$` `C:\>` **aws organizations list-handshakes-for-organization**
  ```

  **For invitations you have received:**

  Run the following command find the [handshake](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#invitations-handshakes "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#invitations-handshakes") ID.

  ```
  `$` `C:\>` **aws organizations list-handshakes-for-account**
  ```

  2.  From the response, note the handshake ID for the invitation you want to view details for.
  3.  Run the following command to view details for the invitation:

  ```
  `$` `C:\>` **aws organizations describe-handshake \
   --id `examplehandshakeid`**
  ```

- AWS SDKs: [list-handshakes-for-organization](../../../cli/latest/reference/organizations/API_ListHandshakesForOrganization.md "../../../cli/latest/reference/organizations/API_ListHandshakesForOrganization.md"), [list-handshakes-for-account](../../../cli/latest/reference/organizations/API_ListHandshakesForAccount.md "../../../cli/latest/reference/organizations/API_ListHandshakesForAccount.md"), and [describe-handshake](../../../organizations/latest/APIReference/API_DescribeHandshake.md "../../../organizations/latest/APIReference/API_DescribeHandshake.md")

###### Invitations are deleted after 30 days

You can view invitations for 30 days before they are deleted. If you accept an invitation, details for that transfer are not deleted.
