

# Use Jupyter AI in JupyterLab or Studio Classic
<a name="sagemaker-jupyterai-use"></a>

You can use Jupyter AI in JupyterLab or Studio Classic by invoking language models from either the chat UI or from notebook cells. The following sections give information about the steps needed to complete this.

## Use language models from the chat UI
<a name="sagemaker-jupyterai-use-chatui"></a>

Compose your message in the chat UI text box to start interacting with your model. To clear the message history, use the `/clear` command.

**Note**  
Clearing the message history does not erase the chat context with the model provider.

## Use language models from notebook cells
<a name="sagemaker-jupyterai-use-magic-commands"></a>

Before using the `%%ai` and `%ai` commands to invoke a language model, load the IPython extension by running the following command in a JupyterLab or Studio Classic notebook cell.

```
%load_ext jupyter_ai_magics
```
+ **For models hosted by AWS:**
  + To invoke a model deployed in SageMaker AI, pass the string `sagemaker-endpoint:{{endpoint-name}}` to the `%%ai` magic command with the required parameters below, then add your prompt in the following lines.

    The following table lists the required and optional parameters when invoking models hosted by SageMaker AI or Amazon Bedrock.<a name="sagemaker-jupyterai-jumpstart-inference-params"></a>    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-jupyterai-use.html)

    The following command invokes a [Llama2-7b](https://sagemaker.readthedocs.io/en/stable/doc_utils/pretrainedmodels.html) model hosted by SageMaker AI.

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
  + To invoke a model deployed in Amazon Bedrock, pass the string `bedrock:{{model-name}}` to the `%%ai` magic command with any optional parameter defined in the list of [parameters for invoking models hosted by JumpStart or Amazon Bedrock](#sagemaker-jupyterai-jumpstart-inference-params), then add your prompt in the following lines.

    The following example invokes an [AI21 Labs Jurassic-2 model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-jurassic2.html) hosted by Amazon Bedrock.

    ```
    %%ai bedrock:ai21.j2-mid-v1 -m {"model_kwargs":{"maxTokens":256}} -f code
    Write a function in python implementing a bubbble sort.
    ```
+ **For models hosted by third-party providers**

  To invoke a model hosted by third-party providers, pass the string `{{provider-id}}:{{model-name}}` to the `%%ai` magic command with an optional [`Output format`](#sagemaker-jupyterai-output-format-params), then add your prompt in the following lines. You can find the details of each provider, including their ID, in the Jupyter AI [list of model providers](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#model-providers).

  The following command asks an Anthropic Claude model to output an HTML file containing the image of a white square with black borders.

  ```
  %%ai anthropic:claude-v1.2 -f html
  Create a square using SVG with a black border and white fill.
  ```