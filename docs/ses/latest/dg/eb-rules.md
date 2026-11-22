

# Rule sets and rules

After a traffic policy accepts an email, the ingress endpoint passes the email to its assigned rule set. A rule set is a reusable group of ordered rules that controls how Mail Manager processes accepted email. You can assign the same rule set to multiple ingress endpoints.

Each rule can select email or individual recipients with conditions, skip its actions when an `Unless` condition matches, and run one or more actions. Use rules to route email, retain a compliance copy, isolate suspicious email, invoke an application, or change an email before delivery.

## How rule sets process email
<a name="eb-rules-how-it-works"></a>

The following diagram shows how a rule evaluates conditions and `Unless` conditions, runs ordered actions, and continues to the next rule.

![Accepted email enters a rule set. Rule 1 checks all its conditions and then its Unless conditions. If all conditions match and no Unless condition matches, the rule adds an X-Route header and relays the selected recipients. A condition that does not match or an Unless condition that matches skips the actions for those recipients. Processing then continues with Rule 2, named Invoices.](https://docs.aws.amazon.com/ses/latest/dg/images/rule-set-processing.png)


Rules run in the order that you configure. Each rule uses the following flow:

1. The rule starts with the email's current recipients.

1. Each condition narrows the selected recipients. A recipient remains selected only if all conditions match.

1. Each `Unless` condition checks the selected recipients. If any `Unless` condition matches a recipient, the actions do not run for that recipient.

1. The actions run in configured order for the recipients that remain selected. The next rule then evaluates the current recipient list.

## Example: Route email by recipient
<a name="eb-rules-example"></a>

This example shows how conditions select recipients and an `Unless` condition removes a recipient from that selection.
+ **Email recipients** – `orders@example.com` and `test@example.com`.
+ **Conditions** – Recipient `ENDS_WITH` `@example.com`.
+ **Unless conditions** – Recipient `EQUALS` `test@example.com`.
+ **Actions**

  1. Add the header `X-Route: orders`.

  1. Relay the email.
+ **Result** – The actions apply to `orders@example.com`. The `Unless` condition prevents them from applying to `test@example.com`.

Conditions select the recipients for a rule. `Unless` conditions remove recipients from that selection. The actions run only for the recipients that remain.

## Choose a rule-set pattern
<a name="eb-rules-patterns"></a>

The following table maps common email-processing goals to rule-set patterns.


| Goal | Rule-set pattern | 
| --- | --- | 
| Keep a compliance copy and deliver email | [**Archive and deliver email**](eb-rules-examples.md#eb-rules-examples-archive-deliver) – Archive, then relay or send. | 
| Isolate suspicious email | [**Isolate suspicious email**](eb-rules-examples.md#eb-rules-examples-isolate-suspicious) – Match a security result, write to Amazon S3, then drop. | 
| Process application email | [**Process email with Lambda**](eb-rules-examples.md#eb-rules-examples-lambda) – Match a recipient or subject, then invoke a Lambda function. | 
| Route departments separately | [**Route email by department**](eb-rules-examples.md#eb-rules-examples-department-routing) – Match a department recipient, then relay. | 
| Mark email for downstream processing | [**Add routing information**](eb-rules-examples.md#eb-rules-examples-add-header) – Add a header before delivery. | 
| Change a destination during migration | [**Replace recipients during migration**](eb-rules-examples.md#eb-rules-examples-replace-recipient) – Replace the recipient before later actions. | 

**Related resource**  
For an end-to-end routing and archiving walkthrough, see [AWS Messaging Blog: Mail Manager – Amazon SES introduces new email routing and archiving features](https://aws.amazon.com/blogs/messaging-and-targeting/mail-manager-amazon-ses-introduces-new-email-routing-and-archiving-features/).

## Reference for rule conditions and actions
<a name="eb-rules-reference"></a>
+ For information about selecting email and recipients with `Conditions` and `Unless` conditions, see [Rule conditions](eb-rules-conditions.md).
+ For information about action order, configuration, permissions, and failure behavior, see [Rule actions](eb-rules-actions.md).

**Topics**
+ [How rule sets process email](#eb-rules-how-it-works)
+ [Example: Route email by recipient](#eb-rules-example)
+ [Choose a rule-set pattern](#eb-rules-patterns)
+ [Reference for rule conditions and actions](#eb-rules-reference)
+ [Create and manage rule sets](eb-rules-setup.md)
+ [Rule conditions](eb-rules-conditions.md)
+ [Rule actions](eb-rules-actions.md)
+ [Rule set examples](eb-rules-examples.md)
+ [Monitor and troubleshoot rule sets](eb-rules-monitoring.md)