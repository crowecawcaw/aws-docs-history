# Control the job environment with OpenJD queue

environments

You can define customized environments for your rendering jobs using _queue
environments_. A queue environment is a template that controls the environment
variables, file mappings, and other settings for jobs running in a specific queue. It enables
you to tailor the execution environment for the jobs submitted to a queue to the requirements of
your workloads. AWS Deadline Cloud provides three nested levels where you can apply [Open Job Description (OpenJD) environments](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment "https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment"): queue, job, and step. By defining queue
environments, you can ensure consistent and optimized performance for different types of jobs,
streamline resource allocation, and simplify queue management.

The queue environment is a template that you attach to a queue in your AWS account from
the AWS management console or using the AWS CLI. You can create one environment for a queue, or
you can create multiple queue environments that applied in order to create the execution
environment. This enables you to create and test an environment in steps to help ensure that it
works correctly for you jobs.

Job and step environments are defined in the job template you use to create a job in your
queue. The OpenJD syntax is the same in these different forms of environments. In this section
we will show them inside of job templates.

###### Topics

- [Set environment variables in a queue
  environment](set-environment-variables.md "set-environment-variables.md")
- [Set the path in a queue environment](set-the-path.md "set-the-path.md")
- [Run a background daemon process from the
  queue environment](run-a-background-daemon-process.md "run-a-background-daemon-process.md")
