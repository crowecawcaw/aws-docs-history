# Hello Amazon Bedrock Runtime

The following code examples show how to get started using Amazon Bedrock Runtime.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Bedrock-runtime#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Bedrock-runtime#code-examples").

```

using Amazon;
using Amazon.BedrockRuntime;
using Amazon.BedrockRuntime.Model;

namespace BedrockRuntimeActions;

/// <summary>
/// This example shows how to use the Converse API to send a text message
/// to Amazon Bedrock.
/// </summary>
internal class HelloBedrockRuntime
{
    static async Task Main(string[] args)
    {
        // Create a Bedrock Runtime client in the AWS Region you want to use.
        // You can change the region to match your setup.
        var client = new AmazonBedrockRuntimeClient(RegionEndpoint.USWest2);

        // Set the model ID, e.g., Claude Haiku.
        // The "global." prefix enables cross-region inference, allowing the request
        // to be routed to the nearest available region for the specified model.
        var modelId = "global.anthropic.claude-haiku-4-5-20251001-v1:0";

        // Define the user message.
        var userMessage = "Hi. In a short paragraph, explain what you can do.";

        // Create a request with the model ID, the user message, and an inference configuration.
        var request = new ConverseRequest
        {
            ModelId = modelId,
            Messages = new List<Message>
            {
                new Message
                {
                    Role = ConversationRole.User,
                    Content = new List<ContentBlock> { new ContentBlock { Text = userMessage } }
                }
            }
        };

        try
        {
            // Send the request to the Bedrock Runtime and wait for the response.
            var response = await client.ConverseAsync(request);

            // Extract and print the response text.
            string responseText = response?.Output?.Message?.Content?[0]?.Text ?? "";
            Console.WriteLine(responseText);
        }
        catch (AmazonBedrockRuntimeException e)
        {
            Console.WriteLine($"ERROR: Can't invoke '{modelId}'. Reason: {e.Message}");
            throw;
        }
    }
}



```

- For API details, see
  [Converse](../../../goto/DotNetSDKV3/bedrock-runtime-2023-09-30/Converse.md "../../../goto/DotNetSDKV3/bedrock-runtime-2023-09-30/Converse.md")
  in _AWS SDK for .NET API Reference_.

**SDK for .NET (v4)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/Bedrock-runtime#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/Bedrock-runtime#code-examples").

```

using Amazon;
using Amazon.BedrockRuntime;
using Amazon.BedrockRuntime.Model;

namespace BedrockRuntimeActions;

/// <summary>
/// This example shows how to use the Converse API to send a text message
/// to Amazon Bedrock.
/// </summary>
internal class HelloBedrockRuntime
{
    static async Task Main(string[] args)
    {
        // Create a Bedrock Runtime client in the AWS Region you want to use.
        // You can change the region to match your setup.
        var client = new AmazonBedrockRuntimeClient(RegionEndpoint.USWest2);

        // Set the model ID, e.g., Claude Haiku.
        // The "global." prefix enables cross-region inference, allowing the request
        // to be routed to the nearest available region for the specified model.
        var modelId = "global.anthropic.claude-haiku-4-5-20251001-v1:0";

        // Define the user message.
        var userMessage = "Hi. In a short paragraph, explain what you can do.";

        // Create a request with the model ID, the user message, and an inference configuration.
        var request = new ConverseRequest
        {
            ModelId = modelId,
            Messages = new List<Message>
            {
                new Message
                {
                    Role = ConversationRole.User,
                    Content = new List<ContentBlock> { new ContentBlock { Text = userMessage } }
                }
            }
        };

        try
        {
            // Send the request to the Bedrock Runtime and wait for the response.
            var response = await client.ConverseAsync(request);

            // Extract and print the response text.
            string responseText = response?.Output?.Message?.Content?[0]?.Text ?? "";
            Console.WriteLine(responseText);
        }
        catch (AmazonBedrockRuntimeException e)
        {
            Console.WriteLine($"ERROR: Can't invoke '{modelId}'. Reason: {e.Message}");
            throw;
        }
    }
}



```

- For API details, see
  [Converse](../../../goto/DotNetSDKV4/bedrock-runtime-2023-09-30/Converse.md "../../../goto/DotNetSDKV4/bedrock-runtime-2023-09-30/Converse.md")
  in _AWS SDK for .NET API Reference_.

Go

**SDK for Go V2**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples").

```

package main

import (
	"context"
	"flag"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime/types"
)

// main uses the AWS SDK for Go (v2) to create an Amazon Bedrock Runtime client
// and invokes Anthropic Claude using the Converse API.
// This example uses the default settings specified in your shared credentials
// and config files.
func main() {

	region := flag.String("region", "us-east-1", "The AWS region")
	flag.Parse()

	fmt.Printf("Using AWS region: %s\n", *region)

	ctx := context.Background()
	sdkConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(*region))
	if err != nil {
		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
		fmt.Println(err)
		return
	}

	client := bedrockruntime.NewFromConfig(sdkConfig)

	// Set the model ID, e.g., Claude Haiku.
	// The "global." prefix enables cross-region inference, allowing the request
	// to be routed to the nearest available region for the specified model.
	modelId := "global.anthropic.claude-haiku-4-5-20251001-v1:0"

	// Start a conversation with the user message.
	prompt := "Hello. In a short paragraph, explain what you can do."

	message := types.Message{
		Content: []types.ContentBlock{
			&types.ContentBlockMemberText{Value: prompt},
		},
		Role: types.ConversationRoleUser,
	}

	fmt.Printf("Model: %s\n", modelId)
	fmt.Printf("Prompt: %s\n\n", prompt)

	result, err := client.Converse(ctx, &bedrockruntime.ConverseInput{
		ModelId:  aws.String(modelId),
		Messages: []types.Message{message},
	})

	if err != nil {
		log.Fatalf("ERROR: Can't invoke '%s'. Reason: %v\n", modelId, err)
	}

	// Extract and print the response text.
	responseMessage, ok := result.Output.(*types.ConverseOutputMemberMessage)
	if !ok {
		log.Fatal("ERROR: Unexpected output type from Converse API")
	}
	responseContentBlock := responseMessage.Value.Content[0]
	text, ok := responseContentBlock.(*types.ContentBlockMemberText)
	if !ok {
		log.Fatal("ERROR: Unexpected content block type from Converse API")
	}
	fmt.Printf("Response: %s\n", text.Value)
}



```

- For API details, see
  [Converse](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.Converse "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.Converse")
  in _AWS SDK for Go API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/bedrock-runtime#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/bedrock-runtime#code-examples").

```

import { fileURLToPath } from "node:url";
import {
  BedrockRuntimeClient,
  ConverseCommand,
} from "@aws-sdk/client-bedrock-runtime";

// Send a prompt to Amazon Bedrock using the Converse API.

const AWS_REGION = "us-east-1";

// Set the model ID, e.g., Claude Haiku.
// The "global." prefix enables cross-region inference, allowing the request
// to be routed to the nearest available region for the specified model.
const MODEL_ID = "global.anthropic.claude-haiku-4-5-20251001-v1:0";
const PROMPT = "Hi. In a short paragraph, explain what you can do.";

const hello = async () => {
  console.log("=".repeat(35));
  console.log("Welcome to the Amazon Bedrock demo!");
  console.log("=".repeat(35));

  console.log("Model: Anthropic Claude Haiku");
  console.log(`Prompt: ${PROMPT}\n`);
  console.log("Invoking model...\n");

  // Create a new Bedrock Runtime client instance.
  const client = new BedrockRuntimeClient({ region: AWS_REGION });

  // Create the command with the model ID, the user message, and a basic configuration.
  const command = new ConverseCommand({
    modelId: MODEL_ID,
    messages: [
      {
        role: "user",
        content: [{ text: PROMPT }],
      },
    ],
  });

  // Send the command to the model and wait for the response.
  try {
    const response = await client.send(command);

    // Extract and print the response text.
    const responseText = response.output.message.content[0].text;
    console.log(`Response: ${responseText}`);
  } catch (caught) {
    if (
      caught instanceof Error &&
      caught.name === "BedrockRuntimeServiceException"
    ) {
      console.error(
        `ERROR: Can't invoke '${MODEL_ID}'. Reason: ${caught.message}`,
      );
      throw caught;
    }
    throw caught;
  }
};

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  await hello();
}


```

- For API details, see
  [Converse](../../../AWSJavaScriptSDK/v3/latest/client/bedrock-runtime/command/ConverseCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/bedrock-runtime/command/ConverseCommand.md")
  in _AWS SDK for JavaScript API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Bedrock with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
