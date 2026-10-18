

# How Custom Detection Rules work
<a name="custom-detection-rules-how-it-works"></a>

Begin by browsing the rules that GuardDuty offers to identify the ones that detect activity relevant to your environment. Then associate each rule with the accounts where the activity is unexpected. For more information about associating rules with accounts, see [Managing Custom Detection Rules](custom-detection-rules-managing.md).

## Data sources and signals
<a name="custom-detection-rules-how-it-works-data-sources"></a>

After you associate a rule, GuardDuty monitors the data sources that the rule depends on and evaluates the incoming logs for matching events. Custom Detection Rules supports AWS CloudTrail management events and Runtime Monitoring events. When observed activity matches a rule, GuardDuty generates a *signal*. A signal represents a single observed occurrence of the activity that the rule detects.

Each data source has its own requirements:

AWS CloudTrail management events  
GuardDuty analyzes these events in every account where GuardDuty is enabled. No additional setup is required.

Runtime Monitoring events  
Runtime Monitoring rules evaluate the process, file, and network activity that the GuardDuty security agent observes on your resources. A Runtime Monitoring rule can match activity only on a resource that meets both of the following requirements:  
+ Runtime Monitoring is enabled for the resource type: Amazon EKS, Amazon EC2, or Amazon ECS on Fargate. For more information, see [GuardDuty Runtime Monitoring](runtime-monitoring.md).
+ The GuardDuty security agent runs on the resource, at or above the rule's minimum agent version for that platform.
Each Runtime Monitoring rule states the minimum agent version that it requires on each platform where it can run. To view these requirements, call the [GetCustomDetectionRule](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRule.html) operation.  
If the agent on a resource is older than a rule's minimum version, the rule does not match activity on that resource. GuardDuty does not report an error in this case, so keep the agent up to date on the resources where you enable Runtime Monitoring rules. For information about agent versions, see [GuardDuty security agent release versions](runtime-monitoring-agent-release-history.md).

## Modes
<a name="custom-detection-rules-how-it-works-modes"></a>

Every association runs in one of two modes:
+ **Live** – GuardDuty generates a finding when the rule matches.
+ **Dry run** – GuardDuty emits Amazon CloudWatch metrics that count how often the rule matches but does not generate findings. Use dry run to measure how frequently a rule matches before it can create findings or trigger automated responses. Dry run associations expire 14 days after creation, live associations do not expire.

For more information, see [Dry run](custom-detection-rules-managing.md#custom-detection-rules-dryrun) and [Live](custom-detection-rules-managing.md#custom-detection-rules-live).

## Finding aggregation
<a name="custom-detection-rules-how-it-works-finding-aggregation"></a>

Each finding follows the format `Tactic:Service/Technique`, for example, `Persistence:IAM/AccountManipulation` or `Persistence:Runtime/SuspiciousCommand`. How GuardDuty groups signals into findings depends on the data source that generated the signal, as described in the following list:
+ **AWS CloudTrail rules** – GuardDuty aggregates signals that share the same tactic, service, and technique into a single finding. A single finding can contain multiple signals when GuardDuty observes the same activity repeatedly from the same principal.
+ **Runtime Monitoring rules** – GuardDuty aggregates signals that share the same rule, resource, and process details into a single finding. Each finding covers one resource, such as an instance, a task, or a container. The process details that GuardDuty compares depend on the finding type. For example, file modification findings also compare the file operation and the user that ran the process. A repeat match updates the existing finding instead of creating a new one. Findings from different rules stay separate, even when the rules generate the same finding type for the same resource and process.

For more information about the finding structure and fields, see [Custom Detection Rules finding details](guardduty_findings-summary.md#custom-detection-rules-finding-details).

## Redacted event fields
<a name="custom-detection-rules-how-it-works-redacted-fields"></a>

AWS CloudTrail rules evaluate the fields that AWS CloudTrail records in an event. Redaction happens upstream of GuardDuty. An AWS service can redact the value of a field in the events that it publishes. This redaction protects potentially sensitive data. When a field is redacted, AWS CloudTrail records that the field was present but does not record its value.

The service that publishes the event decides which fields it redacts. A service redacts a field when that field can carry sensitive information. The redaction applies to the field, not to a specific value. A service therefore redacts a field even when the value in a particular request is not sensitive. It redacts those fields for every request, regardless of whether you use the AWS Management Console, the AWS CLI, or an AWS SDK.

GuardDuty cannot evaluate a value that is not in the event. If a rule's detection logic depends on a redacted field, the rule does not match. GuardDuty then produces no signal and no finding, even though the activity occurred. A rule is unaffected if it inspects only fields that services do not redact, such as the event name, the AWS service, and the calling identity.

Redaction can also make a rule match one request but not another that had the same effect. When an API operation accepts more than one field for the same change, one field might be redacted and another might not. Whether the rule matches then depends on which field the request used.

**Note**  
Custom Detection Rules are a detection capability, not a complete audit record. To confirm whether a specific API call occurred in your account, review the event in AWS CloudTrail. For more information, see [Viewing events with AWS CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).