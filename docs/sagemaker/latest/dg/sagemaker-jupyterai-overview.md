# Access Jupyter AI Features

You can access Jupyter AI capabilities through two distinct methods: using the chat UI or
using magic commands within notebooks.

## From the chat user interface AI

assistant

The chat interface connects you with Jupyternaut, a conversational agent that uses the
language model of your choice.

After launching a JupyterLab application installed with Jupyter AI, you can access the
chat interface by choosing the chat icon (
![Icon of a rectangular shape with a curved arrow pointing to the upper right corner.](images/studio/icons/jupyterai/jupyterai-chat-ui.png)
) in the left navigation panel. First-time users are prompted to
configure their model. See [Configure your model
provider in the chat UI](sagemaker-jupyterai-model-configuration.md#sagemaker-jupyterai-model-configuration-chatui "sagemaker-jupyterai-model-configuration.md#sagemaker-jupyterai-model-configuration-chatui") for configuration
instructions.

###### Using the chat UI, you can:

- **Answer questions**: For instance, you can ask
  Jupyternaut to create a Python function that adds CSV files to an Amazon S3 bucket.
  Subsequently, you can refine your answer with a follow-up question, such as adding a
  parameter to the function to choose the path where the files are written.
- **Interact with files in JupyterLab**: You can
  include a portion of your notebook in your prompt by selecting it. Then, you can either
  replace it with the model's suggested answer or manually copy the answer to your
  clipboard.
- **Generate entire notebooks** from prompts: By
  starting your prompt with `/generate`, you trigger a notebook generation
  process in the background without interrupting your use of Jupyternaut. A message
  containing the link to the new file is displayed upon completion of the process.
- **Learn from
  and ask questions about local files**: Using the `/learn` command,
  you can teach an embedding model of your choice about local files and then ask questions
  about those files using the `/ask` command. Jupyter AI stores the embedded
  content in a local [FAISS vector
  database](https://github.com/facebookresearch/faiss "https://github.com/facebookresearch/faiss"), then uses retrieval-augmented generation (RAG) to provide answers
  based on what it has learned. To erase all previously learned information from your
  embedding model, use `/learn -d`.

###### Note

Amazon Q developer doesn't have the capability to generate notebooks from
scratch.

For a complete list of features and detailed instructions on their usage, see the [Jupyter AI chat interface](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#the-chat-interface "https://jupyter-ai.readthedocs.io/en/latest/users/index.html#the-chat-interface") documentation. To learn about how to configure access
to a model in Jupyternaut, see [Configure your model
provider in the chat UI](sagemaker-jupyterai-model-configuration.md#sagemaker-jupyterai-model-configuration-chatui "sagemaker-jupyterai-model-configuration.md#sagemaker-jupyterai-model-configuration-chatui").

## From notebook cells

Using `%%ai` and `%ai` magic commands, you can interact with the
language model of your choice from your notebook cells or any IPython command line
interface. The `%%ai` command applies your instructions to the entire cell,
whereas `%ai` apply them to the specific line.

The following example illustrates an `%%ai` magic command invoking an
Anthropic Claude model to output an HTML file containing the image of a white square with
black borders.

```
%%ai anthropic:claude-v1.2 -f html
Create a square using SVG with a black border and white fill.
```

To learn about the syntax of each command, use `%ai help`. To list the
providers and models supported by the extension, run `%ai list`.

For a complete list of features and detailed instructions on their usage, see the Jupyter
AI [magic commands](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#the-ai-and-ai-magic-commands "https://jupyter-ai.readthedocs.io/en/latest/users/index.html#the-ai-and-ai-magic-commands") documentation. In particular, you can customize the output format
of your model using the `-f` or `--format` parameter, allow variable
interpolation in prompts, including special `In` and `Out` variables,
and more.

To learn about how to configure the access to a model, see [Configure your
model provider in a notebook](sagemaker-jupyterai-model-configuration.md#sagemaker-jupyterai-model-configuration-magic-commands "sagemaker-jupyterai-model-configuration.md#sagemaker-jupyterai-model-configuration-magic-commands").
