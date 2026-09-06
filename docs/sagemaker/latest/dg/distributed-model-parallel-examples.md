

# Amazon SageMaker AI model parallelism library v1 examples
<a name="distributed-model-parallel-examples"></a>

This page provides a list of blogs and Jupyter notebooks that present practical examples of implementing the SageMaker model parallelism (SMP) library v1 to run distributed training jobs on SageMaker AI.

## Blogs and Case Studies
<a name="distributed-model-parallel-examples-blog"></a>

The following blogs discuss case studies about using SMP v1.
+ [New performance improvements in the Amazon SageMaker AI model parallelism library](https://aws.amazon.com/blogs/machine-learning/new-performance-improvements-in-amazon-sagemaker-model-parallel-library/), *AWS Machine Learning Blog* (December 16, 2022)
+ [Train gigantic models with near-linear scaling using sharded data parallelism on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/train-gigantic-models-with-near-linear-scaling-using-sharded-data-parallelism-on-amazon-sagemaker/), *AWS Machine Learning Blog* (October 31, 2022)

## Example notebooks
<a name="distributed-model-parallel-examples-pytorch"></a>

Example notebooks are provided in the [SageMaker AI examples GitHub repository](https://github.com/aws/amazon-sagemaker-examples/tree/master/training/distributed_training/). To download the examples, run the following command to clone the repository and go to `training/distributed_training/pytorch/model_parallel`.

**Note**  
Clone and run the example notebooks in the following SageMaker AI ML IDEs.  
[SageMaker JupyterLab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl.html) (available in [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) created after December 2023)
[SageMaker Code Editor](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html) (available in [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) created after December 2023)
[Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html) (available as an application in [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) created after December 2023)
[SageMaker Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)

```
git clone https://github.com/aws/amazon-sagemaker-examples.git
cd amazon-sagemaker-examples/training/distributed_training/pytorch/model_parallel
```

**SMP v1 example notebooks for PyTorch**
+ [Train GPT-2 with near-linear scaling using the sharded data parallelism technique in the SageMaker model parallelism library](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel/gpt2/smp-train-gpt-sharded-data-parallel.ipynb)
+ [Fine-tune GPT-2 with near-linear scaling using sharded data parallelism technique in the SageMaker model parallelism library](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel/gpt2/smp-fine-tune-gpt-sharded-data-parallel.ipynb)
+ [Train GPT-NeoX-20B with near-linear scaling using the sharded data parallelism technique in the SageMaker model parallelism library](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel/gpt-neox/smp-train-gpt-neox-sharded-data-parallel.ipynb)
+ [Train GPT-J 6B using the sharded data parallelism and tensor parallelism techniques in the SageMaker model parallelism library](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel/gpt-j/smp-train-gptj-sharded-data-parallel-tp.ipynb)
+ [Train FLAN-T5 with near-linear scaling using sharded data parallelism technique in the SageMaker model parallelism library](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel/flan-t5/smp-train-t5-sharded-data-parallel.ipynb)
+ [Train Falcon with near-linear scaling using sharded data parallelism technique in the SageMaker model parallelism library](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel/falcon/smp-train-falcon-sharded-data-parallel.ipynb)

**SMP v1 example notebooks for TensorFlow**
+ [CNN with TensorFlow 2.3.1 and the SageMaker model parallelism library](https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/tensorflow/model_parallel/mnist/tensorflow_smmodelparallel_mnist.html)
+ [HuggingFace with TensorFlow Distributed model parallelism library Training on SageMaker AI](https://github.com/huggingface/notebooks/blob/master/sagemaker/04_distributed_training_model_parallelism/sagemaker-notebook.ipynb)