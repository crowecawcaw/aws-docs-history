# Model evaluation notebook

tutorials

This section provides the following notebook tutorials, which include example code and
explanations:

- How to evaluate a JumpStart model for prompt stereotyping.
- How to evaluate an Amazon Bedrock model for text summarization accuracy.

###### Topics

- [Evaluate a JumpStart model for prompt stereotyping](clarify-foundation-model-evaluate-auto-tutorial-one.md "clarify-foundation-model-evaluate-auto-tutorial-one.md")
- [Evaluate an Amazon Bedrock model for text summarization accuracy](clarify-foundation-model-evaluate-auto-tutorial-two.md "clarify-foundation-model-evaluate-auto-tutorial-two.md")
- [Additional
  notebooks](#clarify-foundation-model-evaluate-auto-tutorial-ex "#clarify-foundation-model-evaluate-auto-tutorial-ex")

## Additional

notebooks

The [fmeval
GitHub](https://github.com/aws/fmeval/tree/main/examples "https://github.com/aws/fmeval/tree/main/examples") directory contains the following additional example
notebooks:

- [bedrock-claude-factual-knowledge.ipnyb](https://github.com/aws/fmeval/blob/main/examples/bedrock-claude-factual-knowledge.ipynb "https://github.com/aws/fmeval/blob/main/examples/bedrock-claude-factual-knowledge.ipynb") – Evaluates an
  [Anthropic Claude
  2](https://www.anthropic.com/index/claude-2 "https://www.anthropic.com/index/claude-2") model hosted on Amazon Bedrock for factual knowledge.
- [byo-model-outputs.ipynb](https://github.com/aws/fmeval/blob/main/examples/byo-model-outputs.ipynb "https://github.com/aws/fmeval/blob/main/examples/byo-model-outputs.ipynb") – Evaluates a [Falcon 7b model](https://huggingface.co/tiiuae/falcon-7b "https://huggingface.co/tiiuae/falcon-7b")
  hosted on JumpStart for factual knowledge where you bring your own model
  outputs instead of sending inference requests to your model.
- [custom_model_runner_chat_gpt.ipnyb](https://github.com/aws/fmeval/blob/main/examples/custom_model_runner_chat_gpt.ipynb "https://github.com/aws/fmeval/blob/main/examples/custom_model_runner_chat_gpt.ipynb") – Evaluates a custom
  `ChatGPT 3.5` model hosted on `Hugging Face` for
  factual knowledge.
