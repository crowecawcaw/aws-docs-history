

# Secret Label Updated event
<a name="event-detail-secret-label-updated-secretsmanager"></a>

Secrets Manager sends a `Secret Label Updated` event when a staging label moves to a new version of a secret, for all labels except `AWSPENDING` and `AWSPREVIOUS`.

The following example shows the structure of the `Secret Label Updated` event. For descriptions of each field, see the list that follows.

The `source` and `detail-type` fields are included below because they contain specific values for Secrets Manager events. For definitions of the other metadata fields that are included in all events, see [Event structure](https://docs.aws.amazon.com/eventbridge/latest/ref/overview-event-structure.html) in the *Amazon EventBridge Events Reference*.

```
{
  "detail-type": "Secret Label Updated",
  "source": "aws.secretsmanager",
  "detail": {
    "name" : "string",
    "labelUpdated" : "string",
    "versionId" : "string"
  }
}
```

`detail-type`  <a name="secret-label-updated-detail-type"></a>
Identifies the type of event.  
For this event, this value is `Secret Label Updated`.

`source`  <a name="secret-label-updated-source"></a>
Identifies the service that generated the event. For Secrets Manager events, this value is `aws.secretsmanager`.

`detail`  <a name="secret-label-updated-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For this event, this data includes:    
`name`  <a name="secret-label-updated-name"></a>
The friendly name of the secret.  
`labelUpdated`  <a name="secret-label-updated-labelUpdated"></a>
The staging label that was attached to the new version.  
`versionId`  <a name="secret-label-updated-versionId"></a>
The unique identifier of the new version of the secret.

**Example Secret Label Updated event**  <a name="event-detail-secret-label-updated.example"></a>
The following example shows a `Secret Label Updated` event for a secret whose `AWSCURRENT` label moved to a new version.  

```
{
  "version": "0",
  "id": "6a7e8feb-b491-4cf7-a9f1-bf3703467718",
  "detail-type": "Secret Label Updated",
  "source": "aws.secretsmanager",
  "account": "012345678901",
  "time": "2024-02-06T16:43:48Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:secretsmanager:us-west-2:012345678901:secret:mySecret-a1b2c3"
  ],
  "detail": {
    "name": "mySecret",
    "labelUpdated": "AWSCURRENT",
    "versionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
  }
}
```