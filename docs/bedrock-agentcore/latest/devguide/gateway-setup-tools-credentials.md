# Set up dependencies and credentials to create, maintain, and use gateway resources

The AgentCore Gateway service involves the following main processes:

- **Creation and maintenance of gateway resources** – You can create gateway and gateway target resources through the Amazon Bedrock AgentCore Control Plane service.
- **Invocation of gateways** – After creating a gateway and gateway target, you can invoke the gateway through direct HTTP requests to the gateway or through the help of an MCP client or agent.
  Select a topic to learn about setting up tools and credentials for carrying out these processes:

###### Topics

- [Set up tools and credentials for the creation and maintenance of gateway resources](#gateway-setup-control-plane "#gateway-setup-control-plane")
- [Invocation of gateways](#gateway-setup-data-plane "#gateway-setup-data-plane")

## Set up tools and credentials for the creation and maintenance of gateway resources

You create, modify, delete, and retrieve information about gateway and gateway target resources through making calls to the Amazon Bedrock AgentCore Control Plane service. The [Amazon Bedrock AgentCore Control Plane service API reference](../../../bedrock-agentcore-control/latest/APIReference/Welcome.md "../../../bedrock-agentcore-control/latest/APIReference/Welcome.md") details information about the API operations and structures in this service.

You can interact with the Amazon Bedrock AgentCore Control Plane service in the following ways. Expand a topic to learn how to install the tool and set up authentication for it.

The AWS Management Console lets you create and maintain gateway and gateway target resources through an interactive graphical interface in a web browser.

- **Installation** – None needed. To manage gateways through the AgentCore console, you can navigate to [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#") and select **Gateways** from the left navigation pane.
- **Authentication** – Sign in with an IAM identity with permissions to use AgentCore Gateway actions.
  The [Amazon Bedrock AgentCore Control Plane service API reference](../../../bedrock-agentcore-control/latest/APIReference/Welcome.md "../../../bedrock-agentcore-control/latest/APIReference/Welcome.md") page for each API operations provides the information you need to make an API request.

- **Installation** – None needed.
- **Authentication** – You can use the [Authorization header](../../../IAM/latest/UserGuide/reference_sigv-authentication-methods.md "../../../IAM/latest/UserGuide/reference_sigv-authentication-methods.md") or query parameters (using [AWS Signature Version 4](../../../AmazonS3/latest/API/sigv4-query-string-auth.md "../../../AmazonS3/latest/API/sigv4-query-string-auth.md")) to authenticate.
  AWS SDKs let you make API requests to AWS services through a programming language of your choice. Refer to the following resources in the [AWS SDKs and Tools Reference Guide](../../../sdkref/latest/guide/overview.md "../../../sdkref/latest/guide/overview.md") to get set up:

- **Installation** – To learn about an SDK and how to install it, select the **AWS SDK for** link that corresponds to your programming language of choice.
- **Authentication** – To learn about configuring SDKs and authentication, refer to the links in the **This guide's relevant sections for you are:** column.
- **Other resources** – In the language-specific reference, search for the Amazon Bedrock AgentCore Core Control service to see the syntax of specific API methods.
  The AWS Command Line Interface (CLI) lets you interact with the AWS API in a command line interface. To learn how to install and set up the AWS CLI, see [Getting started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

- **Installation** – To learn how to install the AWS CLI see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- **Authentication** – To learn about configuring your credentials in the AWS CLI see [Setting up the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md").
- **Other resources** – To see the syntax of specific API methods in the Amazon Bedrock AgentCore control plane service, see the [bedrock-agentcore-control](../../../cli/latest/reference/bedrock-agentcore-control.md "../../../cli/latest/reference/bedrock-agentcore-control.md") reference.
  The AgentCore starter toolkit is a Python SDK that provides tools to help you easily interact with the AgentCore API. Refer to the following resources in the [AgentCore starter toolkit repository](../../../https:/github.com/aws/bedrock-agentcore-starter-toolkit.md "../../../https:/github.com/aws/bedrock-agentcore-starter-toolkit.md").

- **Installation** – To learn how to install the starter toolkit, follow the steps at [Installation](../../../https:/github.com/aws/bedrock-agentcore-starter-toolkit.md#installation "../../../https:/github.com/aws/bedrock-agentcore-starter-toolkit.md#installation").
- **Authentication** – To access your AWS credentials and configure them for the AgentCore starter toolkit, follow the steps at [Using IAM Identity Center to authenticate AWS SDK and Tools](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md").
- **Other resources** – You use the Gateway client in this toolkit to interact with AgentCore Gateway. For more information, see [AgentCore Gateway client](../../../https:/github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/src/bedrock_agentcore_starter_toolkit/operations/gateway/client.md "../../../https:/github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/src/bedrock_agentcore_starter_toolkit/operations/gateway/client.md").

## Invocation of gateways

After you create a gateway and gateway targets, you can interact with the gateway through direct HTTP requests or through an MCP client or agent.

To make an HTTP request to an AgentCore gateway, you make a POST request to a gateway endpoint that you set up when creating a gateway.

- **Installation** – None needed.
- **Authentication** – You can use the [Authorization header](../../../IAM/latest/UserGuide/reference_sigv-authentication-methods.md "../../../IAM/latest/UserGuide/reference_sigv-authentication-methods.md") or query parameters (using [AWS Signature Version 4](../../../AmazonS3/latest/API/sigv4-query-string-auth.md "../../../AmazonS3/latest/API/sigv4-query-string-auth.md")) to authenticate.
  To interact with an AgentCore gateway using an MCP client, you need to install the MCP client by following the **Setting up your environment** and **Setting up your API key** steps at [Build an MCP client](https://modelcontextprotocol.io/docs/develop/build-client "https://modelcontextprotocol.io/docs/develop/build-client") after choosing your programming language of choice. By following the steps, you'll also retrieve an Anthropic API key for authentication.

To interact with an AgentCore gateway using the Strands Agents SDK, you need to install the Strands SDK by following the steps at [Strands Agents SDK](https://strandsagents.com/latest/documentation/docs/ "https://strandsagents.com/latest/documentation/docs/") to install the SDK and set up credentials.

To interact with an AgentCore gateway using a Langgraph agent, you need to install Langgraph by navigating to [LangGraph](https://www.langchain.com/langgraph "https://www.langchain.com/langgraph"), selecting **Docs**, and choosing the **LangGraph** page that corresponds to your programming language of choice. By following these steps, you'll also receive an API key to help set up your credentials.
