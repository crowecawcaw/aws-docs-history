

# Email draft auto-save in the agent workspace
<a name="email-drafts"></a>

Amazon Connect Customer automatically saves in-progress emails as drafts, helping agents resume work without losing progress when connectivity is interrupted or when their browser is accidentally closed or refreshed. When agents return, their drafts are restored with the message body, recipients, subject line, and attachment references intact.

Automatically saving drafts doesn't require any configuration, and is available in the Agent Workspace and the Contact Control Panel (CCP).

## How draft auto-save works
<a name="email-drafts-how-it-works"></a>

As an agent composes an email, Connect Customer automatically saves the draft every few seconds. The agent can also save at any time by choosing the options menu (the three-dot icon next to **Send**) and then **Save draft**. After a save, the composer shows a **Draft saved** status with the time of the most recent save, next to the **Send** and **Discard** controls.

The following screenshot shows the agent workspace email composer. The options menu (the three-dot icon) is open at the bottom of the composer, next to the **Send** button. The menu lists **Save draft** first, followed by **Number Pad**, **Create Task**, and **New Email**.

![Email composer options menu listing Save draft, Number Pad, Create Task, and New Email.](https://docs.aws.amazon.com/connect/latest/adminguide/images/email-drafts-save-draft-menu.png)


A draft saves the following:
+ The message body.
+ The From, To, and CC email addresses.
+ The subject.
+ References to any attachments the agent has added.

The following screenshot shows the composer after a draft is saved. The status reads **Draft saved** followed by the time of the most recent save (for example, **Draft saved: 3:22 PM**), and appears at the bottom of the composer, to the left of the **Send** and **Discard** controls.

![Email composer showing the status Draft saved: 3:22 PM, to the left of Send and Discard.](https://docs.aws.amazon.com/connect/latest/adminguide/images/email-drafts-draft-saved-status.png)


Agents can add or remove CC recipients and attachments while composing, and those changes are saved with the draft.

If a save can't be completed — for example, when a CC address is not a valid email address — Connect Customer shows the message **Failed to save draft. Please try again.** The agent can correct the issue and the draft saves on the next attempt.

## Recovering a draft
<a name="email-drafts-recovering"></a>

When an agent reopens an email contact that has a saved draft, Connect Customer automatically loads the draft content into the email composer. The agent can continue editing the draft or discard it.

Draft recovery has the following behavior:
+ Draft recovery works across sessions, including after the agent signs out and signs back in.
+ A draft is tied to its specific email contact and isn't reused across other contacts.
+ Connect Customer keeps only the most recent draft for a contact. Each save replaces the previous draft.
+ Only the agent who created the draft can access it.

## Discarding a draft
<a name="email-drafts-discarding"></a>

An agent can choose **Discard** to delete the draft. When an agent discards a draft, Connect Customer deletes the saved draft message from your Amazon S3 bucket.

## Draft expiry and retention
<a name="email-drafts-expiry"></a>

The following rules govern draft expiry and retention:
+ Draft contacts inherit the default 14-day expiry period, consistent with existing outbound email behavior.
+ Draft contacts can have their expiry period extended. For more information about extending the expiry period, see the [UpdateContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateContact.html) API.
+ Draft contacts that an agent doesn't send or discard within the expiry period automatically expire and close, and Connect Customer deletes the saved draft message from your Amazon S3 bucket.

## Considerations
<a name="email-drafts-considerations"></a>

Keep the following considerations in mind:
+ Draft auto-save requires no administrator configuration. It's on by default for the email channel.
+ Connect Customer stores draft message content in the Amazon S3 bucket associated with your Connect Customer instance.
+ Draft auto-save is available in the agent workspace and the CCP. It is not available in custom agent applications built on the Connect Customer Streams API.