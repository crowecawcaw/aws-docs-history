# Considerations

When you're using a Amazon SageMaker HyperPod recipes, there are some factors that can impact
the process of model training.

- The `transformers` version must be `4.45.2` or greater
  for Llama 3.2. If you're using a Slurm or K8s workflow, the version is
  automatically updated.
- Mixtral does not support 8-bit floating point precision (FP8)
- Amazon EC2 p4 instance does not support FP8
