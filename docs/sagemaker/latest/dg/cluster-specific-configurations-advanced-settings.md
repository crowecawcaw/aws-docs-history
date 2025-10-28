# Advanced

settings

The SageMaker HyperPod recipe adapter is built on top of the Nvidia Nemo and
Pytorch-lightning frameworks. If you've already used these frameworks, integrating your
custom models or features into the SageMaker HyperPod recipe adapter is a similar process. In
addition to modifying the recipe adapter, you can change your own pre-training or
fine-tuning script. For guidance on writing your custom training script, see [examples](https://github.com/aws/sagemaker-hyperpod-training-adapter-for-nemo/tree/main/examples "https://github.com/aws/sagemaker-hyperpod-training-adapter-for-nemo/tree/main/examples").

## Use the SageMaker HyperPod adapter to create your own model

Within the recipe adapter, you can customize the following files in the following
locations:

1. `collections/data`: Contains a module responsible for loading
   datasets. Currently, it only supports datasets from HuggingFace. If you have
   more advanced requirements, the code structure allows you to add custom data
   modules within the same folder.
2. `collections/model`: Includes the definitions of various
   language models. Currently, it supports common large language models like
   Llama, Mixtral, and Mistral. You have the flexibility to introduce your own
   model definitions within this folder.
3. `collections/parts`: This folder contains strategies for
   training models in a distributed manner. One example is the Fully Sharded
   Data Parallel (FSDP) strategy, which allows for sharding a large language
   model across multiple accelerators. Additionally, the strategies support
   various forms of model parallelism. You also have the option to introduce
   your own customized training strategies for model training.
4. `utils`: Contains various utilities aimed at facilitating the
   management of a training job. It serves as a repository where for your own
   tools. You can use your own tools for tasks such as troubleshooting or
   benchmarking. You can also add your own personalized PyTorch Lightning
   callbacks within this folder. You can use PyTorch Lightning callbacks to
   seamlessly integrate specific functionalities or operations into the
   training lifecycle.
5. `conf`: Contains the configuration schema definitions used for
   validating specific parameters in a training job. If you introduce new
   parameters or configurations, you can add your customized schema to this
   folder. You can use the customized schema to define the validation rules.
   You can validate data types, ranges, or any other parameter constraint. You
   can also define you own custom schema to validate the parameters.
