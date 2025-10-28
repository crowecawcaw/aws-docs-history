Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Deploy to Kubernetes cluster' action YAML

The following is the YAML definition of the **Deploy to Kubernetes cluster**
action. To learn how to use this action, see [Deploying to Amazon EKS with a
workflow](deploy-action-eks.md "deploy-action-eks.md").

This action definition exists as a section within a broader workflow definition file. For
more information about this file, see [Workflow YAML definition](workflow-reference.md "workflow-reference.md").

###### Note

Most of the YAML properties that follow have corresponding UI elements in the visual
editor. To look up a UI element, use **Ctrl+F**. The element will be
listed with its associated YAML property.

```
# The workflow definition starts here.
# See Top-level properties for details.

Name: MyWorkflow
SchemaVersion: 1.0
Actions:

# The action definition starts here.
  `DeployToKubernetesCluster_nn`:
    Identifier: aws/kubernetes-deploy@v1
    DependsOn:
      - `build-action`
    Compute:
        - Type: `EC2 | Lambda`
        - Fleet: `fleet-name`
    Timeout: `timeout-minutes`
    Environment:
      Name: `environment-name`
      Connections:
        - Name: `account-connection-name`
          Role: `DeployToEKS`
    Inputs:
      # Specify a source or an artifact, but not both.
      Sources:
        - `source-name-1`
      Artifacts:
        - `manifest-artifact`
    Configuration:
      Namespace: `namespace`
      Region: `us-east-1`
      Cluster: `eks-cluster`
      Manifests: `manifest-path`
```

## DeployToKubernetesCluster

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in action names.

Default: `DeployToKubernetesCluster_nn`.

Corresponding UI: Configuration tab/**Action display name**

## Identifier

(`DeployToKubernetesCluster`/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version. For
more information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

Default: `aws/kubernetes-deploy@v1`.

Corresponding UI: Workflow
diagram/DeployToKubernetesCluster_nn/**aws/kubernetes-deploy@v1**
label

## DependsOn

(`DeployToKubernetesCluster`/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to
run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute

(`DeployToKubernetesCluster`/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

## Type

(`DeployToKubernetesCluster`/Compute/**Type**)

(Required if [Compute](#deploy.action.eks.computename "#deploy.action.eks.computename") is included)

The type of compute engine. You can use one of the following values:

- **EC2** (visual editor) or `EC2` (YAML editor)

Optimized for flexibility during action runs.

- **Lambda** (visual editor) or `Lambda` (YAML
  editor)

Optimized action start-up speeds.

For more information about compute types, see [Compute types](workflows-working-compute.md#compute.types "workflows-working-compute.md#compute.types").

Corresponding UI: Configuration tab/Advanced - optional/**Compute
type**

## Fleet

(`DeployToKubernetesCluster`/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/Advanced - optional/**Compute
fleet**

## Timeout

(`DeployToKubernetesCluster`/**Timeout**)

(Optional)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor),
that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is
described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). The default timeout is
the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional**

## Environment

(`DeployToKubernetesCluster`/**Environment**)

(Required)

Specify the CodeCatalyst environment to use with the action. The action connects to
the AWS account and optional Amazon VPC specified in the chosen environment. The action uses the
default IAM role specified in the environment to connect to the AWS account, and uses the
IAM role specified in the [Amazon VPC connection](../adminguide/managing-vpcs.md "../adminguide/managing-vpcs.md") to
connect to the Amazon VPC.

###### Note

If the default IAM role does not have the permissions required by the action, you can
configure the action to use a different role. For more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md "deploy-environments-switch-role.md").

For more information about environments, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md") and [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

Corresponding UI: Configuration tab/**Environment**

## Name

(`DeployToKubernetesCluster`/Environment/**Name**)

(Required if [Environment](#deploy.action.eks.environment "#deploy.action.eks.environment") is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration tab/**Environment**

## Connections

(`DeployToKubernetesCluster`/Environment/**Connections**)

(Optional in newer versions of the action; required in older versions)

Specify the account connection to associate with the action. You can specify a maximum of
one account connection under `Environment`.

If you do not specify an account connection:

- The action uses the AWS account connection and default IAM role specified in the
  environment in the CodeCatalyst console. For information about adding an account connection and
  default IAM role to environment, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").
- The default IAM role must include the policies and permissions required by the action.
  To determine what those policies and permissions are, see the description of the **Role** property in the action's YAML definition documentation.

For more information about account connections, see [Allowing access to AWS resources with connected
AWS accounts](ipa-connect-account.md "ipa-connect-account.md"). For information about adding an account connection to
an environment, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration tab/'Environment/account/role'/**AWS
  account connection**

## Name

(`DeployToKubernetesCluster`/Environment/Connections/**Name**)

(Optional)

Specify the name of the account connection.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration tab/'Environment/account/role'/**AWS
  account connection**

## Role

(`DeployToKubernetesCluster`/Environment/Connections/**Role**)

(Required if [Connections](#deploy.action.eks.environment.connections "#deploy.action.eks.environment.connections") is included)

Specify the name of the IAM role that the **Deploy to Kubernetes cluster**
action uses to access AWS. Make sure that you have [added the role to your CodeCatalyst space](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md"), and that
the role includes the following policies.

If you do not specify an IAM role, then the action uses the default IAM role listed in
the [environment](deploy-environments.md "deploy-environments.md") in the CodeCatalyst console. If you use the
default role in the environment, make sure it has the following policies.

- The following permissions policy:

###### Warning

Limit the permissions to those shown in the following policy. Using a role with
broader permissions might pose a security risk.

JSON

```
`{
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
}`

```

###### Note

The first time the role is used, use the following wildcard in the resource policy
statement and then scope down the policy with the resource name after it is
available.

```
"Resource": "*"
```

- The following custom trust policy:

Make sure that this role is added to:

- Your account connection. To learn more about adding an IAM role to an account
  connection, see [Adding IAM roles to account
  connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md").
- Your Kubernetes ConfigMap. To learn more about adding an IAM role to a ConfigMap, see
  [Manage IAM users and
  roles](https://eksctl.io/usage/iam-identity-mappings/ "https://eksctl.io/usage/iam-identity-mappings/") in the `eksctl` documentation.

###### Tip

See also [Tutorial: Deploy an application to Amazon EKS](deploy-tut-eks.md "deploy-tut-eks.md") for instructions
on adding am IAM role to an account connection and ConfigMap.

###### Note

You can use the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role with this action, if you'd like. For more information
 about this role, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create"). Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role has
full access permissions which may pose a security risk. We recommend that you only use this
role in tutorials and scenarios where security is less of a concern.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration
  tab/'Environment/account/role'/**Role**

## Inputs

(`DeployToKubernetesCluster`/**Inputs**)

(Required if [Connections](#deploy.action.eks.environment.connections "#deploy.action.eks.environment.connections") is included)

The `Inputs` section defines the data that the
`DeployToKubernetesCluster` needs during a workflow run.

###### Note

Only one input (either a source or an artifact) is allowed per **Deploy to
Amazon EKS**
action.

Corresponding UI: **Inputs** tab

## Sources

(`DeployToKubernetesCluster`/Inputs/**Sources**)

(Required if your manifest file is stored in a source repository)

If your Kubernetes manifest file or files are stored in a source repository, specify the label of that
source repository. Currently, the only supported label is `WorkflowSource`.

If your manifest files are not contained within a source repository, they must
reside in an artifact generated by another action.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md").

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts -

input

(`DeployToKubernetesCluster`/Inputs/**Artifacts**)

(Required if your manifest file is stored in an [output artifact](workflows-working-artifacts-output.md "workflows-working-artifacts-output.md") from a previous
action)

If the Kubernetes manifest file or files are contained in an artifact generated by
a previous action, specify that artifact here. If your manifest files are not contained
within an artifact, they must reside in your source repository.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Configuration tab/**Artifacts - optional**

## Configuration

(`DeployToKubernetesCluster`/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## Namespace

(`DeployToKubernetesCluster`/Configuration/**Namespace**)

(Optional)

Specify the Kubernetes namespace into which your Kubernetes application will be deployed. Use
`default` if you are not using namespaces with your cluster. For more information
on namespaces, see [Subdividing your cluster using Kubernetes namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/#subdividing-your-cluster-using-kubernetes-namespaces "https://kubernetes.io/docs/tasks/administer-cluster/namespaces/#subdividing-your-cluster-using-kubernetes-namespaces") in the Kubernetes documentation.

If you omit the namespace, a value of `default` is used.

Corresponding UI: Configuration tab/**Namespace**

## Region

(`DeployToKubernetesCluster`/Configuration/**Region**)

(Required)

Specify the AWS Region where your Amazon EKS cluster and service reside. For a list of Region
codes, see [Regional endpoints](../../../general/latest/gr/rande.md#region-names-codes "../../../general/latest/gr/rande.md#region-names-codes") in the _AWS General Reference_.

Corresponding UI: Configuration tab/**Region**

## Cluster

(`DeployToKubernetesCluster`/Configuration/**Cluster**)

(Required)

Specify the name of an existing Amazon EKS cluster. The **Deploy to Kubernetes cluster** action
will deploy your containerized application into this cluster. For more information about Amazon EKS
clusters, see [Clusters](../../../eks/latest/userguide/clusters.md "../../../eks/latest/userguide/clusters.md") in the
**Amazon EKS User Guide**.

Corresponding UI: Configuration tab/**Cluster**

## Manifests

(`DeployToKubernetesCluster`/Configuration/**Manifests**)

(Required)

Specify the path to your YAML-formatted Kubernetes manifest file(s), which are called
_configuration files_, _config files_, or simply,
_configurations_ in the Kubernetes documentation.

If you're using multiple manifest files, place them in a single folder and reference that
folder. Manifest files are processed alphanumerically by Kubernetes, so make sure to prefix file names
with increasing numbers or letters to control the processing order. For example:

`00-namespace.yaml`

`01-deployment.yaml`

If your manifest files reside in your source repository, the path is relative to the source
repository root folder. If the files reside in an artifact from a previous workflow action, the
path is relative to the artifact root folder.

Examples:

`Manifests/`

`deployment.yaml`

`my-deployment.yml`

Do not use wildcards (`*`).

###### Note

[Helm charts](https://helm.sh/docs/topics/charts/ "https://helm.sh/docs/topics/charts/") and [kustomization files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/ "https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/") are not supported.

For more information about manifest files, see [Organizing resource configurations](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#organizing-resource-configurations "https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#organizing-resource-configurations") in the Kubernetes documentation.

Corresponding UI: Configuration tab/**Manifests**
