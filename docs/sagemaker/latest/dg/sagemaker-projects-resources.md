

# View Project Resources
<a name="sagemaker-projects-resources"></a>

After you create a project, view the resources associated with the project in Amazon SageMaker Studio Classic.

------
#### [ Studio ]

1. Open the SageMaker Studio console by following the instructions in [Launch Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-launch.html).

1. In the left navigation pane, choose **Deployments**, and then choose **Projects**.

1. Select the name of the project for which you want to view details. A page with the project details appears.

On the project details page, you can view the following entities can open any of the following tabs corresponding to the entity associated with the project.
+ Repositories: Code repositories (repos) associated with this project. If you use a SageMaker AI-provided template when you create your project, it creates a AWS CodeCommit repo or a third-party Git repo. For more information about CodeCommit, see [What is AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html).
+ Pipelines: SageMaker AI ML pipelines that define steps to prepare data, train, and deploy models. For information about SageMaker AI ML pipelines, see [Pipelines actions](pipelines-build.md).
+ Experiments: One or more Amazon SageMaker Autopilot experiments associated with the project. For information about Autopilot, see [SageMaker Autopilot](autopilot-automate-model-development.md).
+ Model groups: Groups of model versions that were created by pipeline executions in the project. For information about model groups, see [Create a Model Group](model-registry-model-group.md).
+ Endpoints: SageMaker AI endpoints that host deployed models for real-time inference. When a model version is approved, it is deployed to an endpoint.
+ Tags: All the tags associated with the project. For more information about tags, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.
+ Metadata: Metadata associated with the project. This includes the template and version used, and the template launch path.

------
#### [ Studio Classic ]

1. Sign in to Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

1. In the Studio Classic sidebar, choose the **Home** icon ( ![](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Select **Deployments** from the menu, and then select **Projects**.

1. Select the name of the project for which you want to view details.

   A tab with the project details appears.

On the project details tab, you can view the following entities associated with the project.
+ Repositories: Code repositories (repos) associated with this project. If you use a SageMaker AI-provided template when you create your project, it creates a AWS CodeCommit repo or a third-party Git repo. For more information about CodeCommit, see [What is AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html).
+ Pipelines: SageMaker AI ML pipelines that define steps to prepare data, train, and deploy models. For information about SageMaker AI ML pipelines, see [Pipelines actions](pipelines-build.md).
+ Experiments: One or more Amazon SageMaker Autopilot experiments associated with the project. For information about Autopilot, see [SageMaker Autopilot](autopilot-automate-model-development.md).
+ Model groups: Groups of model versions that were created by pipeline executions in the project. For information about model groups, see [Create a Model Group](model-registry-model-group.md).
+ Endpoints: SageMaker AI endpoints that host deployed models for real-time inference. When a model version is approved, it is deployed to an endpoint.
+ Settings: Settings for the project. This includes the name and description of the project, information about the project template and `SourceModelPackageGroupName`, and metadata about the project.

------