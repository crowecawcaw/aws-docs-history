

# Valid action providers in CodePipeline
<a name="actions-valid-providers"></a>

The pipeline structure format is used to build actions and stages in a pipeline. An action type consists of an action category and provider type. 

Each action category has a valid list of action providers. To reference the valid action providers for each action category, see the [Action structure reference](action-reference.md). 

Each action category has a designated set of providers. Each action provider, such as Amazon S3, has a provider name, such as `S3`, that must be used in the `Provider` field in the action category in your pipeline structure. 

There are three valid values for the `Owner` field in the action category section in your pipeline structure: `AWS`, `ThirdParty`, and `Custom`.

To find the provider name and owner information for your action provider, see the [Action structure reference](action-reference.md) or [Valid input and output artifacts for each action type](reference-action-artifacts.md).

This table lists valid providers by action type.

**Note**  
For Bitbucket, GitHub, or GitHub Enterprise Server actions, refer to the [CodeStarSourceConnection for Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab self-managed actions](action-reference-CodestarConnectionSource.md) action reference topic.


**Valid action providers by action type**  


- **Source**
  - **Valid action providers:** Amazon S3 / **Pipeline type supported:** V1, V2 / **Action reference:** [Amazon S3 source action reference](action-reference-S3.md)
  - **Valid action providers:** Amazon ECR / **Pipeline type supported:** V1, V2 / **Action reference:** [Amazon ECR source action reference](action-reference-ECR.md)
  - **Valid action providers:** CodeCommit / **Pipeline type supported:** V1, V2 / **Action reference:** [CodeCommit source action reference](action-reference-CodeCommit.md)
  - **Valid action providers:** CodeStarSourceConnection (for Bitbucket, GitHub, GitHub Enterprise Server actions) / **Pipeline type supported:** V1, V2 / **Action reference:** [CodeStarSourceConnection for Bitbucket Cloud, GitHub, GitHub Enterprise Server, GitLab.com, and GitLab self-managed actions](action-reference-CodestarConnectionSource.md)

- **Build**
  - **Valid action providers:** Amazon ECR ECRBuildAndPublish action / **Pipeline type supported:** V2 only / **Action reference:** [`ECRBuildAndPublish` build action reference](action-reference-ECRBuildAndPublish.md)
  - **Valid action providers:** CodeBuild / **Pipeline type supported:** V1, V2 / **Action reference:** [AWS CodeBuild build and test action reference](action-reference-CodeBuild.md)
  - **Valid action providers:** Commands action (see Compute) / **Pipeline type supported:** V2 only / **Action reference:** 
  - **Valid action providers:** Custom CloudBees / **Pipeline type supported:** V1, V2 / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Custom Jenkins / **Pipeline type supported:** V1, V2 / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Custom TeamCity / **Pipeline type supported:** V1, V2 / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)

- **Test**
  - **Valid action providers:** CodeBuild / **Pipeline type supported:** V1, V2 / **Action reference:** [AWS CodeBuild build and test action reference](action-reference-CodeBuild.md)
  - **Valid action providers:** AWS Device Farm / **Pipeline type supported:** V1, V2 / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Custom BlazeMeter / **Pipeline type supported:** V1, V2 / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** ThirdParty GhostInspector / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Custom Jenkins / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** ThirdParty Micro Focus StormRunner Load / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** ThirdParty Nouvola / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** ThirdParty Runscope / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)

- **Deploy**
  - **Valid action providers:** Amazon S3 / **Pipeline type supported:**  / **Action reference:** [Amazon S3 deploy action reference](action-reference-S3Deploy.md)
  - **Valid action providers:** CloudFormation / **Pipeline type supported:**  / **Action reference:** [CloudFormation deploy action reference](action-reference-CloudFormation.md)
  - **Valid action providers:** CodeDeploy / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** EC2 Deploy action / **Pipeline type supported:** V2 only / **Action reference:** [Amazon EC2 action reference](action-reference-EC2Deploy.md)
  - **Valid action providers:** Amazon ECS / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Amazon ECS (Blue/Green) (this is the CodeDeployToECS action) / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Amazon EKS action / **Pipeline type supported:** V2 only / **Action reference:** [Amazon Elastic Kubernetes Service `EKS` deploy action reference](action-reference-EKS.md)
  - **Valid action providers:** Elastic Beanstalk / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** AWS AppConfig / **Pipeline type supported:**  / **Action reference:** [AWS AppConfig deploy action reference](action-reference-AppConfig.md)
  - **Valid action providers:** OpsWorks / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Service Catalog / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Amazon Alexa / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)
  - **Valid action providers:** Custom XebiaLabs / **Pipeline type supported:**  / **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)

- **Approval**
  - **Valid action providers:** Manual
  - **Pipeline type supported:** 
  - **Action reference:** [Valid input and output artifacts for each action type](reference-action-artifacts.md)

- **Invoke**
  - **Valid action providers:** CodePipeline Invoke action / **Pipeline type supported:**  / **Action reference:** [AWS CodePipeline invoke action reference](action-reference-PipelineInvoke.md)
  - **Valid action providers:** AWS Lambda / **Pipeline type supported:**  / **Action reference:** [AWS Lambda invoke action reference](action-reference-Lambda.md)
  - **Valid action providers:** AWS Step Functions / **Pipeline type supported:**  / **Action reference:** [AWS Step Functions invoke action reference](action-reference-StepFunctions.md) 
  - **Valid action providers:** InspectorScan / **Pipeline type supported:**  / **Action reference:** [Amazon Inspector `InspectorScan` invoke action reference](action-reference-InspectorScan.md)

- **Compute**
  - **Valid action providers:** Commands action
  - **Pipeline type supported:** 
  - **Action reference:** [Commands action reference](action-reference-Commands.md)



Some action types in CodePipeline are available in select AWS Regions only. It is possible that an action type is available in an AWS Region, but an AWS provider for that action type is not available.

For more information about each action provider, see [Integrations with CodePipeline action types](integrations-action-type.md). 