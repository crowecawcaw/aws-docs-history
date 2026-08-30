# Creating private workflows in HealthOmics

_Private workflows_ depend on a variety of resources that you create and configure before
creating the workflow:

- **Workflow definition file:** A workflow definition file written in WDL,
  Nextflow, or CWL. The workflow definition specifies the inputs and outputs
  for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow,
  including compute and memory requirements. The workflow definition file must be in `.zip` format.
  For more information, see [Workflow definition files](workflow-definition-files.md "workflow-definition-files.md").

  - You can use [Kiro CLI](../../../kiro/latest/userguide/what-is.md "../../../kiro/latest/userguide/what-is.md")
    to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see
    [Example prompts for Kiro CLI](getting-started.md#omics-kiro-prompts "getting-started.md#omics-kiro-prompts")
    and the [HealthOmics Agentic generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai "https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai")
    on GitHub.

- **(Optional) Parameter template file:** A parameter template file written in JSON.
  Create the file to define the run parameters, or HealthOmics generates the parameter template for you. For more information,
  see [Parameter template files for HealthOmics workflows](parameter-templates.md "parameter-templates.md").
- **Amazon ECR container images:** Create a private Amazon ECR repository for the workflow. Create
  container images in the private repository, or synchronize the contents of a supported upstream registry with
  your Amazon ECR private repository.
- **(Optional) Sentieon licenses:** Request a Sentieon license to use the
  Sentieon software in private workflows.
  In addition to built-in linters, you can optionally run a linter locally on your workflow definition
  before you create the workflow. For more information on built-in and optional external linters, see
  [Workflow linters in HealthOmics](workflows-linter.md "workflows-linter.md").

###### Topics

- [HealthOmics workflow integration with Git-based repositories](workflows-git-integration.md "workflows-git-integration.md")
- [Workflow definition files in HealthOmics](workflow-definition-files.md "workflow-definition-files.md")
- [Parameter template files for HealthOmics workflows](parameter-templates.md "parameter-templates.md")
- [Container images for private workflows](workflows-ecr.md "workflows-ecr.md")
- [HealthOmics Workflow README files](workflows-readme.md "workflows-readme.md")
- [Requesting Sentieon licenses for private workflows](private-workflows-subscribe.md "private-workflows-subscribe.md")
- [Workflow linters in HealthOmics](workflows-linter.md "workflows-linter.md")
- [HealthOmics workflow operations](creating-private-workflows.md "creating-private-workflows.md")
