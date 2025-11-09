# AWS CodePipeline in AWS GovCloud (US)

AWS CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software. You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.

## How AWS CodePipeline differs for AWS GovCloud (US)

The following actions/provider types are not supported:

- Custom actions
- Source Actions. The following actions are only available in AWS GovCloud (US-East):
  - AWS CodeStar Source Connection (Bitbucket Cloud)
  - AWS CodeStar Source Connection (GitHub)
  - AWS CodeStar Source Connection (GitHub Enterprise Server)
  - AWS CodeStar﻿ Source Connection (GitLab.com)

- Build Actions:
  - Jenkins
  - For the CodeBuild action, enabling batch builds is not supported. For the CodeBuild action type, the action configuration does not contain the following parameters : BatchEnabled, CombineArtifacts.

- Test Actions:
  - Device Farm
  - Jenkins

- Deploy Actions:
  - OpsWorks
  - Amazon Alexa
  - AWS AppConfig (Supported in CLI, not supported in console)
  - AWS CloudFormation StackSets

- Invoke Actions:
  - AWS Step Functions

- Since AWS GovCloud (US) operates as isolated regions, you cannot share or use CodePipeline resources with other services outside of the Regions. For example, you cannot use a CodeCommit repository in AWS GovCloud (US-West) as the source for a pipeline in CodePipeline that is not in the AWS GovCloud (US-West) Region.
- All policy statements must refer to the GovCloud ARNs for the AWS GovCloud (US) Region. For example, policies for AWS Artifact buckets, CloudWatch Events rules, and trigger resources must use the AWS GovCloud (US) ARNs for those services. For more information, see .
- All users and service roles must exist in the AWS GovCloud (US) Region.
- Cross-region actions such as multi-region deployment are not supported.

## Documentation for AWS CodePipeline

[AWS CodePipeline documentation](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Pipeline Name
- Stage Name
- Action Name
- CodeCommit Branch Name
- GitHub Branch Name
