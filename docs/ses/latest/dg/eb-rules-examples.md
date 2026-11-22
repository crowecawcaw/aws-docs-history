

# Rule set examples

Use these examples to identify the pattern that matches your email-processing goal. Each example explains which recipients or messages the rule selects, which `Unless` conditions exclude matches, the order in which actions run, and the expected result.

Each JSON block is a complete value for the `Rules` list in a `CreateRuleSet` or `UpdateRuleSet` request. The resource identifiers, addresses, and names are example values. Replace them with resources and addresses from your environment. For instructions on applying a `Rules` list, see [Create and manage rule sets](eb-rules-setup.md). For condition fields, action fields, permissions, and failure behavior, see [Rule conditions](eb-rules-conditions.md) and [Rule actions](eb-rules-actions.md).

Choose an example.
+ [Archive and deliver email](#eb-rules-examples-archive-deliver) – Retain email before delivering it through an SMTP relay.
+ [Isolate suspicious email](#eb-rules-examples-isolate-suspicious) – Mark and store email that matches a security result, and then stop processing.
+ [Process email with Lambda](#eb-rules-examples-lambda) – Invoke a Lambda function for email sent to a selected recipient.
+ [Route email by department](#eb-rules-examples-department-routing) – Send sales and support recipients through separate SMTP relays.
+ [Add routing information](#eb-rules-examples-add-header) – Add a routing header before relaying selected recipients.
+ [Replace recipients during migration](#eb-rules-examples-replace-recipient) – Replace an old recipient address before routing email to a new mail platform.

## Archive and deliver email
<a name="eb-rules-examples-archive-deliver"></a>

**Goal**  
Retain email for compliance before delivering it to an existing mail server.

**How the pattern works**  
The rule selects recipients in the `example.com` domain, except `test@example.com`. Archive runs before SMTP relay. Setting the Archive action's `ActionFailurePolicy` to `DROP` prevents relay after a customer configuration error stops the archive action.

**Rule configuration**  
The rule uses the following conditions and ordered actions.
+ **Conditions** – `RECIPIENT ENDS_WITH @example.com`.
+ **Unless** – `RECIPIENT EQUALS test@example.com`.
+ **Actions**

  1. Archive in `ar-id-1234`.

  1. Relay through `rl-0123456789abcdef`.

**Literal configuration**  
The following `Rules` list implements the pattern.

```json
[
  {
    "Name": "archive-and-relay-orders",
    "Conditions": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "ENDS_WITH",
          "Values": [
            "@example.com"
          ]
        }
      }
    ],
    "Unless": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "EQUALS",
          "Values": [
            "test@example.com"
          ]
        }
      }
    ],
    "Actions": [
      {
        "Archive": {
          "TargetArchive": "ar-id-1234",
          "ActionFailurePolicy": "DROP"
        }
      },
      {
        "Relay": {
          "Relay": "rl-0123456789abcdef",
          "MailFrom": "REPLACE",
          "ActionFailurePolicy": "DROP"
        }
      }
    ]
  }
]
```

**Expected result**  
For an email addressed to `orders@example.com` and `test@example.com`, the Archive and Relay actions run only for `orders@example.com`. The archive operation completes before relay starts. The rule takes no action for `test@example.com`, which remains available to later rules.

**Related AWS walkthrough**  
For a complete in-transit archiving and SMTP delivery walkthrough, see [Archiving and sending to final SMTP server](https://aws.amazon.com/blogs/messaging-and-targeting/archiving-and-sending-to-final-smtp-server/).

**Related details**  
See [SMTP connection and envelope conditions](eb-rules-conditions.md#eb-rules-conditions-reference-smtp) for recipient matching. See [How action order works](eb-rules-actions.md#eb-rules-actions-order), [Archive](eb-rules-actions.md#eb-rules-actions-archive), [SMTP relay](eb-rules-actions.md#eb-rules-actions-relay), and [Handling an action failure](eb-rules-actions.md#eb-rules-actions-failure-policy) for action configuration and behavior.

## Isolate suspicious email
<a name="eb-rules-examples-isolate-suspicious"></a>

**Goal**  
Store suspicious email for security review and prevent it from reaching its selected recipients.

**How the pattern works**  
This pattern uses Vade Advanced Email Security, an Email Add On. The condition matches the `addon.verdict` result when Vade reports `scam`, `suspect`, `phishing`, or `malware`. A subject containing `Action required` skips this rule. For a match, the actions add a result header, store the email in S3, and then stop processing.

**Rule configuration**  
The rule uses the following condition, exception, and ordered actions.
+ **Conditions** – Vade `addon.verdict EQUALS scam, suspect, phishing, or malware`.
+ **Unless** – `SUBJECT CONTAINS Action required`.
+ **Actions**

  1. Add `X-vedacheck: failed`.

  1. Write the email to the `security-review` prefix in `mail-quarantine-example`.

  1. Drop the selected recipients.

**Literal configuration**  
The following `Rules` list implements the pattern.

```json
[
  {
    "Name": "scan-and-isolate",
    "Conditions": [
      {
        "StringExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "arn:aws:ses:us-east-1:111122223333:addon-instance/ai-0123456789abcdef",
              "ResultField": "addon.verdict"
            }
          },
          "Operator": "EQUALS",
          "Values": [
            "scam",
            "suspect",
            "phishing",
            "malware"
          ]
        }
      }
    ],
    "Unless": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "SUBJECT"
          },
          "Operator": "CONTAINS",
          "Values": [
            "Action required"
          ]
        }
      }
    ],
    "Actions": [
      {
        "AddHeader": {
          "HeaderName": "X-vedacheck",
          "HeaderValue": "failed"
        }
      },
      {
        "WriteToS3": {
          "RoleArn": "arn:aws:iam::111122223333:role/MailManagerS3ActionRole",
          "S3Bucket": "mail-quarantine-example",
          "S3Prefix": "security-review",
          "ActionFailurePolicy": "DROP"
        }
      },
      {
        "Drop": {}
      }
    ]
  }
]
```

**Expected result**  
For an email to `student@example.edu` with subject `Quarterly account notice` and Vade verdict `phishing`, the stored email contains `X-vedacheck: failed`. After storage completes, Drop stops all remaining rule-set processing for `student@example.edu`.

For an email with subject `Action required: reset account`, the `Unless` condition matches. None of this rule's actions run, and the recipient remains available to later rules.

**Related AWS walkthrough**  
This pattern follows the *Scan and isolate malicious content* rule in [Streamlining outbound emails with SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/streamlining-outbound-emails-with-amazon-ses-mail-manager/). For additional security scenarios, see [How SES Mail Manager Elevates Email Security and Efficiency](https://aws.amazon.com/blogs/messaging-and-targeting/how-amazon-ses-mail-manager-elevates-email-security-and-efficiency/).

**Related details**  
See [Email Add On result conditions](eb-rules-conditions.md#eb-rules-conditions-reference-addons) and [Email Add Ons](eb-addons.md) for Email Add On conditions. See [Add header](eb-rules-actions.md#eb-rules-actions-add-header), [Write to S3](eb-rules-actions.md#eb-rules-actions-write-to-s3), and [Drop](eb-rules-actions.md#eb-rules-actions-drop) for the action fields and behavior.

## Process email with Lambda
<a name="eb-rules-examples-lambda"></a>

**Goal**  
Invoke an application when a tenant submits documents through its dedicated email address.

**How the pattern works**  
The recipient condition selects email sent to `acme@uploads.anycompany.io`. A subject beginning with `[TEST]` skips the invocation. The Lambda action invokes `ProcessInboundAttachments` asynchronously for the selected recipient.

**Rule configuration**  
The rule uses the following condition, exception, and action.
+ **Conditions** – `RECIPIENT EQUALS acme@uploads.anycompany.io`.
+ **Unless** – `SUBJECT STARTS_WITH [TEST]`.
+ **Actions**

  1. Invoke `ProcessInboundAttachments` with invocation type `EVENT`.

**Literal configuration**  
The following `Rules` list implements the pattern.

```json
[
  {
    "Name": "process-acme-uploads",
    "Conditions": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "EQUALS",
          "Values": [
            "acme@uploads.anycompany.io"
          ]
        }
      }
    ],
    "Unless": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "SUBJECT"
          },
          "Operator": "STARTS_WITH",
          "Values": [
            "[TEST]"
          ]
        }
      }
    ],
    "Actions": [
      {
        "InvokeLambda": {
          "FunctionArn": "arn:aws:lambda:us-east-1:111122223333:function:ProcessInboundAttachments",
          "InvocationType": "EVENT",
          "RoleArn": "arn:aws:iam::111122223333:role/MailManagerLambdaActionRole",
          "ActionFailurePolicy": "DROP"
        }
      }
    ]
  }
]
```

**Expected result**  
For an email with subject `Invoice 1042` addressed to `acme@uploads.anycompany.io` and `globex@uploads.anycompany.io`, the function receives one asynchronous invocation for `acme@uploads.anycompany.io`. The rule does not select `globex@uploads.anycompany.io`.

If the subject is `[TEST] Invoice 1042`, the `Unless` condition skips the invocation.

**Related AWS walkthrough**  
For a multi-tenant attachment-processing example, see [Build an AI email pipeline with Amazon Bedrock and SES Mail Manager](https://aws.amazon.com/blogs/messaging-and-targeting/build-an-ai-email-pipeline-with-amazon-bedrock-and-ses-mail-manager/).

**Related details**  
See [Recipient-level and message-level matching](eb-rules-conditions.md#eb-rules-conditions-recipient-message) for recipient and subject behavior. See [Invoke Lambda function](eb-rules-actions.md#eb-rules-actions-invoke-lambda) for the payload, permissions, invocation types, responses, and failure behavior.

## Route email by department
<a name="eb-rules-examples-department-routing"></a>

**Goal**  
Send sales and support recipients to separate departmental mail systems.

**How the pattern works**  
Two ordered rules evaluate each SMTP envelope recipient separately. The first rule sends `sales@example.com` through the sales relay. The second rule sends `support@example.com` through the support relay. Both rules exclude messages from the automated test sender.

**Rule configuration**  
The rule set uses the following rules.
+ **Rule 1**
  + **Conditions** – `RECIPIENT EQUALS sales@example.com`.
  + **Unless** – `MAIL_FROM EQUALS automated-test@example.net`.
  + **Actions** – Relay through `rl-0123456789abcdef`.
+ **Rule 2**
  + **Conditions** – `RECIPIENT EQUALS support@example.com`.
  + **Unless** – `MAIL_FROM EQUALS automated-test@example.net`.
  + **Actions** – Relay through `rl-fedcba9876543210`.

**Literal configuration**  
The following `Rules` list implements the pattern.

```json
[
  {
    "Name": "route-sales",
    "Conditions": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "EQUALS",
          "Values": [
            "sales@example.com"
          ]
        }
      }
    ],
    "Unless": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "MAIL_FROM"
          },
          "Operator": "EQUALS",
          "Values": [
            "automated-test@example.net"
          ]
        }
      }
    ],
    "Actions": [
      {
        "Relay": {
          "Relay": "rl-0123456789abcdef",
          "MailFrom": "REPLACE",
          "ActionFailurePolicy": "DROP"
        }
      }
    ]
  },
  {
    "Name": "route-support",
    "Conditions": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "EQUALS",
          "Values": [
            "support@example.com"
          ]
        }
      }
    ],
    "Unless": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "MAIL_FROM"
          },
          "Operator": "EQUALS",
          "Values": [
            "automated-test@example.net"
          ]
        }
      }
    ],
    "Actions": [
      {
        "Relay": {
          "Relay": "rl-fedcba9876543210",
          "MailFrom": "REPLACE",
          "ActionFailurePolicy": "DROP"
        }
      }
    ]
  }
]
```

**Expected result**  
For an email from `customer@example.net` addressed to both `sales@example.com` and `support@example.com`, the first rule relays only `sales@example.com`. The second rule then relays only `support@example.com`.

For an email from `automated-test@example.net`, both `Unless` conditions match and neither relay action runs.

**Related AWS walkthrough**  
For recipient-oriented processing and condition-based SMTP relay patterns, see [Mail Manager – SES introduces new email routing and archiving features](https://aws.amazon.com/blogs/messaging-and-targeting/mail-manager-amazon-ses-introduces-new-email-routing-and-archiving-features/).

**Related details**  
See [SMTP connection and envelope conditions](eb-rules-conditions.md#eb-rules-conditions-reference-smtp) for `RECIPIENT` and `MAIL_FROM`. See [SMTP relay](eb-rules-actions.md#eb-rules-actions-relay) for relay configuration, permissions, and delivery behavior.

## Add routing information
<a name="eb-rules-examples-add-header"></a>

**Goal**  
Add routing information for one recipient before relaying the email.

**How the pattern works**  
The recipient condition selects `orders@example.com`. An original `X-Route: manual` header skips the rule. Otherwise, Add header adds `X-Route: orders` before SMTP relay. The relay action receives the modified MIME email.

**Rule configuration**  
The rule uses the following condition, exception, and ordered actions.
+ **Conditions** – `RECIPIENT EQUALS orders@example.com`.
+ **Unless** – Custom header `X-Route EQUALS manual`.
+ **Actions**

  1. Add `X-Route: orders`.

  1. Relay through `rl-0123456789abcdef`.

**Literal configuration**  
The following `Rules` list implements the pattern.

```json
[
  {
    "Name": "mark-and-route-orders",
    "Conditions": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "EQUALS",
          "Values": [
            "orders@example.com"
          ]
        }
      }
    ],
    "Unless": [
      {
        "StringExpression": {
          "Evaluate": {
            "MimeHeaderAttribute": "X-Route"
          },
          "Operator": "EQUALS",
          "Values": [
            "manual"
          ]
        }
      }
    ],
    "Actions": [
      {
        "AddHeader": {
          "HeaderName": "X-Route",
          "HeaderValue": "orders"
        }
      },
      {
        "Relay": {
          "Relay": "rl-0123456789abcdef",
          "MailFrom": "REPLACE",
          "ActionFailurePolicy": "DROP"
        }
      }
    ]
  }
]
```

**Expected result**  
For an email addressed to `orders@example.com` and `audit@example.com` without an original `X-Route` header, the relayed email for `orders@example.com` contains:

```
X-Route: orders
```

The rule does not select `audit@example.com`, so its email variant does not receive the header. If the original email contains `X-Route: manual`, the `Unless` condition skips both actions for `orders@example.com`.

**Related AWS walkthrough**  
For the recipient-oriented header pattern that applies a change only to matching recipients, see [Mail Manager – SES introduces new email routing and archiving features](https://aws.amazon.com/blogs/messaging-and-targeting/mail-manager-amazon-ses-introduces-new-email-routing-and-archiving-features/).

**Related details**  
See [Message header and metadata conditions](eb-rules-conditions.md#eb-rules-conditions-reference-message) for matching an original custom header. See [Add header](eb-rules-actions.md#eb-rules-actions-add-header) and [SMTP relay](eb-rules-actions.md#eb-rules-actions-relay) for the action fields and ordering behavior.

## Replace recipients during migration
<a name="eb-rules-examples-replace-recipient"></a>

**Goal**  
Move an old email address to a new mail platform while excluding a migration test address.

**How the pattern works**  
The first rule selects recipients in `old.example.com`, except `migration-test@old.example.com`. Replace recipient changes `orders@old.example.com` to `orders@new.example.com`. The next action associates `X-Migration-Route: new-platform` with the replacement recipient. A later rule matches the updated recipient and relays it to the new mail system.

**Rule configuration**  
The rule set uses the following rules.
+ **Rule 1**
  + **Conditions** – `RECIPIENT ENDS_WITH @old.example.com`.
  + **Unless** – `RECIPIENT EQUALS migration-test@old.example.com`.
  + **Actions**

    1. Replace the selected recipient with `orders@new.example.com`.

    1. Add `X-Migration-Route: new-platform`.
+ **Rule 2**
  + **Conditions** – `RECIPIENT EQUALS orders@new.example.com`.
  + **Unless** – None.
  + **Actions** – Relay through `rl-fedcba9876543210`.

**Literal configuration**  
The following `Rules` list implements the pattern.

```json
[
  {
    "Name": "replace-old-orders",
    "Conditions": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "ENDS_WITH",
          "Values": [
            "@old.example.com"
          ]
        }
      }
    ],
    "Unless": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "EQUALS",
          "Values": [
            "migration-test@old.example.com"
          ]
        }
      }
    ],
    "Actions": [
      {
        "ReplaceRecipient": {
          "ReplaceWith": [
            "orders@new.example.com"
          ]
        }
      },
      {
        "AddHeader": {
          "HeaderName": "X-Migration-Route",
          "HeaderValue": "new-platform"
        }
      }
    ]
  },
  {
    "Name": "route-new-orders",
    "Conditions": [
      {
        "StringExpression": {
          "Evaluate": {
            "Attribute": "RECIPIENT"
          },
          "Operator": "EQUALS",
          "Values": [
            "orders@new.example.com"
          ]
        }
      }
    ],
    "Unless": [],
    "Actions": [
      {
        "Relay": {
          "Relay": "rl-fedcba9876543210",
          "MailFrom": "REPLACE",
          "ActionFailurePolicy": "DROP"
        }
      }
    ]
  }
]
```

**Expected result**  
For an email addressed to `orders@old.example.com` and `migration-test@old.example.com`, the first rule replaces only `orders@old.example.com`. Its Add header action then applies to `orders@new.example.com`.

The second rule evaluates the updated recipient list. It matches `orders@new.example.com` and relays that recipient with:

```
X-Migration-Route: new-platform
```

`migration-test@old.example.com` remains unchanged and does not match the second rule. Replacing the SMTP envelope recipient does not change `orders@old.example.com` in the visible `To` or `CC` header.

**Related AWS walkthrough**  
For modifying recipient lists, routing by recipient, and supporting old and new mail platforms during migration, see [Mail Manager – SES introduces new email routing and archiving features](https://aws.amazon.com/blogs/messaging-and-targeting/mail-manager-amazon-ses-introduces-new-email-routing-and-archiving-features/).

**Related details**  
See [Recipient-level and message-level matching](eb-rules-conditions.md#eb-rules-conditions-recipient-message) for recipient selection. See [Replace recipient](eb-rules-actions.md#eb-rules-actions-replace-recipient), [Add header](eb-rules-actions.md#eb-rules-actions-add-header), and [SMTP relay](eb-rules-actions.md#eb-rules-actions-relay) for action behavior.

## Apply and monitor a rule-set pattern
<a name="eb-rules-examples-apply-monitor"></a>

Use [Create and manage rule sets](eb-rules-setup.md) to create or update a rule set with one of these `Rules` lists and assign the rule set to an ingress endpoint.

Create the resources and permissions required by each action before applying the rule set. See [Rule actions](eb-rules-actions.md) for the required resources, permissions, and failure behavior.

Use [Monitor and troubleshoot rule sets](eb-rules-monitoring.md) to confirm successful processing and investigate an individual message. Use [Setting up Mail Manager log delivery](eb-logging.md#setting-up-log-delivery) to configure logs. See [Rule set logs – `APPLICATION_LOGS`](eb-logging.md#rule-set-logs) to review which recipients matched each rule and the status and order of its actions.