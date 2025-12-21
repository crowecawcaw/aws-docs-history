# Using tools

###### Note

This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Sonic guide, visit [Tool configuration](../nova2-userguide/sonic-tool-configuration.md "../nova2-userguide/sonic-tool-configuration.md").

In order to use a tool, it must be defined as part of the `promptStart` event in your session configuration. This is demonstrated in the following code:

```
{
  "event": {
    "promptStart": {
      "promptName": "string",
      "textOutputConfiguration": {
        "mediaType": "text/plain"
      },
      "audioOutputConfiguration": {
        "mediaType": "audio/lpcm",
        "sampleRateHertz": 8000 | 16000 | 24000,
        "sampleSizeBits": 16,
        "channelCount": 1,
        "voiceId": "matthew" | "tiffany" | "amy",
        "encoding": "base64",
        "audioType": "SPEECH"
      },
      "toolUseOutputConfiguration": {
        "mediaType": "application/json"
      },
      "toolConfiguration": {
        "tools": [
          {
            "toolSpec": {
              "name": "string",
              "description": "string",
              "inputSchema": {
                "json": "{}"
              }
            }
          }
        ]
      }
    }
  }
}
```

## Tool definition components

Each tool specification requires the following elements:

- **Name** - A unique identifier for the tool.
- **Description** - A explanation of what the tool does and when it should be used.
- **Input schema** - The JSON schema that defines the required parameters.

## Basic tool example

Here's an example of a simple tool that retrieves information about the current date. For more information on how to define a tool, see [Defining a tool](tool-use-definition.md "tool-use-definition.md").

```
// A simple tool with no required parameters
const dateTool = {
  toolSpec: {
    name: "getDateTool",
    description: "Get information about the current date",
    inputSchema: {
      json: JSON.stringify({
        type: "object",
        properties: {},
        required: []
      })
    }
  }
};
```

And here is what the `promptStart` event would look like:

```

{
  event: {
    promptStart: {
      promptName: "string",
      textOutputConfiguration: {
        mediaType: "text/plain"
      },
      audioOutputConfiguration: {
        mediaType: "audio/lpcm",
        sampleRateHertz: 24000,
        sampleSizeBits: 16,
        channelCount: 1,
        voiceId: "tiffany",
        encoding: "base64",
        audioType: "SPEECH"
      },
      toolUseOutputConfiguration: {
        mediaType: "application/json"
      },
      toolConfiguration: {
        tools: [
          {
            toolSpec: {
              name: "getDateTool",
              description: "get information about the current date",
              inputSchema: {
                json: JSON.stringify({
                  type: "object",
                  properties: {},
                  required: []
                })
              }
            }
          }
        ]
      }
    }
  }
}
```
