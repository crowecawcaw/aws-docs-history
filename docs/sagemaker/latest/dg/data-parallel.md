# Run distributed training with the SageMaker AI distributed data

parallelism library

The SageMaker AI distributed data parallelism (SMDDP) library extends SageMaker training
capabilities on deep learning models with near-linear scaling efficiency by providing
implementations of collective communication operations optimized for AWS infrastructure.

When training large machine learning (ML) models, such as large language models (LLM) and
diffusion models, on a huge training dataset, ML practitioners use clusters of accelerators and
distributed training techniques to reduce the time to train or resolve memory constraints for
models that cannot fit in each GPU memory. ML practitioners often start with multiple
accelerators on a single instance and then scale to clusters of instances as their workload
requirements increase. As the cluster size increases, so does the communication overhead between
multiple nodes, which leads to drop in overall computational performance.

To address such overhead and memory problems, the SMDDP library offers the following.

- The SMDDP library optimizes training jobs for AWS network infrastructure and
  Amazon SageMaker AI ML instance topology.
- The SMDDP library improves communication between nodes with implementations of
  `AllReduce` and `AllGather` collective communication operations that
  are optimized for AWS infrastructure.
  To learn more about the details of the SMDDP library offerings, proceed to [Introduction to the SageMaker AI distributed data parallelism
  library](data-parallel-intro.md "data-parallel-intro.md").

For more information about training with the model-parallel strategy offered by SageMaker AI,
see also [(Archived) SageMaker model parallelism library v1.x](model-parallel.md "model-parallel.md").

###### Topics

- [Introduction to the SageMaker AI distributed data parallelism
  library](data-parallel-intro.md "data-parallel-intro.md")
- [Supported frameworks, AWS Regions, and
  instances types](distributed-data-parallel-support.md "distributed-data-parallel-support.md")
- [Distributed training with the SageMaker AI
  distributed data parallelism library](data-parallel-modify-sdp.md "data-parallel-modify-sdp.md")
- [Amazon SageMaker AI data parallelism library
  examples](distributed-data-parallel-v2-examples.md "distributed-data-parallel-v2-examples.md")
- [Configuration tips for the SageMaker AI distributed data
  parallelism library](data-parallel-config.md "data-parallel-config.md")
- [Amazon SageMaker AI distributed data parallelism library FAQ](data-parallel-faq.md "data-parallel-faq.md")
- [Troubleshooting for distributed
  training in Amazon SageMaker AI](distributed-troubleshooting-data-parallel.md "distributed-troubleshooting-data-parallel.md")
- [SageMaker AI data parallelism library release notes](data-parallel-release-notes.md "data-parallel-release-notes.md")
