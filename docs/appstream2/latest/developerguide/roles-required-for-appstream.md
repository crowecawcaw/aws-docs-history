

# Roles Required for WorkSpaces Applications, Application Auto Scaling, and AWS Certificate Manager Private CA
<a name="roles-required-for-appstream"></a>

In AWS, IAM roles are used to grant permissions to an AWS service so it can access AWS resources. The policies that are attached to the role determine which AWS resources the service can access and what it can do with those resources. For WorkSpaces Applications, in addition to having the permissions defined in the **AmazonAppStreamFullAccess** policy, you must also have the following roles in your AWS account.

**Topics**
+ [AmazonAppStreamServiceAccess](#AmazonAppStreamServiceAccess)
+ [ApplicationAutoScalingForAmazonAppStreamAccess](#ApplicationAutoScalingForAmazonAppStreamAccess)
+ [AWSServiceRoleForApplicationAutoScaling\_AppStreamFleet](#AWSServiceRoleForApplicationAutoScaling_AppStreamFleet)
+ [AmazonAppStreamPCAAccess](#AppStreamPCAAccess)

## AmazonAppStreamServiceAccess
<a name="AmazonAppStreamServiceAccess"></a>

This role is a service role that is created for you automatically when you get started with WorkSpaces Applications in an AWS Region. For more information about services roles, see [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

While WorkSpaces Applications resources are being created, the WorkSpaces Applications service makes API calls to other AWS services on your behalf by assuming this role. To create fleets, you must have this role in your account. If this role is not in your AWS account and the required IAM permissions and trust relationship policies are not attached, you cannot create WorkSpaces Applications fleets.

For more information, see [Checking for the AmazonAppStreamServiceAccess Service Role and Policies](controlling-access-checking-for-iam-service-access.md) to check whether the **AmazonAppStreamServiceAccess** service role is present and has the correct policies attached. 

**Note**  
This service role can have permissions that are different from the first user that is getting started with WorkSpaces Applications. For details on the permissions of this role see “AmazonAppStreamServiceAccess” in [AWS Managed Policies Required to Access WorkSpaces Applications Resources](managed-policies-required-to-access-appstream-resources.md).

## ApplicationAutoScalingForAmazonAppStreamAccess
<a name="ApplicationAutoScalingForAmazonAppStreamAccess"></a>

This role is a service role that is created for you automatically when you get started with WorkSpaces Applications in an AWS Region. For more information about services roles, see [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

Automatic scaling is a feature of WorkSpaces Applications fleets. To configure scaling policies, you must have this service role in your AWS account. If this service role is not in your AWS account and the required IAM permissions and trust relationship policies are not attached, you cannot scale WorkSpaces Applications fleets.

For more information, see [Checking for the ApplicationAutoScalingForAmazonAppStreamAccess Service Role and Policies](controlling-access-checking-for-iam-autoscaling.md).

## AWSServiceRoleForApplicationAutoScaling\_AppStreamFleet
<a name="AWSServiceRoleForApplicationAutoScaling_AppStreamFleet"></a>

This role is a service-linked role that is created for you automatically. For more information, see [Service-linked roles](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html) in the *Application Auto Scaling User Guide*.

Application Auto Scaling uses a service-linked role to perform automatic scaling on your behalf. A *service-linked role* is an IAM role that is linked directly to an AWS service. This role includes all the permissions that the service requires to call other AWS services on your behalf.

For more information, see [Checking for the `AWSServiceRoleForApplicationAutoScaling_AppStreamFleet` Service-Linked Role and Policies](controlling-access-checking-for-iam-service-linked-role-application-autoscaling-appstream-fleet.md).

## AmazonAppStreamPCAAccess
<a name="AppStreamPCAAccess"></a>

This role is a service role that is created for you automatically when you get started with WorkSpaces Applications in an AWS Region. For more information about services roles, see [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*.

Certificate-based authentication is a feature of WorkSpaces Applications fleets joined to Microsoft Active Directory domains. To enable and use certificate-based authentication, you must have this service role in your AWS account. If this service role is not in your AWS account and the required IAM permissions and trust relationship policies are not attached, you cannot enable or use certificate-based authentication.

For more information, see [Checking for the AmazonAppStreamPCAAccess Service Role and Policies](controlling-access-checking-for-AppStreamPCAAccess.md).