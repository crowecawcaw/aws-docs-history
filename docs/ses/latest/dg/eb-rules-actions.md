

# Rule actions

Rule actions process the recipients selected by a rule's `Conditions` and `Unless` lists. A rule contains from 1 through 10 actions. The actions run sequentially in the order that you configure.

An action can change the email or its recipient list before the next action runs. For example, an action can add a header that a later storage action includes, or replace recipients before a later delivery action. For a complete log example and the `action_metadata` value for each action, see [Follow rule execution](eb-rules-monitoring.md#eb-rules-monitoring-follow-execution). To investigate a failed action, see [An action failed](eb-rules-monitoring.md#eb-rules-monitoring-action-failed). If later actions or rules did not run, see [Processing stopped early](eb-rules-monitoring.md#eb-rules-monitoring-stopped-early).

## How action order works
<a name="eb-rules-actions-order"></a>

A rule runs its actions as follows:

1. The first action receives the recipients selected by the rule.

1. Each action runs in configured order.

1. An action can modify the email or recipient list used by later actions.

1. The `Drop` action stops rule-set processing for its selected recipients.

1. When recipients remain, processing continues with the next action and then the next rule.

An `Unless` condition and a `Drop` action have different effects. An `Unless` match skips the current rule's actions for that recipient. The recipient remains available to later rules. `Drop` stops all remaining rule-set processing for the selected recipient.

**Add a header before storage**  
The Write to S3 action in this example stores the email with the added `X-Route: orders` header.

```
Actions:
1. Add header X-Route: orders
2. Write to S3 bucket inbound-orders-example
```

**Replace a recipient before delivery**  
The relay action in this example uses `processing@example.net` as the SMTP envelope recipient. The replacement does not change addresses displayed in the email's `To` or `CC` header.

```
Matched recipient: orders@example.com
Actions:
1. Replace recipient with processing@example.net
2. Relay through CorporateRelay
```

**Store an email before dropping a recipient**  
The first action in this example stores the email. `Drop` then stops rule-set processing for `blocked@example.com`, so Relay and later rules do not run for that recipient. `allowed@example.com` remains available to later rules because the current rule did not select it.

```
Current recipients: blocked@example.com, allowed@example.com
Matched recipient: blocked@example.com
Actions:
1. Write to S3 bucket blocked-mail-example
2. Drop
3. Relay through CorporateRelay
```

## Rule action reference
<a name="eb-rules-actions-reference"></a>

The following lists group the supported actions by customer outcome. Some actions require an AWS Identity and Access Management (IAM) execution role with access to another AWS service or resource. For the required policies, see [Permission and trust polices to execute rule actions](eb-policies.md#eb-policies-rule-action).

Follow each action's API link for its complete parameters, value constraints, and required resources.

Choose an action to go to its detailed section.
+ [Actions that modify email or recipients](#eb-rules-actions-reference-modify)
  + [Add header](#eb-rules-actions-add-header) – Adds a custom header that later actions or downstream systems can use.
  + [Replace recipient](#eb-rules-actions-replace-recipient) – Replaces selected recipients with specified addresses.
+ [Actions that store or process email](#eb-rules-actions-reference-store-process)
  + [Write to S3](#eb-rules-actions-write-to-s3) – Stores the email content in an S3 bucket.
  + [Archive](#eb-rules-actions-archive) – Stores the email in an SES Mail Manager archive.
  + [Publish to SNS](#eb-rules-actions-publish-to-sns) – Publishes the email content to an Amazon SNS topic.
  + [Invoke Lambda function](#eb-rules-actions-invoke-lambda) – Invokes an AWS Lambda function to process the email.
  + [Deliver to Q Business](#eb-rules-actions-deliver-to-q-business) – Sends the email to an Amazon Q Business application for ingestion into its knowledge base.
+ [Actions that deliver email](#eb-rules-actions-reference-deliver)
  + [SMTP relay](#eb-rules-actions-relay) – Forwards the email to another mail server through a configured relay.
  + [Send to internet](#eb-rules-actions-send) – Uses SES to send the email to its current recipients.
  + [Deliver to WorkMail mailbox](#eb-rules-actions-deliver-to-mailbox) – Delivers the email to an Amazon WorkMail organization.
+ [Actions that respond or stop processing](#eb-rules-actions-reference-respond-stop)
  + [Drop](#eb-rules-actions-drop) – Stops rule-set processing for the selected recipients.
  + [Bounce](#eb-rules-actions-bounce) – Sends a non-delivery report to the sender.

### Actions that modify email or recipients
<a name="eb-rules-actions-reference-modify"></a>

#### Add header
<a name="eb-rules-actions-add-header"></a>

The *Add header* action adds a custom header to the email for the recipients selected by the rule. Use it to pass routing, classification, or processing information to a later action or downstream system.

The action changes only the email header block. It does not change the message body or recipient list. In the following example, only the email variant for `orders@example.com` receives the header:

```
Selected recipient: orders@example.com
Added header: X-Route: orders
```

##### Using the added header in later actions
<a name="eb-rules-actions-add-header-order"></a>

Actions that later render, store, publish, or deliver the email receive the added header. Place Add header before an action that must receive the header:

```
Actions:
1. Add header X-Route: orders
2. Write to S3 bucket inbound-orders-example
```

The stored email contains the following header:

```
X-Route: orders
```

An Add header action does not replace an existing header with the same name. If the original email already contains the header, both values remain, with the added value first:

```
Added by the rule:
X-Route: orders

Original email:
X-Route: external

Result:
X-Route: orders
X-Route: external
```

**Later rule conditions use the original headers**  
A later action receives the added header, but later rule conditions evaluate the headers from the original accepted email. Do not add a header in one rule and expect a later rule condition to match that added value. Use the original rule conditions to select the recipients that need the custom header.

##### Configuration fields and limits
<a name="eb-rules-actions-add-header-configuration"></a>

Header name  
Required. The name must start with `X-` or `x-`. After the prefix, use only letters, numbers, and hyphens. The complete name can contain up to 64 characters.  
Valid examples are `X-Route`, `X-Message-Type`, and `X-Department-123`. Invalid examples are `Route`, `X_Route`, and `X-Route.Value`.

Header value  
Required. The value must contain from 1 through 128 characters.

**Encoding non-ASCII header values**  
Header values are not always Base64-encoded. Printable ASCII values, such as `orders`, remain unchanged. A value containing non-ASCII characters is MIME-encoded as an RFC 2047 encoded word. The raw header can use quoted-printable `Q` encoding or `B` encoding, which uses Base64. Email clients normally decode the value when displaying the header.

Add header does not accept `ActionFailurePolicy`.

##### Creating an Add header action with the AWS CLI
<a name="eb-rules-actions-add-header-cli"></a>

The following command creates a rule set with one Add header action:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{add-header-example}} \
  --rules '[{
    "Name": "mark-orders",
    "Actions": [{
      "AddHeader": {
        "HeaderName": "X-Route",
        "HeaderValue": "orders"
      }
    }]
  }]'
```

Replace the AWS Region and rule set name with your values.

##### Recommendations
<a name="eb-rules-actions-add-header-recommendations"></a>
+ Use a descriptive header name that identifies one purpose, such as `X-Route` or `X-Message-Type`.
+ Place Add header before every action that must receive the header.
+ Use a unique header name when downstream systems expect one value. Add header preserves existing values with the same name.
+ Do not depend on the added header in a later rule condition.
+ Do not put credentials, access tokens, or other secrets in a header value. The header travels with the email to later destinations.
+ Use a recipient condition when only specific recipients must receive the header.

**Recipient-specific message variants**  
Different recipients of one email can receive different added headers. A later action can run separately for each distinct header variant.  
For example, suppose one rule adds `X-User: User1` for `user1@example.com` and another adds `X-User: User2` for `user2@example.com`. A later Invoke Lambda function action receives one invocation for each recipient and its corresponding header. Account for separate invocations when a downstream action has per-request cost or side effects.

For complete field constraints, see [AddHeaderAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_AddHeaderAction.html) in the *SES Mail Manager API Reference*.

#### Replace recipient
<a name="eb-rules-actions-replace-recipient"></a>

The *Replace recipient* action replaces selected SMTP envelope recipients with one or more new addresses. It changes only the SMTP envelope recipient list. It does not change addresses displayed in the email's `To`, `CC`, or other headers, and it does not change the message body.

```
Original envelope recipients:
orders@example.com
audit@example.com

Selected recipient:
orders@example.com

Replacement:
processing@example.net

Resulting envelope recipients:
processing@example.net
audit@example.com
```

##### Effect on later actions and rules
<a name="eb-rules-actions-replace-recipient-order"></a>

Later actions in the current rule use the replacement recipients. The rule does not evaluate its conditions again for the new addresses:

```
Condition:
RECIPIENT EQUALS orders@example.com

Actions:
1. Replace recipient with processing@example.net
2. Relay through CorporateRelay
```

Relay uses `processing@example.net`, even though that address does not match the original condition. Later rules evaluate the updated recipient list. A later rule can match `processing@example.net`; it no longer receives `orders@example.com`.

Headers added for the original selected recipient remain associated with its replacements:

```
Actions:
1. Add header X-Route: orders
2. Replace orders@example.com with processing@example.net
3. Relay through CorporateRelay
```

The relayed email for `processing@example.net` contains `X-Route: orders`.

##### Replacing one recipient with multiple recipients
<a name="eb-rules-actions-replace-recipient-multiple"></a>

Each selected recipient is replaced with the complete `ReplaceWith` list:

```
Selected recipient:
orders@example.com

ReplaceWith:
processing@example.net
audit@example.net

Result:
processing@example.net
audit@example.net
```

When a rule selects more than one recipient, the complete replacement list is applied to each selected recipient:

```
Selected recipients:
orders-us@example.com
orders-eu@example.com

ReplaceWith:
processing@example.net
```

The replacement address is inserted once for each selected original recipient. Use conditions that select one source recipient when repeated replacement addresses are not intended.

##### Configuration fields and limits
<a name="eb-rules-actions-replace-recipient-configuration"></a>

Specify from 1 through 100 unique replacement email addresses in `ReplaceWith`. Each address can contain up to 254 characters. Use a plain email address, such as `processing@example.net`. Do not include a display name such as `Order Processing <processing@example.net>`.

Replace recipient does not accept `ActionFailurePolicy`.

**ReplaceWith must be supplied**  
The public API marks `ReplaceWith` as optional, but action processing requires the list. Always supply from 1 through 100 addresses. Omitting the list can fail rule-set execution, and Replace recipient does not accept `ActionFailurePolicy`.

##### Creating a Replace recipient action with the AWS CLI
<a name="eb-rules-actions-replace-recipient-cli"></a>

The following command creates a rule set that replaces `orders@example.com` with `processing@example.net`. Replace the AWS Region, rule set name, source recipient, and replacement recipient with your values:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{replace-recipient-example}} \
  --rules '[{
    "Name": "reroute-orders",
    "Conditions": [{
      "StringExpression": {
        "Evaluate": {
          "Attribute": "RECIPIENT"
        },
        "Operator": "EQUALS",
        "Values": [
          "{{orders@example.com}}"
        ]
      }
    }],
    "Actions": [{
      "ReplaceRecipient": {
        "ReplaceWith": [
          "{{processing@example.net}}"
        ]
      }
    }]
  }]'
```

##### Recommendations
<a name="eb-rules-actions-replace-recipient-recommendations"></a>
+ Use a `RECIPIENT` condition to select individual SMTP envelope recipients.
+ Put Replace recipient before every delivery action that must use the new address.
+ Remember that the visible `To` and `CC` headers do not change.
+ Select one source recipient when each replacement address must appear only once.
+ Use a separate rule for each source-to-destination mapping when replacements differ by source address.
+ Verify that later delivery actions can deliver to the replacement domains.
+ Avoid creating a loop in which later routing replaces an address with an address that enters the same routing path again.

For complete field constraints, see [ReplaceRecipientAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ReplaceRecipientAction.html) in the *SES Mail Manager API Reference*.

### Actions that store or process email
<a name="eb-rules-actions-reference-store-process"></a>

#### Write to S3
<a name="eb-rules-actions-write-to-s3"></a>

The *Write to S3* action stores the email's MIME content in an S3 bucket. The stored object contains the message headers and body.

Headers added by earlier rule actions are included in the stored email:

```
Actions:
1. Add header X-Route: orders
2. Write to S3 bucket inbound-orders-example
```

The stored object contains the following header:

```
X-Route: orders
```

##### S3 object name
<a name="eb-rules-actions-write-to-s3-object-name"></a>

Without an S3 prefix, the object key is the Mail Manager message ID:

```
example-message-id-1234567890
```

With the prefix `orders`, the object key is:

```
orders/example-message-id-1234567890
```

Mail Manager adds the separating slash when the configured prefix does not end with one.

When recipient-specific message changes create more than one email variant, an object key can include an additional instance identifier:

```
orders/example-message-id-1234567890_7f54cdb2
```

Do not require object keys to end with the message ID when a rule set creates recipient-specific variants.

##### Configuration fields and limits
<a name="eb-rules-actions-write-to-s3-configuration"></a>

IAM role ARN  
Required. The role grants access to the destination bucket. The ARN length is 20–2,048 characters.

S3 bucket  
Required. Specify the bucket name, not its ARN. The name can contain letters, numbers, periods, and hyphens. Follow the linked API reference for the current length constraints.

S3 prefix  
Optional. The prefix contains from 1 through 62 characters. It can contain letters, numbers, `!`, `_`, `.`, `*`, `'`, `(`, `)`, `/`, and `-`. The message ID or variant object name follows the prefix.

S3 server-side encryption KMS key ID  
Optional. Specifies the AWS KMS key for S3 server-side encryption. The value contains from 20 through 2,048 characters.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`.

When `S3SseKmsKeyId` is present, the action requests S3 server-side encryption with AWS KMS. The request includes an encryption context containing the message ID, rule set ID, and source account.

When `S3SseKmsKeyId` is absent, the action does not request a specific AWS KMS key. Any default encryption configured on the bucket still applies.

##### Required permissions
<a name="eb-rules-actions-write-to-s3-permissions"></a>

The principal that creates or updates the rule set needs permission for the corresponding Mail Manager rule-set operation and `iam:PassRole` permission for the role specified by `RoleArn`.

The rule action's IAM role must trust the SES service principal. It needs `s3:PutObject` permission for objects in the destination bucket and `s3:ListBucket` permission for the bucket. When you specify a customer managed AWS KMS key, the role also needs the AWS KMS permission described in the linked policy.

For the trust policy, see [Permission and trust polices to execute rule actions](eb-policies.md#eb-policies-rule-action). For the S3 and AWS KMS permission policies, see [Permission policy for *Write to S3* rule action](eb-policies.md#eb-policies-s3).

##### Creating a Write to S3 action with the AWS CLI
<a name="eb-rules-actions-write-to-s3-cli"></a>

The following command creates a rule set that writes email to the `orders` prefix and stops processing if storage fails with a customer configuration error. Replace the AWS Region, account ID, role name, bucket name, and rule set name with your values:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{write-to-s3-example}} \
  --rules '[{
    "Name": "store-orders",
    "Actions": [{
      "WriteToS3": {
        "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{MailManagerS3ActionRole}}",
        "S3Bucket": "{{inbound-orders-example}}",
        "S3Prefix": "orders",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

##### Failure behavior
<a name="eb-rules-actions-write-to-s3-failures"></a>

The action treats configuration problems such as the following as customer errors:
+ The bucket does not exist.
+ The role cannot access the bucket.
+ The AWS KMS key does not exist or is disabled.
+ The role cannot use the AWS KMS key.
+ The S3 request is invalid.

`CONTINUE` lets later actions run even though the email was not stored. `DROP` stops rule-set processing for the selected recipients.

Transient S3 failures, including throttling and HTTP `503` responses, use the execution retry path instead of immediately applying `ActionFailurePolicy`.

##### Recommendations
<a name="eb-rules-actions-write-to-s3-recommendations"></a>
+ Put Add header before Write to S3 when the stored email must contain the added header.
+ Put Write to S3 before Invoke Lambda function when the function needs the email body.
+ Use a prefix such as `orders/`, `security-review/`, or `compliance/` to separate workflows.
+ Use `DROP` when later delivery must not continue unless the email is stored successfully.
+ Use `CONTINUE` when storage is optional and later delivery must continue.
+ Configure S3 lifecycle rules according to the required retention period.
+ Use a customer managed AWS KMS key when your encryption requirements need control over the key policy, rotation, or auditing.

**Destination validation and object variants**  
Rule-set creation validates the field formats but does not confirm that the bucket and permissions remain valid. A missing bucket or revoked permission can fail when an email reaches the action.  
The action writes objects with the `bucket-owner-full-control` canned ACL. Stored objects do not receive a `.eml` extension. Recipient-specific message variants can produce more than one object for one Mail Manager message ID.

For complete field constraints, see [S3Action](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_S3Action.html) in the *SES Mail Manager API Reference*.

#### Archive
<a name="eb-rules-actions-archive"></a>

The *Archive* action stores the email in an existing SES Mail Manager archive. You can search archived email, download individual messages, and export search results.

Create the archive before referencing it in a rule action. The archive controls retention and encryption independently of the action.

Headers added by earlier actions are included in the archived email:

```
Actions:
1. Add header X-Record-Type: compliance
2. Archive in ComplianceArchive
```

##### Choosing the action order
<a name="eb-rules-actions-archive-order"></a>

Place Archive before delivery or Drop when you need to retain the email first:

```
Actions:
1. Archive in ComplianceArchive
2. Relay through CorporateRelay
```

For email that must not continue unless archiving succeeds, configure `ActionFailurePolicy` as `DROP`.

##### Configuration fields and limits
<a name="eb-rules-actions-archive-configuration"></a>

Target archive  
Required. Specify the ID or ARN of an existing Mail Manager archive. The value contains from 1 through 2,048 characters.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`.

Rule-set creation or update fails when the archive does not exist in the account or the archive is pending deletion.

Retention and encryption are properties of the archive resource, not the Archive action. The default archive retention period is 180 days unless you configure another supported period.

##### Required permissions
<a name="eb-rules-actions-archive-permissions"></a>

Archive does not contain an IAM execution role and does not require `iam:PassRole`. The principal creating or updating the rule set needs permission for `ses:CreateRuleSet` or `ses:UpdateRuleSet`.

Separate permissions can be required when you create or update an archive that uses a customer managed AWS KMS key, or when you export archived email to an S3 bucket. For archive creation, retention, search, and export instructions, see [Email archiving](eb-archiving.md). For AWS KMS and export policies, see [Permission policies for Email archiving](eb-policies.md#eb-policies-archiving).

##### Creating an Archive action with the AWS CLI
<a name="eb-rules-actions-archive-cli"></a>

The following command creates a rule set that writes email to the existing archive `ar-id-1234`. Replace the AWS Region, archive ID, and rule set name with your values:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{archive-action-example}} \
  --rules '[{
    "Name": "archive-orders",
    "Actions": [{
      "Archive": {
        "TargetArchive": "{{ar-id-1234}}",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

##### Archive lifecycle
<a name="eb-rules-actions-archive-lifecycle"></a>

A referenced archive cannot be deleted while a rule set uses it. Remove the Archive action or change its target before deleting the archive. An archive pending deletion cannot be assigned to a new or updated rule set. Deleting the rule set does not delete the archive or its stored email.

##### Recommendations
<a name="eb-rules-actions-archive-recommendations"></a>
+ Put Add header before Archive when the archived email must contain the added header.
+ Put Archive before SMTP relay, Send to internet, Bounce, or Drop when retention must happen first.
+ Use `DROP` when processing must stop if the Archive action reports a customer configuration error.
+ Configure the archive retention period according to your regulatory and business requirements.
+ Configure a customer managed AWS KMS key when you require control over key policy, rotation, or auditing.
+ Test archive searches and exports before relying on the archive for a compliance workflow.

**Archive and Write to S3 are different**  
Archive stores email in a managed Mail Manager archive that supports search and export. Write to S3 stores an object directly in your bucket.  
Use Archive when you need managed retention and search. Use Write to S3 when an application needs direct access to the MIME object.

For complete field constraints, see [ArchiveAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ArchiveAction.html) in the *SES Mail Manager API Reference*.

#### Publish to SNS
<a name="eb-rules-actions-publish-to-sns"></a>

The *Publish to SNS* action publishes one JSON notification to an Amazon Simple Notification Service (Amazon SNS) topic. Use this action when applications or multiple subscribers need to process information about received email.

The notification contains a `mail` object with message metadata and extracted headers, and a `receipt` object with authentication results and the recipients selected for the action. It also contains a `content` field when `PayloadType` is `CONTENT`.

##### Behavior and ordering effects
<a name="eb-rules-actions-publish-to-sns-behavior"></a>

The action makes one Amazon SNS `Publish` request for the selected recipient group. The selected SMTP envelope recipients appear in `receipt.recipients`.

Publish to SNS uses the Mail Manager SNS payload format. In this format, `mail.destination` contains addresses from the email's `To` header and preserves display names. It does not include addresses from the `CC` header. If the `To` header cannot be read, the field contains the SMTP envelope recipients selected for the action.

Use `receipt.recipients` to identify the SMTP envelope recipients selected by the rule.

Headers added by an earlier Add header action appear in `mail.headers`. With `PayloadType` set to `CONTENT`, the added headers also appear in the full MIME email in `content`.

```
Selected recipient: orders@example.com

Actions:
1. Add header X-Route: orders
2. Publish to SNS
```

With `PayloadType` set to `CONTENT` and `Encoding` set to `UTF-8`, the notification has the following structure. Fields without values are omitted:

```json
{
  "notificationType": "Received",
  "mail": {
    "timestamp": "2026-11-14T18:30:00.000Z",
    "messageId": "010001example-message-id",
    "source": "sender@example.net",
    "destination": [
      "orders@example.com"
    ],
    "headersTruncated": false,
    "commonHeadersTruncated": false,
    "headers": [
      {
        "name": "X-Route",
        "value": "orders"
      },
      {
        "name": "From",
        "value": "sender@example.net"
      },
      {
        "name": "To",
        "value": "orders@example.com"
      },
      {
        "name": "Subject",
        "value": "New order"
      }
    ],
    "commonHeaders": {
      "from": [
        "sender@example.net"
      ],
      "to": [
        "orders@example.com"
      ],
      "messageId": "010001example-message-id",
      "subject": "New order"
    }
  },
  "receipt": {
    "timestamp": "2026-11-14T18:30:00.000Z",
    "recipients": [
      "orders@example.com"
    ],
    "type": "SNS",
    "action": {
      "topicArn": "arn:aws:sns:us-east-1:111122223333:mail-manager-notifications",
      "encoding": "UTF-8",
      "payloadType": "CONTENT"
    },
    "processingTimeMillis": 0,
    "spamVerdict": {
      "status": "PASS"
    },
    "virusVerdict": {
      "status": "PASS"
    },
    "spfVerdict": {
      "status": "PASS"
    },
    "dkimVerdict": {
      "status": "PASS"
    },
    "dmarcVerdict": {
      "status": "PASS"
    }
  },
  "content": "X-Route: orders\r\nFrom: sender@example.net\r\nTo: orders@example.com\r\nSubject: New order\r\n\r\nOrder 1234"
}
```

With `PayloadType` set to `HEADERS`, the `mail` and `receipt` objects use the same structure, but the notification omits `content`. With `Encoding` set to `BASE64`, `content` contains the Base64-encoded MIME email instead of the UTF-8 string. Values in `mail.headers` preserve their MIME header encoding.

Place Add header before Publish to SNS when subscribers need the added header. For details about how ASCII and non-ASCII values appear, see [Add header](#eb-rules-actions-add-header).

##### Configuration fields and limits
<a name="eb-rules-actions-publish-to-sns-configuration"></a>

Topic ARN  
Required. Specify a standard Amazon SNS topic in the same AWS partition, Region, and account as the rule set.  
The ARN must contain 20–2,048 characters. The topic name can contain 1–256 letters, numbers, underscores, and hyphens. FIFO topic names contain `.fifo`, which the accepted topic ARN format does not allow.

IAM role ARN  
Required. Specify the execution role that Mail Manager assumes to publish the notification. The ARN must contain 20–2,048 characters and identify an IAM role in the same AWS partition. Because `iam:PassRole` applies only within one account, use a role in the rule set's account.

Payload type  
Optional. Valid values are:  
+ `CONTENT` includes the full MIME email in `content`, including the header block, body, and attachments. The notification also extracts up to 20 KiB (20,480 bytes) of headers into `mail.headers`. This is the default.
+ `HEADERS` extracts up to 100 KiB (102,400 bytes) of headers into `mail.headers`. The notification does not contain the `content` field or the email body.
If the extracted header block exceeds the applicable limit, the notification sets `mail.headersTruncated` to `true`. Header truncation does not prevent the action from publishing the notification.  
For `CONTENT`, the full email after earlier header changes can contain at most 150 KiB (153,600 bytes). The action fails without publishing when the content exceeds this limit.

Encoding  
Optional. Valid values are:  
+ `UTF-8` places the email content in the JSON notification as a UTF-8 string. This is the default. It might not preserve every byte when the original email uses another encoding.
+ `BASE64` Base64-encodes the complete MIME email. Subscribers must decode the `content` value before processing it. Use this value when subscribers must preserve the original MIME bytes.
`Encoding` applies only to the `content` field. It does not encode `mail.headers`, and it has no content to encode when `PayloadType` is `HEADERS`.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`. For their effects, see [Handling an action failure](#eb-rules-actions-failure-policy).

**Amazon SNS message limit**  
Amazon SNS counts the notification JSON and its message attributes against the topic's `MaximumMessageSize`. The default is 256 KiB (262,144 bytes).

If the rendered notification exceeds the topic's configured limit, Amazon SNS rejects the publish request. The notification is not partially delivered.

##### Required permissions
<a name="eb-rules-actions-publish-to-sns-permissions"></a>

The principal that creates or updates the rule set needs permission for the corresponding Mail Manager rule-set operation and `iam:PassRole` permission for the role specified by `RoleArn`.

The execution role must trust the SES service principal and allow `sns:Publish` on the configured topic. When the topic uses server-side encryption with a customer managed AWS KMS key, the role also needs `kms:GenerateDataKey*` and `kms:Decrypt` on that key. The key policy must allow the execution role to use the key.

For the execution-role trust policy, see [Permission and trust polices to execute rule actions](eb-policies.md#eb-policies-rule-action). For the Amazon SNS and AWS KMS permissions, see [Permission policy for *Publish to SNS* rule action](eb-policies.md#eb-policies-sns).

For current encrypted-topic requirements, see [Managing Amazon SNS encryption keys and costs](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html).

##### Creating a Publish to SNS action with the AWS CLI
<a name="eb-rules-actions-publish-to-sns-cli"></a>

The following command creates a rule set with one Publish to SNS action:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{publish-to-sns-example}} \
  --rules '[{
    "Name": "publish-email",
    "Actions": [{
      "PublishToSns": {
        "TopicArn": "arn:aws:sns:{{us-east-1}}:{{123456789012}}:{{mail-manager-notifications}}",
        "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{MailManagerSnsActionRole}}",
        "Encoding": "BASE64",
        "PayloadType": "CONTENT",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

Replace the AWS Region, account ID, topic name, and IAM role name with your values. This example publishes the full email as Base64-encoded content. `DROP` stops rule-set processing for the selected recipients after a customer configuration failure.

##### Failure behavior
<a name="eb-rules-actions-publish-to-sns-failures"></a>

Customer configuration failures include the following:
+ Mail Manager cannot assume the execution role.
+ The topic does not exist.
+ The execution role lacks `sns:Publish`.
+ The encrypted topic's AWS KMS key is missing, disabled, inaccessible, or not configured for the role.
+ The email exceeds the 150 KiB `CONTENT` limit.
+ Amazon SNS rejects the request with a client error, including a notification that exceeds the topic's message-size limit.

For these failures, `CONTINUE` records the action as failed and runs later actions and rules for the selected recipients. `DROP` records the action as failed and stops rule-set processing for the selected recipients. `DROP` does not retry the failed action.

Amazon SNS service faults, timeouts, and other retriable service failures use the separate rule-set execution retry path. `ActionFailurePolicy` does not control those failures.

The action uses one publish request for the selected recipient group. It does not report separate success or failure for each recipient.

##### Recommendations
<a name="eb-rules-actions-publish-to-sns-recommendations"></a>
+ Use `HEADERS` when subscribers need message metadata and headers but must not receive the body or attachments.
+ Use `BASE64` when subscribers must preserve the complete MIME email without character conversion.
+ Check `mail.headersTruncated` before depending on the extracted header list.
+ Place Add header before Publish to SNS when subscribers need the added header.
+ Restrict topic publishing and subscription permissions because `CONTENT` can expose the complete email to every subscriber.
+ Use `DROP` when later processing must not continue after a customer configuration failure.
+ Use a standard Amazon SNS topic in the same Region and account as the rule set.

##### Notes
<a name="eb-rules-actions-publish-to-sns-notes"></a>

**Store larger email before publishing metadata**  
With `CONTENT`, the action fails with a customer configuration error when the email exceeds 150 KiB after earlier header changes. When an integration must retain a larger email, place Write to S3 before Publish to SNS and use `HEADERS`. The S3 object contains the complete MIME email, and the Amazon SNS notification contains its metadata and headers.

**Action completion**  
A successful action means that Amazon SNS accepted and stored the publish request. It does not confirm that every subscriber successfully processed the notification.

**Header and content limits**  
The 20 KiB and 100 KiB limits apply to the extracted `mail.headers` list. With `CONTENT`, the separate `content` field contains the complete MIME email, subject to the 150 KiB content limit.

##### API reference
<a name="eb-rules-actions-publish-to-sns-api"></a>
+ [SnsAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_SnsAction.html)
+ [CreateRuleSet](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateRuleSet.html)
+ [AWS CLI`mailmanager create-rule-set`](https://docs.aws.amazon.com/cli/latest/reference/mailmanager/create-rule-set.html)
+ [Amazon SNS Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html)

#### Invoke Lambda function
<a name="eb-rules-actions-invoke-lambda"></a>

The *Invoke Lambda function* action sends information about the selected email and recipients to an AWS Lambda function. Use it to run application logic or to control whether rule-set processing continues.

The action sends one event containing email metadata, headers, authentication results, and the selected recipients. The event does not contain the email body. Headers added by an earlier action are included in the event.

The following example shows the event for an `EVENT` invocation after an earlier action adds `X-Route: orders`. Fields without values are omitted:

```json
{
  "Records": [
    {
      "eventSource": "aws:ses",
      "eventVersion": "1.0",
      "ses": {
        "mail": {
          "timestamp": "2026-11-14T18:30:00.000Z",
          "messageId": "010001example-message-id",
          "source": "sender@example.net",
          "destination": [
            "orders@example.com"
          ],
          "headersTruncated": false,
          "commonHeadersTruncated": false,
          "headers": [
            {
              "name": "X-Route",
              "value": "orders"
            },
            {
              "name": "From",
              "value": "sender@example.net"
            },
            {
              "name": "To",
              "value": "orders@example.com"
            },
            {
              "name": "Subject",
              "value": "New order"
            }
          ],
          "commonHeaders": {
            "from": [
              "sender@example.net"
            ],
            "to": [
              "orders@example.com"
            ],
            "subject": "New order"
          }
        },
        "receipt": {
          "timestamp": "2026-11-14T18:30:00.000Z",
          "recipients": [
            "orders@example.com"
          ],
          "type": "Lambda",
          "action": {
            "functionArn": "arn:aws:lambda:us-east-1:111122223333:function:ProcessInboundEmail",
            "invocationType": "Event"
          },
          "processingTimeMillis": 0,
          "spamVerdict": {
            "status": "PASS"
          },
          "virusVerdict": {
            "status": "PASS"
          },
          "spfVerdict": {
            "status": "PASS"
          },
          "dkimVerdict": {
            "status": "PASS"
          },
          "dmarcVerdict": {
            "status": "PASS"
          }
        }
      }
    }
  ]
}
```

For a `REQUEST_RESPONSE` invocation, `receipt.action.invocationType` is `RequestResponse`. The event does not contain a `content` field. Invoke Lambda uses the SES email receiving Lambda event format. In this format, `mail.destination` contains addresses from the email's `To` and `CC` headers, with display names removed. Use `receipt.recipients` to identify the SMTP envelope recipients selected by the rule. Values in `mail.headers` are unfolded and MIME-decoded.

For the complete event structure, see [Lambda action event object](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda-event.html#receiving-email-action-lambda-event-lambdaaction). This compatibility applies to Invoke Lambda. Publish to SNS uses the Mail Manager SNS payload format described in [Behavior and ordering effects](#eb-rules-actions-publish-to-sns-behavior).

##### Choosing an invocation type
<a name="eb-rules-actions-invoke-lambda-invocation-type"></a>

Choose one of the following invocation types:

`EVENT`  
Invokes the function asynchronously. Rule-set processing continues after Lambda accepts the invocation. It does not wait for the function to finish or use its response.

`REQUEST_RESPONSE`  
Invokes the function synchronously. Rule-set processing waits for the function's response and applies its returned disposition.

Use `EVENT` when the function processes metadata without controlling later actions. Use `REQUEST_RESPONSE` only when the function must control rule processing.

For `REQUEST_RESPONSE`, return a JSON object containing one of the following dispositions:

`CONTINUE`  

```json
{"disposition": "CONTINUE"}
```
Runs the next action and later rules for the selected recipients.

`STOP_RULE`  

```json
{"disposition": "STOP_RULE"}
```
Skips the remaining actions in the current rule for the selected recipients. Later rules can still process those recipients.

`STOP_RULE_SET`  

```json
{"disposition": "STOP_RULE_SET"}
```
Stops all remaining rule-set processing for the selected recipients.

A missing disposition, an empty response, or an unrecognized response is treated as `CONTINUE`. A function error is treated as an invocation failure rather than a disposition.

##### Configuration fields and limits
<a name="eb-rules-actions-invoke-lambda-configuration"></a>

Function ARN  
Required. Specify a Lambda function in the same AWS partition, Region, and account as the rule set. The ARN length is 20–2,048 characters.

Invocation type  
Required. Valid values are `EVENT` and `REQUEST_RESPONSE`.

IAM role ARN  
Required. Specify the execution role that Mail Manager assumes when invoking the function. The ARN length is 20–2,048 characters.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`.

Retry time in minutes  
Optional. Valid values are 0–2,160 minutes. If omitted, the retry period is 2,160 minutes, or 36 hours. `RetryTimeMinutes` controls retries for `REQUEST_RESPONSE` invocations. `EVENT` invocation failures use the standard rule-set execution retry path.

A synchronous function must return within 30 seconds. A timeout or retriable function failure can cause another invocation.

##### Required permissions
<a name="eb-rules-actions-invoke-lambda-permissions"></a>

The principal that creates or updates the rule set needs permission for the corresponding Mail Manager rule-set operation and `iam:PassRole` permission for the role specified by `RoleArn`.

The rule action's IAM role must trust the SES service principal and allow `lambda:InvokeFunction` on the configured function. For the trust policy, see [Permission and trust polices to execute rule actions](eb-policies.md#eb-policies-rule-action). For the function permission, see [Permission policy for *Invoke Lambda function* rule action](eb-policies.md#eb-policies-lambda).

##### Creating an Invoke Lambda function action with the AWS CLI
<a name="eb-rules-actions-invoke-lambda-cli"></a>

The following command creates a rule set containing one asynchronous Lambda action. Replace the AWS Region, account ID, function name, and IAM role name with your values:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{invoke-lambda-example}} \
  --rules '[{
    "Name": "invoke-lambda",
    "Actions": [{
      "InvokeLambda": {
        "FunctionArn": "arn:aws:lambda:{{us-east-1}}:{{123456789012}}:function:{{ProcessInboundEmail}}",
        "InvocationType": "EVENT",
        "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{MailManagerLambdaActionRole}}",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

The command uses `EVENT` invocation and stops rule-set processing for the selected recipients after a customer configuration failure.

##### Recommendations
<a name="eb-rules-actions-invoke-lambda-recommendations"></a>
+ Use `EVENT` unless the function must control whether later actions or rules run.
+ Make the function idempotent because a retriable failure can invoke it more than once.
+ Keep `REQUEST_RESPONSE` processing below 30 seconds.
+ Add headers before Invoke Lambda function when the function needs those headers.
+ Write the email to S3 before Invoke Lambda function when the function needs the email body. The Lambda event contains the message ID but not the body.
+ Return an explicit disposition from `REQUEST_RESPONSE` functions. Do not depend on an invalid response being treated as `CONTINUE`.
+ Use `DROP` as the action failure policy only when later processing must stop after a permanent function or configuration failure.

**Retries and action completion**  
With `EVENT`, a successful action means that Lambda accepted the asynchronous invocation. It does not confirm that the function completed successfully.  
`ActionFailurePolicy` applies immediately to permanent failures, such as a missing function or insufficient permission. Retriable `REQUEST_RESPONSE` failures use the retry period first. The failure policy applies after that period expires.

For complete field constraints, see [InvokeLambdaAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_InvokeLambdaAction.html) in the *SES Mail Manager API Reference*.

#### Deliver to Q Business
<a name="eb-rules-actions-deliver-to-q-business"></a>

The *Deliver to Q Business* action converts the email body and supported attachments into documents and adds them to an Amazon Q Business index.

The action creates separate documents for the body and each supported attachment. Document IDs use the Mail Manager message ID:

```
Email body:
<message-id>_body

First attachment:
<message-id>_attachment1

Second attachment:
<message-id>_attachment2
```

Each document can include `Subject`, `From`, and `To` attributes. Attachment documents can also include `FileName` and `FileSize`.

##### Email body and attachment handling
<a name="eb-rules-actions-deliver-to-q-business-content"></a>

The plain-text email body becomes one `PLAIN_TEXT` document. Text attachments can become additional documents. Supported MIME content types include `text/csv`, `text/html`, `text/plain`, `text/xml`, `text/markdown`, `text/richtext`, and `text/rtf`. Other `text/*` attachments are submitted as `PLAIN_TEXT`.

Non-text attachments are skipped. For example, the body of an email with a PDF attachment is indexed, but the PDF is not:

```
Email:
Body: indexed as <message-id>_body
Attachment: invoice.pdf

Result:
Body indexed
invoice.pdf skipped
```

##### Document limits
<a name="eb-rules-actions-deliver-to-q-business-document-limits"></a>
+ The action submits up to 10 documents per email.
+ The body counts as one document.
+ When the email has a body, up to nine supported attachments can be submitted.
+ Each attachment can contain up to 5 MiB (5,242,880 bytes).
+ Attachments above 5 MiB are skipped.
+ Only the first five addresses from the visible `To` header are included in the Q Business `To` attribute.

If an email contains more supported attachments than the document limit, additional attachments are skipped.

##### Message headers and recipients
<a name="eb-rules-actions-deliver-to-q-business-message-data"></a>

The Q Business document attributes use the email's visible MIME headers. The `To` attribute does not use the SMTP envelope recipient list. A preceding Replace recipient action changes SMTP envelope recipients but does not change the Q Business `To` attribute:

```
Visible To header:
support@example.com

Envelope recipient after replacement:
processing@example.net

Q Business To attribute:
support@example.com
```

The current Q Business conversion reads the original MIME message. Headers added by an earlier Add header action are not included as Q Business document attributes or content.

##### Configuration fields and limits
<a name="eb-rules-actions-deliver-to-q-business-configuration"></a>

Application ID  
Required. The Q Business application ID must contain exactly 36 lowercase letters, numbers, and hyphens.

Index ID  
Required. The Q Business index ID must contain exactly 36 lowercase letters, numbers, and hyphens.

IAM role ARN  
Required. The role grants access to the application and index. The ARN contains from 20 through 2,048 characters.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`.

The action is available only in Regions enabled for the Mail Manager Q Business integration. Rule-set creation validates field formats and regional availability. It does not verify that the application and index exist.

##### Required permissions
<a name="eb-rules-actions-deliver-to-q-business-permissions"></a>

The principal that creates or updates the rule set needs permission for the corresponding Mail Manager rule-set operation and `iam:PassRole` permission for the role specified by `RoleArn`.

The rule action's IAM role must trust the SES service principal and allow `qbusiness:BatchPutDocument` on the configured application and index. The role needs the documented AWS KMS permissions when the Q Business index uses a customer managed key.

For the trust policy, see [Permission and trust polices to execute rule actions](eb-policies.md#eb-policies-rule-action). For the Q Business and AWS KMS policies, see [Permission policy for *Deliver to Q Business* rule action](eb-policies.md#eb-policies-q).

##### Creating a Deliver to Q Business action with the AWS CLI
<a name="eb-rules-actions-deliver-to-q-business-cli"></a>

The following command creates a rule set that adds email documents to a Q Business index. Replace the AWS Region, application ID, index ID, account ID, role name, and rule set name with your values:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{q-business-example}} \
  --rules '[{
    "Name": "index-support-email",
    "Actions": [{
      "DeliverToQBusiness": {
        "ApplicationId": "{{a1b2c3d4-e5f6-7890-abcd-ef1234567890}}",
        "IndexId": "{{01234567-89ab-cdef-0123-456789abcdef}}",
        "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{MailManagerQBusinessActionRole}}",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

##### Failure behavior
<a name="eb-rules-actions-deliver-to-q-business-failures"></a>

A role assumption failure, a Q Business authorization or resource error, invalid MIME content, or rejection of every submitted document is a customer configuration error. `DROP` stops rule-set processing for the selected recipients. `CONTINUE` runs later actions and rules. Service errors use the separate execution retry path.

A partial document failure does not fail the action. If at least one document succeeds, the action completes successfully. Unsupported attachments, attachments above 5 MiB, and documents above the 10-document limit are skipped before the request. These skips do not apply `ActionFailurePolicy`.

##### Recommendations
<a name="eb-rules-actions-deliver-to-q-business-recommendations"></a>
+ Use `DROP` when later processing must not continue if every Q Business document fails.
+ Keep important information in the plain-text body because unsupported attachments are skipped.
+ Convert PDF or binary content to a supported text format before ingestion.
+ Keep each text attachment at or below 5 MiB.
+ Keep the body and supported attachments within the 10-document total.
+ Do not depend on `ActionFailurePolicy` to detect skipped or partially failed attachments.
+ Use the visible `To`, `From`, and `Subject` headers for metadata that Q Business must index.

**Partial ingestion can still report success**  
If the email body and one attachment succeed but another attachment fails, the action completes successfully. The configured `ActionFailurePolicy` does not stop later rule-set processing.

For complete field constraints, see [DeliverToQBusinessAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeliverToQBusinessAction.html) in the *SES Mail Manager API Reference*.

### Actions that deliver email
<a name="eb-rules-actions-reference-deliver"></a>

#### SMTP relay
<a name="eb-rules-actions-relay"></a>

The *SMTP relay* action forwards the email and selected recipients to an existing Mail Manager relay. The relay connects to the external mail server configured in the relay resource.

Simple Mail Transfer Protocol (SMTP) is the protocol that mail servers use to transfer email. Create the relay before referencing it in a rule action. For relay setup, authentication, and supported external mail servers, see [SMTP relay](eb-relay.md).

##### How relay processing works
<a name="eb-rules-actions-relay-processing"></a>

The action sends the current email content and selected recipients to the configured relay. Headers added by earlier actions are included:

```
Actions:
1. Add header X-Route: corporate
2. Relay through CorporateRelay
```

The external mail server receives the `X-Route: corporate` header.

Rule-set processing waits for a final outcome for every selected recipient. A recipient can be delivered successfully, bounced, or rejected by the destination. A temporary delivery-delay notification does not complete the action. Processing waits for a later delivery or failure outcome.

For CloudWatch metrics that count final delivery and rejection outcomes by relay ID, see [CloudWatch metrics for rule sets and SMTP relays](eb-rules-monitoring.md#eb-rules-monitoring-cloudwatch-metrics).

##### Choosing the SMTP envelope sender
<a name="eb-rules-actions-relay-mail-from"></a>

The SMTP envelope sender is the address that mail servers use for delivery-status responses. It can differ from the address displayed in the email's `From` header.

The `MailFrom` field controls the envelope sender used for the relay:

`REPLACE`  
Uses a Mail Manager address associated with the message ID. This is the default.

`PRESERVE`  
Uses the original SMTP envelope sender when one is present.

**REPLACE example**  
Suppose the original SMTP envelope sender is `returns@example.org`, the visible `From` header is `Alice <alice@example.org>`, and the Mail Manager message ID is `6e33e183-2d6f-418a-a6fa-0cf5ae87dc80`. With `REPLACE`, the relay uses a generated envelope sender such as:

```
6e33e183-2d6f-418a-a6fa-0cf5ae87dc80@feedback.examplehash.mail-manager-smtp.amazonaws.com
```

**PRESERVE example**  
With `PRESERVE`, the relay uses the original envelope sender:

```
returns@example.org
```

In both examples, the visible `From` header remains `Alice <alice@example.org>`. If the original SMTP envelope sender is empty, `PRESERVE` uses a generated Mail Manager address instead.

This setting does not replace the visible `From` header. Use `REPLACE` unless the destination mail server requires the original SMTP envelope sender. Use `PRESERVE` only when the destination accepts and correctly processes that address.

##### Configuration fields and limits
<a name="eb-rules-actions-relay-configuration"></a>

Relay  
Required. Specify the ID or ARN of an existing relay. The value contains from 1 through 2,048 characters. Rule-set creation or update fails if the relay does not exist in the account.

Mail from  
Optional. Valid values are `REPLACE` and `PRESERVE`. If omitted, processing uses `REPLACE`.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`.

The SMTP server name, port, authentication, secret, and encryption settings belong to the relay resource rather than the rule action.

##### Required permissions
<a name="eb-rules-actions-relay-permissions"></a>

The SMTP relay action does not contain an IAM role and does not require `iam:PassRole`. The principal creating or updating the rule set needs permission for `ses:CreateRuleSet` or `ses:UpdateRuleSet`.

An authenticated relay can require an AWS Secrets Manager resource policy that allows SES to read the relay credentials and an AWS KMS key policy that allows SES to decrypt the secret. For relay creation, see [Creating an SMTP relay in the SES console](eb-relay.md#eb-relay-create-console). For the credential and key policies, see [Permission policies for SMTP relay](eb-policies.md#eb-policies-relay).

##### Creating an SMTP relay action with the AWS CLI
<a name="eb-rules-actions-relay-cli"></a>

The following command creates a rule set that uses the existing relay `rl-0123456789abcdef`. Replace the AWS Region, relay ID, and rule set name with your values:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{smtp-relay-example}} \
  --rules '[{
    "Name": "relay-orders",
    "Actions": [{
      "Relay": {
        "Relay": "{{rl-0123456789abcdef}}",
        "MailFrom": "REPLACE",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

##### Failure behavior
<a name="eb-rules-actions-relay-failures"></a>

A relay can fail before delivery starts when the referenced relay has been deleted, an unauthenticated relay uses an unverified recipient domain, or the email is malformed. The destination can also deliver some recipients and reject others.

`ActionFailurePolicy` controls which recipients continue after the final delivery outcomes:

`CONTINUE`  
Keeps all selected recipients available to later actions and rules, including recipients that the destination rejected.

`DROP`  
Stops rule-set processing for recipients that the destination rejected. Recipients delivered successfully remain available to later actions and rules.

The action is recorded as failed when at least one selected recipient is rejected, even when other recipients are delivered.

##### Recommendations
<a name="eb-rules-actions-relay-recommendations"></a>
+ Use `REPLACE` unless preserving the original SMTP envelope sender is required.
+ Put Add header before SMTP relay when the destination must receive the added header.
+ Use `DROP` when a destination rejection must stop processing for that recipient.
+ Use `CONTINUE` when another later action must process recipients that the relay rejected.
+ Configure authentication when the destination server requires credentials.
+ For an unauthenticated relay, verify every intended recipient identity as described in [SMTP relay](eb-relay.md).

**A later relay is not a failure-only fallback**  
With `CONTINUE`, every selected recipient continues to the next action. This includes recipients that the first relay delivered successfully.  
For example, suppose `PrimaryRelay` delivers `user1@example.com` but rejects `user2@example.com`. If `BackupRelay` is the next action, both recipients continue to it. This can deliver a duplicate email to `user1@example.com`. Do not use consecutive relay actions as an automatic failure-only fallback unless duplicate delivery is acceptable or different rules separate the recipients.

For complete field constraints, see [RelayAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RelayAction.html) in the *SES Mail Manager API Reference*.

#### Send to internet
<a name="eb-rules-actions-send"></a>

The *Send to internet* action uses SES to send the email to the recipients currently selected by the rule. Use this action to deliver accepted email to external addresses through the SES outbound delivery service.

The action sends the complete MIME email, including its headers, body, and attachments. SES applies the sending limits, identity requirements, and delivery controls of the account associated with the execution role.

##### Recipient and message handling
<a name="eb-rules-actions-send-recipients"></a>

The action sends to the current SMTP envelope recipients. Earlier Replace recipient actions change these destination addresses.

```
Selected recipient: orders@example.com

Actions:
1. Replace recipient with processing@example.net
2. Send to internet
```

The action sends the email to `processing@example.net`. Replacing the envelope recipient does not change the address displayed in the email's `To` or `CC` header.

Earlier Add header actions change the MIME email sent to recipients:

```
Actions:
1. Add header X-Route: orders
2. Send to internet

Delivered header:
X-Route: orders
```

Mail Manager passes the selected recipients to SES as destination addresses. These addresses are not added to the visible `To` or `CC` headers.

SES accepts at most 50 recipients in one send request. When more than 50 recipients are selected, the action divides them into groups of at most 50 and sends each group sequentially. Each group receives a separate SES message ID.

##### Changes made before sending
<a name="eb-rules-actions-send-message-changes"></a>

Before sending, the action:
+ Applies headers added by earlier actions.
+ Removes existing `DKIM-Signature` headers so SES can sign the outbound email.
+ Removes the original `Return-Path` header.
+ Sends the resulting message as raw MIME content.

SES supplies its own `Message-ID` and `Date` headers during outbound delivery.

##### Configuration fields
<a name="eb-rules-actions-send-configuration"></a>

IAM role ARN  
Required. Specify the execution role that Mail Manager assumes when sending the email. The ARN must contain 20–2,048 characters. The role must be in the rule set's account because `iam:PassRole` applies only within one account.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`.  
`CONTINUE` runs later actions and rules after a customer configuration failure, even though the email was not sent. `DROP` stops rule-set processing for the selected recipients after a customer configuration failure.  
Use `DROP` when later processing depends on successful outbound delivery. For complete behavior, see [Handling an action failure](#eb-rules-actions-failure-policy).

##### Sending requirements and limits
<a name="eb-rules-actions-send-requirements"></a>

The email must meet the SES raw-message requirements:
+ The `From` address or domain must be a verified identity in the account used by the execution role.
+ The message must contain valid MIME headers and a body separated by a blank line.
+ Each line can contain at most 1,000 characters, including the line ending.
+ The complete encoded message, including attachments, can contain up to 40 MB.
+ SES sending quotas and account-level sending controls apply. For details, see [Managing your SES sending limits](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html).
+ While the account is in the SES sandbox, recipients must be verified addresses or SES mailbox simulator addresses. See [Requesting production access](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html) and [Using the mailbox simulator](https://docs.aws.amazon.com/ses/latest/dg/test-email-sending.html#send-email-simulator).

##### Required permissions
<a name="eb-rules-actions-send-permissions"></a>

The principal that creates or updates the rule set needs permission for the corresponding Mail Manager rule-set operation and `iam:PassRole` permission for the role specified by `RoleArn`.

The execution role must trust the SES service principal and allow `ses:SendEmail` and `ses:SendRawEmail` for the sending identity. Include the configuration-set resource when the sending identity uses a default configuration set.

For the trust policy, see [Permission and trust polices to execute rule actions](eb-policies.md#eb-policies-rule-action). For the sending permissions, see [Permission policy for *Send to internet* rule action](eb-policies.md#eb-policies-internet).

##### Creating a Send to internet action with the AWS CLI
<a name="eb-rules-actions-send-cli"></a>

The following command creates a rule set with one Send to internet action:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{send-to-internet-example}} \
  --rules '[{
    "Name": "send-external-email",
    "Actions": [{
      "Send": {
        "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{MailManagerSendActionRole}}",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

Replace the AWS Region, account ID, and IAM role name with your values. The example stops rule-set processing for the selected recipients after a customer configuration failure.

##### Failure behavior
<a name="eb-rules-actions-send-failures"></a>

Customer configuration failures include the following:
+ Mail Manager cannot assume the execution role.
+ The execution role lacks permission to send.
+ The sending identity is not verified.
+ Sending is paused or the account is suspended.
+ SES rejects the message because its content or parameters are invalid.

For these failures, `ActionFailurePolicy` controls whether processing continues.

Sending-rate throttling, account resource limits, SES service faults, and other retriable failures use the separate rule-set execution retry path. `ActionFailurePolicy` does not control these failures.

##### Recommendations
<a name="eb-rules-actions-send-recommendations"></a>
+ Verify the identity in the `From` header before using this action. For instructions, see [Creating and verifying identities in SES](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html).
+ Place Replace recipient before Send to internet when delivery must use replacement addresses.
+ Place Add header before Send to internet when recipients must receive the added header.
+ Use `DROP` when later processing must not continue after outbound delivery fails because of customer configuration.
+ Ensure that the execution role permits both the sending identity and its default configuration set, when applicable.
+ Keep the MIME message within the SES raw-message limits.

##### API reference
<a name="eb-rules-actions-send-api"></a>
+ [SendAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_SendAction.html)
+ [SES API v2 SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html)
+ [RawMessage](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_RawMessage.html)
+ [AWS CLI`mailmanager create-rule-set`](https://docs.aws.amazon.com/cli/latest/reference/mailmanager/create-rule-set.html)

#### Deliver to WorkMail mailbox
<a name="eb-rules-actions-deliver-to-mailbox"></a>

The *Deliver to WorkMail mailbox* action delivers the email to selected recipients in an Amazon WorkMail organization. The `MailboxArn` field identifies the WorkMail organization. Individual recipients come from the rule's selected SMTP envelope recipients.

```
Selected recipient:
employee@example.com

WorkMail organization:
arn:aws:workmail:us-east-1:123456789012:organization/m-0123456789abcdef0123456789abcdef
```

The action verifies that `employee@example.com` belongs to the configured organization before delivery.

##### Recipient handling
<a name="eb-rules-actions-deliver-to-mailbox-recipients"></a>

Each selected recipient is checked separately. A recipient in the configured WorkMail organization receives the email. A recipient in another organization is not delivered to that WorkMail organization. When the SMTP envelope sender is present, the action attempts to send a bounce for an invalid recipient. When the SMTP envelope sender is empty, the action does not send a bounce.

Use Replace recipient before this action when an incoming address must map to a WorkMail address:

```
Matched recipient:
support@example.net

Actions:
1. Replace recipient with support@example.com
2. Deliver to WorkMail mailbox
```

The WorkMail action validates and delivers `support@example.com`.

Headers added by earlier actions are included in the delivered email:

```
Actions:
1. Add header X-Route: workmail
2. Deliver to WorkMail mailbox
```

##### Configuration fields and limits
<a name="eb-rules-actions-deliver-to-mailbox-configuration"></a>

Mailbox ARN  
Required. Specify a WorkMail organization ARN. The value contains from 1 through 2,048 characters.

IAM role ARN  
Required. Specify the execution role used to call WorkMail. The value contains from 20 through 2,048 characters.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`.

The WorkMail organization must be in a Region where WorkMail and this action are supported. It must be in the same Region as the rule set and use an organization ID beginning with `m-`. The organization and IAM role must belong to the same account.

##### Required permissions
<a name="eb-rules-actions-deliver-to-mailbox-permissions"></a>

The principal that creates or updates the rule set needs permission for the corresponding Mail Manager rule-set operation and `iam:PassRole` permission for the role specified by `RoleArn`.

The rule action's IAM role must trust the SES service principal and allow `workmail:DeliverToMailbox` on the configured WorkMail organization. For the trust policy, see [Permission and trust polices to execute rule actions](eb-policies.md#eb-policies-rule-action). For the WorkMail permission policy, see [Permission policy for *Deliver to mailbox* rule action](eb-policies.md#eb-policies-workmail).

##### Creating a Deliver to WorkMail mailbox action with the AWS CLI
<a name="eb-rules-actions-deliver-to-mailbox-cli"></a>

The following command creates a rule set that delivers selected recipients to a WorkMail organization. Replace the AWS Region, account ID, organization ID, role name, and rule set name with your values:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{workmail-delivery-example}} \
  --rules '[{
    "Name": "deliver-workmail",
    "Actions": [{
      "DeliverToMailbox": {
        "MailboxArn": "arn:aws:workmail:{{us-east-1}}:{{123456789012}}:organization/{{m-0123456789abcdef0123456789abcdef}}",
        "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{MailManagerWorkMailActionRole}}",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

##### Failure behavior
<a name="eb-rules-actions-deliver-to-mailbox-failures"></a>

Permission failures and WorkMail API errors are customer configuration errors. `CONTINUE` runs later actions and rules for the selected recipients. `DROP` stops rule-set processing for the selected recipients. Retriable failures in the delivery path use the separate execution retry path.

A recipient that does not belong to the configured WorkMail organization is not delivered, and a bounce is attempted when the SMTP envelope sender is present. This recipient-level outcome does not fail the entire action.

##### Recommendations
<a name="eb-rules-actions-deliver-to-mailbox-recommendations"></a>
+ Use a `RECIPIENT` condition to select intended WorkMail recipients.
+ Use Replace recipient before WorkMail delivery when inbound addresses differ from WorkMail addresses.
+ Put Add header before WorkMail delivery when the mailbox must receive the added header.
+ Use `DROP` when later processing must not continue after an authorization or WorkMail configuration error.
+ Confirm that the organization and execution role belong to the same account.
+ Confirm that the WorkMail organization is in the rule set's Region.

**Invalid recipients can continue to later actions**  
A recipient that does not belong to the WorkMail organization is not removed from the rule-set recipient list by this action. Later actions and rules can still process that recipient.  
Use explicit conditions or a later Drop action when invalid WorkMail recipients must not continue.

For complete field constraints, see [DeliverToMailboxAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeliverToMailboxAction.html) in the *SES Mail Manager API Reference*.

### Actions that respond or stop processing
<a name="eb-rules-actions-reference-respond-stop"></a>

#### Drop
<a name="eb-rules-actions-drop"></a>

The *Drop* action stops rule-set processing for the recipients selected by the rule. Use this action when Mail Manager must take no more actions for those recipients.

Drop does not send a response to the sender. Use Bounce before Drop when the sender must receive a delivery-status notification.

##### Recipient and processing behavior
<a name="eb-rules-actions-drop-behavior"></a>

Drop removes only the selected SMTP envelope recipients from further rule-set processing. Later actions in the current rule and all later rules do not run for those recipients.

Other recipients continue through the rule set.

```
Current recipients:
blocked@example.com
allowed@example.com

Selected recipient:
blocked@example.com

Actions:
1. Drop
2. Send to internet
```

Drop stops processing for `blocked@example.com`. Send to internet does not run for that recipient. Because the rule did not select `allowed@example.com`, that recipient remains available to later rules.

When Drop removes every remaining recipient, rule-set processing ends.

##### Effect on earlier actions
<a name="eb-rules-actions-drop-order"></a>

Drop does not reverse actions that already completed.

```
Actions:
1. Write to S3 bucket blocked-mail-example
2. Bounce
3. Drop
```

Write to S3 retains the email, Bounce sends a delivery-status notification, and Drop then stops further processing for the selected recipients.

Place Drop after every storage, delivery, notification, or processing action that must still run.

##### Configuration
<a name="eb-rules-actions-drop-configuration"></a>

Drop has no configuration fields. It does not accept an IAM role ARN, `ActionFailurePolicy`, a message or response, or a destination resource.

The rule's `Conditions` and `Unless` lists determine which recipients the action drops.

##### Creating a Drop action with the AWS CLI
<a name="eb-rules-actions-drop-cli"></a>

The following command creates a rule set that drops only `blocked@example.com`:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{drop-example}} \
  --rules '[{
    "Name": "drop-blocked-recipient",
    "Conditions": [{
      "StringExpression": {
        "Evaluate": {
          "Attribute": "RECIPIENT"
        },
        "Operator": "EQUALS",
        "Values": [
          "blocked@example.com"
        ]
      }
    }],
    "Actions": [{
      "Drop": {}
    }]
  }]'
```

Replace the AWS Region, rule-set name, and recipient address with your values.

##### Failure behavior
<a name="eb-rules-actions-drop-failures"></a>

Drop runs locally as part of rule-set processing. It does not call another AWS service and has no customer resource configuration that can fail. `ActionFailurePolicy` does not apply to Drop.

##### Recommendations
<a name="eb-rules-actions-drop-recommendations"></a>
+ Place Drop last among the actions for the selected recipients.
+ Store or archive the email before Drop when a retained copy is required.
+ Place Bounce before Drop when the sender must receive a delivery-status notification.
+ Use recipient conditions to limit which recipients are dropped.
+ Review rules without conditions carefully because a Drop action in such a rule applies to every remaining recipient.
+ Use Drop without Bounce when the sender must not receive a response.

##### Notes
<a name="eb-rules-actions-drop-notes"></a>

**Accepted email**  
Drop stops Mail Manager rule-set processing. It does not reject the SMTP transaction that already accepted the email.

**Envelope recipients**  
Drop changes the active envelope recipient list. It does not rewrite addresses displayed in the email's `To` or `CC` headers.

##### API reference
<a name="eb-rules-actions-drop-api"></a>
+ [DropAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DropAction.html)
+ [CreateRuleSet](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_CreateRuleSet.html)
+ [AWS CLI`mailmanager create-rule-set`](https://docs.aws.amazon.com/cli/latest/reference/mailmanager/create-rule-set.html)

#### Bounce
<a name="eb-rules-actions-bounce"></a>

The *Bounce* action sends a delivery status notification, also called a bounce, to the sender of the received email. Use this action when the selected recipients cannot accept the email and the sender must receive the reason.

The bounce contains one failure entry for each recipient selected by the rule. It includes the configured SMTP reply code, enhanced status code, and diagnostic message.

##### Recipient and processing behavior
<a name="eb-rules-actions-bounce-behavior"></a>

The action sends one bounce message to the original SMTP envelope sender. The configured `Sender` address becomes the `From` address of the bounce.

```
Original sender: customer@example.net
Selected recipients:
orders@example.com
returns@example.com

Bounce sender: bounce@example.com
SMTP reply code: 550
Status code: 5.7.1
Diagnostic message: Delivery not authorized
```

The bounce sent to `customer@example.net` contains a failed delivery entry for both selected recipients:

```
Final-Recipient: rfc822; orders@example.com
Action: failed
Status: 5.7.1
Diagnostic-Code: smtp; 550 5.7.1 Delivery not authorized

Final-Recipient: rfc822; returns@example.com
Action: failed
Status: 5.7.1
Diagnostic-Code: smtp; 550 5.7.1 Delivery not authorized
```

An earlier Replace recipient action changes the recipients listed in the bounce because Bounce uses the current selected recipients.

A successful Bounce action does not stop later actions or rules. Add Drop after Bounce when processing must stop for the selected recipients:

```
Actions:
1. Bounce
2. Drop
```

**Preventing bounce loops**  
If the original message has an empty SMTP `MAIL FROM` value, the action does not send a bounce. An empty sender normally indicates that the received email is already a delivery status notification. The action completes successfully without sending another notification, which prevents a bounce loop.

##### Configuration fields
<a name="eb-rules-actions-bounce-configuration"></a>

IAM role ARN  
Required. Specify the execution role that Mail Manager assumes when sending the bounce. The ARN must contain 20–2,048 characters. The role must be in the rule set's account because `iam:PassRole` applies only within one account.

Sender  
Required. Specify the verified email address that appears in the bounce's `From` header. The address can contain up to 254 characters and must match the `local-part@domain` format.

SMTP reply code  
Required. Specify a three-digit code that starts with `4` or `5`. A `4xx` code identifies a temporary delivery failure. A `5xx` code identifies a permanent delivery failure. For example, `550` identifies a permanent failure.

Enhanced status code  
Required. Specify a code in `x.y.z` format that starts with `4` or `5`. The value must contain 5–9 characters. For example, `5.7.1` commonly identifies a permanent rejection caused by policy or authorization.  
Use an enhanced status code that is consistent with the SMTP reply code. Do not combine a temporary `4xx` SMTP code with a permanent `5.x.x` status code.

Diagnostic message  
Required. Specify the explanation included in the bounce's `Diagnostic-Code` field. The value must contain 1–256 printable ASCII characters.  

```
SMTP reply code: 550
Enhanced status code: 5.7.1
Diagnostic message: Delivery not authorized

Result:
Diagnostic-Code: smtp; 550 5.7.1 Delivery not authorized
```

Message  
Optional. Specify human-readable text for the bounce message. The value must contain 1–500 printable ASCII characters or line breaks.  
If you omit this field, SES generates explanatory text from the recipient delivery-status information.

Action failure policy  
Optional. Valid values are `CONTINUE` and `DROP`. If omitted, processing uses `CONTINUE`.  
`ActionFailurePolicy` applies only when sending the bounce fails. `CONTINUE` runs later actions and rules for the selected recipients. `DROP` stops rule-set processing for the selected recipients.  
A successful bounce does not activate `DROP`. Add a separate Drop action when processing must stop after a successful bounce. For complete failure-policy behavior, see [Handling an action failure](#eb-rules-actions-failure-policy).

##### Required permissions
<a name="eb-rules-actions-bounce-permissions"></a>

The principal that creates or updates the rule set needs permission for the corresponding Mail Manager rule-set operation and `iam:PassRole` permission for the role specified by `RoleArn`.

The execution role must trust the SES service principal and allow `ses:SendBounce` for the verified identity specified by `Sender`.

For the trust policy, see [Permission and trust polices to execute rule actions](eb-policies.md#eb-policies-rule-action). For the sending permission, see [Permission policy for *Bounce* rule action](eb-policies.md#eb-policies-bounce).

##### Creating a Bounce action with the AWS CLI
<a name="eb-rules-actions-bounce-cli"></a>

The following command creates a rule set with one Bounce action:

```bash
PROMPT> aws mailmanager create-rule-set \
  --region {{us-east-1}} \
  --rule-set-name {{bounce-example}} \
  --rules '[{
    "Name": "reject-unauthorized-mail",
    "Actions": [{
      "Bounce": {
        "RoleArn": "arn:aws:iam::{{123456789012}}:role/{{MailManagerBounceActionRole}}",
        "Sender": "{{bounce@example.com}}",
        "SmtpReplyCode": "550",
        "StatusCode": "5.7.1",
        "DiagnosticMessage": "Delivery not authorized",
        "Message": "Your message was rejected by the recipient policy.",
        "ActionFailurePolicy": "DROP"
      }
    }]
  }]'
```

Replace the AWS Region, account ID, role name, and sender address with your values. The sender address must be a verified SES identity.

##### Failure behavior
<a name="eb-rules-actions-bounce-failures"></a>

Customer configuration failures include the following:
+ Mail Manager cannot assume the execution role.
+ The execution role lacks `ses:SendBounce`.
+ The configured sender identity is not verified.
+ Sending is paused or the account is suspended.
+ SES rejects the bounce message or its parameters.

For these failures, `ActionFailurePolicy` controls whether processing continues.

SES throttling, resource limits, service faults, and other retriable failures use the separate rule-set execution retry path. `ActionFailurePolicy` does not control these failures.

Skipping a bounce because the original SMTP sender is empty is successful loop prevention, not a failure. The failure policy does not apply.

##### Recommendations
<a name="eb-rules-actions-bounce-recommendations"></a>
+ Use a verified address dedicated to delivery-status notifications as the bounce sender.
+ Use matching SMTP and enhanced status-code classes, such as `550` with `5.7.1`.
+ Write a diagnostic message that states the delivery problem without exposing internal system details.
+ Add Drop after Bounce when rule-set processing must stop after the notification is sent.
+ Use only Drop when the sender does not need a delivery-status notification.
+ Use `DROP` as the failure policy when later processing must not continue if sending the bounce fails.

##### Notes
<a name="eb-rules-actions-bounce-notes"></a>

**SendBounce limits**  
The underlying SES `SendBounce` operation can be used only for email received through SES and within 24 hours of receipt. The operation accepts no more than one request per second. Throttling uses the retriable service-failure path.

**Action completion**  
A successful action means that SES accepted the bounce request and returned a bounce message ID.

##### API reference
<a name="eb-rules-actions-bounce-api"></a>
+ [BounceAction](https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_BounceAction.html)
+ [SES SendBounce](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBounce.html)
+ [AWS CLI`mailmanager create-rule-set`](https://docs.aws.amazon.com/cli/latest/reference/mailmanager/create-rule-set.html)

## Handling an action failure
<a name="eb-rules-actions-failure-policy"></a>

The following actions support `ActionFailurePolicy`:
+ Write to S3
+ SMTP relay
+ Archive
+ Publish to SNS
+ Invoke Lambda function
+ Deliver to Q Business
+ Send to internet
+ Deliver to WorkMail mailbox
+ Bounce

The policy applies when the action reports a customer configuration error. Examples include a deleted resource, an invalid resource, or insufficient permission to use the configured resource.

`CONTINUE`  
Records the action as failed and continues to the next action with the same selected recipients.

`DROP`  
Records the action as failed and stops rule-set processing for its selected recipients. Later actions and later rules do not run for those recipients.

If you omit `ActionFailurePolicy`, processing uses `CONTINUE`.

`ActionFailurePolicy` does not control service faults or action timeouts. Those failures are handled separately and can cause the execution to retry or fail.

**Use DROP when later processing depends on action success**  
`CONTINUE` runs later actions and later rules for the selected recipients after an action fails with a customer configuration error. Use `DROP` when later processing must not continue unless the action completes successfully.  
`DROP` does not retry the failed action. Retriable service errors use the separate execution retry path regardless of the configured `ActionFailurePolicy`.

**Continue after a storage failure**  
If the S3 bucket in this example no longer exists, the first action fails with a customer configuration error. Processing continues to Relay for the selected recipients.

```
Action 1: Write to S3 bucket deleted-orders-example
          ActionFailurePolicy: CONTINUE
Action 2: Relay through CorporateRelay
```

**Drop recipients after a bounce failure**  
If the bounce sender identity in this example is not verified, Bounce fails with a customer configuration error. `DROP` stops rule-set processing for the selected recipients, so Write to S3 does not run for them.

```
Action 1: Bounce from bounce@invalid-unverified-domain.example
          ActionFailurePolicy: DROP
Action 2: Write to S3 bucket failed-bounces-example
```

## Choosing action order
<a name="eb-rules-actions-choose-order"></a>

Use the following guidelines when ordering actions:
+ Modify the email before storing or delivering it when the destination must receive the modification.
+ Replace recipients before a storage or delivery action that must use the replacement addresses.
+ Archive or write to S3 before Drop when you need to retain the email.
+ Put Bounce before Drop when you need to notify the sender and then stop processing the selected recipients.
+ Put Drop after every action that must still run for the selected recipients.
+ Select `CONTINUE` when later actions must run after a customer configuration error.
+ Select `DROP` when later actions and rules must not process recipients affected by that error.

**Archive and deliver**  
The Archive action in this example retains a copy before the SMTP relay delivers the email to the configured mail server.

```
Actions:
1. Archive in ComplianceArchive
2. Relay through CorporateRelay
```

## Common rule-action scenarios
<a name="eb-rules-actions-scenarios"></a>

The following scenarios show how ordered actions and rules can form an email processing workflow. Adapt the conditions, resource names, and destinations to your environment.

### Isolate unsafe email and deliver clean email
<a name="eb-rules-actions-scenarios-security"></a>

Use an early rule to retain and stop email identified by a security add-on. Use a later rule to archive and deliver recipients that remain:

```
Rule 1: Scan and isolate
Condition:
Security add-on result identifies scam, suspect, phishing, or malware content
Actions:
1. Add header X-Security-Result: failed
2. Write to S3 bucket mail-quarantine-example
3. Drop

Rule 2: Archive and deliver clean email
Conditions:
None
Actions:
1. Add header X-Security-Result: approved
2. Archive in ComplianceArchive
3. Send to internet
```

Drop stops processing for recipients selected by Rule 1. Those recipients do not reach Rule 2. Recipients not selected by Rule 1 continue to Rule 2, where the email is marked, archived, and sent.

For a walkthrough of this pattern, see [Streamlining outbound emails with SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/streamlining-outbound-emails-with-amazon-ses-mail-manager/).

### Archive email before delivery to an existing mail server
<a name="eb-rules-actions-scenarios-archive-relay"></a>

Place Archive before SMTP relay to retain the email while it is in transit and then deliver it to your existing mail server:

```
Rule: Archive inbound email
Conditions:
None
Actions:
1. Archive in ComplianceArchive
2. Relay through CorporateRelay
```

This order retains the email before the relay attempts delivery. For an in-transit archiving example, see [Archiving and sending to final SMTP server](https://aws.amazon.com/blogs/messaging-and-targeting/archiving-and-sending-to-final-smtp-server/).

### Route recipients during a mailbox migration
<a name="eb-rules-actions-scenarios-hybrid-routing"></a>

Use recipient conditions in separate rules to route addresses to different mail platforms during hybrid operation or migration:

```
Rule 1: Route on-premises recipients
Condition:
Recipient ends with @onprem.example
Action:
Relay through OnPremisesRelay

Rule 2: Route cloud recipients
Condition:
Recipient ends with @cloud.example
Action:
Relay through CloudRelay
```

Rules evaluate recipients separately. An email addressed to both domains can route each recipient through the corresponding relay. For more hybrid and migration patterns, see [Mail Manager – SES introduces new email routing and archiving features](https://aws.amazon.com/blogs/messaging-and-targeting/mail-manager-amazon-ses-introduces-new-email-routing-and-archiving-features/).