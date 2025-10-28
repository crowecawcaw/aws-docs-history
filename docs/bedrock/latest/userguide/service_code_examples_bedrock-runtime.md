# Code examples for Amazon Bedrock Runtime using AWS SDKs

The following code examples show how to use Amazon Bedrock Runtime with an AWS software development kit (SDK).

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Bedrock with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Amazon Bedrock.

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
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
)

// Each model provider defines their own individual request and response formats.
// For the format, ranges, and default values for the different models, refer to:
// https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html

type ClaudeRequest struct {
	Prompt            string `json:"prompt"`
	MaxTokensToSample int    `json:"max_tokens_to_sample"`
	// Omitting optional request parameters
}

type ClaudeResponse struct {
	Completion string `json:"completion"`
}

// main uses the AWS SDK for Go (v2) to create an Amazon Bedrock Runtime client
// and invokes Anthropic Claude 2 inside your account and the chosen region.
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

	modelId := "anthropic.claude-v2"

	prompt := "Hello, how are you today?"

	// Anthropic Claude requires you to enclose the prompt as follows:
	prefix := "Human: "
	postfix := "\n\nAssistant:"
	wrappedPrompt := prefix + prompt + postfix

	request := ClaudeRequest{
		Prompt:            wrappedPrompt,
		MaxTokensToSample: 200,
	}

	body, err := json.Marshal(request)
	if err != nil {
		log.Panicln("Couldn't marshal the request: ", err)
	}

	result, err := client.InvokeModel(ctx, &bedrockruntime.InvokeModelInput{
		ModelId:     aws.String(modelId),
		ContentType: aws.String("application/json"),
		Body:        body,
	})

	if err != nil {
		errMsg := err.Error()
		if strings.Contains(errMsg, "no such host") {
			fmt.Printf("Error: The Bedrock service is not available in the selected region. Please double-check the service availability for your region at https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/.\n")
		} else if strings.Contains(errMsg, "Could not resolve the foundation model") {
			fmt.Printf("Error: Could not resolve the foundation model from model identifier: \"%v\". Please verify that the requested model exists and is accessible within the specified region.\n", modelId)
		} else {
			fmt.Printf("Error: Couldn't invoke Anthropic Claude. Here's why: %v\n", err)
		}
		os.Exit(1)
	}

	var response ClaudeResponse

	err = json.Unmarshal(result.Body, &response)

	if err != nil {
		log.Fatal("failed to unmarshal", err)
	}
	fmt.Println("Prompt:\n", prompt)
	fmt.Println("Response from Anthropic Claude:\n", response.Completion)
}



```

- For API details, see
  [InvokeModel](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModel "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModel")
  in _AWS SDK for Go API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/bedrock-runtime#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/bedrock-runtime#code-examples").

```

/**
 * @typedef {Object} Content
 * @property {string} text
 *
 * @typedef {Object} Usage
 * @property {number} input_tokens
 * @property {number} output_tokens
 *
 * @typedef {Object} ResponseBody
 * @property {Content[]} content
 * @property {Usage} usage
 */

import { fileURLToPath } from "node:url";
import {
  BedrockRuntimeClient,
  InvokeModelCommand,
} from "@aws-sdk/client-bedrock-runtime";

const AWS_REGION = "us-east-1";

const MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0";
const PROMPT = "Hi. In a short paragraph, explain what you can do.";

const hello = async () => {
  console.log("=".repeat(35));
  console.log("Welcome to the Amazon Bedrock demo!");
  console.log("=".repeat(35));

  console.log("Model: Anthropic Claude 3 Haiku");
  console.log(`Prompt: ${PROMPT}\n`);
  console.log("Invoking model...\n");

  // Create a new Bedrock Runtime client instance.
  const client = new BedrockRuntimeClient({ region: AWS_REGION });

  // Prepare the payload for the model.
  const payload = {
    anthropic_version: "bedrock-2023-05-31",
    max_tokens: 1000,
    messages: [{ role: "user", content: [{ type: "text", text: PROMPT }] }],
  };

  // Invoke Claude with the payload and wait for the response.
  const apiResponse = await client.send(
    new InvokeModelCommand({
      contentType: "application/json",
      body: JSON.stringify(payload),
      modelId: MODEL_ID,
    }),
  );

  // Decode and return the response(s)
  const decodedResponseBody = new TextDecoder().decode(apiResponse.body);
  /** @type {ResponseBody} */
  const responseBody = JSON.parse(decodedResponseBody);
  const responses = responseBody.content;

  if (responses.length === 1) {
    console.log(`Response: ${responses[0].text}`);
  } else {
    console.log("Haiku returned multiple responses:");
    console.log(responses);
  }

  console.log(`\nNumber of input tokens:   ${responseBody.usage.input_tokens}`);
  console.log(`Number of output tokens: ${responseBody.usage.output_tokens}`);
};

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  await hello();
}


```

- For API details, see
  [InvokeModel](../../../AWSJavaScriptSDK/v3/latest/client/bedrock-runtime/command/InvokeModelCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/bedrock-runtime/command/InvokeModelCommand.md")
  in _AWS SDK for JavaScript API Reference_.

###### Code examples

- [Basics](service_code_examples_bedrock-runtime_basics.md "service_code_examples_bedrock-runtime_basics.md")
  - [Hello Amazon Bedrock](bedrock-runtime_example_bedrock-runtime_Hello_section.md "bedrock-runtime_example_bedrock-runtime_Hello_section.md")

- [Scenarios](service_code_examples_bedrock-runtime_scenarios.md "service_code_examples_bedrock-runtime_scenarios.md")
  - [Create a playground application to interact with Amazon Bedrock foundation models](bedrock-runtime_example_cross_FMPlayground_section.md "bedrock-runtime_example_cross_FMPlayground_section.md")
  - [Create and invoke a managed prompt](bedrock-runtime_example_bedrock-agent_GettingStartedWithBedrockPrompts_section.md "bedrock-runtime_example_bedrock-agent_GettingStartedWithBedrockPrompts_section.md")
  - [Generate videos from text prompts using Amazon Bedrock](bedrock-runtime_example_bedrock-runtime_Scenario_GenerateVideos_NovaReel_section.md "bedrock-runtime_example_bedrock-runtime_Scenario_GenerateVideos_NovaReel_section.md")
  - [Invoke multiple foundation models on Amazon Bedrock](bedrock-runtime_example_bedrock-runtime_Scenario_InvokeModels_section.md "bedrock-runtime_example_bedrock-runtime_Scenario_InvokeModels_section.md")
  - [Orchestrate generative AI applications with Step Functions](bedrock-runtime_example_cross_ServerlessPromptChaining_section.md "bedrock-runtime_example_cross_ServerlessPromptChaining_section.md")
  - [Tool use with the Converse API](bedrock-runtime_example_bedrock-runtime_Scenario_ToolUse_section.md "bedrock-runtime_example_bedrock-runtime_Scenario_ToolUse_section.md")

- [Amazon Nova](service_code_examples_bedrock-runtime_amazon_nova.md "service_code_examples_bedrock-runtime_amazon_nova.md")
  - [Converse](bedrock-runtime_example_bedrock-runtime_Converse_AmazonNovaText_section.md "bedrock-runtime_example_bedrock-runtime_Converse_AmazonNovaText_section.md")
  - [ConverseStream](bedrock-runtime_example_bedrock-runtime_ConverseStream_AmazonNovaText_section.md "bedrock-runtime_example_bedrock-runtime_ConverseStream_AmazonNovaText_section.md")
  - [Document understanding](bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_AmazonNova_section.md "bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_AmazonNova_section.md")
  - [Scenario: Tool use with the Converse API](bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_AmazonNova_section.md "bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_AmazonNova_section.md")

- [Amazon Nova Canvas](service_code_examples_bedrock-runtime_amazon_nova_canvas.md "service_code_examples_bedrock-runtime_amazon_nova_canvas.md")
  - [InvokeModel](bedrock-runtime_example_bedrock-runtime_InvokeModel_AmazonNovaImageGeneration_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModel_AmazonNovaImageGeneration_section.md")

- [Amazon Nova Reel](service_code_examples_bedrock-runtime_amazon_nova_reel.md "service_code_examples_bedrock-runtime_amazon_nova_reel.md")
  - [Text-to-video](bedrock-runtime_example_bedrock-runtime_Scenario_AmazonNova_TextToVideo_section.md "bedrock-runtime_example_bedrock-runtime_Scenario_AmazonNova_TextToVideo_section.md")

- [Amazon Titan Image Generator](service_code_examples_bedrock-runtime_amazon_titan_image_generator.md "service_code_examples_bedrock-runtime_amazon_titan_image_generator.md")
  - [InvokeModel](bedrock-runtime_example_bedrock-runtime_InvokeModel_TitanImageGenerator_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModel_TitanImageGenerator_section.md")

- [Amazon Titan Text](service_code_examples_bedrock-runtime_amazon_titan_text.md "service_code_examples_bedrock-runtime_amazon_titan_text.md")
  - [InvokeModel](bedrock-runtime_example_bedrock-runtime_InvokeModel_TitanText_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModel_TitanText_section.md")

- [Amazon Titan Text Embeddings](service_code_examples_bedrock-runtime_amazon_titan_text_embeddings.md "service_code_examples_bedrock-runtime_amazon_titan_text_embeddings.md")
  - [InvokeModel](bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_TitanTextEmbeddings_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_TitanTextEmbeddings_section.md")

- [Anthropic Claude](service_code_examples_bedrock-runtime_anthropic_claude.md "service_code_examples_bedrock-runtime_anthropic_claude.md")
  - [Converse](bedrock-runtime_example_bedrock-runtime_Converse_AnthropicClaude_section.md "bedrock-runtime_example_bedrock-runtime_Converse_AnthropicClaude_section.md")
  - [ConverseStream](bedrock-runtime_example_bedrock-runtime_ConverseStream_AnthropicClaude_section.md "bedrock-runtime_example_bedrock-runtime_ConverseStream_AnthropicClaude_section.md")
  - [Document understanding](bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_AnthropicClaude_section.md "bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_AnthropicClaude_section.md")
  - [InvokeModel](bedrock-runtime_example_bedrock-runtime_InvokeModel_AnthropicClaude_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModel_AnthropicClaude_section.md")
  - [InvokeModelWithResponseStream](bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_AnthropicClaude_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_AnthropicClaude_section.md")
  - [Reasoning](bedrock-runtime_example_bedrock-runtime_Converse_AnthropicClaudeReasoning_section.md "bedrock-runtime_example_bedrock-runtime_Converse_AnthropicClaudeReasoning_section.md")
  - [Reasoning with a streaming response](bedrock-runtime_example_bedrock-runtime_ConverseStream_AnthropicClaudeReasoning_section.md "bedrock-runtime_example_bedrock-runtime_ConverseStream_AnthropicClaudeReasoning_section.md")
  - [Scenario: Tool use with the Converse API](bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_AnthropicClaude_section.md "bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_AnthropicClaude_section.md")

- [Cohere Command](service_code_examples_bedrock-runtime_cohere_command.md "service_code_examples_bedrock-runtime_cohere_command.md")
  - [Converse](bedrock-runtime_example_bedrock-runtime_Converse_CohereCommand_section.md "bedrock-runtime_example_bedrock-runtime_Converse_CohereCommand_section.md")
  - [ConverseStream](bedrock-runtime_example_bedrock-runtime_ConverseStream_CohereCommand_section.md "bedrock-runtime_example_bedrock-runtime_ConverseStream_CohereCommand_section.md")
  - [Document understanding](bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_CohereCommand_section.md "bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_CohereCommand_section.md")
  - [InvokeModel: Command R and R+](bedrock-runtime_example_bedrock-runtime_InvokeModel_CohereCommandR_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModel_CohereCommandR_section.md")
  - [InvokeModelWithResponseStream: Command R and R+](bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_CohereCommandR_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_CohereCommandR_section.md")
  - [Scenario: Tool use with the Converse API](bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_CohereCommand_section.md "bedrock-runtime_example_bedrock-runtime_Scenario_ToolUseDemo_CohereCommand_section.md")

- [DeepSeek](service_code_examples_bedrock-runtime_deepseek.md "service_code_examples_bedrock-runtime_deepseek.md")
  - [Document understanding](bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_DeepSeek_section.md "bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_DeepSeek_section.md")

- [Meta Llama](service_code_examples_bedrock-runtime_meta_llama.md "service_code_examples_bedrock-runtime_meta_llama.md")
  - [Converse](bedrock-runtime_example_bedrock-runtime_Converse_MetaLlama_section.md "bedrock-runtime_example_bedrock-runtime_Converse_MetaLlama_section.md")
  - [ConverseStream](bedrock-runtime_example_bedrock-runtime_ConverseStream_MetaLlama_section.md "bedrock-runtime_example_bedrock-runtime_ConverseStream_MetaLlama_section.md")
  - [Document understanding](bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_MetaLlama_section.md "bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_MetaLlama_section.md")
  - [InvokeModel](bedrock-runtime_example_bedrock-runtime_InvokeModel_MetaLlama3_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModel_MetaLlama3_section.md")
  - [InvokeModelWithResponseStream](bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_MetaLlama3_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_MetaLlama3_section.md")

- [Mistral AI](service_code_examples_bedrock-runtime_mistral_ai.md "service_code_examples_bedrock-runtime_mistral_ai.md")
  - [Converse](bedrock-runtime_example_bedrock-runtime_Converse_Mistral_section.md "bedrock-runtime_example_bedrock-runtime_Converse_Mistral_section.md")
  - [ConverseStream](bedrock-runtime_example_bedrock-runtime_ConverseStream_Mistral_section.md "bedrock-runtime_example_bedrock-runtime_ConverseStream_Mistral_section.md")
  - [Document understanding](bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_Mistral_section.md "bedrock-runtime_example_bedrock-runtime_DocumentUnderstanding_Mistral_section.md")
  - [InvokeModel](bedrock-runtime_example_bedrock-runtime_InvokeModel_MistralAi_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModel_MistralAi_section.md")
  - [InvokeModelWithResponseStream](bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_MistralAi_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModelWithResponseStream_MistralAi_section.md")

- [Stable Diffusion](service_code_examples_bedrock-runtime_stable_diffusion.md "service_code_examples_bedrock-runtime_stable_diffusion.md")
  - [InvokeModel](bedrock-runtime_example_bedrock-runtime_InvokeModel_StableDiffusion_section.md "bedrock-runtime_example_bedrock-runtime_InvokeModel_StableDiffusion_section.md")
