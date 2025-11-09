# HealthOmics workflow definition requirements

The HealthOmics workflow definition files must meet the following requirements:

- Tasks must define input/output parameters, Amazon ECR container repositories, and runtime
  specifications such as memory or CPU allocation.
- Verify that your IAM roles have the required permissions.
  - Your workflow has access to input data from AWS resources, such as Amazon S3.
  - Your workflow has access to external repository services when needed.

- Declare the output files in the workflow definition. To copy intermediate run files to
  the output location, declare them as workflow outputs.
- The input and output locations must be in the same Region as the workflow.
- HealthOmics storage workflow inputs must be in `ACTIVE` status. HealthOmics won't import inputs with an
  `ARCHIVED` status, causing the workflow to fail. For information about Amazon S3 object inputs, see
  [HealthOmics run inputs](workflows-run-inputs.md "workflows-run-inputs.md").
- A **main** location of the workflow is optional if your ZIP archive contains either a
  single workflow definition or a file named 'main'.
  - Example path: `workflow-definition/main-file.wdl`

- Before you create a workflow from Amazon S3 or your local drive, create a zip archive of the workflow
  definition files and any dependencies, such as subworkflows.
- We recommend that you declare Amazon ECR containers in the workflow as input parameters for validation of the
  Amazon ECR permissions.
  Additional Nextflow considerations:

- **/bin**

Nextflow workflow definitions may include a /bin folder with executable scripts. This path has read-only
plus executable access to tasks. Tasks that rely on these scripts should use a container built with the
appropriate script interpreters. Best practice is to call the interpreter directly. For example:

```
process my_bin_task {
   ...
   script:
      """
      python3 my_python_script.py
      """
}

```

- **includeConfig**

Nextflow-based workflow definitions can include nextflow.config files that help to abstract parameter
definitions or process resource profiles. To support development and execution of Nextflow pipelines on
multiple environments, use a HealthOmics-specific configuration that you add to the global config using the
includeConfig directive. To maintain portability, configure the workflow to include the file only when running
on HealthOmics by using the following code:

```
// at the end of the nextflow.config file
if ("$AWS_WORKFLOW_RUN") {
    includeConfig 'conf/omics.config'
}
```

- **Reports**

HealthOmics doesn't support engine-generated dag, trace, and execution reports. You can generate alternatives to
the trace and execution reports using a combination of GetRun and GetRunTask API calls.
Additional CWL considerations:

- **Container image uri interpolation**

HealthOmics allows the dockerPull property of the DockerRequirement to be an inline javascript expression.
For example:

```
requirements:
  DockerRequirement:
    dockerPull: "$(inputs.container_image)"
```

This allows you to specifying container image URIs as input parameters to the workflow.

- **Javascript expressions**

Javascript expressions must be `strict mode` compliant.

- **Operation process**

HealthOmics doesn't support CWL Operation processes.
