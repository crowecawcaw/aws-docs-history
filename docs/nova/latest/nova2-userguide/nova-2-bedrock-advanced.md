# Amazon Nova 2.0 advanced fine-tuning capabilities

Amazon Nova 2.0 introduces enhanced fine-tuning capabilities on Amazon Bedrock, including supervised fine-tuning with reasoning content and reinforcement fine-tuning with reward-based optimization.

## Supervised fine-tuning on Amazon Nova 2.0

Amazon Nova 2.0 supervised fine-tuning uses the same Converse API format as Amazon Nova 1.0 with optional reasoning content fields, allowing you to train models that show their thinking process before generating final answers.

**Key features**

- Support for text, image and video inputs in user content blocks
- Optional reasoning content in assistant responses to capture intermediate thinking steps
- Homogeneous dataset requirements (choose text-only, text+image, or text+video)
- Support for PNG, JPEG and GIF images
- Support for MOV, MKV and MP4 videos
- Configurable reasoning modes for training optimization

For detailed information about data preparation, format specifications and reasoning modes, see [Supervised fine-tuning on Amazon Nova 2.0](../../../bedrock/latest/userguide/nova-2-sft-data-prep.md "../../../bedrock/latest/userguide/nova-2-sft-data-prep.md") in the Amazon Bedrock user guide.

## Reinforcement fine-tuning (RFT)

Reinforcement fine-tuning optimizes Amazon Nova models using measurable feedback signals rather than exact correct answers. This approach excels when you can reliably measure response quality but defining exact correct outputs is challenging.

**Key features**

- Reward-based optimization using custom reward functions
- Support for subjective or multifaceted quality assessment
- Ideal for mathematical problem-solving and code generation
- Effective for scientific reasoning and structured data analysis
- Programmatic success verification through execution results
- OpenAI Reinforcement Fine-Tuning format with messages and reference answers
- Evaluation-first approach to validate reward functions before scaling

For detailed information about RFT data format, dataset recommendations and training characteristics, see [Reinforcement fine-tuning (RFT) for Amazon Nova models](../../../bedrock/latest/userguide/nova-rft.md "../../../bedrock/latest/userguide/nova-rft.md") in the Amazon Bedrock user guide.
