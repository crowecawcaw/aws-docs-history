# Link BYOL accounts in WorkSpaces

You can use BYOL linking to link accounts and share
BYOL configurations. BYOL configurations include the CIDR range
used by your accounts and the images you use to create WorkSpaces with your Windows
license. All accounts that are linked share the same underlying hardware infrastructure.

The account enabled for BYOL linking is the primary owner of the underlying hardware
infrastructure, and is called the Source account. The Source account manages access to the
underlying hardware infrastructure. Target accounts are the accounts that are linked to the Source account.

###### Important

APIs for BYOL account linking are not available in the AWS GovCloud (US) Region.

###### Note

The AWS accounts that you want to link with must be part of your organization and under the same payer account.
You can only link accounts within the same Region.

###### To link the Source and Target accounts

1. Send an invitation link from your Source account to the Target account by using the **[CreateAccountLinkInvitation](../api/API_CreateAccountLinkInvitation.md "../api/API_CreateAccountLinkInvitation.md")** API.
2. Accept the pending link from your Target account by using the **[AcceptAccountLinkInvitation](../api/API_AcceptAccountLinkInvitation.md "../api/API_AcceptAccountLinkInvitation.md")** API.
3. Verify the link has been established by using the **[GetAccountLink](../api/API_GetAccountLink.md "../api/API_GetAccountLink.md")** or **[ListAccountLinks](../api/API_ListAccountLinks.md "../api/API_ListAccountLinks.md")** API.
