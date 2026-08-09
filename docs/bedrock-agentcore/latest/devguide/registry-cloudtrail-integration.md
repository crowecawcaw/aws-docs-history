# AWS CloudTrail integration

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

AWS Agent Registry is integrated with AWS CloudTrail, which provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures API calls for AWS Agent Registry as events. The calls captured include calls from the AWS Agent Registry console and code calls to the AWS Agent Registry API operations.

AWS Agent Registry supports logging two categories of events:

- **Management events** — Control-plane operations that create, configure, and manage registries and registry records (for example, `CreateRegistry`, `UpdateRegistryRecord`). Management events are **logged by default**; you do not need to take any action to receive them.
- **Data events** — High-volume, data-plane operations performed on or within a registry (for example, discovering records or invoking MCP). Data events are **not logged by default**. To receive them, you must create a trail and explicitly enable data event logging for the `AWS::AgentRegistry::Registry` resource type.
  For an ongoing record of events in your AWS account, including events for AWS Agent Registry, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. If you don’t configure a trail, you can still view the most recent management events in the CloudTrail console in **Event history** (data events do not appear in Event history).

## Management events

Management events (also called control-plane events) show management operations performed on registries and registry records. Management events are logged by default.

**Event source:**
`agent-registry.amazonaws.com`

Supported management events:

| API operation                   | readOnly |
| ------------------------------- | -------- |
| CreateRegistry                  | No       |
| GetRegistry                     | Yes      |
| UpdateRegistry                  | No       |
| DeleteRegistry                  | No       |
| ListRegistries                  | Yes      |
| CreateRegistryRecord            | No       |
| GetRegistryRecord               | Yes      |
| UpdateRegistryRecord            | No       |
| DeleteRegistryRecord            | No       |
| ListRegistryRecords             | Yes      |
| SubmitRegistryRecordForApproval | No       |
| UpdateRegistryRecordStatus      | No       |

Customer free-text fields such as `name`, `description`, `statusReason`, and descriptor `data` are redacted to `HIDDEN_DUE_TO_SECURITY_REASONS`. The `clientToken` (an idempotency token, not a secret) is preserved in clear text.

### Sample management event — CreateRegistry

```
{
  "eventVersion": "1.11",
  "eventSource": "agent-registry.amazonaws.com",
  "eventName": "CreateRegistry",
  "eventCategory": "Management",
  "eventType": "AwsApiCall",
  "readOnly": false,
  "managementEvent": true,
  "awsRegion": "us-east-1",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "requestID": "b2c3d4e5-6789-01bc-def0-EXAMPLE22222",
  "sourceIPAddress": "192.0.2.1",
  "recipientAccountId": "123456789012",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:Alice",
    "arn": "arn:aws:sts::123456789012:assumed-role/Admin/Alice",
    "accountId": "123456789012",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/Admin",
        "accountId": "123456789012",
        "userName": "Admin"
      },
      "attributes": {
        "creationDate": "2026-07-14T20:46:07Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "requestParameters": {
    "name": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "description": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "clientToken": "12345678-1234-1234-1234-123456789012"
  },
  "responseElements": {
    "registryArn": "arn:aws:agent-registry:us-east-1:123456789012:registry/EXAMPLEregistry"
  },
  "resources": [
    {
      "type": "AWS::AgentRegistry::Registry",
      "accountId": "123456789012",
      "ARN": "arn:aws:agent-registry:us-east-1:123456789012:registry/EXAMPLEregistry"
    }
  ]
}
```

## Data events

Data events provide visibility into the resource operations performed on or within a registry. These operations are often high volume. Data events are not logged by default; you must enable them on a trail.

**Event source:**
`agent-registry.amazonaws.com`

**Resource type:**
`AWS::AgentRegistry::Registry`

Supported data events (all readOnly):

| API operation                      | Description                                                     |
| ---------------------------------- | --------------------------------------------------------------- |
| SearchDiscoverableRegistryRecords  | Search for discoverable registry records                        |
| ListDiscoverableRegistryRecords    | List discoverable registry records in a registry                |
| BatchGetDiscoverableRegistryRecord | Retrieve multiple discoverable registry records                 |
| InvokeRegistryMcp                  | Invoke the Model Context Protocol (MCP) endpoint for a registry |

###### Note

The default setting for CloudTrail is to log only management events. Ensure that you have data events enabled for your account. Because a busy registry can generate a large number of events in a short amount of time, be mindful of how long you enable data event logging.

###### Important

Additional charges apply for data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/") on the AWS website.

### Sample data event — SearchDiscoverableRegistryRecords

Customer free-text fields (`searchQuery`, `filters`) are redacted to `HIDDEN_DUE_TO_SECURITY_REASONS`. Because these are read-only operations, `responseElements` is null and is omitted.

```
{
  "eventVersion": "1.11",
  "eventSource": "agent-registry.amazonaws.com",
  "eventName": "SearchDiscoverableRegistryRecords",
  "eventCategory": "Data",
  "eventType": "AwsApiCall",
  "readOnly": true,
  "managementEvent": false,
  "awsRegion": "us-east-1",
  "eventID": "c3d4e5f6-7890-12cd-ef01-EXAMPLE33333",
  "requestID": "d4e5f6a7-8901-23de-f012-EXAMPLE44444",
  "sourceIPAddress": "192.0.2.1",
  "userAgent": "aws-sdk-java/2.0",
  "recipientAccountId": "123456789012",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROAEXAMPLEID:Alice",
    "arn": "arn:aws:sts::123456789012:assumed-role/Admin/Alice",
    "accountId": "123456789012",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROAEXAMPLEID",
        "arn": "arn:aws:iam::123456789012:role/Admin",
        "accountId": "123456789012",
        "userName": "Admin"
      },
      "attributes": {
        "creationDate": "2026-07-23T06:16:34Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "requestParameters": {
    "searchQuery": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "registryIds": ["arn:aws:agent-registry:us-east-1:123456789012:registry/EXAMPLEregistry"],
    "filters": "HIDDEN_DUE_TO_SECURITY_REASONS"
  },
  "resources": [
    {
      "type": "AWS::AgentRegistry::Registry",
      "accountId": "123456789012",
      "ARN": "arn:aws:agent-registry:us-east-1:123456789012:registry/EXAMPLEregistry"
    }
  ]
}
```

## Enabling CloudTrail logging for AWS Agent Registry

### Management events (no setup required)

Management events are logged by default and appear in the CloudTrail **Event history** for 90 days at no additional cost. To retain them longer or deliver them to Amazon S3, create a trail as described in the next section; trails include management events by default.

### Data events (require a trail with a data event selector)

To log AWS Agent Registry data events, create a trail (or edit an existing one) and add a data event selector for the `AWS::AgentRegistry::Registry` resource type.

#### Using the console

1. Open the [AWS CloudTrail console](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Trails**, then **Create trail** (or choose an existing trail and **Edit**).
3. Enter a **Trail name** and choose or create an **S3 bucket** for log delivery. Choose your other trail settings, then choose **Next**.
4. Under **Events**, select **Data events**.
5. For **Data event type**, choose **AWS Agent Registry** from the dropdown.
6. Choose a **Log selector template**:

   - **Log all events** to record every data event, or
   - **Custom** to filter by attributes such as `readOnly`, `eventName`, or `resources.ARN` (for example, to log only a specific registry).

7. Choose **Next**, review your settings, and choose **Create trail** (or **Save changes**).

After the trail is created, AWS Agent Registry data events are delivered to your S3 bucket.

#### Using the AWS CLI

Create a trail (if you don’t already have one), then attach an advanced event selector for the `AWS::AgentRegistry::Registry` resource type.

###### Note

The Amazon S3 bucket you use for log delivery must have a bucket policy that grants CloudTrail permission to write log files. If you specify a bucket that was not created through the CloudTrail console, you must attach this policy yourself. For more information, see [Amazon S3 bucket policy for CloudTrail](../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md") and [Creating a trail with the AWS CLI](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.md") in the AWS CloudTrail User Guide.

```
# 1. Create a trail (skip if you already have one; the S3 bucket must already have the
#    CloudTrail bucket policy attached — see the note above)
aws cloudtrail create-trail \
    --name my-agent-registry-trail \
    --s3-bucket-name my-cloudtrail-bucket

# 2. Log all Agent Registry data events
aws cloudtrail put-event-selectors \
    --trail-name my-agent-registry-trail \
    --advanced-event-selectors '[
      {
        "Name": "Log all Agent Registry data events",
        "FieldSelectors": [
          { "Field": "eventCategory", "Equals": ["Data"] },
          { "Field": "resources.type", "Equals": ["AWS::AgentRegistry::Registry"] }
        ]
      }
    ]'

# 3. Start logging
aws cloudtrail start-logging --name my-agent-registry-trail
```

To narrow the events you log, add more field selectors. For example, to log only a specific registry:

```
aws cloudtrail put-event-selectors \
    --trail-name my-agent-registry-trail \
    --advanced-event-selectors '[
      {
        "Name": "Log data events for one registry",
        "FieldSelectors": [
          { "Field": "eventCategory", "Equals": ["Data"] },
          { "Field": "resources.type", "Equals": ["AWS::AgentRegistry::Registry"] },
          { "Field": "resources.ARN", "Equals": ["arn:aws:agent-registry:us-east-1:123456789012:registry/EXAMPLEregistry"] }
        ]
      }
    ]'
```
