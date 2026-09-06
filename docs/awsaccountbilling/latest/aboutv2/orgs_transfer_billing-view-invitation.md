

# Viewing invitations
<a name="orgs_transfer_billing-view-invitation"></a>

When you sign in to your organization's management account, you can view recent invitations you have sent or received.

## Status
<a name="orgs_transfer_billing-view-invitation-status"></a>

The following are the statuses for invitations:
+ **Awaiting response** (`REQUESTED`): Invitation awaiting a response from the recipient.
+ **Invitation declined** (`DECLINED`): Invitation declined by the recipient.
+ **Invitation canceled** (`CANCELED`): Invitation canceled by the sender.
+ **Invitation expired** (`EXPIRED`): Invitation has expired.

![Status list showing invitation sent, invitation declined, invitation canceled, and invitation expired.](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/images/transfer-billing-invitation-statuses.png)


*Figure 1: Invitation statues as displayed in the AWS Billing and Cost Management console.*

## View an invitation
<a name="orgs_transfer_billing-view-invitations-steps"></a>

**Terms and concepts**  
The following are terms and concepts used in the AWS Billing and Cost Management console:  
**Inbound billing**: Billing transfers that allow you to manage and pay for another organization’s consolidated bill.
**Outbound billing**: Billing transfers that allow an account outside your organization to manage and pay your consolidated bill.

**Minimum permissions**  
To view an invitation, you must have the following permissions  
`organizations:ListHandshakesForOrganization`
`organizations:ListHandshakesForAccount`
`organizations:DescribeHandshake`

To view an invitation, complete the following steps.

------
#### [  ]

**To view an invitation**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. On the left navigation in **Preferences and Settings**, choose **Billing transfers**.

1. 

**For inbound billings:**

   1. On the **Billing transfers** page, select the **Inbound billing** tab.

   1. On the **Inbound billing** tab, select the invitation you want to view details for.

   1. Choose the **Actions** dropdown menu, and then chose **View details**.

1. 

**For outbound billings:**

   1. On the **Billing transfers** page, select the **Outbound billing** tab.

   1. On the **Outbound billing** tab, you can view details for the invitation.

**Invitations are deleted after 30 days**  
You can view invitations for 30 days before they are deleted. If you accept an invitation, details for that transfer are not deleted.

------
#### [  ]

**To view an invitation**  
You can use one of the following operations:
+ AWS CLI: [list-handshakes-for-organization](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-handshakes-for-organization.html), [list-handshakes-for-account](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-handshakes-for-account.html), and [describe-handshake](https://docs.aws.amazon.com/cli/latest/reference/organizations/describe-handshake.html)

  1. **For invitations you have sent:**

     Run the following command find the [handshake](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#invitations-handshakes) ID.

     ```
     $ C:\> aws organizations list-handshakes-for-organization
     ```

     **For invitations you have received:**

     Run the following command find the [handshake](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#invitations-handshakes) ID.

     ```
     $ C:\> aws organizations list-handshakes-for-account
     ```

  1. From the response, note the handshake ID for the invitation you want to view details for.

  1. Run the following command to view details for the invitation:

     ```
     $ C:\> aws organizations describe-handshake \
         --id {{examplehandshakeid}}
     ```
+ AWS SDKs: [list-handshakes-for-organization](https://docs.aws.amazon.com/cli/latest/reference/organizations/API_ListHandshakesForOrganization.html), [list-handshakes-for-account](https://docs.aws.amazon.com/cli/latest/reference/organizations/API_ListHandshakesForAccount.html), and [describe-handshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeHandshake.html)

**Invitations are deleted after 30 days**  
You can view invitations for 30 days before they are deleted. If you accept an invitation, details for that transfer are not deleted.

------