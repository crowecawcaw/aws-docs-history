# Provision access for alert ingestion to Incident Detection and Response

To allow AWS Incident Detection and Response to ingest alarms from your account, install the `AWSServiceRoleForHealth_EventProcessor` service-linked
role (SLR). AWS assumes the
SLR to create an Amazon EventBridge-managed rule. The managed rule sends notifications from
your accounts to AWS Incident Detection and Response. For information about this SLR, including the associated
AWS managed policy, see [Using service-linked
roles](../../../health/latest/ug/using-service-linked-roles.md "../../../health/latest/ug/using-service-linked-roles.md") in the _AWS Health User Guide_.

You can install this service-linked role in your account by following the
instructions in [Create service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _AWS Identity and Access Management User Guide_. Or, you can use the following AWS Command Line Interface (AWS CLI) command:

```
aws iam create-service-linked-role --aws-service-name event-processor.health.amazonaws.com
```

**Key outputs**

- Successful installation of the service-linked role in your account.
  **Related information**

For more information, see the following topics:

- [Using service-linked roles for AWS Health](../../../health/latest/ug/using-service-linked-roles.md "../../../health/latest/ug/using-service-linked-roles.md")
- [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role")
- [AWS managed policy: AWSHealth_EventProcessorServiceRolePolicy](../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-Health_EventProcessorServiceRolePolicy "../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-Health_EventProcessorServiceRolePolicy")
