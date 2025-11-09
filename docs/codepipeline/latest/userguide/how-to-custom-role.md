# Manage the CodePipeline service role

The CodePipeline service role is configured with one or more policies that control
access to the AWS resources used by the pipeline. You might want to attach more
policies to this role, edit the policy attached to the role, or configure policies for
other service roles in AWS. You might also want to attach a policy to a role when you
configure cross-account access to your pipeline.

###### Important

Modifying a policy statement or attaching another policy to the role can prevent
your pipelines from functioning. Be sure that you understand the implications before
you modify the service role for CodePipeline in any way. Make sure you test your
pipelines after you make any change to the service role.

###### Note

In the console, service roles created before September 2018 are created with the
name
`oneClick_AWS-CodePipeline-Service_`ID-Number``.

Service roles created after September 2018 use the service role name format
`AWSCodePipelineServiceRole-`Region`-`Pipeline_Name``.
 For example, for a pipeline named `MyFirstPipeline`in
`eu-west-2`, the console names the role and policy
 `AWSCodePipelineServiceRole-eu-west-2-MyFirstPipeline`.

## CodePipeline service role policy

The CodePipeline service role policy statement contains the minimum permissions for
managing pipelines. You can edit the service role statement to remove or add access
to resources you do not use. See the appropriate action reference for the minimum
required permissions CodePipeline uses for each action.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowS3BucketAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketVersioning",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::[[pipeArtifactBucketNames]]"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "{{accountId}}"
 }
 }
 },
 {
 "Sid": "AllowS3ObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:PutObjectTagging",
 "s3:GetObjectTagging",
 "s3:GetObjectVersionTagging"
 ],
 "Resource": [
 "arn:aws:s3:::[[pipeArtifactBucketNames]]/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "{{accountId}}"
 }
 }
 }
 ]
}`

```

###### Note

In the policy, the following permissions are required when the S3 objects in
your source bucket have tags in them:

```
s3:PutObjectTagging
s3:GetObjectTagging
s3:GetObjectVersionTagging
```

## Remove permissions from the CodePipeline

service role

You can edit the service role statement to remove access to resources you do not
use. For example, if none of your pipelines include Elastic Beanstalk, you can edit the policy
statement to remove the section that grants access to Elastic Beanstalk resources.

Similarly, if none of your pipelines includes CodeDeploy, you can edit the policy
statement to remove the section that grants access to CodeDeploy resources:

```
    {
    "Action": [
        "codedeploy:CreateDeployment",
        "codedeploy:GetApplicationRevision",
        "codedeploy:GetDeployment",
        "codedeploy:GetDeploymentConfig",
        "codedeploy:RegisterApplicationRevision"
    ],
    "Resource": "*",
    "Effect": "Allow"
},
```

## Add permissions to the CodePipeline

service role

You must update your service role policy statement with permissions for an
AWS service not already included in the default service role policy statement
before you can use it in your pipelines.

This is especially important if the service role you use for your pipelines was
created before support was added to CodePipeline for an AWS service.

The following table shows when support was added for other AWS services.

| AWS service                                                                                                                                                                                                                                                                                                                                                                                                             | CodePipeline support date                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| CodePipeline invoke action support added. See [Service role policy<br>permissions for the CodePipeline invoke action](action-reference-PipelineInvoke.md#action-reference-PipelineInvoke-permissions-action "action-reference-PipelineInvoke.md#action-reference-PipelineInvoke-permissions-action").                                                                                                                   | March 14, 2025                                                                      |
| `EC2` action support added. See [Service role policy<br>permissions for the EC2 deploy action](action-reference-EC2Deploy.md#action-reference-EC2Deploy-permissions-action "action-reference-EC2Deploy.md#action-reference-EC2Deploy-permissions-action").                                                                                                                                                              | February 21, 2025                                                                   |
| `EKS` action support added. See [Service role policy<br>permissions](action-reference-EKS.md#action-reference-EKS-service-role "action-reference-EKS.md#action-reference-EKS-service-role").                                                                                                                                                                                                                            | February 20, 2025                                                                   |
| Amazon Elastic Container Registry `ECRBuildAndPublish` action support added.<br>See [Service role permissions:<br>ECRBuildAndPublish action](action-reference-ECRBuildAndPublish.md#edit-role-ECRBuildAndPublish "action-reference-ECRBuildAndPublish.md#edit-role-ECRBuildAndPublish").                                                                                                                                | November 22, 2024                                                                   |
| Amazon Inspector `InspectorScan` action support added. See<br>[Service role permissions:<br>InspectorScan action](action-reference-InspectorScan.md#edit-role-InspectorScan "action-reference-InspectorScan.md#edit-role-InspectorScan").                                                                                                                                                                               | November 22, 2024                                                                   |
| Commands action support added. See [Service role permissions: Commands action](action-reference-Commands.md#edit-role-Commands "action-reference-Commands.md#edit-role-Commands").                                                                                                                                                                                                                                      | October 03, 2024                                                                    |
| AWS CloudFormation action support added. See [Service role permissions:<br>CloudFormationStackSet action](action-reference-StackSets.md#edit-role-cfn-stackset "action-reference-StackSets.md#edit-role-cfn-stackset") and [Service role permissions:<br>CloudFormationStackInstances action](action-reference-StackSets.md#edit-role-cfn-stackinstances "action-reference-StackSets.md#edit-role-cfn-stackinstances"). | December 30, 2020                                                                   |
| CodeCommit full clone output artifact format action support added. See<br>[Service role permissions: CodeCommit action](action-reference-CodeCommit.md#edit-role-codecommit "action-reference-CodeCommit.md#edit-role-codecommit").                                                                                                                                                                                     | November 11, 2020                                                                   |
| CodeBuild batch builds action support added. See [Service role permissions: CodeCommit action](action-reference-CodeCommit.md#edit-role-codecommit "action-reference-CodeCommit.md#edit-role-codecommit").                                                                                                                                                                                                              | July 30, 2020                                                                       |
| AWS AppConfig action support added. See [Service role permissions:<br>AppConfig action](action-reference-AppConfig.md#edit-role-appconfig "action-reference-AppConfig.md#edit-role-appconfig").                                                                                                                                                                                                                         | June 22, 2020                                                                       |
| AWS Step Functions action support added. See [Service role permissions:<br>StepFunctions action](action-reference-StepFunctions.md#edit-role-stepfunctions "action-reference-StepFunctions.md#edit-role-stepfunctions").                                                                                                                                                                                                | May 27, 2020                                                                        |
| AWS CodeStar Connections action support added. See [Service role permissions: CodeConnections<br>action](action-reference-CodestarConnectionSource.md#edit-role-connections "action-reference-CodestarConnectionSource.md#edit-role-connections").                                                                                                                                                                      | December 18, 2019                                                                   |
| S3 deploy action support added. See [Service role permissions: S3 deploy action](action-reference-S3Deploy.md#edit-role-s3deploy "action-reference-S3Deploy.md#edit-role-s3deploy").                                                                                                                                                                                                                                    | January 16, 2019                                                                    |
| The `CodeDeployToECS` action action support added. See<br>[Service role permissions:<br>CodeDeployToECS action](action-reference-ECSbluegreen.md#edit-role-codedeploy-ecs "action-reference-ECSbluegreen.md#edit-role-codedeploy-ecs").                                                                                                                                                                                 | November 27, 2018                                                                   |
| Amazon ECR action support added. See [Service role permissions: Amazon ECR action](action-reference-ECR.md#edit-role-ecr "action-reference-ECR.md#edit-role-ecr").                                                                                                                                                                                                                                                      | November 27, 2018                                                                   |
| Service Catalog action support added. See [Service role permissions: Service Catalog action](action-reference-ServiceCatalog.md#edit-role-servicecatalog "action-reference-ServiceCatalog.md#edit-role-servicecatalog").                                                                                                                                                                                                | October 16, 2018                                                                    |
| AWS Device Farm action support added. See [Service role permissions: AWS Device Farm<br>action](action-reference-DeviceFarm.md#edit-role-devicefarm "action-reference-DeviceFarm.md#edit-role-devicefarm").                                                                                                                                                                                                             | July 19, 2018                                                                       |
| Amazon ECS action support added. See [Service role permissions: Amazon ECS standard action](action-reference-ECS.md#edit-role-ecs "action-reference-ECS.md#edit-role-ecs").                                                                                                                                                                                                                                             | December 12, 2017 / Update for opt in for tagging authorization<br>on July 21, 2017 |
| CodeCommit action support added. See [Service role permissions: CodeCommit action](action-reference-CodeCommit.md#edit-role-codecommit "action-reference-CodeCommit.md#edit-role-codecommit").                                                                                                                                                                                                                          | April 18, 2016                                                                      |
| AWS OpsWorks action support added. See [Service role permissions: AWS OpsWorks action](action-reference-OpsWorks.md#edit-role-opsworks "action-reference-OpsWorks.md#edit-role-opsworks").                                                                                                                                                                                                                              | June 2, 2016                                                                        |
| AWS CloudFormation action support added. See [Service role permissions: AWS CloudFormation<br>action](action-reference-CloudFormation.md#edit-role-cloudformation "action-reference-CloudFormation.md#edit-role-cloudformation").                                                                                                                                                                                       | November 3, 2016                                                                    |
| AWS CodeBuild action support added. See [Service role permissions: CodeBuild action](action-reference-CodeBuild.md#edit-role-codebuild "action-reference-CodeBuild.md#edit-role-codebuild").                                                                                                                                                                                                                            | December 1, 2016                                                                    |
| Elastic Beanstalk action support added. See [Service role permissions:<br>ElasticBeanstalk deploy action](action-reference-Beanstalk.md#edit-role-beanstalk "action-reference-Beanstalk.md#edit-role-beanstalk").                                                                                                                                                                                                       | Initial service launch                                                              |
| CodeDeploy action support added. See [Service role permissions: AWS CodeDeploy action](action-reference-CodeDeploy.md#edit-role-codedeploy "action-reference-CodeDeploy.md#edit-role-codedeploy").                                                                                                                                                                                                                      | Initial service launch                                                              |
| S3 source action support added. See [Service role permissions: S3 source action](action-reference-S3.md#edit-role-s3source "action-reference-S3.md#edit-role-s3source").                                                                                                                                                                                                                                                | Initial service launch                                                              |

Follow these steps to add permissions for a supported service:

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the IAM console, in the navigation pane, choose
   **Roles**, and then choose your
   `AWS-CodePipeline-Service` role from the list of
   roles.
3. On the **Permissions** tab, in **Inline policies**, in the row for your service role policy,
   choose **Edit Policy**.
4. Add the required permissions in the **Policy document**
   box.

###### Note

When you create IAM policies, follow the standard security advice of
granting least privilege—that is, granting only the permissions required
to perform a task. Some API calls support resource-based permissions and
allow access to be limited. For example, in this case, to limit
permissions when calling `DescribeTasks` and
`ListTasks`, you can replace the wildcard character (\*)
with a resource ARN or with a resource ARN that contains a wildcard
character (\*). For more information about creating a policy that grants
least-privilege access, see [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege"). 5. Choose **Review policy** to ensure the policy
contains no errors. When the policy is error-free, choose **Apply policy**.
