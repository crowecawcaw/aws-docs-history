# Service-linked role permissions for MediaConnect

MediaConnect uses the service-linked role named **AWSServiceRoleForMediaConnect** –
The default Service-Linked Role that enables access to AWS Services and Resources used or managed by MediaConnect..

The AWSServiceRoleForMediaConnect service-linked role trusts the following services to assume the
role:

- `MediaConnect`
  The role permissions policy named MediaConnectServiceRolePolicy allows MediaConnect to complete the following actions on the
  specified resources:

- Action: `ecs:CreateCluster,
ecs:RegisterTaskDefinition,
ecs:DescribeTaskDefinition,
ecs:ListAttributes,
ecs:UpdateContainerInstancesState,
ecs:DeregisterContainerInstance` on Resource
  `arn:aws:ecs:*:*:*`
- Action: `ecs:UpdateCluster,
ecs:UpdateClusterSettings,
ecs:DescribeClusters` on
  Resource`arn:aws:ecs:*:*:cluster/MediaConnect`
- Action: `ecs:CreateService,
 ecs:UpdateService,
 ecs:RunTask,
 ecs:StartTask,
 ecs:StopTask,
 ecs:ExecuteCommand,
 ecs:PutAttributes,
 ecs:DeleteAttributes,
 ecs:DescribeServices,
 ecs:DescribeTasks,
 ecs:ListTasks` on Resource
  `arn:aws:ecs:*:*:*` with the Condition of `StringLike:
 {ecs:Cluster: arn:aws:ecs:*:*:cluster/MediaConnect}`
  You must configure permissions to allow an IAM entity (such as a user, group, or role)
  to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User Guide_.
