# Use a Provisioned Throughput with an Amazon Bedrock resource

After you purchase a Provisioned Throughput, you can use it with the following features:

- **Model inference** – You can test the Provisioned Throughput in an Amazon Bedrock console playground. When you're ready to deploy the Provisioned Throughput, set up your application to invoke the provisioned model. Choose the tab for your preferred method, and then follow the steps:

Console

###### To use a Provisioned Throughput in the Amazon Bedrock console playground

    1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
     [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
    2. From the left navigation pane, select **Chat**, **Text**, or **Image** under **Playgrounds**, depending your use case.
    3. Choose **Select model**.
    4. In the **1. Category** column, select a provider or custom model category. Then, in the **2. Model** column, select the model that your Provisioned Throughput is associated with.
    5. In the **3. Throughput** column, select your Provisioned Throughput.
    6. Choose **Apply**.

To learn how to use the Amazon Bedrock playgrounds, see [Generate responses in the console using playgrounds](playgrounds.md "playgrounds.md").

API
To run inference using a Provisioned Throughput, send an [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md"), [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md"), [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"), or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") request with an [Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#br-rt "../../../general/latest/gr/bedrock.md#br-rt"). Specify the provisioned model ARN as the `modelId` parameter. To see requirements for the request body for different models, see [Inference request parameters and response fields for foundation models](model-parameters.md "model-parameters.md").

[See code examples](prov-thru-code-examples.md "prov-thru-code-examples.md")

- **Associate a Provisioned Throughput with an agent alias** – You can associate a Provisioned Throughput when you [create](agents-deploy.md "agents-deploy.md") or [update](agents-alias-edit.md "agents-alias-edit.md") an agent alias. In the Amazon Bedrock console, you choose the Provisioned Throughput when setting up the alias or editing it. In the Amazon Bedrock API, you specify the `provisionedThroughput` in the `routingConfiguration` when you send a [CreateAgentAlias](../APIReference/API_agent_CreateAgentAlias.md "../APIReference/API_agent_CreateAgentAlias.md") or [UpdateAgentAlias](../APIReference/API_agent_UpdateAgentAlias.md "../APIReference/API_agent_UpdateAgentAlias.md"); request.
