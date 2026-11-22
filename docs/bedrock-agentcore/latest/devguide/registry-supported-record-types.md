

# Supported record types and descriptors

**Migration Now Open**  
 AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on October 30, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md).

 AWS Agent Registry validates record content against official protocol schemas. The console displays the reference schema side-by-side with your input and shows inline validation errors with a **Diagnose with Amazon Q** button. The registry supports all versions of the MCP Protocol Schema and the A2A Schema.

When you create a record, you choose two things:
+ The record’s **record type** — a semantic classification (`AGENT`, `MCP`, `SKILL`, `CUSTOM`, or `WEB_BOT`) that determines which descriptors are valid.
+ The record’s **descriptor** — the shape of the actual record content (schema, versioning rules, sync support). Exactly one primary descriptor key may be populated per record.

Each record also has metadata fields — `name` (a unique name for each record), `displayName`, `description`, `recordVersion`, `recordType`, and `tags` — plus the `descriptors` structure where the descriptor content lives.

Valid descriptors per record type:
+  **AGENT:** `a2aAgentCard`, `mcpServer`, `custom` 
+  **MCP:** `mcpServer`, `custom` 
+  **SKILL:** `agentSkillsDefinition`, `custom` 
+  **CUSTOM:** `custom` 
+  **WEB\_BOT:** `signatureAgentCard` 

## MCP descriptors
<a name="registry-mcp-descriptors"></a>

An MCP server record uses the `mcpServer` primary descriptor. Store the server definition JSON in `descriptors.mcpServer.data` and set `descriptors.mcpServer.dataSchemaVersion` to the schema version. Tool definitions nest under `descriptors.mcpServer.additionalData.tools`:
+  **Server** — Based on the server.json definition from the [official Model Context Protocol registry](https://registry.modelcontextprotocol.io/) on the Model Context Protocol website. The content is validated against the selected schema version, which can be found in the [MCP schema repository](https://github.com/modelcontextprotocol/static/tree/main/schemas) on the GitHub website. Supported `dataSchemaVersion` values: [2025-12-11](https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json), [2025-10-17](https://static.modelcontextprotocol.io/schemas/2025-10-17/server.schema.json), [2025-10-11](https://static.modelcontextprotocol.io/schemas/2025-10-11/server.schema.json), [2025-09-29](https://static.modelcontextprotocol.io/schemas/2025-09-29/server.schema.json), [2025-09-16](https://static.modelcontextprotocol.io/schemas/2025-09-16/server.schema.json), [2025-07-09](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json). If you do not have a server.json, we recommend you create one with the latest schema.
+  **Tools** — Tools available on the server, validated against the [MCP protocol specification](https://modelcontextprotocol.io/specification/2025-11-25/schema) on the Model Context Protocol website. Supported `dataSchemaVersion` values: [2025-11-25](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-11-25/schema.json), [2025-06-18](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-06-18/schema.json), [2025-03-26](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-03-26/schema.json), [2024-11-05](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2024-11-05/schema.json).

 **Minimal valid example of server descriptor:** 

```json
{
  "name": "my-org/weather-server",
  "description": "Weather data and forecasts via OpenWeatherMap API",
  "version": "1.0.0"
}
```

 **Minimal valid example of tools descriptor:** 

```json
{
    "tools":
    [
        {
            "name": "get_weather",
            "description": "Get the current weather for a given location",
            "inputSchema":
            {
                "type": "object",
                "properties":
                {
                    "location":
                    {
                        "type": "string",
                        "description": "City name, postal code, or latitude,longitude"
                    }
                },
                "required": ["location"]
            }
        }
    ]
}
```

 **Console:** Select **MCP** under Record type, then select **MCP server** under Descriptor. The editor shows server and tools JSON editors with an optional official schema reference.

## Agent descriptors
<a name="registry-agent-descriptors"></a>

Agents are autonomous programs that reason, plan, and take actions. For agents that follow the A2A protocol, the agent record uses the `a2aAgentCard` primary descriptor. Store the agent card in `descriptors.a2aAgentCard.data` and set `descriptors.a2aAgentCard.dataSchemaVersion`.
+  **Agent card** — Capabilities, skills, and communication interface validated against the [A2A agent card specification](https://a2a-protocol.org/latest/specification/#441-agentcard) on the A2A Protocol website. Supported `dataSchemaVersion` values, each linking to its JSON schema on the GitHub website: [1.0](https://github.com/a2aproject/A2A/blob/v1.0.1/specification/json/a2a.json), [0.3](https://github.com/a2aproject/A2A/blob/v0.3.0/specification/json/a2a.json#L138). A 1.0 card describes its endpoints in `supportedInterfaces[]` and omits the top-level `url` and `protocolVersion` that 0.3 uses. New records default to 1.0. Note that the content will be validated against \#/definitions/AgentCard in the json schema.

 **Minimal valid example (1.0):** 

```json
{
    "name": "My Agent",
    "description": "Brief description of what this agent does",
    "version": "1.0.0",
    "supportedInterfaces": [
        {
            "url": "https://api.example.com/a2a",
            "protocolBinding": "JSONRPC",
            "protocolVersion": "1.0"
        }
    ],
    "capabilities": {},
    "defaultInputModes": ["text/plain"],
    "defaultOutputModes": ["text/plain"],
    "skills": [
        {
            "id": "default-skill",
            "name": "Default Skill",
            "description": "Description of what this skill does",
            "tags": ["general"]
        }
    ]
}
```

 **Minimal valid example (0.3):** 

```json
{
    "name": "My Agent",
    "description": "Brief description of what this agent does",
    "version": "1.0.0",
    "protocolVersion": "0.3.0",
    "url": "https://api.example.com/a2a",
    "capabilities": {},
    "defaultInputModes": ["text/plain"],
    "defaultOutputModes": ["text/plain"],
    "skills": [
        {
            "id": "default-skill",
            "name": "Default Skill",
            "description": "Description of what this skill does",
            "tags": ["general"]
        }
    ]
}
```

 **Console:** Select **Agent** under Record type, then select **A2A Agent Card** under Descriptor. The editor shows **Your agent card** alongside an **Official agent card** reference schema with a version dropdown offering 1.0 (default) and 0.3. Toggle **Show official schema** to display the reference.

**Note**  
If your agent does not follow the A2A protocol, you can still publish the record under the `Agent` record type. Use the `mcpServer` descriptor if your agent uses the MCP protocol, or the `custom` descriptor for all other protocols (including agents that only expose an HTTP endpoint).

## AgentSkills descriptors
<a name="registry-agentskills-descriptors"></a>

Skills are reusable capabilities shared across agents. A skill record uses the `agentSkillsDefinition` primary descriptor. Skill content follows the [Agent Skills specification](https://agentskills.io/specification) on the Agent Skills website.

A skill record can carry its content in one of these ways:
+ Inline SKILL.md text, an inline skill definition, or both.
+ A skill package that you upload: a ZIP archive that contains SKILL.md and the scripts, references, and other files that the skill uses.
+ A source in Amazon S3 or GitHub that the registry synchronizes from. The source provides either SKILL.md only or a full skill package.

For information about how to choose between them and publish each one, see [Publish skill packages](registry-skill-packages.md).

The `agentSkillsDefinition` descriptor has the following members. All of them are optional.
+  **Skill definition** — Structured definition validated against an Amazon pre-defined schema. Store in `descriptors.agentSkillsDefinition.data`. Supported `dataSchemaVersion`: 0.1.0.
+  **Skill markdown** — `descriptors.agentSkillsDefinition.additionalData.skillMd`, with these members:
  +  `data` — Content of SKILL.md, in the format of the Agent Skills specification. Inline text gets a lighter check than a SKILL.md in a package or a synchronized source: the registry checks the frontmatter fence and the `name` and `description` fields, and the frontmatter can’t use YAML anchors, aliases, merge keys, or explicit tags. The frontmatter `name` can’t be a name that Windows reserves for a device. Otherwise, the request fails with "agentSkillsDefinition.additionalData.skillMd: The SKILL.md frontmatter name is a device name Windows reserves, such as CON or NUL. Choose another name." A SKILL.md that you later package or synchronize must meet every rule in [Skill package format and validation](registry-skill-package-format.md). When the record has a skill package or a synchronized source, the registry sets `data` to the SKILL.md from the package or source.
  +  `source` — A source that the registry synchronizes SKILL.md from, set in `source.fromUrl.url`. Use an Amazon S3 URL that names a SKILL.md or skill.md object (`s3://{bucket}/{key}`), or a GitHub URL for the folder that contains SKILL.md (`https://{host}/{owner}/{repo}/tree/{ref}/{path}`) together with `repositoryProvider`. The registry copies only SKILL.md into `skillMd.data` and serves no package.
+  **Skill package source** — `descriptors.agentSkillsDefinition.additionalData.skillPackage.source`. A source that the registry synchronizes a full skill package from: an Amazon S3 URL for a ZIP archive, or a GitHub folder URL together with `repositoryProvider`. The registry validates the package, stores it, and sets `skillMd.data` to its SKILL.md.
+  **Repository provider** — `descriptors.agentSkillsDefinition.additionalData.repositoryProvider`. Set it to `GITHUB` when `skillMd.source` or `skillPackage.source` is a GitHub folder URL. Omit it for an Amazon S3 source.
+  **Source configuration** — `descriptors.agentSkillsDefinition.additionalData.sourceConfiguration.s3.bucketOwnerAccountId`. The 12-digit AWS account ID that owns the source bucket. It applies only to an Amazon S3 source. It’s required for a public object that the registry reads without credentials, and for a bucket that is in another account.

To authorize a source, add one entry to `source.fromUrl.credentialProviderConfigurations`. An Amazon S3 source takes no credential provider (for a public object) or one `IAM` provider with `roleArn`. A GitHub source takes one `OAUTH` provider with `providerArn` and `grantType` set to `AUTHORIZATION_CODE`. For setup instructions, see [Synchronize a skill from Amazon S3](registry-skill-sync-s3.md) and [Synchronize a skill from GitHub](registry-skill-sync-github.md).

The following rules apply to skill content:
+ A record synchronizes from one source. Set `skillMd.source` or `skillPackage.source`, not both.
+ A request can upload a package or synchronize from a source, not both. A request that does either can’t also set new `skillMd.data`.
+ If you send new `skillMd.data` without an upload or a synchronization, your text replaces the package or the synchronized content, and the record no longer has a package. A source that the record had stays on the record, unused, until you change it or set `triggerSynchronization`. For more information, see [Change how a record gets its content](registry-skill-package-upload.md#registry-skill-package-upload-switch).
+ When a record gets its content from a package or a source, you don’t need to send `data` or `skillMd.data` in `agentSkillsDefinition`. With an upload, you can send `agentSkillsDefinition` as `{}`.
+ For a SKILL record, no part of the record name between slashes can be a name that Windows reserves for a device, such as `CON` or `NUL`, with or without an extension, or end with a dot. Otherwise, the request fails with "No part of a SKILL record’s name, between slashes, may be a name Windows reserves for a device, such as CON or NUL, with or without an extension, or end with a dot. Choose another name."
+ The registry doesn’t accept an `https://` URL in `skillMd.source` without `repositoryProvider` when you create a record, or when you set or change the source. A record that already stores one keeps it.
+ Skill packages and skill sources are supported only on records with `recordType` `SKILL` and the `agentSkillsDefinition` descriptor.

**Important**  
 AWS Agent Registry checks the skill definition only against the following schema. It doesn’t verify the packages in `packages[].identifier` or the repository in `repository.url`. Before you install or download them, validate them. When the registry validates a skill package, it checks the archive structure and the SKILL.md format. It doesn’t check what the scripts and other files in the package do. For more information, see [Validate record metadata before you act on it](registry-data-protection.md#registry-consumer-validation).

The skill definition schema is defined as follow:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Agent skills skill definition schema",
  "description": "Schema for skill definition metadata. All top-level fields are optional. Unknown fields are allowed for forward compatibility.",
  "type": "object",
  "properties": {
    "_meta": {
      "description": "Extension metadata using reverse DNS namespacing for vendor-specific data.",
      "type": "object"
    },
    "repository": {
      "$ref": "#/definitions/Repository"
    },
    "websiteUrl": {
      "description": "URL to the skill's homepage, documentation, or project website.",
      "type": "string",
      "format": "uri"
    },
    "packages": {
      "description": "Package distribution configurations for the skill.",
      "type": "array",
      "items": {
        "$ref": "#/definitions/Package"
      }
    }
  },
  "definitions": {
    "Repository": {
      "description": "Source code repository metadata for the skill.",
      "type": "object",
      "properties": {
        "url": {
          "description": "Repository URL for browsing source code.",
          "type": "string",
          "format": "uri"
        },
        "source": {
          "description": "Repository hosting service identifier (e.g., 'github', 'gitlab', 'codecommit').",
          "type": "string"
        }
      },
      "required": ["url", "source"]
    },
    "Package": {
      "description": "Package distribution configuration.",
      "type": "object",
      "properties": {
        "registryType": {
          "description": "Package registry type (e.g., 'npm', 'pypi').",
          "type": "string"
        },
        "identifier": {
          "description": "Package identifier in the registry (e.g., '@scope/package-name').",
          "type": "string"
        },
        "version": {
          "description": "Package version. Must be a specific version.",
          "type": "string"
        }
      },
      "required": ["registryType", "identifier"]
    }
  }
}
```

 **A valid example of skill markdown:** 

```
---
name: my-skill
description: Brief description of what this skill does.
---

# My Skill

Describe your skill's purpose, usage, and capabilities here.
```

 **A valid example of skill definition:** 

```json
{
  "websiteUrl": "https://example.com/my-skill",
  "repository": {"url": "https://github.com/example/my-skill", "source": "github"}
}
```

 **Console:** Select **Skills** under Record type, then select **Agent skills definition** under Descriptor. Under **Skill content source**, choose **Author inline** or **Upload a package**. To synchronize from Amazon S3 or GitHub, choose **Synchronize from source** as the source type when you create the record, or as the skill content source when you edit it.

### Skill package members in requests and responses
<a name="registry-agentskills-package-members"></a>

To upload a skill package, use the `artifact` request member of `CreateRegistryRecord`. It sits at the top level of the request, outside `descriptors`:
+  `artifact.content` (required) — The bytes of the ZIP archive. In JSON input, such as `--cli-input-json` in the AWS CLI, the content is base64-encoded. The AWS SDKs take the raw bytes.
+  `artifact.sha256` (optional) — The SHA-256 checksum of the ZIP archive, as 64 lowercase hexadecimal characters. The registry computes its own checksum. If yours doesn’t match, the request fails.

On `UpdateRegistryRecord`, send `artifact` as `{"optionalValue": {…​}}` to replace the package, or as `{}` to remove an uploaded package. If you omit `artifact`, the package doesn’t change. For more information, see [Upload a skill package](registry-skill-package-upload.md).

 `GetRegistryRecord` returns these additional members for a skill record. The `CreateRegistryRecord` and `UpdateRegistryRecord` responses don’t include them.
+  `artifact` — Returned when the record has a skill package. It contains `downloadUrl`, a presigned URL that is valid for up to 5 minutes, and `sha256`, the checksum to verify the downloaded package against. For more information, see [Download a skill package](registry-skill-package-download.md).
+  `synchronizedSource` — The last synchronization that the registry accepted. A synchronization that fails leaves the previous value. `synchronizedSource` is absent until the first synchronization is accepted, and after an update that replaces the synchronized content, for example with an upload. It contains one of these members:
  +  `s3` — `url`, `synchronizedAt`, and, when recorded, `versionId` (for a versioned bucket) or `eTag`.
  +  `gitHub` — `url`, `synchronizedAt`, and `commitId`.

 `BatchGetDiscoverableRegistryRecord` returns `artifact` for a record whose approved revision has a skill package. The discovery APIs return `skillMd.data`, and return the `skillMd.source` URL without its credential providers. They omit an Amazon S3 (`s3://`) source URL, and they don’t return `skillPackage`, `repositoryProvider`, or `sourceConfiguration`.

## Custom descriptors
<a name="registry-custom-descriptors"></a>

For resources not fitting standard types (for example, APIs, Lambda functions, knowledge bases, databases, and agents using other protocols), you can use the `custom` descriptor. Store the JSON content in `descriptors.custom.data`. The content must be a valid JSON.

 **Console:** Select **Custom** under Record type. The Descriptor is set to **Custom** automatically. The editor shows a single **Definition** JSON editor with no official schema reference.

## Web bot record type
<a name="registry-web-bot-record-type"></a>

The Web bot record type represents a signed-request bot identity. You can tag Web bot records — the `TagResource`, `UntagResource`, and `ListTagsForResource` actions apply to this record type. For a full description of the record type, its conceptual relationship to AWS WAF, and the scope boundary for the enforcement flow, see [Web bot records](registry-web-bot.md).

A Web bot record uses the record-type enum value `WEB_BOT` and the `signatureAgentCard` primary descriptor.
+  **Web bot definition** — Captures the record `name` and the **JWKS URL** (`jwks_uri`), the signing-directory URL where the bot publishes its public keys for verification. The record `name` (or the `client_name` in the Signature Agent Card) identifies the bot.
+  **Signature Agent Card** (`signatureAgentCard`) — The reference schema for the descriptor. It carries the bot’s identity attributes: `client_id`, `client_name`, `client_uri`, `contacts`, and `jwks_uri`. Use it as a reference while you configure your bot’s signing directory.

Keys published at the JWKS URL must be Ed25519 (`kty=OKP`, `crv=Ed25519`).

 **Category:** The record carries a category that describes the kind of web bot. Select the category that best describes your web bot — for example, **Search engine**, **AI assistant**, **AI training**, **Advertising**, **Monitoring**, or **Social media**. The console presents the full list of categories to choose from.

 **Console:** Select **Web bot** under Record type. Specify the web bot’s name, category, and the JWKS URL used for verification. The console shows the **Signature Agent Card** reference schema side-by-side as a reference while you configure your bot.

For the conceptual relationship to AWS WAF, see [Web bot records](registry-web-bot.md).