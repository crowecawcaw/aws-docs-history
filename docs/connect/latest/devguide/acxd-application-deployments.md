# Application Deployments

Deploying an application pushes a successful build to the channels where users interact:
chat, voice, IVR, website, mobile, or MCP clients. Only one build is live per application at a
time. Deploying a new build deactivates the previous one. You can roll back to any previous
build at any time.

###### Contents

- [Quick Start](#acxd-application-deployments-quick-start "#acxd-application-deployments-quick-start")
- [ListApplicationDeployments](#acxd-application-deployments-listapplicationdeployments "#acxd-application-deployments-listapplicationdeployments")
- [CreateApplicationDeployment](#acxd-application-deployments-createapplicationdeployment "#acxd-application-deployments-createapplicationdeployment")
- [GetApplicationDeployment](#acxd-application-deployments-getapplicationdeployment "#acxd-application-deployments-getapplicationdeployment")
- [UpdateApplicationDeployment](#acxd-application-deployments-updateapplicationdeployment "#acxd-application-deployments-updateapplicationdeployment")
- [DeleteApplicationDeployment](#acxd-application-deployments-deleteapplicationdeployment "#acxd-application-deployments-deleteapplicationdeployment")
- [Request Parameters](#acxd-application-deployments-request-parameters "#acxd-application-deployments-request-parameters")

## Quick Start

```
// 1. Create Application
const app = await client.send(new CreateApplicationCommand({
  name: "DeploymentTestApp",
  settings: { conversationTTL: 5, thresholds: { incomprehensionCount: 2 }
}
}));

// 2. Create Flow
const flow = await client.send(new CreateFlowCommand({
  flowId: "DeployTestFlow",
  description: "Flow for deployment testing",
  nodes: {}
}));

// 3. Attach Flow
const updatedApp = await client.send(new UpdateApplicationCommand({
  applicationIdentifier: app.applicationId,
  flows: [{ flowId: "DeployTestFlow" }]
}));

// 4. Create Build
const build = await client.send(new CreateApplicationBuildCommand({
  applicationIdentifier: app.applicationId,
}));

// 5. Wait for build
await new Promise(r => setTimeout(r, 5000));
const buildStatus = await client.send(new GetApplicationBuildCommand({
  applicationIdentifier: app.applicationId,
  buildIdentifier: build.buildId,
}));

if (buildStatus.status !== "BUILT") {
  console.log("Build failed, cannot deploy. Stopping.");
  return;
}

// 6. Create Deployment
const deployment = await client.send(new CreateApplicationDeploymentCommand({
  applicationIdentifier: app.applicationId,
  buildIdentifier: build.buildId,
  environment: "production",
  languageCodes: ["en-US"],
}));

// 7. Wait and Get Deployment
await new Promise(r => setTimeout(r, 5000));
const deployStatus = await client.send(new GetApplicationDeploymentCommand({
  applicationIdentifier: app.applicationId,
  deploymentIdentifier: deployment.deploymentId,
}));

// 8. List Deployments
const deployments = await client.send(new ListApplicationDeploymentsCommand({
  applicationIdentifier: app.applicationId,
}));
```

## ListApplicationDeployments

Lists deployments for an application.

**Input**

| Parameter               | Type    | Required |
| ----------------------- | ------- | -------- |
| `applicationIdentifier` | string  | Yes      |
| `nextToken`             | string  | No       |
| `maxResults`            | integer | No       |

**Sample Request**

```
await client.send(new ListApplicationDeploymentsCommand({
    applicationIdentifier: app.applicationId,
}));
```

**Output**

```
{
  "items": [
    {
      "deploymentId": "d1e2f3a4-5678-90ab-cdef-1234567890ab",
      "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
      "buildId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
      "description": "Production release v1.0",
      "deploymentStatus": "deployed",
      "environment": "production",
      "analyticsTags": [{ "label": "resolved_issue" }],
      "contextAttributes": [{ "key": "region", "value": "us-west-2" }],
      "createdAt": "2026-08-01T16:00:00.000Z",
      "updatedAt": "2026-08-01T16:00:00.000Z",
      "updatedBy": "ci-deploy-bot"
    }
  ],
  "nextToken": null
}
```

**Errors**

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## CreateApplicationDeployment

Deploys a build to an environment, making it live for end users on all configured
channels.

**Input**

| Parameter               | Type         | Required |
| ----------------------- | ------------ | -------- |
| `applicationIdentifier` | string       | Yes      |
| `buildIdentifier`       | string       | Yes      |
| `description`           | string       | No       |
| `environment`           | string, enum | No       |
| `languageCodes`         | array        | No       |
| `analyticsTags`         | array        | No       |
| `contextAttributes`     | array        | No       |

**Sample Request**

```
await client.send(new CreateApplicationDeploymentCommand({
      applicationIdentifier: app.applicationId,
      buildIdentifier: build.buildId,
      description: "Production release v1.0",
      environment: "production",
      languageCodes: ["en-US"],
      analyticsTags: [{ label: "resolved_issue" }],
      contextAttributes: [{ key: "region", value: "us-west-2" }],
}));
```

**Output**

```
{
  "deploymentId": "d1e2f3a4-5678-90ab-cdef-1234567890ab",
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "buildId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
  "description": "Production release v1.0",
  "deploymentStatus": "pending",
  "environment": "production",
  "analyticsTags": [{ "label": "resolved_issue" }],
  "contextAttributes": [{ "key": "region", "value": "us-west-2" }],
  "createdAt": "2026-08-01T16:00:00.000Z",
  "updatedAt": "2026-08-01T16:00:00.000Z",
  "updatedBy": "ci-deploy-bot"
}
```

**Errors**

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## GetApplicationDeployment

Gets deployment details and status.

**Input**

| Parameter               | Type   | Required |
| ----------------------- | ------ | -------- |
| `applicationIdentifier` | string | Yes      |
| `deploymentIdentifier`  | string | Yes      |

**Sample Request**

```
await client.send(new GetApplicationDeploymentCommand({
  applicationIdentifier: "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  deploymentIdentifier: "d1e2f3a4-5678-90ab-cdef-1234567890ab",
}));
```

**Output**

```
{
  "deploymentId": "d1e2f3a4-5678-90ab-cdef-1234567890ab",
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "buildId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
  "description": "Production release v1.0",
  "deploymentStatus": "deployed",
  "environment": "production",
  "analyticsTags": [{ "label": "resolved_issue" }],
  "contextAttributes": [{ "key": "region", "value": "us-west-2" }],
  "createdAt": "2026-08-01T16:00:00.000Z",
  "updatedAt": "2026-08-01T16:00:00.000Z",
  "updatedBy": "ci-deploy-bot"
}
```

**Errors**

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## UpdateApplicationDeployment

Updates a deployment (e.g., deploy a different build, change environment, or roll back to
a previous version).

**Input**

| Parameter               | Type         | Required |
| ----------------------- | ------------ | -------- |
| `applicationIdentifier` | string       | Yes      |
| `deploymentIdentifier`  | string       | Yes      |
| `buildIdentifier`       | string       | Yes      |
| `description`           | string       | No       |
| `environment`           | string, enum | No       |
| `languageCodes`         | array        | No       |
| `analyticsTags`         | array        | No       |
| `contextAttributes`     | array        | No       |

**Sample Request**

```
await client.send(new UpdateApplicationDeploymentCommand({
      applicationIdentifier: "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
      buildIdentifier: "b1c2d3e4-5678-90ab-cdef-1234567890ab",
      deploymentIdentifier: "d1e2f3a4-5678-90ab-cdef-1234567890ab",
      description: "Production release v2.0",
      environment: "production",
      analyticsTags: [{ label: "resolved_issue" }],
      contextAttributes: [{ key: "region", value: "us-west-2" }],
}));
```

**Output**

```
{
  "deploymentId": "d1e2f3a4-5678-90ab-cdef-1234567890ab",
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "buildId": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
  "description": "Production release v2.0",
  "deploymentStatus": "deployed",
  "environment": "production",
  "analyticsTags": [{ "label": "resolved_issue" }],
  "contextAttributes": [{ "key": "region", "value": "us-west-2" }],
  "createdAt": "2026-08-01T16:00:00.000Z",
  "updatedAt": "2026-08-01T16:00:00.000Z",
  "updatedBy": "ci-deploy-bot"
}
```

**Errors**

- `ResourceNotFoundException` (404)
- `ValidationException` (400)
- `InternalServerException` (500)

## DeleteApplicationDeployment

Removes a deployment, taking the application offline. The application stays offline until
you redeploy.

**Input**

| Parameter               | Type   | Required |
| ----------------------- | ------ | -------- |
| `applicationIdentifier` | string | Yes      |
| `deploymentIdentifier`  | string | Yes      |

**Sample Request**

```
await client.send(new DeleteApplicationDeploymentCommand({
  applicationIdentifier: "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  deploymentIdentifier: "d1e2f3a4-5678-90ab-cdef-1234567890ab"
}));
```

**Output**

No response body.

**Errors**

- `ValidationException` (400)
- `ResourceNotFoundException` (404)
- `InternalServerException` (500)

## Request Parameters

**applicationIdentifier**

Type: String

The application ID that owns the deployments.

**deploymentIdentifier**

Type: String

The unique identifier for a deployment (assigned on creation) and is used in Get, Update,
and Delete operations.

**buildIdentifier**

Type: String

The build ID to deploy.

**deploymentStatus**

Type: String

The current deployment status (e.g., `pending`, `deployed`).

**environment**

Type: String

The target environment. One of: `development`, `qa`,
`staging`, `production`.

**description**

Type: String

Deployment description. Max 200 characters.

**languageCodes**

Type: Array

Languages to deploy (e.g., `["en-US", "es-ES"]`).

**analyticsTags**

Type: Array

Analytics tag references to attach to this deployment:
`[{ "label": "tag_name" }]`.

**contextAttributes**

Type: Array

Context attribute values for this deployment:
`[{ "key": "attribute_name", "value": "..." }]`. Max 50 entries.

**createdAt**

Type: String

When the deployment was created (ISO 8601).

**updatedAt**

Type: String

When the deployment was last modified (ISO 8601).

**updatedBy**

Type: String

The identity of who last modified the deployment.
