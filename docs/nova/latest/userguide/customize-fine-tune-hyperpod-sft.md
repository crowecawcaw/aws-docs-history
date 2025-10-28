# Supervised fine-tuning (Full FT, PEFT)

Supervised fine-tuning (SFT) is the process of providing a collection of
prompt-response pairs to a foundation model to improve the performance of a pre-trained
foundation model on a specific task. The labeled examples are formatted as
prompt-response pairs and phrased as instructions. This fine-tuning process modifies the
weights of the model.

You should use SFT when you have domain-specific data that requires providing specific
prompt-response pairs for optimal results. Both full-rank
SFT and parameter-efficient SFT are available.

For detailed instructions about using SFT with Amazon Nova model customization, see the [Supervised Fine-Tuning (Full FT, PEFT)](../../../sagemaker/latest/dg/nova-fine-tune.md "../../../sagemaker/latest/dg/nova-fine-tune.md") section from SageMakeruser guide.
