

# Logging Amazon S3 data events for data governance, security, and compliance
<a name="logging-s3-data-events-governance"></a>

Amazon S3 often stores an organization's most sensitive data, such as customer records, financial reports, and intellectual property. CloudTrail data events record object-level activity on that data: who read it, who changed it, who deleted it, and when. Data events also record operations that Amazon S3 performs on your behalf, such as lifecycle expirations and storage class transitions. This gives you a complete record of how each object changed over time.

This section describes how you can use Amazon S3 data events to:

Govern your data  
Know who uses your data and how it changes over its lifecycle.

Secure your data  
Detect and investigate data exfiltration, destructive activity, and credential misuse.

Prove compliance  
Show auditors evidence of access, retention, and deletion.

By default, trails don't log data events. Additional charges apply for data events. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

**Contents**
+ [Amazon S3 resource types for data events](#logging-s3-data-events-resource-types)
  + [Identify who performed an action](#logging-s3-data-events-identify-actor)
+ [Data governance: know who uses your data and how it changes](#logging-s3-data-events-data-governance)
+ [Security: detect and investigate threats](#logging-s3-data-events-security)
  + [Investigate authentication failures](#logging-s3-data-events-investigate-authn-failures)
  + [Determine whether a person or a lifecycle rule deleted an object](#logging-s3-data-events-who-deleted-object)
+ [Compliance: prove your controls work](#logging-s3-data-events-compliance)
  + [Verify that Amazon S3 data event logging is turned on](#logging-s3-data-events-verify-logging)
+ [Logging and excluding Amazon S3 lifecycle and authentication failure events](#logging-s3-lifecycle-authn-events)
  + [Amazon S3 lifecycle events](#logging-s3-lifecycle-events)
  + [Considerations](#logging-s3-lifecycle-authn-considerations)
  + [Examples: Log Amazon S3 lifecycle and authentication failure events](#logging-s3-lifecycle-authn-examples-log)
    + [Example 1: Log all Amazon S3 data events, including lifecycle and authentication failure events](#logging-s3-example-log-all)
    + [Example 2: Log only lifecycle events](#logging-s3-example-log-lifecycle-only)
    + [Example 3: Log only authentication failure events](#logging-s3-example-log-authn-only)
    + [Example 4: Log lifecycle events for a specific bucket](#logging-s3-example-log-lifecycle-one-bucket)
  + [Examples: Exclude Amazon S3 lifecycle and authentication failure events](#logging-s3-lifecycle-authn-examples-exclude)
    + [Example 5: Exclude lifecycle events](#logging-s3-example-exclude-lifecycle)
    + [Example 6: Exclude authentication failure events](#logging-s3-example-exclude-authn)
    + [Example 7: Exclude both lifecycle and authentication failure events](#logging-s3-example-exclude-both)
    + [Example 8: Exclude lifecycle storage class transitions only](#logging-s3-example-exclude-transitions)
    + [Exclude lifecycle events by using the console](#logging-s3-example-exclude-lifecycle-console)

## Amazon S3 resource types for data events
<a name="logging-s3-data-events-resource-types"></a>

To log Amazon S3 data events, specify one or more of the following values for the `resources.type` field in your trail's advanced event selectors. For the full list of resource types, see [Data events](logging-data-events-with-cloudtrail.md#logging-data-events).



| Resource type | resources.type value | Description | 
| --- | --- | --- | 
| S3 | AWS::S3::Object | Object-level activity in general purpose buckets. Includes Amazon S3 lifecycle events and authentication failure events. | 
| S3 Access Point | AWS::S3::AccessPoint | Activity on objects accessed through access points for general purpose buckets. | 
| S3 Express | AWS::S3Express::Object | Object-level activity in directory buckets. | 
| S3 Express Access Point | AWS::S3Express::AccessPoint | Activity on objects accessed through access points for directory buckets. | 
| S3 Object Lambda | AWS::S3ObjectLambda::AccessPoint | Activity on Amazon S3 Object Lambda access points. | 
| S3 Outposts | AWS::S3Outposts::Object | Object-level activity on Amazon S3 on Outposts. | 
| S3 table | AWS::S3Tables::Table | Activity on tables in Amazon S3 Tables. | 
| S3 table bucket | AWS::S3Tables::TableBucket | Activity on table buckets in Amazon S3 Tables. | 
| S3 vector index | AWS::S3Vectors::Index | Activity on vector indexes in Amazon S3 Vectors. | 
| S3 vector bucket | AWS::S3Vectors::VectorBucket | Activity on vector buckets in Amazon S3 Vectors. | 

### Identify who performed an action
<a name="logging-s3-data-events-identify-actor"></a>

Each Amazon S3 data event has an `eventType` value that tells you whether a person or application performed the action, or whether Amazon S3 performed it.
+ `AwsApiCall`: A principal, such as an IAM user, role, or application, made the request.
+ `AwsServiceEvent`: Amazon S3 performed the action on your behalf, for example because of a lifecycle rule or a replication configuration.

The following Amazon S3 data events are service-initiated (`AwsServiceEvent`) events.



| Event source | Event names | What triggers the event | 
| --- | --- | --- | 
| s3lifecycle.amazonaws.com | `ExpireObject`, `CreateDeleteMarker`, `DeleteUpload`, `TransitionObject`, `TransitionSIAObject`, `TransitionZIAObject`, `TransitionINTObject`, `TransitionGIRObject`, `TransitionGDAObject` | An Amazon S3 Lifecycle rule. For more information about Amazon S3 Lifecycle events, see [Amazon S3 lifecycle events](#logging-s3-lifecycle-events). | 
| s3.amazonaws.com | `InitiateReplication` | Amazon S3 Replication starts to replicate an object. | 
| s3.amazonaws.com | `S3ComputeChecksum`, `S3ComputeObjectChecksum` | Amazon S3 computes a checksum for an object. | 
| `s3.amazonaws.com`, `s3express.amazonaws.com` | `DeleteObject` | Amazon S3 deletes an object on your behalf. | 

## Data governance: know who uses your data and how it changes
<a name="logging-s3-data-events-data-governance"></a>

Data governance requires visibility into which principals access your critical data stores, where your data comes from, and what happens to it over time. Amazon S3 data events help you answer the following questions.



| Question | Data events that answer it | 
| --- | --- | 
| Who read or searched this data? | `GetObject`, `HeadObject`, `GetObjectAttributes`, `SelectObjectContent`, `GetObjectTorrent`, `ListObjects`, `ListObjectVersions`, `GetVectors`, `QueryVectors`, `ListVectors`, `WriteGetObjectResponse` | 
| Where did this data come from? | `PutObject`, `CopyObject`, `CreateMultipartUpload`, `UploadPart`, `UploadPartCopy`, `CompleteMultipartUpload`, `RestoreObject`, `RenameObject`, `PutVectors` | 
| How is this data classified? | `PutObjectTagging`, `GetObjectTagging`, `DeleteObjectTagging` | 
| What happened to this data over its lifecycle? | All events with the `s3lifecycle.amazonaws.com` event source | 

## Security: detect and investigate threats
<a name="logging-s3-data-events-security"></a>

When a security incident occurs, Amazon S3 data events show which objects were accessed, which principal accessed them, from which IP address or VPC endpoint, and at what time. Use the following events to detect and investigate common threats.



| Scenario | Data events to analyze | 
| --- | --- | 
| Data exfiltration | High volumes of `GetObject`, `SelectObjectContent`, or `QueryVectors` from a single principal, IP address (`sourceIPAddress`), or VPC endpoint (`vpcEndpointId`) | 
| Destructive or ransomware-like activity | `DeleteObject`, `DeleteObjects`, `DeleteVectors`, overwrites with `PutObject`, and `UpdateObjectEncryption` | 
| Changes to object permissions | `PutObjectAcl`, `GetObjectAcl` | 
| Credential misuse and probing | Events with the `s3-authn-errors.amazonaws.com` event source | 
| Directory bucket session activity | `CreateSession` | 

### Investigate authentication failures
<a name="logging-s3-data-events-investigate-authn-failures"></a>

Amazon S3 authentication failure events record requests that Amazon S3 rejected because the request couldn't be authenticated. These events use the `s3-authn-errors.amazonaws.com` event source.

A spike in authentication failures can indicate that someone is using stolen, expired, or guessed credentials against your buckets. Other failed requests, such as requests denied by a bucket policy (`AccessDenied`), are logged with their original event source and event name.

### Determine whether a person or a lifecycle rule deleted an object
<a name="logging-s3-data-events-who-deleted-object"></a>

Check the `eventType` and `eventSource` fields of the event. If `eventType` is `AwsServiceEvent` and `eventSource` is `s3lifecycle.amazonaws.com`, a lifecycle rule removed the object. If `eventType` is `AwsApiCall`, the `userIdentity` element shows which principal deleted it.

## Compliance: prove your controls work
<a name="logging-s3-data-events-compliance"></a>

Regulated industries must continuously prove who accessed what data, when, and whether that access was authorized. Amazon S3 data events provide this evidence at the API-call level, recorded by AWS rather than reported by your application.



| Requirement | Data events and features | 
| --- | --- | 
| Proof of deletion or retention | `DeleteObject`, `DeleteObjects`, and lifecycle events such as `ExpireObject` and `CreateDeleteMarker`. These events show when each object was removed and whether a principal or a lifecycle rule removed it. | 
| Data residency | `InitiateReplication` events show when Amazon S3 replicates objects, so you can confirm where copies of your data go. | 
| Access reviews | Read events, such as `GetObject` and `HeadObject`, on in-scope buckets show who accessed regulated data. | 
| Continuous monitoring of logging | Use AWS Config and AWS Security Hub CSPM to verify that Amazon S3 data event logging stays turned on. See the following section. | 

### Verify that Amazon S3 data event logging is turned on
<a name="logging-s3-data-events-verify-logging"></a>

Use the following controls to check continuously that your accounts log Amazon S3 data events:
+ **AWS Config**: The [cloudtrail-s3-dataevents-enabled](https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-s3-dataevents-enabled.html) managed rule checks whether at least one trail logs Amazon S3 data events for all buckets, or for the buckets that you specify.
+ **AWS Security Hub CSPM**: The `S3.22` and `S3.23` controls check whether your account logs object-level write events and read events for all general purpose buckets.

To protect the integrity of your logs, turn on log file integrity validation for your trails. For more information about log file integrity validation, see [Validating CloudTrail log file integrity](cloudtrail-log-file-validation-intro.md).

## Logging and excluding Amazon S3 lifecycle and authentication failure events
<a name="logging-s3-lifecycle-authn-events"></a>

CloudTrail logs two categories of Amazon S3 data events that aren't direct requests from your principals:
+ **Lifecycle events** record actions that Amazon S3 performs because of your Amazon S3 Lifecycle rules. These events use the `s3lifecycle.amazonaws.com` event source and the `AwsServiceEvent` event type.
+ **Authentication failure events** record requests that Amazon S3 rejected because they couldn't be authenticated. These events use the `s3-authn-errors.amazonaws.com` event source.

Both categories are logged for the `AWS::S3::Object` resource type (general purpose buckets). If your trail already logs `AWS::S3::Object` data events, you receive these events automatically. You don't need to change your configuration. These events are charged as data events.

### Amazon S3 lifecycle events
<a name="logging-s3-lifecycle-events"></a>



| Event name | Description | S3 server access logs operation | 
| --- | --- | --- | 
| ExpireObject | A lifecycle rule permanently deleted an object. | S3.EXPIRE.OBJECT | 
| CreateDeleteMarker | A lifecycle rule added a delete marker to an object in a versioned bucket. | S3.CREATE.DELETEMARKER | 
| DeleteUpload | A lifecycle rule stopped an incomplete multipart upload and deleted its parts. | S3.DELETE.UPLOAD | 
| TransitionObject | A lifecycle rule moved an object to S3 Glacier Flexible Retrieval. | S3.TRANSITION.OBJECT | 
| TransitionSIAObject | A lifecycle rule moved an object to S3 Standard-IA. | S3.TRANSITION\_SIA.OBJECT | 
| TransitionZIAObject | A lifecycle rule moved an object to S3 One Zone-IA. | S3.TRANSITION\_ZIA.OBJECT | 
| TransitionINTObject | A lifecycle rule moved an object to S3 Intelligent-Tiering. | S3.TRANSITION\_INT.OBJECT | 
| TransitionGIRObject | A lifecycle rule moved an object to S3 Glacier Instant Retrieval. | S3.TRANSITION\_GIR.OBJECT | 
| TransitionGDAObject | A lifecycle rule moved an object to S3 Glacier Deep Archive. | S3.TRANSITION\_GDA.OBJECT | 

Each lifecycle event includes the bucket name, object key, version ID, object size, and, for transitions, the destination storage class.

### Considerations
<a name="logging-s3-lifecycle-authn-considerations"></a>
+ To log only some of these events, or to exclude them, use advanced event selectors with a condition on the `eventSource` field. Basic event selectors can't filter on `eventSource`.
+ Trails can use either basic event selectors or advanced event selectors, but not both. If you apply advanced event selectors to a trail, they overwrite its existing basic event selectors.
+ A condition of `eventType` `NotEquals` `AwsServiceEvent`, or the **Exclude AWS service initiated events** log selector template in the console, excludes lifecycle events and all other service-initiated Amazon S3 events, such as `InitiateReplication` and checksum events. To exclude only lifecycle events, filter on `eventSource` instead.
+ When you specify more than one value for a `NotEquals` condition, CloudTrail excludes events that match any of the values. For more information, see [How CloudTrail evaluates multiple conditions for a field](filtering-data-events.md#filtering-data-events-conditions).

### Examples: Log Amazon S3 lifecycle and authentication failure events
<a name="logging-s3-lifecycle-authn-examples-log"></a>

**Topics**
+ [Example 1: Log all Amazon S3 data events, including lifecycle and authentication failure events](#logging-s3-example-log-all)
+ [Example 2: Log only lifecycle events](#logging-s3-example-log-lifecycle-only)
+ [Example 3: Log only authentication failure events](#logging-s3-example-log-authn-only)
+ [Example 4: Log lifecycle events for a specific bucket](#logging-s3-example-log-lifecycle-one-bucket)

#### Example 1: Log all Amazon S3 data events, including lifecycle and authentication failure events
<a name="logging-s3-example-log-all"></a>

The following AWS CLI command configures a trail to log all data events for objects in general purpose buckets. The trail logs object API activity, lifecycle events, and authentication failure events.

```
aws cloudtrail put-event-selectors \
--trail-name {{trailName}} \
--advanced-event-selectors \
'[
  {
    "Name": "Log all S3 data events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] }
    ]
  }
]'
```

#### Example 2: Log only lifecycle events
<a name="logging-s3-example-log-lifecycle-only"></a>

The following AWS CLI command configures a trail to log only Amazon S3 lifecycle events. You can use a dedicated trail that delivers to a separate S3 bucket to give auditors evidence of retention and deletion without giving them access to your other activity.

```
aws cloudtrail put-event-selectors \
--trail-name {{trailName}} \
--advanced-event-selectors \
'[
  {
    "Name": "Log only S3 lifecycle events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventSource", "Equals": ["s3lifecycle.amazonaws.com"] }
    ]
  }
]'
```

#### Example 3: Log only authentication failure events
<a name="logging-s3-example-log-authn-only"></a>

The following AWS CLI command configures a trail to log only Amazon S3 authentication failure events. You can send these events to a trail that your security team monitors for credential misuse.

```
aws cloudtrail put-event-selectors \
--trail-name {{trailName}} \
--advanced-event-selectors \
'[
  {
    "Name": "Log only S3 authentication failure events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventSource", "Equals": ["s3-authn-errors.amazonaws.com"] }
    ]
  }
]'
```

#### Example 4: Log lifecycle events for a specific bucket
<a name="logging-s3-example-log-lifecycle-one-bucket"></a>

The following AWS CLI command configures a trail to log lifecycle events for objects in one bucket. Replace {{amzn-s3-demo-bucket}} with the name of your bucket.

```
aws cloudtrail put-event-selectors \
--trail-name {{trailName}} \
--advanced-event-selectors \
'[
  {
    "Name": "Log S3 lifecycle events for one bucket",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventSource", "Equals": ["s3lifecycle.amazonaws.com"] },
      { "Field": "resources.ARN", "StartsWith": ["arn:aws:s3:::amzn-s3-demo-bucket/"] }
    ]
  }
]'
```

### Examples: Exclude Amazon S3 lifecycle and authentication failure events
<a name="logging-s3-lifecycle-authn-examples-exclude"></a>

If you don't need these events, you can exclude them to reduce costs while you continue to log all other Amazon S3 data events.

**Topics**
+ [Example 5: Exclude lifecycle events](#logging-s3-example-exclude-lifecycle)
+ [Example 6: Exclude authentication failure events](#logging-s3-example-exclude-authn)
+ [Example 7: Exclude both lifecycle and authentication failure events](#logging-s3-example-exclude-both)
+ [Example 8: Exclude lifecycle storage class transitions only](#logging-s3-example-exclude-transitions)
+ [Exclude lifecycle events by using the console](#logging-s3-example-exclude-lifecycle-console)

#### Example 5: Exclude lifecycle events
<a name="logging-s3-example-exclude-lifecycle"></a>

The following AWS CLI command configures a trail to log all Amazon S3 data events except lifecycle events. The trail continues to log all requests made by your principals.

```
aws cloudtrail put-event-selectors \
--trail-name {{trailName}} \
--advanced-event-selectors \
'[
  {
    "Name": "Log S3 data events but exclude lifecycle events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventSource", "NotEquals": ["s3lifecycle.amazonaws.com"] }
    ]
  }
]'
```

#### Example 6: Exclude authentication failure events
<a name="logging-s3-example-exclude-authn"></a>

The following AWS CLI command configures a trail to log all Amazon S3 data events except authentication failure events. The trail continues to log all other Amazon S3 data events, including other failed requests such as `AccessDenied` errors.

```
aws cloudtrail put-event-selectors \
--trail-name {{trailName}} \
--advanced-event-selectors \
'[
  {
    "Name": "Log S3 data events but exclude authentication failure events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventSource", "NotEquals": ["s3-authn-errors.amazonaws.com"] }
    ]
  }
]'
```

#### Example 7: Exclude both lifecycle and authentication failure events
<a name="logging-s3-example-exclude-both"></a>

The following AWS CLI command configures a trail to log all Amazon S3 data events except lifecycle and authentication failure events.

```
aws cloudtrail put-event-selectors \
--trail-name {{trailName}} \
--advanced-event-selectors \
'[
  {
    "Name": "Log S3 data events but exclude lifecycle and authentication failure events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventSource", "NotEquals": ["s3lifecycle.amazonaws.com", "s3-authn-errors.amazonaws.com"] }
    ]
  }
]'
```

#### Example 8: Exclude lifecycle storage class transitions only
<a name="logging-s3-example-exclude-transitions"></a>

Storage class transitions are often the highest-volume lifecycle events. The following AWS CLI command logs all Amazon S3 data events, including lifecycle expirations, delete markers, and incomplete multipart upload cleanups, but excludes storage class transitions. The example uses two selectors: the first logs all non-lifecycle events, and the second logs lifecycle events whose names don't start with `Transition`.

```
aws cloudtrail put-event-selectors \
--trail-name {{trailName}} \
--advanced-event-selectors \
'[
  {
    "Name": "Log S3 data events except lifecycle events",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventSource", "NotEquals": ["s3lifecycle.amazonaws.com"] }
    ]
  },
  {
    "Name": "Log S3 lifecycle events except transitions",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::S3::Object"] },
      { "Field": "eventSource", "Equals": ["s3lifecycle.amazonaws.com"] },
      { "Field": "eventName", "NotStartsWith": ["Transition"] }
    ]
  }
]'
```

#### Exclude lifecycle events by using the console
<a name="logging-s3-example-exclude-lifecycle-console"></a>

1. Open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1. In the navigation pane, choose **Trails**, and then choose the trail that you want to update.

1. In **Data events**, choose **Edit**.

1. For **Resource type**, select **S3**.

1. For **Log selector template**, select **Custom**.

1. Under **Advanced event selectors**, choose **\+ Condition**. For **Field**, select `eventSource`. For **Operator**, select **does not equal**. For **Value**, enter `s3lifecycle.amazonaws.com`.

1. To also exclude authentication failure events, add a second value of `s3-authn-errors.amazonaws.com`.

1. Choose **Save changes**.