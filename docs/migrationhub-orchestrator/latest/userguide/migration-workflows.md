AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Migration workflows for Migration Hub Orchestrator

Migration workflows are created using templates. The predefined templates provided by Migration Hub Orchestrator
offer automation capabilities and facilitate the migration of your on-premises servers and
applications to AWS. A template consists of one or more step groups that contain at least one
step each. You can create a migration workflow with one of the predefined templates, or with a
custom template that you can create.

Each template will have different prerequisites and configuration options. You should refer
to the documentation for the template that you intend to use before creating a migration workflow.
Once you create a migration workflow, you can perform various actions to customize it for your use
case. For more information, see [Migration Hub Orchestrator templates](templates.md "templates.md").

###### Topics

- [Considerations and limitations](#considerations-limitations-migration-workflows "#considerations-limitations-migration-workflows")
- [Creating step groups](#create-step-groups-migration-workflow "#create-step-groups-migration-workflow")
- [Creating steps in an existing step group](#create-steps-migration-workflow "#create-steps-migration-workflow")
- [Updating step groups](#update-step-groups-migration-workflow "#update-step-groups-migration-workflow")
- [Updating steps](#update-steps-migration-workflow "#update-steps-migration-workflow")
- [Deleting step groups](#delete-step-groups-migration-workflow "#delete-step-groups-migration-workflow")
- [Deleting steps](#delete-steps-migration-workflow "#delete-steps-migration-workflow")
- [Running workflows](#running-migration-workflows "#running-migration-workflows")
- [Pausing workflows](#pausing-migration-workflows "#pausing-migration-workflows")
- [Deleting workflows](#deleting-migration-workflows "#deleting-migration-workflows")

## Considerations and limitations

The following are considerations and limitations when working with migration workflows:

- You can make modifications to a migration workflow after it's created.
- You can only make modifications to step groups and steps that you have added to a
  migration workflow.
- A step must be placed within a step group. You can choose to add a step to an existing
  step group or create a new step group.
- A step group must have at least one step.
- A step can't be added to a step group with a status of
  **Completed**.
- To delete an ongoing migration workflow, you must pause it first.

- For the **Import virtual machine images to AWS** and **Rehost
  applications on Amazon EC2** predefined templates provided by Migration Hub Orchestrator, only steps added to
  the first step group are retained when you save a new custom template.

## Creating step groups

You can add step groups using the Migration Hub Orchestrator console or the AWS CLI. Each step group must contain
a step.

Console

###### To add step groups using the Migration Hub Orchestrator console

1. Sign in to the AWS Management Console and access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, select the workflow and choose
   **View details**.
4. Under **Steps**, select an existing step group.
5. Choose **Add**, **Add step group above** or
   **Add step group below**.
6. For **Step group name**, enter a name.
7. (Optional) for **Step Group description**, enter a
   description.
8. For **Name**, enter a name for the step.
9. (Optional) For **Description**, enter a description for the
   step.
10. (Optional) For **Script location**, choose **Amazon S3
    URI** or **Upload a file**.
    1. If you chose **Amazon S3 URI**, provide the following details:
       1. For **Script run command**, enter a command to run the
          script.
       2. For **Script run environment**, choose **On
          premises** or **AWS**.
          1. If you chose **On premises**, for **Server**,
             choose a server from the dropdown menu. The resources listed are based on what you
             configured in AWS Application Discovery Service. For more information, refer to the documentation on the
             template your workflow was created from in the [Templates](templates.md "templates.md")
             section.
          2. If you chose **AWS**, for **EC2 instance**,
             select the instances to run the script on.

    2. If you chose **Upload a file**, provide the following
       details:
       1. For **Script file**, choose **Choose file**
          and select a shell or PowerShell script file to use.
       2. For **Script run command**, enter a command to run the
          script.
       3. For Script run environment, choose On premises or
          AWS. The servers listed are the application servers that you
          configured in AWS Application Discovery Service. For more information, refer to the documentation on the
          template your workflow was created from in the [Templates](templates.md "templates.md")
          section.
          1. If you chose **On premises**, for
             **Server**, choose a server from the dropdown menu. The resources
             listed are based on what you configured in AWS Application Discovery Service. For more information,
             refer to the documentation on the template your workflow was created from in the
             [Templates](templates.md "templates.md")
             section.
          2. If you chose **AWS**, for **EC2
             instance**, select the instances to run the script on.

###### Note

If you don’t make a selection for **Script location**, the step’s type will be set to **Manual** which requires user intervention.
After completing the manual procedure for the step, you must update the status to complete for the migration workflow to continue.

AWS CLI
You can use the [CreateWorkflowStepGroup](../APIReference/API_CreateWorkflowStepGroup.md "../APIReference/API_CreateWorkflowStepGroup.md") API operation to add step groups to a
workflow.

## Creating steps in an existing step group

You can add steps using the Migration Hub Orchestrator console or the AWS CLI.

Console

###### To add steps using the Migration Hub Orchestrator console

1. Sign in to the AWS Management Console and access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, select the workflow that you want to
   customize and choose **View details**.
4. Select the step group in which you want to add steps.
5. Under **Steps**, select **Add**, **Add step
   to group**.
6. For **Name**, enter a name for the step.
7. (Optional) For **Description**, enter a description for the
   step.
8. (Optional) For **Script location**, choose **Amazon S3
   URI** or **Upload a file**.
   1. If you chose **Amazon S3 URI**, provide the following details:
      1. For **Script run command**, enter a command to run the
         script.
      2. For **Script run environment**, choose **On
         premises** or **AWS**.
         1. If you chose **On premises**, for **Server**,
            choose a server from the dropdown menu. The resources listed are based on what you
            configured in AWS Application Discovery Service. For more information, refer to the documentation on the
            template your workflow was created from in the [Templates](templates.md "templates.md")
            section.
         2. If you chose **AWS**, for **EC2 instance**,
            select the instances to run the script on.

   2. If you chose **Upload a file**, provide the following
      details:
      1. For **Script file**, choose **Choose file** and
         select a shell or PowerShell script file to use.
      2. For **Script run command**, enter a command to run the
         script.
      3. For Script run environment, choose On premises or
         AWS. The servers listed are the application servers that you
         configured in AWS Application Discovery Service. For more information, refer to the documentation on the
         template your workflow was created from in the [Templates](templates.md "templates.md")
         section.
         1. If you chose **On premises**, for **Server**,
            choose a server from the dropdown menu. The resources listed are based on what you
            configured in AWS Application Discovery Service. For more information, refer to the documentation on the
            template your workflow was created from in the [Templates](templates.md "templates.md")
            section.
         2. If you chose **AWS**, for **EC2 instance**,
            select the instances to run the script on.

###### Note

If you don’t make a selection for **Script location**, the step’s type will be set to **Manual** which requires user intervention.
After completing the manual procedure for the step, you must update the status to complete for the migration workflow to continue.

AWS CLI
You can use the [CreateWorkflowStep](../APIReference/API_CreateWorkflowStep.md "../APIReference/API_CreateWorkflowStep.md") API operation to add steps to a step
group.

## Updating step groups

You can update step groups using the Migration Hub Orchestrator console or the AWS CLI.

Console

###### To update step groups

1. Sign in to the AWS Management Console and access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, select the workflow that you want to
   customize and choose **View details**.
4. If you need to update the order of step groups in the workflow:
   1. In the **Steps** pane, select an existing step group.
   2. Choose **Move up** or **Move down** to reorder the
      step groups as needed.

5. If you need to update information about a step group:
   1. In the **Steps** pane, select an existing step group, then choose
      **Actions**, **Edit step group**.
   2. Update the **Step group name** and **Step group
      description** as required.
   3. Choose **Save**.

AWS CLI
You can use the [UpdateWorkflowStepGroup](../APIReference/API_UpdateWorkflowStepGroup.md "../APIReference/API_UpdateWorkflowStepGroup.md") API operation to update the step groups
in a workflow.

###### Important

You can only update step groups that you have added to a migration workflow that isn't
running or paused.

## Updating steps

You can update steps using the Migration Hub Orchestrator console or the AWS CLI.

Console

###### To update steps

1. Sign in to the AWS Management Console and access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, select the workflow that you want to
   customize and choose **View details**.
4. In the **Steps** pane, select the step group in which you need to
   update.
5. Choose **Expand all** to view the steps within the step group.
6. If you need to update the order of step groups in the workflow:
   1. In the **Steps** pane, select the step you need to move within the
      step group.
   2. Choose **Move up** or **Move down** to reorder the
      step as needed.

7. If you need to update information about a step group:
   1. In the **Steps** pane, select an existing step group, then choose
      **Actions**, **Edit step**.
   2. Update the **Step name** and **Step group
      description**, and **Script location** configuration as
      required.
   3. Choose **Save**.

AWS CLI
You can use the [UpdateWorkflowStep](../APIReference/API_UpdateWorkflowStep.md "../APIReference/API_UpdateWorkflowStep.md") API operation to update the steps in a step
group.

###### Important

You can only update steps that you have added to a migration workflow that isn't running or
paused.

## Deleting step groups

You can delete step groups using the Migration Hub Orchestrator console or the AWS CLI.

Console
You can only delete step groups when the following conditions are met:

- The workflow has a **Status** of **Not started** or
  **Paused**.
- The step group has a **Status** of **Awaiting
  dependencies**.
- The step group has a **Managed by** value of
  **Custom**.

###### To delete step groups

1. Sign in to the AWS Management Console and access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, select the workflow that you want to
   customize and choose **View details**.
4. In the **Steps** pane, select the step group to delete.
5. Choose **Actions**, **Delete step group**.
6. Enter `delete` and choose **Delete** to
   proceed.

AWS CLI
You can use the [DeleteWorkflowStepGroup](../APIReference/API_DeleteWorkflowStepGroup.md "../APIReference/API_DeleteWorkflowStepGroup.md") API operation to delete step groups in a
workflow.

## Deleting steps

You can delete steps using the Migration Hub Orchestrator console or the AWS CLI.

Console
You can only delete steps when the following conditions are met:

- The workflow has a **Status** of **Not started** or
  **Paused**.
- The step has a **Status** of **Awaiting
  dependencies**.
- The step has a **Managed by** value of
  **Custom**.

###### To delete steps

1. Sign in to the AWS Management Console and access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, select the workflow that you want to
   customize and choose **View details**.
4. In the **Steps** pane, select the step group that contains the step to
   delete.
5. Choose **Expand all** to view the steps within the step group.
6. Select the step to delete.
7. Choose **Actions**, **Delete step**.
8. Enter `delete` and choose **Delete** to
   proceed.

AWS CLI
You can use the [DeleteWorkflowStep](../APIReference/API_DeleteWorkflowStep.md "../APIReference/API_DeleteWorkflowStep.md") API operation to delete steps in a step
group.

## Running workflows

For guidance on running a migration workflow, refer to the documentation for the template
that was used. For more information on the available templates, see [Migration Hub Orchestrator templates](templates.md "templates.md").

## Pausing workflows

You can pause a running migration workflow using the Migration Hub Orchestrator console or the AWS CLI. You can
only pause a running workflow.

Console

###### To pause a running workflow

1. Sign in to the AWS Management Console and access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, select the workflow that you want to
   pause.
4. Choose **Actions**, **Pause**.

AWS CLI
You can use the [UpdateWorkflow](../APIReference/API_UpdateWorkflow.md "../APIReference/API_UpdateWorkflow.md") API operation to pause a workflow.

## Deleting workflows

You can delete migration workflows using the Migration Hub Orchestrator console or the AWS CLI. The workflow must
have a **Status** of **Not started**,
**Paused**, or **Failed**.

Console

###### To delete a migration workflow

1. Sign in to the AWS Management Console and access the Migration Hub Orchestrator console at [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, under **Orchestrate**, choose
   **Workflows**.
3. On the **Workflows** page, select the workflow that you want to
   delete.
4. Choose **Actions**, **Delete**.
5. Enter `delete` and choose **Delete** to
   proceed.

AWS CLI
You can use the [DeleteWorkflow](../APIReference/API_DeleteWorkflow.md "../APIReference/API_DeleteWorkflow.md") API operation to delete a paused or failed
workflow.
