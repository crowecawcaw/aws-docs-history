# When to use Fargate

We recommend using Fargate in most scenarios. Fargate launches and scales the compute to
closely match the resource requirements that you specify for the container. With Fargate, you
don't need to over-provision or pay for additional servers. You also don't need to worry about
the specifics of infrastructure-related parameters such as instance type. When the compute
environment needs to be scaled up, jobs that run on Fargate resources can get started more
quickly. Typically, it takes a few minutes to spin up a new Amazon EC2 instance. However, jobs that
run on Fargate can be provisioned in about 30 seconds. The exact time required depends on
several factors, including container image size and number of jobs.

However, we recommend that you use Amazon EC2 if your jobs require any of the following:

- More than 16 vCPUs
- More than 120 gibibytes (GiB) of memory
- A GPU
- A custom Amazon Machine Image (AMI)
- Any of the [linuxParameters](job_definition_parameters.md#ContainerProperties-linuxParameters "job_definition_parameters.md#ContainerProperties-linuxParameters")
  parameters
  If you have a large number of jobs, we recommend that you use Amazon EC2 infrastructure. For
  example, if the number of concurrently running jobs exceeds the Fargate throttling limits. This
  is because, with EC2, jobs can be dispatched at a higher rate to EC2 resources than to Fargate
  resources. Moreover, more jobs can run concurrently when you use EC2. For more information, see
  [Fargate
  service quotas](../../../AmazonECS/latest/developerguide/service-quotas.md#service-quotas-fargate "../../../AmazonECS/latest/developerguide/service-quotas.md#service-quotas-fargate") in the _Amazon Elastic Container Service Developer Guide_.
