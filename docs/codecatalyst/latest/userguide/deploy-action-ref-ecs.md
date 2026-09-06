

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# 'Deploy to Amazon ECS' action YAML
<a name="deploy-action-ref-ecs"></a>

The following is the YAML definition of the **Deploy to Amazon ECS** action. To learn how to use this action, see [Deploying to Amazon ECS with a workflow](deploy-action-ecs.md).

This action definition exists as a section within a broader workflow definition file. For more information about this file, see [Workflow YAML definition](workflow-reference.md).

**Note**  
Most of the YAML properties that follow have corresponding UI elements in the visual editor. To look up a UI element, use **Ctrl\+F**. The element will be listed with its associated YAML property.

```
# The workflow definition starts here.
# See Top-level properties for details.
        
Name: MyWorkflow
SchemaVersion: 1.0 
Actions:

# The action definition starts here.   
  {{ECSDeployAction\_nn}}: 
    Identifier: aws/ecs-deploy@v1
    DependsOn:
      - {{build-action}}
    Compute:  
      Type: {{EC2 | Lambda}}
      Fleet: {{fleet-name}}
    Timeout: {{timeout-minutes}}
    Environment:
      Name: {{environment-name}}
      Connections:
        - Name: {{account-connection-name}}
          Role: {{iam-role-name}}
    Inputs:
      # Specify a source or an artifact, but not both.
      Sources:
        - {{source-name-1}}
      Artifacts:
        - {{task-definition-artifact}}
    Configuration: 
      region: {{us-east-1}} 
      cluster: {{ecs-cluster}}
      service: {{ecs-service}}
      task-definition: {{task-definition-path}}
      force-new-deployment: {{false|true}}
      codedeploy-appspec: {{app-spec-file-path}}
      codedeploy-application: {{application-name}}
      codedeploy-deployment-group: {{deployment-group-name}}
      codedeploy-deployment-description: {{deployment-description}}
```

## ECSDeployAction
<a name="deploy.action.ecs.name"></a>

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed. You cannot use quotation marks to enable special characters and spaces in action names.

Default: `ECSDeployAction_nn`.

Corresponding UI: Configuration tab/**Action display name**

## Identifier
<a name="deploy.action.ecs.identifier"></a>

({{ECSDeployAction}}/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version. For more information, see [Specifying the action version to use](workflows-action-versions.md).

Default: `aws/ecs-deploy@v1`.

Corresponding UI: Workflow diagram/ECSDeployAction\_nn/**aws/ecs-deploy@v1** label

## DependsOn
<a name="deploy.action.ecs.dependson"></a>

({{ECSDeployAction}}/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md).

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute
<a name="deploy.action.ecs.computename"></a>

({{ECSDeployAction}}/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level, but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow level, you can also run multiple actions on the same instance. For more information, see [Sharing compute across actions](compute-sharing.md).

Corresponding UI: *none*

## Type
<a name="deploy.action.ecs.computetype"></a>

({{ECSDeployAction}}/Compute/**Type**)

(Required if [Compute](#deploy.action.ecs.computename) is included)

The type of compute engine. You can use one of the following values:
+ **EC2** (visual editor) or `EC2` (YAML editor)

  Optimized for flexibility during action runs.
+ **Lambda** (visual editor) or `Lambda` (YAML editor)

  Optimized action start-up speeds.

For more information about compute types, see [Compute types](workflows-working-compute.md#compute.types).

Corresponding UI: Configuration tab/Advanced - optional/**Compute type**

## Fleet
<a name="deploy.action.ecs.computefleet"></a>

({{ECSDeployAction}}/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand).

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets).

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/Advanced - optional/**Compute fleet**

## Timeout
<a name="deploy.action.ecs.timeout"></a>

({{ECSDeployAction}}/**Timeout**)

(Optional)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor), that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md). The default timeout is the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional **

## Environment
<a name="deploy.action.ecs.environment"></a>

({{ECSDeployAction}}/**Environment**)

(Required)

Specify the CodeCatalyst environment to use with the action. The action connects to the AWS account and optional Amazon VPC specified in the chosen environment. The action uses the default IAM role specified in the environment to connect to the AWS account, and uses the IAM role specified in the [Amazon VPC connection](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.add.html) to connect to the Amazon VPC.

**Note**  
If the default IAM role does not have the permissions required by the action, you can configure the action to use a different role. For more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md).

For more information about environments, see [Deploying into AWS accounts and VPCs](deploy-environments.md) and [Creating an environment](deploy-environments-creating-environment.md).

Corresponding UI: Configuration tab/**Environment**

## Name
<a name="deploy.action.ecs.environment.name"></a>

({{ECSDeployAction}}/Environment/**Name**)

(Required if [Environment](#deploy.action.ecs.environment) is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration tab/**Environment**

## Connections
<a name="deploy.action.ecs.environment.connections"></a>

({{ECSDeployAction}}/Environment/**Connections**)

(Optional in newer versions of the action; required in older versions)

Specify the account connection to associate with the action. You can specify a maximum of one account connection under `Environment`.

If you do not specify an account connection:
+ The action uses the AWS account connection and default IAM role specified in the environment in the CodeCatalyst console. For information about adding an account connection and default IAM role to environment, see [Creating an environment](deploy-environments-creating-environment.md).
+ The default IAM role must include the policies and permissions required by the action. To determine what those policies and permissions are, see the description of the **Role** property in the action's YAML definition documentation.

For more information about account connections, see [Allowing access to AWS resources with connected AWS accounts](ipa-connect-account.md). For information about adding an account connection to an environment, see [Creating an environment](deploy-environments-creating-environment.md).

Corresponding UI: One of the following depending on the action version:
+ (Newer versions) Configuration tab/Environment/What's in {{my-environment}}?/three dot menu/**Switch role**
+ (Older versions) Configuration tab/'Environment/account/role'/**AWS account connection**

## Name
<a name="deploy.action.ecs.environment.connections.name"></a>

({{ECSDeployAction}}/Environment/Connections/**Name**)

(Required if [Connections](#deploy.action.ecs.environment.connections) is included)

Specify the name of the account connection.

Corresponding UI: One of the following depending on the action version:
+ (Newer versions) Configuration tab/Environment/What's in {{my-environment}}?/three dot menu/**Switch role**
+ (Older versions) Configuration tab/'Environment/account/role'/**AWS account connection**

## Role
<a name="deploy.action.ecs.environment.connections.role"></a>

({{ECSDeployAction}}/Environment/Connections/**Role**)

(Required if [Connections](#deploy.action.ecs.environment.connections) is included)

Specify the name of the IAM role that the **Deploy to Amazon ECS** action uses to access AWS. Make sure that you have [added the role to your CodeCatalyst space](ipa-connect-account-addroles.md), and that the role includes the following policies.

If you do not specify an IAM role, then the action uses the default IAM role listed in the [environment](deploy-environments.md) in the CodeCatalyst console. If you use the default role in the environment, make sure it has the following policies.
+ The following permissions policy:
**Warning**  
Limit the permissions to those shown in the following policy. Using a role with broader permissions might pose a security risk.

------
#### [ JSON ]

****  

  ```
  {
      "Version":"2012-10-17",		 	 	 
      "Statement": [{
      "Action":[
        "ecs:DescribeServices",
        "ecs:CreateTaskSet",
        "ecs:DeleteTaskSet",
        "ecs:ListClusters",
        "ecs:RegisterTaskDefinition",
        "ecs:UpdateServicePrimaryTaskSet",
        "ecs:UpdateService",
        "elasticloadbalancing:DescribeTargetGroups",
        "elasticloadbalancing:DescribeListeners",
        "elasticloadbalancing:ModifyListener",
        "elasticloadbalancing:DescribeRules",
        "elasticloadbalancing:ModifyRule",
        "lambda:InvokeFunction",
        "lambda:ListFunctions",
        "cloudwatch:DescribeAlarms",
        "sns:Publish",
        "sns:ListTopics", 
        "s3:GetObject",
        "s3:GetObjectVersion",
        "codedeploy:CreateApplication", 
        "codedeploy:CreateDeployment", 
        "codedeploy:CreateDeploymentGroup", 
        "codedeploy:GetApplication", 
        "codedeploy:GetDeployment", 
        "codedeploy:GetDeploymentGroup", 
        "codedeploy:ListApplications", 
        "codedeploy:ListDeploymentGroups", 
        "codedeploy:ListDeployments", 
        "codedeploy:StopDeployment", 
        "codedeploy:GetDeploymentTarget", 
        "codedeploy:ListDeploymentTargets", 
        "codedeploy:GetDeploymentConfig", 
        "codedeploy:GetApplicationRevision", 
        "codedeploy:RegisterApplicationRevision", 
        "codedeploy:BatchGetApplicationRevisions", 
        "codedeploy:BatchGetDeploymentGroups", 
        "codedeploy:BatchGetDeployments", 
        "codedeploy:BatchGetApplications", 
        "codedeploy:ListApplicationRevisions", 
        "codedeploy:ListDeploymentConfigs", 
        "codedeploy:ContinueDeployment"           
     ],
     "Resource":"*",
     "Effect":"Allow"
  },{"Action":[
        "iam:PassRole"
     ],
     "Effect":"Allow",
     "Resource":"*",
     "Condition":{"StringLike":{"iam:PassedToService":[
              "ecs-tasks.amazonaws.com",
              "codedeploy.amazonaws.com"
           ]
        }
     }
  }]
  }
  ```

------
**Note**  
The first time the role is used, use the following wildcard in the resource policy statement and then scope down the policy with the resource name after it is available.  

  ```
  "Resource": "*"
  ```
+ The following custom trust policy:

**Note**  
You can use the `CodeCatalystWorkflowDevelopmentRole-{{spaceName}}` role with this action, if you'd like. For more information about this role, see [Creating the **CodeCatalystWorkflowDevelopmentRole-{{spaceName}}** role for your account and space](ipa-iam-roles.md#ipa-iam-roles-service-create). Understand that the `CodeCatalystWorkflowDevelopmentRole-{{spaceName}}` role has full access permissions which may pose a security risk. We recommend that you only use this role in tutorials and scenarios where security is less of a concern. 

Corresponding UI: One of the following depending on the action version:
+ (Newer versions) Configuration tab/Environment/What's in {{my-environment}}?/three dot menu/**Switch role**
+ (Older versions) Configuration tab/'Environment/account/role'/**Role**

## Inputs
<a name="deploy.action.ecs.inputs"></a>

({{ECSDeployAction}}/**Inputs**)

(Optional)

The `Inputs` section defines the data that the `ECSDeployAction` needs during a workflow run.

**Note**  
Only one input (either a source or an artifact) is allowed per **Deploy to Amazon ECS** action.

Corresponding UI: **Inputs** tab

## Sources
<a name="deploy.action.ecs.inputs.sources"></a>

({{ECSDeployAction}}/Inputs/**Sources**)

(Required if your task definition file is stored in a source repository)

If your task definition file is stored in a source repository, specify the label of that source repository. Currently, the only supported label is `WorkflowSource`.

If your task definition file is not contained within a source repository, it must reside in an artifact generated by another action.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md).

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts - input
<a name="deploy.action.ecs.inputs.artifacts"></a>

({{ECSDeployAction}}/Inputs/**Artifacts**)

(Required if your task definition file is stored in an [output artifact](workflows-working-artifacts-output.md) from a previous action)

If the task definition file that you want to deploy is contained in an artifact generated by a previous action, specify that artifact here. If your task definition file is not contained within an artifact, it must reside in your source repository.

For more information about artifacts, including examples, see [Sharing artifacts and files between actions](workflows-working-artifacts.md).

Corresponding UI: Configuration tab/**Artifacts - optional**

## Configuration
<a name="deploy.action.ecs.configuration"></a>

({{ECSDeployAction}}/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## region
<a name="deploy.action.ecs.region"></a>

(Configuration/**region**)

(Required)

Specify the AWS Region where your Amazon ECS cluster and service reside. For a list of Region codes, see [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) in the *AWS General Reference*.

Corresponding UI: Configuration tab/**Region**

## cluster
<a name="deploy.action.ecs.cluster"></a>

({{ECSDeployAction}}/Configuration/**cluster**)

(Required)

Specify the name of an existing Amazon ECS cluster. The **Deploy to Amazon ECS** action will deploy your containerized application as a task into this cluster. For more information about Amazon ECS clusters, see [Clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html#welcome-clusters) in the *Amazon Elastic Container Service Developer Guide*.

Corresponding UI: Configuration tab/**Cluster**

## service
<a name="deploy.action.ecs.service"></a>

({{ECSDeployAction}}/Configuration/**service**)

(Required)

Specify the name of an existing Amazon ECS service that will instantiate the task definition file. This service must reside under the cluster specified in the `cluster` field. For more information about Amazon ECS services, see [Amazon ECS services](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html) in the *Amazon Elastic Container Service Developer Guide*.

Corresponding UI: Configuration tab/**Service**

## task-definition
<a name="deploy.action.ecs.task.definition"></a>

({{ECSDeployAction}}/Configuration/**task-definition**)

(Required)

Specify the path to an existing task definition file. If the file resides in your source repository, the path is relative to the source repository root folder. If your file resides in an artifact from a previous workflow action, the path is relative to the artifact root folder. For more information about task definition files, see [Task definitions](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html#welcome-task-definitions) in the *Amazon Elastic Container Service Developer Guide*.

Corresponding UI: Configuration tab/**Task definition**

## force-new-deployment
<a name="deploy.action.ecs.forcenewdeployment"></a>

({{ECSDeployAction}}/Configuration/**force-new-deployment**)

(Required)

If enabled, the Amazon ECS service is able to start new deployments without service definition changes. Forcing a deployment causes the service to stop all currently running tasks and launch new tasks. For more information about forcing new deployments, see [Updating a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service.html) in the *Amazon Elastic Container Service Developer Guide*.

Default: `false`

Corresponding UI: Configuration tab/**Force a new deployment of the service**

## codedeploy-appspec
<a name="deploy.action.ecs.codedeploy.appspec"></a>

({{ECSDeployAction}}/Configuration/**codedeploy-appspec**)

(Required if you have configured your Amazon ECS service to use blue/green deployments, otherwise, omit)

Specify the name and path to an existing CodeDeploy application specification (AppSpec) file. This file must reside in the root of your CodeCatalyst source repository. For more information about AppSpec files, see [CodeDeploy application specification (AppSpec) files](https://docs.aws.amazon.com/codedeploy/latest/userguide/application-specification-files.html) in the *AWS CodeDeploy User Guide*.

**Note**  
Only supply CodeDeploy information if you have configured your Amazon ECS service to perform blue/green deployments. For rolling update deployments (the default), omit CodeDeploy information. For more information about Amazon ECS deployments, see [Amazon ECS deployment types](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html) in the *Amazon Elastic Container Service Developer Guide*.

**Note**  
The **CodeDeploy** fields may be hidden in the visual editor. To get them to appear, see [Why are CodeDeploy fields missing from the visual editor?](troubleshooting-workflows.md#troubleshooting-workflows-codedeploy).

Corresponding UI: Configuration tab/**CodeDeploy AppSpec**

## codedeploy-application
<a name="deploy.action.ecs.codedeploy.application"></a>

({{ECSDeployAction}}/Configuration/**codedeploy-application**)

(Required if `codedeploy-appspec` is included)

Specify the name of an existing CodeDeploy application. For more information about CodeDeploy applications, see [Working with applications in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/applications.html) in the *AWS CodeDeploy User Guide*.

Corresponding UI: Configuration tab/**CodeDeploy application**

## codedeploy-deployment-group
<a name="deploy.action.ecs.codedeploy.deploymentgroup"></a>

({{ECSDeployAction}}/Configuration/**codedeploy-deployment-group**)

(Required if `codedeploy-appspec` is included)

Specify the name of an existing CodeDeploy deployment group. For more information about CodeDeploy deployment groups, see [Working with deployment groups in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-groups.html) in the *AWS CodeDeploy User Guide*.

Corresponding UI: Configuration tab/**CodeDeploy deployment group**

## codedeploy-deployment-description
<a name="deploy.action.ecs.codedeploy.deploymentdescription"></a>

({{ECSDeployAction}}/Configuration/**codedeploy-deployment-description**)

(Optional)

Specify a description of the deployment that this action will create. For more information, see [Working with deployments in CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments.html) in the *AWS CodeDeploy User Guide*.

Corresponding UI: Configuration tab/**CodeDeploy deployment description**