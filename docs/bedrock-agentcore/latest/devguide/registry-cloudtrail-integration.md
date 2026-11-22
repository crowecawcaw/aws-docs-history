

# AWS CloudTrail integration

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

 AWS Agent Registry is integrated with AWS CloudTrail, which provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures API calls for AWS Agent Registry as events. The calls captured include calls from the AWS Agent Registry console and code calls to the AWS Agent Registry API operations.

 AWS Agent Registry supports logging two categories of events:
+  **Management events** — Control-plane operations that create, configure, and manage registries and registry records (for example, `CreateRegistry`, `UpdateRegistryRecord`). Management events are **logged by default**; you do not need to take any action to receive them.
+  **Data events** — High-volume, data-plane operations performed on or within a registry (for example, discovering records or invoking MCP). Data events are **not logged by default**. To receive them, you must create a trail and explicitly enable data event logging for the `AWS::AgentRegistry::Registry` resource type.

For an ongoing record of events in your AWS account, including events for AWS Agent Registry, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. If you don’t configure a trail, you can still view the most recent management events in the CloudTrail console in **Event history** (data events do not appear in Event history).

## Management events
<a name="registry-cloudtrail-management-events"></a>

Management events (also called control-plane events) show management operations performed on registries and registry records. Management events are logged by default.

 **Event source:** `agent-registry.amazonaws.com` 

Supported management events:


| API operation | readOnly | 
| --- | --- | 
| CreateRegistry | No | 
| GetRegistry | Yes | 
| UpdateRegistry | No | 
| DeleteRegistry | No | 
| ListRegistries | Yes | 
| CreateRegistryRecord | No | 
| GetRegistryRecord | Yes | 
| UpdateRegistryRecord | No | 
| DeleteRegistryRecord | No | 
| ListRegistryRecords | Yes | 
| SubmitRegistryRecordForApproval | No | 
| UpdateRegistryRecordStatus | No | 
| CompleteRegistryRecordTokenAuth | No | 

 `CompleteRegistryRecordTokenAuth` is recorded when the AWS Agent Registry console completes a GitHub authorization for a skill record. For more information, see [Synchronize a skill from GitHub](registry-skill-sync-github.md).

Customer free-text fields such as `name`, `description`, `statusReason`, and descriptor `data` are redacted to `HIDDEN_DUE_TO_SECURITY_REASONS`. The `clientToken` (an idempotency token, not a secret) is preserved in clear text.

### Sample management event — CreateRegistry
<a name="registry-cloudtrail-sample-management"></a>

```json
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
<a name="registry-cloudtrail-data-events"></a>

Data events provide visibility into the resource operations performed on or within a registry. These operations are often high volume. Data events are not logged by default; you must enable them on a trail.

 **Event source:** `agent-registry.amazonaws.com` 

 **Resource type:** `AWS::AgentRegistry::Registry` 

Supported data events (all readOnly):


| API operation | Description | 
| --- | --- | 
| SearchDiscoverableRegistryRecords | Search for discoverable registry records | 
| ListDiscoverableRegistryRecords | List discoverable registry records in a registry | 
| BatchGetDiscoverableRegistryRecord | Retrieve multiple discoverable registry records | 
| InvokeRegistryMcp | Invoke the Model Context Protocol (MCP) endpoint for a registry | 

**Note**  
The default setting for CloudTrail is to log only management events. Ensure that you have data events enabled for your account. Because a busy registry can generate a large number of events in a short amount of time, be mindful of how long you enable data event logging.

**Important**  
Additional charges apply for data events. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/) on the AWS website.

### Sample data event — SearchDiscoverableRegistryRecords
<a name="registry-cloudtrail-sample-data"></a>

CloudTrail redacts customer free-text fields (`searchQuery`, `filters`) to `HIDDEN_DUE_TO_SECURITY_REASONS`, and records the `searchType` that you send in clear text. Because these are read-only operations, `responseElements` is null, and CloudTrail omits it.

```json
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
    "filters": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "searchType": "KEYWORD"
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

## Skill package and skill synchronization events
<a name="registry-cloudtrail-skills"></a>

CloudTrail events don’t record skill package content or package download URLs:
+ In `CreateRegistryRecord` and `UpdateRegistryRecord` events, the package content (`artifact.content`) is redacted to `HIDDEN_DUE_TO_SECURITY_REASONS`.
+  `GetRegistryRecord` and `BatchGetDiscoverableRegistryRecord` are read-only, so their events have no `responseElements` and don’t record the download URLs that they return.
+ In `InvokeRegistryMcp` events, tool results are redacted, so the download URLs that the batch get tool returns aren’t recorded.
+ For a GitHub source, `CreateRegistryRecord` and `UpdateRegistryRecord` events leave out the `authorizationData` that the response returns, including the authorization URL.
+ The `customParameters` of an OAuth credential provider are redacted to `HIDDEN_DUE_TO_SECURITY_REASONS`.

The following request fields of skill records appear in clear text:
+  `artifact.sha256`, the SHA-256 checksum of an uploaded package.
+ The source URL (`fromUrl.url`) of an Amazon S3 or GitHub skill source, including the bucket name and object key, or the repository, branch or tag, and folder path.
+ The IAM role ARN (`roleArn`) of an Amazon S3 source, and `bucketOwnerAccountId`.
+ The credential provider ARN (`providerArn`), the `scopes`, and the `returnUrl` of a GitHub source.
+  `repositoryProvider`, `triggerSynchronization`, and `forceAuthentication`.

Don’t put sensitive information in bucket names, object keys, repository names, branch or tag names, folder paths, or `returnUrl`.

Skill synchronization also produces events from other services in your account:
+ When AWS Agent Registry reads an Amazon S3 source with an IAM role, CloudTrail records an `AssumeRole` event for the role. The role session name is `AgentCore-RegistryRecord-<recordId>`.
+ For a registry encrypted with a customer managed key, AWS KMS events record the use of your key. For more information, see [Monitoring how AWS Agent Registry uses your key](registry-data-encryption.md#registry-encryption-monitoring).

## Enabling CloudTrail logging for AWS Agent Registry
<a name="registry-cloudtrail-enabling"></a>

### Management events (no setup required)
<a name="registry-cloudtrail-management-setup"></a>

Management events are logged by default and appear in the CloudTrail **Event history** for 90 days at no additional cost. To retain them longer or deliver them to Amazon S3, create a trail as described in the next section; trails include management events by default.

### Data events (require a trail with a data event selector)
<a name="registry-cloudtrail-data-setup"></a>

To log AWS Agent Registry data events, create a trail (or edit an existing one) and add a data event selector for the `AWS::AgentRegistry::Registry` resource type.

#### Using the console
<a name="registry-cloudtrail-data-console"></a>

1. Open the [AWS CloudTrail console](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, choose **Trails**, then **Create trail** (or choose an existing trail and **Edit**).

1. Enter a **Trail name** and choose or create an **S3 bucket** for log delivery. Choose your other trail settings, then choose **Next**.

1. Under **Events**, select **Data events**.

1. For **Data event type**, choose ** AWS Agent Registry** from the dropdown.

1. Choose a **Log selector template**:
   +  **Log all events** to record every data event, or
   +  **Custom** to filter by attributes such as `readOnly`, `eventName`, or `resources.ARN` (for example, to log only a specific registry).

1. Choose **Next**, review your settings, and choose **Create trail** (or **Save changes**).

After the trail is created, AWS Agent Registry data events are delivered to your S3 bucket.

#### Using the AWS CLI
<a name="registry-cloudtrail-data-cli"></a>

Create a trail (if you don’t already have one), then attach an advanced event selector for the `AWS::AgentRegistry::Registry` resource type.

**Note**  
The Amazon S3 bucket you use for log delivery must have a bucket policy that grants CloudTrail permission to write log files. If you specify a bucket that was not created through the CloudTrail console, you must attach this policy yourself. For more information, see [Amazon S3 bucket policy for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html) and [Creating a trail with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail-by-using-the-aws-cli-create-trail.html) in the AWS CloudTrail User Guide.

```bash
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

```bash
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