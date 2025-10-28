# Enrich CloudTrail events by adding resource tag

keys and IAM global condition keys

You can enrich CloudTrail management events and data events by adding resource tag keys, principal
tag keys, and IAM global condition keys when you create or update an event data store.
This allows you to categorize, search, and analyze CloudTrail events based on the business
context, such as cost allocation and financial management, operations, and data security
requirements. You can analyze events by running queries in CloudTrail Lake. You can also choose to
[federate](query-federation.md "query-federation.md") your event data store and run queries
in Amazon Athena. You can add resource tag keys and IAM global condition keys to an event data
store using the [CloudTrail console](query-event-data-store-cloudtrail.md "query-event-data-store-cloudtrail.md"), [AWS CLI](lake-cli-manage-eds.md#lake-cli-put-event-configuration "lake-cli-manage-eds.md#lake-cli-put-event-configuration"), and SDKs.

###### Note

Resource tags that you add after resource creation or updates might experience a delay
before those tags are reflected in CloudTrail events. CloudTrail events for resource deletions might
not include tag information.

IAM global condition keys will always be visible in the output of a query, but might
not be visible to the resource owner.

When you add resource tag keys to enriched events, CloudTrail includes the selected tag keys
associated with the resources that were involved in the API call.

When you add IAM global condition keys to an event data store, CloudTrail includes information
about the selected condition keys that were evaluated during the authorization process,
including additional details about the principal, session, and the request itself.

###### Note

Configuring CloudTrail to include a condition key or principal tag does not mean that this
condition key or principal tag will be present in every event. For example, if you've
set up CloudTrail to include a specific global condition key but you don't see it in a
particular event, this indicates that the key wasn't relevant to the IAM policy
evaluation for that action.

After you add resource tag keys or IAM condition keys, CloudTrail includes a
`eventContext` field in CloudTrail events that provides the selected contextual
information for the API action.

There are some exceptions when the event will not include the `eventContext`
field, including the following:

- API events related to deleted resources might or might not have resource tags.
- The `eventContext` field will not have data for delayed events, and will not be
  present for events that were updated after the API call. For example, if there is a
  delay or outage for Amazon EventBridge, tags for events might remain out of date for some time
  after the outage is resolved. Some AWS services will experience longer delays. For
  more information, see [Resource tag updates in CloudTrail for enriched events](#resrouce-tags-updates "#resrouce-tags-updates").
- If you modify or delete the AWSServiceRoleForCloudTrailEventContext service-linked role used for enriched events,
  CloudTrail will not populate any resource tags into `eventContext` .

###### Note

The `eventContext` field is only present in events for event data stores that are
configured to include resource tag keys, principal tag keys, and IAM global condition
keys. Events delivered to **Event history**, Amazon EventBridge, viewable with
the AWS CLI `lookup-events` command, and delivered to trails, will not include
the `eventContext` field.

###### Topics

- [AWS services supporting resource
  tags](#resource-tags-supported-services "#resource-tags-supported-services")
- [AWS services supporting IAM
  global condition keys](#condition-keys-supported-services "#condition-keys-supported-services")
- [Event examples](#context-event-examples "#context-event-examples")

## AWS services supporting resource

tags

All AWS services support resource tags. For more information, see [Services
that support the AWS Resource Groups Tagging API](../../../resourcegroupstagging/latest/APIReference/supported-services.md "../../../resourcegroupstagging/latest/APIReference/supported-services.md") .

### Resource tag updates in CloudTrail for enriched events

When configured to do so, CloudTrail captures information about resource tags and uses them to
provide information in enriched events. When working with resource tags, there are
certain conditions in which a resource tag might not be accurately reflected at the
time of the system request for events. During standard operation, tags applied at
resource creation time are always present and will experience minimal or no delays.
However, the following services are expected to have delays in resource tag changes
appearing in CloudTrail events:

- Amazon Chime Voice Connector
- AWS CloudTrail
- AWS CodeConnections
- Amazon DynamoDB
- Amazon ElastiCache
- Amazon Keyspaces (for Apache Cassandra)
- Amazon Kinesis
- Amazon Lex
- Amazon MemoryDB
- Amazon S3
- Amazon Security Lake
- AWS Direct Connect
- AWS IAM Identity Center
- AWS Key Management Service
- AWS Lambda
- AWS Marketplace Vendor Insights
- AWS Organizations
- AWS Payment Cryptography
- Amazon Simple Queue Service

Service outages can also cause delays in updates to resource tag information. In the event
of a service outage delay, subsequent CloudTrail events will include an
`addendum` field that includes information about the resource tag
change. This additional information will be used as specified to provide enriched
CloudTrailevents.

## AWS services supporting IAM

global condition keys

The following AWS services support IAM global condition keys for enriched events:

- AWS Certificate Manager
- AWS CloudTrail
- Amazon CloudWatch
- Amazon CloudWatch Logs
- AWS CodeBuild
- AWS CodeCommit
- AWS CodeDeploy
- Amazon Cognito Sync
- Amazon Comprehend
- Amazon Comprehend Medical
- Amazon Connect Voice ID
- AWS Control Tower
- Amazon Data Firehose
- Amazon Elastic Block Store
- Elastic Load Balancing
- AWS End User Messaging Social
- Amazon EventBridge
- Amazon EventBridge Scheduler
- Amazon Data Firehose
- Amazon FSx
- AWS HealthImaging
- AWS IoT Events
- AWS IoT FleetWise
- AWS IoT SiteWise
- AWS IoT TwinMaker
- AWS IoT Wireless
- Amazon Kendra
- AWS KMS
- AWS Lambda
- AWS License Manager
- Amazon Lookout for Equipment
- Amazon Lookout for Vision
- AWS Network Firewall
- AWS Payment Cryptography
- Amazon Personalize
- AWS Proton
- Amazon Rekognition
- Amazon SageMaker AI
- AWS Secrets Manager
- Amazon Simple Email Service (Amazon SES)
- Amazon Simple Notification Service (Amazon SNS)
- Amazon SQS
- AWS Step Functions
- AWS Storage Gateway
- Amazon SWF
- AWS Supply Chain
- Amazon Timestream
- Amazon Timestream for InfluxDB
- Amazon Transcribe
- AWS Transfer Family
- AWS Trusted Advisor
- Amazon WorkSpaces
- AWS X-Ray

### Supported IAM global condition keys for enriched events

The following table lists the supported IAM global condition keys for CloudTrail enriched
events, with example values:

| Global Condition Keys and Sample Values | Key                                               | Example value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws:FederatedProvider`                 | "`IdP`"                                           |
| `aws:TokenIssueTime`                    | "`123456789`"                                     |
| `aws:MultiFactorAuthAge`                | "99"                                              |
| `aws:MultiFactorAuthPresent`            | "`true`"                                          |
| `aws:SourceIdentity`                    | "`UserName`"                                      |
| `aws:PrincipalAccount`                  | "111122223333"                                    |
| `aws:PrincipalArn`                      | "arn:aws:iam::`555555555555:role/myRole`"         |
| `aws:PrincipalIsAWSService`             | "`false`"                                         |
| `aws:PrincipalOrgI`D                    | "`o-rganization`"                                 |
| `aws:PrincipalOrgPaths`                 | ["`o-rganization/path-of-org`"]                   |
| `aws:PrincipalServiceName`              | "`cloudtrail.amazonaws.com`"                      |
| `aws:PrincipalServiceNamesList`         | ["`cloudtrail.amazonaws.com","s3.amazonaws.com`"] |
| `aws:PrincipalType`                     | "`AssumedRole`"                                   |
| `aws:userid`                            | "`userid`"                                        |
| `aws:username`                          | "`username`"                                      |
| `aws:RequestedRegion`                   | `us-east-2`"                                      |
| `aws:SecureTransport`                   | "`true`"                                          |
| `aws:ViaAWSService`                     | "`false`"                                         |
| `aws:CurrentTime`                       | "`2025-04-30 15:30:00`"                           |
| `aws:EpochTime`                         | "`1746049800`"                                    |
| `aws:SourceAccount`                     | "`111111111111`"                                  |
| `aws:SourceOrgID`                       | "`o-rganization`"                                 | ## Event examples In the following example, the `eventContext` field includes IAM global condition key `aws:ViaAWSService` with a value of `false`, which indicates the API call was not made by an AWS service. `{ "eventVersion": "1.11", "userIdentity": { "type": "AssumedRole", "principalId": "ASIAIOSFODNN7EXAMPLE", "arn": "arn:aws:sts::123456789012:assumed-role/admin", "accountId": "123456789012", "accessKeyId": "ASIAIOSFODNN7EXAMPLE", "sessionContext": { "sessionIssuer": { "type": "Role", "principalId": "ASIAIOSFODNN7EXAMPLE", "arn": "arn:aws:iam::123456789012:role/admin", "accountId": "123456789012", "userName": "admin" }, "attributes": { "creationDate": "2025-01-22T22:05:56Z", "mfaAuthenticated": "false" } } }, "eventTime": "2025-01-22T22:06:16Z", "eventSource": "cloudtrail.amazonaws.com", "eventName": "GetTrailStatus", "awsRegion": "us-east-1", "sourceIPAddress": "192.168.0.0", "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:133.0) Gecko/20100101 Firefox/133.0", "requestParameters": { "name": "arn:aws:cloudtrail:us-east-1:123456789012:trail/myTrail" }, "responseElements": null, "requestID": "d09c4dd2-5698-412b-be7a-example1a23", "eventID": "9cb5f426-7806-46e5-9729-exampled135d", "readOnly": true, "eventType": "AwsApiCall", "managementEvent": true, "recipientAccountId": "123456789012", "eventCategory": "Management", "tlsDetails": { "tlsVersion": "TLSv1.3", "cipherSuite": "TLS_AES_128_GCM_SHA256", "clientProvidedHostHeader": "cloudtrail.us-east-1.amazonaws.com" }, "sessionCredentialFromConsole": "true", "eventContext": { "requestContext": { "aws:ViaAWSService": "false" }, "tagContext": {} } }` |
