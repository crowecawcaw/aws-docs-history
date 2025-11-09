# Using HealthOmics runs

After you create a workflow, you can start runs using the workflow.

When you start a run, HealthOmics allocates temporary run storage for the workflow engine to use during the run. To
ensure data isolation and security, HealthOmics provisions the storage at the start of each run, and deprovisions it at the
end of the run.

HealthOmics provides several quotas related to workflow runs and tasks. Default values are intentionally conservative,
to help you avoid unexpected cost overruns. You can request an increase in these quotas. For more information, see
[HealthOmics service quotas](service-quotas.md "service-quotas.md").

When you start a run, HealthOmics assigns a run ID and a run uuid to the run. Runs in an account have unique run IDs.
However, HealthOmics reuses deleted run IDs, so a run and a deleted run can have the same run ID. Also, it's rare but
possible for a shared workflow to have the same run ID as a run in your account.

The **run uuid** is a Globally Unique Identifier (guid) that you can use to identify runs across
accounts or to distinguish between two runs in your account that have the same run ID.

###### Note

For data provenance purposes, we recommend that you use the **run uuid** to uniquely identify
runs. The **run uuid** is also the best identifier to link to your internal lab information
management system (LIMs) or sample tracking system.

You can use [Amazon Q CLI](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md")
to optimize your runs and analyze run performance. For more information, see
[Example prompts for Amazon Q CLI](getting-started.md#omics-q-prompts "getting-started.md#omics-q-prompts") and the
[HealthOmics Agentic generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai "https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai")
on GitHub.

###### Topics

- [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md")
- [Run retention mode for HealthOmics runs](run-retention.md "run-retention.md")
- [HealthOmics run inputs](workflows-run-inputs.md "workflows-run-inputs.md")
- [Run lifecycle in a HealthOmics workflow](monitoring-runs.md "monitoring-runs.md")
- [HealthOmics run outputs](workflows-run-outputs.md "workflows-run-outputs.md")
- [Run failure reasons](workflows-run-errors.md "workflows-run-errors.md")
- [Task lifecycle in a HealthOmics run](workflow-run-tasks.md "workflow-run-tasks.md")
- [Run optimization for a private HealthOmics workflow](workflows-run-optimize.md "workflows-run-optimize.md")
- [Run operations in HealthOmics](run-operations.md "run-operations.md")
