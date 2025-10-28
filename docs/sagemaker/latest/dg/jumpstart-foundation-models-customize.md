# Foundation model

customization

Foundation models are extremely powerful models able to solve a wide array of tasks.
To solve most tasks effectively, these models require some form of customization.

The recommended way to first customize a foundation model to a specific use case is
through prompt engineering. Providing your foundation model with well-engineered,
context-rich prompts can help achieve desired results without any fine-tuning or
changing of model weights. For more information, see [Prompt
engineering for foundation models](jumpstart-foundation-models-customize-prompt-engineering.md "jumpstart-foundation-models-customize-prompt-engineering.md").

If prompt engineering alone is not enough to customize your foundation model to a
specific task, you can fine-tune a foundation model on additional domain-specific data.
For more information, see [Foundation models and
hyperparameters for fine-tuning](jumpstart-foundation-models-fine-tuning.md "jumpstart-foundation-models-fine-tuning.md"). The fine-tuning process
involves changing model weights.

If you want to customize your model with information from a knowledge library without
any retraining, see [Retrieval Augmented
Generation](jumpstart-foundation-models-customize-rag.md "jumpstart-foundation-models-customize-rag.md").
