# Action structure reference

This section is a reference for action configuration only. For a conceptual overview of the
pipeline structure, see [CodePipeline pipeline structure reference](reference-pipeline-structure.md "reference-pipeline-structure.md").

Each action provider in CodePipeline uses a set of required and optional configuration fields in
the pipeline structure. This section provides the following reference information by action
provider:

- Valid values for the `ActionType` fields included in the pipeline structure
  action block, such as `Owner` and `Provider`.
- Descriptions and other reference information for the `Configuration`
  parameters (required and optional) included in the pipeline structure action section.
- Valid example JSON and YAML action fields.
  This section is updated periodically with more action providers. Reference information is
  currently available for the following action providers:

###### Topics

- [Amazon EC2 action reference](action-reference-EC2Deploy.md "action-reference-EC2Deploy.md")
- [Amazon ECR source action reference](action-reference-ECR.md "action-reference-ECR.md")
- [ECRBuildAndPublish build action reference](action-reference-ECRBuildAndPublish.md "action-reference-ECRBuildAndPublish.md")
- [Amazon ECS and CodeDeploy blue-green deploy action reference](action-reference-ECSbluegreen.md "action-reference-ECSbluegreen.md")
- [Amazon Elastic Container Service deploy action reference](action-reference-ECS.md "action-reference-ECS.md")
- [Amazon Elastic Kubernetes Service EKS deploy action reference](action-reference-EKS.md "action-reference-EKS.md")
- [AWS Lambda deploy action reference](action-reference-LambdaDeploy.md "action-reference-LambdaDeploy.md")
- [Amazon S3 deploy action reference](action-reference-S3Deploy.md "action-reference-S3Deploy.md")
- [Amazon S3 source action reference](action-reference-S3.md "action-reference-S3.md")
- [AWS AppConfig deploy action reference](action-reference-AppConfig.md "action-reference-AppConfig.md")
- [CloudFormation deploy action reference](action-reference-CloudFormation.md "action-reference-CloudFormation.md")
- [CloudFormation StackSets](action-reference-StackSets.md "action-reference-StackSets.md")
- [AWS CodeBuild build and test action reference](action-reference-CodeBuild.md "action-reference-CodeBuild.md")
- [AWS CodePipeline invoke action reference](action-reference-PipelineInvoke.md "action-reference-PipelineInvoke.md")
- [AWS CodeCommit source action reference](action-reference-CodeCommit.md "action-reference-CodeCommit.md")
- [AWS CodeDeploy deploy action reference](action-reference-CodeDeploy.md "action-reference-CodeDeploy.md")
- [CodeStarSourceConnection for Bitbucket Cloud, GitHub, GitHub Enterprise Server,
  GitLab.com, and GitLab self-managed actions](action-reference-CodestarConnectionSource.md "action-reference-CodestarConnectionSource.md")
- [Commands action reference](action-reference-Commands.md "action-reference-Commands.md")
- [AWS Device Farm test action reference](action-reference-DeviceFarm.md "action-reference-DeviceFarm.md")
- [Elastic Beanstalk deploy action reference](action-reference-Beanstalk.md "action-reference-Beanstalk.md")
- [Amazon Inspector InspectorScan invoke action reference](action-reference-InspectorScan.md "action-reference-InspectorScan.md")
- [AWS Lambda invoke action reference](action-reference-Lambda.md "action-reference-Lambda.md")
- [AWS OpsWorks deploy action reference](action-reference-OpsWorks.md "action-reference-OpsWorks.md")
- [AWS Service Catalogdeploy action reference](action-reference-ServiceCatalog.md "action-reference-ServiceCatalog.md")
- [AWS Step Functions](action-reference-StepFunctions.md "action-reference-StepFunctions.md")
