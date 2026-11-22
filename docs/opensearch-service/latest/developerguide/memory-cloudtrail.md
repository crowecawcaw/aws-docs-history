

# Monitoring Amazon OpenSearch Memory with AWS CloudTrail

Amazon OpenSearch Memory is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or AWS service in OpenSearch Memory. CloudTrail captures API calls for OpenSearch Memory as events. Using the information collected by CloudTrail, you can determine the request that was made to OpenSearch Memory, the IP address from which the request was made, who made the request, when it was made, and additional details.

CloudTrail records OpenSearch Memory events with the event source `osm.amazonaws.com`. The `eventName` of each event is the name of the operation, such as [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html).

For more information about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

**Topics**
+ [Management events](#memory-cloudtrail-management)
+ [Data events](#memory-cloudtrail-data)
+ [Service events](#memory-cloudtrail-service)
+ [Example event](#memory-cloudtrail-example)

## Management events
<a name="memory-cloudtrail-management"></a>

Management events record operations on spaces and their tags. CloudTrail logs them by default, and you can view the most recent 90 days in **Event history** in the CloudTrail console without creating a trail.


| Event type | Operations | 
| --- | --- | 
| Write | CreateSpace, [UpdateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html), [DeleteSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteSpace.html), [TagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UntagResource.html) | 
| Read | [GetSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetSpace.html), [ListSpaces](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListSpaces.html), [ListTagsForResource](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListTagsForResource.html) | 

## Data events
<a name="memory-cloudtrail-data"></a>

Data events record operations on the events and memories in a space. CloudTrail doesn't log data events by default, and they incur additional charges. To log them, add an advanced event selector to your trail or event data store with the resource type `AWS::Osm::Space`. The resource of each data event is the ARN of the space.


| Event type | Operations | 
| --- | --- | 
| Write | [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html), [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html), [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html), [UpdateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html), [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html) | 
| Read | [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html), [BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html), [ListEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListEvents.html), [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html), [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html), [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html), [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) | 

The following advanced event selector logs all OpenSearch Memory data events in the account.

```json
[
    {
        "Name": "Log all OpenSearch Memory data events",
        "FieldSelectors": [
            { "Field": "eventCategory",  "Equals": [ "Data" ] },
            { "Field": "resources.type", "Equals": [ "AWS::Osm::Space" ] }
        ]
    }
]
```

To log data events for specific spaces only, add a `resources.ARN` field selector with the ARNs of those spaces. To log only writes, add `{ "Field": "readOnly", "Equals": [ "false" ] }`. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

The content of events and memories is sensitive, so CloudTrail records don't include it. The `requestParameters` of a data event include identifiers such as the space, actor, session, and event or memory ID, and the `responseElements` include the IDs that the operation returned.

## Service events
<a name="memory-cloudtrail-service"></a>

Service events record work that OpenSearch Memory does in your spaces on its own, after your requests return. CloudTrail logs them by default and delivers them to the account that owns the space. In a service event, `userIdentity.type` is `AWSService` and `userIdentity.invokedBy` is `osm.amazonaws.com`.


| Event name | What it records | 
| --- | --- | 
| ExtractMemories | A strategy extracted new memories from events in the space. | 
| ConsolidateMemories | Consolidation updated or replaced existing memories. | 
| ExpireEvents | Events reached the end of the space's event retention period and were removed. | 
| ExpireMemories | Memories reached the end of the space's memory retention period and were removed. | 

Service events let you confirm that extraction is running for a space and audit when data was removed by retention rather than by a caller.

## Example event
<a name="memory-cloudtrail-example"></a>

The following example shows a CloudTrail management event for a `CreateSpace` call.

```json
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEID:dev-session",
        "arn": "arn:aws:sts::111122223333:assumed-role/MemoryAdmin/dev-session",
        "accountId": "111122223333"
    },
    "eventTime": "2026-11-14T00:30:12Z",
    "eventSource": "osm.amazonaws.com",
    "eventName": "CreateSpace",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "203.0.113.42",
    "userAgent": "aws-cli/2.27.0",
    "requestParameters": {
        "name": "getting-started-space",
        "memoryStrategies": [
            { "type": "SEMANTIC", "name": "user-facts" },
            { "type": "SUMMARY" }
        ]
    },
    "responseElements": {
        "spaceId": "sp-02864597b164",
        "arn": "arn:aws:osm:us-east-1:111122223333:space/sp-02864597b164",
        "status": "CREATING"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "b2c3d4e5-6789-01bc-def0-EXAMPLE22222",
    "readOnly": false,
    "resources": [
        {
            "type": "AWS::Osm::Space",
            "ARN": "arn:aws:osm:us-east-1:111122223333:space/sp-02864597b164"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```