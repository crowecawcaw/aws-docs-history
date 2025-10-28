# AWS CodeDeploy deploy action reference

You use an AWS CodeDeploy action to deploy application code to your deployment fleet. Your
deployment fleet can consist of Amazon EC2 instances, on-premises instances, or both.

###### Note

This reference topic describes the CodeDeploy deployment action for CodePipeline where the
deployment platform is Amazon EC2. For reference information about Amazon Elastic Container Service to CodeDeploy
blue/green deployment actions in CodePipeline, see [Amazon Elastic Container Service and CodeDeploy blue-green deploy action reference](action-reference-ECSbluegreen.md "action-reference-ECSbluegreen.md").

###### Topics

- [Action type](#action-reference-CodeDeploy-type "#action-reference-CodeDeploy-type")
- [Configuration parameters](#action-reference-CodeDeploy-config "#action-reference-CodeDeploy-config")
- [Input artifacts](#action-reference-CodeDeploy-input "#action-reference-CodeDeploy-input")
- [Output artifacts](#action-reference-CodeDeploy-output "#action-reference-CodeDeploy-output")
- [Service role permissions: AWS CodeDeploy action](#edit-role-codedeploy "#edit-role-codedeploy")
- [Action declaration](#action-reference-CodeDeploy-example "#action-reference-CodeDeploy-example")
- [See also](#action-reference-CodeDeploy-links "#action-reference-CodeDeploy-links")

## Action type

- Category: `Deploy`
- Owner: `AWS`
- Provider: `CodeDeploy`
- Version: `1`

## Configuration parameters

**ApplicationName**

Required: Yes

The name of the application that you created in CodeDeploy.

**DeploymentGroupName**

Required: Yes

The deployment group that you created in CodeDeploy.

## Input artifacts

- **Number of artifacts:**
  `1`
- **Description:** The AppSpec file that CodeDeploy uses
  to determine:

      + What to install onto your instances from your application revision in
       Amazon S3 or GitHub.
      + Which lifecycle event hooks to run in response to deployment lifecycle
       events.

  For more information about the AppSpec file, see the [CodeDeploy AppSpec File
  Reference](../../../codedeploy/latest/userguide/reference-appspec-file.md "../../../codedeploy/latest/userguide/reference-appspec-file.md").

## Output artifacts

- **Number of artifacts:**
  `0`
- **Description:** Output artifacts do not apply
  for this action type.

## Service role permissions: AWS CodeDeploy action

For AWS CodeDeploy support, add the following to your policy statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codedeploy:CreateDeployment",
 "codedeploy:GetApplication",
 "codedeploy:GetDeployment",
 "codedeploy:RegisterApplicationRevision",
 "codedeploy:ListDeployments",
 "codedeploy:ListDeploymentGroups",
 "codedeploy:GetDeploymentGroup"
 ],
 "Resource": [
 "arn:aws:codedeploy:*:`111122223333`:application:[[codedeployApplications]]",
 "arn:aws:codedeploy:*:`111122223333`:deploymentgroup:[[codedeployApplications]]/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "codedeploy:GetDeploymentConfig"
 ],
 "Resource": [
 "arn:aws:codedeploy:*:`111122223333`:deploymentconfig:[[deploymentConfigs]]"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "codedeploy:ListDeploymentConfigs"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Action declaration

YAML

```
Name: Deploy
Actions:
  - Name: Deploy
    ActionTypeId:
      Category: Deploy
      Owner: AWS
      Provider: CodeDeploy
      Version: '1'
    RunOrder: 1
    Configuration:
      ApplicationName: my-application
      DeploymentGroupName: my-deployment-group
    OutputArtifacts: []
    InputArtifacts:
      - Name: SourceArtifact
    Region: us-west-2
    Namespace: DeployVariables

```

JSON

```
{
    "Name": "Deploy",
    "Actions": [
        {
            "Name": "Deploy",
            "ActionTypeId": {
                "Category": "Deploy",
                "Owner": "AWS",
                "Provider": "CodeDeploy",
                "Version": "1"
            },
            "RunOrder": 1,
            "Configuration": {
                "ApplicationName": "my-application",
                "DeploymentGroupName": "my-deployment-group"
            },
            "OutputArtifacts": [],
            "InputArtifacts": [
                {
                    "Name": "SourceArtifact"
                }
            ],
            "Region": "us-west-2",
            "Namespace": "DeployVariables"
        }
    ]
},
```

## See also

The following related resources can help you as you work with this action.

- [Tutorial: Create a simple pipeline (S3 bucket)](tutorials-simple-s3.md "tutorials-simple-s3.md")
  – This tutorial walks you through the creation of a source bucket, EC2
  instances, and CodeDeploy resources to deploy a sample application. You then build
  your pipeline with a CodeDeploy deployment action that deploys code maintained in
  your S3 bucket to your Amazon EC2 instance.
- [Tutorial: Create a simple pipeline (CodeCommit
  repository)](tutorials-simple-codecommit.md "tutorials-simple-codecommit.md") – This tutorial walks
  you through the creation of your CodeCommit source repository, EC2 instances, and
  CodeDeploy resources to deploy a sample application. You then build your pipeline
  with a CodeDeploy deployment action that deploys code from your CodeCommit repository to
  your Amazon EC2 instance.
- [CodeDeploy AppSpec File
  Reference](../../../codedeploy/latest/userguide/reference-appspec-file.md "../../../codedeploy/latest/userguide/reference-appspec-file.md") – This reference chapter in the
  _AWS CodeDeploy User Guide_ provides reference information and
  examples for CodeDeploy AppSpec files.
