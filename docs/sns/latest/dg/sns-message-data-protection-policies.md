# Understanding Amazon SNS data protection

policies

## What are data protection

policies?

Amazon SNS uses **data protection policies** to select the
sensitive data for which you want to scan, and the actions that you want to take to
protect that data from being exchanged by your Amazon SNS topics. To select the sensitive
data of interest, you use [data
identifiers](sns-message-data-protection-managed-data-identifiers.md "sns-message-data-protection-managed-data-identifiers.md"). Amazon SNS message data protection then detects the sensitive data by
using machine learning and pattern matching. To act upon data identifiers that are
found, you can define an **audit**, **de-identify**, or **deny** operation. These
operations let you log the sensitive data that is found (or not found), mask or redact
sensitive data, or deny message delivery.

![Amazon SNS utilizes data protection policies to manage and secure sensitive data across different AWS services. It shows the workflow for both inbound and outbound messages, detailing how data is monitored and actions are taken based on policy settings like auditing, de-identifying, or denying data transmission to safeguard information such as personally identifiable information (PII) and protected health information (PHI).](images/message-data-protection-policies-overview.png)

## How is the data protection policy

structured?

As illustrated in the following figure, a data protection policy document includes the
following elements:

- Optional policy-wide information at the top of the document
- One or more individual statements

Each statement includes information about a single permission.

![The structure of a data protection policy in Amazon SNS, illustrating how the policy is composed of various elements like the policy name, description, version, and multiple statements that specify actions like auditing, de-identifying, or denying based on data direction, identifiers, and involved principals.](images/payload-policy-process.png)

Only one data protection policy can be defined per Amazon SNS topic. The data protection
policy can have one or more deny or de-identify statements, but only one audit
statement.

### JSON properties for the

data protection policy

A data protection policy requires the following basic policy information for
identification:

- **Name** – The policy name.
- **Description** (Optional) – The
  policy description.
- **Version** – The policy language
  version. The current version is 2021-06-01.
- **Statement** – A list of statements
  that specifies data protection policy actions.

```
{
  "Name": "basicPII-protection",
  "Description": "Protect basic types of sensitive data",
  "Version": "2021-06-01",
  "Statement": [
        ...
  ]
}
```

### JSON properties for a policy

statement

A policy statement sets the detection context for the data protection
operation.

- **Sid** (Optional) – The statement
  identifier.
- **DataDirection** – Inbound (for
  Publish API requests) or Outbound (for notification deliveries) with respect
  to the Amazon SNS topic.
- **DataIdentifier** – The sensitive
  data for which the Amazon SNS topic should scan. For example, name, address, or
  phone number.
- **Principal** – The IAM principal
  that is published to the topic, or the IAM principal that is subscribed to
  the topic.
- **Operation** – The follow-on action,
  either **Audit**, **De-identify** (mask or
  redact), or **Deny** (block), which the Amazon SNS topic
  executes once it finds sensitive data.

```
{
    "Sid": "basicPII-inbound-protection",
    "DataDirection": "Inbound",
    "Principal": ["*"],
    "DataIdentifier": [
        "arn:aws:dataprotection::aws:data-identifier/Name",
        "arn:aws:dataprotection::aws:data-identifier/PhoneNumber-US"
    ],
    "Operation": {
        ...
    }
}
```

### JSON properties for a policy

statement operation

A policy statement sets one of the following data protection operations.

- [Audit](sns-message-data-protection-operations.md#statement-operation-json-properties-audit "sns-message-data-protection-operations.md#statement-operation-json-properties-audit") – Emits metrics and
  finding logs without interrupting message publishing or delivery.
- [De-identify](sns-message-data-protection-operations.md#statement-operation-json-properties-deidentify "sns-message-data-protection-operations.md#statement-operation-json-properties-deidentify") – Mask or redact
  sensitive data without interrupting message publishing.
- [Deny](sns-message-data-protection-operations.md#statement-operation-json-properties-deny "sns-message-data-protection-operations.md#statement-operation-json-properties-deny") – Blocks the Amazon SNS publish
  request or fails the message delivery.

## How do I determine the

IAM principals for my data protection policy?

Message data protection uses two IAM principals that interact with Amazon SNS.

1. **Publish API Principal** (Inbound) – The
   authenticated IAM principal calling the Amazon SNS `Publish` API.
2. **Subscription Principal** (Outbound) –
   The authenticated IAM principal that called the `Subscribe` API
   during subscription creation.

The `SubscriptionPrincipal` is a publicly available Amazon SNS subscription
property that can be retrieved from the `GetSubscriptionAttributes`
API.

```
{
  "Attributes": {
    "SubscriptionPrincipal": "arn:aws:iam::123456789012:user/NoNameAccess",
    "Owner": "123412341234",
    "RawMessageDelivery": "true",
    "TopicArn": "arn:aws:sns:us-east-1:123412341234:PII-data-topic",
    "Endpoint": "arn:aws:sqs:us-east-1:123456789012:NoNameAccess",
    "Protocol": "sqs",
    "PendingConfirmation": "false",
    "ConfirmationWasAuthenticated": "true",
    "SubscriptionArn": "arn:aws:sns:us-east-1:123412341234:PII-data-topic:5d8634ef-67ef-49eb-a824-4042b28d6f55"
  }
}
```
