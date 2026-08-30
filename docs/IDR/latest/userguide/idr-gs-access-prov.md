# Provision access for alarm ingestion to Incident Detection and Response

###### Note

If you didn't create the service-linked role (SLR) during the IDR CLI onboarding, follow the steps below to manually provision access.

To allow AWS Incident Detection and Response to ingest alarms from your account, create the `AWSServiceRoleForHealth_EventProcessor` SLR. AWS assumes the SLR to create a Managed EventBridge rule in your account. The managed EventBridge rule sends notifications from your account to AWS Incident Detection and Response. For information about this SLR, including the associated AWS managed policy, see [Using service-linked roles for AWS Health](../../../health/latest/ug/using-service-linked-roles.md "../../../health/latest/ug/using-service-linked-roles.md") in the _AWS Health User Guide_.

You can create this service-linked role in your account by following the instructions in [Create service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _AWS Identity and Access Management User Guide_. Or, you can use the following AWS Command Line Interface (AWS CLI) command:

```
aws iam create-service-linked-role --aws-service-name event-processor.health.amazonaws.com
```

**Key outputs**

- Successful creation of the service-linked role in your account.

###### Note

The service-linked role - AWSServiceRoleForHealth\_EventProcessor needs to be created in each account you will use to send alarms to AWS Incident Detection and Response.

**Related information**

For more information, see the following topics:

- [Using service-linked roles for AWS Health](../../../health/latest/ug/using-service-linked-roles.md "../../../health/latest/ug/using-service-linked-roles.md")
- [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role")
- [AWS managed policy: AWSHealth\_EventProcessorServiceRolePolicy](../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-Health_EventProcessorServiceRolePolicy "../../../health/latest/ug/security-iam-awsmanpol.md#security-iam-awsmanpol-Health_EventProcessorServiceRolePolicy")
