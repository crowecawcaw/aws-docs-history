

# Resource Sync Status Change event detail
<a name="event-detail-resource-sync-status-change"></a>

Below are the detail fields for Resource Sync Status Change events.

The `source` and `detail-type` fields are included because they contain specific values for events.

```
{
  . . .,
  "detail-type": "Git Sync Resource Sync Status Change",
  "source": "aws.codeconnections",
  . . .,
  "detail": {
    "providerType" : "string",
    "commit" : "string",
    "repositoryName": "string",
    "branch": "string",
    "syncType": "string",
    "syncTarget": "string",
    "status": "string",
    "previousSync": "string"
  }
}
```

`detail-type`  <a name="resource-sync-status-change-detail-type"></a>
Identifies the type of event.  
For Repository Sync status events, this value is `Git Sync Repository Sync Status Change`.

`source`  <a name="resource-sync-status-change-source"></a>
Identifies the service that generated the event. For Git sync events, this value is `aws.codeconnections`.

`detail`  <a name="resource-sync-status-change-detail"></a>
A JSON object that contains information about the event. The service generating the event determines the content of this field.  
For resource sync status events, this data includes:    
`providerType`  <a name="resource-sync-status-change-provider-type"></a>
The Git provider connected to CloudFormation.  
*Valid values*: `GitHub` \| `GitHub Enterprise` \| `GitLab` \| `BitBucket`  
`commit`  <a name="resource-sync-status-change-commit"></a>
The unique ID associated with the repository commit.  
`repositoryName`  <a name="resource-sync-status-change-repository-name"></a>
The Git repository name.  
`branch`  <a name="resource-sync-status-change-branch"></a>
The unique ID associated with the repository branch.  
`syncType`  <a name="resource-sync-status-change-sync-type"></a>
The type of sync being performed.  
`syncTarget`  <a name="resource-sync-status-change-sync-target"></a>
The target stack for the resource sync.  
`status`  <a name="resource-sync-status-change-status"></a>
The current repository sync status.  
*Valid values*: `FAILED` \| `INITIATED` \| `IN_PROGRESS` \| `SUCCEEDED`  
`previousSync`  <a name="resource-sync-status-change-previous-sync"></a>
The sync status previous to the current status.  
*Valid values*: `FAILED` \| `INITIATED` \| `IN_PROGRESS` \| `SUCCEEDED`

**Example: Resource Sync Status Change event**  <a name="event-detail-resource-sync-status-change.example"></a>
The following is an example resource sync status change event. The event details that CodeConnections has successfully synchronized the resource.  

```
{
  "version": "0",
  "id": "1b5d8feb-agbv-4cf7-a9f1-bf3703467718",
  "detail-type": "Git Sync Resource Sync Status Change",
  "source": "aws.codeconnections",
  "account": "111122223333",
  "time": "2023-12-22T18:43:48Z",
  "region": "us-east-1",
  "resources": ["arn:aws:aws:cloudformation:us-east-1:111122223333:stack/targetStack1"],
  "detail": {
    "providerType": "GitHub",
    "commit": "sample-commit-id",
    "repositoryName": "sample-repository-name",
    "branch": "main",
    "syncType": "CFN_STACK_SYNC",
    "syncTarget": "arn:aws:aws:cloudformation:us-east-1:111122223333:stack/targetStack1",
    "status": "SUCCEEDED",
    "previousStatus": "IN_PROGRESS"
  }
}
```