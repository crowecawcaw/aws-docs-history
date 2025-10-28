# Design principles

When designing for HPC in the cloud, a number of principles help
you achieve performance efficiency:

- **Design the cluster for the
  application**: Traditional clusters are static and
  require that the application is designed for the cluster. AWS
  offers the capability to design the cluster for the
  application. A one- size-fits-all model is no longer necessary
  with individual clusters for each application. When running a
  variety of applications on AWS, a variety of architectures can
  be used to meet each application's demands. This allows for
  the best performance while minimizing cost.
- **Test performance with a meaningful use case**: The best
  method to gauge an HPC application's performance on a particular architecture is to run a
  meaningful demonstration of the application itself. An inadvertently small or large
  demonstration case one without the expected compute, memory, data transfer, or network
  traffic will not provide a meaningful test of application performance on AWS. Although
  system-specific benchmarks offer an understanding of the underlying compute infrastructure
  performance, they do not reflect how an application will perform in the aggregate. The
  AWS pay-as-you-go model makes a proof-of-concept quick and cost-effective.
- **Use cloud-native architectures
  where applicable**: In the cloud, managed,
  serverless, and cloud-native architectures remove the need
  for you to run and maintain servers to carry out
  traditional compute activities. Cloud-native components
  for HPC target compute, storage, job orchestration and
  organization of the data and metadata. The variety of AWS
  services allows each step in the workload process to be
  decoupled and optimized for a more performant capability.
- **Experiment often**:
  Virtual and automatable resources help you quickly carry
  out comparative testing using different types of
  instances, storage, and configurations.
