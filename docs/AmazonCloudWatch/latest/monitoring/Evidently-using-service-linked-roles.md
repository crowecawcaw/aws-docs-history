# Using service-linked roles for
 Evidently

###### Important

End of support notice: On October 16, 2025, AWS 
 will discontinue support for CloudWatch Evidently. After October 16, 2025, you will 
 no longer be able to access the Evidently console or Evidently resources. 
 

CloudWatch Evidently uses AWS Identity and Access Management (IAM)[service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
 linked directly to Evidently. Service-linked roles are predefined by Evidently and
 include all the permissions that the service requires to call other AWS services on your
 behalf. 

A service-linked role makes setting up Evidently easier because you don’t have to
 manually add the necessary permissions. Evidently defines the permissions of its
 service-linked roles, and unless defined otherwise, only Evidently can assume its roles. The
 defined permissions include the trust policy and the permissions policy, and that permissions
 policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
 protects your Evidently resources because you can't inadvertently remove permission to
 access the resources.

For information about other services that support service-linked roles, see [AWS Services That Work with
 IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html") and look for the services that have **Yes** in the
 **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that
 service.


## Service-linked role permissions for
 Evidently


Evidently uses the service-linked role named **AWSServiceRoleForCloudWatchEvidently** –
 Allows CloudWatch Evidently to manage associated AWS resourcees on behalf of the customer.


The AWSServiceRoleForCloudWatchEvidently service-linked role trusts the following services to assume the
 role:



* `CloudWatch Evidently`

The role permissions policy named AmazonCloudWatchEvidentlyServiceRolePolicy allows Evidently to complete the following actions on the
 specified resources:



* Actions: `appconfig:StartDeployment`, 
 `appconfig:StopDeployment`, `appconfig:ListDeployments`, and `appconfig:TagResource`
 on
 Evidently thick clients.

You must configure permissions to allow an IAM entity (such as a user, group, or role)
 to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions") in the *IAM User Guide*.


## Creating a service-linked role for
 Evidently


You don't need to manually create a service-linked role. When you
 start using an Evidently thick client in the AWS Management Console, the AWS CLI, or the AWS API, Evidently
 creates the service-linked role for you. 


If you delete this service-linked role, and then need to create it again, you can use the
 same process to recreate the role in your account. When you start using an Evidently thick client,
 Evidently creates the service-linked role for you again. 


## Editing a service-linked role for
 Evidently


Evidently does not allow you to edit the AWSServiceRoleForCloudWatchEvidently service-linked role. After you
 create a service-linked role, you cannot change the name of the role because various entities
 might reference the role. However, you can edit the description of the role using IAM. For
 more information, see [Editing a
 service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role") in the *IAM User Guide*.


## Deleting a service-linked role for
 Evidently


If you no longer need to use a feature or service that requires a service-linked role, we
 recommend that you delete that role. That way you don’t have an unused entity that is not
 actively monitored or maintained. However, you must clean up the resources for your
 service-linked role before you can manually delete it. You must delete all Evidently projects 
 that are using thick clients. 


###### Note

If the Evidently service is using the role when you try to delete the resources,
 then the deletion might fail. If that happens, wait for a few minutes and try the
 operation again.


###### To delete Evidently resources used by AWSServiceRoleForCloudWatchEvidently

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application monitoring**, **Evidently**.
3. In the list of projects, select the check box next to the projects that used thick clients.
4. Choose **Project actions**, **Delete project**.

**To manually delete the service-linked role using
 IAM**


Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForCloudWatchEvidently
 service-linked role. For more information, see [Deleting a
 service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role "https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role") in the *IAM User Guide*.


## Supported regions for
 Evidently service-linked roles


Evidently supports using service-linked roles in all of the regions where the service is available. For more information, see [AWS regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html "https://docs.aws.amazon.com/general/latest/gr/rande.html").
