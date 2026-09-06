# Forward email contacts to external email addresses

Agents can forward email contacts to external email addresses (for example, `firstname.lastname@anycompany.com`) or distribution lists (for example, `support-team-distro@anycompany.com`) when they need to involve other parties outside of Connect Customer. This feature allows agents to share customer emails with external teams, partners, or systems while maintaining the email thread within Connect Customer.

## Overview of email forwarding

Email forwarding enables agents to:

- Send a copy of the email contact to external email addresses
- Forward emails to distribution lists or group email addresses
- Include additional context or instructions when forwarding

###### Important

Forwarding an email contact sends a copy to external recipients but does not transfer the contact out of Connect Customer. The agent remains responsible for the contact until they end it or transfer it to another agent or queue within Connect Customer.

## How to forward an email contact

To forward an email contact to an external address:

1. In the CCP, open the email contact you want to forward.
2. Choose the **Forward** option or button.
3. In the **To** field, enter the external email address or addresses where you want to forward the email. You can only enter 1 email address in the **To** field. Additional recipients can be added to the **CC** field.
4. Optionally, add a message in the body field to provide context or instructions for the external recipients.
5. Optionally, attach files you want to include. Original inbound
   attachments do not carry over to the forwarded email.
6. Review the forwarded content, which includes:

   - The original email message and thread
   - Your additional message (if provided)

7. Choose **Send** to forward the email.

![The email forward interface in the CCP.](images/email-forward-interface.png)

The forwarded email is sent to the external recipients. The email contact remains active in your CCP until you end it either by responding to it or choosing **Done** to close it.

## Forwarding to distribution lists

You can forward email contacts to distribution lists or group email addresses in the same way you forward to individual addresses. Simply enter the distribution list email address in the **To** field.

Common use cases for forwarding to distribution lists include:

- Escalating issues to specialized teams
- Sharing customer feedback with product teams
- Notifying management of high-priority issues
- Coordinating with external partners or vendors

## Permissions and restrictions

Email forwarding capabilities are controlled by your security profile permissions. Your administrator configures which agents can forward emails ("Initiate email conversation" must be enabled on your [Contact Control Panel (CCP)](security-profile-list.md#ccp-permissions-list "security-profile-list.md#ccp-permissions-list")) and to which external addresses (based on checking contact attributes in the [Default outbound flow in Connect Customer: "This call is not being recorded"](default-outbound.md "default-outbound.md")).

Potential restrictions might include:

- Allowed external domains or email addresses
- Blocked domains to prevent forwarding to unauthorized recipients
- Limits on the number of external recipients per forward
- Requirements for manager approval before forwarding

###### Note

If you attempt to forward an email to an address that is not permitted by your organization's policies, you might receive an error message.

## Best practices for forwarding emails

Follow these best practices when forwarding email contacts:

- **Verify recipient addresses**: Double-check that you're forwarding to the correct external address before sending.
- **Protect customer privacy**: Be mindful of customer data and privacy regulations when forwarding emails to external parties. Only forward to authorized recipients.
- **Add context**: Include a brief message explaining why you're forwarding the email and what action you expect from the recipients.
- **Review attachments**: Make sure that any attachments being forwarded are appropriate and don't contain sensitive information that shouldn't be shared externally.
- **Follow up**: If you're forwarding an email for action by external parties, make sure to follow up to ensure the issue is resolved.
- **Document the forward**: Add notes to the contact record indicating that you forwarded the email, to whom, and why.

## Forwarding compared to transferring

It's important to understand the difference between forwarding and transferring an email contact:

- **Forwarding**: Sends a copy of the email to external recipients outside of Connect Customer. You remain responsible for the contact and must continue to handle it or end it.
- **Transferring**: [Quick connect scenarios for transferring contacts](how-quick-connects-work.md "how-quick-connects-work.md"), transfers the email contact to another agent or queue within Connect Customer. The contact is removed from your queue and assigned to the transfer destination.

Use forwarding when you need to share information with external parties while maintaining ownership of the contact. Use transferring when you need to hand off the contact to another agent or team within your contact center.
