# Using service-linked roles for Amazon MWAA Serverless

Amazon MWAA Serverless uses an AWS Identity and Access Management (IAM) [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") named `AWSServiceRoleForAmazonMWAAServerless`. This service-linked role is an (IAM) role
that's linked directly to Amazon MWAA Serverless. It's predefined by Amazon MWAA Serverless, and it includes all the permissions that Amazon MWAA Serverless requires to call other AWS services
and monitor AWS resources on your behalf. Amazon MWAA Serverless uses this service-linked role in all the AWS Regions where Amazon MWAA Serverless is available.

A service-linked role makes setting up Amazon MWAA Serverless easier because you don't have to manually add the necessary permissions. Amazon MWAA Serverless defines the permissions of
its service-linked role, and unless defined otherwise, only Amazon MWAA Serverless can assume the role. The defined permissions include the trust policy and the permissions policy,
and you can't attach that permissions policy to any other IAM entity.

You can delete the Amazon MWAA Serverless service-linked role only after you disable Amazon MWAA Serverless in all the Regions where it's enabled.
This protects your Amazon MWAA Serverless resources because you can't inadvertently remove permissions to access them.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

###### Topics

- [Service-linked role permissions for Amazon MWAA Serverless](#slr-permissions "#slr-permissions")
- [Creating a service-linked role for Amazon MWAA Serverless](#create-slr "#create-slr")
- [Editing a service-linked role for Amazon MWAA Serverless](#edit-slr "#edit-slr")
- [Deleting a service-linked role for Amazon MWAA Serverless](#delete-slr "#delete-slr")

## Service-linked role permissions for Amazon MWAA Serverless

Amazon MWAA Serverless uses the service-linked role named `AWSServiceRoleForAmazonMWAAServerless`. It's a service-linked role required for
Amazon MWAA Serverless to access your resources. This service-linked role allows Amazon MWAA Serverless Provides access to Amazon MWAA Serverless to manage networking for your workflows and access other
AWS services on your behalf. The `AWSServiceRoleForAmazonMWAAServerless` service-linked role
trusts the `airflow-serverless.amazonaws.com` service to assume the role.

The `AWSServiceRoleForAmazonMWAAServerless` service-linked role uses the managed policy
[AmazonMWAAServerlessServiceRolePolicy](mwaa-serverless-aws-managed-policy.md#aws-managed-policy-AmazonMWAAServerlessServiceRolePolicy "mwaa-serverless-aws-managed-policy.md#aws-managed-policy-AmazonMWAAServerlessServiceRolePolicy").

You must grant permissions to allow the `airflow-serverless.amazonaws.com` service principal to assume `AWSServiceRoleForAmazonMWAAServerless` service-linked role.
Add the following trust policy:

JSON

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "airflow-serverless.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

```

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, refer to [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Amazon MWAA Serverless

You don't need to manually create a service-linked role. When you
create a workflow in the AWS Management Console, the AWS CLI, or the AWS API, Amazon MWAA Serverless creates
the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in
another service that uses the features supported by this role. To learn more, refer to [A
new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you CreateWorkflow,
Amazon MWAA Serverless creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the
**MWAA-S - Networking** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `airflow-serverless.amazonaws.com` service name. For more
information, refer to [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for Amazon MWAA Serverless

Amazon MWAA Serverless does not allow you to edit the AWSServiceRoleForAmazonMWAAServerless service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, refer to [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for Amazon MWAA Serverless

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

When you delete a workflow, Amazon MWAA Serverless deletes all the associated resources it uses as a part of the service. However, you must wait before Amazon MWAA Serverless
completes deleting your workflow, before attempting to delete the service-linked role. If you delete the service-linked role before
Amazon MWAA Serverless deletes the workflow, Amazon MWAA Serverless might be unable to delete all of the workflow's associated resources.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonMWAAServerless service-linked
role. For more information, refer to [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
