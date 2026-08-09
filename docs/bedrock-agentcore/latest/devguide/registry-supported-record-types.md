# Supported record types and descriptors

###### Migration Now Open

AWS Agent Registry has launched under the new `agent-registry` namespace. Support for the public preview `bedrock-agentcore` namespace will be discontinued on September 17, 2026. For migration instructions, see [Comprehensive registry migration guide](registry-faq.md "registry-faq.md").

AWS Agent Registry validates record content against official protocol schemas. The console displays the reference schema side-by-side with your input and shows inline validation errors with a **Diagnose with Amazon Q** button. The registry supports all versions of the MCP Protocol Schema and the A2A Schema.

When you create a record, you choose two things:

- The record’s **record type** — a semantic classification (`AGENT`, `MCP`, `SKILL`, or `CUSTOM`) that determines which descriptors are valid.
- The record’s **descriptor** — the shape of the actual record content (schema, versioning rules, sync support). Exactly one primary descriptor key may be populated per record.
  Each record also has metadata fields — `name` (a unique name for each record), `displayName`, `description`, `recordVersion`, `recordType`, and `tags` — plus the `descriptors` structure where the descriptor content lives.

Valid descriptors per record type:

- **AGENT:**
  `a2aAgentCard`, `mcpServer`, `custom`
- **MCP:**
  `mcpServer`, `custom`
- **SKILL:**
  `agentSkillsDefinition`, `custom`
- **CUSTOM:**
  `custom`

## MCP descriptors

An MCP server record uses the `mcpServer` primary descriptor. Store the server definition JSON in `descriptors.mcpServer.data` and set `descriptors.mcpServer.dataSchemaVersion` to the schema version. Tool definitions nest under `descriptors.mcpServer.additionalData.tools`:

- **Server** — Based on the server.json definition from the [official Model Context Protocol registry](https://registry.modelcontextprotocol.io/ "https://registry.modelcontextprotocol.io/") on the Model Context Protocol website. The content is validated against the selected schema version, which can be found in the [MCP schema repository](https://github.com/modelcontextprotocol/static/tree/main/schemas "https://github.com/modelcontextprotocol/static/tree/main/schemas") on the GitHub website. Supported `dataSchemaVersion` values: [2025-12-11](https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json"), [2025-10-17](https://static.modelcontextprotocol.io/schemas/2025-10-17/server.schema.json "https://static.modelcontextprotocol.io/schemas/2025-10-17/server.schema.json"), [2025-10-11](https://static.modelcontextprotocol.io/schemas/2025-10-11/server.schema.json "https://static.modelcontextprotocol.io/schemas/2025-10-11/server.schema.json"), [2025-09-29](https://static.modelcontextprotocol.io/schemas/2025-09-29/server.schema.json "https://static.modelcontextprotocol.io/schemas/2025-09-29/server.schema.json"), [2025-09-16](https://static.modelcontextprotocol.io/schemas/2025-09-16/server.schema.json "https://static.modelcontextprotocol.io/schemas/2025-09-16/server.schema.json"), [2025-07-09](https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json "https://static.modelcontextprotocol.io/schemas/2025-07-09/server.schema.json"). If you do not have a server.json, we recommend you create one with the latest schema.
- **Tools** — Tools available on the server, validated against the [MCP protocol specification](https://modelcontextprotocol.io/specification/2025-11-25/schema "https://modelcontextprotocol.io/specification/2025-11-25/schema") on the Model Context Protocol website. Supported `dataSchemaVersion` values: [2025-11-25](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-11-25/schema.json "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-11-25/schema.json"), [2025-06-18](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-06-18/schema.json "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-06-18/schema.json"), [2025-03-26](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-03-26/schema.json "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2025-03-26/schema.json"), [2024-11-05](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2024-11-05/schema.json "https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/schema/2024-11-05/schema.json").

**Minimal valid example of server descriptor:**

```
{
  "name": "my-org/weather-server",
  "description": "Weather data and forecasts via OpenWeatherMap API",
  "version": "1.0.0"
}
```

**Minimal valid example of tools descriptor:**

```
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

Agents are autonomous programs that reason, plan, and take actions. For agents that follow the A2A protocol, the agent record uses the `a2aAgentCard` primary descriptor. Store the agent card in `descriptors.a2aAgentCard.data` and set `descriptors.a2aAgentCard.dataSchemaVersion`.

- **Agent card** — Capabilities, skills, and communication interface validated against the [A2A agent card specification](https://a2a-protocol.org/latest/specification/#441-agentcard "https://a2a-protocol.org/latest/specification/#441-agentcard") on the A2A Protocol website. Supported `dataSchemaVersion`: [0.3](https://github.com/a2aproject/A2A/blob/v0.3.0/specification/json/a2a.json#L138 "https://github.com/a2aproject/A2A/blob/v0.3.0/specification/json/a2a.json#L138"). Note that the content will be validated against #/definitions/AgentCard in the json schema.

**Minimal valid example:**

```
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

**Console:** Select **Agent** under Record type, then select **A2A Agent Card** under Descriptor. The editor shows **Your agent card** alongside an **Official agent card** reference schema with a version dropdown (e.g., 0.3). Toggle **Show official schema** to display the reference.

###### Note

If your agent does not follow the A2A protocol, you can still publish the record under the `Agent` record type. Use the `mcpServer` descriptor if your agent uses the MCP protocol, or the `custom` descriptor for all other protocols (including agents that only expose an HTTP endpoint).

## AgentSkills descriptors

Skills are reusable capabilities shared across agents. A skill record uses the `agentSkillsDefinition` primary descriptor. The optional skill markdown nests under `descriptors.agentSkillsDefinition.additionalData.skillMd`.

- **Skill markdown (optional)** — Content of SKILL.md, validated against the [official AgentSkills specification](https://agentskills.io/home "https://agentskills.io/home") on the AgentSkills website. Store in `descriptors.agentSkillsDefinition.additionalData.skillMd.data`. Note that the markdown is only used as metadata for discovery purpose. Registry does not support storing other agent skill files.
- **Skill definition (optional)** — Structured definition validated against an Amazon pre-defined schema. Store in `descriptors.agentSkillsDefinition.data`. Supported `dataSchemaVersion`: 0.1.0.

The skill definition schema is defined as follow:

```
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

```
{
  "websiteUrl": "https://example.com/my-skill",
  "repository": {"url": "https://github.com/example/my-skill", "source": "github"}
}
```

**Console:** Select **Skills** under Record type, then select **Agent skills definition** under Descriptor.

## Custom descriptors

For resources not fitting standard types (for example, APIs, Lambda functions, knowledge bases, databases, and agents using other protocols), you can use the `custom` descriptor. Store the JSON content in `descriptors.custom.data`. The content must be a valid JSON.

**Console:** Select **Custom** under Record type. The Descriptor is set to **Custom** automatically. The editor shows a single **Definition** JSON editor with no official schema reference.
