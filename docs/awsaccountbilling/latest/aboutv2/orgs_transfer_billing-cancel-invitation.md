

# Canceling invitations
<a name="orgs_transfer_billing-cancel-invitation"></a>

When you sign in to your organization's management account, you can cancel invitations you sent that have not yet been responded to.

## Cancel an invitation
<a name="orgs_transfer_billing-cancel-invitations-steps"></a>

**Terms and concepts**  
The following are terms and concepts used in the AWS Billing and Cost Management console:  
**Inbound billing**: Billing transfers that allow you to manage and pay for another organization’s consolidated bill.
**Outbound billing**: Billing transfers that allow an account outside your organization to manage and pay your consolidated bill.

**Minimum permissions**  
To cancel an invitation, you must have the following permissions  
`organizations:ListHandshakesForOrganization`
`organizations:CancelHandshake`

To cancel an invitation, complete the following steps.

------
#### [  ]

**To cancel an invitation**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. On the left navigation in **Preferences and Settings**, choose **Billing transfers**.

1. On the **Inbound billing** tab, select the invitation you want to cancel.

1. Choose the **Actions** dropdown menu, and then chose **Cancel**.

------
#### [  ]

**To cancel an invitation**  
You can use one of the following operations:
+ AWS CLI: [list-handshakes-for-organization](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-handshakes-for-organization.html) and [cancel-handshake](https://docs.aws.amazon.com/cli/latest/reference/organizations/cancel-handshake.html)

  1. Run the following command find the [handshake](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#invitations-handshakes) ID.

     ```
     $ C:\> aws organizations list-handshakes-for-organization
     ```

  1. From the response, note the handshake ID for the invitation you want to cancel.

  1. Run the following command to cancel an invitation:

     ```
     $ C:\> aws organizations cancel-handshake \
         --id {{examplehandshakeid}}
     ```
+ AWS SDKs: [list-handshakes-for-organization](https://docs.aws.amazon.com/cli/latest/reference/organizations/API_ListHandshakesForOrganization.html), and [cancel-handshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CancelHandshake.html)

------

**What to do next**  
If you cancel an invitation, you can send another one at any time in the AWS Billing and Cost Management console or using the . For more information, see [Send invitation](orgs_transfer_billing-send-invitation.md).