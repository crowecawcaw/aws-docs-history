# Supervised fine-tuning (SFT)

The SFT training process consists of two main stages:

- **Data Preparation**: Follow established guidelines to
  create, clean, or reformat datasets into the required structure. Ensure that inputs,
  outputs, and auxiliary information (such as reasoning traces or metadata) are properly
  aligned and formatted.
- **Training Configuration**: Define how the model will be
  trained. When usingSageMaker AI Hyperpod, this configuration is written in a YAML recipe file that
  includes:
  - Data source paths (training and validation datasets)
  - Key hyperparameters (epochs, learning rate, batch size)
  - Optional components (distributed training parameters, etc)

## Nova Model Comparison and Selection

Amazon Nova 2.0 is a model trained on a larger and more diverse dataset than Amazon Nova 1.0. Key
improvements include:

- **Enhanced reasoning abilities** with explicit
  reasoning mode support
- **Broader multilingual performance** across additional
  languages
- **Improved performance on complex tasks** including
  coding and tool use
- **Extended context handling** with better accuracy and
  stability at longer context lengths

## When to Use Nova 1.0 vs. Nova 2.0

Choose Amazon Nova 2.0 when:

- Superior performance with advanced reasoning capabilities is needed
- Multilingual support or complex task handling is required
- Better results on coding, tool calling, or analytical tasks are needed
