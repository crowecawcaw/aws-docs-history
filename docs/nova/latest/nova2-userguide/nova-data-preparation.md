# Data preparation

This section provides data preparation guides for each training technique and model version.

###### Topics

- [Validation tools](#nova-data-validation-tools "#nova-data-validation-tools")
- [Preparing data for SFT on Amazon Nova 2](nova-data-prep-sft-2.md "nova-data-prep-sft-2.md")
- [Preparing data for RFT on Amazon Nova 2](nova-data-prep-rft-2.md "nova-data-prep-rft-2.md")
- [Preparing data for CPT on Amazon Nova 2](nova-data-prep-cpt-2.md "nova-data-prep-cpt-2.md")

## Validation tools

Before submitting a fine-tuning job, we recommend validating your dataset to catch formatting issues early. You have two options:

- **Dataset validation script** – A standalone Python script hosted on GitHub. See the [dataset validation script](https://github.com/aws-samples/amazon-nova-samples/tree/main/customization/bedrock-finetuning/understanding/dataset_validation "https://github.com/aws-samples/amazon-nova-samples/tree/main/customization/bedrock-finetuning/understanding/dataset_validation").
- **Amazon Nova Forge SDK** – Validation support is built into the SDK. See [Data preparation](https://github.com/aws/nova-forge-sdk#data-preparation "https://github.com/aws/nova-forge-sdk#data-preparation") in the Amazon Nova Forge SDK README.
