# Use Jupyter AI in JupyterLab or Studio Classic

You can use Jupyter AI in JupyterLab or Studio Classic by invoking language models from either the
chat UI or from notebook cells. The following sections give information about the steps needed
to complete this.

## Use language models from the chat

UI

Compose your message in the chat UI text box to start interacting with your model. To
clear the message history, use the `/clear` command.

###### Note

Clearing the message history does not erase the chat context with the model
provider.

## Use language models from notebook

cells

Before using the `%%ai` and `%ai` commands to invoke a language
model, load the IPython extension by running the following command in a JupyterLab or
Studio Classic notebook cell.

```
%load_ext jupyter_ai_magics
```

- **For models hosted by AWS:**
  - To invoke a model deployed in SageMaker AI, pass the string
    `sagemaker-endpoint:`endpoint-name``to the`%%ai` magic command with the required parameters below, then add your
    prompt in the following lines.

  The following table lists the required and optional parameters when invoking
  models hosted by SageMaker AI or Amazon Bedrock.

  | **Parameter Name**        | **Parameter**        | **Short Version** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | ------------------------- | -------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ----- | ---- | -------- | ---- | --- | ------------------------------------------------------------------------- |
  | Request schema            | `--request-schema`   | `-q`              | **Required**: The JSON object the endpoint<br>expects, with the prompt being substituted into any value that matches the<br>string literal `<prompt>`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | Region name               | `--region-name`      | `-n`              | **Required**: The AWS Region where the model<br>is deployed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | Response path             | `--response-path`    | `-p`              | **Required**: A JSONPath string used to extract<br>the language model's output from the JSON response of the endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | Extra model<br>parameters | `--model-parameters` | `-m`              | **Optional**: A JSON value specifying<br>additional parameters to be passed to the model. The accepted value is<br>parsed into a dictionary, unpacked, and directly passed to the provider<br>class. This is useful when the endpoint or the model requires custom<br>parameters. For example, in Llama 2 models when accepting the End User<br>License Agreement (EULA) is necessary, you can pass the EULA acceptance to<br>the endpoint using `-m<br>{"endpoint_kwargs":{"CustomAttributes":"accept_eula=true"}}`.<br>Alternatively, you can use the `-m` parameter to pass extra model<br>parameters, such as setting the maximum number of tokens for a model's<br>generated response. For example, when working with an AI21 Labs Jurassic<br>model: `-m {"model_kwargs":{"maxTokens":256}}`. |
  | Output<br>format          | `--format`           | `-f`              | **Optional**: The IPython display used to<br>render the output. It can be any of the following values<br>`[code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | html | image | json | markdown | math | md  | text]`, provided that<br>the invoked model supports the specified format. |

  The following command invokes a [Llama2-7b](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html "https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html") model hosted by SageMaker AI.

  ```
  %%ai sagemaker-endpoint:jumpstart-dft-meta-textgeneration-llama-2-7b -q {"inputs":"<prompt>","parameters":{"max_new_tokens":64,"top_p":0.9,"temperature":0.6,"return_full_text":false}} -n us-east-2 -p [0].generation -m {"endpoint_kwargs":{"CustomAttributes":"accept_eula=true"}} -f text
  Translate English to French:
  sea otter => loutre de mer
  peppermint => menthe poivrée
  plush girafe => girafe peluche
  cheese =>
  ```

  The following example invokes a Flan-t5-small model hosted by SageMaker AI.

  ```
  %%ai sagemaker-endpoint:hf-text2text-flan-t5-small --request-schema={"inputs":"<prompt>","parameters":{"num_return_sequences":4}} --region-name=us-west-2 --response-path=[0]["generated_text"] -f text
  What is the atomic number of Hydrogen?
  ```

  - To invoke a model deployed in Amazon Bedrock, pass the string
    `bedrock:`model-name``to the`%%ai` magic command with any optional parameter defined in the list of
    [parameters for
    invoking models hosted by JumpStart or Amazon Bedrock](#sagemaker-jupyterai-jumpstart-inference-params "#sagemaker-jupyterai-jumpstart-inference-params"), then add your prompt
    in the following lines.

  The following example invokes an [AI21 Labs
  Jurassic-2 model](../../../bedrock/latest/userguide/model-parameters-jurassic2.md "../../../bedrock/latest/userguide/model-parameters-jurassic2.md") hosted by Amazon Bedrock.

  ```
  %%ai bedrock:ai21.j2-mid-v1 -m {"model_kwargs":{"maxTokens":256}} -f code
  Write a function in python implementing a bubbble sort.
  ```

- **For models hosted by third-party providers**

To invoke a model hosted by third-party providers, pass the string
``provider-id`:`model-name``
to the `%%ai` magic command with an optional [Output format](#sagemaker-jupyterai-output-format-params "#sagemaker-jupyterai-output-format-params"),
then add your prompt in the following lines. You can find the details of each provider,
including their ID, in the Jupyter AI [list of model providers](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#model-providers "https://jupyter-ai.readthedocs.io/en/latest/users/index.html#model-providers").

The following command asks an Anthropic Claude model to output an HTML file
containing the image of a white square with black borders.

```
%%ai anthropic:claude-v1.2 -f html
Create a square using SVG with a black border and white fill.
```
