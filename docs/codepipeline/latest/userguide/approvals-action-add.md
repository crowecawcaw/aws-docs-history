# Add a manual approval action to a pipeline in

CodePipeline

You can add an approval action to a stage in a CodePipeline pipeline at the point where you
want the pipeline to stop so someone can manually approve or reject the action.

###### Note

Approval actions can't be added to Source stages. Source stages can contain only
source actions.

If you want to use Amazon SNS to send notifications when an approval action is ready for
review, you must first complete the following prerequisites:

- Grant permission to your CodePipeline service role to access Amazon SNS resources. For
  information, see [Grant Amazon SNS permissions to a CodePipeline
  service role](approvals-service-role-permissions.md "approvals-service-role-permissions.md").
- Grant permission to one or more IAM identities in your organization to update
  the status of an approval action. For information, see [Grant approval permissions to an IAM user
  in CodePipeline](approvals-iam-permissions.md "approvals-iam-permissions.md").
  In this example, you create a new approval stage and add a manual approval action to
  the stage. You can also add a manual approval action to an existing stage that contains
  other actions.

## Add a manual approval action to a

CodePipeline pipeline (console)

You can use the CodePipeline console to add an approval action to an existing CodePipeline
pipeline. You must use the AWS CLI if you want to add approval actions when you
create a new pipeline.

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. In **Name**, choose the pipeline.
3. On the pipeline details page, choose **Edit**.
4. If you want to add an approval action to a new stage, choose **+
   Add stage** at the point in the pipeline where you want to add
   an approval request, and enter a name for the stage. On the **Add
   stage** page, in **Stage name**, enter your
   new stage name. For example, add a new stage and name it
   `Manual_Approval`.

If you want to add an approval action to an existing stage, choose
**Edit stage**. 5. In the stage where you want to add the approval action, choose **+
Add action group**. 6. On the **Edit action** page, do the following:

    1. In **Action name**, enter a name to identify the
     action.
    2. In **Action provider**, under
     **Approval**, choose **Manual
     approval**.
    3. (Optional) In **SNS topic ARN**, choose the name
     of the topic to be used to send notifications for the approval
     action.
    4. (Optional) In **URL for review**, enter the URL
     of the page or application you want the approver to examine.
     Approvers can access this URL through a link included in the console
     view of the pipeline.
    5. (Optional) In **Comments**, enter any other
     information you want to share with the reviewer.
    6. Choose **Save**.

## Add a manual approval action to a CodePipeline

pipeline (CLI)

You can use the CLI to add an approval action to an existing pipeline or when you
create a pipeline. You do this by including an approval action, with the Manual
approval type, in a stage you are creating or editing.

For more information about creating and editing pipelines, see [Create a pipeline, stages, and actions](pipelines-create.md "pipelines-create.md") and [Edit a pipeline in CodePipeline](pipelines-edit.md "pipelines-edit.md").

To add a stage to a pipeline that includes only an approval action, you would
include something similar to the following example when you create or update the
pipeline.

###### Note

The `configuration` section is optional. This is just a portion,
not the entire structure, of the file. For more information, see [CodePipeline pipeline structure reference](reference-pipeline-structure.md "reference-pipeline-structure.md").

```
{
    "name": "`MyApprovalStage`",
    "actions": [
        {
            "name": "`MyApprovalAction`",
            "actionTypeId": {
                "category": "Approval",
                "owner": "AWS",
                "version": "1",
                "provider": "Manual"
            },
            "inputArtifacts": [],
            "outputArtifacts": [],
            "configuration": {
                "NotificationArn": "``arn:aws:sns:us-east-2:80398EXAMPLE:MyApprovalTopic``",
                "ExternalEntityLink": "`http://example.com`",
                "CustomData": "`The latest changes include feedback from Bob.`"},
            "runOrder": 1
        }
    ]
}
```

If the approval action is in a stage with other actions, the section of your JSON
file that contains the stage might look similar instead to the following
example.

###### Note

The `configuration` section is optional. This is just a portion,
not the entire structure, of the file. For more information, see [CodePipeline pipeline structure reference](reference-pipeline-structure.md "reference-pipeline-structure.md").

```
,
{
    "name": "`Production`",
    "actions": [
        {
            "inputArtifacts": [],
            "name": "`MyApprovalAction`",
            "actionTypeId": {
                "category": "Approval",
                "owner": "AWS",
                "version": "1",
                "provider": "Manual"
            },
            "outputArtifacts": [],
            "configuration": {
                "NotificationArn": "`arn:aws:sns:us-east-2:80398EXAMPLE:MyApprovalTopic`",
                "ExternalEntityLink": "`http://example.com`",
                "CustomData": "`The latest changes include feedback from Bob.`"
            },
            "runOrder": 1
        },
        {
            "inputArtifacts": [
                {
                    "name": "`MyApp`"
                }
            ],
            "name": "`MyDeploymentAction`",
            "actionTypeId": {
                "category": "Deploy",
                "owner": "AWS",
                "version": "1",
                "provider": "CodeDeploy"
            },
            "outputArtifacts": [],
            "configuration": {
                "ApplicationName": "`MyDemoApplication`",
                "DeploymentGroupName": "`MyProductionFleet`"
            },
            "runOrder": 2
        }
    ]
}
```
