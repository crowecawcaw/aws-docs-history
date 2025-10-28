# Support for

FlashAttention

Support for FlashAttention is a feature of the library only applicable for the
_distributed transformer_ model, which is a Transformer model
wrapped by [`smp.DistributedModel()`](https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed-modelparallel-torch-distributedmodel "https://sagemaker.readthedocs.io/en/v2.199.0/api/training/smp_versions/latest/smd_model_parallel_pytorch.html#smdistributed-modelparallel-torch-distributedmodel") for model-parallel training. This
feature is also compatible with [Tensor
Parallelism](model-parallel-extended-features-pytorch-tensor-parallelism.md "model-parallel-extended-features-pytorch-tensor-parallelism.md").

The [FlashAttention](https://github.com/HazyResearch/flash-attention "https://github.com/HazyResearch/flash-attention") library only supports models when
`attention_head_size` is set to a value that's a multiple of 8 and less
than 128. Therefore, when you train a distributed transformer and make sure that
FlashAttention works properly, you should adjust parameters to make the attention head
size comply the requirements. For more information, see also [Installation and features](https://github.com/HazyResearch/flash-attention#installation-and-features "https://github.com/HazyResearch/flash-attention#installation-and-features") in the _FlashAttention GitHub
repository_.

For
example,
assume that you configure a Transformer model with `hidden_width=864` and
`num_heads=48`. The head size of FlashAttention is calculated as
`attention_head_size = hidden_width / num_heads = 864 / 48 = 18`. To
enable FlashAttention, you need to adjust the `num_heads` parameter to
`54`, so that `attention_head_size = hidden_width / num_heads = 864
 / 54 = 16`, which is a multiple of 8.
