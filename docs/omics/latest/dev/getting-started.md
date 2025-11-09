# Getting started with HealthOmics

To get started with HealthOmics, ensure that you have properly set up your
[IAM permissions and roles for HealthOmics](setting-up-new.md#setting-up-create-iam-user "setting-up-new.md#setting-up-create-iam-user").

## Using a Ready2Run workflow in the HealthOmics console

The following exercise shows how to use a Ready2Run workflow. A Ready2Run workflow is preconfigured
with the parameters and tool references you need to run the workflow. The workflow publisher provides
sample data, so you do not need to create your own data.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. Select the navigation pane (≡) in the top left, and select **Ready2Run workflows**.
3. On the **Ready2Run workflows** page, choose the
   **ESMFold for up to 800 residues** workflow.
   The console opens the details page for that workflow.
4. The details tab provides information about the workflow. To try out the workflow,
   in the top right of the page select **Start run**.
5. In the **Specify run details** page, enter a run name.
6. Enter or select an Amazon S3 location for the run output.
7. For **Run metadata retention mode**, choose whether to retain or remove runmeta data.
8. In the **Service role** panel, choose **Create and use a new service
   role**.
9. Choose **Next**.
10. On the **Add parameter values** page, choose **Run workflow with Ready2Run test
    data**.
11. Choose **Next**.
12. Review your inputs, then choose **Start run**.

## Example prompts for Amazon Q CLI

Amazon Q CLI can run genomic workflows and analysis tasks in AWS HealthOmics using natural language commands.
The following example prompts allow you to create workflows, manage runs, and analyze genomic data. For
more information and example prompts for HealthOmics, see the
[HealthOmics Agentic
generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai "https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai") on GitHub.

- "Create a WDL 1.1 workflow file as `main.wdl` that will run on HealthOmics. The workflow will
  take a reference genome as an input and pairs of fastq files. It will index the reference genome
  using BWA and then map each pair of fastq files to the reference. Finally merge each mapped BAM to
  a single BAM file and output this file and it's bai index."
- "Package the workflow and create it in HealthOmics"
- "Update the inputs.json file to use real files from my Amazon S3 bucket
  `omics-my-bucket-with-genome-data`" (Provide a specific Amazon S3 bucket location, or let
  Amazon Q explore)
- "Find suitable containers in my Amazon ECR repositories and update inputs.json to use these"
- "Find or create a suitable IAM role to use when running the workflow"
- "Create a run cache for my workflow"
- "Run the workflow in HealthOmics"
- "Check the status of the run"

###### Warning

When working with Amazon Q CLI, review all generated content and proposed actions before proceeding.
Provide feedback to improve response quality and to match your workflow’s requirements. For more information, see
[Security considerations and best practices](../../../amazonq/latest/qdeveloper-ug/command-line-chat-security.md "../../../amazonq/latest/qdeveloper-ug/command-line-chat-security.md") for Amazon Q.
