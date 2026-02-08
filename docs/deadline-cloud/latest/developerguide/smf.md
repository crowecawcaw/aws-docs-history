# Configure and use Deadline Cloud service-managed fleets

A service-managed fleet (SMF) is a collection of workers managed by Deadline Cloud. An SMF eliminates
the need to manage fleet scaling for processing demands or reduce fleet size after task
completion.

When an SMF is associated with a queue using the default conda queue environment, Deadline Cloud
configures the workers in the fleet with the appropriate software package. For supported partner
applications, see [Default conda queue
environment](../userguide/create-queue-environment.md "../userguide/create-queue-environment.md") in the _AWS Deadline Cloud User Guide_.

In most cases, you don't need to change an SMF to process your workloads. However, some
situations may require you make changes to your fleets.

###### Topics

- [Run scripts as an administrator to configure workers](smf-admin.md "smf-admin.md")
- [Connect VPC resources to your SMF with VPC resource endpoints](smf-vpc.md "smf-vpc.md")
- [Use job attachments with service-managed fleets](smf-job-attachments.md "smf-job-attachments.md")
