# Job templates

Use job templates to preconfigure jobs that you can deploy to multiple sets of target
devices. To deploy frequently performed remote actions to your devices, like rebooting or
installing an application, you can use templates to define standard configurations. To
perform operations such as deploying security patches and bug fixes, you can create
templates from existing jobs.

When creating a job template, specify the following additional configurations and
resources.

- Job properties
- Job documents and targets
- Rollout, scheduling, and cancel criteria
- Timeout and retry criteria

## Custom and AWS managed templates

Depending on the remote action that you want to perform, you can either create a
custom job template or use an AWS managed template. Use custom job templates to
provide your own custom job document and create reusable jobs to deploy to your devices.
AWS managed templates are job templates provided by AWS IoT Jobs for commonly performed
actions. These templates have a predefined job document for some remote actions so you
don't have to create your own job document. Managed templates help you create reusable
jobs for faster
launch
to your devices.

###### Topics

- [Use AWS managed templates to deploy common
  remote operations](job-templates-managed.md "job-templates-managed.md")
- [Create custom job templates](job-templates-create.md "job-templates-create.md")
