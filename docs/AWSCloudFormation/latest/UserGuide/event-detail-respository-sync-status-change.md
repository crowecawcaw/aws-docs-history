# Repository Sync Status
 Change event detail

Below are the detail fields for Repository Sync Status Change events.

The `source` and `detail-type` fields are included
 because they contain specific values for AWS CloudFormation events.


```
{
  . . .,
  "detail-type": "Git Sync Repository Sync Status Change",
  "source": "aws.codeconnections",
  . . .,
  "detail": {
    "connectionArn" : "string",
    "providerType" : "string",
    "repositoryName": "string",
    "providerType": "string",
    "repositoryName": "string",
    "repositoryArn": "string",
    "repositoryLinkId": "string",
    "ownerId": "string",
    "commit": "string",
    "branch": "string",
    "syncType": "string",
    "status": "string",
    "previousSync": "string"
    }
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


For Repository sync status events, this data includes:




`connectionArn`

The Amazon Resource Name (ARN) associated with
 CodeConnections.



`providerType`

The Git provider connected to CloudFormation.


*Valid values*: `GitHub` |
 `GitHub Enterprise` | `GitLab` |
 `BitBucket`



`repositoryName`

The Git repository name.



`repositoryArn`

The ARN associated with the Git repository.



`repositoryLinkId`

The unique ID associated with repository link.



`ownerId`

The unique ID associated with repository owner.



`commit`

The unique ID associated with the repository
 commit.



`branch`

The unique ID associated with the repository
 branch.



`syncType`

The type of sync being performed.



`status`

The current repository sync status.


*Valid values*: `FAILED` |
 `INITIATED` | `IN_PROGRESS` |
 `SUCCEEDED`



`previousSync`

The sync status previous to the current status.


*Valid values*: `FAILED` |
 `INITIATED` | `IN_PROGRESS` |
 `SUCCEEDED`





###### Example:
 Repository Sync Status Change event

The following is an example Repository Sync Status Change event. The event
 details that CodeConnections has successfully synchronized the repository.


```
{
  "version": "0",
  "id": "1b5d8feb-agbv-4cf7-a9f1-bf3703467718",
  "detail-type": "GitSync Repository Sync Status Change",
  "source": "aws.codeconnections",
  "account": "111122223333",
  "time": "2023-12-22T18:43:48Z",
  "region": "us-east-1",
  "resources": ["arn:aws:aws:codestar-connections:us-east-1:111122223333:repository-link/550e8400-e29b-41d4-a716-446655440000",],
  "detail": {
    "connectionArn": "arn:aws:codestar-connections:us-east-1:111122223333:connection/sample-connection-id",
    "providerType": "GitHub",
    "repositoryName": "sample-repository-name",
    "repositoryArn": "arn:aws:aws:codestar-connections:us-east-1:111122223333:repository-link/550e8400-e29b-41d4-a716-446655440000"
    "repositoryLinkId": "550e8400-e29b-41d4-a716-446655440000"
    "ownerId": "sample-owner-id",
    "commit": "sample-commit-id",
    "branch": "main",
    "syncType": "CFN_STACK_SYNC",
    "status": "SUCCEEDED",
    "previousStatus": "IN_PROGRESS",
  }
}
```
