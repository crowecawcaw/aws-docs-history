

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# 'Deploy to Kubernetes cluster' action YAML
<a name="deploy-action-ref-eks"></a>

The following is the YAML definition of the **Deploy to Kubernetes cluster** action. To learn how to use this action, see [Deploying to Amazon EKS with a workflow](deploy-action-eks.md).

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
  {{DeployToKubernetesCluster\_nn}}: 
    Identifier: aws/kubernetes-deploy@v1
    DependsOn:
      - {{build-action}}
    Compute:  
        - Type: {{EC2 | Lambda}}
        - Fleet: {{fleet-name}}
    Timeout: {{timeout-minutes}}
    Environment:
      Name: {{environment-name}}
      Connections:
        - Name: {{account-connection-name}}
          Role: {{DeployToEKS}}
    Inputs:
      # Specify a source or an artifact, but not both.
      Sources:
        - {{source-name-1}}
      Artifacts:
        - {{manifest-artifact}}
    Configuration:
      Namespace: {{namespace}}
      Region: {{us-east-1}} 
      Cluster: {{eks-cluster}}
      Manifests: {{manifest-path}}
```

## DeployToKubernetesCluster
<a name="deploy.action.eks.name"></a>

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed. You cannot use quotation marks to enable special characters and spaces in action names.

Default: `DeployToKubernetesCluster_nn`.

Corresponding UI: Configuration tab/**Action display name**

## Identifier
<a name="deploy.action.eks.identifier"></a>

({{DeployToKubernetesCluster}}/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version. For more information, see [Specifying the action version to use](workflows-action-versions.md).

Default: `aws/kubernetes-deploy@v1`.

Corresponding UI: Workflow diagram/DeployToKubernetesCluster\_nn/**aws/kubernetes-deploy@v1** label

## DependsOn
<a name="deploy.action.eks.dependson"></a>

({{DeployToKubernetesCluster}}/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md).

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute
<a name="deploy.action.eks.computename"></a>

({{DeployToKubernetesCluster}}/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level, but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow level, you can also run multiple actions on the same instance. For more information, see [Sharing compute across actions](compute-sharing.md).

Corresponding UI: *none*

## Type
<a name="deploy.action.eks.computetype"></a>

({{DeployToKubernetesCluster}}/Compute/**Type**)

(Required if [Compute](#deploy.action.eks.computename) is included)

The type of compute engine. You can use one of the following values:
+ **EC2** (visual editor) or `EC2` (YAML editor)

  Optimized for flexibility during action runs.
+ **Lambda** (visual editor) or `Lambda` (YAML editor)

  Optimized action start-up speeds.

For more information about compute types, see [Compute types](workflows-working-compute.md#compute.types).

Corresponding UI: Configuration tab/Advanced - optional/**Compute type**

## Fleet
<a name="deploy.action.eks.computefleet"></a>

({{DeployToKubernetesCluster}}/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand).

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets).

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/Advanced - optional/**Compute fleet**

## Timeout
<a name="deploy.action.eks.timeout"></a>

({{DeployToKubernetesCluster}}/**Timeout**)

(Optional)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor), that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md). The default timeout is the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional **

## Environment
<a name="deploy.action.eks.environment"></a>

({{DeployToKubernetesCluster}}/**Environment**)

(Required)

Specify the CodeCatalyst environment to use with the action. The action connects to the AWS account and optional Amazon VPC specified in the chosen environment. The action uses the default IAM role specified in the environment to connect to the AWS account, and uses the IAM role specified in the [Amazon VPC connection](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-vpcs.add.html) to connect to the Amazon VPC.

**Note**  
If the default IAM role does not have the permissions required by the action, you can configure the action to use a different role. For more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md).

For more information about environments, see [Deploying into AWS accounts and VPCs](deploy-environments.md) and [Creating an environment](deploy-environments-creating-environment.md).

Corresponding UI: Configuration tab/**Environment**

## Name
<a name="deploy.action.eks.environment.name"></a>

({{DeployToKubernetesCluster}}/Environment/**Name**)

(Required if [Environment](#deploy.action.eks.environment) is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration tab/**Environment**

## Connections
<a name="deploy.action.eks.environment.connections"></a>

({{DeployToKubernetesCluster}}/Environment/**Connections**)

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
<a name="deploy.action.eks.environment.connections.name"></a>

({{DeployToKubernetesCluster}}/Environment/Connections/**Name**)

(Optional)

Specify the name of the account connection.

Corresponding UI: One of the following depending on the action version:
+ (Newer versions) Configuration tab/Environment/What's in {{my-environment}}?/three dot menu/**Switch role**
+ (Older versions) Configuration tab/'Environment/account/role'/**AWS account connection**

## Role
<a name="deploy.action.eks.environment.connections.role"></a>

({{DeployToKubernetesCluster}}/Environment/Connections/**Role**)

(Required if [Connections](#deploy.action.eks.environment.connections) is included)

Specify the name of the IAM role that the **Deploy to Kubernetes cluster ** action uses to access AWS. Make sure that you have [added the role to your CodeCatalyst space](ipa-connect-account-addroles.md), and that the role includes the following policies.

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
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "eks:DescribeCluster",
                  "eks:ListClusters"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

------
**Note**  
The first time the role is used, use the following wildcard in the resource policy statement and then scope down the policy with the resource name after it is available.  

  ```
  "Resource": "*"
  ```
+ The following custom trust policy:

Make sure that this role is added to:
+ Your account connection. To learn more about adding an IAM role to an account connection, see [Adding IAM roles to account connections](ipa-connect-account-addroles.md).
+ Your Kubernetes ConfigMap. To learn more about adding an IAM role to a ConfigMap, see [Manage IAM users and roles](https://eksctl.io/usage/iam-identity-mappings/) in the `eksctl` documentation.

**Tip**  
See also [Tutorial: Deploy an application to Amazon EKS](deploy-tut-eks.md) for instructions on adding am IAM role to an account connection and ConfigMap.

**Note**  
You can use the `CodeCatalystWorkflowDevelopmentRole-{{spaceName}}` role with this action, if you'd like. For more information about this role, see [Creating the **CodeCatalystWorkflowDevelopmentRole-{{spaceName}}** role for your account and space](ipa-iam-roles.md#ipa-iam-roles-service-create). Understand that the `CodeCatalystWorkflowDevelopmentRole-{{spaceName}}` role has full access permissions which may pose a security risk. We recommend that you only use this role in tutorials and scenarios where security is less of a concern. 

Corresponding UI: One of the following depending on the action version:
+ (Newer versions) Configuration tab/Environment/What's in {{my-environment}}?/three dot menu/**Switch role**
+ (Older versions) Configuration tab/'Environment/account/role'/**Role**

## Inputs
<a name="deploy.action.eks.inputs"></a>

({{DeployToKubernetesCluster}}/**Inputs**)

(Required if [Connections](#deploy.action.eks.environment.connections) is included)

The `Inputs` section defines the data that the `DeployToKubernetesCluster` needs during a workflow run.

**Note**  
Only one input (either a source or an artifact) is allowed per **Deploy to Amazon EKS** action.

Corresponding UI: **Inputs** tab

## Sources
<a name="deploy.action.eks.inputs.sources"></a>

({{DeployToKubernetesCluster}}/Inputs/**Sources**)

(Required if your manifest file is stored in a source repository)

If your Kubernetes manifest file or files are stored in a source repository, specify the label of that source repository. Currently, the only supported label is `WorkflowSource`.

If your manifest files are not contained within a source repository, they must reside in an artifact generated by another action.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md).

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts - input
<a name="deploy.action.eks.inputs.artifacts"></a>

({{DeployToKubernetesCluster}}/Inputs/**Artifacts**)

(Required if your manifest file is stored in an [output artifact](workflows-working-artifacts-output.md) from a previous action)

If the Kubernetes manifest file or files are contained in an artifact generated by a previous action, specify that artifact here. If your manifest files are not contained within an artifact, they must reside in your source repository.

For more information about artifacts, including examples, see [Sharing artifacts and files between actions](workflows-working-artifacts.md).

Corresponding UI: Configuration tab/**Artifacts - optional**

## Configuration
<a name="deploy.action.eks.configuration"></a>

({{DeployToKubernetesCluster}}/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## Namespace
<a name="deploy.action.eks.namespace"></a>

({{DeployToKubernetesCluster}}/Configuration/**Namespace**)

(Optional)

Specify the Kubernetes namespace into which your Kubernetes application will be deployed. Use `default` if you are not using namespaces with your cluster. For more information on namespaces, see [Subdividing your cluster using Kubernetes namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/#subdividing-your-cluster-using-kubernetes-namespaces) in the Kubernetes documentation.

If you omit the namespace, a value of `default` is used.

Corresponding UI: Configuration tab/**Namespace**

## Region
<a name="deploy.action.eks.region"></a>

({{DeployToKubernetesCluster}}/Configuration/**Region**)

(Required)

Specify the AWS Region where your Amazon EKS cluster and service reside. For a list of Region codes, see [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#region-names-codes) in the *AWS General Reference*.

Corresponding UI: Configuration tab/**Region**

## Cluster
<a name="deploy.action.eks.cluster"></a>

({{DeployToKubernetesCluster}}/Configuration/**Cluster**)

(Required)

Specify the name of an existing Amazon EKS cluster. The **Deploy to Kubernetes cluster** action will deploy your containerized application into this cluster. For more information about Amazon EKS clusters, see [Clusters](https://docs.aws.amazon.com/eks/latest/userguide/clusters.html) in the **Amazon EKS User Guide**.

Corresponding UI: Configuration tab/**Cluster**

## Manifests
<a name="deploy.action.eks.manifest"></a>

({{DeployToKubernetesCluster}}/Configuration/**Manifests**)

(Required)

Specify the path to your YAML-formatted Kubernetes manifest file(s), which are called *configuration files*, *config files*, or simply, *configurations* in the Kubernetes documentation.

If you're using multiple manifest files, place them in a single folder and reference that folder. Manifest files are processed alphanumerically by Kubernetes, so make sure to prefix file names with increasing numbers or letters to control the processing order. For example:

`00-namespace.yaml`

`01-deployment.yaml`

If your manifest files reside in your source repository, the path is relative to the source repository root folder. If the files reside in an artifact from a previous workflow action, the path is relative to the artifact root folder. 

Examples:

`Manifests/`

`deployment.yaml`

`my-deployment.yml`

Do not use wildcards (`*`).

**Note**  
[Helm charts](https://helm.sh/docs/topics/charts/) and [kustomization files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/) are not supported.

For more information about manifest files, see [Organizing resource configurations](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#organizing-resource-configurations) in the Kubernetes documentation.

Corresponding UI: Configuration tab/**Manifests**