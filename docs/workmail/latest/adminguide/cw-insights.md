# Using CloudWatch Insights with Amazon WorkMail

If you turned on email event logging in the Amazon WorkMail console or enabled audit logs
delivery to CloudWatch Logs, you can use Amazon CloudWatch Logs Insights to query your event logs. For more
information about turning on email event logging, see [Enabling email event logging](tracking.md "tracking.md"). For more information about CloudWatch Logs Insights, see
[Analyze log data with
CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") in the _Amazon CloudWatch Logs User Guide_.

The following examples demonstrate how to query CloudWatch Logs for common email events. You
run these queries in the CloudWatch console. For instructions about how to run these
queries, see [Tutorial: Run and modify a sample query](../../../AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_RunSampleQuery.md "../../../AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_RunSampleQuery.md") in the
_Amazon CloudWatch Logs User Guide_.

###### Example See why User B did not receive an email sent by User A.

The following code example demonstrates how to query for an outgoing email
sent by User A to User B, sorted by timestamp.

````
fields @timestamp, traceId

| sort @timestamp asc
| filter (event.from like /(?i)`userA@example.com`/ and event.eventName = "OUTGOING_EMAIL_SUBMITTED" and event.recipients.0 like /(?i)`userB@example.com`/) ``` This returns the sent message and trace ID. Use the trace ID in the following code example to query the event logs for the sent message. ``` fields @timestamp, event.eventName
| sort @timestamp asc
| filter traceId = "$`TRACEID`" ``` This returns the email message ID and the email events. `OUTGOING_EMAIL_SENT` indicates that the email was sent. `OUTGOING_EMAIL_BOUNCED` indicates that the email bounced. To see whether the email was received, query using the message ID in the following code example. ``` fields @timestamp, event.eventName
| sort @timestamp asc
| filter event.messageId like "$`MESSAGEID`" ``` This should also return the received message, because it has the same message ID. Use the trace ID in the following code example to query for delivery. ``` fields @timestamp, event.eventName
| sort @timestamp asc
| filter traceId = "$`TRACEID`" ``` This returns the delivery action and any applicable rule actions. ###### Example See all mail received from a user or domain The following code example demonstrates how to query for all mail received from a specified user. ``` fields @timestamp, event.eventName
| sort @timestamp asc
| filter (event.from like /(?i)`user@example.com`/ and event.eventName = "ORGANIZATION_EMAIL_RECEIVED") ``` The following code example demonstrates how to query for all mail received from a specified domain. ``` fields @timestamp, event.eventName
| sort @timestamp asc
| filter (event.from like "`example.com`" and event.eventName = "ORGANIZATION_EMAIL_RECEIVED") ``` ###### Example See who sent bounced emails The following code example demonstrates how to query for outgoing emails that bounced, and also returns the reasons for bouncing. ``` fields @timestamp, event.destination, event.reason
| sort @timestamp desc
| filter event.eventName = "OUTGOING_EMAIL_BOUNCED" ``` The following code example demonstrates how to query for incoming emails that bounced. It also returns the bounced recipients' email addresses and the reasons for bouncing. ``` fields @timestamp, event.bouncedRecipient.emailAddress, event.bouncedRecipient.reason, event.bouncedRecipient.status
| sort @timestamp desc
| filter event.eventName = "INCOMING_EMAIL_BOUNCED" ``` ###### Example See which domains are sending spam The following code example demonstrates how to query for recipients in your organization that are receiving spam. ``` stats count(*) as c by event.recipients.0
| filter (event.eventName = "ORGANIZATION_EMAIL_RECEIVED" and event.spamVerdict = "FAIL")
| sort c desc ``` The following code example demonstrates how to query for the sender of the spam emails. ``` fields @timestamp, event.recipients.0, event.sender, event.from
| sort @timestamp asc
| filter (event.spamVerdict = "FAIL") ``` ###### Example See why an email was sent to a recipient's spam folder The following code example demonstrates how to query for emails identified as spam, filtered by subject. ``` fields @timestamp, event.recipients.0, event.spamVerdict, event.spfVerdict, event.dkimVerdict, event.dmarcVerdict
| sort @timestamp asc
| filter event.subject like /(?i)$`SUBJECT`/ and event.eventName = "ORGANIZATION_EMAIL_RECEIVED" ``` You can also query by the email trace ID to see all events for the email. ###### Example See emails that match email flow rules The following code example demonstrates how to query for emails that matched outbound email flow rules. ``` fields @timestamp, event.ruleName, event.ruleActions.0.action
| sort @timestamp desc
| filter event.ruleType = "OUTBOUND_RULE" ``` The following code example demonstrates how to query for emails that matched inbound email flow rules. ``` fields @timestamp, event.ruleName, event.ruleActions.0.action, event.ruleActions.0.recipients.0
| sort @timestamp desc
| filter event.ruleType = "INBOUND_RULE" ``` ###### Example See how many emails are received or sent by your organization The following code example demonstrates how to query for the number of emails received by each recipient in your organization. ``` stats count(*) as c by event.recipient
| filter event.eventName = "MAILBOX_EMAIL_DELIVERED"
| sort c desc ``` The following code example demonstrates how to query for the number of emails sent by each sender in your organization. ``` stats count(*) as c by event.from
| filter event.eventName = "OUTGOING_EMAIL_SUBMITTED"
| sort c desc ```
````
