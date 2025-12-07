# Special considerations

HyperPod managed tiered checkpointing and elastic training: note that HyperPod checkpointless training is currently incompatible with HyperPod
managed tiered checkpointing and elastic training.

**Instance support**

Currently HyperPod checkpointless training only supports p5 instances as EFA only have abort functionality on p5.

**Recipes**

Checkpointless training recipes for GPT OSS 120B and Llama models are provided to simplify getting started. These recipes can be adapted to full finetuning workflows as well.
For custom models, we recommend reviewing the getting started examples on GitHub to see the necessary training loop modifications required to run checkpointless training.
