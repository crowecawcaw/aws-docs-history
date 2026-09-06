

# Applications
<a name="acxd-applications"></a>

Manage conversational AI applications, the top-level container for flows, builds, and deployments. Each application bundles your flows, knowledge bases, language settings, guardrails, and integrations into a single deployable package within your workspace.

**Topics**
+ [ListApplications](#acxd-applications-listapplications)
+ [CreateApplication](#acxd-applications-createapplication)
+ [GetApplication](#acxd-applications-getapplication)
+ [UpdateApplication](#acxd-applications-updateapplication)
+ [DeleteApplication](#acxd-applications-deleteapplication)
+ [Request Parameters](#acxd-applications-request-parameters)
+ [Application Settings](#acxd-applications-application-settings)
+ [Deployment Settings](#acxd-applications-deployment-settings)

## ListApplications
<a name="acxd-applications-listapplications"></a>

Lists all applications in the workspace.

**Input**


| Parameter | Type | Required | 
| --- | --- | --- | 
| nextToken | string | No | 
| maxResults | integer | No | 

**Sample Request**

```
await client.send(new ListApplicationsCommand({}));
```

**Output**

```
{
  "items": [
    {
      "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
      "name": "MyFirstApp",
      "description": "My first application",
      "metadata": { "path": "/production", "tags": ["support"] },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T14:30:00.000Z"
    },
    {
      "applicationId": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
      "name": "My Support Bot",
      "description": "Handles customer support inquiries",
      "metadata": { "path": "/production", "tags": ["support"] },
      "createdAt": "2026-08-01T12:00:00.000Z",
      "updatedAt": "2026-08-01T14:30:00.000Z"
    }
  ],
  "nextToken": null
}
```

**Errors**
+ `ValidationException` (400)
+ `InternalServerException` (500)

## CreateApplication
<a name="acxd-applications-createapplication"></a>

Creates a new application. An application can start empty and you can attach flows, configure settings, and build it to make it runnable.

**Input**


| Parameter | Type | Required | 
| --- | --- | --- | 
| name | string | Yes | 
| flows | array | No | 
| settings | object | Yes | 
| description | string | No | 
| metadata | object | No | 
| deploymentSettings | object | No | 

**Sample Request**

```
await client.send(new CreateApplicationCommand({
      name: "MyFirstApp",
      description: "My first application",
      settings: {
        conversationTTL: 5,
        thresholds: { incomprehensionCount: 2 }
      }
}));
```

**Output**

```
{
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "name": "MyFirstApp",
  "flows": [],
  "settings": {
    "languageCode": "en-US",
    "languageCodes": [
      "en-US"
    ],
    "languageSettings": [
      {
        "languageCode": "en-US",
        "useNativeLanguage": true
      }
    ],
    "defaultFlows": {},
    "thresholds": {
      "incomprehensionCount": 2
    },
    "conversationTTL": 5,
    "repeatOnIncomprehension": false,
    "clusters": {
      "enabled": false,
      "frequency": {
        "count": 1,
        "resolution": "MONTH"
      },
      "phraseThreshold": {
        "count": 100
      },
      "retention": {
        "count": 30,
        "resolution": "DAY"
      }
    }
  },
  "deploymentSettings": {
    "oneClickDeployEnabled": true,
    "environment": "production",
    "contextAttributes": []
  },
  "description": "My first application",
  "createdAt": "2026-08-07T22:36:43.411Z",
  "updatedAt": "2026-08-07T22:36:43.411Z",
  "metadata": {},
  "updatedBy": "ci-deploy-bot"
}
```

**Errors**
+ `ValidationException` (400)
+ `ConflictException` (409)
+ `InternalServerException` (500)

## GetApplication
<a name="acxd-applications-getapplication"></a>

Gets full application details including flows, settings, guardrails, and deployment configuration.

**Input**


| Parameter | Type | Required | 
| --- | --- | --- | 
| applicationIdentifier | string | Yes | 

**Sample Request**

```
await client.send(new GetApplicationCommand({
  applicationIdentifier: "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
}));
```

**Output**

```
{
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "name": "MyFirstApp",
  "flows": [],
  "settings": {
    "languageCode": "en-US",
    "languageCodes": [
      "en-US"
    ],
    "languageSettings": [
      {
        "languageCode": "en-US",
        "useNativeLanguage": true
      }
    ],
    "defaultFlows": {},
    "thresholds": {
      "incomprehensionCount": 2
    },
    "conversationTTL": 5,
    "repeatOnIncomprehension": false,
    "clusters": {
      "enabled": false,
      "frequency": {
        "count": 1,
        "resolution": "MONTH"
      },
      "phraseThreshold": {
        "count": 100
      },
      "retention": {
        "count": 30,
        "resolution": "DAY"
      }
    }
  },
  "deploymentSettings": {
    "oneClickDeployEnabled": true,
    "environment": "production",
    "contextAttributes": []
  },
  "description": "My first application",
  "createdAt": "2026-08-07T22:36:43.411Z",
  "updatedAt": "2026-08-07T22:36:43.411Z",
  "metadata": {},
  "updatedBy": "ci-deploy-bot"
}
```

**Errors**
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## UpdateApplication
<a name="acxd-applications-updateapplication"></a>

Updates an application. Only include fields you want to change.

**Input**


| Parameter | Type | Required | 
| --- | --- | --- | 
| applicationIdentifier | string | Yes | 
| name | string | No | 
| flows | array | No | 
| settings | object | No | 
| description | string | No | 
| metadata | object | No | 
| deploymentSettings | object | No | 

**Sample Request**

```
await client.send(new UpdateApplicationCommand({
  applicationIdentifier: "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  description: "Updated via SDK",
}));
```

**Output**

Returns the full updated application.

```
{
  "applicationId": "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
  "name": "MyFirstApp",
  "flows": [],
  "settings": {
    "languageCode": "en-US",
    "languageCodes": [
      "en-US"
    ],
    "languageSettings": [
      {
        "languageCode": "en-US",
        "useNativeLanguage": true
      }
    ],
    "defaultFlows": {},
    "thresholds": {
      "incomprehensionCount": 2
    },
    "conversationTTL": 5,
    "repeatOnIncomprehension": false,
    "clusters": {
      "enabled": false,
      "frequency": {
        "count": 1,
        "resolution": "MONTH"
      },
      "phraseThreshold": {
        "count": 100
      },
      "retention": {
        "count": 30,
        "resolution": "DAY"
      }
    }
  },
  "deploymentSettings": {
    "oneClickDeployEnabled": true,
    "environment": "production",
    "contextAttributes": []
  },
  "createdAt": "2026-08-07T22:36:43.411Z",
  "updatedAt": "2026-08-07T23:01:19.732Z",
  "description": "Updated via SDK",
  "metadata": {},
  "updatedBy": "ci-deploy-bot"
}
```

**Errors**
+ `ResourceNotFoundException` (404)
+ `ValidationException` (400)
+ `InternalServerException` (500)

## DeleteApplication
<a name="acxd-applications-deleteapplication"></a>

Deletes an application. This removes the application and all its builds and deployments.

**Input**


| Parameter | Type | Required | 
| --- | --- | --- | 
| applicationIdentifier | string | Yes | 

**Sample Request**

```
await client.send(new DeleteApplicationCommand({
    applicationIdentifier: "05c3fcc2-7900-41c4-adee-b59dc69be8ae",
}));
```

**Output**

No response body.

**Errors**
+ `ValidationException` (400)
+ `ResourceNotFoundException` (404)
+ `InternalServerException` (500)

## Request Parameters
<a name="acxd-applications-request-parameters"></a>

**`applicationIdentifier`**

Type: String

The unique identifier for the application (assigned on creation) that is used in Get, Update, and Delete operations.

**`name`**

Type: String

Application name. 1–100 characters.

**`description`**

Type: String

Application description. Max 200 characters.

**`flows`**

Type: Array

List of flow references attached to this application. Each entry is an object with a `flowId` field.

```
[
  {"flowId": "MainFlow"},
  {"flowId": "MainFlowTwo"}
]
```

**`settings`**

Type: Object

Application settings controlling language, NLP, guardrails, and runtime behavior. See Application Settings.

**`deploymentSettings`**

Type: Object

One-click deploy configuration. See Deployment Settings.

**`metadata`**

Type: Object

Organizational metadata. See Common Types.

**`createdAt`**

Type: String

When the application was created (ISO 8601).

**`updatedAt`**

Type: String

When the application was last modified (ISO 8601).

**`updatedBy`**

Type: String

The identity of who last modified the application.

## Application Settings
<a name="acxd-applications-application-settings"></a>


| Field | Type | Required | 
| --- | --- | --- | 
| languageCode | string | No | 
| languageCodes | array | No | 
| languageSettings | array | No | 
| defaultFlows | object | No | 
| guardrails | array | No | 
| lifecycleHooks | object | No | 
| thresholds | object | No | 
| conversationTTL | integer | No | 
| autoCorrection | boolean | No | 
| childDirected | boolean | No | 
| repeatOnIncomprehension | boolean | No | 
| clusters | object | No | 

**`languageCode`**

Type: String

Primary language for the application. See Common Types.

**`languageCodes`**

Type: Array

Supported languages for the application. See Common Types.

**`languageSettings`**

Type: Array

Per-language configuration. Each entry contains:


| Field | Type | Required | 
| --- | --- | --- | 
| languageCode | string | Yes | 
| useNativeLanguage | boolean | No | 
| useLex3pAsr | boolean | No | 
| projectId | string | No | 
| voice | string | No | 

**`languageSettings.languageCode`**

Type: String

The language this setting applies to. See Common Types.

**`languageSettings.useNativeLanguage`**

Type: Boolean

Whether to use native language processing for this language.

**`languageSettings.useLex3pAsr`**

Type: Boolean

Whether to use Lex third-party ASR for this language.

**`languageSettings.projectId`**

Type: String

External project ID for this language configuration.

**`languageSettings.voice`**

Type: String

Voice identifier for text-to-speech output in this language.

**`defaultFlows`**

Type: Object

Default flow assignments for system events. Each field is an object with `flowId` and optional `quickReplies`.

**`defaultFlows.welcome`**

Type: Object

Flow triggered on conversation start. `{ "flowId": "...", "quickReplies": ["Yes", "No"] }`

**`defaultFlows.fallback`**

Type: Object

Flow triggered when no intent matches.

**`defaultFlows.unknown`**

Type: Object

Flow triggered on unknown input. Supports optional `knowledgeBaseId`: `{ "flowId": "...", "knowledgeBaseId": "...", "quickReplies": [...] }`

**`defaultFlows.escalation`**

Type: Object

Flow triggered when escalation is requested.

**`defaultFlows.frustration`**

Type: Object

Flow triggered when frustration is detected.

**`defaultFlows.help`**

Type: Object

Flow triggered when user asks for help.

**`defaultFlows.repeat`**

Type: Object

Flow triggered when user asks to repeat.

**`defaultFlows.resume`**

Type: Object

Flow triggered when a conversation resumes.

**`guardrails`**

Type: Array

Guardrail references attached to the application: `[{ "guardrailId": "..." }]`.

**`lifecycleHooks`**

Type: Object

Flow IDs invoked at specific lifecycle events.

**`lifecycleHooks.conversationStart`**

Type: String

Flow ID invoked when a conversation begins.

**`lifecycleHooks.conversationEnd`**

Type: String

Flow ID invoked when a conversation ends.

**`lifecycleHooks.escalation`**

Type: String

Flow ID invoked on escalation.

**`lifecycleHooks.stateModification`**

Type: String

Flow ID invoked when state is modified externally.

**`lifecycleHooks.messageReceived`**

Type: String

Flow ID invoked on each incoming message.

**`thresholds`**

Type: Object

Threshold configuration for conversation behavior.

**`thresholds.incomprehensionCount`**

Type: Integer

Number of consecutive incomprehensions before triggering fallback. Default: 2.

**`conversationTTL`**

Type: Integer

Session timeout in minutes (1–60). Default: 5.

**`autoCorrection`**

Type: Boolean

Enable auto-correction of user input. Default: false.

**`childDirected`**

Type: Boolean

COPPA compliance flag. Default: false.

**`repeatOnIncomprehension`**

Type: Boolean

Repeat last message on incomprehension. Default: false.

**`clusters`**

Type: Object

Configuration for clustering similar user messages for analytics.

**`clusters.enabled`**

Type: Boolean

Whether clustering is active. Default: false.

**`clusters.frequency`**

Type: Object

How often clusters are computed. `{ "count": 1, "resolution": "HOUR|DAY|WEEK|MONTH" }`

**`clusters.phraseThreshold`**

Type: Object

Minimum phrase count to form a cluster. `{ "count": 100 }` (minimum 30).

**`clusters.retention`**

Type: Object

How long to retain cluster data. `{ "count": 30, "resolution": "DAY" }` (1–90 days).

## Deployment Settings
<a name="acxd-applications-deployment-settings"></a>

**`oneClickDeployEnabled`**

Type: Boolean

Enable automatic deployment on build success.

**`environment`**

Type: String

Target environment for automatic deployments. One of: `development`, `qa`, `staging`, `production`.

**`contextAttributes`**

Type: Array

Context attribute values injected into automatic deployments: `[{ "key": "attribute_name", "value": ... }]`. Max 50 entries.