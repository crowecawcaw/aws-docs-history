

# Troubleshooting AWS Service Catalog identity and access
<a name="security_iam_troubleshoot"></a>

Use the following information to help you diagnose and fix common issues you might encounter when working with AWS Service Catalog and IAM.

**Topics**
+ [I am not authorized to perform an action in AWS Service Catalog](#troubleshoot-one)
+ [I am not authorized to perform `iam:PassRole`](#troubleshoot-two)
+ [I want to allow people outside of my AWS account to access my AWS Service Catalog resources](#troubleshoot-five)

## I am not authorized to perform an action in AWS Service Catalog
<a name="troubleshoot-one"></a>

If the AWS Management Console tells you that you're not authorized to perform an action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your sign-in credentials. The following example error occurs when the mateojackson user tries to use the console to view details about a fictional my-example-widget resource but does not have the fictional `aws:GetWidget` permissions. 

```
User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: aws:GetWidget on resource: my-example-widget
```

In this case, Mateo asks his administrator to update his policies to allow him to access the `my-example-widget` resource using the `aws:GetWidget` action.

## I am not authorized to perform `iam:PassRole`
<a name="troubleshoot-two"></a>

If you receive an error that you're not authorized to perform the `iam:PassRole` action, then you must contact your administrator for assistance. Your administrator is the person that provided you with your user name and password. Ask that person to update your policies to allow you to pass a role to AWS Service Catalog.

Some AWS services allow you to pass an existing role to that service, instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service.

The following example error occurs when a user named marymajor tries to use the console to perform an action in AWS Service Catalog. However, the action requires the service to have permissions granted by a service role. Mary does not have permissions to pass the role to the service.

```
User: arn:aws:iam::123456789012:user/marymajor is not authorized to perform: iam:PassRole
```

In this case, Mary asks her administrator to update her policies to allow her to perform the iam:PassRole action.

## I want to allow people outside of my AWS account to access my AWS Service Catalog resources
<a name="troubleshoot-five"></a>

You can create a role that users in other accounts or people outside of your organization can use to access your resources. You can specify who is trusted to assume the role. For services that support resource-based policies or access control lists (ACLs), you can use those policies to grant people access to your resources.

To learn more, consult the following:
+ To learn whether AWS Service Catalog supports these features, see [AWS Identity and Access Management in AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/controlling_access.html) in the *AWS Service Catalog Administrator Guide*.
+ To learn how to provide access to your resources across AWS accounts that you own, see [Providing access to an IAM user in another AWS account that you own ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) in the *IAM User Guide*.
+ To learn how to provide access to your resources to third-party AWS accounts, see [Providing access to AWS accounts owned by third parties](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html) in the *IAM User Guide*.
+ To learn how to provide access through identity federation, see [Providing access to externally authenticated users (identity federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html) in the *IAM User Guide*.
+ To learn the difference between using roles and resource-based policies for cross-account access, see [How IAM roles differ from resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html) in the *IAM User Guide*.