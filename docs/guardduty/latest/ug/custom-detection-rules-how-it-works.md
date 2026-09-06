# How Custom Detection Rules work

Begin by browsing the rules that GuardDuty offers to identify the ones that detect
activity relevant to your environment. Then associate each rule with the accounts
where the activity is unexpected. For more information about associating
rules with accounts, see [Managing Custom Detection Rules](custom-detection-rules-managing.md "custom-detection-rules-managing.md").

## Data sources and signals

After you associate a rule, GuardDuty monitors the data sources that the rule depends
on and evaluates the incoming logs for matching events. Custom Detection Rules
currently supports AWS CloudTrail management events. When observed activity matches a
rule, GuardDuty generates a _signal_. A signal represents a single
observed occurrence of the activity that the rule detects.

## Modes

Every association runs in one of two modes:

- **Live** – GuardDuty generates a finding
  when the rule matches.
- **Dry run** – GuardDuty emits Amazon CloudWatch
  metrics that count how often the rule matches but does not generate
  findings. Use dry run to measure how frequently a rule matches before it
  can create findings or trigger automated responses. Dry run associations
  expire 14 days after creation, live associations do not expire.

For more information, see [Dry run](custom-detection-rules-managing.md#custom-detection-rules-dryrun "custom-detection-rules-managing.md#custom-detection-rules-dryrun") and [Live](custom-detection-rules-managing.md#custom-detection-rules-live "custom-detection-rules-managing.md#custom-detection-rules-live").

## Finding aggregation

GuardDuty aggregates signals that share the same tactic, service, and technique into a
single finding. Each finding follows the format
`Tactic:Service/Technique`, for example,
`Persistence:IAM/AccountManipulation`. A single finding can contain multiple
signals when GuardDuty observes the same activity repeatedly from the same principal.

For more information about the finding structure and fields, see
[Custom Detection Rules finding details](guardduty_findings-summary.md#custom-detection-rules-finding-details "guardduty_findings-summary.md#custom-detection-rules-finding-details").
