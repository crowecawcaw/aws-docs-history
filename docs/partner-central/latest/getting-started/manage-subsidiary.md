# Managing AWS subsidiary account connections

From **Account Connections** in AWS Partner Central, you can connect your subsidiary seller accounts to your primary partner account. Connecting accounts improves PRM attribution accuracy. You can also optionally consolidate qualifications across your organization.

## Key concepts

### Primary account

The primary account is the account that initiates connection requests and owns the subsidiary relationship. This is typically the acquiring company's account for M&A scenarios, or the central partner account for organizations with multiple seller accounts. You must be signed in to your primary account to send connection requests.

### Subsidiary account

A subsidiary account is an account that you own and connect to your primary account. This might be an AWS Marketplace seller account that you operate in a different Region or business unit, or an account that belongs to a company your organization has acquired.

### Connection levels

Subsidiary connections work in two levels:

| Level                                  | How to activate                                 | What it does                                                                                                                                                                                                                                                                                                   |
| -------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Level 1 — Connection**               | Primary sends a request; subsidiary accepts     | PRM considers the subsidiary's revenue when calculating the primary's attribution. The primary account gains a consolidated Attributed Revenue report across all connected subsidiaries. No profile, scorecard, or display name changes occur.                                                                 |
| **Level 2 — Associate qualifications** | Subsidiary chooses **Associate qualifications** | Subsidiary's display name updates to "[Subsidiary Name] by [Primary Name]". All connected accounts receive a consolidated scorecard. Tier eligibility is recalculated based on the consolidated scorecard. Specializations, certifications, and select eligible programs are shared across connected accounts. |

Level 2 is optional and subsidiary-initiated. A partner can connect accounts and remain at Level 1 indefinitely, benefiting from PRM accuracy without making any profile or qualifications changes.

## When to use a subsidiary connection

### Multi-account consolidation

If you operate multiple AWS Marketplace seller accounts — for example, separate accounts by Region or business unit — connect them to your primary partner account. This ensures PRM accurately attributes revenue across all your accounts. Without connections, revenue from your seller accounts might not count toward your partner attribution, which directly affects your funding eligibility and Solution Consulting Agreement compliance. Your primary account also receives a consolidated Attributed Revenue report across all connected subsidiaries.

### Mergers and acquisitions

If your organization has acquired another AWS partner, you can use a subsidiary connection to:

- Ensure PRM accurately attributes combined revenue across both organizations immediately upon connection
- Optionally, through **Associate qualifications**, consolidate qualifications and scorecards, recalculate tier eligibility based on combined metrics, and update the acquired partner's display name to reflect the relationship. Associating qualifications also updates the subsidiary account to carry the brand of the primary account, so the acquired partner is presented as an affiliate of the primary brand (for example, "Northstar Cloud by Apex Technologies")

###### Important

The primary account's brand is used for all connected accounts. When a subsidiary associates qualifications, the subsidiary is branded as an affiliate of the primary account.

**What gets shared when a subsidiary associates qualifications:**

| Qualification                | What changes                                                                                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Specializations**          | Both accounts display the combined set of specializations from all connected accounts on their public profiles, in Partner Discovery, and in Partner Solution Finder (PSF) |
| **Certifications**           | Both accounts display the combined set of certifications across connected accounts                                                                                         |
| **Select eligible programs** | Program enrollments are shared across connected accounts for visibility and eligibility purposes                                                                           |
| **Tier**                     | Scorecard is consolidated from combined metrics; tier eligibility is recalculated based on the consolidated scorecard                                                      |

###### Important

Although select program enrollments are shared across connected accounts, only the account that originally enrolled in a program can apply for related funding. Wallets are not shared — each account retains its own wallet and can only draw funding against its own balance.

**Examples:**

- A global technology company acquires a cloud-native managed services partner. The acquiring company connects the acquired partner as a subsidiary. PRM immediately attributes the acquired partner's revenue. After the acquired partner chooses **Associate qualifications**, both accounts display the combined specializations and certifications, the consolidated scorecard determines tier eligibility, and the acquired partner's display name updates to reflect the parent company's brand.
- A large systems integrator acquires a boutique cloud consultancy. The connection at Level 1 fixes PRM attribution. The acquired company can later choose **Associate qualifications** when the organizations are ready to consolidate their public-facing presence.
- Two companies merge while maintaining fully separate brands. The subsidiary connection records the corporate relationship and ensures combined PRM attribution. Neither company chooses **Associate qualifications**, so no display name, scorecard, or qualifications changes occur.

## How the primary account is determined

For multi-account consolidation, the primary account is typically the account where both Partner and Seller registrations exist. For M&A, the acquiring company designates their account as primary by initiating the connection request — whichever account sends the request becomes the primary.

If you are unsure which account should be primary, contact your Partner Development Manager (PDM) or [AWS Partner Support](https://partnercentral.awspartner.com/partnercentral2/s/support "https://partnercentral.awspartner.com/partnercentral2/s/support").

## Sending a connection request

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral "https://us-east-1.console.aws.amazon.com/partnercentral") using your **primary account**.
2. In the left navigation pane, choose **Account Connections**.
3. Choose **Send connection request**.
4. Fill out the connection request form with:

   - Your full name
   - Your email address
   - The 12-digit AWS Account ID(s) of the accounts you want to connect (up to 10 per submission)

5. Review your selections and choose **Send connection request**.

###### Note

If you need to find an AWS Account ID, see [Finding your AWS account ID](../../../accounts/latest/reference/manage-acct-identifiers.md "../../../accounts/latest/reference/manage-acct-identifiers.md").

###### Important

Only connect accounts that you own or that belong to an organization you have acquired.

## Accepting a connection request

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral "https://us-east-1.console.aws.amazon.com/partnercentral") using the subsidiary account that received the request.
2. In the left navigation pane, choose **Account Connections**.
3. Choose the **Connection Requests** tab.
4. Select the connection request from the primary account.
5. Choose **Accept** to activate the connection, or **Reject** to decline.

After the subsidiary accepts the request, the connection is active at Level 1. PRM attribution and consolidated reporting are now active. No display name, scorecard, or qualifications changes occur at this point.

## Associating qualifications

After you establish a connection, the subsidiary account can choose **Associate qualifications** to consolidate qualifications across connected accounts. This is Level 2 of the connection. Choosing this option:

- Updates the subsidiary's display name to "[Subsidiary Name] by [Primary Name]" across Partner Discovery, PSF, and the public partner profile
- Replaces individual scorecards with a consolidated scorecard combining metrics from all connected accounts
- Triggers tier recalculation based on the consolidated scorecard
- Shares specializations, certifications, and select eligible program enrollments across connected accounts

1. Sign in to [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral "https://us-east-1.console.aws.amazon.com/partnercentral") using the **subsidiary account**.
2. In the left navigation pane, choose **Account Connections**, and then open the active connection.
3. Choose **Associate qualifications**.
4. Review the preview of how your display name and profile will appear.
5. Confirm to activate.

###### Note

This action updates your display name and public profile. Review the preview carefully before confirming.

### Disassociating qualifications

A subsidiary account can disassociate qualifications at any time. In the left navigation pane, choose **Account Connections**, open the active connection, and then choose **Disassociate qualifications**. After disassociation:

- The subsidiary's scorecard reverts to what it was prior to qualification association
- Shared specializations, certifications, and program enrollments are removed from the connected accounts' profiles
- Tier eligibility is recalculated independently for each account

## What changes after associating qualifications

| Change                        | Details                                                                                                                                                                                                                                                                               |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Subsidiary display name**   | Updated to "[Subsidiary Name] by [Primary Name]" in Partner Discovery, PSF, and the public partner profile                                                                                                                                                                            |
| **Specializations**           | Both accounts display the combined set of specializations from all connected accounts                                                                                                                                                                                                 |
| **Certifications**            | Both accounts display the combined set of certifications from all connected accounts                                                                                                                                                                                                  |
| **Select eligible programs**  | Program enrollments shared across connected accounts for visibility and eligibility. Only the account that originally enrolled can apply for related funding — wallets are not shared.                                                                                                |
| **Consolidated scorecard**    | All connected accounts receive a consolidated scorecard based on combined knowledge, experience, certifications, launched opportunities, and revenue metrics                                                                                                                          |
| **Tier recalculation**        | Tier eligibility is recalculated based on the consolidated scorecard. Select and Advanced tiers are automatically applied if combined metrics qualify. If Premier tier eligibility is triggered, either account can submit a Premier upgrade request using the manual review process. |
| **Tier downgrade protection** | If combined metrics later fall below the current tier's requirements, a 30-day grace period begins before any downgrade. Both accounts are notified.                                                                                                                                  |

## View and manage connected accounts

1. Sign in to your primary account in [AWS Partner Central](https://us-east-1.console.aws.amazon.com/partnercentral "https://us-east-1.console.aws.amazon.com/partnercentral").
2. In the left navigation pane, choose **Account Connections**.
3. On the **Account Connections** tab, view all connected accounts and their status.

From the primary account's analytics dashboard, you can view a consolidated Attributed Revenue report across all connected subsidiary accounts.
