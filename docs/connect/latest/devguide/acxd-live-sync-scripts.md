

# Live Sync Scripts
<a name="acxd-live-sync-scripts"></a>

**Topics**
+ [ListLiveSyncScripts](#acxd-live-sync-scripts-listlivesyncscripts)
+ [CreateLiveSyncScript](#acxd-live-sync-scripts-createlivesyncscript)
+ [GetLiveSyncScript](#acxd-live-sync-scripts-getlivesyncscript)
+ [UpdateLiveSyncScript](#acxd-live-sync-scripts-updatelivesyncscript)
+ [DeleteLiveSyncScript](#acxd-live-sync-scripts-deletelivesyncscript)
+ [ListLiveSyncScriptBuilds](#acxd-live-sync-scripts-listlivesyncscriptbuilds)
+ [CreateLiveSyncScriptBuild](#acxd-live-sync-scripts-createlivesyncscriptbuild)
+ [GetLiveSyncScriptBuild](#acxd-live-sync-scripts-getlivesyncscriptbuild)
+ [ListLiveSyncScriptDeployments](#acxd-live-sync-scripts-listlivesyncscriptdeployments)
+ [CreateLiveSyncScriptDeployment](#acxd-live-sync-scripts-createlivesyncscriptdeployment)
+ [GetLiveSyncScriptDeployment](#acxd-live-sync-scripts-getlivesyncscriptdeployment)
+ [UpdateLiveSyncScriptDeployment](#acxd-live-sync-scripts-updatelivesyncscriptdeployment)
+ [DeleteLiveSyncScriptDeployment](#acxd-live-sync-scripts-deletelivesyncscriptdeployment)
+ [Request Parameters](#acxd-live-sync-scripts-request-parameters)
+ [Metadata](#acxd-live-sync-scripts-metadata)
+ [Step](#acxd-live-sync-scripts-step)

## ListLiveSyncScripts
<a name="acxd-live-sync-scripts-listlivesyncscripts"></a>

### Input
<a name="acxd-live-sync-scripts-listlivesyncscripts-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-live-sync-scripts-listlivesyncscripts-sample-request"></a>

```
await client.send(new ListLiveSyncScriptsCommand({}));
```

### Output
<a name="acxd-live-sync-scripts-listlivesyncscripts-output"></a>

```
{
  "items": [
    {
      "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
      "name": "test-script",
      "steps": [
        {
          "stepId": "d4e5f6a7-8b9c-4d0e-1f2a-3b4c5d6e7f80",
          "body": "Welcome! Can I help you find something?",
          "name": "welcome-step",
          "action": "continue",
          "trigger": {
            "event": "pageLoad",
            "once": true
          }
        }
      ],
      "createdAt": "2026-08-24T18:03:53.046Z",
      "updatedAt": "2026-08-24T18:03:53.046Z",
      "description": "Created via SDK",
      "metadata": {
        "path": "/sdk-tests",
        "tags": [
          "test"
        ]
      },
      "updatedBy": "ci-DeployBot"
    }
  ]
}
```

### Errors
<a name="acxd-live-sync-scripts-listlivesyncscripts-errors"></a>
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateLiveSyncScript
<a name="acxd-live-sync-scripts-createlivesyncscript"></a>

### Input
<a name="acxd-live-sync-scripts-createlivesyncscript-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| steps | array | Yes | 
| description | string | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-live-sync-scripts-createlivesyncscript-sample-request"></a>

```
await client.send(new CreateLiveSyncScriptCommand({
  name: 'test-script',
  description: 'Created via SDK',
  steps: [
      {
          stepId: "d4e5f6a7-8b9c-4d0e-1f2a-3b4c5d6e7f80",
          name: 'welcome-step',
          body: 'Welcome! Can I help you find something?',
          action: 'continue',
          trigger: { event: 'pageLoad', once: true },
      },
  ],
  metadata: { path: '/sdk-tests', tags: ['test'] },
}));
```

### Output
<a name="acxd-live-sync-scripts-createlivesyncscript-output"></a>

```
{
  "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  "name": "test-script",
  "steps": [
    {
      "stepId": "d4e5f6a7-8b9c-4d0e-1f2a-3b4c5d6e7f80",
      "body": "Welcome! Can I help you find something?",
      "name": "welcome-step",
      "action": "continue",
      "trigger": {
        "event": "pageLoad",
        "once": true
      }
    }
  ],
  "createdAt": "2026-08-24T18:03:53.046Z",
  "updatedAt": "2026-08-24T18:03:53.046Z",
  "description": "Created via SDK",
  "metadata": {
    "path": "/sdk-tests",
    "tags": [
      "test"
    ]
  },
  "apiKey": "aB3dEfGh1JkLmN0pQrStU=vWxYz2A4bCd",
  "updatedBy": "ci-DeployBot"
}
```

### Errors
<a name="acxd-live-sync-scripts-createlivesyncscript-errors"></a>
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetLiveSyncScript
<a name="acxd-live-sync-scripts-getlivesyncscript"></a>

### Input
<a name="acxd-live-sync-scripts-getlivesyncscript-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 

### Sample Request
<a name="acxd-live-sync-scripts-getlivesyncscript-sample-request"></a>

```
await client.send(new GetLiveSyncScriptCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
}));
```

### Output
<a name="acxd-live-sync-scripts-getlivesyncscript-output"></a>

```
{  
  "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  "name": "test-script",
  "steps": [
    {
      "stepId": "d4e5f6a7-8b9c-4d0e-1f2a-3b4c5d6e7f80",
      "body": "Welcome! Can I help you find something?",
      "name": "welcome-step",
      "action": "continue",
      "trigger": {
        "event": "pageLoad",
        "once": true
      }
    }
  ],
  "createdAt": "2026-08-24T18:03:53.046Z",
  "updatedAt": "2026-08-24T18:03:53.046Z",
  "description": "Created via SDK",
  "metadata": {
    "path": "/sdk-tests",
    "tags": [
      "test"
    ]
  },
  "apiKey": "aB3dEfGh1JkLmN0pQrStU=vWxYz2A4bCd",
  "updatedBy": "ci-DeployBot"
}
```

### Errors
<a name="acxd-live-sync-scripts-getlivesyncscript-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateLiveSyncScript
<a name="acxd-live-sync-scripts-updatelivesyncscript"></a>

### Input
<a name="acxd-live-sync-scripts-updatelivesyncscript-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| name | string | No | 
| steps | array | No | 
| description | string | No | 
| metadata | object | No | 

### Sample Request
<a name="acxd-live-sync-scripts-updatelivesyncscript-sample-request"></a>

```
await client.send(new UpdateLiveSyncScriptCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  name: 'test-script',
  description: 'Updated via SDK',
  steps: [
      {
          stepId: "d4e5f6a7-8b9c-4d0e-1f2a-3b4c5d6e7f80",
          name: 'welcome-step',
          body: 'Welcome! Can I help you find something?',
          action: 'continue',
          trigger: { event: 'pageLoad', once: true },
      },
  ],
  metadata: { path: '/sdk-tests', tags: ['test'] },
}));
```

### Output
<a name="acxd-live-sync-scripts-updatelivesyncscript-output"></a>

```
{
  "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  "name": "test-script",
  "steps": [
    {
      "stepId": "d4e5f6a7-8b9c-4d0e-1f2a-3b4c5d6e7f80",
      "body": "Welcome! Can I help you find something?",
      "name": "welcome-step",
      "action": "continue",
      "trigger": {
        "event": "pageLoad",
        "once": true
      }
    }
  ],
  "createdAt": "2026-08-24T18:03:53.046Z",
  "updatedAt": "2026-08-24T18:03:53.046Z",
  "description": "Updated via SDK",
  "metadata": {
    "path": "/sdk-tests",
    "tags": [
      "test"
    ]
  },
  "apiKey": "aB3dEfGh1JkLmN0pQrStU=vWxYz2A4bCd",
  "updatedBy": "ci-DeployBot"
}
```

### Errors
<a name="acxd-live-sync-scripts-updatelivesyncscript-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteLiveSyncScript
<a name="acxd-live-sync-scripts-deletelivesyncscript"></a>

### Input
<a name="acxd-live-sync-scripts-deletelivesyncscript-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 

### Sample Request
<a name="acxd-live-sync-scripts-deletelivesyncscript-sample-request"></a>

```
await client.send(new DeleteLiveSyncScriptCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
}));
```

### Output
<a name="acxd-live-sync-scripts-deletelivesyncscript-output"></a>

No response body.

### Errors
<a name="acxd-live-sync-scripts-deletelivesyncscript-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## ListLiveSyncScriptBuilds
<a name="acxd-live-sync-scripts-listlivesyncscriptbuilds"></a>

### Input
<a name="acxd-live-sync-scripts-listlivesyncscriptbuilds-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Output
<a name="acxd-live-sync-scripts-listlivesyncscriptbuilds-output"></a>

Returns `items` (a list of builds) and an optional `nextToken`.

### Sample Request
<a name="acxd-live-sync-scripts-listlivesyncscriptbuilds-sample-request"></a>

```
await client.send(new ListLiveSyncScriptBuildsCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  maxResults: 10
}));
```

### Sample Response
<a name="acxd-live-sync-scripts-listlivesyncscriptbuilds-sample-response"></a>

```
{
  "items": [
      {
        "buildId": "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
        "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
        "status": "PENDING",
        "createdAt": "2026-08-24T18:35:15.164Z",
        "updatedAt": "2026-08-24T18:35:15.164Z",
        "description": "first build",
        "languageSettings": [
          {
            "languageCode": "en-US"
          }
        ]
      }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-live-sync-scripts-listlivesyncscriptbuilds-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateLiveSyncScriptBuild
<a name="acxd-live-sync-scripts-createlivesyncscriptbuild"></a>

### Input
<a name="acxd-live-sync-scripts-createlivesyncscriptbuild-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| description | string | No | 
| languageSettings | array | No | 

### Sample Request
<a name="acxd-live-sync-scripts-createlivesyncscriptbuild-sample-request"></a>

```
await client.send(new CreateLiveSyncScriptBuildCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  description: 'first build',
  languageSettings: [
    { languageCode: 'en-US'}
  ],
}));
```

### Output
<a name="acxd-live-sync-scripts-createlivesyncscriptbuild-output"></a>

```
{
  "buildId": "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
  "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  "status": "PENDING",
  "description": "first build",
  "languageSettings": [
    {
      "languageCode": "en-US"
    }
  ],
  "createdAt": "2026-08-24T18:35:15.164Z",
  "updatedAt": "2026-08-24T18:35:15.164Z"
}
```

### Errors
<a name="acxd-live-sync-scripts-createlivesyncscriptbuild-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## GetLiveSyncScriptBuild
<a name="acxd-live-sync-scripts-getlivesyncscriptbuild"></a>

### Input
<a name="acxd-live-sync-scripts-getlivesyncscriptbuild-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| buildIdentifier | string | Yes | 

### Sample Request
<a name="acxd-live-sync-scripts-getlivesyncscriptbuild-sample-request"></a>

```
await client.send(new GetLiveSyncScriptBuildCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  buildIdentifier: "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
}));
```

### Output
<a name="acxd-live-sync-scripts-getlivesyncscriptbuild-output"></a>

```
{
  "buildId": "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
  "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  "status": "PENDING",
  "description": "first build",
  "languageSettings": [
    {
      "languageCode": "en-US"
    }
  ],
  "createdAt": "2026-08-24T18:35:15.164Z",
  "updatedAt": "2026-08-24T18:35:15.164Z"
}
```

### Errors
<a name="acxd-live-sync-scripts-getlivesyncscriptbuild-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## ListLiveSyncScriptDeployments
<a name="acxd-live-sync-scripts-listlivesyncscriptdeployments"></a>

### Input
<a name="acxd-live-sync-scripts-listlivesyncscriptdeployments-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| nextToken | string | No | 
| maxResults | integer | No | 

### Sample Request
<a name="acxd-live-sync-scripts-listlivesyncscriptdeployments-sample-request"></a>

```
await client.send(new ListLiveSyncScriptDeploymentsCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  maxResults: 10
}));
```

### Output
<a name="acxd-live-sync-scripts-listlivesyncscriptdeployments-output"></a>

```
{
  "items": [
      {
        "deploymentId": "c3d4e5f6-7a8b-4c9d-0e1f-2a3b4c5d6e7f",
        "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
        "buildId": "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
        "description": "first deployment",
        "deploymentStatus": "scheduled",
        "environment": "development",
        "createdAt": "2026-08-24T18:45:52.812Z",
        "updatedAt": "2026-08-24T18:46:30.523Z"
      }
  ],
  "nextToken": null
}
```

### Errors
<a name="acxd-live-sync-scripts-listlivesyncscriptdeployments-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateLiveSyncScriptDeployment
<a name="acxd-live-sync-scripts-createlivesyncscriptdeployment"></a>

### Input
<a name="acxd-live-sync-scripts-createlivesyncscriptdeployment-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| buildIdentifier | string | Yes | 
| description | string | No | 
| environment | string | No | 
| languageCodes | array | No | 
| analyticsTags | array | No | 

### Sample Request
<a name="acxd-live-sync-scripts-createlivesyncscriptdeployment-sample-request"></a>

```
await client.send(new CreateLiveSyncScriptDeploymentCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  buildIdentifier: "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
  description: 'first deployment',
  environment: 'development'
}));
```

### Output
<a name="acxd-live-sync-scripts-createlivesyncscriptdeployment-output"></a>

```
{
  "deploymentId": "c3d4e5f6-7a8b-4c9d-0e1f-2a3b4c5d6e7f",
  "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  "buildId": "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
  "description": "first deployment",
  "deploymentStatus": "scheduled",
  "environment": "development",
  "createdAt": "2026-08-24T18:45:52.812Z",
  "updatedAt": "2026-08-24T18:45:52.812Z"
}
```

### Errors
<a name="acxd-live-sync-scripts-createlivesyncscriptdeployment-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## GetLiveSyncScriptDeployment
<a name="acxd-live-sync-scripts-getlivesyncscriptdeployment"></a>

### Input
<a name="acxd-live-sync-scripts-getlivesyncscriptdeployment-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| deploymentIdentifier | string | Yes | 

### Sample Request
<a name="acxd-live-sync-scripts-getlivesyncscriptdeployment-sample-request"></a>

```
await client.send(new GetLiveSyncScriptDeploymentCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  deploymentIdentifier: "c3d4e5f6-7a8b-4c9d-0e1f-2a3b4c5d6e7f"
}));
```

### Output
<a name="acxd-live-sync-scripts-getlivesyncscriptdeployment-output"></a>

```
{
  "deploymentId": "c3d4e5f6-7a8b-4c9d-0e1f-2a3b4c5d6e7f",
  "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  "buildId": "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
  "description": "first deployment",
  "deploymentStatus": "scheduled",
  "environment": "development",
  "createdAt": "2026-08-24T18:45:52.812Z",
  "updatedAt": "2026-08-24T18:45:52.812Z"
}
```

### Errors
<a name="acxd-live-sync-scripts-getlivesyncscriptdeployment-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateLiveSyncScriptDeployment
<a name="acxd-live-sync-scripts-updatelivesyncscriptdeployment"></a>

### Input
<a name="acxd-live-sync-scripts-updatelivesyncscriptdeployment-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| deploymentIdentifier | string | Yes | 
| buildIdentifier | string | Yes | 
| description | string | No | 
| environment | string | No | 
| languageCodes | array | No | 
| analyticsTags | array | No | 

### Output
<a name="acxd-live-sync-scripts-updatelivesyncscriptdeployment-output"></a>

Returns the updated deployment.

### Sample Request
<a name="acxd-live-sync-scripts-updatelivesyncscriptdeployment-sample-request"></a>

```
await client.send(new UpdateLiveSyncScriptDeploymentCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  deploymentIdentifier: "c3d4e5f6-7a8b-4c9d-0e1f-2a3b4c5d6e7f",
  buildIdentifier: "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
  description: 'updated deployment',
  environment: 'development',
}));
```

### Sample Response
<a name="acxd-live-sync-scripts-updatelivesyncscriptdeployment-sample-response"></a>

```
{
  "deploymentId": "c3d4e5f6-7a8b-4c9d-0e1f-2a3b4c5d6e7f",
  "liveSyncScriptId": "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  "buildId": "b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e",
  "description": "updated deployment",
  "deploymentStatus": "scheduled",
  "environment": "development",
  "createdAt": "2026-08-24T18:45:52.812Z",
  "updatedAt": "2026-08-24T18:45:52.812Z"
}
```

### Errors
<a name="acxd-live-sync-scripts-updatelivesyncscriptdeployment-errors"></a>
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteLiveSyncScriptDeployment
<a name="acxd-live-sync-scripts-deletelivesyncscriptdeployment"></a>

### Input
<a name="acxd-live-sync-scripts-deletelivesyncscriptdeployment-input"></a>


| Parameter | Type | Required | 
| --- | --- | --- | 
| liveSyncScriptIdentifier | string | Yes | 
| deploymentIdentifier | string | Yes | 

### Sample Request
<a name="acxd-live-sync-scripts-deletelivesyncscriptdeployment-sample-request"></a>

```
await client.send(new DeleteLiveSyncScriptDeploymentCommand({
  liveSyncScriptIdentifier: "a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d",
  deploymentIdentifier: "c3d4e5f6-7a8b-4c9d-0e1f-2a3b4c5d6e7f",
}));
```

### Output
<a name="acxd-live-sync-scripts-deletelivesyncscriptdeployment-output"></a>

No response body.

### Errors
<a name="acxd-live-sync-scripts-deletelivesyncscriptdeployment-errors"></a>
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-live-sync-scripts-request-parameters"></a>

`liveSyncScriptIdentifier`  
Type: String  
The unique identifier for the Live Sync Script (a UUIDv4, assigned on creation) used in Get, Update, Delete, and all build/deployment operations.

`buildIdentifier`  
Type: String  
The unique identifier for a build (a UUIDv4). Referenced when getting a build or creating/updating a deployment.

`deploymentIdentifier`  
Type: String  
The unique identifier for a deployment (a UUIDv4).

`name`  
Type: String  
Live Sync Script name. 1–100 characters; letters, numbers, spaces, underscores, and hyphens.

`description`  
Type: String  
Live Sync Script, build, or deployment description. Max 200 characters.

`steps`  
Type: Array  
The ordered body of the script. Each entry is a step object. See Step.

`metadata`  
Type: Object  
Organizational metadata. See Metadata.

`languageSettings`  
Type: Array  
Per-language build configuration. Same shape as the application language settings. See Common Types.

`environment`  
Type: String  
Target environment for the deployment. One of: `development`, `qa`, `staging`, `production`.

`languageCodes`  
Type: Array  
Languages included in the deployment. See Common Types.

`analyticsTags`  
Type: Array  
Analytics tag references applied to the deployment: `[{ "label": "..." }]`.

`apiKey`  
Type: String (sensitive)  
The script's API key, returned on Create/Get/Update of the full resource. Omitted from list summaries.

`createdAt`  
Type: String  
When the resource was created (ISO 8601).

`updatedAt`  
Type: String  
When the resource was last modified (ISO 8601).

`updatedBy`  
Type: String  
The identity of who last modified the resource.

`status`  
Type: String  
Build status.

`deploymentStatus`  
Type: String  
Deployment status.

## Metadata
<a name="acxd-live-sync-scripts-metadata"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| path | string | No | 
| tags | array | No | 

`metadata.path`  
Type: String  
Organizational path for the script. Max 512 characters.

`metadata.tags`  
Type: Array  
Classification tags (max 5; each 1–256 characters).

## Step
<a name="acxd-live-sync-scripts-step"></a>

A single step in a Live Sync Script's `steps` array.


| Field | Type | Required | 
| --- | --- | --- | 
| stepId | string | Yes | 
| name | string | No | 
| description | string | No | 
| action | string | No | 
| group | string | No | 
| body | string | Yes | 
| skipTranslation | boolean | No | 
| translated | boolean | No | 
| variations | array | No | 
| trigger | object | No | 
| stateModifications | array | No | 
| tags | array | No | 

`step.stepId`  
Type: String  
Unique identifier for the step (a UUIDv4).

`step.name`  
Type: String  
Step name. Max 100 characters.

`step.description`  
Type: String  
Step description. Max 200 characters.

`step.action`  
Type: String  
Terminal action for the step. One of: `escalate`, `end`, `continue`.

`step.group`  
Type: String  
Optional grouping label for the step. Max 100 characters.

`step.body`  
Type: String  
The step's message content shown to the user. Max 1000 characters.

`step.skipTranslation`  
Type: Boolean  
Whether to skip translation of this step's content.

`step.translated`  
Type: Boolean  
Whether this step's content has been translated.

`step.variations`  
Type: Array  
Alternative message bodies for A/B testing. Each entry contains `body` (max 1000 chars), `percentage` (0–100), and optional `tags`.

`step.trigger`  
Type: Object  
Defines when the step fires on the page. Contains:  
+ `event`: one of `click`, `pageLoad`, `appear`, `enterViewport`.
+ `query`: a selector/query document identifying the target element.
+ `once`: boolean; fire only once.
+ `highlight`: boolean; highlight the target element.
+ `urlCondition`: an object `{ "operator": "contains" | "matches_regex" | "smart_match", "value": "..." }` restricting the step to matching URLs.

`step.stateModifications`  
Type: Array  
State values written when the step runs. Each entry is a state modification object:  
+ `type`: `context`.
+ `name`: the state variable name.
+ `modification`: one of `clear`, `set`, `increment`, `decrement`, `push`, `pop`, `custom`.
+ `functionName`: function name (used with the `custom` modification).
+ `value`: an operand object describing the value source.
See Common Types.

`step.tags`  
Type: Array  
Analytics tag references applied to the step: `[{ "label": "..." }]`.