

# Amazon SageMaker AI model parallelism library v2 examples
<a name="distributed-model-parallel-v2-examples"></a>

This page provides a list of blogs and Jupyter notebooks that present practical examples of implementing the SageMaker model parallelism (SMP) library v2 to run distributed training jobs on SageMaker AI.

## Blogs and Case Studies
<a name="distributed-model-parallel-v2-examples-blog"></a>

The following blogs discuss case studies about using SMP v2.
+ [Amazon SageMaker AI model parallel library now accelerates PyTorch FSDP workloads by up to 20%](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-model-parallel-library-now-accelerates-pytorch-fsdp-workloads-by-up-to-20/)

## PyTorch example notebooks
<a name="distributed-model-parallel-examples-v2-pytorch"></a>

Example notebooks are provided in the [SageMaker AI examples GitHub repository](https://github.com/aws/amazon-sagemaker-examples/tree/master/training/distributed_training/). To download the examples, run the following command to clone the repository and go to `training/distributed_training/pytorch/model_parallel_v2`.

**Note**  
Clone and run the example notebooks in the following SageMaker AI ML IDEs.  
[SageMaker JupyterLab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl.html) (available in [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) created after December 2023)
[SageMaker Code Editor](https://docs.aws.amazon.com/sagemaker/latest/dg/code-editor.html) (available in [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) created after December 2023)
[Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html) (available as an application in [Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html) created after December 2023)
[SageMaker Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)

```
git clone https://github.com/aws/amazon-sagemaker-examples.git
cd amazon-sagemaker-examples/training/distributed_training/pytorch/model_parallel_v2
```

**SMP v2 example notebooks**
+ [Accelerate training of Llama v2 with SMP v2, PyTorch FSDP, and Transformer Engine by running FP8 training on P5 instances](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel_v2/llama_v2/smp-train-llama-fsdp-tp-fp8.ipynb)
+ [Fine-tune Llama v2 with SMP v2 and PyTorch FSDP at large-scale using tensor parallelism, hybrid sharding, and activation offloading](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel_v2/llama_v2/smp-finetuning-llama-fsdp-tp.ipynb)
+ [Train GPT-NeoX with SMP v2 and PyTorch FSDP at large scale](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel_v2/gpt-neox/smp-train-gpt-neox-fsdp-tp.ipynb)
+ [Fine-tune GPT-NeoX with SMP v2 and PyTorch FSDP at large-scale using tensor parallelism, hybrid sharding, and activation offloading](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/model_parallel_v2/gpt-neox/smp-finetuning-gpt-neox-fsdp-tp.ipynb)