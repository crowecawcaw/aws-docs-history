

# Using roles to allow Amazon ECS to manage clusters
<a name="using-service-linked-roles-for-clusters"></a>

Amazon Elastic Container Service uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Amazon ECS. Service-linked roles are predefined by Amazon ECS and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Amazon ECS easier because you don’t have to manually add the necessary permissions. Amazon ECS defines the permissions of its service-linked roles, and unless defined otherwise, only Amazon ECS can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your Amazon ECS resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for Amazon ECS
<a name="service-linked-role-permissions-clusters"></a>

Amazon ECS uses the service-linked role named **AWSServiceRoleForECS** – Role to allow Amazon ECS to manage your cluster.

The AWSServiceRoleForECS service-linked role trusts the following services to assume the role:
+ `ecs.amazonaws.com`

The role permissions policy named AmazonECSServiceRolePolicy allows Amazon ECS to complete the following actions on the specified resources:
+ Action: When using the `awsvpc` network mode for your Amazon ECS tasks, Amazon ECS manages the lifecycle of the elastic network interfaces associated with the task. This also includes tags that Amazon ECS adds to your elastic network interfaces.
+ Action: When using a load balancer with your Amazon ECS service, Amazon ECS manages the registration and deregistration of resources with the load balancer.
+ Action: When using Amazon ECS service discovery, Amazon ECS manages the required Route 53 and AWS Cloud Map resources for service discovery to work.
+ Action: When using Amazon ECS service auto scaling, Amazon ECS manages the required Auto Scaling resources.
+ Action: Amazon ECS creates and manages CloudWatch alarms and log streams that assist in the monitoring of your Amazon ECS resources.
+ Action: When using Amazon ECS Exec, Amazon ECS manages the permissions needed to start Amazon ECS Exec sessions to your tasks.
+ Action: When using Amazon ECS Service Connect, Amazon ECS manages the required AWS Cloud Map resources to use the feature.
+ Action: When using Amazon ECS capacity providers, Amazon ECS manages the permissions required to modify the Auto Scaling group and its Amazon EC2 instances.
+ Action: Amazon ECS can update AWS Cloud Map service attributes for services that Amazon ECS manages.
+ Action: Amazon ECS can invoke Amazon EC2 provision and de-provision ENI when starting and stopping tasks.
+ Action: Amazon ECS can fetch Amazon EC2 Event Windows for services and clusters associated with Event Windows.

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for Amazon ECS
<a name="create-service-linked-role-clusters"></a>

You don't need to manually create a service-linked role. When you create a cluster, or create or update a service in the AWS Management Console, the AWS CLI, or the AWS API, Amazon ECS creates the service-linked role for you. 

**Important**  
 This service-linked role can appear in your account if you completed an action in another service that uses the features supported by this role. If you were using the Amazon ECS service before January 1, 2017, when it began supporting service-linked roles, then Amazon ECS created the AWSServiceRoleForECS role in your account. To learn more, see [A new role appeared in my AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

You can also use the IAM console to create a service-linked role with the **AWSServiceRoleForECS** use case. In the AWS CLI or the AWS API, use IAM to create a service-linked role with the `ecs.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create a cluster, or create or update a service, Amazon ECS creates the service-linked role for you again. 

If you delete this service-linked role, you can use the same IAM process to create the role again.

## Editing a service-linked role for Amazon ECS
<a name="edit-service-linked-role-clusters"></a>

Amazon ECS does not allow you to edit the AWSServiceRoleForECS service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for Amazon ECS
<a name="delete-service-linked-role-clusters"></a>

You don't need to manually delete the AWSServiceRoleForECS role. When you delete clusters in all Regions in the AWS Management Console, the AWS CLI, or the AWS API, Amazon ECS cleans up the resources and deletes the service-linked role for you.

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up a service-linked role
<a name="service-linked-role-review-before-delete-clusters"></a>

Before you can use IAM to delete a service-linked role, you must first delete any resources used by the role.

**Note**  
If the Amazon ECS service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete Amazon ECS resources used by the AWSServiceRoleForECS (console)**

1. Scale all Amazon ECS services down to a desired count of 0 in all regions, and then delete the services. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md) and [Deleting an Amazon ECS service using the console](delete-service-v2.md).

1. Force deregister all container instances from all clusters in all Regions. For more information, see [Deregistering an Amazon ECS container instance](deregister_container_instance.md).

1. Delete all Amazon ECS clusters in all regions. For more information, see [Deleting an Amazon ECS cluster](delete_cluster-new-console.md).

**To delete Amazon ECS resources used by the AWSServiceRoleForECS (AWS CLI)**

1. Scale all Amazon ECS services down to a desired count of 0 in all regions, and then delete the services. For more information, see [update-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/update-service.html) and [delete-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/delete-service.html) in the AWS Command Line Interface Reference.

1. Force deregister all container instances from all clusters in all Regions. For more information, see [deregister-container-instance](https://docs.aws.amazon.com/cli/latest/reference/ecs/deregister-container-instance.html).

1. Delete all Amazon ECS clusters in all Regions. For more information, see [delete-cluster](https://docs.aws.amazon.com/cli/latest/reference/ecs/delete-cluster.html).

**To delete Amazon ECS resources used by the AWSServiceRoleForECS (API)**

1. Scale all Amazon ECS services down to a desired count of 0 in all regions, and then delete the services. For more information, see [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) and [DeleteService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteService.html) in the *Amazon ECS API Reference*.

1. Force deregister all container instances from all clusters in all Regions. For more information, see [DeregisterContainerInstance](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeregisterContainerInstance.html).

1. Delete all Amazon ECS clusters in all Regions. For more information, see [DeleteCluster](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeleteCluster.html).

### Manually delete the service-linked role
<a name="slr-manual-delete-clusters"></a>

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForECS service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for Amazon ECS service-linked roles
<a name="slr-regions-clusters"></a>

Amazon ECS supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).