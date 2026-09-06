

# AWS CodePipeline in AWS GovCloud (US)
<a name="govcloud-acp"></a>

AWS CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software. You can quickly model and configure the different stages of a software release process. CodePipeline automates the steps required to release your software changes continuously.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How AWS CodePipeline differs
<a name="govcloud-acp-diffs"></a>

The following differences apply to AWS CodePipeline:
+ Custom actions are not available.
+ Source Actions. The following actions are only available in AWS GovCloud (US-East):
  +  AWS CodeStar Source Connection (Bitbucket Cloud)
  +  AWS CodeStar Source Connection (GitHub)
  +  AWS CodeStar Source Connection (GitHub Enterprise Server)
  +  AWS CodeStar﻿ Source Connection (GitLab.com)
+ Build Actions:
  + Jenkins
  + For the CodeBuild action, enabling batch builds is not available. For the CodeBuild action type, the action configuration does not contain the following parameters : BatchEnabled, CombineArtifacts.
+ Test Actions:
  +  Device Farm 
  + Jenkins
+ Deploy Actions:
  +  OpsWorks 
  + Amazon Alexa
  + AWS AppConfig (Supported in CLI, not supported in console)
  + AWS CloudFormation StackSets
+ Invoke Actions:
  +  AWS Step Functions 
+ Since AWS GovCloud (US) operates as isolated regions, you cannot share or use CodePipeline resources with other services outside of the Regions. For example, you cannot use a CodeCommit repository in AWS GovCloud (US-West) as the source for a pipeline in CodePipeline that is not in the AWS GovCloud (US-West) Region.
+ All policy statements must refer to the GovCloud ARNs for the AWS GovCloud (US) Region. For example, policies for AWS Artifact buckets, CloudWatch Events rules, and trigger resources must use the AWS GovCloud (US) ARNs for those services. For more information, see [Amazon Resource Names in AWS GovCloud (US)](https://docs.aws.amazon.com/general/latest/gr/arns.html).
+ All users and service roles must exist in the AWS GovCloud (US) Region.
+ Cross-region actions such as multi-region deployment are not available.

## Documentation
<a name="govcloud-acp-docs"></a>
+  [AWS CodePipeline documentation](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) 

## Export-controlled content
<a name="govcloud-acp-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Pipeline Name
+ Stage Name
+ Action Name
+ CodeCommit Branch Name
+ GitHub Branch Name