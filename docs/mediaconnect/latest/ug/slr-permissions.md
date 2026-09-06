

# Service-linked role permissions for MediaConnect
<a name="slr-permissions"></a>

MediaConnect uses the service-linked role named **AWSServiceRoleForMediaConnect**. This is the default Service-Linked Role that enables access to AWS services and resources used or managed by MediaConnect.

The AWSServiceRoleForMediaConnect service-linked role trusts the following services to assume the role:
+ `MediaConnect`

The role permissions policy named MediaConnectServiceRolePolicy allows MediaConnect to complete the following actions on the specified resources:

1. **Actions on all ECS resources**
   + Actions: 
     + `ecs:CreateCluster`
     + `ecs:RegisterTaskDefinition`
   + Resource: `*` 

1. **Actions on the MediaConnect Gateway ECS cluster**
   + Actions:
     + `ecs:DeregisterContainerInstance`
     + `ecs:DescribeClusters` 
     + `ecs:ListAttributes`
     + `ecs:ListContainerInstances` 
     + `ecs:UpdateCluster`
     + `ecs:UpdateClusterSettings`
   + Resource: `arn:aws:ecs:*:*:cluster/MediaConnectGateway`

1. **Actions on ECS services and tasks within the MediaConnect Gateway cluster** 
   + Actions:
     + `ecs:CreateService`
     + `ecs:DeleteAttributes`
     + `ecs:DeleteService`
     + `ecs:DescribeContainerInstances`
     + `ecs:DescribeServices`
     + `ecs:DescribeTasks`
     + `ecs:ListTasks`
     + `ecs:PutAttributes`
     + `ecs:RunTask`
     + `ecs:StartTask`
     + `ecs:StopTask`
     + `ecs:UpdateContainerInstancesState`
     + `ecs:UpdateService`
   + Resource: `*`
   + Condition: `ArnLike: {"ecs:cluster": "arn:aws:ecs:*:*:cluster/MediaConnectGateway"}`

1. **Actions on network interfaces within the MediaConnect router**
   + Actions:
     + `ec2:DeleteNetworkInterface`
     + `ec2:DeleteNetworkInterfacePermission`
     + `ec2:CreateNetworkInterfacePermission`
   + Resource: `arn:aws:ec2:*:*:network-interface/*"`
   + Condition: `aws:ResourceTag/created-for-service": "MediaConnect"`

1. **Actions to describe available network resources**
   + Actions:
     + `ec2:DescribeNetworkInterfaces`
     + `ec2:DescribeSecurityGroups`
     + `ec2:DescribeSubnets`
   + Resource: `*`

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.