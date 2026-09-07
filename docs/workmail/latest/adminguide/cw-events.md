

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Monitoring Amazon WorkMail email event logs
<a name="cw-events"></a>

When you turn on email event logging for your Amazon WorkMail organization, Amazon WorkMail logs email events with CloudWatch. For more information about turning on email event logging, see [Enabling email event logging](tracking.md).

The following tables describe the events that Amazon WorkMail logs with CloudWatch, when the events are transmitted, and what the event fields contain.

**`ORGANIZATION_EMAIL_RECEIVED`**  
This event is logged when your Amazon WorkMail organization receives an email message.


| Field | Description | 
| --- | --- | 
| recipients | The intended recipients of the message. | 
| sender | The email address of the user who sent the email message on behalf of another user. This field is set only when an email is sent on behalf of another user. | 
| from | The **From** address, which is usually the email address of the user who sent the message. If the user sent the message as another user or on behalf of another user, this field returns the email address of the user on whose behalf the email was sent, not the email address of the actual sender. | 
| subject | The email message subject. | 
| messageId | The SMTP message ID. | 
| spamVerdict | Indicates whether the message is marked as spam by Amazon SES. For more information, see [Contents of Notifications for Amazon SES Email Receiving](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-notifications-contents.html) in the *Amazon Simple Email Service Developer Guide*. | 
| dkimVerdict | Indicates whether the DomainKeys Identified Mail (DKIM) check passed. For more information, see [Contents of Notifications for Amazon SES Email Receiving](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-notifications-contents.html) in the *Amazon Simple Email Service Developer Guide*. | 
| dmarcVerdict | Indicates whether the Domain-based Message Authentication, Reporting and Conformance (DMARC) check passed. For more information, see [Contents of Notifications for Amazon SES Email Receiving](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-notifications-contents.html) in the *Amazon Simple Email Service Developer Guide*. | 
| dmarcPolicy | Appears only when the dmarcVerdict field contains "FAIL". Indicates the action to take on the email when the DMARC check fails (NONE, QUARANTINE, or REJECT). This is set by the owner of the sending email domain.  | 
| spfVerdict | Indicates whether the Sender Policy Framework (SPF) checks passed. For more information, see [Contents of Notifications for Amazon SES Email Receiving](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-notifications-contents.html) in the *Amazon Simple Email Service Developer Guide*. | 
| messageTimestamp | Indicates when the message is received. | 

**`MAILBOX_EMAIL_DELIVERED`**  
This event is logged when a message is delivered to a mailbox in your organization. This is logged once for each mailbox to which a message is delivered, so a single `ORGANIZATION_EMAIL_RECEIVED` event can result in multiple `MAILBOX_EMAIL_DELIVERED` events.


| Field | Description | 
| --- | --- | 
| recipient | The mailbox to which the message is delivered. | 
| folder | The mailbox folder where the message is placed. | 

**`RULE_APPLIED`**  
This event is logged when an incoming or outgoing message starts an email flow rule.


| Field | Description | 
| --- | --- | 
| ruleName | The name of the rule. | 
| ruleType | The type of rule applied (INBOUND\_RULE, OUTBOUND\_RULE, or MAILBOX\_RULE). Inbound and outbound rules apply to your Amazon WorkMail organization. Mailbox rules apply only to specified mailboxes. For more information, see [Managing email flows](email-flows.md). | 
| ruleActions | Actions taken based on the rule. Different recipients of the message might have different actions, such as a bounced email or a successfully delivered email. | 
| targetFolder | Intended destination folder for a `Move` or `Copy` MAILBOX\_RULE. | 
| targetRecipient | Intended recipient of a `Forward` or `Redirect` MAILBOX\_RULE. | 

**`JOURNALING_INITIATED`**  
This event is logged when Amazon WorkMail sends an email to the journaling address specified by your organization administrator. This is only transmitted if journaling is configured for your organization. For more information, see [Using email journaling with Amazon WorkMail](journaling_overview.md).


| Field | Description | 
| --- | --- | 
| journalingAddress | The email address to which the journaling message is sent. | 

**`INCOMING_EMAIL_BOUNCED`**  
This event is logged when an incoming message can't be delivered to a target recipient. Emails can bounce for a number of reasons, such as a full target mailbox. The system logs this event once for each recipient that results in a bounced email. For example, if an incoming message is addressed to three recipients and two of them have full mailboxes, two INCOMING\_EMAIL\_BOUNCED events are logged.


| Field | Description | 
| --- | --- | 
| bouncedRecipient | The intended recipient for which Amazon WorkMail bounced the message. | 

**`OUTGOING_EMAIL_SUBMITTED`**  
This event is logged when a user in your organization submits an email message for sending. This is logged before the message leaves Amazon WorkMail, so this event doesn't indicate whether the email is successfully delivered.


| Field | Description | 
| --- | --- | 
| recipients | The recipients of the message as specified by the sender. Includes all recipients on the To, CC, and BCC lines. | 
| sender | The email address of the user who sent the email message on behalf of another user. This field is set only when an email is sent on behalf of another user. | 
| from | The **From** address, which is usually the email address of the user who sent the message. If the user sent the message as another user or on behalf of another user, this field returns the email address of the user on whose behalf the email was sent, not the email address of the actual sender. | 
| subject | The email message subject. | 

**`OUTGOING_EMAIL_SENT`**  
This event is logged when an outgoing email is successfully delivered to a target recipient. This is logged once for each successful recipient, so a single `OUTGOING_EMAIL_SUBMITTED` can result in multiple `OUTGOING_EMAIL_SENT` entries.


| Field | Description | 
| --- | --- | 
| recipient | The recipient of the successfully delivered email. | 
| sender | The email address of the user who sent the email message on behalf of another user. This field is set only when an email is sent on behalf of another user. | 
| from | The **From** address, which is usually the email address of the user who sent the message. If the user sent the message as another user or on behalf of another user, this field returns the email address of the user on whose behalf the email was sent, not the email address of the actual sender. | 
| messageId | The SMTP message ID. | 

**`OUTGOING_EMAIL_BOUNCED`**  
This event is logged when an outgoing message can't be delivered to a target recipient. Emails can bounce for a number of reasons, such as a full target mailbox. The system logs a bounce for each recipient that results in a bounced email. For example, if an outgoing message is addressed to three recipients and two of them have full mailboxes, two `OUTGOING_EMAIL_BOUNCED` events are logged.


| Field | Description | 
| --- | --- | 
| bouncedRecipient | The intended recipient for which the destination mail server bounced the message. | 

**`DMARC_POLICY_APPLIED`**  
This event is logged when a DMARC policy is applied to an email sent to your organization.


| Field | Description | 
| --- | --- | 
| from |  The From address, which is usually the email address of the user who sent the message. If the user sent the message as another user or on behalf of another user, this field returns the email address of the user on whose behalf the email was sent, not the email address of the actual sender. | 
| recipients |  The intended recipients of the message. | 
| policy | The applied DMARC policy, indicating the action to take on the email when the DMARC check fails (NONE, QUARANTINE, or REJECT). This is the same as the dmarcPolicy field in the ORGANIZATION\_EMAIL\_RECEIVED event. | 