# Application Builds

A build creates an immutable package of your application's flow logic, language settings, and configuration. A build compiles an application's flows and configuration into a deployable artifact.

###### Contents

- [Quick Start](#acxd-application-builds-quick-start "#acxd-application-builds-quick-start")
- [ListApplicationBuilds](#acxd-application-builds-listapplicationbuilds "#acxd-application-builds-listapplicationbuilds")
- [CreateApplicationBuild](#acxd-application-builds-createapplicationbuild "#acxd-application-builds-createapplicationbuild")
- [GetApplicationBuild](#acxd-application-builds-getapplicationbuild "#acxd-application-builds-getapplicationbuild")
- [GetApplicationBuildDiff](#acxd-application-builds-getapplicationbuilddiff "#acxd-application-builds-getapplicationbuilddiff")
- [Request Parameters](#acxd-application-builds-request-parameters "#acxd-application-builds-request-parameters")

## Quick Start

This example creates an application, attaches a flow, builds it, and checks build status.

```
// 1. Create an Application
const app = await client.send(new CreateApplicationCommand({
  name: "CustomerSupport",
  settings: { conversationTTL: 5, thresholds: { incomprehensionCount: 2 }
}
}));
// 2. Create a Flow
const flow = await client.send(new CreateFlowCommand({
  flowId: "GreetingFlow",
  description: "GreetingFlow",
  nodes: {},
}));
// 3. Attach flow to app
const updatedApp = await client.send(new UpdateApplicationCommand({
  applicationIdentifier: app.applicationId,
  flows: [{ flowId: "GreetingFlow" }]
}));
// 4. Create a build
const build = await client.send(new CreateApplicationBuildCommand({
  applicationIdentifier: app.applicationId,
}));
// 5. Get Build Status
const status = await client.send(new GetApplicationBuildCommand({
  applicationIdentifier: app.applicationId,
  buildIdentifier: build.buildId,
}));
console.log(status.status); // "PENDING" | "BUILT" | "FAILED"
```

## ListApplicationBuilds

Lists builds for an application.

### Input

| Parameter               | Type    | Required |
| ----------------------- | ------- | -------- |
| `applicationIdentifier` | string  | Yes      |
| `nextToken`             | string  | No       |
| `maxResults`            | integer | No       |

### Sample Request

```
await client.send(new ListApplicationBuildsCommand({
  applicationIdentifier: "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
}));
```

### Output

```
{
  "items": [
    {
      "buildId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
      "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
      "status": "BUILT",
      "version": "1.0",
      "description": "Initial build",
      "createdAt": "2026-08-01T15:00:00.000Z",
      "updatedAt": "2026-08-01T15:02:00.000Z",
      "updatedBy": "ci-deploy-bot",
      "languageSettings": [
        {
          "languageCode": "en-US",
          "useNativeLanguage": true,
          "region": "global"
        }
      ]
    }
  ]
}
```

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## CreateApplicationBuild

Starts a new build. A validation check runs automatically, review the results to catch errors before deploying. Builds are immutable once created.

### Input

| Parameter               | Type   | Required |
| ----------------------- | ------ | -------- |
| `applicationIdentifier` | string | Yes      |
| `version`               | string | No       |
| `description`           | string | No       |
| `languageSettings`      | array  | No       |

### Sample Request

```
await client.send(new CreateApplicationBuildCommand({
  applicationIdentifier: app.applicationId,
  version: "1.0",
  description: "Release build",
  languageSettings: [
    { languageCode: "en-US", useNativeLanguage: true, region: "global" },
  ],
}));
```

### Output

```
{
  "buildId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "status": "PENDING",
  "version": "1.0",
  "description": "Release build",
  "createdAt": "2026-08-01T15:00:00.000Z",
  "updatedAt": "2026-08-01T15:00:00.000Z",
  "updatedBy": "ci-deploy-bot",
  "languageSettings": [
      {
        "languageCode": "en-US",
        "useNativeLanguage": true,
        "region": "global"
      }
    ]
}
```

### Errors

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## GetApplicationBuild

Gets build details and status. A build transitions from PENDING → BUILT (success) or FAILED. Failed builds include details on what caused the error.

### Input

| Parameter               | Type   | Required |
| ----------------------- | ------ | -------- |
| `applicationIdentifier` | string | Yes      |
| `buildIdentifier`       | string | Yes      |

### Sample Request

```
await client.send(new GetApplicationBuildCommand({
  applicationIdentifier: app.applicationId,
  buildIdentifier: build.buildId,
}));
```

### Output

```
{
  "buildId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "status": "BUILT",
  "version": "1.0",
  "description": "Release build",
  "createdAt": "2026-08-01T15:00:00.000Z",
  "updatedAt": "2026-08-01T15:00:00.000Z",
  "updatedBy": "ci-deploy-bot",
  "languageSettings": [
      {
        "languageCode": "en-US",
        "useNativeLanguage": true,
        "region": "global"
      }
    ]
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## GetApplicationBuildDiff

Gets the diff between two builds showing what changed.

### Input

| Parameter                 | Type   | Required |
| ------------------------- | ------ | -------- |
| `applicationIdentifier`   | string | Yes      |
| `buildIdentifier`         | string | Yes      |
| `previousBuildIdentifier` | string | Yes      |

### Sample Request

```
await client.send(new GetApplicationBuildDiffCommand({
  applicationIdentifier: APP_ID,
  buildIdentifier: SECOND_BUILD_ID,
  previousBuildIdentifier: FIRST_BUILD_ID,
}));
```

### Output

```
{
  "application": {
    "properties": {},
    "settings": {},
    "modifiedSlotTypes": {},
    "modifiedDataRequests": {},
    "modifiedActions": {},
    "attachedFlows": {},
    "detachedFlows": {},
    "modifiedFlows": {}
  }
}
```

### Errors

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

`applicationIdentifier`

Type: String

The application ID that owns the builds.

`buildIdentifier`

Type: String

The unique identifier for a build (assigned on creation) and used in Get and Diff operations.

`previousBuildIdentifier`

Type: String

The build ID to compare against when generating a diff.

`status`

Type: String

The current build status. One of: `PENDING`, `BUILT`, `FAILED`.

`version`

Type: String

A version label for the build. Max 16 characters.

`description`

Type: String

Build description. Max 200 characters.

`languageSettings`

Type: Array

Per-language build configuration. Each entry: `{ "languageCode": "en-US", "useNativeLanguage": true, "region": "global" }`. See Application languageSettings.

`createdAt`

Type: String

When the build was created (ISO 8601).

`updatedAt`

Type: String

When the build was last modified (ISO 8601).

`updatedBy`

Type: String

The identity of who last modified the build.
