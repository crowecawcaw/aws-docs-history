# EDI Cloud Operations customer account access reasons

In certain circumstances ECO operators can access your account console and instances to manage your resources. You can view these access events
in your AWS CloudTrail logs.

EDI customer account access activity is driven by triggers in response to CloudWatch alarms and events, and incident reports or service requests that you submit.
The ECO operator might perform multiple service calls and host-level activities for each access.

Access justiﬁcation, the triggers, and the initiator of the trigger are listed in the following table.

| Access                                 | Initiator | Trigger                                                               |
| -------------------------------------- | --------- | --------------------------------------------------------------------- |
| Internal problem investigation         | ECO       | Problem issue (an issue that has been identiﬁed as systemic)          |
| Alert investigation and remediation    | ECO       | AWS Systems Manager operational work items (SSM OpsItems)             |
| Incident investigation and remediation | You       | Inbound support case (an incident or service request that you submit) |
| Inbound service request fulﬁllment     | You       | Inbound support case (an incident or service request that you submit) |

For information about how to review ECO operations and automation activity in your account, see
[Tracking changes in your AMS Accelerate accounts](../../../managedservices/latest/accelerate-guide/acc-change-record.md "../../../managedservices/latest/accelerate-guide/acc-change-record.md"),
in the _AMS Accelerate User Guide_.
