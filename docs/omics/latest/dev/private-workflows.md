AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Private workflows in HealthOmics

Use _Private workflows_ when you want to create your own workflow definition. The workflow definition
specifies information about the workflow and defines the workflow tasks. A _run_ is a single
invocation of a workflow, and a _task_ is a single process within the run.

HealthOmics supports workflow definitions that you create in Workflow Description Language (WDL), Common Workflow Language
(CWL), or Nextflow.

HealthOmics workflows provide the following optional features:

- **[Run groups](creating-run-groups.md "creating-run-groups.md")** – You can add private workflows to a run group to control compute usage. A _run group_ is a
  collection of workflow runs that share a set of resource limits, such as maximum concurrent runs and maximum run
  duration. You set these limits to control the compute resources that the run group consumes.
- **[Call caching](workflows-call-caching.md "workflows-call-caching.md")** – You can use a call
  cache to save and reuse task outputs, which results in shorter run durations and compute cost savings.
- **[Sharing workflows](sharing-workflows.md "sharing-workflows.md")** – You can share your private workflows with other AWS accounts in the
  same Region.
- **[Workflow versions](workflow-versions.md "workflow-versions.md")** – You can create
  versions of a private workflow. Workflow versioning provides the ability for users to choose when to start using updated
  functionality. Workflow versions are immutable and provide the same level of data provenance as
  workflows.
  For information about configuring IAM permissions for workflows, see [IAM permissions for HealthOmics](omics-permissions.md "omics-permissions.md").

For full examples of how to use HealthOmics private workflows, see [HealthOmics Github tutorials](https://github.com/aws-samples/amazon-omics-tutorials "https://github.com/aws-samples/amazon-omics-tutorials") or the [AWS workshop end to end tutorial for HealthOmics](https://catalog.workshops.aws/amazon-omics-end-to-end " https://catalog.workshops.aws/amazon-omics-end-to-end").

###### Topics

- [Creating private workflows in HealthOmics](workflows-setup.md "workflows-setup.md")
- [Working with a README file](workflows-readme.md "workflows-readme.md")
- [Workflow versioning in HealthOmics](workflow-versions.md "workflow-versions.md")
- [Using HealthOmics runs](running-workflows.md "running-workflows.md")
- [Using HealthOmics run groups](creating-run-groups.md "creating-run-groups.md")
- [Call caching for HealthOmics runs](workflows-call-caching.md "workflows-call-caching.md")
- [Sharing HealthOmics workflows](sharing-workflows.md "sharing-workflows.md")
