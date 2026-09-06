

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Custom templates for Migration Hub Orchestrator
<a name="custom-templates"></a>

You can customize the templates provided by AWS Migration Hub Orchestrator for your use case and save them for reuse. You must first use a template provided by Migration Hub Orchestrator to create a migration workflow. Once the migration workflow is created, you can proceed with making customizations to the workflow.

To help ensure that the custom template works as expected, we recommend that you run the customized workflow after making your changes. Once the updated migration workflow completes successfully, you can save your changes as a new custom template.

**Topics**
+ [Prerequisites](#custom-templates-prerequisites)
+ [Creating custom templates](#creating-custom-templates)
+ [Running custom templates](#running-custom-templates)
+ [Updating custom templates](#updating-custom-templates)

## Prerequisites
<a name="custom-templates-prerequisites"></a>

The following prerequisites must be met to create custom templates:
+ If the AWS managed template that you will customize requires the Migration Hub Orchestrator plugin, you must configure it before running the workflow. For more information, see [Run the workflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/how-mho-works.html#run-workflow).
+ To create a migration workflow, you must have the resources required by your desired AWS managed template available.
+ If you are going to create steps in the workflow of the **Automated** type, ensure that the scripts are accessible using one of the following methods:
  + If the scripts for your custom template will be sourced from an Amazon Simple Storage Service (Amazon S3) location, the script files must be uploaded to an Amazon S3 bucket with the prefix `migrationhub-orchestrator-`. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) in the *Amazon Simple Storage Service User Guide*.
  + If the scripts for your template will be uploaded to the AWS Management Console, you must be able to upload a copy of the script from the device that you are using.

## Creating custom templates
<a name="creating-custom-templates"></a>

You can use the following steps to create a custom template using the Migration Hub Orchestrator Console or the AWS CLI.

------
#### [ Console ]

**To create a custom template using the Migration Hub Orchestrator console**

1. Sign in to the AWS Management Console and open the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/?region=us-east-1\#/templates](https://console.aws.amazon.com/migrationhub/orchestrator/).

1. Choose the template from the list that you want to customize. For more information about the available templates, see [Templates](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/templates.html).

1. Choose **Create workflow**.

1. Customize the workflow steps and step groups of the template as necessary. For more information about how to modify a workflow, see [Migration workflows](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migration-workflows.html).

1. (Recommended) Once you have finished modifying the workflow, choose **Run** to start the workflow and ensure it completes successfully. For more information, see [Running workflows](migration-workflows.md#running-migration-workflows).

1. Choose **Save as a template**.

1. For **Name**, enter a name for the custom template.

1. (Optional) For **Description**, enter a description for the custom template.

1. (Optional) Add tags to your custom template:

   1. Choose **Add new tag** for each tag that you'd like to associate with the custom template.

   1. Enter values in the **Key** and **Value** fields as necessary.

1. Choose **Save**.

Your custom template will now be available in the workflow templates list.

------
#### [ AWS CLI ]

You can use the [CreateTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateTemplate.html) Migration Hub Orchestrator API operation to create a custom template using the AWS CLI.

------

## Running custom templates
<a name="running-custom-templates"></a>

You can use the Migration Hub Orchestrator console or the AWS CLI to run custom templates.

**Tip**  
Each template might have prerequisites and manual steps to run the workflow successfully. You can refer to the documentation for the predefined templates provided by Migration Hub Orchestrator your custom template is based on. For more information, see [Templates](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/templates.html).

------
#### [ Console ]

**To run a custom template using the Migration Hub Orchestrator console**

1. Sign in to the AWS Management Console and open the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/?region=us-east-1\#/templates](https://console.aws.amazon.com/migrationhub/orchestrator/).

1. Choose the custom template from the list that you want to run.

1. Choose **Create workflow**.

1. Choose **Run**.

1. In the **Steps** tab, choose **Expand all**. Steps with a **Status** of **User attention required** need additional input to complete the step.

1. Choose the step which requires further input, choose **Actions**, **Change status**, **Completed**.

1.  Take action on any steps which require your input for the workflow to proceed to completion.

------
#### [ AWS CLI ]

You can use the [CreateWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflow.html) Migration Hub Orchestrator API operation to create a custom template using the AWS CLI.

------

## Updating custom templates
<a name="updating-custom-templates"></a>

You can't directly update a custom template. Instead, you can create a workflow from a custom template and make updates to the migration workflow it creates. Once you have made your updates, you can save your updates to a new custom template.

------
#### [ Console ]

**To update a custom template and save them as a new template using the Migration Hub Orchestrator console**

1. Sign in to the AWS Management Console and open the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/?region=us-east-1\#/templates](https://console.aws.amazon.com/migrationhub/orchestrator/).

1. Choose the custom template from the list that you want to update.

1. Choose **Create workflow**.

1. Customize the workflow steps and step groups of the template as necessary. For more information about how to modify a workflow, see [Migration workflows](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/migration-workflows.html).

1. (Recommended) Once you have finished modifying the workflow, choose **Run** to start the workflow. For more information, see [Running custom templates](#running-custom-templates).

1. Choose **Save as a template**.

1. For **Name**, enter a name for the custom template.

1. (Optional) For **Description**, enter a description for the custom template.

1. (Optional) Add tags to your custom template:

   1. Choose **Add new tag** for each tag that you'd like to associate with the custom template.

   1. Enter values in the **Key** and **Value** fields as necessary.

1. Choose **Save**.

Your new custom template will be available in the workflow templates list.

------
#### [ AWS CLI ]

You can use the [UpdateTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateTemplate.html) Migration Hub Orchestrator API operation to create a custom template using the AWS CLI.

------