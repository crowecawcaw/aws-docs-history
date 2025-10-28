# Domains in Amazon SWF

Workflows run in an AWS resource called a _domain_ which provide a way of scoping Amazon SWF
resources within your AWS account. All the components of a workflow,
such as the workflow type and activity types, must be specified to be in a domain.

An AWS account can have multiple domains, each of which can contain multiple workflows, but workflows in different domains
can't interact.

When setting up a new workflow, before you set up any of the other workflow components you need to register a
domain if you have not already done so.

When you register a domain, you specify a _workflow history retention period_. The retention period
is the length of time that Amazon SWF will continue to retain information about the workflow execution after the workflow
execution is complete.

Domain registration is the only functionality initially available in the console. After at least one domain is registered, you can perform the following actions for the domain:

- Register workflow and activity types.
- Initiate workflow executions.
- Cancel, terminate, and send signals to running workflow executions.
- Restart closed workflow executions.
  You can also perform domain management actions, such as deprecating and undeprecating domains.

After you deprecate a domain, you can't use it to create new workflow executions or register new workflows. Deprecating a domain also deprecates all the activity and workflows registered in the domain. Executions that
were started before the domain was deprecated continue to run.

After undeprecating a previously deprecated domain, you can resume using the domain to register workflow types and start new workflow executions.

For more information about these domain management actions, see
[DeprecateDomain](../apireference/API_DeprecateDomain.md "../apireference/API_DeprecateDomain.md") and
[UndeprecateDomain](../apireference/API_UndeprecateDomain.md "../apireference/API_UndeprecateDomain.md").
