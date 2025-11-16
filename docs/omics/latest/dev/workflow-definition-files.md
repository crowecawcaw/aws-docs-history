# Workflow definition files in HealthOmics

You use a workflow definition to specify information about the workflow, runs, and the tasks in the runs. You
create workflow definitions in one or more files using a workflow definition language. HealthOmics supports workflow
definitions written in WDL, Nextflow, or CWL.

HealthOmics supports the following choices for WDL workflow definitions:

- WDL – Provides a spec-conformant WDL engine.
- WDL lenient – Designed to handle workflows migrated from Cromwell. It supports customer Cromwell
  directives and some non-conformant logic. For details, see [Implicit type conversion in WDL lenient](workflow-languages-wdl.md#workflow-wdl-type-conversion "workflow-languages-wdl.md#workflow-wdl-type-conversion").
  For information about each of the workflow languages, see the language-specific detailed sections below.

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
