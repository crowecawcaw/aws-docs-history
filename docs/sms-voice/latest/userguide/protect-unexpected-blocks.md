# Managing unexpected blocks in SMS Protect

Filter mode might occasionally block a legitimate message that was flagged as potential
AIT. This page describes how to manage legitimate traffic that is being blocked, and how to
reduce unexpected blocks at the source.

## Confirm the messages are legitimate

Before adjusting any configuration, verify that the blocked messages are actually
legitimate. Confirm the blocked traffic is legitimate before loosening controls. High,
sustained volumes to a number (or many numbers with identical parallel patterns) might
indicate a real AIT attack. Use the following approaches to gather evidence:

- **Protect configuration monitoring** –
  Review the protect configuration metrics in the AWS End User Messaging SMS console. The monitoring
  dashboard shows the volume and rate of blocked messages by country, helping you
  identify sudden spikes that might indicate AIT rather than unexpected blocks. For
  more information, see [View protect metrics in AWS End User Messaging SMS](filter-and-monitor-messages-monitor.md "filter-and-monitor-messages-monitor.md").
- **Event destinations** – Configure an event
  destination on your configuration set to receive detailed per-message delivery
  events. Events with a `PROTECT_BLOCKED` status indicate messages
  blocked by Filter mode. Cross-reference these events with your application logs
  to determine whether the destination phone numbers belong to real users. For more
  information, see [Event destinations in AWS End User Messaging SMS](configuration-sets-event-destinations.md "configuration-sets-event-destinations.md").
- **Amazon CloudWatch metrics** – Use CloudWatch to create
  alarms on protect-related metrics. You can set thresholds to alert you when the
  block rate exceeds normal levels, which might indicate either an AIT attack or an
  increase in unexpected blocks. For more information, see [View protect metrics in AWS End User Messaging SMS](filter-and-monitor-messages-monitor.md "filter-and-monitor-messages-monitor.md").

If your investigation confirms that the blocked messages were sent to real users who
initiated an action (such as requesting a one-time password or transactional
notification), proceed with remediation.

## Remediation options

The following options are ordered from narrowest to broadest scope. Apply the narrowest
control that resolves the issue.

### Phone number overrides

Add known-good numbers as Allow exceptions to bypass evaluation. This is the
narrowest impact and the fastest way to clear a legitimate number that was blocked.
You can manage overrides from the console or API.

You can set override rules as permanent or with an expiration date. If your
customers report not receiving messages, integrate override creation with your
support workflows or customer data platforms to dynamically allow specific
numbers.

For more information, see [Phone number override rules in AWS End User Messaging SMS](protect-rule-override.md "protect-rule-override.md").

### Country rule mode

Set the country to Allow, or Monitor (delivers while still surfacing AIT signals),
if Filter is blocking legitimate traffic. This is per configuration, effective
immediately, and affects all traffic to that country.

- **Filter to Monitor** – Messages
  continue to be evaluated, but high-risk messages are delivered instead of
  blocked. You receive events indicating the risk assessment without impacting
  delivery.
- **Filter to Allow** – Disables risk
  evaluation entirely for the country. All messages are delivered regardless
  of risk score. Use this only for countries where you have strong
  application-layer controls in place to prevent AIT.

For more information about country rule modes, see [Country rule modes in AWS End User Messaging SMS](filter-and-monitor-messages.md "filter-and-monitor-messages.md").

### Separate protect configurations per use case

Isolate a sensitive use case (such as authentication) so a mode change does not
affect unrelated traffic. If your account sends both high-risk traffic (such as
sign-up flows) and low-risk traffic (such as transactional alerts to verified users),
create separate protect configurations. Associate each configuration with different
phone numbers or pools.

For more information about creating protect configurations, see [Using protect configurations in AWS End User Messaging SMS](protect-configuration.md "protect-configuration.md").

## Reduce unexpected blocks at the source

Protect is complementary to your application-layer controls, not a replacement.
Implement the following controls to cut both attack volume and unexpected blocks:

- **Cap OTP requests per user** – Limit the
  number of OTP or verification messages a single user can request within a time
  window before calling the AWS End User Messaging SMS API. This cuts both attack volume and unexpected
  blocks.
- **CAPTCHA or proof-of-work challenges** –
  Add a CAPTCHA or similar challenge before triggering an SMS send. This prevents
  bots from generating high volumes of send requests that produce traffic patterns
  similar to AIT.
- **Message feedback API** – Use the message
  feedback API to confirm OTP delivery and usage, and right-size your rate limits.
  For more information, see [Message feedback in AWS End User Messaging SMS](message-feedback.md "message-feedback.md").

## What you cannot configure

The risk model and its detection sensitivity are managed by AWS and apply uniformly
across all customers. The following aspects are not configurable:

- The risk scoring threshold that determines whether a message is blocked or
  flagged.
- The specific signals the model uses to evaluate risk.
- Tuning or training of the model for individual accounts.

To request new capabilities (for example, configurable detection sensitivity by
country), contact your account team.

## When to contact support

Open an AWS Support case if any of the following apply:

- Blocking persists after applying the options above.
- A message to a number on your Allow override list is blocked.
- A message that should have been blocked is delivered.

Include the following information: destination country, per-number send rate, affected
time window, and relevant override rules.
