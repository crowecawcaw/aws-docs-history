AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Creating or updating a workflow

To create a private workflow, you need:

- **Workflow definition file:** A workflow definition file written in WDL,
  Nextflow, or CWL. The workflow definition specifies the inputs and outputs
  for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow,
  including compute and memory requirements. The workflow definition file must be in `.zip` format.
  For more information, see [Workflow definition files](workflow-definition-files.md "workflow-definition-files.md") in HealthOmics.
  - You can use [Amazon Q CLI](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md")
    to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see
    [Example prompts for Amazon Q CLI](getting-started.md#omics-q-prompts "getting-started.md#omics-q-prompts") and the
    [HealthOmics Agentic generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai "https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai")
    on GitHub.

- **(Optional) Parameter template file:** A parameter template file written in JSON.
  Create the file to define the run parameters, or HealthOmics generates the parameter template for you. For more information,
  see [Parameter template files for HealthOmics workflows](parameter-templates.md "parameter-templates.md").
- **Amazon ECR container images:** Create private Amazon ECR repositories for each container used in the
  workflow. Create container images for the workflow and store them in a private repository, or synchronize the
  contents of a supported upstream registry with your ECR private repository.
- **(Optional) Sentieon licenses:** Request a Sentieon license to use the
  Sentieon software in private workflows.
  For workflow definition files larger than 4 MiB (zipped), choose one of these options during workflow creation:

- Upload to an Amazon Simple Storage Service folder and specify the location.
- Upload to an external repository (max size 1 GiB) and specify the repository details.
  After you create a workflow, you can update the following workflow information with the
  `UpdateWorkflow` operation:

- Name
- Description
- Default storage type
- Default storage capacity (with workflow ID)
- README.md file
  To change other information in the workflow, create a new workflow or workflow version.

Use workflow versioning to organize and structure you workflows. Versions also help you to manage the
introduction of iterative workflow updates. For more information about versions, see [Create a workflow version](workflows-version-create.md "workflows-version-create.md").

###### Topics

- [Create a private workflow](create-private-workflow.md "create-private-workflow.md")
- [Update a private workflow](update-private-workflow.md "update-private-workflow.md")
- [Delete a private workflow](delete-private-workflow.md "delete-private-workflow.md")
- [Verify the workflow status](using-get-workflow.md "using-get-workflow.md")
- [Referencing genome files from a workflow definition](create-ref-files.md "create-ref-files.md")
