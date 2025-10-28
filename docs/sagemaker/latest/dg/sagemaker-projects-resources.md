# View Project Resources

After you create a project, view the resources associated with the project in
Amazon SageMaker Studio Classic.

Studio

1. Open the SageMaker Studio console by following the instructions in [Launch
   Amazon SageMaker Studio](studio-updated-launch.md "studio-updated-launch.md").
2. In the left navigation pane, choose **Deployments**, and then
   choose **Projects**.
3. Select the name of the project for which you want to view details.
   A page with the project details appears.

On the project details page, you can view the following entities can open any of the following tabs
corresponding to the entity associated with the project.

- Repositories: Code repositories (repos) associated with this project. If you
  use a SageMaker AI-provided template when you create your project, it creates a
  AWS CodeCommit repo or a third-party Git repo. For more information about CodeCommit, see
  [What is AWS CodeCommit](../../../codecommit/latest/userguide/welcome.md "../../../codecommit/latest/userguide/welcome.md").
- Pipelines: SageMaker AI ML pipelines that define steps to prepare data, train, and
  deploy models. For information about SageMaker AI ML pipelines, see [Pipelines actions](pipelines-build.md "pipelines-build.md").
- Experiments: One or more Amazon SageMaker Autopilot experiments associated with the project. For
  information about Autopilot, see [SageMaker Autopilot](autopilot-automate-model-development.md "autopilot-automate-model-development.md").
- Model groups: Groups of model versions that were created by pipeline
  executions in the project. For information about model groups, see [Create a Model Group](model-registry-model-group.md "model-registry-model-group.md").
- Endpoints: SageMaker AI endpoints that host deployed models for real-time inference.
  When a model version is approved, it is deployed to an endpoint.
- Tags: All the tags associated with the project. For more information about
  tags, see [Tagging AWS
  resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the
  _AWS General Reference_.
- Metadata: Metadata associated with the project. This includes the template
  and version used, and the template launch path.

Studio Classic

1. Sign in to Studio Classic. For more information, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").
2. In the Studio Classic sidebar, choose the **Home** icon (
   ![Black square icon representing a placeholder or empty image.](images/studio/icons/house.png)
   ).
3. Select **Deployments** from the menu, and then
   select **Projects**.
4. Select the name of the project for which you want to view
   details.

A tab with the project details appears.

On the project details tab, you can view the following entities associated with the
project.

- Repositories: Code repositories (repos) associated with this project. If you
  use a SageMaker AI-provided template when you create your project, it creates a
  AWS CodeCommit repo or a third-party Git repo. For more information about CodeCommit, see
  [What is AWS CodeCommit](../../../codecommit/latest/userguide/welcome.md "../../../codecommit/latest/userguide/welcome.md").
- Pipelines: SageMaker AI ML pipelines that define steps to prepare data, train, and
  deploy models. For information about SageMaker AI ML pipelines, see [Pipelines actions](pipelines-build.md "pipelines-build.md").
- Experiments: One or more Amazon SageMaker Autopilot experiments associated with the project. For
  information about Autopilot, see [SageMaker Autopilot](autopilot-automate-model-development.md "autopilot-automate-model-development.md").
- Model groups: Groups of model versions that were created by pipeline
  executions in the project. For information about model groups, see [Create a Model Group](model-registry-model-group.md "model-registry-model-group.md").
- Endpoints: SageMaker AI endpoints that host deployed models for real-time inference.
  When a model version is approved, it is deployed to an endpoint.
- Settings: Settings for the project. This includes the name and description of
  the project, information about the project template and
  `SourceModelPackageGroupName`, and metadata about the
  project.
