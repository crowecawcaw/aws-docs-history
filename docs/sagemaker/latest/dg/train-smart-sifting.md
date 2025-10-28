# Data refining during training with

Amazon SageMaker smart sifting

SageMaker smart sifting is a capability of SageMaker Training that helps improve the efficiency of your
training datasets and reduce total training time and cost.

Modern deep learning models such as large language models (LLMs) or vision transformer
models often require massive datasets to achieve acceptable accuracy. For example, LLMs
often require trillions of tokens or petabytes of data to converge. The growing size of
training datasets, along with the size of state-of-the-art models, can increase the compute
time and cost of model training.

Invariably, samples in a dataset do not contribute equally to the learning process during
model training. A significant proportion of computational resources provisioned during
training might be spent on processing easy samples that do not contribute substantially to
the overall accuracy of a model. Ideally, training datasets would only include samples that
are actually improving the model convergence. Filtering out less helpful data can reduce
training time and compute cost. However, identifying less helpful data can be challenging
and risky. It is practically difficult to identify which samples are less informative before
training, and model accuracy can be impacted if the wrong samples or too many samples are
excluded.

Smart sifting of data with Amazon SageMaker AI can help reduce training time and cost by improving
data efficiency. The SageMaker smart sifting algorithm evaluates the loss value of each data during the
data loading stage of a training job and excludes samples which are less informative to the
model. By using refined data for training, the total time and cost of training your model is
reduced by eliminating unnecessary forward and backward passes on non-improving data.
Therefore, there is minimal or no impact on the accuracy of the model.

SageMaker smart sifting is available through SageMaker Training Deep Learning Containers (DLCs) and
supports PyTorch workloads via the PyTorch `DataLoader`. Just a few lines of code
change are needed to implement SageMaker smart sifting and you do not need to change your existing
training or data processing workflows.

###### Topics

- [How SageMaker smart sifting works](train-smart-sifting-how-it-works.md "train-smart-sifting-how-it-works.md")
- [Supported frameworks and AWS
  Regions](train-smart-sifting-what-is-supported.md "train-smart-sifting-what-is-supported.md")
- [SageMaker smart sifting within your training
  script](train-smart-sifting-apply-to-script.md "train-smart-sifting-apply-to-script.md")
- [Troubleshooting](train-smart-sifting-best-prac-considerations-troubleshoot.md "train-smart-sifting-best-prac-considerations-troubleshoot.md")
- [Security in SageMaker smart sifting](train-smart-sifting-security.md "train-smart-sifting-security.md")
- [SageMaker smart sifting Python SDK
  reference](train-smart-sifting-pysdk-reference.md "train-smart-sifting-pysdk-reference.md")
- [SageMaker smart sifting release notes](train-smart-sifting-release-notes.md "train-smart-sifting-release-notes.md")
