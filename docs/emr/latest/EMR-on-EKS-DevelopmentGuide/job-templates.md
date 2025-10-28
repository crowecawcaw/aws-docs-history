# Using job templates

A job template stores values that can be shared across `StartJobRun` API
invocations when starting a job run. It supports two use cases:

- To prevent repetitive recurring `StartJobRun` API request values.
- To enforce a rule that certain values must be provided via `StartJobRun`
  API requests.
  Job templates enable you to define a reusable template for job runs to apply additional
  customization, for example:

- Configuring executor and driver compute capacity
- Setting security and governance properties such as IAM roles
- Customizing a docker image to use across multiple applications and data
  pipelines
  The following topics provide detailed information on using templates, including how to use them to start a job run
  and how to change template parameters.

###### Topics

- [Create and using a job template to start a job
  run](create-job-template.md "create-job-template.md")
- [Defining job template parameters](use-job-template-parameters.md "use-job-template-parameters.md")
- [Controlling access to job templates](iam-job-template.md "iam-job-template.md")
