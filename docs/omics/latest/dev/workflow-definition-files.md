AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Workflow definition files in HealthOmics

You use a workflow definition to specify information about the workflow, runs, and the tasks in the runs.
You create workflow definitions in one or more files using a workflow definition language. HealthOmics supports workflow
definitions written in WDL, Nextflow, or CWL. For details about each of these languages, see
the language-specific detailed sections below.

You specify the following types of information in the workflow definition:

- **Language version** – The language and version of the workflow definition.
- **Compute and memory** – The compute and memory requirements for tasks in the workflow.
- **Inputs** – Location of the inputs to the workflow tasks. For more information, see
  [HealthOmics run inputs](workflows-run-inputs.md "workflows-run-inputs.md").
- **Outputs** – Location to save the outputs that the tasks generate.
- **Task resources** – Compute and memory requirements for each task.
- **Accelerators** – other resources that the tasks require, such as accelerators.

###### Topics

- [HealthOmics workflow definition requirements](workflow-defn-requirements.md "workflow-defn-requirements.md")
- [Version support for HealthOmics workflow definition languages](workflows-lang-versions.md "workflows-lang-versions.md")
- [Compute and memory requirements for HealthOmics tasks](memory-and-compute-tasks.md "memory-and-compute-tasks.md")
- [Task outputs in a HealthOmics workflow definition](workflows-task-outputs.md "workflows-task-outputs.md")
- [Task resources in a HealthOmics workflow definition](task-resources.md "task-resources.md")
- [Task accelerators in a HealthOmics workflow definition](task-accelerators.md "task-accelerators.md")
- [WDL workflow definition specifics](workflow-languages-wdl.md "workflow-languages-wdl.md")
- [Nextflow workflow definition specifics](workflow-definition-nextflow.md "workflow-definition-nextflow.md")
- [CWL workflow definition specifics](workflow-languages-cwl.md "workflow-languages-cwl.md")
- [Example workflow definitions](workflow-definition-examples.md "workflow-definition-examples.md")
