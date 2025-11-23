# Monitor and log with AWS CloudTrail

AWS CloudTrail is a service that provides a record of actions taken by a user, role, or an AWS
service. CloudTrail records all API calls as events. You can use Amazon Location Service with CloudTrail to monitor
your API calls, which include calls from the Amazon Location Service console and AWS SDK calls to the
Amazon Location Service API operations.

CloudTrail is automatically enabled when you create your AWS account. When activity occurs in
Amazon Location Service, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download event
history for the past 90 days per AWS Region.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md"). There are no CloudTrail charges for viewing the **Event history**.

For an ongoing records of events in your AWS account past 90 days, including events from
Amazon Location Service, create a trail or a [CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") data
store.

**CloudTrail trails**

A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. When you create a trail in
AWS Management Console, the trail applies to all AWS Regions. The trail logs events from all regions in
the AWS Partition and delivers the log files to the S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and act upon the
event data collected in CloudTrail logs.

For more information on how to create a trail, see [Overview
for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md").

For a list of CloudTrail supported services and integrations, see [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations").

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no
charge from CloudTrail by creating a trail. However, there are Amazon S3 storage charges.

For more information about CloudTrail pricing, see [AWS CloudTrail pricing](https://aws.amazon.com//cloudtrail/pricing/ "https://aws.amazon.com//cloudtrail/pricing/").

For information about Amazon S3 pricing, see [Amazon S3
pricing](https://aws.amazon.com//s3/pricing/ "https://aws.amazon.com//s3/pricing/").

**CloudTrail Lake event data stores**

CloudTrail Lake lets you run SQL-based queries on your events. Events are aggregated into
_event data stores_, which are immutable collections of
events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store
control which events persist and are available for you to query.

For more information about CloudTrail Lake, see [Working with AWS CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md").

CloudTrail Lake event data stores and queries incur costs. When you create an event data store,
you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option
determines the cost for ingesting and storing events, and the default and maximum retention
period for the event data store.

For more information about CloudTrail pricing, see [AWS CloudTrail pricing](https://aws.amazon.com//cloudtrail/pricing/ "https://aws.amazon.com//cloudtrail/pricing/").

###### Topics

- [Amazon Location management events in
  CloudTrail](#cloudtrail-management-events "#cloudtrail-management-events")
- [Amazon Location data events in CloudTrail](#cloudtrail-data-events "#cloudtrail-data-events")
- [Learn about Amazon Location Service log file entries](#cloudtrail-log-entries "#cloudtrail-log-entries")
- [Example: CloudTrail log file entry for an Amazon Location management event](#cloudtrail-management-event-example "#cloudtrail-management-event-example")
- [Example: CloudTrail log file entry for an Amazon Location data event](#cloudtrail-data-event-example "#cloudtrail-data-event-example")

## Amazon Location management events in

CloudTrail

You can view Amazon Location management events in your CloudTrail event history. These events
include all API calls that manage Amazon Location resources and configurations. For a complete
list of supported actions, refer to the [Amazon Location Service API references](../../previous/APIReference/index.md "../../previous/APIReference/index.md").

## Amazon Location data events in CloudTrail

Data events provide information about operations performed directly on a resource.
These events, also known as data plane operations, can be high-volume. By default, CloudTrail
does not log data events, and the CloudTrail Event History does not record them. You incur
additional charges when you enable data events. For more information about CloudTrail pricing,
see [AWS CloudTrail
Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can choose which Amazon Location resource types log data events by using the CloudTrail
console, AWS CLI, or CloudTrail API operations. For instructions on how to enable and manage
data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-console.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-console.md") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cli.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cli.md") .

The following table lists the Amazon Location resource types for which you can log data
events:

| Supported Amazon Location Data Events | Data event type (console) | resources.type value                                                                                                                                                            | Data APIs logged to CloudTrail |
| ------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| Geo Maps                              | AWS::GeoMaps::Provider    | See the Amazon [GeoMaps API](../APIReference/Welcome.md#Welcome_Amazon_Location_Service_Maps "../APIReference/Welcome.md#Welcome_Amazon_Location_Service_Maps") reference       |
| Geo Places                            | AWS::GeoPlaces::Provider  | See the Amazon [GeoPlaces API](../APIReference/Welcome.md#Welcome_Amazon_Location_Service_Places "../APIReference/Welcome.md#Welcome_Amazon_Location_Service_Places") reference |
| Geo Routes                            | AWS::GeoRoutes::Provider  | See the Amazon [GeoRoutes API](../APIReference/Welcome.md#Welcome_Amazon_Location_Service_Routes "../APIReference/Welcome.md#Welcome_Amazon_Location_Service_Routes") reference |

###### Note

Amazon Location does not publish CloudTrail events for the following GeoMaps APIs:
`GetStyleDescriptor`, `GetGlyphs`, and
`GetSprites`. These APIs are free of charge and do not require
authentication.

You can configure advanced event selectors to filter events by
`eventName`, `readOnly`, and `resources.ARN`. This
helps you log only those events that matter to you. For more information, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") .

## Learn about Amazon Location Service log file entries

When you configure a trail, CloudTrail delivers events as log files to an S3 bucket that
you specify, or to Amazon CloudWatch Logs. For more information, see [Working with CloudTrail log files](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-log-files.md") in the AWS CloudTrail User Guide.

CloudTrail log files can contain one or more log entries. Each event entry represents a
single request from any source and includes details such as the requested operation, the
date and time of the operation, request parameters, and more.

###### Note

CloudTrail log files are not an ordered stack trace of API calls. They do not appear in
chronological order. To determine the order of operations, use `eventTime`.

Every event or log entry contains information about who made the request. This
identity information helps you determine:

- Whether the request was made with root or user credentials.
- Whether the request was made with temporary security credentials for a role or
  a federated user.
- Whether the request was made by another AWS service.

## Example: CloudTrail log file entry for an Amazon Location management event

The following example shows a CloudTrail log entry for the `CreateTracker`
operation, which creates a tracker resource.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "111122223333",
        "arn": "arn:aws:geo:us-east-1:111122223333:tracker/ExampleTracker",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "111122223333",
                "arn": "arn:aws:geo:us-east-1:111122223333:tracker/ExampleTracker",
                "accountId": "111122223333",
                "userName": "exampleUser"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2020-10-22T16:36:07Z"
            }
        }
    },
    "eventTime": "2020-10-22T17:43:30Z",
    "eventSource": "geo.amazonaws.com",
    "eventName": "CreateTracker",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "SAMPLE_IP_ADDRESS",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.864 Linux/4.14.193-110.317.amzn2.x86_64 OpenJDK_64-Bit_Server_VM/11.0.8+10-LTS java/11.0.8 kotlin/1.3.72 vendor/Amazon.com_Inc. exec-env/AWS_Lambda_java11",
    "requestParameters": {
        "TrackerName": "ExampleTracker",
        "Description": "Resource description"
    },
    "responseElements": {
        "TrackerName": "ExampleTracker",
        "Description": "Resource description",
        "TrackerArn": "arn:partition:service:region:account-id:resource-id",
        "CreateTime": "2020-10-22T17:43:30.521Z"
    },
    "requestID": "557ec619-0674-429d-8e2c-eba0d3f34413",
    "eventID": "3192bc9c-3d3d-4976-bbef-ac590fa34f2c",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

## Example: CloudTrail log file entry for an Amazon Location data event

The following example shows a CloudTrail log entry for the `Geocode` operation,
which retrieves coordinates, addresses, and other details about a place.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AROA6ODU7M35SFGUCGXHMSAMPLE",
    "arn": "arn:aws:sts::111122223333:assumed-role/Admin/vingu-Isengard",
    "accountId": "111122223333",
    "accessKeyId": "ASIA6ODU7M352GLR5CFMSAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AROA6ODU7M35SFGUCGXHMSAMPLE",
        "arn": "arn:aws:iam::111122223333:role/Admin",
        "accountId": "111122223333",
        "userName": "Admin"
      },
      "attributes": {
        "creationDate": "2024-09-16T14:41:33Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2024-09-16T14:42:16Z",
  "eventSource": "geo-places.amazonaws.com",
  "eventName": "Geocode",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "52.94.133.129",
  "userAgent": "Amazon CloudFront",
  "requestParameters": {
    "Query": "***",
    "Filter": {
      "IncludeCountries": [
        "USA"
      ]
    }
  },
  "responseElements": null,
  "requestID": "1ef7e0b8-c9fc-4a20-80c3-b5340d634c4e",
  "eventID": "913d256c-3a9d-40d0-9bdf-705f12c7659f",
  "readOnly": true,
  "resources": [
    {
      "accountId": "111122223333",
      "type": "AWS::GeoPlaces::Provider",
      "ARN": "arn:aws:geoplaces:us-west-2:111122223333:provider"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "111122223333",
  "eventCategory": "Data"
}
```
