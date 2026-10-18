

# Creating private workflows in HealthOmics
<a name="workflows-setup"></a>

You can bring your own workflow to AWS HealthOmics as a *Private workflow* and run your research or production bioinformatics workloads on HealthOmics. To get there, you prepare a workflow definition and configure the resources it depends on.
+ **Workflow definition file:** A workflow definition file written in WDL, Nextflow, or CWL. The workflow definition specifies the inputs and outputs for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow, including compute and memory requirements. The workflow definition file must be in `.zip` format. For more information, see [Workflow definition files](workflow-definition-files.md).
  + You can use [Kiro CLI](https://docs.aws.amazon.com/kiro/latest/userguide/what-is.html) to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see [Example prompts for Kiro CLI](getting-started.md#omics-kiro-prompts) and the [HealthOmics Agentic generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai) on GitHub.
+ **Container images:** If your workflow needs container images from public registries or from your own repositories, you can configure Amazon Elastic Container Registry (Amazon ECR) and AWS Identity and Access Management (IAM) permissions for your run. With HealthOmics, you can use your own private containers and container images from Docker Hub, Amazon ECR Public, GitHub Container Registry, GitLab Container Registry, Google Artifact or Container Registry, Kubernetes Container Registry, Microsoft Azure Container Registry, NVIDIA NGC, Quay, and Seqera Containers. For more information about supported registries, see [Container images for private workflows](workflows-ecr.md).
+ **(Optional) Parameter template file:** A parameter template file written in JSON. Create the file to define the run parameters, or HealthOmics generates the parameter template for you. For more information, see [Parameter template files for HealthOmics workflows](parameter-templates.md).
+ **(Optional) README file:** You can attach comprehensive documentation, implementation details, and diagrams directly to your bioinformatics workflows and workflow versions using README files. README files improve workflow management by providing a centralized location for critical workflow documentation, enabling more effective knowledge sharing across research teams. For more information, see [Workflow README files](workflows-readme.md).
+ **(Optional) Sentieon licenses:** Request a Sentieon license to use the Sentieon software in private workflows.
+ **(Optional) Illumina DRAGEN:** Run Illumina DRAGEN software mode as a task in a private workflow. For more information, see [Illumina DRAGEN on HealthOmics private workflows](workflows-illumina-dragen.md).

You can catch issues in your workflows before you start a run, saving time. HealthOmics provides two resources to help find issues in your workflow definition.
+ **[Workflow linters](workflows-linter.md)**: Lint your workflow definition to catch errors and warnings early. HealthOmics includes built-in linters that run during workflow creation, and you can optionally run a linter locally before you create the workflow. When the built-in linter finds issues, the structured lint results appear in the `statusMessage` so you can review and fix them.
+ **[Supported language specifications and engine versions](workflows-supported-languages.md)**: HealthOmics supports workflow definitions written in three workflow languages. Each language has its own syntax, capabilities, and version support.

When your workflow definition and container images are ready, create the workflow in the console, with the AWS Command Line Interface (AWS CLI), or with an AWS SDK. The workflow starts in `CREATING` and becomes `ACTIVE` when it is ready. After the workflow is `ACTIVE`, you can start a run. For more information, see [HealthOmics workflow operations](creating-private-workflows.md).

**Topics**
+ [HealthOmics workflow integration with Git-based repositories](workflows-git-integration.md)
+ [Workflow definition files in HealthOmics](workflow-definition-files.md)
+ [Parameter template files for HealthOmics workflows](parameter-templates.md)
+ [Container images for private workflows](workflows-ecr.md)
+ [Environment variables for HealthOmics workflows](ecr-env-vars.md)
+ [HealthOmics Workflow README files](workflows-readme.md)
+ [Requesting Sentieon licenses for private workflows](private-workflows-subscribe.md)
+ [Illumina DRAGEN on HealthOmics private workflows](workflows-illumina-dragen.md)
+ [Supported workflow languages for HealthOmics](workflows-supported-languages.md)
+ [Workflow linters in HealthOmics](workflows-linter.md)
+ [HealthOmics workflow operations](creating-private-workflows.md)