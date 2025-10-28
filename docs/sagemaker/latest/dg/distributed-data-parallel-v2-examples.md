# Amazon SageMaker AI data parallelism library

examples

This page provides Jupyter notebooks that present examples of implementing the SageMaker AI
distributed data parallelism (SMDDP) library to run distributed training jobs on
SageMaker AI.

## Blogs and Case Studies

The following blogs discuss case studies about using the SMDDP library.

**SMDDP v2 blogs**

- [Enable faster training with Amazon SageMaker AI data parallel library](https://aws.amazon.com/blogs/machine-learning/enable-faster-training-with-amazon-sagemaker-data-parallel-library/ "https://aws.amazon.com/blogs/machine-learning/enable-faster-training-with-amazon-sagemaker-data-parallel-library/"),
  _AWS Machine Learning Blog_ (December 05,

2023.

**SMDDP v1 blogs**

- [How I trained 10TB for Stable Diffusion on SageMaker AI](https://medium.com/@emilywebber/how-i-trained-10tb-for-stable-diffusion-on-sagemaker-39dcea49ce32 "https://medium.com/@emilywebber/how-i-trained-10tb-for-stable-diffusion-on-sagemaker-39dcea49ce32") in _Medium_ (November 29, 2022)
- [Run PyTorch Lightning and native PyTorch DDP on Amazon SageMaker Training,
  featuring Amazon Search](https://aws.amazon.com/blogs/machine-learning/run-pytorch-lightning-and-native-pytorch-ddp-on-amazon-sagemaker-training-featuring-amazon-search/ "https://aws.amazon.com/blogs/machine-learning/run-pytorch-lightning-and-native-pytorch-ddp-on-amazon-sagemaker-training-featuring-amazon-search/") , _AWS Machine
  Learning Blog_ (August 18, 2022)
- [Training YOLOv5 on AWS with PyTorch and the SageMaker AI distributed data
  parallel library](https://medium.com/@sitecao/training-yolov5-on-aws-with-pytorch-and-sagemaker-distributed-data-parallel-library-a196ab01409b "https://medium.com/@sitecao/training-yolov5-on-aws-with-pytorch-and-sagemaker-distributed-data-parallel-library-a196ab01409b"), _Medium_ (May 6,

2022.

- [Speed up EfficientNet model training on SageMaker AI with PyTorch and the
  SageMaker AI distributed data parallel library](https://medium.com/@dangmz/speed-up-efficientnet-model-training-on-amazon-sagemaker-with-pytorch-and-sagemaker-distributed-dae4b048c01a "https://medium.com/@dangmz/speed-up-efficientnet-model-training-on-amazon-sagemaker-with-pytorch-and-sagemaker-distributed-dae4b048c01a"), _Medium_ (March 21, 2022)
- [Speed up EfficientNet training on AWS with the SageMaker AI distributed data
  parallel library](https://towardsdatascience.com/speed-up-efficientnet-training-on-aws-by-up-to-30-with-sagemaker-distributed-data-parallel-library-2dbf6d1e18e8 "https://towardsdatascience.com/speed-up-efficientnet-training-on-aws-by-up-to-30-with-sagemaker-distributed-data-parallel-library-2dbf6d1e18e8"), _Towards Data
  Science_ (January 12, 2022)
- [Hyundai reduces ML model training time for autonomous driving models using
  Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/hyundai-reduces-training-time-for-autonomous-driving-models-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/hyundai-reduces-training-time-for-autonomous-driving-models-using-amazon-sagemaker/"), _AWS Machine Learning
  Blog_ (June 25, 2021)
- [Distributed Training: Train BART/T5 for Summarization using Transformers
  and Amazon SageMaker AI](https://huggingface.co/blog/sagemaker-distributed-training-seq2seq "https://huggingface.co/blog/sagemaker-distributed-training-seq2seq"), the _Hugging Face
  website_ (April 8, 2021)

## Example

notebooks

Example notebooks are provided in the [SageMaker AI examples GitHub repository](https://github.com/aws/amazon-sagemaker-examples/tree/master/training/distributed_training/ "https://github.com/aws/amazon-sagemaker-examples/tree/master/training/distributed_training/"). To download the examples, run the
following command to clone the repository and go to
`training/distributed_training/pytorch/data_parallel`.

###### Note

Clone and run the example notebooks in the following SageMaker AI ML IDEs.

- [SageMaker AI JupyterLab](studio-updated-jl.md "studio-updated-jl.md") (available in [Studio](studio-updated.md "studio-updated.md") created after December 2023)
- [SageMaker AI Code Editor](code-editor.md "code-editor.md") (available in [Studio](studio-updated.md "studio-updated.md") created after December 2023)
- [Studio Classic](studio.md "studio.md") (available as an application in [Studio](studio-updated.md "studio-updated.md") created after December 2023)
- [SageMaker Notebook Instances](nbi.md "nbi.md")

```
git clone https://github.com/aws/amazon-sagemaker-examples.git
cd amazon-sagemaker-examples/training/distributed_training/pytorch/data_parallel
```

**SMDDP v2 examples**

- [Train Llama 2 using the SageMaker AI distributed data parallel library (SMDDP)
  and DeepSpeed](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/data_parallel/deepspeed/llama2/smddp_deepspeed_example.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/data_parallel/deepspeed/llama2/smddp_deepspeed_example.ipynb")
- [Train Falcon using the SageMaker AI distributed data parallel library (SMDDP)
  and PyTorch Fully Sharded Data Parallelism (FSDP)](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/data_parallel/fully_sharded_data_parallel/falcon/smddp_fsdp_example.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/data_parallel/fully_sharded_data_parallel/falcon/smddp_fsdp_example.ipynb")

**SMDDP v1 examples**

- [CNN with PyTorch and the SageMaker AI data parallelism library](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/data_parallel/mnist/pytorch_smdataparallel_mnist_demo.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/data_parallel/mnist/pytorch_smdataparallel_mnist_demo.ipynb")
- [BERT with PyTorch and the SageMaker AI data parallelism library](https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/data_parallel/bert/pytorch_smdataparallel_bert_demo.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/training/distributed_training/pytorch/data_parallel/bert/pytorch_smdataparallel_bert_demo.ipynb")
- [CNN with TensorFlow 2.3.1 and the SageMaker AI data parallelism
  library](https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/tensorflow/data_parallel/mnist/tensorflow2_smdataparallel_mnist_demo.html "https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/tensorflow/data_parallel/mnist/tensorflow2_smdataparallel_mnist_demo.html")
- [BERT with TensorFlow 2.3.1 and the SageMaker AI data parallelism
  library](https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/tensorflow/data_parallel/bert/tensorflow2_smdataparallel_bert_demo.html "https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/tensorflow/data_parallel/bert/tensorflow2_smdataparallel_bert_demo.html")
- [HuggingFace Distributed Data Parallel Training in PyTorch on SageMaker AI -
  Distributed Question Answering](https://github.com/huggingface/notebooks/blob/master/sagemaker/03_distributed_training_data_parallelism/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/master/sagemaker/03_distributed_training_data_parallelism/sagemaker-notebook.ipynb")
- [HuggingFace Distributed Data Parallel Training in PyTorch on SageMaker AI -
  Distributed Text Summarization](https://github.com/huggingface/notebooks/blob/master/sagemaker/08_distributed_summarization_bart_t5/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/master/sagemaker/08_distributed_summarization_bart_t5/sagemaker-notebook.ipynb")
- [HuggingFace Distributed Data Parallel Training in TensorFlow on
  SageMaker AI](https://github.com/huggingface/notebooks/blob/master/sagemaker/07_tensorflow_distributed_training_data_parallelism/sagemaker-notebook.ipynb "https://github.com/huggingface/notebooks/blob/master/sagemaker/07_tensorflow_distributed_training_data_parallelism/sagemaker-notebook.ipynb")
