

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Amazon EventBridge rule service-linked role for AMS Advanced
<a name="slr-evb-rule-advanced"></a>

AMS Advanced uses the service-linked role (SLR) named **AWSServiceRoleForManagedServices\_Events** – This role trusts one of the AWS Managed Services service principals (events.managedservices.amazonaws.com) to assume the role for you. The service uses the role to create EventBridge managed rule. This rule is the infrastructure required in your AWS account to deliver alarm state change information from your account to AWS Managed Services.

## Permissions for EventBridge SLR for AMS Advanced
<a name="slr-permissions-create-evb-rule"></a>

The **AWSServiceRoleForManagedServices\_Events** service-linked role trusts the following services to assume the role:
+ events.managedservices.amazonaws.com

Attached to this role is the **AWSManagedServices\_EventsServiceRolePolicy** AWS managed policy (see [AWS managed policy: AWSManagedServices\_EventsServiceRolePolicy](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/security-iam-awsmanpol.html#EventsServiceRolePolicy)). The service uses the role to deliver alarm state change information from your account to AWS Managed Services. You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *AWS Identity and Access Management* User Guide.

You can download the JSON **AWSManagedServices\_EventsServiceRolePolicy** in this ZIP: [EventsServiceRolePolicy.zip](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/samples/EventsServiceRolePolicy.zip).

## Creating an EventBridge SLR for AMS Advanced
<a name="slr-evb-rule-create"></a>

You don't need to manually create a service-linked role. When you Onboard to AMS in the AWS Management Console, the AWS CLI, or the AWS API, then AMS Advanced creates the service-linked role for you. 

**Important**  
This service-linked role can appear in your account if you were using the AMS Advanced service before February 7, 2023, when it began supporting service-linked roles then AMS Accelerate created the AWSServiceRoleForManagedServices\_Events role in your account. To learn more, see [A new role appeared in my IAM account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you Onboard to AMS, AMS Advanced creates the service-linked role for you again. 

## Editing an EventBridge SLR for AMS Advanced
<a name="slr-evb-rule-edit"></a>

AMS Advanced does not allow you to edit the AWSServiceRoleForManagedServices\_Events service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting an EventBridge SLR for AMS Advanced
<a name="slr-evb-rule-delete"></a>

You don't need to manually delete the AWSServiceRoleForManagedServices\_Events role. When you Offboard from AMS in the AWS Management Console, the AWS CLI or the AWS API, AMS Advanced cleans up the resources and deletes the service-linked role for you.

You can also use the IAM console, the AWS CLI or the AWS API to manually delete the service-linked role. To do this, you must first manually clean up the resources for your service-linked role and then you can manually delete it.

**Note**  
If the AMS Advanced service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete AMS Advanced resources **used by the AWSServiceRoleForManagedServices\_Events service-linked role****

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForManagedServices\_Events service-linked role. 

For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.