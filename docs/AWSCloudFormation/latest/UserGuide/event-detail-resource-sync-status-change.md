# Resource Sync Status

Change event detail

Below are the detail fields for Resource Sync Status Change events.

The `source` and `detail-type` fields are included
because they contain specific values for events.

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

`detail-type`

Identifies the type of event.

For Repository Sync status events, this value is `Git Sync
 Repository Sync Status Change`.

`source`

Identifies the service that generated the event. For Git sync events,
this value is `aws.codeconnections`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For resource sync status events, this data includes:

`providerType`

The Git provider connected to CloudFormation.

_Valid values_: `GitHub` |
`GitHub Enterprise` | `GitLab` |
`BitBucket`

`commit`

The unique ID associated with the repository
commit.

`repositoryName`

The Git repository name.

`branch`

The unique ID associated with the repository
branch.

`syncType`

The type of sync being performed.

`syncTarget`

The target stack for the resource sync.

`status`

The current repository sync status.

_Valid values_: `FAILED` |
`INITIATED` | `IN_PROGRESS` |
`SUCCEEDED`

`previousSync`

The sync status previous to the current status.

_Valid values_: `FAILED` |
`INITIATED` | `IN_PROGRESS` |
`SUCCEEDED`

###### Example: Resource Sync Status Change event

The following is an example resource sync status change event. The event
details that CodeConnections has successfully synchronized the resource.

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
