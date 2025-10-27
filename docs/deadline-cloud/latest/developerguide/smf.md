# Configure and use Deadline Cloud service-managed fleets

A service-managed fleet (SMF) is a collection of workers managed by Deadline Cloud. An SMF eliminates
the need to manage fleet scaling for processing demands or reduce fleet size after task
completion.

When an SMF is associated with a queue using the default Conda queue environment, Deadline Cloud
configures the workers in the fleet with the appropriate software package. For supported partner
applications, see [Default Conda queue
environment](../userguide/create-queue-environment.md "../userguide/create-queue-environment.md") in the _AWS Deadline Cloud User Guide_.

In most cases, you don't need to change an SMF to process your workloads. However, some
situations may require you make changes to your fleets. These include:

- Running scripts that require elevated permissions to install software or
  Docker containers.

###### Topics

- [Run scripts as an administrator to configure workers](smf-admin.md "smf-admin.md")
- [Connect VPC resources to your SMF with VPC resource endpoints](smf-vpc.md "smf-vpc.md")
