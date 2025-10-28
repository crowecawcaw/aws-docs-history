# Unlinking AWS Partner Central and AWS

accounts

When you link AWS Partner Central to an AWS account, AWS resources, such as APN Customer Engagement (ACE) opportunities, are created in the linked AWS account.
If you unlink to that AWS account and then link to a different AWS account, you lose access to the AWS resources in the original account.

The following list describes what happens to your AWS resources when you unlink from an original account and link to a different account. Consider the impact on your business
before you submit an unlinking request.

**AWS Partner Central users lose the ability to perform tasks listed in [Understanding the role permissions](linking-prerequisites.md#standard-role-permissions "linking-prerequisites.md#standard-role-permissions").
You must reassign the applicable IAM permissions after linking the new AWS account.**

For example, ACE users can't link ACE opportunities with private offers until IAM permissions in the new AWS account have been reassigned.

**You lose access to pending multi-partner opportunity invitations, and partners must re-invite you to them.**

For example, say AnyCompany has five unique invitations from AWS partners to collaborate on multi-partner opportunities.
If AnyCompany unlinks from the original AWS account and links to a different account without accepting the invitations,
all five partners must re-invite AnyCompany in order to collaborate on multi-partner deals.

**You lose access to shared multi-partner opportunities, and partners must re-share them even if you're the primary ACE opportunity owner.**

For example, say AnyCompany uses Partner Connections to share an ACE opportunity with Example Corp.
If AnyCompany unlinks from the original account and links to a different account, the ACE opportunity still exists,
but AnyCompany can't access it, even as a primary owner, until Example Corp shares the opportunity again.

**The APIs stop sending updates to ACE opportunities. For this reason, AWS recommends completing your sales engagements prior to unlinking.**

For example, say AnyCompany uses the Partner Central APIs to integrate their CRM systems with AWS Partner Central, and AnyCompany
uses their CRM system to manage those ACE opportunities. If AnyCompany unlinks from the original account and links to a different account,
any AWS updates to the ACE opportunities by will not sync and partners won't be notified about the updates.

**You can't access or edit linked private offers associated with ACE opportunities.**

For example, say AnyCompany linked AWS Partner Central with an AWS Marketplace seller account, and then associated the ACE opportunities with private offers.
If AnyCompany unlinks from the original account and links to a different account, AnyCompany can't access linked ACE opportunities and private offers. In addition, the linked
private offers can't be associated with ACE opportunities from the newly linked AWS account.

**The system automatically rejects AWS Originated (AO) opportunities pending acceptance.
AWS Sales teams see the AO's as rejected and share them again with the partner.**

For example, if AnyCompany unlinks from the original account and connects to a different account,
AnyCompany can't accept or reject pending AO's, which expire automatically in five days.
The AWS Sales team sees the rejected AO's and has to share them again.

If you decide to link to a different AWS account, AWS recommends:

- Accepting or rejecting pending AWS originated opportunities.
- Accepting or rejecting pending multi-partner opportunity invitations.
- For ACE opportunities linking to or disconnecting from private offers as needed.
- Completing sales engagements prior to unlinking if possible.

###### Note

There is no impact if you relink to the original AWS account.

###### To request unlinking

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") as an alliance lead or cloud administrator.
2. Under **Account linking**, choose **Manage linked
   account**.
3. Choose **Unlink account**.
4. Review the warning message and select a reason for unlinking your account.
5. Enter `confirm` and choose **Open support
   case**.
6. On the confirmation banner, choose **View case details** to track
   the progress of your request.
