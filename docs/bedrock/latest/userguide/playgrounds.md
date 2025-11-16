# Generate responses in the console using playgrounds

The Amazon Bedrock playgrounds are a tool in the AWS Management Console that provide a visual interface to experiment with running inference on different models and using different configurations. You can use the playgrounds to test different models and values before you integrate them into your application.

Running a prompt in a playground is equivalent to making an [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md"), [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md"), [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"), or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") request in the API.

Amazon Bedrock offers the following playgrounds for you to experiment with:

- **Chat/text** – Submit text prompts and generate responses, or interact with speech. You can select one of the following modes:
  - **Chat** – Submit a text prompt or interact with speech. For text prompts, you can also include images or documents to supplement the prompt. Subsequent prompts that you submit will include your previous prompts as context, such that the sequence of prompts and responses resembles a conversation.
  - **Single prompt** – Submit a single text prompt and generate a response to it.

###### Note

Speech-to-speech models such as Amazon Nova Sonic are only available in chat mode. Compare mode is not supported for speech-to-speech models.

- **Image** – Submit a text prompt to generate an image. You can also submit an image prompt and specify whether to edit it or to generate variations of it.
  The following procedure describes how to submit a prompt in the playground, the options that you can adjust, and the actions that you can take after the model generates a response.

###### To use a playground

1.  If you haven't already, request access to the models that you want to use.
    For more information, see [Access Amazon Bedrock foundation models](model-access.md "model-access.md").
2.  Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
    [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
3.  From the navigation pane, under
    **Playgrounds**, choose **Chat/text** or
    **Image**.
4.  If you're in the **Chat/text** playground, select a **Mode**.
5.  Choose **Select model** and select a provider, model, and throughput to use. For more information about increasing throughput, see [Increase throughput with cross-Region
    inference](cross-region-inference.md "cross-region-inference.md") and [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](prov-throughput.md "prov-throughput.md").
6.  Submit the following information to generate a response:
    - Prompt – One or more sentences of text that set up a scenario, question, or
      task for a model. For information about creating prompts, see [Prompt engineering concepts](prompt-engineering-guidelines.md "prompt-engineering-guidelines.md").

    If you're using the chat mode of the chat/text playground, some models (refer to [Supported models and
    model features](conversation-inference-supported-models-features.md "conversation-inference-supported-models-features.md")) allow you to include a file in the following ways:

        + Select the attachment icon and choose a file to upload.
        + Select the attachment icon and choose an Amazon S3 object to upload.
        + Drag a file onto the prompt.

    Include files to complement your prompt. You can refer to the file in the prompt text. For example, you could write `Summarize this document for me` or `Tell me what's in this image`. You can include the following types of files:

        + **Documents** – Add documents to complement the prompt. For a list of supported file types, see the `format` field in [DocumentBlock](../APIReference/API_runtime_DocumentBlock.md "../APIReference/API_runtime_DocumentBlock.md").


        ###### Warning

        Document names are vulnerable to prompt injections, because the model might inadvertently interpret them as instructions. Therefore, we recommend that you specify a neutral name.
        + **Images** – Add images to complement the prompt, if the model supports multimodal image and text inputs. For a list of supported file types, see the `format` field in the [ImageBlock](../APIReference/API_runtime_ImageBlock.md "../APIReference/API_runtime_ImageBlock.md").
        + **Videos** – Add videos to complement the prompt, if the model supports multimodal video and text inputs. For a list of supported file types, see the `format` field in the [VideoBlock](../APIReference/API_runtime_VideoBlock.md "../APIReference/API_runtime_VideoBlock.md").

    - Configurations – Settings that you adjust to modify the model response. Configurations include the following:
      - Inference parameters – Values that affect or limit how the model generates the response. For more information, see [Influence response generation with inference parameters](inference-parameters.md "inference-parameters.md"). To see inference parameters for specific models, refer to [Inference request parameters and response fields for foundation models](model-parameters.md "model-parameters.md").
      - System prompts – Prompts that provide instructions or context to the model about the task that it should perform or the persona that it should adopt. These are only available in the chat mode of the chat/text playground. For more information and a list of models that support system prompts, see [Carry out a conversation with the
        Converse API operations](conversation-inference.md "conversation-inference.md").
      - Guardrails – Filters out harmful or unwanted content in prompts and model responses. For more information, see [Detect and filter harmful content by using Amazon Bedrock Guardrails](guardrails.md "guardrails.md").

7.  (Optional) If a model supports streaming, the default behavior in the chat/text playground is to stream the responses. You can turn off streaming by choosing the options icon (

![Vertical ellipsis icon representing a menu or more options.](images/icons/vertical-ellipsis.png)

) and modifying the **Streaming preference** option. 8. (Optional) In the chat mode of the chat/text playground, you can compare responses from different models by doing the following:

    1. Turn on **Compare mode**.
    2. Choose **Select model** and select a provider, model, and throughput to use.
    3. Choose the configurations icon (

     ![Three horizontal sliders with adjustable circular controls for settings or parameters.](images/icons/configurations.png)

     ) to modify the configurations to use.
    4. To add more models to compare, choose the + icon on the right, select a model, and modify the configurations as necessary.

9. (Optional) If a model supports prompt caching, you can open the **Configurations** panel and turn
   on **Prompt caching** to enabling caching of your input and model responses for reduced cost and latency.
   For more information, see [Prompt caching for faster model inference](prompt-caching.md "prompt-caching.md").
10. To run the prompt, choose **Run**. Amazon Bedrock doesn't store any text, images, or documents that you provide. The data is only used to generate the response.

###### Note

If the response violates the content moderation policy, Amazon Bedrock doesn't
display it. If you have turned on streaming, Amazon Bedrock clears the entire
response if it generates content that violates the policy. For more details,
navigate to the Amazon Bedrock console, select **Providers**, and read the
text under the **Content limitations** section. 11. The model returns the response. If you're using the chat mode of the chat/text playground, you can submit a prompt to reply to the response and generate another response. 12. After generating a response, you have the following options:

    * To export the response as a JSON file, choose the options icon (

     ![Vertical ellipsis icon representing a menu or more options.](images/icons/vertical-ellipsis.png)

     ) and select **Export as JSON**.
    * To view the API request that you made, choose the options icon (

     ![Vertical ellipsis icon representing a menu or more options.](images/icons/vertical-ellipsis.png)

     ) and select **View API request**.
    * In the chat mode of the chat/text playground, you can view metrics in the **Model metrics** section. The following model metrics are available:




    	+ **Latency** — The time it takes between when the request is received by Amazon Bedrock and when the response is returned (for non-streaming responses) or when the response stream is completed (for streaming responses).
    	+ **Input token count** — The number of tokens that
    	 are fed into the model as input during inference.
    	+ **Output token count** — The number of tokens
    	 generated in response to a prompt. Longer, more conversational, responses require more
    	 tokens.
    	+ **Cost** — The cost of processing the input and
    	 generating output tokens.
    To set metric criteria that you want the response to match, choose **Define metric criteria** and define conditions for the model to match. After you apply the criteria, the **Model metrics** section shows how many and which criteria were met by the response.


    If criteria are unmet, you can choose a different model, rewrite the prompt, or modify configurations and rerun the prompt.
